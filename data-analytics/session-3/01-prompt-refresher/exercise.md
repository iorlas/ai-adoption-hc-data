# Exercise — one real prompt, in your window

**4 minutes.** Straight after the game.

---

> **Who does what:** **▸ We run it first, then you** — watch, then repeat it ·
> **▸ Your turn** — you drive, we are on the floor · **▸ Together** — whole room,
> out loud. Nothing here is a test.

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
