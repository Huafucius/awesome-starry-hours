#!/usr/bin/env python3
"""Structural audit for a generated figure skill.

Checks structural integrity only — the critical, binary gates that a script
can verify without judgment:
  1. Do all required files and directories exist?
  2. Does SKILL.md have name + description in frontmatter? (needed for triggering)
  3. Is manifest.json valid JSON with at least one source?

Content quality, research depth, mode coverage — those are the LLM's job,
enforced through the smoke test in Phase 6, not through this script.

Usage:
    python3 audit.py --skill-dir skills/<figure-slug>

Exit code 0 on pass, 1 on any issue.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REQUIRED_MODES = ["dialogue", "voice", "methodology", "critique", "advisory"]
REQUIRED_AXES = ["identity", "thinking", "expression", "boundaries"]
REQUIRED_STRUCTURED_CATEGORIES = ["primary", "critical", "distillations"]
REQUIRED_MANIFEST_FIELDS = [
    "path",
    "category",
    "title",
    "source_url",
    "source_type",
    "language",
    "reliability",
    "retrieved_at",
    "author",
]


def check_frontmatter_fields(path: Path, required: list[str]) -> list[str]:
    text = path.read_text()
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return [f"{path.name}: missing YAML frontmatter"]
    values: dict[str, str] = {}
    closed = False
    for line in lines[1:]:
        if line.strip() == "---":
            closed = True
            break
        if ":" in line:
            key, _, value = line.partition(":")
            values[key.strip()] = value.strip().strip('"').strip("'")
    if not closed:
        return [f"{path.name}: frontmatter never closed"]
    issues = [f"{path.name}: frontmatter missing field '{k}'" for k in required if k not in values]
    issues.extend(
        f"{path.name}: frontmatter field '{k}' is blank" for k in required if k in values and not values[k]
    )
    return issues


def audit(skill_dir: Path) -> list[str]:
    issues: list[str] = []

    # Top-level files
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        issues.append("SKILL.md missing")
    else:
        issues.extend(check_frontmatter_fields(skill_md, ["name", "description"]))

    if not (skill_dir / "meta.json").is_file():
        issues.append("meta.json missing")

    # modes/ — files must exist; content quality is the LLM's call
    modes_dir = skill_dir / "modes"
    if not modes_dir.is_dir():
        issues.append("modes/ missing")
    else:
        for mode in REQUIRED_MODES:
            if not (modes_dir / f"{mode}.md").is_file():
                issues.append(f"modes/{mode}.md missing")

    # research/ — files must exist; depth is the LLM's call
    research_dir = skill_dir / "research"
    if not research_dir.is_dir():
        issues.append("research/ missing")
    else:
        for axis in REQUIRED_AXES:
            if not (research_dir / f"{axis}.md").is_file():
                issues.append(f"research/{axis}.md missing")
        if not (research_dir / "README.md").is_file():
            issues.append("research/README.md missing")

    # sources/
    sources_dir = skill_dir / "sources"
    if not sources_dir.is_dir():
        issues.append("sources/ missing")
    else:
        manifest = sources_dir / "manifest.json"
        if not manifest.is_file():
            issues.append("sources/manifest.json missing")
        else:
            try:
                data = json.loads(manifest.read_text())
                sources = data.get("sources")
                if not sources:
                    issues.append("sources/manifest.json has no entries (run manifest.py after Corpus Preparation)")
                if data.get("count") != len(sources or []):
                    issues.append("sources/manifest.json count does not match source entries")
                for index, entry in enumerate(sources or []):
                    for field in REQUIRED_MANIFEST_FIELDS:
                        if not entry.get(field):
                            issues.append(
                                f"sources/manifest.json entry {index} missing field '{field}'"
                            )
                    entry_path = entry.get("path")
                    if entry_path and not (sources_dir / entry_path).is_file():
                        issues.append(
                            f"sources/manifest.json entry {index} points to missing file '{entry_path}'"
                        )
            except json.JSONDecodeError as e:
                issues.append(f"sources/manifest.json is not valid JSON: {e}")

        for category in REQUIRED_STRUCTURED_CATEGORIES:
            for sub in ["raw", "cleaned", "summaries"]:
                if not (sources_dir / category / sub).is_dir():
                    issues.append(f"sources/{category}/{sub}/ missing")

        prior_dir = sources_dir / "prior"
        if not prior_dir.is_dir():
            issues.append("sources/prior/ missing")
        elif not (prior_dir / "snapshot.md").is_file():
            issues.append("sources/prior/snapshot.md missing")

    return issues


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit a generated figure skill's skeleton.")
    parser.add_argument("--skill-dir", required=True, help="Path to the generated skill.")
    args = parser.parse_args()

    skill_dir = Path(args.skill_dir).resolve()
    if not skill_dir.is_dir():
        print(f"Error: {skill_dir} not found.", file=sys.stderr)
        sys.exit(1)

    issues = audit(skill_dir)
    if not issues:
        print(f"OK · {skill_dir} passes skeleton audit.")
        sys.exit(0)

    print(f"FAIL · {skill_dir} has {len(issues)} issue(s):")
    for issue in issues:
        print(f"  - {issue}")
    sys.exit(1)


if __name__ == "__main__":
    main()
