# 1 — Prompt refresher (and two windows)

**20 minutes · Claude Code, in the terminal and in the desktop app**

**First six minutes: setup.** The workshop folder did not reach you before
today, so we do it together — one `git clone`, one check, and you are running.
Everything is in [`setup.md`](setup.md).

**You do not need Power BI until after the break.** Everything this morning runs
on the files.

## Why this is here

It has been a month, and the first thing you do today should be something small
and real rather than the hard part cold.

There is also a practical bit of housekeeping: you were asked to install the
desktop app, and July ran in the terminal. Two minutes settles that so it is not
sitting under the rest of the day.

## The two windows, quickly

> **Same Claude Code. Same model, same `CLAUDE.md`, same files. Two windows.**
>
> **For everything in these two days they are equal.** Every prompt in every
> exercise works identically in both.

> **If you are not already a terminal person, use the desktop app. If you are,
> stay in the terminal.** Same Claude, same answers. Whichever you pick, do not
> switch mid-day.

Use whichever you will actually open. If the terminal suits you, stay in the
terminal — nothing this week needs the app. If you would rather work in a normal
window, the app gives you that and changes nothing else. Plenty of people end up
using both.

The honest differences, where each is genuinely nicer, are one page:
[`reference/desktop-or-terminal.md`](../../reference/desktop-or-terminal.md).

## The shape of a prompt that works

Most working prompts are some combination of three things:

| | |
|---|---|
| **Situation** | what is going on, and what it should look at |
| **Question** | what you actually want to know |
| **Task** | what you want it to do, or hand back |

**And you rarely need all three.** That is the point of this part, and it is the
thing most worth unlearning:

- If Claude can already see the file, do not describe it. *"How many rows in
  `supporters.csv`?"* is a complete prompt.
- Question and task are often the same sentence. Splitting them is padding.
- **A short prompt is not a lazy prompt.**

**Add a part when the answer came back wrong in a way that part would have
prevented.** Not before.

## Where the fuller version fits

In July we took a prompt apart into four named pieces — **request · target ·
location · actions.** That is the complete anatomy, and it is exactly what to
reach for when a prompt keeps giving you the wrong *shape* of answer: prose
instead of a query, the wrong file, Python when you wanted SQL.

**It is a diagnostic, not a template.** Something to run a failing prompt
against, not a form to fill in every time. Full version, with what each missing
part looks like:
[`reference/prompt-patterns.md`](../../reference/prompt-patterns.md).

## How this part runs

Read the two tables above. Then we play a short game to see whether it stuck —
five prompts on screen, you call whether each one is fine or what it is missing.
Then everyone runs one real prompt against the shared data.

→ **`game.md`** · **`exercise.md`**

## What you leave with

The first profile of the shared dataset — which part 2 picks straight up — and a
settled answer to which window you are working in today.
