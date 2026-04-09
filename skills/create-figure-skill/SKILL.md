---
name: create-figure-skill
description: Create a self-contained public-information figure skill from source texts, research notes, and distilled markdown. Use this whenever the user wants to turn a real person into a reusable Claude skill, especially for thinkers, founders, writers, creators, or historical figures.
---

# Create Figure Skill

Build a new figure skill from public sources.

This is a factory skill. Its output is another skill folder, not just a report.

## Outcome

Produce a self-contained figure skill with:

- `SKILL.md`
- `references/sources/`
- `references/research/`
- `references/distilled/`
- optional `scripts/`

## Core Principle

Distill how the figure thinks, judges, acts, and speaks.

Do not reduce the figure to quotes, biography trivia, or cosplay.

## Figure Schema

Use this 10-dimension ontology when source coverage allows:

1. identity and biography
2. worldview and values
3. mental models
4. decision heuristics
5. actions and works
6. expression DNA
7. relational patterns
8. stress and conflict
9. evolution and contradictions
10. boundaries and unknowns

The following 4 are mandatory even in a lightweight build:

- mental models
- decision heuristics
- actions and works
- boundaries and unknowns

## Source Rules

- Prefer first-hand material: books, essays, speeches, interviews, transcripts, letters, official archives.
- Use second-hand material only to add biography, criticism, or contradiction context.
- Keep the skill self-contained by storing cleaned source texts inside the generated skill folder.
- Preserve uncertainty. If evidence is thin, say so.

## Workflow

### Phase 0: Define target

Confirm:

- exact figure name
- output slug
- intended use: advisor, critic, writing lens, decision lens, etc.

### Phase 1: Create scaffold

Run:

```bash
python3 skills/create-figure-skill/scripts/create_scaffold.py --name "Figure Name" --slug figure-slug --output-dir skills
```

This creates the empty skill folder.

It also creates a starter `meta.json`. Before assembly, make sure the fields still match the figure and intended use case.

### Phase 2: Gather sources

Collect public texts into:

- `references/sources/raw/` when raw downloads are useful
- `references/sources/cleaned/` for normalized markdown that the model can read directly

Each cleaned source file should begin with frontmatter like:

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

Then build the source manifest:

This is not a search index and not a retrieval system. It is a compact source catalog that tells future agents what cleaned source files exist, where they came from, and which ones are worth reading first.

```bash
python3 skills/create-figure-skill/scripts/build_source_manifest.py --skill-dir skills/figure-slug
```

### Phase 3: Research the figure

Write the 10 research files under `references/research/`.

Do not pad missing dimensions with fluff. Mark thin evidence clearly.

If the scaffolded `meta.json` is still generic, refine it here before moving on.

### Phase 4: Distill for runtime use

Write the distilled files:

- `core.md`
- `heuristics.md`
- `expression.md`
- `evidence.md`
- `boundaries.md`

These files should be concise, actionable, and source-aware.

### Phase 5: Assemble the final skill

Run:

```bash
python3 skills/create-figure-skill/scripts/assemble_skill.py --skill-dir skills/figure-slug
```

This generates the figure skill's `SKILL.md` from the distilled files.

### Phase 6: Audit

Run:

```bash
python3 skills/create-figure-skill/scripts/audit_skill.py --skill-dir skills/figure-slug
```

The audit must pass before treating the result as complete.

## Writing Guidance

- Put biography in service of cognition, not the other way around.
- Separate evidence from inference.
- Preserve contradictions.
- Put "when to use" and "when not to use" near the top of the final skill.
- Keep the final skill thin. Put heavy material in references.

## Anti-Patterns

- quote dump
- pure roleplay
- generic motivational persona
- unsupported certainty
- biography-heavy, judgment-light skills

## Files To Read

- `references/figure-schema.md` for the 10-dimension ontology
- `references/source-policy.md` for source selection rules
- `references/templates/research-template.md` for research-file shape
- `references/templates/distilled-template.md` for distilled-file shape
- `references/templates/figure-skill-template.md` for final `SKILL.md` expectations
