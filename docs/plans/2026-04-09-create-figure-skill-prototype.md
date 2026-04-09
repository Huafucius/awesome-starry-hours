# Create Figure Skill Prototype Plan

**Goal:** Add a runnable `create-figure-skill` prototype to this repository and verify the full workflow by generating a Lu Xun figure skill from public-source inputs.

**Scope:** Introduce a new in-repo skill generator under `skills/` while preserving the existing awesome-list function of the repository. The prototype only supports figure generation in this round; books and brands remain future extensions. The implementation should stay lightweight: local files, scripts, markdown references, and a generated sample skill, without web services or heavy retrieval infrastructure.

**Architecture:** The repository becomes dual-track: an index of external skills plus an internal skill factory. The factory itself is a skill that creates other skills. Its product is a self-contained figure-skill folder with `SKILL.md`, `references/`, and optional `scripts/`. The prototype uses a source -> research -> distilled -> assembled-skill pipeline, with scripts handling deterministic fetching/normalization and markdown carrying the durable knowledge artifacts.

**Success criteria:** A new `skills/create-figure-skill/` prototype exists, the repository documentation clearly explains the new dual-track purpose, the prototype can generate a Lu Xun figure skill into the workspace, and the generated skill includes a usable `SKILL.md` plus source-backed supporting files.

---

## Docs Impact

| File | Action | What changes |
|------|--------|-------------|
| `docs/README.md` | Update | Record the new prototype plan alongside prior editorial work |
| `docs/plans/2026-04-09-create-figure-skill-prototype.md` | Create | Document the prototype goal, scope, tasks, and verification criteria |
| `README.md` | Update | Explain the repository's new dual-track structure and point to the in-repo figure-skill factory |
| `README.en.md` | Update | Mirror the same dual-track explanation in English |
| `CONTRIBUTING.md` | Update | Replace the old single-file original-skill guidance with contributor guidance for in-repo skill folders |

---

## Tasks

### Task 1: Establish the product baseline for the in-repo skill factory

**Files:**
- Update: `docs/README.md`
- Create: `docs/plans/2026-04-09-create-figure-skill-prototype.md`

**Steps:**
1. Record the prototype as a first-class repository initiative
2. Define the repository as both an awesome index and a skill factory
3. Commit the plan before implementation begins
4. Commit: `docs: record figure skill prototype plan`

---

### Task 2: Implement the `create-figure-skill` prototype

**Files:**
- Create: `skills/create-figure-skill/` (skill files, references, scripts)

**Steps:**
1. Define the figure-skill schema and generation workflow in `SKILL.md`
2. Add reference docs for source policy, schema, and templates
3. Add minimal scripts for normalization, indexing, and assembly
4. Keep the first version local and file-based, with no heavy infra
5. Commit: `feat: add create-figure-skill prototype`

---

### Task 3: Verify the prototype by generating a Lu Xun skill

**Files:**
- Create: generated Lu Xun skill output inside the repository

**Steps:**
1. Prepare a small, public-source-backed Lu Xun input set
2. Run the prototype scripts to assemble a Lu Xun figure skill
3. Re-read the generated skill to confirm it contains `SKILL.md` and supporting references
4. Keep the generated output as a demo artifact in the repository
5. Commit: `feat: add Lu Xun figure skill demo`

---

### Task 4: Integrate the prototype into the repository narrative

**Files:**
- Update: `README.md`
- Update: `README.en.md`
- Update: `CONTRIBUTING.md`

**Steps:**
1. Describe the repository as an awesome index plus an internal factory for distilled skills
2. Point readers to the figure-skill prototype and its Lu Xun demo
3. Update contribution guidance to match folder-based in-repo skills
4. Commit: `docs: document figure skill factory`

---

## Verification (Phase 5)

- [ ] `skills/create-figure-skill/` exists and contains a runnable prototype
- [ ] The prototype can generate a Lu Xun figure skill inside the repository
- [ ] The generated Lu Xun skill includes `SKILL.md`
- [ ] The generated Lu Xun skill includes source-backed supporting files under `references/`
- [ ] `README.md` and `README.en.md` both explain the dual-track repository structure
- [ ] `CONTRIBUTING.md` no longer suggests single-file in-repo original skills
- [ ] `git diff --name-only` matches the planned file set
- [ ] `git status` is clean
