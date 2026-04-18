# Figure Skill Maintenance Layer

**Goal:** Close three targeted gaps in the v2 `create-figure-skill` so generated figure skills become **self-maintainable compilation products** — not just one-shot outputs.

**Scope:** Additive only. Touch `scripts/scaffold.py`, `SKILL.md`, and add one new reference file. Do not change the four routes, the four axes, source policy, or the existing logic of `audit.py` / `manifest.py`.

**Why:** v2 already supports incremental routes (`update` / `repair` / `extend`), but the generated skill itself carries no memory of what has been done to it. Three concrete symptoms:

1. No durable changelog. After multiple passes, a future agent cannot see what was touched and why. `route-planning.md` mentions "update logs, if kept" but no file exists.
2. Probe results are ephemeral. Phase 6 says "failures feed back into `boundaries.md`" but the probe itself is not recorded, so regression probing in later passes has nothing to compare against.
3. `File Back` and `Lint` are absent as operations. Karpathy's wiki model treats archiving valuable query outputs and periodic self-audit as first-class verbs; v2's routes cover bootstrap / new evidence but not these day-2 operations.

**Success criteria:**

- `scripts/scaffold.py --slug <s>` produces two new non-empty stubs: `<slug>/CHANGELOG.md` and `<slug>/research/probe-log.md`, each with clear instructional content about when and how to append.
- `skills/create-figure-skill/SKILL.md` gains an "Operations within a pass" section introducing `ingest` / `query` / `file-back` / `lint` as vocabulary, with a pointer to the new reference. The section is under ~25 lines; it does not duplicate route content.
- A new `references/maintenance-operations.md` (target 50–80 lines) specifies: when to use each operation, File Back destination and dedup rule, Lint checklist items, and the relationship between operations and routes.
- `audit.py` is NOT extended to check CHANGELOG / probe-log contents (LLM judgment, not script).
- `scaffold.py` remains structural; no content generation beyond the stubs.
- Running the audit on a freshly scaffolded skill still passes.
- No existing file's core logic is refactored; only additive edits.

---

## Docs Impact

| File | Action | What changes |
|------|--------|-------------|
| `docs/README.md` | Update | Add a plan entry for this maintenance-layer change |
| `docs/plans/2026-04-18-figure-skill-maintenance-layer.md` | Create | This plan |
| `skills/create-figure-skill/scripts/scaffold.py` | Update | Add CHANGELOG.md and research/probe-log.md stubs to the skeleton |
| `skills/create-figure-skill/SKILL.md` | Update | Add a short "Operations within a pass" section pointing to the new reference |
| `skills/create-figure-skill/references/maintenance-operations.md` | Create | New reference — defines ingest / query / file-back / lint and their artifact discipline |
| `skills/create-figure-skill/references/route-planning.md` | Update | Tighten the artifact-mutability section: name CHANGELOG.md and probe-log.md as append-only; remove the speculative "if kept" hedge |

---

## Task Breakdown

### T1 · Write the new reference

Create `skills/create-figure-skill/references/maintenance-operations.md`. Content outline:

- Opening paragraph: operations sit *inside* routes, not next to them. A `bootstrap` pass may include all four operations; a `repair` pass may only use `lint` + `file-back`.
- `ingest`: how new raw sources enter the corpus; pointer to `source-policy.md`.
- `query`: the run-time use of the generated skill — a reminder that modes ARE query. This is the runtime face of compilation.
- `file-back`: when a query produces a durable synthesis, archive it to `sources/distillations/cleaned/` with `source_type: distillation` and `author: "<figure-slug> self-query"`. Dedup by content; do not archive every answer.
- `lint`: periodic self-audit checklist — orphan claims (cited in `research/` but no longer in manifest), stale "no evidence found" tags (queries that should be retried), quote drift (verbatim quotes in `research/` whose source file changed), unfilled adversarial gaps.
- CHANGELOG and probe-log artifact conventions.

### T2 · Extend `scaffold.py`

Add two stub files to the skeleton:

- `<slug>/CHANGELOG.md` — append-only log; first entry is the bootstrap date.
- `<slug>/research/probe-log.md` — append-only probe archive; stub explains entry format (date, mode, prompt, outcome, boundary update).

Stubs must be non-empty (have instructional content for the human/LLM who will append later). No other scaffold changes.

### T3 · Update `SKILL.md`

Add a new section after "Four principles", before "The workflow — six phases":

- Title: "Operations within a pass"
- ≤25 lines of prose
- Names the four operations, says they live inside routes, points to `references/maintenance-operations.md` for detail.

### T4 · Tighten `route-planning.md`

In the "Artifact discipline" section:

- Move `CHANGELOG.md` and `research/probe-log.md` from the vague "update logs, if kept" language into the explicit **Append-only** category.
- Remove the "if kept" hedge.

### T5 · Update `docs/README.md`

Add one row to the Plans table linking this plan.

### T6 · Verification

- Run `scripts/scaffold.py --slug throwaway-test --output-dir /tmp` — confirm both new stubs exist, are non-empty, and the existing skeleton still matches audit expectations.
- Run `scripts/audit.py --skill-dir /tmp/throwaway-test` — must still pass (new files are ignored by audit, which is the design).
- `git diff --name-only` must match the Docs Impact table exactly.
- Clean up `/tmp/throwaway-test`.

---

## Out of Scope

- Modifying `audit.py` or `manifest.py` core logic.
- Changing the four-route vocabulary, the four axes, or source-policy frontmatter.
- Touching `lu-xun-skill/` (lives outside origin/main; separate concern).
- Introducing `index.md`, `state.json`, or other maintenance-layer artifacts beyond the two stubs.
- Any backward-compatibility consideration — per project directive.
