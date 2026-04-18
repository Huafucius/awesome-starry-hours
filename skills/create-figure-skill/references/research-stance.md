# Research Stance

This file is the posture that makes a figure skill non-trivial. Without it, the skill will drift toward a whitewash.

Read it before any pass that changes evidence, claims, or modes. Re-read it whenever Evidence Expansion or Knowledge Distillation starts feeling formulaic.

## The core problem

Famous people generate admiring material. Search engines surface that material first. Training data contains more of that material. If you research a figure by reading what comes easily, you will produce a skill that sounds like a fan letter with chapter headings.

Good research actively fights this gravity.

## Four ideas to internalize

### 1. Turn every page (Caro)

Robert Caro, on researching Lyndon Johnson:

> Turn every page. Never assume anything. Turn every goddamned page.

Agents have an advantage here: we can turn pages in parallel. Don't stop at the first three results. If the figure has forty years of output, expect to surface it across categories, languages, and decades. Use the heuristics in `deepresearch-playbook.md` to keep "enough" from becoming a vibe, but do not mistake heuristics for ritual.

### 2. Show the seams (Malcolm)

Janet Malcolm, on biography:

> A fundamental rule of journalism is to tell a story and stick to it. Cinderella must remain good and the stepsisters bad.

A researcher who shows no seams is lying. When three sources contradict, do not pick one and discard the rest — keep all three and explain the tension. When a dimension has no evidence, write "no evidence found" and list the queries actually tried. Never invent plausible content to fill a gap. The gap is information.

### 3. The four corpora, and what each betrays

An agent researching a figure has four source types, each with a built-in bias:

- **Prior** (the model's training-data impression) — the ambient consensus. Safe, bland, sanded-smooth. Useful as a baseline to cross-check against. Never as ground truth.
- **Primary** (the figure's own words) — the figure's preferred self-narrative. Weight highly, but watch for the too-clean story. People curate their own record; so do their estates.
- **Critical** (adversaries, reassessments, rivals) — the correction force. Without it, the skill is hagiography. Over-weight this deliberately when primary sources feel monotonically flattering — the imbalance you feel is probably real.
- **Distillations** (what other thinkers have already compressed about this figure) — useful acceleration, dangerous amplification. If every distillation makes the same point, ask why. Sometimes a single early profile propagates unchecked for decades.

For `bootstrap`, never collect from only one category. For `update`, `repair`, and `extend`, start narrow if you must — but before you let a strong new claim into the skill, ask whether you have given it enough cross-category pressure. See `source-policy.md` for category rules.

### Adversarial work is three jobs, not one

"Critical" is a storage category. Adversarial pressure is an epistemic job, and for contested figures it splits into three distinct tasks that collapse into each other if you are not careful:

- **Textual-critical** — *is this really what the figure wrote?* Forgeries, posthumous compilations edited by family or estate (Nietzsche's sister and *Der Wille zur Macht*), composite authorship (*Zhuangzi* Inner vs. Outer vs. Miscellaneous chapters), Cultural-Revolution-era editorial elision (鲁迅). Without this pass, interpretive debate happens on an unstable text.
- **Interpretive** — *given the text, what does it mean?* Competing readings by serious scholars, schools of interpretation, philosophical or critical traditions that disagree. Kaufmann vs. Heidegger vs. Deleuze on Nietzsche; Graham vs. Ziporyn vs. Watson on Zhuangzi. This is the classical "critical source" work.
- **Reception-historical** — *who has claimed this figure, for what, and at what cost?* Weaponization (Nazi Nietzsche; Mao-era 鲁迅), rival custodianships, partisan canonization presented as consensus, the figure's afterlife as a distinct object from the figure.

For canonical figures with active reception battles, all three are load-bearing and Phase 3 should explicitly note which one a given critical source is addressing. For lesser-known figures, the interpretive pass is usually sufficient; note that in `sources/research-plan.md`.

## Delta discipline

Not every pass is a full rebuild.

- In `bootstrap`, search broadly and establish the first durable corpus.
- In `update`, search for the new evidence and then widen only when the delta exposes a deeper hole.
- In `repair`, gather only what is needed to fix the broken claim, weak boundary, or failed mode.
- In `extend`, gather what the new capability needs and no more.

The discipline does not change: the narrower the pass, the more explicit you must be about what you did **not** re-evaluate.

### 4. Principle + Trace + Limits

Peter Kaufman's preface to *Poor Charlie's Almanack* does not just list Munger's principles — it shows each one executing on a real problem and names where it breaks. That is the structure to imitate.

When writing `research/thinking.md`, no mental model appears as "name + one-liner + an anecdote". That is the most common failure mode of figure skills — a trope dressed as insight. Demand three pieces for every mental model you record:

- **Principle** — the claim, stated plainly.
- **Trace** — a specific decision or text where the figure applied this principle, with source citation.
- **Limits** — a case where the principle fails, or a named critic who disputes its generality.

If you cannot produce the Trace and Limits for a given principle, the principle is not yet established. Either keep researching or drop it. "Provisional" principles without traces become slogans.

## Anti-patterns that will produce a bad skill

| Pattern | What it looks like | What to do instead |
|---|---|---|
| **Quote-scaffold** | "[Figure]'s five core principles: 1. A slogan. 2. A slogan. ..." | Principle + Trace + Limits. No Trace → no principle. |
| **Hagiography** | The research reads like the figure's Wikipedia on a good day. | Run the Adversarial Pass. No principle without a named critic or a documented failure. |
| **Template fatigue** | Every figure fills the same ten dimensions in the same rhythm. | Dimensions without evidence get "no evidence found, tried X/Y/Z". A figure with no sense of humor gets a thin humor section. |
| **Cosplay as distillation** | The skill is evaluated by "does it sound like him" rather than "does it reason like him". | Judgment and method are the substance. Voice is one axis of four, not the whole. |
| **Decision by access** | The figure's 1,000-page memoir shapes the skill because it was easy to parse. | Source weight is by evidence quality, not by word count. A single letter can outweigh a memoir. |
| **Convergence theater** | Contradictions smoothed into a clean narrative. | Keep the contradiction visible. Contradictions are data, not noise. |

## The smell test before moving on

Before considering the pass done, answer the questions that fit the route you actually ran:

- If this was `bootstrap`, can I point to a moment where the figure was publicly wrong? Is it in `boundaries.md`?
- If this pass changed `thinking.md`, does each major new or revised principle have critical pressure behind it?
- If this pass changed `expression.md`, did I refresh the layers that were actually touched instead of collapsing them into one blob?
- Did I search in the figure's native language if they wrote in one and the route required new evidence?
- Is every new "no evidence found" paired with the specific queries I actually tried?
- If this pass changed `identity.md`, did I add the relevant relational patterns, stress events, or evolution instead of only surface biography?

If a relevant answer is no, the pass is not done. Go back.
