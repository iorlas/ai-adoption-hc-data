# Session 4 — ADF, and a look at what's next

Tuesday 18 August 2026 · 3 hours · both teams together throughout.

Same rhythm as Monday: **we do it, then you do it, then you tell us you are
ready, and only then do we move on.**

Most of today goes to ADF, because you told us plainly where the pain is:

> "ADF is our biggest pain. Everyone hates it. It's a nightmare. Everything's
> really old and we don't understand it… some of them are enormous and none of
> us made them and the documentation is very weak."

We are not going to try to change how you build pipelines. You already know how
to do that. The goal is narrower and more useful: **make the ones you inherited
understandable.**

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

Every part is one folder, and the files are always the same:

| | |
|---|---|
| **`README.md`** | **Read it** — what this part is, and why it matters |
| **`exercise.md`** | **Do it** — every step marked with who drives |
| **`game.md`** | **Capture it** — a few cards, called out loud. Only some parts have one |

`exercise.md` is the single description of what happens, so there is never a
question of whether you or we are driving a given step:

> **▸ We run it first, then you** — watch, then repeat the same thing
> **▸ Your turn** — you drive, we are on the floor
> **▸ Together** — whole room, out loud

Nothing is a test and nothing is graded. The openings and closes have neither
exercise nor game.

Tuesday has no card games — the ADF parts produce a document you can look at,
which is a better check than any set of cards. The one place we play it out
loud is inside part 3, using the data-quality rules **you** wrote on Monday
rather than cards we wrote.

Parts 1–3 are three passes over the **same** pipeline, in `adf/`. You do not
need an ADF instance for any of it — the pipeline is JSON, and Claude reads JSON
as text.

## What you need in front of you

- The Claude desktop app, signed in
- This folder on your machine, including yesterday's `CLAUDE.md` with your
  definitions in it, and `docs/data-quality-rules.md`
- Power BI Desktop is **not** needed today

## If you missed Monday

Two of today's parts use files Session 3 produced. **Tell us at the start and we
will send you both** — two minutes to drop in, and nothing today is blocked. No
need to announce it to the room; a quiet message is fine.
