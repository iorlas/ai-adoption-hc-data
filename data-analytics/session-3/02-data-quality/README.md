# 2 — Data quality: what is wrong, how much, and what would catch it

**30 minutes, hands-on · Claude Code + SQL**
*8 min we demo · 17 min you do it · 5 min we compare answers.*

> **Who does what:** **▸ We run it first, then you** — watch, then repeat it ·
> **▸ Your turn** — you drive, we are on the floor · **▸ Together** — whole room,
> out loud. Nothing here is a test.

## Why this one is first

It was your top ask in June, and it is the foundation for everything else today.
In part 4 you will find two reports disagreeing about how many active supporters
there are. One of the reasons will be sitting in this exercise.

We do it **in SQL, not Python**, because SQL is what most of your people use
every day.

## The principle — the generator is cheap, the judgement is the value

Ask Claude for data-quality rules and it will happily give you thirty. Getting
thirty rules is not the skill. **Keeping the six that matter and rejecting the
rest is the skill.**

A rule that fires on healthy data is worse than no rule at all, because it
teaches everyone to ignore the alerts. Within a month nobody reads them, and the
one real failure goes past unnoticed.

So the question to ask of every candidate rule is:

> **Does violating this mean the data is actually wrong for how we use it — or
> is it just different from how I would have typed it?**

Postcodes written `m19bh` instead of `M1 9BH` are not wrong. A supporter whose
`status` says `Activ` **is** wrong, and it is quietly shrinking a number
somebody reports to a trustee board.

---

# The exercise

Open Claude — desktop app or terminal, whichever you settled on — with this
repository folder as your project. Start each prompt fresh in the same
conversation; Claude keeps the context.

## Step 1 — Profile the data (~6 min)

**▸ We run it first, then you.**

> Profile `data/supporters.csv` and `data/donations.csv` using DuckDB SQL.
> For every column tell me: how many rows, how many are blank, how many distinct
> values, and for the text columns the five most common values. Show me the SQL
> you ran, then the results.

**What you should see.** Row counts of **4,022** supporters and **12,376**
donations. If you get different numbers, stop and tell us — you are on different
data from everybody else, which is exactly the failure this whole shared-dataset
idea exists to prevent.

**The one thing to actually look at:** the `status` column. Read its distinct
values, not the summary sentence Claude writes about them.

> Give me the full `value_counts` for `supporters.status` — every distinct
> value with its row count, no summarising.

If you asked for a summary you might have been told there are four statuses.
There are five. One of them is a typo — and it is quietly removing people from
every report in the building that filters on Active.

**That is two of the five tells** from
[`reference/checking-the-answer.md`](../../reference/checking-the-answer.md):
an all-clear with no exceptions named, and an answer too clean to be true. Keep
that page open — you will use three of them in this exercise alone.

## Step 2 — Make it find the defects (~5 min)

**▸ We run it first, then you.**

> Find data-quality problems in these files. For each one: what the problem is,
> the SQL that finds it, and the number of rows affected. Look at least for
> impossible dates, records that reference something that does not exist,
> duplicates, and values that do not belong to their column's vocabulary.

Then challenge it — this is the important half:

> For each problem you just listed, show me five actual example rows.

**Why.** An answer with no exceptions named is the single most common way a
confident wrong answer gets through. Real checks name their exceptions. If it
cannot show you the rows, it did not run the check.

**A rough sense of what is there**, so you know whether you have found it: a
status typo in the tens of rows, duplicate people in the tens, donations
pointing at supporters who do not exist in the tens, impossible dates in the
single figures to low tens, and a few dozen duplicated gifts. If Claude reports
a defect in the thousands, ask it to prove that one first.

## Step 3 — Turn findings into rules, then throw most of them away (~6 min)

**▸ Your turn.**

> From what you found, propose data-quality rules for these files. One per line:
> the column, the check as a SQL predicate, and one sentence on why a violation
> matters.

Now do the part that is yours, not Claude's. Go down the list and sort every
rule into **meaningful** or **noise**, using the test above: *would a violation
mean the data is wrong for how we use it?*

Some of them will be noise. Postcode formatting is the obvious one. Marketing
consent set to 0 is a lawful choice, not a defect. Supporters with no donations
are normal.

`docs/data-quality-rules.md` already exists with the headings in place — you are
filling it in, not starting from a blank page.

> Fill in `docs/data-quality-rules.md`. Keep only these rules: [list them]. For
> each: the table, the SQL predicate, the count of rows currently failing, and
> one sentence on why a violation matters. Then fill the "Rejected" table with
> the rules I threw out and one line each on why they are noise. Leave the
> headings as they are.

Six kept rules is a good target. Twenty is a list nobody will read.

If you want to see what a finished one looks like — a different organisation, so
it does not hand you today's answers — `templates/example-library/docs/` has one.
**After you write yours, not before.**

## Step 4 — Then the game

**▸ Together, out loud.** [`game.md`](game.md) — six proposed rules, keep or bin.

Before we play it, have `docs/data-quality-rules.md` open on screen, and be able
to answer these two:

1. Name one rule you **rejected**, and why it would have been harmful to keep.
2. How many supporters have `status = 'Active'`? And how many *should*?

We compare answers across the room before moving on. If two people got different
numbers, that is the most interesting five minutes of the session — we will not
let it slide.

---

## One thing worth noticing about how it answered

When Claude answers a question about the data, it does it by **writing a SQL
query and running it**. The rows come back to your machine. The model read your
*schema*, not your supporters.

That is the boundary worth understanding precisely rather than vaguely — it is
why a version of this is usable on real data one day. Not today: today is
synthetic and stays synthetic.

## What you leave with

`docs/data-quality-rules.md` — the rules you decided were worth keeping, written
as something you could actually run. Plus a shorter list of the ones you
rejected, and why. **The rejected list is the more interesting half.**

---

## If it goes wrong

**Claude writes Python instead of SQL.** Say so: *"use DuckDB SQL over the CSVs,
not pandas."* `CLAUDE.md` already says this, but it is thin today and gets
overridden. Part 4 is where you fix that properly.

**A query fails on a date comparison.** The CSV columns are text until you cast
them. `CAST(sign_up_date AS DATE)` — and it is fair to just paste the error back
to Claude and let it fix its own query.

**It says the data is clean.** It ran on something else, or it summarised
without checking. Ask for `value_counts` and for failing rows.
