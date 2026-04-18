# Rewrite Create Figure Skill Workflow to V2

**Goal:** Fully refactor `skills/create-figure-skill/` so the skill reads and behaves like a knowledge compiler for public figures instead of a rigid, bootstrap-only SOP.

**Scope:** Update `SKILL.md`, the bundled `references/*.md`, and the deterministic helper scripts in `scripts/` so the full skill is internally consistent with the v2 philosophy: bootstrap/update/repair/extend routing, evidence-first judgment, deterministic choke points only, and no backward-compatibility ballast.

**Why:** The current skill still over-indexes on ritual, fixed sequencing, and bootstrap assumptions even after the phase rewrite. The references and scripts need to be brought into the same model so the whole skill consistently supports agent freedom, evidence-driven judgment, deterministic scripts only at choke points, and incremental work without backward-compatibility drag.

**Success criteria:** `SKILL.md`, `references/*.md`, and `scripts/*.py` all align on the v2 model; the skill explicitly supports bootstrap/update/repair/extend; old SOP language is removed or softened; deterministic scripts only check deterministic facts; and the resulting skill remains simple, coherent, and ready for iterative use.

---

## Docs Impact

| File | Action | What changes |
|------|--------|-------------|
| `docs/README.md` | Update | Record the new workflow rewrite plan |
| `docs/plans/2026-04-18-rewrite-create-figure-skill-phases-v2.md` | Update | Expand the plan from a phase-only rewrite to a full skill refactor |
| `skills/create-figure-skill/SKILL.md` | Update | Keep the v2 workflow and align the rest of the skill text around it |
| `skills/create-figure-skill/references/*.md` | Update | Reframe reference docs around route-aware knowledge compilation |
| `skills/create-figure-skill/scripts/*.py` | Update | Keep only deterministic choke-point logic and simplify audit behavior |
