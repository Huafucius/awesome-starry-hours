# Rename Source Manifest Builder Plan

**Goal:** Rename `build_source_index.py` to a less misleading name and update the workflow language so `create-figure-skill` clearly treats it as a source-manifest builder, not a search or retrieval step.

**Scope:** Keep the behavior unchanged. This task only touches naming, references, and explanatory wording around the helper script and the generated `manifest.json` file.

**Why:** The current name suggests search infrastructure or retrieval logic, but the script only scans cleaned source markdown files and emits a compact catalog. That naming mismatch makes the workflow harder to reason about.

**Success criteria:** The script has a clearer name, all references are updated, the workflow copy explains the file as a source manifest / source catalog, and the Lu Xun demo still verifies cleanly after the rename.

---

## Docs Impact

| File | Action | What changes |
|------|--------|-------------|
| `docs/README.md` | Update | Record the rename-and-clarify plan |
| `docs/plans/2026-04-09-rename-source-manifest.md` | Create | Document the naming correction and verification steps |
| `skills/create-figure-skill/SKILL.md` | Update | Replace "source index" wording with clearer source-manifest wording and explain the file as a source catalog |

---

## Tasks

### Task 1: Record the naming correction plan

**Files:**
- Update: `docs/README.md`
- Create: `docs/plans/2026-04-09-rename-source-manifest.md`

**Steps:**
1. Add the plan to the documentation index
2. Explain why the rename is needed
3. Commit before implementation
4. Commit: `docs: record source manifest rename plan`

---

### Task 2: Rename the helper script and update references

**Files:**
- Rename: `skills/create-figure-skill/scripts/build_source_index.py` to `skills/create-figure-skill/scripts/build_source_manifest.py`
- Update: all references to the old script name

**Steps:**
1. Rename the helper script to a source-manifest-oriented name
2. Rename the generated catalog file to `manifest.json` for consistency
3. Update workflow commands and surrounding prose
4. Commit: `refactor: rename source manifest builder`

---

### Task 3: Verify the renamed workflow still works

**Files:**
- No planned content changes beyond any necessary wording touch-ups from verification

**Steps:**
1. Re-run the renamed helper script on `skills/luxun-perspective/`
2. Re-run assemble and audit
3. Confirm `git status` is clean after commits
4. Commit: `docs: clarify source manifest language` if any final wording updates are needed

---

## Verification

- [ ] The old helper script name no longer appears in the repository
- [ ] `skills/create-figure-skill/SKILL.md` describes the step as building a source manifest or source catalog
- [ ] The renamed script runs successfully against `skills/luxun-perspective/`
- [ ] `assemble_skill.py` and `audit_skill.py` still pass after the rename
- [ ] `git status` is clean
