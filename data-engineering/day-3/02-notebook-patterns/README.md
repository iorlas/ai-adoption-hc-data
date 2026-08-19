# 2 — An inherited notebook, and the module hiding inside it

**35 minutes, hands-on**
*5 min read it · 10 min find the clusters · 15 min build the module · 5 min the equivalence argument.*

> **Who does what:** **▸ We run it first, then you** on step 1, then
> **▸ Your turn** for the rest. No workspace needed — this is a file on your
> laptop.

## Why it is here

Adrian's June ask, close to verbatim: *profile Databricks notebooks into
reusable functions.* This is that, on a notebook shaped like the ones that
actually accumulate: **written once per column, by copy-paste, by three
different people, over two years.**

Nobody wrote it badly. It grew.

## What we are working on

**Scene.** One window: Claude Code, in the `data-engineering/` folder, a fresh
conversation. One file in play:

```
later-days/notebooks/donor_profiling.py
```

120 lines, a Databricks notebook in source form (`# COMMAND ----------`
separates the cells). It profiles the `donor` table: null counts, distinct
counts, some standardisation, one business rule. **You cannot run it** — there
is no Spark on your laptop and no workspace for most of you. That is fine, and
it is also the point: everything valuable here is done by reading.

## Step 1 — read it before you refactor it

**▸ We run it first, then you.**

> @later-days/notebooks/donor_profiling.py — describe what this notebook does,
> cell by cell, in one line per cell. Do not suggest any improvements yet.

Then check it yourself against the file. **This is the Day-1 habit and it is not
optional here**, because everything you do next is built on this description
being right.

## Step 2 — find the clusters, and do not accept the first answer

**▸ Your turn.**

> In that notebook, group the cells into clusters of near-duplicate logic. For
> each cluster: what varies between the copies, and what stays the same?

You are looking for the thing that varies — that is your function parameter.

Push back once, whatever it says:

> Are any of those clusters actually two different jobs that happen to look
> alike? I would rather have four honest functions than three that need a flag.

That second prompt is the whole skill. A model asked to find repetition will
find repetition, including where there is none. **Merging two things that were
never the same is how a "reusable" module becomes the thing nobody reuses.**

## Step 3 — build the module

**▸ Your turn.**

> Write `day-3/02-notebook-patterns/profiling.py`: one function per cluster,
> each taking the DataFrame and the column name(s) as arguments, each with a
> docstring saying what it returns. Pure functions — no `display`, no printing
> inside them, nothing that assumes a notebook. Then show me the notebook
> rewritten to import and call them.

Three constraints in that prompt, and each one is there for a reason:

| Constraint | Why |
|---|---|
| **Returns, does not print** | A function that prints can only be used by a human watching. One that returns can be tested, joined, or written to a table |
| **No `display`** | `display` is Databricks-only. The moment it is in your module, the module is Databricks-only |
| **Docstring says what it returns** | It is the cheapest documentation that survives, and the next person's model reads it |

## Step 4 — the equivalence argument

**▸ Your turn.** This is the step people skip, and it is the deliverable.

> Give me a table: notebook cell → the function that replaces it → anything that
> could now behave differently. Be specific about ordering, nulls, and types. If
> nothing differs for a row, say so explicitly.

**Be honest with yourself about this part: there is no green check here.** You
cannot run either version. What you have instead is an argument you would be
willing to show a reviewer — which is exactly the situation you are in at work
when the notebook takes forty minutes to run against production.

Then have it reviewed:

```
/code-review
```

## Step 5 — write it down

**▸ Your turn.**

> Add a section to `data-engineering/docs/notebooks.md` — what `donor_profiling` is for, what
> `profiling.py` now provides, and the one thing you would still not trust it
> with.

## What you should have

- `day-3/02-notebook-patterns/profiling.py` — four to six functions, docstrings, no printing
- A rewritten notebook that reads as a list of questions instead of a wall of blocks
- The equivalence table
- A `docs/` entry the next person finds before they copy-paste the block again

## One thing to notice on your way out

Somewhere in that notebook is a line that would put several thousand donors'
names, dates of birth and NHS numbers on a screen — and it is not a mistake
anyone would flag in review, because everybody writes it.

If you found it, say so. If not, it is the first thing in the answer key.
