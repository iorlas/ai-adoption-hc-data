# Supporter Analytics — workshop sample repository

> **Sessions 3 & 4, start here.** Open the **Git Bash** terminal, then two
> commands and you are running:
>
> ```bash
> git clone https://github.com/iorlas/ai-adoption-hc-data.git
> cd ai-adoption-hc-data/data-analytics
> uv run verify.py
> ```
>
> Every line should say `OK`, and `supporters.csv` should read **4,022 rows**.
> Say that number out loud
> — it is how we know the whole room is on the same data.
>
> **Power BI is not needed until after the break.** Everything this morning runs
> on these files.

A small, synthetic supporter-analytics dataset and codebase for the Claude Code
workshop. It is shaped like a charity's supporter and fundraising data
(supporters, donations, campaigns, email activity, fulfilment tasks) so the
exercises feel like your work — but **every row is synthetic and fictional. No
real supporter, donor or patient data is used anywhere in this repository.**

Everyone in the room works from **this same data**, on purpose. When you follow
a step, you should get the same number we got — and if you do not, that is
worth stopping for.

## Two pages to keep open

1. **[`reference/checking-the-answer.md`](reference/checking-the-answer.md)** —
   five tells for a wrong answer, and the cheap question that catches each. **If
   you keep one page from these two days, keep this one.**
2. **[`reference/desktop-or-terminal.md`](reference/desktop-or-terminal.md)** —
   terminal or desktop app, and the honest differences. They are the same Claude
   Code; either is fine for everything here.

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
verify.py     the green check — run it first, expect 4,022 supporters
quirks.md     when something misbehaves. Windows, every rough edge we know
              about, with the fix
```

## Set up

Nothing to install beyond the prerequisites you were sent (Claude, Python 3.11+,
`uv`, Git, VS Code). There is **no database to install** — the CSVs are queried
in place through DuckDB, which `uv` fetches for you the first time it is needed.

```bash
git clone https://github.com/iorlas/ai-adoption-hc-data.git
cd ai-adoption-hc-data/data-analytics
uv run verify.py
```

`verify.py` checks Python, `uv`, DuckDB and that all five CSVs are readable, and
prints one row count per file. **If anything is not green, say so straight away**
— it takes a minute to fix at the start and costs you the morning if it waits.

Anything that misbehaves — here or later — is in
**[`quirks.md`](quirks.md)**, with the fix.

## Power BI — during the break, not now

Nothing before the break needs it. **In the break**: open Power BI Desktop
(dismiss the sign-in form if it appears — you do not need to sign in; if it
opens on the Home screen, pick **New → Report**), then **Home → Get data →
Text/CSV** and **Load** each of the five files from `data/` in turn. Save the
`.pbix` anywhere on your own machine.

**No new workspace, and nothing to ask IT for.** Workspaces belong to Power BI
*Service* — for publishing a report to other people. Nothing here is published;
every report you build is a file on your own laptop, and you do not need to sign
in to Power BI to do any of it.

**Stop once the five tables are loaded** — no relationships, no measures. We
build the model together straight after the break, and starting early just
means redoing it.

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
