# Iter-3: observe operation, reception baseline, raw counterpart

**Goal:** Close three specific gaps surfaced by the iter-2 regression eval (round 3): add an `observe` operation for non-textual primaries (Kurosawa-motivated), add a reception-baseline requirement to mode files (Nietzsche-motivated), and tighten the `raw/` counterpart rule in source policy (caught by the user inspecting r3 artifacts).

**Why:** The iter-2 regression eval returned "ship it" from all four figures but named three precise next-step items, each tied to a real defect:

1. The Kurosawa agent said: *"Add a `rewatch/relisten` (or generically, `observe`) operation with a structured-observation artifact format before this skill meets Phase 3 on any visual- or audio-primary figure — otherwise `cleaned/` will keep pretending text is the substrate."* Without it, a filmmaker or musician skill has no honest way to land primary evidence.
2. The Nietzsche agent said: *"Close the loop by adding one paragraph to `mode-writing-guide.md` telling mode authors to declare which Nietzsche (lived vs. received) each mode answers as."* The Archive/Reception Integrity section in `four-axes.md` exists; the mode-layer handshake does not.
3. Direct inspection caught that the iter-1 P2 eval's pre-cleaned-markdown input was routed straight to `cleaned/`, bypassing `raw/`. The agent did what the prompt asked; the prompt asked for a shortcut the policy did not authorize. The policy's "What raw/ holds" section can be read either way — it needs an explicit statement that every `cleaned/` entry has a `raw/` counterpart, even for already-markdown inputs.

**Success criteria:**

- `maintenance-operations.md` gains an `observe` operation with: definition, required frontmatter fields, artifact placement (`sources/primary/cleaned/`), and the Axis-3-grid pointer.
- `source-policy.md`'s `source_type` enum includes `observation`.
- `SKILL.md`'s Operations section lists `observe` alongside the existing four verbs.
- `mode-writing-guide.md`'s "What every mode file must include" adds a "Reception baseline" item required for figures with Archive/Reception integrity findings.
- `source-policy.md`'s "What `raw/` holds" adds an explicit rule: every `cleaned/` entry has a `raw/` counterpart; pre-clean inputs still land in `raw/` first.
- Scaffold still runs clean; audit behavior unchanged.
- Each amendment stays under 25 lines. No cascade rewrites.

## Docs Impact

| File | Action | What changes |
|------|--------|-------------|
| `docs/README.md` | Update | Add plan row |
| `docs/plans/2026-04-18-iter3-observe-reception-raw.md` | Create | This plan |
| `skills/create-figure-skill/references/maintenance-operations.md` | Update | Add `observe` as a fifth operation |
| `skills/create-figure-skill/SKILL.md` | Update | Add `observe` to the operations line in "Operations within a pass" |
| `skills/create-figure-skill/references/mode-writing-guide.md` | Update | Add reception-baseline requirement for contested-reception figures |
| `skills/create-figure-skill/references/source-policy.md` | Update | (a) Add `observation` to `source_type` enum. (b) Tighten "What `raw/` holds" with explicit counterpart rule. |

No script changes.

## Out of scope

- Curie: scientist-variant cognition axis, partnership credit-allocation, target-spec artifact (held for future deliberation).
- Zhuangzi: Phase 1 figure-corpus pre-flight branch, `sources/primary/` stratification (held).
- Template §9 translation-mediation note (held).
- De-duplication between `four-axes.md` Axis 4 §6 and `research-stance.md` three-jobs (held).
- `reliability:` vocabulary extension for "faithful but cross-medium translation" (held — `note:` field is adequate for now).
