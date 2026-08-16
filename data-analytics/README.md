# Supporter Analytics — workshop sample repository

> **Sessions 3 & 4, start here.** You need three things working: the Claude
> desktop app, this folder on your machine, and the sample data loaded into
> Power BI Desktop. Then run `uv run verify.py` — a green result means you are
> ready for Monday.

A small, synthetic supporter-analytics dataset and codebase for the Claude Code
workshop. It is shaped like a charity's supporter and fundraising data
(supporters, donations, campaigns, email activity, fulfilment tasks) so the
exercises feel like your work — but **every row is synthetic and fictional. No
real supporter, donor or patient data is used anywhere in this repository.**

Everyone in the room works from **this same data**, on purpose. When you follow
a step, you should get the same number we got — and if you do not, that is
worth stopping for.

## Read this before Monday

Two things, fifteen minutes total:

1. **[`reference/desktop-or-terminal.md`](reference/desktop-or-terminal.md)** — the app is
   new to everyone. July was the terminal. Five minutes.
2. **[`reference/checking-the-answer.md`](reference/checking-the-answer.md)** —
   five tells for a wrong answer. Keep it open during both sessions; it is the
   one page that outlives the workshop.

## What's in here

```
data/         five CSVs — the shared dataset. Start with data/README.md
reports/      two Power BI reports that disagree with each other, as model
              notes + DAX. The disagreement is Session 3's main exercise
adf/          one large inherited ADF pipeline, as JSON. Session 4's centrepiece
docs/         skeletons you fill in during the sessions — the headings are
              already there so you are editing, not starting from blank
reference/    four short pages: the desktop app, checking an answer, writing a
              prompt, and where a piece of knowledge should live
templates/    a finished version of what you build, for a different
              organisation. Read it after you have built yours, not before
session-3/    Monday — one folder per part of the day
session-4/    Tuesday — one folder per part of the day
CLAUDE.md     project instructions for Claude. Deliberately thin on Monday
              morning; you fill it in during Session 3
verify.py     the green check you run before Session 3
```

## Set up

Nothing to install beyond the prerequisites you were sent (Claude desktop app,
Python 3.11+, `uv`, Git, VS Code). There is **no database to install**. The CSVs
are queried in place through DuckDB, which `uv` fetches automatically the first
time it is needed.

```bash
git clone https://github.com/iorlas/ai-adoption-hc-data.git
cd ai-adoption-hc-data/data-analytics
uv run verify.py
```

`verify.py` checks Python, `uv`, DuckDB and that all five CSVs are readable, and
prints one row count per file. **Do this before Session 3, not on the morning
of it.** If it is not green, tell us on Friday and we will fix it with you.

## Load the data into Power BI

Open Power BI Desktop → **Get Data → Text/CSV** → load all five files from
`data/`. Save the `.pbix` anywhere you like. That is all the preparation
Session 3 needs; we build the model together in the room.

## How each session folder works

Each numbered folder is one part of the day and is self-contained:

- **`README.md`** — what this part is about and why it matters. Read it, or let
  us talk you through it in the room.
- **`exercise.md`** — exactly what to do: the prompts to run, what you should
  see, and how to tell whether it worked.

Parts with nothing for you to run — the openings, the two watch-only
demonstrations, the closes — have a `README.md` but no exercise.

We also keep a facilitator note per part: the clock, what we demonstrate, and
how we check you got there. **Those carry the answers, so they arrive after the
sessions, not before** — you will get the whole set, it just would spoil the two
exercises the days are built around.

The rhythm is the same every time: **we do it, then you do it, then you tell us
you are ready, and only then do we move on.** If we are going too fast, stop us.

## A note on the data

The data contains **deliberate defects** — duplicates, typos, impossible dates,
orphan records, inconsistent categories. That is on purpose. Finding them,
deciding which ones actually matter, and writing rules that catch them is one of
the exercises. Please do not "fix" the CSVs.

The two reports in `reports/` also **disagree about how many active supporters
there are**. That is also on purpose, and neither of them is lying.
