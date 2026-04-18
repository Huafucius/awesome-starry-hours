---
name: create-figure-skill
description: Methodology and workflow for distilling a specific public figure into a reusable, callable agent skill. Use this skill whenever the user wants to turn a specific historical or contemporary public figure into a skill artifact — including requests like "做一个鲁迅 skill", "make me a Feynman skill", "distill how Munger thinks into something reusable", "build a [person] perspective", "create a figure skill for X", or any request that names a specific real person and asks to package their mindset, judgment, or voice into a reusable skill folder. Triggers on verbs like create / build / make / distill / generate / 做 / 建 / 生成 combined with a specific named person. Do NOT trigger when the user is merely asking about or discussing a figure without requesting a skill artifact be created ("explain Feynman's method", "tell me about 鲁迅"). Do NOT trigger for books or brands — those will have sister skills.
---

# Create Figure Skill

The user wants to turn a specific public figure into a reusable agent skill. The output is a complete `skills/<figure-slug>/` folder that future agents can invoke through five core modes: dialogue, voice, methodology, critique, advisory.

This is a methodology, not a template filler. Every figure is different; the research must be responsive to the evidence that actually exists for that person.

## Four principles that bind every phase

1. **Research must be saturated.** Do not ration, do not sample. If a source is findable, find it. Agents have a superpower humans lack — parallel retrieval at scale. Use it.
2. **Adversarial is an obligation.** Every strong claim about the figure is checked against its opposition. A skill built only from admiring sources is a whitewash.
3. **Honesty over completeness.** If evidence runs out for a dimension, say so — and record the queries you tried. Do not fabricate plausible content. This is Malcolm's "show the seams".
4. **The model's prior is a corpus.** Before any web access, snapshot what the model already believes about this figure. That snapshot is a source in its own right — the distilled consensus of training data — and must be weighed against external evidence later. It is never deleted or revised.

Before starting, read `references/research-stance.md` and `references/route-planning.md`. The first sets the posture; the second tells you what kind of pass you are running and which deterministic gates still matter.

## Operations within a pass

Routes name the **pass** (`bootstrap` / `update` / `repair` / `extend`). Operations name the **verb**. A single pass usually involves several operations.

- `ingest` — new textual evidence enters `sources/*/raw/`, gets normalized into `cleaned/`, manifest rebuilt.
- `observe` — structured re-encounter with a **non-textual primary** (film, recording, artwork, performance). Produces observation notes against a declared framework; lands in `sources/primary/cleaned/` with `source_type: observation`. The text-primary analogue of `ingest` for visual / auditory / performance figures.
- `query` — the generated skill is used at run time; a mode answers a real prompt. This is the point of the compilation.
- `file-back` — when a query produces a durable synthesis, archive it into `sources/distillations/cleaned/` so the skill accumulates instead of re-deriving.
- `lint` — periodic self-audit of the knowledge layer: orphan claims, stale "no evidence" tags, quote drift, unfilled adversarial gaps. LLM judgment, not script.

Every generated skill keeps two append-only records: `CHANGELOG.md` (one entry per pass) and `research/probe-log.md` (one entry per probe). Both are seeded by `scripts/scaffold.py` and extended by the LLM; `scripts/audit.py` does not grade their content.

See `references/maintenance-operations.md` for when to use each operation and the file-back / lint details.

## The workflow — six phases

Treat this skill as a knowledge compiler for public figures:

`target spec -> evidence corpus -> normalized corpus -> distilled knowledge -> callable interface`

Each phase still produces artifacts for later phases, but this is a harness, not a cage. Use the smallest sufficient pass for the task in front of you. New skills usually run the full flow. Non-bootstrap passes may revisit only the impacted later phases.

### Phase 1 · Route & Target Spec

Decide what kind of compilation this is before doing any research. The first question is not "what should I search?" but "what am I changing?"

Route the task into one of four modes:

- **`bootstrap`** — create a new figure skill from scratch.
- **`update`** — add new evidence to an existing figure skill.
- **`repair`** — fix a weak mode, thin boundary, or incorrect claim.
- **`extend`** — add a new mode, axis, or output behavior beyond the current surface.

Then define the target:

1. Confirm the exact figure. Disambiguate same-name cases.
2. Confirm the target slug and skill path.
3. Draft or revise the generated skill's `description`, including both **triggers** and **anti-triggers**.
4. Identify which axes and modes are in scope for this pass.
5. If this is `bootstrap`, run scaffold to create the empty skeleton:

   ```bash
   python3 skills/create-figure-skill/scripts/scaffold.py --slug <figure-slug>
   ```

**Produces:** for `bootstrap`, `skills/<slug>/` with placeholder files + `meta.json`; for all modes, a clear target definition for what is being created or changed.

### Phase 2 · Prior Capture

Capture the model's starting state before outside evidence starts reshaping it. The prior is not truth; it is a baseline artifact that later lets you see what changed and why.

Do **not** search anything in this phase. For `bootstrap`, write freely into `sources/prior/snapshot.md`: what you already think the figure is known for, the uncertainties, the reputational blur, the places where your memory feels thin or suspiciously smooth.

For `update`, `repair`, and `extend`, read the existing prior snapshot and the current skill first. Note what already exists, what feels load-bearing, and where the weak spots are. Do not overwrite the original prior snapshot; treat it as immutable baseline evidence. If a later pass needs to record how new evidence corrected the prior, append a dated note next to it rather than silently revising history.

**Produces:** `sources/prior/snapshot.md`; for non-bootstrap passes, an explicit understanding of the current skill baseline.

### Phase 3 · Evidence Expansion

Build or expand the evidence corpus needed for this pass. Search deeply, but search in service of the target, not in service of a quota. Stop when the intended delta is well-supported or when the remaining holes are explicit and honest.

Use `references/deepresearch-playbook.md` for query planning, parallel retrieval, gap analysis, and adversarial work. Follow its spirit rigorously: primary and distillation sources carry structural pro-figure bias, so strong claims need critical pressure. But do not perform box-checking research just to satisfy ritual counts.

For `bootstrap`, this phase usually spans primary, critical, and distillation sources broadly. For `update`, `repair`, or `extend`, begin with the delta: gather only the evidence needed to support the changed modes, weak boundaries, disputed claims, or newly requested dimensions. Expand outward only when the delta exposes a deeper gap.

**Produces:** `sources/{primary,critical,distillations}/raw/`, usually plus `sources/research-plan.md` and `sources/gap-report.md`; when needed for contested or load-bearing claims, `sources/claims.md` and `sources/adversarial-findings.md`.

### Phase 4 · Corpus Preparation

Turn heterogeneous raw files into a stable, queryable corpus. This phase is about normalization, provenance, and substrate quality — not summarization and not interpretation.

For each file in `raw/`:

- If PDF, extract to markdown (see `references/source-policy.md` for format handling).
- Strip HTML chrome, ads, navigation, and pagination artifacts.
- Add YAML frontmatter per the schema in `references/source-policy.md`.
- Preserve the full text. `cleaned/` is a fidelity-preserving layer, not a compression layer.

Then rebuild the manifest:

```bash
python3 skills/create-figure-skill/scripts/manifest.py --skill-dir skills/<slug>
```

For non-bootstrap work, only newly added or changed raw files need to be normalized. Do not reprocess the full corpus unless the format policy itself changed.

**Produces:** `sources/*/cleaned/*.md` with consistent frontmatter + `sources/manifest.json`.

### Phase 5 · Knowledge Distillation

Compile the normalized corpus into the durable knowledge layer. This is the layer future agents should read first instead of rediscovering the figure from raw files every time.

Use agent-native parallelism where it helps, but preserve judgment in the main agent. The exact workflow can vary with corpus size; create or refresh summaries only where the changed corpus or changed claims make them useful, then rewrite the affected research files. The default compilation targets are the four axis files defined in `references/four-axes.md`:

- `research/identity.md`
- `research/thinking.md`
- `research/expression.md`
- `research/boundaries.md`

Every strong claim should cite a source file. Every thin area should be labeled honestly. When working incrementally, rewrite only the affected axes unless new evidence forces a broader reconciliation. Then update `research/README.md` so future readers know what changed and how the axes connect.

**Produces:** `sources/*/summaries/*.md` as needed + `research/{identity,thinking,expression,boundaries}.md` + `research/README.md`.

### Phase 6 · Interface Assembly & Probe

Turn the distilled knowledge layer into a callable skill surface, then test whether it actually works. A figure skill is not done when the research is elegant; it is done when the interface stays useful, honest, and bounded under real prompts.

1. Write or revise the five mode files following `references/mode-writing-guide.md`. Each mode should be specific to this figure, not a template fill.
2. Write the generated skill's `SKILL.md` as a slim entry + router. The interface should route to the right mode, not duplicate the research corpus.
3. Run the audit:

   ```bash
   python3 skills/create-figure-skill/scripts/audit.py --skill-dir skills/<slug>
   ```

4. Probe the skill with real prompts. For changed modes, test both a straightforward case and a boundary case. For `update`, `repair`, and `extend`, include at least one regression probe so previously good behavior does not silently drift.

Failures feed back into the modes, the router, and `research/boundaries.md`. That loop is part of the compilation process, not an optional polish pass.

**Produces:** complete, usable `skills/<slug>/`, with revised `modes/*.md`, a generated `SKILL.md`, and probe-informed boundaries.

## Where to read what

| Situation | File to consult |
|---|---|
| Phase 1 Route & Target Spec — choose `bootstrap` / `update` / `repair` / `extend` | `references/route-planning.md` |
| Any pass — operation vocabulary (`ingest` / `observe` / `query` / `file-back` / `lint`) | `references/maintenance-operations.md` |
| Any time — posture and anti-patterns | `references/research-stance.md` |
| Phase 2 Prior Capture — snapshot structure | `references/prior-snapshot-template.md` |
| Phase 3 Evidence Expansion — query planning, parallelism, adversarial pass | `references/deepresearch-playbook.md` |
| Phase 4 Corpus Preparation — frontmatter schema, reliability labels, format handling | `references/source-policy.md` |
| Phase 5 Knowledge Distillation — the four axes and their dimensions | `references/four-axes.md` |
| Phase 5 Knowledge Distillation — summary sweep, axis extraction, reconciliation | `references/deepresearch-playbook.md` |
| Phase 6 Interface Assembly — how to write a mode file | `references/mode-writing-guide.md` |
