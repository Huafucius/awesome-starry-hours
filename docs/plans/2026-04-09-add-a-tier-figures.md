# Add A-Tier Figure Candidates Plan

**Goal:** Add the approved A-tier figure candidates discovered in the second and third search rounds to the bilingual figure index.

**Scope:** Update `README.md`, `README.en.md`, and recreate `docs/README.md` with this plan. Preserve the current bilingual split, no-star-table format, books section, brands section, and overall README layout. Only the figure section and selection language should change.

**Architecture:** The repository remains an entity-first awesome index. Figure rows may now represent either a single notable person or a tightly scoped multi-person bundle, as long as every named target is explicit and recognizable. Generic persona packs, arbitrary-person generators, and fuzzy role bundles remain out of scope.

**Success criteria:** The approved A-tier additions appear in both READMEs under the right categories, the figure section continues to use exact names, `legends-mcp` is represented as a notable multi-person bundle, and the selection language no longer contradicts multi-person figure bundles.

---

## Docs Impact

| File | Action | What changes |
|------|--------|-------------|
| `docs/README.md` | Create | Restore a docs index and link this plan |
| `docs/plans/2026-04-09-add-a-tier-figures.md` | Create | Record the approved additions and editorial boundary changes |
| `README.md` | Update | Add A-tier figure candidates and relax selection language for explicit multi-person bundles |
| `README.en.md` | Update | Mirror the same additions and selection-language update in English |

---

## Tasks

### Task 1: Recreate the docs baseline for this editorial change

**Files:**
- Create: `docs/README.md`
- Create: `docs/plans/2026-04-09-add-a-tier-figures.md`

**Steps:**
1. Verify `docs/` is absent on the latest `origin/main`
2. Add a minimal docs index and this plan
3. Re-read both files to confirm the new docs baseline exists
4. Commit: `docs: record A-tier figure additions plan`

---

### Task 2: Expand the Chinese figure index

**Files:**
- Modify: `README.md`

**Steps:**
1. Verify the current figure section does not yet contain the approved A-tier candidates
2. Add the approved single-person candidates and the approved multi-person bundle
3. Keep categories stable while placing the new rows in the most natural groups
4. Update the selection language so explicit notable multi-person bundles are allowed
5. Commit: `docs: expand Chinese figure index with A-tier additions`

---

### Task 3: Mirror the expansion in the English README

**Files:**
- Modify: `README.en.md`

**Steps:**
1. Verify the current English figure section mirrors the smaller figure set
2. Add the same approved rows in English
3. Mirror the selection-language update for multi-person bundles
4. Re-read for category and naming consistency across both languages
5. Commit: `docs: mirror A-tier additions in English`

---

## Approved A-Tier Additions

- `alchaincyf/karpathy-skill`
- `alchaincyf/ilya-sutskever-skill`
- `alchaincyf/mrbeast-skill`
- `alchaincyf/paul-graham-skill`
- `alchaincyf/naval-skill`
- `derrickgong87/duan-yongping-skill`
- `AytuncYildizli/legends-mcp`
- `Atypical-Consulting/claude-legends-review`

## Verification (Phase 5)

- [ ] `README.md` includes all 8 approved A-tier additions
- [ ] `README.en.md` mirrors the same 8 additions
- [ ] `README.md` and `README.en.md` both allow explicit notable multi-person bundles in the selection language
- [ ] `docs/README.md` exists and links this plan
- [ ] `git diff --name-only` matches the planned file set
- [ ] `git status` is clean
