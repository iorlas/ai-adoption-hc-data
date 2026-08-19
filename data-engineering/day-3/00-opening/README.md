# 0 — Opening

**5 minutes, watch only**

> **Who does what:** I talk, you listen. Questions out loud whenever you like.

## Where we got to

Day 1 ended on one habit: **you own the answer, so you check it.** Five tells
for a wrong answer, and a verification log.

Day 2 ended on the reason wrong answers happen: **the model was missing context
you never wrote down.** So you wrote it down — a `CLAUDE.md`, a data dictionary,
a glossary, a reference implementation — and the same prompt got visibly better
at the end of the day than at the start.

Both of those were on things you can open in an editor: a CSV, a stored
procedure.

## What today changes

Nothing about the habits. Everything about **where the work lives**.

```
                  you can open it        you cannot
                  in an editor           open it in an editor
                  ---------------        --------------------
  Day 1           donor.csv
  Day 2           the stored proc        (the database, via MCP)
  Day 3           the notebook file      the cluster it runs on
                  the pipeline JSON      the ADF runtime that executes it
  Day 4                                  the workspace itself
```

The left-hand column is the useful surprise: **a Databricks notebook is a file,
and an ADF Mapping Data Flow is a JSON file.** Almost everything you want AI to
do with them needs no connection at all — which is why today is hands-on for
every one of you, whatever your access looks like.

The right-hand column is real too, and it is Day 4.

## The shape of today

Three working parts, one break, and all three are yours.

- **Part 2** — an inherited profiling notebook, grown by copy-paste. You cluster
  the repetition into a module you would actually adopt.
- **Part 3** — a pipeline none of us wrote: eleven activities, no documentation,
  published in 2024 by somebody who has left. You read it, then work out which
  half of the explanation you believe.
- **Part 4** — the big one. A legacy Mapping Data Flow, converted to SQL, with a
  parity check that either goes green or does not. This part contains the honest
  bit: three things in that flow have no clean SQL equivalent, and I want you to
  find them rather than be told.

Parts 3 and 4 are one arc: **read a pipeline, then convert one.** Converting
something you have not read is a rewrite with extra confidence.

**Nothing today needs a Databricks workspace.** Everything with a live
connection in it — the workspace, the CLI, Genie — is Day 4, together, so that
one setup serves the whole of it. Today is the two things you asked for in June,
with the most time on the clock either has had.

## One thing to hold onto

> **Today's two headline goals are the two you asked for in June:** notebooks
> into reusable functions, and Mapping Data Flows into SQL. They are parts 2 and
> 4, and everything else today is in service of them.
