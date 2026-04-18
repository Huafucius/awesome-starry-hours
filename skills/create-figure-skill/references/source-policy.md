# Source Policy

Rules for collecting, classifying, and annotating sources. Consult this during Phase 3 (Evidence Expansion) and Phase 4 (Corpus Preparation).

## The four categories

Every file that enters `sources/` belongs to exactly one storage category:

- **`prior/`** — the model's own prior baseline. Keep `snapshot.md` as the original pre-search snapshot. If later passes need to record how evidence corrected it, add dated notes next to it instead of overwriting it.
- **`primary/`** — material authored by the figure themselves. Books, essays, interviews, speeches, letters, notebooks, diaries. The figure's voice, uncurated.
- **`critical/`** — material authored by people challenging the figure. Rivals, adversaries, disillusioned colleagues, reassessing scholars, documented critiques. This category is the anti-hagiography vaccine.
- **`distillations/`** — material by third parties who have already compressed this figure. Profile essays, academic analyses, existing figure-skills, "best of" compilations, introductions to anthologies.

If a source blends categories (e.g., a critical biography that quotes the figure heavily), classify by **authorial voice**, not by the balance of content. A critical biography goes in `critical/` even if half its pages are the figure's own words.

The category is for provenance and storage, not ontology. One source may still inform many claims across many axes.

### Collaborator testimony is primary-grade evidence *about the work*

For figures who worked in distributed-authorship media — film, big-lab science, co-written drama, collaborative music — first-hand accounts by named collaborators are **load-bearing primary evidence about the work itself**, not distillations. Examples:

- Kurosawa's cinematographer Miyagawa Kazuo testifying to the sun-through-leaves shots in *Rashomon*.
- Pierre Curie's and Irène Joliot-Curie's laboratory accounts of radium isolation.
- A co-writer's account of how a screenplay was actually assembled.
- A primary editor's memoir about how a figure's posthumous manuscripts were assembled (this is also archive-integrity evidence per `four-axes.md` Axis 4 §6).

Store these in `primary/cleaned/` when the collaborator is testifying to **what happened in the work**, and set `author:` in the frontmatter to the collaborator's name (not the figure's). Store in `critical/` only if the collaborator is critiquing the figure rather than testifying. Store in `distillations/` only if they are generalizing across the figure's career from an outside posture.

This is a refinement of the authorial-voice rule above, not a contradiction: collaborators are first-hand *for the work they participated in*, even when not first-hand *for the figure's voice*. Downstream readers need to know who witnessed what, and collapsing collaborator accounts into `distillations/` hides that information.

## Priority of source quality

Within each category, prefer in this order:

1. **First-hand documents** — letters, notebooks, drafts, raw interview transcripts.
2. **Unedited or faithfully archived materials** — full speeches, unabridged interviews, museum archives.
3. **Authoritative collections** — scholarly editions, university repositories, estate-sanctioned complete works.
4. **Journalistic coverage by quality outlets** — Paris Review, New Yorker profiles, long-form pieces in serious publications.
5. **Commentary and interpretation** — peer-reviewed academic papers, long-form essays.
6. **Aggregators and summaries** — only when primary is genuinely unavailable.

## Avoid entirely

- Quote farms (BrainyQuote, Goodreads quote pages, quote-of-the-day sites).
- Anonymous social reposts without provenance.
- Content that cites no source.
- SEO blog posts with no visible author or publication context.
- Screenshots of text without verifiable origin.
- Any page where the figure's name is a draw for unrelated content.

If the only evidence for a claim is a quote farm, the claim does not exist for our purposes. Keep looking.

## Reliability labeling

Every `cleaned/*.md` file carries a `reliability:` field in its frontmatter. Four values:

- **`high`** — primary document from authoritative source. A published book in its canonical edition. A speech transcript from a university archive. A direct scan of a letter with provenance.
- **`medium`** — faithful secondary reproduction. An interview reprinted in a reputable outlet. A scholarly paper that cites its sources. A well-regarded biography.
- **`low`** — useful but unverifiable. A blog post summarizing an event. A podcast transcript with no published counterpart. A memoir recounting the figure at third hand.
- **`suspect`** — known to be unreliable but preserved as a data point about reception. Flag for caution in any citation.

When in doubt, label lower. `research/` citations disclose reliability: "per [source] (medium)".

## Format handling

The agent will encounter many formats during Evidence Expansion. `raw/` accepts any format; `cleaned/` is always markdown.

- **HTML** → strip navigation, ads, pagination, comment sections. Preserve the article text. LLM does this; no script needed.
- **Plain text** → add frontmatter, no other change.
- **PDF** → extract text first (the agent can use tools like `markitdown`, `pdftotext`, or direct PDF reading). Check for table mangling, footnote misplacement, missing page ranges. The first pass is mechanical; the second pass is LLM review.
- **Audio/video** → preserve transcript. If no transcript exists and the content is load-bearing, note it as a research gap rather than hoarding media that will never be processed.
- **Non-English** → keep the original language. Optionally add an English summary in a separate paragraph, clearly labeled as summary not substitute.

## Frontmatter schema for `cleaned/*.md`

Every file in `cleaned/` begins with this YAML block:

```yaml
---
title: "..."
source_url: "https://..."
source_type: essay | interview | speech | letter | biography | critique | profile | scholarly_paper | observation | distillation | other
language: zh-CN | en | ja | ...
reliability: high | medium | low | suspect
retrieved_at: YYYY-MM-DD
author: "..."          # the author of this specific piece, not the figure
note: "..."            # optional, for provenance caveats or translation notes
---
```

The body of the file is the cleaned text. Do not summarize. Do not paraphrase. Do not excerpt to "the good parts". `cleaned/` is a full-fidelity substrate — future agents may grep it for exact phrases, pull direct quotes, or re-read with new questions. If the original is long, keep it long.

### Manifest contract

`scripts/manifest.py` treats the following frontmatter fields as required for every cleaned source:

- `title`
- `source_url`
- `source_type`
- `language`
- `reliability`
- `retrieved_at`
- `author`

If these fields are missing or blank, fix the cleaned file before rebuilding the manifest.

## What `raw/` holds

- Exact downloaded files: `.html`, `.pdf`, `.txt`, `.vtt`, etc.
- No edits. Ever.
- Filename is a readable slug derived from the title.
- `raw/` is the audit trail. If we re-download the same source later, both versions are kept with date suffixes — never overwritten.

**Every `cleaned/` entry has a `raw/` counterpart of the same slug.** The rule is not optional. Even when the input arrives as already-clean markdown with valid frontmatter, copy it unchanged into `raw/` first; `cleaned/` is always derived from a `raw/` original. The `raw/` version preserves the original filename, source format, and retrieval context; without it, the `cleaned/` entry is an orphan and the audit trail is broken.

For `observe` outputs (non-textual primaries), the `raw/` counterpart is a small pointer file naming the artifact observed (e.g., the film, recording, or artwork) and the retrieval context. The primary is not itself text; the pointer records that the observation was made and against what. See `maintenance-operations.md` on `observe`.

## What `summaries/` holds

Produced during Knowledge Distillation when summaries are actually useful. One summary per cleaned source is common in `bootstrap`, but incremental passes may summarize only changed or newly important files.

- Filename mirrors the cleaned filename.
- Same frontmatter as `cleaned/` plus `summary_of: <path-to-cleaned-file>`.
- Content: what the source actually contains; which axis dimensions it touches; notable or adversarial points.
- Do not editorialize. Do not interpret beyond what the source itself does.

## Incremental normalization

For `update`, `repair`, and `extend`, normalize only newly added or changed raw files unless the source policy itself changed. Do not rebuild the whole cleaned corpus just because the workflow re-entered Phase 4.

## What gets dropped and why

Drop candidates:

- True duplicates (same content from mirror sites). Keep the authoritative version.
- Pay-walled previews with no usable content.
- Files that turn out to be about a different person sharing the figure's name.
- Content that on re-read is clearly LLM-generated spam.

Every drop should be logged in `gap-report.md` if it reveals a coverage hole.
