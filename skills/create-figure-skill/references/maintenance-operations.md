# Maintenance Operations

A figure skill is a compiled product. After the first bootstrap, it keeps being touched — new evidence arrives, modes drift, claims need rechecking. This file defines the four operations that live **inside** routes and tell an agent what kind of move it is actually making.

Read this during `update`, `repair`, or `extend` passes. `bootstrap` implicitly uses `ingest` + `file-back` at the end, but a pure bootstrap agent can usually ignore this file.

## The four operations

Operations describe the **verb**; routes describe the **pass**. A single route may involve several operations.

### `ingest`

New evidence enters the corpus. Raw files land in `sources/*/raw/`, get normalized into `sources/*/cleaned/` per `source-policy.md`, and the manifest is rebuilt via `scripts/manifest.py`.

Ingest is the only operation that produces new `cleaned/` entries from outside material. Every `bootstrap` pass ends with a large ingest. `update` passes are dominated by it.

### `query`

The generated figure skill is used at run time — a mode fires, reads `research/` and the relevant `cleaned/` sources, and returns an answer. This is the run-time face of compilation.

Query is not a build-time operation; it is the reason the build exists. Named here so that `file-back` has a referent.

### `file-back`

When a query produces a durable synthesis — a comparison, a timeline, an argument reconstruction that did not exist in the source corpus before — archive it to `sources/distillations/cleaned/` as a new source.

Rules:

- `source_type: distillation` in frontmatter.
- `author:` is `"<figure-slug> self-query"` (e.g., `"lu-xun-skill self-query"`).
- `source_url:` records the prompt that produced the synthesis, prefixed `internal://query/<date>/<short-slug>`.
- Run `scripts/manifest.py` after filing.
- Do **not** file back routine Q&A. Only synthesis with reuse value.
- Dedup by content: if a near-identical synthesis already sits in `distillations/cleaned/`, append to it rather than creating a near-duplicate.

File-back is how the skill accumulates — the Karpathy point. Without it, every complex query restarts from primary sources.

### `observe`

Structured re-encounter with a **non-textual primary** — watching a film, listening to a recording, examining a painting, attending a performance. The operation exists because `cleaned/` is a textual substrate and a filmmaker, composer, or dancer cannot be ingested as text without lossy projection.

The artifact of `observe` is a markdown note of observations made against an explicit framework (usually the Axis 3 scope-note grid: unit size × channel). It is **primary-grade evidence about the work** but it is not the work.

Rules:

- `source_type: observation` in frontmatter.
- `author:` is the observer — the agent's session id or the human's name, **not** the figure's name.
- `source_url:` is a citation URI of the artifact observed (`film://rashomon-1950`, `recording://kurosawa-editing-interview-1980`). If the artifact has a canonical web location or archive entry, use that.
- `note:` must state which channels the observations cover (image / movement / sound / performance / duration) and which channels the notes necessarily lose.
- Store in `sources/primary/cleaned/`. A `raw/` counterpart should still exist — see `source-policy.md` on raw counterparts — typically a pointer file recording the artifact identifier and retrieval context, since the primary is not itself textual.
- Re-observing the same artifact from a new angle produces a new file with a dated suffix; do not overwrite the previous observation.

Plan `observe` early whenever the figure's primary output is non-textual and a text projection (screenplay, transcript, artist statement) would lose load-bearing channels. For filmmakers, painters, dancers, composers, and most performers, `observe` is usually in scope from Phase 3 onward.

### `lint`

Periodic self-audit of the knowledge layer. Unlike `audit.py` (structural only), `lint` is LLM judgment on knowledge health.

Checklist:

- **Orphan claims.** Citations in `research/*.md` pointing to files no longer in `manifest.json`.
- **Stale "no evidence found".** Gaps logged with queries tried more than one pass ago; retry the queries.
- **Quote drift.** Verbatim quotes in `research/` whose source `cleaned/` file has changed since the quote was lifted.
- **Unfilled adversarial gaps.** Strong claims in `research/thinking.md` with no entry in `sources/adversarial-findings.md`.
- **Mode-research drift.** A `modes/*.md` pointing to a research section that has been rewritten away.
- **Probe regressions.** Probes in `research/probe-log.md` marked `fail` and not addressed in subsequent passes.

A `lint` pass writes findings into `gap-report.md` (expanding it if needed) and into `CHANGELOG.md`. It does not silently edit `research/` — fixes are separate `repair` work.

## Operations × routes

| Route | Typical operations |
|---|---|
| `bootstrap` | heavy `ingest` → distillation (file-back at the end for synthesis). `observe` replaces ingest for non-textual primaries. |
| `update` | `ingest` or `observe` + targeted `lint` on the changed surface |
| `repair` | `lint` to surface the problem + localized re-distillation |
| `extend` | narrow `ingest` / `observe` for the new capability + `lint` for regressions elsewhere |

## Artifact contract for operations

Two append-only files in the generated skill record what operations ran:

- `CHANGELOG.md` — one entry per pass. Date, route, operations, touched axes/modes, notable evidence delta. Agents append; they do not rewrite earlier entries.
- `research/probe-log.md` — one entry per probe. Date, mode, prompt, outcome (`pass` / `fail` / `surprise`), boundary update if any.

Both files are seeded as empty-of-entries stubs by `scripts/scaffold.py` — header and format instructions only, no pre-written bootstrap entry. The first real entry is written by the agent completing the first substantive pass. Scaffold creating the skeleton is not itself a pass worth logging; logging it would commit a forward-looking claim about operations that have not yet happened.

Neither file is checked by `audit.py` — their quality is the LLM's responsibility, not a binary gate.
