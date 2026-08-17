# 1 — Prompt refresher (and two windows)

**20 minutes · Claude Code, in the terminal and in the desktop app**
*6 min setup · 2 min two windows · 3 min the shape of a prompt · 5 min the game
· 4 min you run one real prompt.*

> **Who does what:** **▸ We run it first, then you** — watch, then repeat it ·
> **▸ Your turn** — you drive, we are on the floor · **▸ Together** — whole room,
> out loud. Nothing here is a test.

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

Same engine underneath, either way. The app is not the more capable one, and the
terminal is not the serious one — plenty of daily users are in the app for the
file-review view.

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

The same goes for angle brackets and tags around each part: they come into their
own on really long prompts — pages of background, a document pasted in.
Everything we do here is two or three sentences, so we keep it simple.

## How this part runs

Read the two tables above. Then we play a short game to see whether it stuck —
five prompts on screen, you call whether each one is fine or what it is missing.
Then everyone runs one real prompt against the shared data.

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

Three sentences. Situation is implied — the file is right there. Question and
task are doing most of the work, and the last clause is the one that earns its
place.

While you run it, **we run the identical prompt in both windows on screen**, so
you can see the two side by side. Same answer both times, because it is the same
Claude Code.

## What you should get

**4,022 rows** in `supporters.csv`.

**If your number is different, say so now.** It means you are not on the same
data as everyone else, and that is very cheap to fix at twenty past and very
expensive to discover at half eleven. This is exactly the failure the shared
dataset exists to prevent.

## Keep the answer

Part 2 starts from this profile. Do not close it.

---

## What you leave with

The first profile of the shared dataset — which part 2 picks straight up — and a
settled answer to which window you are working in today.

---

## If it goes wrong

**It cannot find the file.** Wrong folder — you want the one containing
`README.md` and `verify.py`.

**It writes Python instead of SQL.** Say *"use DuckDB SQL over the CSVs, not
pandas."* It will come up again later; part 4 is where we fix it properly rather
than repeating ourselves.

**It gives you a summary with no query.** Ask for the query. Every time — that
is card C from the game, and tell 2 in
[`reference/checking-the-answer.md`](../../reference/checking-the-answer.md).

**Your row count is not 4,022.** Stop and tell us.
