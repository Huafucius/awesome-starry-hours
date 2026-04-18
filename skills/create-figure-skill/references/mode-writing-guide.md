# Mode Writing Guide

A mode file tells a future agent how to operate the generated figure skill in one specific use pattern. It is **prose instructions for an LLM**, not a schema, not a template, not a configuration.

A good mode file lets the reading agent answer four questions within thirty seconds:

1. **When to enter this mode** — with counter-examples of intents that look similar but belong elsewhere.
2. **What to read** — which `research/*.md` files, which sections, and why.
3. **What the output should look like** — voice perspective, form, length norms.
4. **What to avoid** — the specific failure modes this mode is prone to.

---

## General shape

Each mode file is usually 30-80 lines of prose. Longer than that often means it has absorbed content that belongs in `research/`. Much shorter than that often means it's under-specified. Treat this as a heuristic, not a law: `repair` passes may be smaller, and some figures need more texture than others.

Structure (guide, not schema):

```markdown
# [Mode Name] Mode

[1-2 sentences: what this mode is for.]

## When to enter this mode

[Describe the user intents this mode serves. Include 2-3 example user phrasings, and 1-2 counter-examples of intents that look similar but should go elsewhere.]

## What to read

[List the research files to consult, with priority order and why. Be specific about which sections of each file matter here.]

## How to produce

[The voice / perspective / form the output should take. Include a short example fragment if it helps.]

## What to avoid

[Specific failure modes for this mode, particularly subtle ones. Avoid generic "be honest" — write the specific traps that this specific mode in this specific figure will fall into.]

## Boundaries specific to this mode

[How boundaries.md applies here. Each mode has different edges — spell them out.]
```

---

## The five modes — character sketches

Each mode has its own character. Do not write them with interchangeable language. The following sketches describe the character each mode should carry when written for a specific figure.

### `dialogue.md` — first-person conversation

The user wants to talk with the figure directly. First-person "I" is allowed and expected. This is cosplay, and cosplay is fine — but disciplined cosplay.

- **Reads:** `identity.md` (life anchoring), `thinking.md` (how he would reason on a new topic), `expression.md` (the 句 and 段 layers shape voice). `boundaries.md` is the hard constraint.
- **Output:** conversational first-person. Greetings are okay. A framing disclaimer at most once per conversation, not per turn.
- **Key trap:** fabricating positions the figure never held. When the user asks about something post-death or off-field, the figure would have had some response, but you must **mark it as inference**: "I suspect — though I cannot have encountered this — ...".

### `voice.md` — write new content in his style

The user has a topic (often one the figure never addressed) and wants the prose to feel like his.

- **Reads:** `expression.md` (all five layers), `identity.md` (which period's voice is appropriate to the topic), `boundaries.md` (do not fabricate stances).
- **Output:** prose on the user's topic, shaped by the figure's voice. No "I am [figure]" framing. No preface about style. Just the content. Let the voice speak for itself.
- **Key trap:** borrowing the style and accidentally adopting his positions. You are writing **about the user's topic**, not pretending the figure is writing it. Position-neutral voice is the target.

### `methodology.md` — apply his analytical method

The user has a problem and wants the figure's reasoning approach applied to it.

- **Reads:** `thinking.md` (the whole file — this is the core), `identity.md` (context of how his method formed), `boundaries.md`.
- **Output:** third-person analytical prose. The figure's method operates on the user's problem. The analysis structure should follow his characteristic moves — if he opens with inversion, the analysis opens with inversion; if he chases failure modes first, so does the analysis.
- **Key trap:** conflating "his method applied to X" with "what he himself would have concluded about X". The output is an analysis through his lens — not his verdict on the user's specific problem.

### `critique.md` — review given text through his eye

The user pastes a text (an essay, a pitch, an argument) and wants the figure's critical perspective on it.

- **Reads:** `thinking.md` (his judgment patterns), `expression.md` (because critique is also a rhetorical act, and his critique has a form), `boundaries.md`.
- **Output:** a critique of the pasted text. The figure's values and sharpness are the lens. His voice leaks in naturally, which is fine — but the **target is always the user's text**, not an essay in his style.
- **Key trap:** the critique shading into parody or impression of the figure. Stay substantive: the reader should come away understanding what's weak in their text, not what the figure sounded like.

### `advisory.md` — speculate what he would think

The user asks "what would [figure] think about X?"

- **Reads:** `thinking.md`, `identity.md` (especially evolution — early vs late views differ), `boundaries.md` (**especially** the knowledge cutoff and unresolved tensions).
- **Output:** third-person speculative analysis. Explicitly labeled as extrapolation. Draw on documented positions on analogous topics.
- **Key trap:** fluency turning extrapolation into declaration. "He would say" must be softened to "based on his documented stance on [analogous topic], it is plausible that ...". If the topic is genuinely post-death or off-field, say so at the start of the response.

---

## Mode revision patterns

Not every pass rewrites all five modes.

- **`bootstrap`** — write the full five-mode surface.
- **`update`** — refresh source pointers, examples, and boundaries in the affected modes.
- **`repair`** — sharpen entry criteria, anti-patterns, or boundary handling for the broken mode without rewriting the rest.
- **`extend`** — add a new mode or widen the router logic without duplicating existing research or mode prose.

Generated figure `SKILL.md` should stay a slim router. Put durable operating detail in the mode files, not in the router.

---

## What every mode file must include

- A **When to enter this mode** section that names competing modes and explains the distinction. ("This is not `voice` because...")
- Explicit pointers into `research/`. Not "read the research" — say which file and, where it matters, which section.
- A **What to avoid** section that names this mode's specific failure modes for this specific figure. A voice-trap for Feynman is different from a voice-trap for 鲁迅.
- **Boundaries specific to this mode.** Not a copy of `boundaries.md` — a selection of which boundaries matter most here.

## What not to put in a mode file

- The full content of research files. They are referenced, not copied.
- A catalog of quotes. Those live in `sources/primary/cleaned/`.
- Long philosophy about distillation vs imitation. That is in `research-stance.md` and applies to all modes, not just this one.
- Boilerplate identical across five figures. If the text doesn't vary with the mode or the figure, it belongs higher up.
- Machine-readable schemas, loading declarations, frontmatter beyond a simple heading. Mode files are read by LLMs; they don't need to be parsed.
