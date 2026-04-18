# Iteration-2 Amendments from Multi-Figure Eval

**Goal:** Apply five targeted amendments to `create-figure-skill` based on convergent findings from a 4-figure eval round (Marie Curie, Friedrich Nietzsche, 庄子 / Zhuangzi, 黒澤明 / Akira Kurosawa). The amendments are additive / adjustive, not structural. Four routes, four axes, five modes all preserved.

**Why:** Round-1 eval only covered two contemporary English-language journalists. Round 2 stressed the skill across eras (ancient → contemporary), languages (English, German, classical Chinese, Japanese), media (text / aphorism / film / bench science), and reception profiles (canonical / weaponized / composite-author / collaborative). Four subagent bootstrap passes produced detailed critique. Eight complaints surfaced; five have multi-figure support and are addressed here. Three are noted for later deliberation and not patched now.

**Findings (summarized from `/tmp/cfs-eval-r2/*/report.md`):**

| # | Finding | Raised by | Addressed in this patch? |
|---|---|---|---|
| 1 | Voice axis (字/词/句/段/章) assumes continuous prose | all 4 | **YES** — scope note + alternative axes for aphorism / visual / parable |
| 2 | Prior snapshot has no template; each agent invents one | Curie (explicit); others implicit | **YES** — new `references/prior-snapshot-template.md` |
| 3 | "Adversarial pass" collapses three epistemic problems (textual-critical, interpretive, reception-historical) | Nietzsche, Zhuangzi | **YES** — distinguish in `research-stance.md` |
| 4 | Boundaries default has no slot for archive/reception integrity (forgeries, contested editions, composite authorship) | Nietzsche, Zhuangzi | **YES** — sixth default section in `four-axes.md` Axis 4 |
| 5 | Collaborator first-hand testimony (DoP / co-writer / lab partner) wrongly classed as `distillations/` under current policy | Kurosawa, Curie | **YES** — collaborator guidance in `source-policy.md` |
| 6 | No pre-emptive warning that some figures have near-zero biography | Zhuangzi | NO (covered by finding #4's archive section and existing "no evidence found" rule) |
| 7 | "Adversaries" assumes named critics of *ideas*; fails for figures attacked for their *presence* (e.g., Curie vs. patriarchy) | Curie | NO (observation to carry; not patched — revisit after #3's reworking lands) |
| 8 | New `rewatch/relisten` operation for visual primaries | Kurosawa | NO (existing `ingest` semantics suffice; adding a new operation would bloat the vocabulary for one medium) |

## Docs Impact

| File | Action | What changes |
|------|--------|-------------|
| `docs/README.md` | Update | Add plan row |
| `docs/plans/2026-04-18-iter2-amendments-from-multi-figure-eval.md` | Create | This plan |
| `skills/create-figure-skill/references/prior-snapshot-template.md` | Create | New light skeleton for prior snapshots (sections + prompts, no rigid schema) |
| `skills/create-figure-skill/references/research-stance.md` | Update | Distinguish three subtypes of adversarial work (textual-critical / interpretive / reception-historical). Add one-line pointer to prior-snapshot template. |
| `skills/create-figure-skill/references/four-axes.md` | Update | (a) Axis 3 gets a short "scope note" acknowledging 字/词/句/段/章 is a continuous-prose scaffold, with pointers to alternative decompositions for aphoristic, classical-Chinese parable, and visual-primary figures. (b) Axis 4 gains a sixth default section: "Archive / Reception Integrity". |
| `skills/create-figure-skill/references/source-policy.md` | Update | Add a "Collaborator testimony" subsection — first-hand accounts by collaborators (DoP, co-writer, lab partner) are primary-grade evidence *about the work*, not distillations. |
| `skills/create-figure-skill/SKILL.md` | Update | One-line addition to the "Where to read what" table pointing at the new prior-snapshot template. |

No script changes. No changes to the four routes, four axes count, mode count, or operation vocabulary.

## Success criteria

- All five amendments land in their designated files.
- `git diff --name-only` matches Docs Impact table exactly.
- Scaffold still runs clean (audit behavior unchanged).
- Each new or modified section is under ~50 lines — no runaway essays.
- Amendments cite the concrete figures that motivated them (in comments or examples) so future readers can see why the guidance exists.

## Out of scope for this patch

- No retrofit operation for pre-maintenance-layer skills.
- No new scripts.
- No changes to `scaffold.py`, `manifest.py`, or `audit.py`.
- No sixth axis, no new route, no new operation.
- The three unaddressed findings above (#6, #7, #8) are recorded for later deliberation.
