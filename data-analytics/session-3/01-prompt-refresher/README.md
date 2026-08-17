# 1 — Prompt refresher (and two windows)

**20 minutes · Claude Code, in the terminal and in the desktop app**
*6 min setup · 2 min two windows · 3 min the shape of a prompt · 5 min the game
· 4 min you run one real prompt.*

> **Who does what:** **▸ We run it first, then you** — watch, then repeat it ·
> **▸ Your turn** — you drive, we are on the floor · **▸ Together** — whole room,
> out loud. Nothing here is a test.

**First six minutes: setup.** One `git clone`, one check, and you are running.
Everything is in [`setup.md`](setup.md).

**You do not need Power BI until after the break.** Everything this morning runs
on the files.

## Why this is here

Start on something small and real rather than the hard part cold. And two
minutes settles which window you are working in, so it is not sitting under the
rest of the day.

## The two windows, quickly

> **Same Claude Code. Same model, same `CLAUDE.md`, same files. Two windows.**
>
> **For everything in these two days they are equal.** Every prompt in every
> exercise works identically in both.

> **If you are not already a terminal person, use the desktop app. If you are,
> stay in the terminal.** Same Claude, same answers. Whichever you pick, do not
> switch mid-day.

The app is not the more capable one, and the terminal is not the serious one.

The honest differences are one page:
[`reference/desktop-or-terminal.md`](../../reference/desktop-or-terminal.md).

## The shape of a prompt that works

Most working prompts combine three things:

| | |
|---|---|
| **Situation** | what is going on, and what it should look at |
| **Question** | what you actually want to know |
| **Task** | what you want it to do, or hand back |

**And you rarely need all three** — the thing most worth unlearning:

- If Claude can already see the file, do not describe it. *"How many rows in
  `supporters.csv`?"* is a complete prompt.
- Question and task are often the same sentence. Splitting them is padding.
- **A short prompt is not a lazy prompt.**

**Add a part when the answer came back wrong in a way that part would have
prevented.** Not before.

## Where the fuller version fits

July's four named pieces — **request · target · location · actions** — are what
to reach for when a prompt keeps giving the wrong *shape* of answer: prose
instead of a query, the wrong file, Python when you wanted SQL.

**A diagnostic, not a template.** Full version:
[`reference/prompt-patterns.md`](../../reference/prompt-patterns.md). Everything here is two or three sentences.

## How this part runs

Read the two tables, play the game, then one real prompt each.

**▸ Together, out loud.** [`game.md`](game.md) — five prompt cards: would you
send it?

---

# The exercise

**One real prompt, in your window. 4 minutes.** Straight after the game.

## Run it

**▸ Your turn — and we run the same prompt alongside you, in both windows.**

Type this into whichever window you are using — terminal or desktop app:

> Profile `data/supporters.csv` using DuckDB SQL. For every column give me the
> row count, how many are blank, how many distinct values, and for the text
> columns the five most common values. Show me the SQL you ran, then the
> results.

Three sentences. Situation is implied — the file is right there. The last clause
is the one that earns its place.

**We run the identical prompt in both windows on screen.** Same answer both
times, because it is the same Claude Code.

## What you should get

**4,022 rows** in `supporters.csv`.

**If your number is different, say so now.** You are not on the same data as
everyone else — cheap to fix at twenty past, expensive at half eleven.

## Keep the answer

Part 2 starts from this profile. Do not close it.

---

## Confirm ready

Tell us when you can show:

1. The row count on your screen reading **4,022** — say it out loud
2. Which window you are working in for the rest of the day

## What you leave with

The first profile of the shared dataset — which part 2 picks straight up — and a
settled answer to which window you are working in today.

---

## If it goes wrong

**It cannot find the file.** Wrong folder — you want the one containing
`README.md` and `verify.py`.

**It writes Python instead of SQL.** Say *"use DuckDB SQL over the CSVs, not
pandas."* Part 4 fixes it properly.

**It gives you a summary with no query.** Ask for the query. Every time — card C
from the game, and tell 2 in
[`reference/checking-the-answer.md`](../../reference/checking-the-answer.md).

**Your row count is not 4,022.** Stop and tell us.
