#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED_FILES = [
    "SKILL.md",
    "meta.json",
    "references/sources/index.json",
    "references/distilled/core.md",
    "references/distilled/heuristics.md",
    "references/distilled/expression.md",
    "references/distilled/evidence.md",
    "references/distilled/boundaries.md",
]

REQUIRED_META_KEYS = [
    "name",
    "title",
    "figure_name",
    "description",
    "use_cases",
]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Audit a generated figure skill for minimum completeness."
    )
    parser.add_argument("--skill-dir", required=True)
    args = parser.parse_args()

    skill_dir = Path(args.skill_dir)
    missing = [rel for rel in REQUIRED_FILES if not (skill_dir / rel).exists()]

    if missing:
        print("AUDIT FAILED")
        for item in missing:
            print(f"- missing: {item}")
        raise SystemExit(1)

    cleaned_dir = skill_dir / "references" / "sources" / "cleaned"
    research_dir = skill_dir / "references" / "research"
    cleaned_count = len(list(cleaned_dir.glob("*.md")))
    research_count = len(list(research_dir.glob("*.md")))

    if cleaned_count == 0:
        print("AUDIT FAILED")
        print("- no cleaned source files found")
        raise SystemExit(1)

    index_text = (
        (skill_dir / "references" / "sources" / "index.json")
        .read_text(encoding="utf-8")
        .strip()
    )
    if index_text in {"", "[]"}:
        print("AUDIT FAILED")
        print("- source index is empty")
        raise SystemExit(1)

    meta_text = (skill_dir / "meta.json").read_text(encoding="utf-8")
    import json

    meta = json.loads(meta_text)
    missing_meta = [key for key in REQUIRED_META_KEYS if not meta.get(key)]
    if missing_meta:
        print("AUDIT FAILED")
        for key in missing_meta:
            print(f"- missing meta key: {key}")
        raise SystemExit(1)

    distilled_files = [
        skill_dir / "references" / "distilled" / "core.md",
        skill_dir / "references" / "distilled" / "heuristics.md",
        skill_dir / "references" / "distilled" / "expression.md",
        skill_dir / "references" / "distilled" / "evidence.md",
        skill_dir / "references" / "distilled" / "boundaries.md",
    ]
    empty_distilled = [
        path.name
        for path in distilled_files
        if not path.read_text(encoding="utf-8").strip()
    ]
    if empty_distilled:
        print("AUDIT FAILED")
        for name in empty_distilled:
            print(f"- empty distilled file: {name}")
        raise SystemExit(1)

    skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    if not skill_text.startswith("---\n"):
        print("AUDIT FAILED")
        print("- SKILL.md is missing frontmatter")
        raise SystemExit(1)

    print("AUDIT PASSED")
    print(f"- cleaned sources: {cleaned_count}")
    print(f"- research files: {research_count}")


if __name__ == "__main__":
    main()
