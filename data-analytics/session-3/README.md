# Session 3 — Numbers you can defend

Monday 17 August 2026 · 2 hours 55 · both teams together throughout.

The whole day answers one question:

> **When AI produces a number for you, how do you know it is right, and how do
> you defend it to the person who asked?**

Two of us are running it. Denis leads and explains; Mykola drives the practical
work on screen — so there is always one of us free to come and unblock you.

Every hands-on part works the same way: **we do it, then you do it, then you
tell us you are ready, and only then do we move on.** If something is going too
fast, stop us. People getting lost and not being able to pick back up was the
main thing that went wrong in July.

## The day

| # | Folder | Min | What you do |
|---|---|---|---|
| 0 | `00-opening/` | 10 | Where July got to, and how today is shaped |
| 1 | `01-data-quality/` | 30 | Find what is wrong with the shared data, and write rules that catch it |
| 2 | `02-genie-vs-claude-code/` | 15 | Watch the same question go into Databricks Genie and into Claude Code |
| — | *break* | 10 | |
| 3 | `03-shared-definitions/` | 40 | Two reports, one measure, two numbers. Agree one definition and write it down |
| 4 | `04-build-and-verify/` | 55 | Build a report with Claude, then prove it is right |
| 5 | `05-close/` | 15 | Retro, and one thing to try before Tuesday |

Every folder holds **`README.md`** (what this part is about) and, where there is
something to run, **`exercise.md`** (exactly what to do). The opening, the Genie
comparison and the close have no exercise.

## The thread running through it

Each part hands something to the next:

1. You find out the data is messier than the reports admit.
2. You see that two tools answer the same question differently, and why.
3. You discover two live reports disagree about "active supporters" — and the
   messiness from part 1 is one of the reasons.
4. You agree a definition, write it into `CLAUDE.md`, and then build a new
   report that uses it — and check it against the old ones.

By the close you have a written definition your team shares, a set of
data-quality rules, and a report you built *and* verified.

## What you need in front of you

- The Claude desktop app, signed in
- This folder, on your machine
- Power BI Desktop with the five CSVs from `data/` loaded
- `uv run verify.py` showing green

## Two pages worth having open

- **[`reference/claude-desktop.md`](../reference/claude-desktop.md)** — read it
  before Monday. Five minutes. The app is new to everyone; July was the terminal.
- **[`reference/checking-the-answer.md`](../reference/checking-the-answer.md)** —
  keep it open all day. Five tells for a wrong answer and the cheap question
  that catches each. You will use three of them before the break.

## What you will have written by the end

Not slides. Files, in this folder, that keep working after Monday:

| File | From |
|---|---|
| `docs/data-quality-rules.md` | part 1 |
| `docs/measure-definitions.md` | part 3 |
| `docs/decisions/0001-active-supporter.md` | part 3 |
| A Definitions section in `CLAUDE.md` | part 3 |
| Your own report, built and then verified | part 4 |

The first four already exist as skeletons with the headings in place. You are
filling them in, not starting from a blank page.
