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
  Day 3                                  a Databricks workspace
                  the notebook file      the cluster it runs on
                  the pipeline JSON      the ADF runtime that executes it
```

The middle column is the useful surprise: **a Databricks notebook is a file, and
an ADF Mapping Data Flow is a JSON file.** Most of what you want AI to do with
them needs no connection at all. The connection matters for exactly two things
today, and I will be the one holding it.

## The shape of today

Four working parts, one break.

- **Part 2** — I connect Claude Code to a real workspace, so you see what the
  live path looks like and what it costs to set up. Watch only.
- **Part 3** — an inherited profiling notebook, grown by copy-paste. You cluster
  the repetition into a module. **Hands-on, no workspace needed.**
- **Part 4** — the big one. A legacy Mapping Data Flow, converted to SQL, with a
  parity check that either goes green or does not. **Hands-on, no workspace
  needed.** This part contains the honest bit: three things in that flow have no
  clean SQL equivalent, and I want you to find them rather than be told.
- **Part 5** — Genie, from the builder side. Not "look, natural language" — the
  point is that Genie is only as good as the metadata *you* maintain.

## One thing to hold onto

> **Today's two headline goals are the two you asked for in June:** notebooks
> into reusable functions, and Mapping Data Flows into SQL. They are parts 3 and
> 4, they are back to back, and they have the most time on the clock.
