#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
from pathlib import Path


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text

    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return {}, text

    raw_meta = parts[0].splitlines()[1:]
    body = parts[1]
    meta: dict[str, str] = {}
    for line in raw_meta:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip()
    return meta, body


def summarize_body(body: str, limit: int = 180) -> str:
    compact = " ".join(line.strip() for line in body.splitlines() if line.strip())
    return compact[:limit] + ("..." if len(compact) > limit else "")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build a source index for a generated figure skill."
    )
    parser.add_argument("--skill-dir", required=True)
    args = parser.parse_args()

    skill_dir = Path(args.skill_dir)
    cleaned_dir = skill_dir / "references" / "sources" / "cleaned"
    index_path = skill_dir / "references" / "sources" / "index.json"

    entries = []
    for path in sorted(cleaned_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
        entries.append(
            {
                "file": str(path.relative_to(skill_dir)).replace("\\", "/"),
                "title": meta.get("title", path.stem),
                "source_url": meta.get("source_url", ""),
                "source_type": meta.get("source_type", "unknown"),
                "language": meta.get("language", "unknown"),
                "reliability": meta.get("reliability", "unknown"),
                "retrieved_at": meta.get("retrieved_at", ""),
                "summary": summarize_body(body),
            }
        )

    index_path.write_text(
        json.dumps(entries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(index_path)


if __name__ == "__main__":
    main()
