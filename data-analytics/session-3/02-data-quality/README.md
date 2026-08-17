# 2 — Data quality: what is wrong, how much, and what would catch it

**30 minutes, hands-on · Claude Code + SQL**
*8 min we demo · 17 min you do it · 5 min we compare answers.*

> **Who does what:** **▸ We run it first, then you** — watch, then repeat it ·
> **▸ Your turn** — you drive, we are on the floor · **▸ Together** — whole room,
> out loud. Nothing here is a test.

## Why this one is first

Your top ask in June, and the foundation for the rest of the day. In part 4 two
reports disagree about active supporters — one reason is sitting in this
exercise.

**In SQL, not Python**, because SQL is what most of your people use every day.

## The principle — the generator is cheap, the judgement is the value

Ask Claude for data-quality rules and it will give you thirty. **Keeping the six
that matter is the skill.**

A rule that fires on healthy data is worse than no rule.
In a month nobody reads the alerts, and the real failure walks past.

So, of every candidate rule:

> **Does violating this mean the data is actually wrong for how we use it — or
> is it just different from how I would have typed it?**

Postcodes written `m19bh` instead of `M1 9BH` are not wrong. A supporter whose
`status` says `Activ` **is** wrong, and it is shrinking a number somebody
reports to a trustee board.

---

# The exercise

Open Claude with this repository folder as your project. Keep one conversation;
Claude keeps the context.

## Step 1 — Profile the data (~6 min)

**▸ We run it first, then you.**

> Profile `data/supporters.csv` and `data/donations.csv` using DuckDB SQL.
> For every column tell me: how many rows, how many are blank, how many distinct
> values, and for the text columns the five most common values. Show me the SQL
> you ran, then the results.

**What you should see: 4,022** supporters and **12,376** donations. Different
numbers means you are on different data from everybody else — stop and tell us.

**The one thing to actually look at:** the `status` column. Read its distinct
values, not Claude's summary of them.

> Give me the full `value_counts` for `supporters.status` — every distinct
> value with its row count, no summarising.

A summary might say four statuses. There are five. One is a typo — quietly
removing people from every report that filters on Active.

**That is two of the five tells** from
[`reference/checking-the-answer.md`](../../reference/checking-the-answer.md):
an all-clear with no exceptions named, and an answer too clean to be true. Three
of them come up in this exercise alone.

## Step 2 — Make it find the defects (~5 min)

**▸ We run it first, then you.**

> Find data-quality problems in these files. For each one: what the problem is,
> the SQL that finds it, and the number of rows affected. Look at least for
> impossible dates, records that reference something that does not exist,
> duplicates, and values that do not belong to their column's vocabulary.

Then challenge it — the important half:

> For each problem you just listed, show me five actual example rows.

**Why.** An answer with no exceptions named is the most common way a confident
wrong answer gets through. If it cannot show you the rows, it did not run the
check.

**A rough sense of what is there**, so you know when you have found it:

- a status typo — tens of rows
- duplicate people — tens
- donations pointing at supporters who do not exist — tens
- impossible dates — single figures to low tens
- duplicated gifts — a few dozen

If Claude reports a defect in the thousands, make it prove that one first.

## Step 3 — Turn findings into rules, then throw most of them away (~6 min)

**▸ Your turn.**

> From what you found, propose data-quality rules for these files. One per line:
> the column, the check as a SQL predicate, and one sentence on why a violation
> matters.

Now the part that is yours, not Claude's. Sort every rule into **meaningful** or
**noise**: *would a violation mean the data is wrong for how we use it?*

Some are noise. Postcode formatting. Marketing consent set to 0 is a lawful
choice, not a defect. Supporters with no donations are normal.

> Fill in `docs/data-quality-rules.md`. Keep only these rules: [list them]. For
> each: the table, the SQL predicate, the count of rows currently failing, and
> one sentence on why a violation matters. Then fill the "Rejected" table with
> the rules I threw out and one line each on why they are noise. Leave the
> headings as they are.

**Six kept rules is a good target. Twenty is a list nobody will read.**

A finished example, for a different organisation, is in
`templates/example-library/docs/`. **After you write yours, not before.**

## Step 4 — Then the game

**▸ Together, out loud.** [`game.md`](game.md) — six proposed rules, keep or bin.

Have `docs/data-quality-rules.md` on screen, and be able to answer:

1. Name one rule you **rejected**, and why keeping it would have been harmful.
2. How many supporters have `status = 'Active'`? And how many *should*?

If two people got different numbers, that is the most interesting five minutes
of the session.

---

## One thing worth noticing about how it answered

Claude answered by **writing a SQL query and running it**. The rows came back to
your machine. The model read your *schema*, not your supporters.

That boundary is why a version of this is usable on real data one day. Not
today.

## What you leave with

`docs/data-quality-rules.md` — the rules worth keeping, written as something you
could run, plus the ones you rejected and why. **The rejected list is the more
interesting half.**

---

## If it goes wrong

**Claude writes Python instead of SQL.** Say *"use DuckDB SQL over the CSVs, not
pandas."* `CLAUDE.md` says this, but it is thin today and gets overridden.

**A query fails on a date comparison.** The CSV columns are text until you cast
them. `CAST(sign_up_date AS DATE)` — or paste the error back and let it fix its
own query.

**It says the data is clean.** It ran on something else, or summarised without
checking. Ask for `value_counts` and for failing rows.
