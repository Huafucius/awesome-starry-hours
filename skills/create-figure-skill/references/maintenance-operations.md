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
| `bootstrap` | heavy `ingest` → distillation (file-back at the end for synthesis) |
| `update` | `ingest` + targeted `lint` on the changed surface |
| `repair` | `lint` to surface the problem + localized re-distillation |
| `extend` | narrow `ingest` for the new capability + `lint` for regressions elsewhere |

## Artifact contract for operations

Two append-only files in the generated skill record what operations ran:

- `CHANGELOG.md` — one entry per pass. Date, route, operations, touched axes/modes, notable evidence delta. Agents append; they do not rewrite earlier entries.
- `research/probe-log.md` — one entry per probe. Date, mode, prompt, outcome (`pass` / `fail` / `surprise`), boundary update if any.

Both files are generated as stubs by `scripts/scaffold.py`. They are not checked by `audit.py` — their quality is the LLM's responsibility, not a binary gate.
