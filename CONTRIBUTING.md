# 贡献指南 / Contributing Guide

## 添加索引 / Add to Index

发现了好的 personalized skill 仓库？直接编辑 `README.md`，将其添加到对应分类表格，提交 PR。

*Found a great personalized skill repo? Edit `README.md`, add it to the right category table, and submit a PR.*

**要求 / Requirements:**
- 仓库必须真实存在、可访问
- 必须对应到**一个或多个具体人物**、**一本具体的书**或**一个具体品牌**
- 描述应说清楚该 skill 蒸馏了什么

## 贡献仓库内 Skill / Contribute In-Repo Skills

仓库内的原创 skill 现在采用**文件夹结构**，而不是单个 `.md` 文件。

```
skills/
├── create-figure-skill/
│   ├── SKILL.md
│   ├── references/
│   └── scripts/
└── ...
```

**推荐结构 / Recommended structure:**

```text
your-skill/
├── SKILL.md
├── references/
│   ├── sources/
│   ├── research/
│   └── distilled/
└── scripts/
```

**最低要求 / Minimum requirements:**
- 必须有 `SKILL.md`
- 如果 skill 基于公开资料蒸馏，请尽量保留 `references/`
- 如果有确定性工作流（采集、清洗、装配、检查），放进 `scripts/`

**特别说明 / Note:**
- `create-figure-skill` 这类“做 skill 的 skill”也是允许的
- 当前工厂只做人物 skill，书籍和品牌以后再说

## 原则 / Principles

**蒸馏 > 模仿**：提取思维框架，而非模仿说话方式。

**实用 > 炫技**：面对真实问题要能产出可操作的拆解。

**诚实 > 万能**：明确说明局限性，不夸大适用范围。
