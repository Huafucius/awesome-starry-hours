# Four Axes

The four core dimensions along which a figure is researched. Each axis usually produces one file in `research/`. The axes are orthogonal as organizing principles — a single piece of evidence may touch several, but each `research/` file is written separately with its own focus.

Read this during Phase 5 · Knowledge Distillation. The dimensions listed under each axis are a **researcher's checklist**, not a mandatory schema. `bootstrap` usually touches all four axes; incremental passes may refresh only the affected sections. Leave dimensions empty — with explicit "no evidence found" and the queries tried — when evidence does not exist.

---

## Axis 1 · Identity → `research/identity.md`

Factual, low-interpretation. Grounds every mode against real history. Every other research file rests on this one.

Dimensions to cover:

1. **Timeline** — birth, death, major life phases. Specific years for major transitions (entered X career, published Y, exiled, married, retired).
2. **Geography** — where they lived, where they worked, how that environment shaped them. Geography is evidence of what a life felt like from inside.
3. **Identity shifts** — role changes (doctor → writer, lawyer → president, engineer → investor). Note the pivot events and what precipitated them.
4. **Relational patterns** — how they addressed:
   - peers (collaborators, equals in field)
   - rivals (named specifically, with examples of friction)
   - students, followers, or mentees
   - the public (audience posture, stagecraft vs reticence)
   - institutions (how they engaged with or resisted them)
5. **Key stress events** — moments when the figure was tested, publicly attacked, or faced irreversible choice. These leak operating system under load. Include at least three.
6. **Evolution** — what changed from early career to late career. Positions they explicitly recanted. Topics they stopped engaging. Views they softened or hardened.

Cite sources (file-level is fine). For contested biographical claims (disputed dates, authorship, events), note the dispute rather than pick a side.

---

## Axis 2 · Cognition → `research/thinking.md`

How they reason. The operating system.

Ten dimensions. Each serves as a potential section heading. Every principle documented must carry **Principle + Trace + Limits** (see `research-stance.md`).

1. **Default unit of analysis** — the smallest object they refuse to decompose further. Munger thinks in incentive systems. Feynman thinks in mechanisms you can visualize. 鲁迅 thinks in the social type in miniature.
2. **Load-bearing metaphors** — the analogies they return to under pressure. Metaphors reveal ontology. Munger's "latticework", "fishing where the fish are". Feynman's "cargo cult". 鲁迅's "铁屋子".
3. **Inversion vs forward mode** — do they start from "how does this succeed?" or "how does this fail?" Munger and Taleb live in the second mode. Most optimists live in the first.
4. **Tradeable vs sacred** — what are they publicly willing to be wrong about, and what is non-negotiable? Buffett trades on price; never on integrity.
5. **Time horizon and reversibility bias** — how far out they discount. How they weight reversible vs irreversible bets.
6. **Evidence threshold** — what actually makes them update? Numbers, a vivid anecdote, a trusted voice's disagreement, peer pressure?
7. **Contrarian priors** — structural disagreements with consensus. Not stylistic edginess. Not tribal markers. The specific ideas where this person diverges from the ambient view.
8. **Circle of competence demarcation** — do they explicitly mark what they will not opine on? How sharp is the boundary? Does it leak?
9. **Decision tempo** — fast heuristic vs slow deliberation. When do they switch modes?
10. **Stopping rule** — when do they decide "enough analysis, act"?

A figure skill whose `thinking.md` reads as slogans instead of these dimensions will fail in every mode except perhaps voice.

---

## Axis 3 · Voice → `research/expression.md`

How they speak and write. Five layers of granularity. Layers 1-3 are sub-attentional and hardest to fake; layers 4-5 are meaning-bearing and easier to imitate but essential for identity. `bootstrap` usually covers all five layers; incremental passes refresh only the layers touched by the new evidence or by the interface change.

### Scope note — when the figure is not a continuous-prose writer

The 字/词/句/段/章 scheme below is a **continuous-prose scaffold**. It generalizes cleanly to most essayists, novelists, and correspondents. It generalizes badly to three common figure types, each of which needs its own adaptation rather than a forced fit:

- **Aphorists and fragmentary writers** (Nietzsche, La Rochefoucauld, Lichtenberg). 段 collapses — the aphorism *is* the paragraph. The missing layer is **arrangement logic** between aphorisms: why this fragment after that one, how the constellation is built. Add an "arrangement" layer above 句 and note explicitly when the figure also writes in a second register (Zarathustra inside Nietzsche; 野草 inside 鲁迅).
- **Parable / persona writers and classical-language figures** (Zhuangzi, Kierkegaard, the Analects). Voice comes through **staged speakers** (the 寓言 of Zhuangzi, Kierkegaard's pseudonyms) and through genre conventions (classical-Chinese particles; biblical cadence). Add a **parable / persona** layer above 章. Note when the figure's voice is inseparable from translation or commentary mediation.
- **Visual-primary figures** (Kurosawa, Cartier-Bresson, any filmmaker, painter, or choreographer). The five-layer *granularity* idea still works, but the single-scale axis does not. Use a **two-dimensional grid**: unit size (frame → shot → scene → act → work) × channel (image, movement, sound, performance, duration). The text layer is a projection (screenplay, interview, artist statement) and `cleaned/` sources should carry a `note:` field stating what the projection loses.

For bench scientists and other figures whose output is mostly technical writing in a conventional register, `research/expression.md` may legitimately be thin. Do not inflate it. Note the thinness and put the interesting material in `thinking.md` (methods, notebook style) and `identity.md` (stance).

The existing five layers follow below. Treat them as the default, not the only decomposition.

### 字 · Character / grapheme layer

- Orthographic tics — punctuation preferences (em-dash, absence of quotation marks, 破折号 usage, no-quotes-McCarthy).
- Register mixing — classical particles in vernacular prose, English in Chinese writing, dialect inclusions.
- Proportion signatures — e.g., 鲁迅 retains 罢/么 over 吧/吗 at detectable frequency.

### 词 · Word layer

- Signature collocations — 所谓, 其实, 大约 for 鲁迅; "in fact", "it is easy to see" for Didion; "folly" for Munger.
- Favored semantic fields — the domains they return to involuntarily.
- Function-word distribution — under-the-radar and the most diagnostic single signal (stylometry's robust finding across Burrows, Koppel, Stamatatos).
- Taboo words — what they never use. What they refuse even when topically appropriate.

### 句 · Sentence layer

- Sentence-length distribution — mean AND variance, not just mean. Hemingway: low-low. 王小波: bimodal.
- Syntactic depth — deep right-branching (Proust) vs shallow coordination via "and" (Hemingway).
- Opener preferences — what word class starts most sentences. 汪曾祺 often opens with bare nouns or 4-character phrases.
- Punctuation rhythm — comma density, dash vs semicolon, 顿号 habits.

### 段 · Paragraph layer

- Cohesion style — explicit connectives (然而, on the other hand) vs juxtaposition.
- Paragraph shape — short-short-long rhythm, one-sentence paragraphs as hinges (Didion).
- Image-to-abstraction ratio — how often concrete image yields to generalization.
- Topic progression — constant-topic scenes vs chained-shift drift.

### 章 / 文 · Full-work layer

- Macro-structure — circular return to opening image, thesis-anecdote-thesis, accumulation.
- Stance markers — hedging density, irony frequency, first-person authority claims.
- Intertextual reflex — what they quote from involuntarily (古籍 for 鲁迅; Russell and Calvino for 王小波).
- Recurring obsessions — the thematic fingerprint across many works.

For each layer you touch, record concrete observations with source citations. If the figure produced in multiple modes (speech vs essay vs letter), note divergences — many figures have a distinctly different voice in private correspondence than in published work.

---

## Axis 4 · Boundaries → `research/boundaries.md`

Where the skill must not claim knowledge. The anti-hagiography file. This is the file that every mode consults before returning a response.

Five default sections:

### 1. Named critics

At least one per major principle documented in `thinking.md`. Format:

> **[Critic name]** ([their standing or relation to the figure]): [quote or paraphrase of the critique]. [Source citation.]

If you cannot find a named critic for a principle, either the principle is not controversial (note this explicitly) or research was insufficient (keep looking). No principle should arrive "uncritiqued" without a researcher's explicit judgment about why.

### 2. Documented failings

Recorded moral, intellectual, or practical failures. Specific events with sources. Do not editorialize; state. Examples of what this looks like:

> Feynman: documented patterns of mistreatment of women across his career (see sources/critical/...). The skill extracts his epistemic methodology, not his personal ethics.
> 鲁迅: biographers note his treatment of 朱安 (first wife) is ethically troubled. Does not undermine his literary value but must be acknowledged when the user asks "was he a good person?"

### 3. Evolution

Positions the figure changed or abandoned. Track at least three if the record allows. Note the pivot points.

### 4. Unresolved tensions

Questions this figure never answered cleanly. Internal contradictions that stayed contradictions across their career. These are often the richest material — they show where even the figure was working things out.

### 5. Knowledge cutoff

The figure's death date (if deceased). Any post-death topic is strict extrapolation. This is the hard rule for `advisory` mode: phrases like "he would say X about AI" must be softened to "based on his documented stance on Y, it is plausible that..." The cutoff is also relevant for `dialogue` mode — the figure cannot know about events after their death.

### 6. Archive / Reception integrity

Where the figure's record, canon, or received view is itself contested. Without this section the skill treats politically stabilized readings as fact. Write as applicable:

- **Contested primary texts.** Forgeries, posthumously assembled works attributed to the figure, composite or multi-author texts, translation-mediated primaries. Examples: *Der Wille zur Macht* is Elisabeth Förster-Nietzsche and Peter Gast, not Nietzsche. The *Zhuangzi* Outer and Miscellaneous chapters are mostly not Zhuangzi. *The Analects* has strata. Post-1949 editions of 鲁迅 elided material.
- **Weaponized or politically canonized reception.** When a later regime, school, or movement captured the figure's reputation and now determines what "everyone knows" about them. Name the settlement and whose interests it serves. Do not collapse the received view with the figure's actual positions.
- **Rival custodianships.** Competing schools of reading (Kaufmann vs. Heidegger vs. Deleuze on Nietzsche; Graham vs. Ziporyn on Zhuangzi). Name the rival readings; do not pick one silently.
- **The afterlife as a distinct object.** For figures whose posthumous evolution is more consequential than their lived evolution, record it here — not buried inside "evolution". The figure-as-she-lived and the figure-as-she-is-now-received are two objects and the skill must be able to address either.

This section is optional for non-canonical figures. For any figure whose reputation predates the agent's training data, it is usually mandatory.

---

## Route guidance

- `bootstrap` usually writes all four axis files in full.
- `update` usually refreshes the touched sections and reconciles the rest only if new evidence forces it.
- `repair` may revise just one subsection plus `boundaries.md`.
- `extend` may add an appendix or route-specific section if the new capability needs it.

The four axes are the default core, not a prison. If a figure truly demands an extra appendix or a route-specific research note, add it without pretending one of the four axes already covered it.

---

## How the axes feed the modes

Approximate mapping, though no mode excludes any axis:

| Mode | Primary reads | Always consults |
|---|---|---|
| dialogue | identity, thinking, expression | boundaries |
| voice | expression (all layers), identity | boundaries |
| methodology | thinking (all dimensions), identity | boundaries |
| critique | thinking, expression, identity | boundaries |
| advisory | thinking, identity (especially evolution) | boundaries (heavily — the cutoff rule) |

**Every mode consults `boundaries.md` without exception.** That is how honesty gets enforced at use-time.
