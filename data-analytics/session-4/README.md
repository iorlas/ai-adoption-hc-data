# Session 4 — ADF, and a look at what's next

Tuesday 18 August 2026 · 3 hours · both teams together throughout.

Same rhythm as Monday: **we do it, then you do it, then you tell us you are
ready, and only then do we move on.**

Most of today goes to ADF, because you told us where the pain is:

> "ADF is our biggest pain. Everyone hates it. It's a nightmare. Everything's
> really old and we don't understand it… some of them are enormous and none of
> us made them and the documentation is very weak."

We are not changing how you build pipelines. The goal is narrower: **make the
ones you inherited understandable.**

## The day

| # | Folder | Min | What you do |
|---|---|---|---|
| 0 | `00-opening/` | 15 | How the practice ask went |
| 1 | `01-adf-explain/` | 25 | Work out what an inherited pipeline actually does |
| 2 | `02-adf-document/` | 30 | Turn that into documentation a colleague could use next year |
| 3 | `03-adf-weak-spots/` | 20 | Find where it will break, before it does at 3am |
| — | *break* | 10 | |
| 4 | `04-better-questions/` | 35 | Hypothesis → query → answer you trust |
| 5 | `05-ml-taster/` | 30 | One machine-learning example, watch only |
| 6 | `06-close/` | 15 | Retro across all four sessions, and what we propose next |

Each part is one folder. Its `README.md` is the part — why it matters, then every
step. We read it with you. Who drives is always marked:

> **▸ We run it first, then you** — watch, then repeat the same thing
> **▸ Your turn** — you drive, we are on the floor
> **▸ Together** — whole room, out loud

Nothing is a test and nothing is graded.

**No card games today.** The ADF parts produce a document instead. The one
out-loud round is in part 3, using the data-quality
rules **you** wrote on Monday.

Parts 1–3 are three passes over the **same** pipeline, in `adf/`. No ADF instance
needed — the pipeline is JSON, and Claude reads JSON as text.

## What you need in front of you

- Claude open and signed in — desktop app or Git Bash terminal, whichever you
  chose
- This folder on your machine, including yesterday's `CLAUDE.md` with your
  definitions in it, and `docs/data-quality-rules.md`
- Power BI Desktop is **not** needed today

If anything misbehaves, **[`quirks.md`](../quirks.md)** has the fix.

## If you missed Monday

Two parts use files Session 3 produced. **Tell us at the start and we will send
you both** — two minutes to drop in, nothing today is blocked.
