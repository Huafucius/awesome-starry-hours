#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
from pathlib import Path


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def preview(text: str, lines: int = 10) -> str:
    stripped = []
    for line in text.splitlines():
        if not line.strip():
            continue
        if line.lstrip().startswith("#"):
            continue
        stripped.append(line)
    kept = stripped[:lines]
    return "\n".join(kept)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Assemble the final SKILL.md for a generated figure skill."
    )
    parser.add_argument("--skill-dir", required=True)
    args = parser.parse_args()

    skill_dir = Path(args.skill_dir)
    meta_path = skill_dir / "meta.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8"))

    core = read_text(skill_dir / "references" / "distilled" / "core.md")
    heuristics = read_text(skill_dir / "references" / "distilled" / "heuristics.md")
    expression = read_text(skill_dir / "references" / "distilled" / "expression.md")
    evidence = read_text(skill_dir / "references" / "distilled" / "evidence.md")
    boundaries = read_text(skill_dir / "references" / "distilled" / "boundaries.md")

    purpose = meta.get(
        "purpose",
        f"借助 {meta['figure_name']} 的公开思维框架来分析问题，而不是做空泛模仿。",
    )

    content = f"""---
name: {meta["name"]}
description: {meta["description"]}
---

# {meta["title"]}

{purpose} 尤其适合 {meta["use_cases"]}。

不要把这个 skill 当成语录机，也不要把它降级成松散的历史 roleplay。

## 读取顺序

1. 先读 `references/distilled/core.md`。
2. 遇到判断、批评、问题拆解任务时，读 `references/distilled/heuristics.md`。
3. 遇到改写、评论、论辩或措辞任务时，读 `references/distilled/expression.md`。
4. 涉及文本出处、生平事实或思想依据时，先看 `references/distilled/evidence.md`，再回到 `references/sources/manifest.json`。
5. 如果证据不足，或问题超出了人物覆盖范围，严格遵守 `references/distilled/boundaries.md`。

## 核心姿态

{preview(core, 12)}

## 判断启发式

{preview(heuristics, 14)}

## 表达 DNA

{preview(expression, 12)}

## 证据纪律

{preview(evidence, 12)}

## 边界

{preview(boundaries, 12)}

## 运行规则

- 优先做诊断，而不是廉价安慰。
- 优先做结构性批评，而不是重复口号。
- 当来源记录存在张力时，保留矛盾，不要强行抹平。
- 严格区分源文本支持的观察与后续推断。
- 如果请求依赖当代事实，而这些事实不在归档来源中，要先说明覆盖不足，再决定是否扩展回答。
"""

    (skill_dir / "SKILL.md").write_text(content, encoding="utf-8")
    print(skill_dir / "SKILL.md")


if __name__ == "__main__":
    main()
