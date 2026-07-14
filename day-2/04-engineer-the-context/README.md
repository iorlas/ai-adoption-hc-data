# Stage 04 — Engineer the context (CLAUDE.md + `docs/`)

The residue of Stages 02–03 becomes a **knowledge layer**. CLAUDE.md is loaded on *every* prompt, so it
stays tiny — pointers and hard rules; the depth lives in `docs/`, read on demand (progressive
disclosure). Build it once, and every teammate and future session inherits it.

## Target structure

```
CLAUDE.md                 # thin: stack, pointers into docs/, conventions, what AI must not touch (PII)
docs/
  data-dictionary.md      # donor columns: meaning, type, valid range, MASKED sample
  glossary.md             # domain terms (locus, workup, HLA…) + "not a typo" rules
  decisions/0001-*.md     # the age-fix ADR (from Stage 02)
  reference/<name>.sql    # the winning set-based proc from Stage 03
```

## The jigsaw (each pair owns ONE, commit into `docs/`)

Copy the skeleton, fill it for real, keep it terse, commit:
- **`claude-md.example.md`** → the repo's `CLAUDE.md` (the *consolidator* pair; pointers must resolve).
- **`data-dictionary.md`** → `docs/data-dictionary.md` (mask every sample).
- **`glossary.md`** → `docs/glossary.md`.
- **`reference-implementation.md`** → register the Stage-03 proc under `docs/reference/`.
- ADR → `docs/decisions/0001-…` (template is in `../02-understand-the-proc/adr-template.md`).

## Governance touch-points

- **Mask before commit** — a sample value in the dictionary is synthetic/redacted, never real PII.
- **What AI must not touch** goes in CLAUDE.md: the PII policy + a deny-list on the raw-data dir; and
  *you can see what Claude read* = your audit trail.

## Debrief (optional, time permitting)

`where-does-knowledge-live.md` — a quick sorting game. Run it *after* you've built these, so it's
concrete recall: name what you just made and when to reach for each home.

## Done when

Each pair has committed its artifact into `docs/` and CLAUDE.md points at all of them.

## Reference illustrations

From Anthropic, [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents):
- **"Prompt engineering vs. context engineering"** — the *curation* figure: context is a budget you curate, not a bucket you fill. This is the CLAUDE.md-points-at-`docs/` idea in one picture (the article's "just in time" section names Claude Code by name — lightweight identifiers loaded on demand).
- **"Calibrating the system prompt"** — the *too specific → just right → too vague* gradient. The target when authoring a CLAUDE.md.
