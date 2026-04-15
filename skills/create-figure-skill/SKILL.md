---
name: create-figure-skill
description: A DeepSearch-driven workflow skill to distill any public figure into a callable Claude skill. Use this to orchestrate parallel search, data cleaning, structural research, and skill assembly.
---

# Create Figure Skill

This is a **DeepSearch-driven workflow skill**. It is designed to turn a public figure into a self-contained, reusable skill folder. 

**This is an agent-led workflow.** You (the agent) are expected to aggressively search, evaluate sources, read materials, and write deep research. The provided Python scripts are merely mechanical helpers for scaffolding and assembly. Do not wait for the user to hand you a dataset. You must build the dataset yourself.

## Core Principle

Distill how the figure thinks, judges, acts, and speaks.
Do not reduce the figure to quotes, biography trivia, or cosplay.

## Workflow

### Phase 0: Intent Alignment
Confirm with the user:
- The exact figure name.
- Any disambiguation (e.g., which person if they share a name).
- The output slug (e.g., `feynman-perspective`).
- The intended use case: advisor, critic, writing lens, decision lens, etc.

### Phase 1: Create Scaffold
Run the mechanical helper to create the empty directory structure:
```bash
python3 skills/create-figure-skill/scripts/create_scaffold.py --name "Figure Name" --slug figure-slug --output-dir skills
```
This creates `meta.json` and empty `references/` folders. Review and refine `meta.json` if needed.

### Phase 2: DeepSearch
**This is the core collection phase.**
- Use your tools (WebSearch, WebFetch, bash, etc.) or dispatch parallel subagents (e.g., `Explore`) to search for public sources across multiple lanes: biography, primary texts, interviews, videos, speeches, and external criticism.
- The goal is to collect **Evidence Bundles**.
- Download actual files (HTML, markdown, PDFs, transcripts) into `references/sources/raw/`. 
- If you find audio/video (mp3/mp4) that is critical but lacks a transcript, ask the user for help or use tools to extract text if available. Do not hoard media files without text.

### Phase 3: Data Cleaning
Convert the heterogeneous files from Phase 2 into clean markdown text in `references/sources/cleaned/`.
- Format each file with YAML frontmatter:
```md
---
title: Example Source
source_url: https://example.com
source_type: interview
language: zh-CN
reliability: high
retrieved_at: 2026-04-09
---
```
- Ensure the text is clean, readable, and free of noisy HTML/ad boilerplate.

### Phase 4: Source Governance
Review all cleaned sources.
- Deduplicate identical texts.
- Classify into primary vs. secondary sources.
- Run the script to generate the source manifest, which acts as the bibliography for future agents:
```bash
python3 skills/create-figure-skill/scripts/build_source_manifest.py --skill-dir skills/figure-slug
```
*Note: This is just a catalog generation step, not a retrieval database.*

### Phase 5: DeepResearch
Read the `cleaned/` sources and write comprehensive research documents in `references/research/`.
- Follow the 10-dimension ontology (Identity, Worldview, Mental Models, Decision Heuristics, Actions/Works, Expression DNA, Relational Patterns, Stress/Conflict, Evolution, Boundaries).
- The 4 mandatory dimensions are: `mental-models`, `decision-heuristics`, `actions-works`, and `boundaries-unknowns`.
- These files must be thick, detailed, and directly cite the sources. Do not write thin, 5-bullet outlines.

### Phase 6: Distill
Compress the heavy research into runtime-ready files in `references/distilled/`.
- `core.md`: What this figure skill is for and its core posture.
- `heuristics.md`: Reusable judgment rules.
- `expression.md`: Tone and rhetorical habits.
- `evidence.md`: Strongest source anchors.
- `boundaries.md`: Limitations and unknowns.
These files must be extremely dense, actionable, and ready to guide an agent during runtime.

### Phase 7: Assemble Final SKILL.md
Run the assembly script:
```bash
python3 skills/create-figure-skill/scripts/assemble_skill.py --skill-dir skills/figure-slug
```
This mechanically combines `meta.json` and the distilled files into the final `SKILL.md`.

### Phase 8: Audit and Smoke Test
Run the audit script to check for structural completeness:
```bash
python3 skills/create-figure-skill/scripts/audit_skill.py --skill-dir skills/figure-slug
```
Finally, perform a "smoke test": act as the newly created skill and attempt to answer a representative question to ensure the rules, tone, and boundaries work properly.

## Files To Read
- `references/figure-schema.md` for the 10-dimension ontology
- `references/source-policy.md` for source selection rules
- `references/templates/research-template.md` for research-file shape
- `references/templates/distilled-template.md` for distilled-file shape
- `references/templates/figure-skill-template.md` for final `SKILL.md` expectations
