# Session 3 — Numbers you can defend

Monday 17 August 2026 · 3 hours · both teams together throughout.

> **When AI produces a number for you, how do you know it is right, and how do
> you defend it to the person who asked?**

Two of us run it, in long stretches. Whoever is not presenting comes to unblock
you.

**Every hands-on part: we do it, you do it, you tell us you are ready, then we
move on.** If it is going too fast, stop us.

## The day

| # | Folder | Min | What you do |
|---|---|---|---|
| 0 | `00-opening/` | 5 | Where July got to, and how today is shaped |
| 1 | `01-prompt-refresher/` | 17 | The shape of a prompt that works — and both windows |
| 2 | `02-data-quality/` | 30 | Find what is wrong with the shared data, and write rules that catch it |
| 3 | `03-genie-vs-claude-code/` | 8 | Watch the same question go into Databricks Genie and into Claude Code |
| — | *break* | 10 | |
| 4 | `04-shared-definitions/` | 40 | Two reports, one measure, two numbers. Agree one definition and write it down |
| 5 | `05-build-and-verify/` | 55 | Build a report with Claude, then prove it is right |
| 6 | `06-close/` | 15 | Retro, and one thing to try before Tuesday |

Each part is one folder, always the same files:

| | |
|---|---|
| **`README.md`** | **The part.** Why it matters, then every step. We read it with you |
| **`game.md`** | **Capture it** — a few cards, called out loud. Only some parts have one |
| **`setup.md`** | Part 1 only — the three commands that get you running |
| **`take-home.md`** | Part 6 only — the practice ask for before Tuesday |

`README.md` says who is driving each step:

> **▸ We run it first, then you** — watch, then repeat the same thing
> **▸ Your turn** — you drive, we are on the floor
> **▸ Together** — whole room, out loud

Nothing is a test and nothing is graded.

## The thread running through it

1. You warm up on the shared data and settle which window you are in — the
   profile you produce is where part 2 starts.
2. You find out the data is messier than the reports admit.
3. You see two tools answer the same question differently, and why.
4. You discover two live reports disagree about "active supporters" — part 2's
   messiness is one of the reasons.
5. You agree a definition, write it down where your team and Claude both read
   it, build a report that uses it, and check it against the old ones.

By the close: a written definition your team shares, a set of data-quality
rules, and a report you built *and* verified.

## What you need in front of you

- Claude open and signed in — desktop app or Git Bash terminal, whichever you
  chose
- This folder, on your machine
- Power BI Desktop installed — we load the data together in the break
- `uv run verify.py` showing green

## Two pages worth having open

- **[`reference/desktop-or-terminal.md`](../reference/desktop-or-terminal.md)** —
  the two windows and how they differ. Same Claude Code, either is fine.
- **[`reference/checking-the-answer.md`](../reference/checking-the-answer.md)** —
  keep it open all day. Five tells for a wrong answer and the cheap question
  that catches each. You will use three before the break.

When something misbehaves: **[`quirks.md`](../quirks.md)** — Windows rough edges
with the fix. Look there before asking.

## What you will have written by the end

Not slides. Files, in this folder, that keep working after Monday:

| File | From |
|---|---|
| `docs/data-quality-rules.md` | part 2 |
| `docs/measure-definitions.md` | part 4 |
| A decision record in `docs/decisions/` | part 4 |
| A Definitions section in `CLAUDE.md` | part 4 |
| Your own report, built and then verified | part 5 |

The first three exist as skeletons with the headings in place, and
`docs/decisions/` has a template to copy. You are filling them in, not starting
from a blank page.
