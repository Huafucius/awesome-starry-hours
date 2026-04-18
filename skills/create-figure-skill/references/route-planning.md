# Route Planning

This file defines what kind of pass you are running. Read it before any work so the skill does not default to "rebuild everything" out of habit.

## The four routes

### `bootstrap`

Create a new figure skill from scratch.

Use this when no usable skill folder exists yet.

- Run the full flow.
- Create the skeleton with `scripts/scaffold.py`.
- Write the original prior snapshot.
- Build the first evidence corpus, normalized corpus, research layer, and mode layer.
- End with full probes across the intended interface.

### `update`

Add new evidence to an existing figure skill.

Use this when the core figure skill already exists and the main task is to ingest more material, revise claims, or refresh the surface after new sources appear.

- Keep the existing skill as baseline.
- Add only the new raw sources.
- Normalize only changed files.
- Refresh only the impacted research axes and modes unless the new evidence exposes a deeper conflict.
- Include at least one regression probe.

### `repair`

Fix a weak mode, thin boundary, broken claim, or obvious mismatch between the skill and its evidence.

Use this when the skill already exists and the problem is quality, not coverage.

- Start from the existing skill.
- Gather only the evidence needed to repair the broken behavior or claim.
- Rewrite the smallest affected research or mode surface.
- Probe the repaired behavior and a nearby regression case.

### `extend`

Add a new capability beyond the current surface.

Use this when the current skill is solid but incomplete: a new mode, a new axis-adjacent appendix, or broader routing behavior is needed.

- Gather only the evidence needed to support the new capability.
- Reuse the existing corpus and research where possible.
- Extend the interface without duplicating the old one.
- Probe both the new capability and one old capability that must remain stable.

## Artifact discipline

Treat the generated skill as a compiled package. Not all files have the same mutability.

- **Immutable evidence trail**
  - `sources/*/raw/` — never edit in place.
  - `sources/prior/snapshot.md` — keep the original snapshot intact.
- **Append-only by default**
  - Notes explaining how later evidence corrected the prior.
  - Update logs and probe records, if kept.
- **Regenerated on demand**
  - `sources/manifest.json`
  - `research/*.md`
  - `modes/*.md`
  - generated figure `SKILL.md`

## Deterministic choke points

These are the places where scripts help. Keep them narrow.

- `scripts/scaffold.py` — bootstrap only; create the empty skeleton.
- `scripts/manifest.py` — whenever cleaned source metadata changes; rebuild the source index.
- `scripts/audit.py` — before release; verify only binary, script-checkable integrity.

Do not turn the scripts into workflow police. Search depth, writing quality, and judgment remain the LLM's job.

## When to create which artifacts

- **`sources/research-plan.md`** — create when retrieval scope is non-trivial or likely to branch.
- **`sources/gap-report.md`** — create when missing coverage affects confidence or next actions.
- **`sources/claims.md` / `sources/adversarial-findings.md`** — create when new or revised strong claims need explicit counterpressure.
- **`sources/*/summaries/*.md`** — create or refresh when the changed corpus is large enough that direct re-reading would waste context.
- **`research/README.md`** — update whenever the research layer changes in a way that future agents should notice.

## Release expectation by route

- `bootstrap` — full interface probes.
- `update` — targeted probes plus regression.
- `repair` — repaired behavior plus regression.
- `extend` — new capability plus regression.

If the route changes mid-task, say so explicitly and update the working artifacts. Silent route drift creates messy skills.
