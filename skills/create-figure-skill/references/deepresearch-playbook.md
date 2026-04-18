# DeepResearch Playbook

Concrete procedures for Phase 3 (Evidence Expansion) and Phase 5 (Knowledge Distillation).

The core move in both phases is the same: **the main agent orchestrates; subagents retrieve or extract in parallel when parallelism buys real coverage or speed**. The goal is not to make every pass massive. The goal is to make every pass honest.

---

## Route defaults

| Route | Retrieval posture | Distillation posture | Probe posture |
|---|---|---|---|
| `bootstrap` | Broad, multi-category corpus build | Compile all four core axes | Probe the full interface |
| `update` | New evidence first; widen only if conflict appears | Refresh impacted axes and modes | Probe changed behavior + regression |
| `repair` | Claim- or boundary-focused retrieval | Rewrite the smallest affected surface | Probe repaired behavior + regression |
| `extend` | Gather what the new capability needs | Distill only what supports the extension | Probe the new capability + regression |

If the route is unclear, stop and clarify it in the working artifacts before searching.

---

## Phase 3 · Evidence Expansion

### 3.1 Scope the delta first

Before issuing searches, write down what is changing.

- Which figure, claim, mode, or axis is being built or revised?
- Which existing files are likely to be touched?
- Which source categories matter most here?
- What would count as enough evidence for this pass?

When the retrieval scope is non-trivial, save this to `sources/research-plan.md`.

### 3.2 Query burst

Generate queries from the actual target, not from abstract completeness guilt.

- Search in the figure's native language first when they wrote in one.
- For `bootstrap`, expect a broad query set spanning primary, critical, and distillation sources.
- For `update`, `repair`, and `extend`, start with targeted queries tied to the delta.
- Expand only when the results reveal a deeper gap, contradiction, or underrepresented period.

There is no sacred query count. What matters is whether the intended delta is well-supported and whether the remaining holes are explicit.

### 3.3 Parallel retrieval

Dispatch subagents in batches when it meaningfully increases coverage.

- Give each retrieval subagent a small batch of focused queries.
- Retrieval subagents retrieve; they do not perform final judgment.
- Save raw files to the correct `sources/*/raw/` category.
- Return a short inventory of what was found and what looks load-bearing.

If the pass is small enough to handle inline without becoming a bottleneck, do it inline.

### 3.4 Gap accounting

After the first pass, ask what is still missing.

- Which intended claims are still single-sourced?
- Which time periods or relationships are underrepresented?
- Which modes or axes still lack enough material?
- Which contradictions remain unresolved?

If the answer changes what you need to search next, write `sources/gap-report.md`.

### 3.5 Adversarial pass

Adversarial work is mandatory for **new or revised strong claims**.

Do not run it performatively across untouched territory. Do run it whenever the pass introduces or materially changes claims about:

- methods or principles
- character, motive, or integrity
- historical impact or originality
- correctness on a disputed issue

When needed:

1. Number the contested claims in `sources/claims.md`.
2. Generate adversarial queries per claim.
3. Record results in `sources/adversarial-findings.md`.
4. If nothing adversarial surfaces, say so explicitly and list the queries tried.

### 3.6 Triangulation

Before a strong claim enters `research/`, prefer at least two independent sources.

Independent means:

- different authors
- different outlets or venues
- not the same source propagated through mirrors

If triangulation fails, either keep the claim with an explicit weak-evidence label or drop it.

---

## Phase 5 · Knowledge Distillation

The normalized corpus is not the final product. Distillation compiles it into the durable knowledge layer that future agents should read first.

### 5.1 Summaries as needed

Summaries are a compression aid, not a ritual tax.

Create or refresh `sources/*/summaries/*.md` when:

- the changed corpus is too large to re-read comfortably
- subagents need a fast index before axis work
- future use-time agents will benefit from a compact map of the new material

For tiny deltas, you may skip new summaries if direct re-reading is cheaper and clearer.

### 5.2 Axis extraction

Distill into the four core research files defined in `four-axes.md`:

- `research/identity.md`
- `research/thinking.md`
- `research/expression.md`
- `research/boundaries.md`

Use parallel subagents when multiple axes are materially affected. For narrow passes, rewrite only the impacted axes.

Each axis writer should:

1. Read the relevant summaries and/or changed cleaned sources.
2. Pull in adversarial findings where the axis depends on contested claims.
3. Cite source files for strong claims.
4. Mark thin areas honestly instead of smoothing them over.

### 5.3 Reconciliation

The main agent performs the final reconciliation pass.

- Deduplicate overlapping observations.
- Surface contradictions instead of hiding them.
- Update `research/README.md` so future agents can navigate what changed.
- Decide whether the delta stayed local or forced a broader rewrite.

---

## Route-neutral anti-laziness checklist

Use this checklist before leaving Phase 5:

- [ ] The pass has a clear route: `bootstrap`, `update`, `repair`, or `extend`.
- [ ] New or revised strong claims have enough evidence to survive contact with a reader.
- [ ] Material gaps are named explicitly somewhere (`gap-report.md`, the relevant `research/*.md`, or both).
- [ ] `boundaries.md` reflects the current risk surface, not the previous one.
- [ ] Untouched areas were left untouched deliberately, not forgotten.

If the main agent is tempted to skip a step for token-budget reasons, delegate the narrow subtask to a subagent. Do not replace evidence with confidence theater.
