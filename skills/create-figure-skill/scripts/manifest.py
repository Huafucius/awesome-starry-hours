#!/usr/bin/env python3
"""Regenerate sources/manifest.json from cleaned source frontmatter.

Usage:
    python3 manifest.py --skill-dir skills/<figure-slug>

Scans sources/*/cleaned/*.md, reads frontmatter, writes manifest.json.
Pure metadata aggregation — no content interpretation.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REQUIRED_FIELDS = [
    "title",
    "source_url",
    "source_type",
    "language",
    "reliability",
    "retrieved_at",
    "author",
]


def parse_frontmatter(text: str) -> dict[str, str]:
    """Minimal frontmatter extractor for the cleaned-source contract."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing YAML frontmatter")

    meta: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            missing = [field for field in REQUIRED_FIELDS if not meta.get(field)]
            if missing:
                raise ValueError(f"missing required frontmatter fields: {', '.join(missing)}")
            return meta
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        meta[key.strip()] = value.strip().strip('"').strip("'")
    raise ValueError("frontmatter never closed")


def main() -> None:
    parser = argparse.ArgumentParser(description="Rebuild sources/manifest.json.")
    parser.add_argument("--skill-dir", required=True, help="Path to generated skill directory.")
    args = parser.parse_args()

    skill_dir = Path(args.skill_dir).resolve()
    sources_dir = skill_dir / "sources"
    if not sources_dir.is_dir():
        print(f"Error: {sources_dir} not found.", file=sys.stderr)
        sys.exit(1)

    entries: list[dict] = []
    for cleaned_file in sorted(sources_dir.glob("*/cleaned/*.md")):
        relative = cleaned_file.relative_to(sources_dir)
        category = cleaned_file.parts[-3]
        text = cleaned_file.read_text()
        try:
            meta = parse_frontmatter(text)
        except ValueError as exc:
            print(f"Error in {relative}: {exc}", file=sys.stderr)
            sys.exit(1)
        entries.append(
            {
                "path": str(relative),
                "category": category,
                "title": meta["title"],
                "source_url": meta["source_url"],
                "source_type": meta["source_type"],
                "language": meta["language"],
                "reliability": meta["reliability"],
                "retrieved_at": meta["retrieved_at"],
                "author": meta["author"],
            }
        )

    manifest = {"count": len(entries), "sources": entries}
    manifest_path = sources_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(f"Wrote {manifest_path} with {len(entries)} entries.")


if __name__ == "__main__":
    main()
