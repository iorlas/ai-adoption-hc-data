# Session 3 — Numbers you can defend

Monday 17 August 2026 · 3 hours · both teams together throughout.

The whole day answers one question:

> **When AI produces a number for you, how do you know it is right, and how do
> you defend it to the person who asked?**

Two of us are running it, and we take turns in long stretches rather than
swapping every few minutes. Whoever is not presenting is free to come and
unblock you — that is the point of there being two of us.

Every hands-on part works the same way: **we do it, then you do it, then you
tell us you are ready, and only then do we move on.** If something is going too
fast, stop us — you asked for more doing and less watching, and the readiness
check is how we hold ourselves to that.

## The day

| # | Folder | Min | What you do |
|---|---|---|---|
| 0 | `00-opening/` | 8 | Where July got to, and how today is shaped |
| 1 | `01-prompt-refresher/` | 14 | The shape of a prompt that works — and both windows |
| 2 | `02-data-quality/` | 30 | Find what is wrong with the shared data, and write rules that catch it |
| 3 | `03-genie-vs-claude-code/` | 8 | Watch the same question go into Databricks Genie and into Claude Code |
| — | *break* | 10 | |
| 4 | `04-shared-definitions/` | 40 | Two reports, one measure, two numbers. Agree one definition and write it down |
| 5 | `05-build-and-verify/` | 55 | Build a report with Claude, then prove it is right |
| 6 | `06-close/` | 15 | Retro, and one thing to try before Tuesday |

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

## The thread running through it

Each part hands something to the next:

1. You warm up on the shared data and settle which window you are working in —
   and the profile you produce is where part 2 starts.
2. You find out the data is messier than the reports admit.
3. You see that two tools answer the same question differently, and why.
4. You discover two live reports disagree about "active supporters" — and the
   messiness from part 2 is one of the reasons.
5. You agree a definition, write it down where your team and Claude both read
   it, then build a new report that uses it — and check it against the old ones.

By the close you have a written definition your team shares, a set of
data-quality rules, and a report you built *and* verified.

## What you need in front of you

- The Claude desktop app, signed in
- This folder, on your machine
- Power BI Desktop with the five CSVs from `data/` loaded
- `uv run verify.py` showing green

## Two pages worth having open

- **[`reference/desktop-or-terminal.md`](../reference/desktop-or-terminal.md)** —
  the two windows and how they differ. Part 1 covers it live; keep this for
  afterwards. They are the same Claude Code and either is fine.
- **[`reference/checking-the-answer.md`](../reference/checking-the-answer.md)** —
  keep it open all day. Five tells for a wrong answer and the cheap question
  that catches each. You will use three of them before the break.

## What you will have written by the end

Not slides. Files, in this folder, that keep working after Monday:

| File | From |
|---|---|
| `docs/data-quality-rules.md` | part 2 |
| `docs/measure-definitions.md` | part 4 |
| `docs/decisions/0001-active-supporter.md` | part 4 |
| A Definitions section in `CLAUDE.md` | part 4 |
| Your own report, built and then verified | part 5 |

The first four already exist as skeletons with the headings in place. You are
filling them in, not starting from a blank page.
