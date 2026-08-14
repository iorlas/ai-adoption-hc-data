# 2 — Genie and Claude Code, side by side

**15 minutes, watch only · Databricks Genie vs Claude Code**

**Nobody needs Databricks access for this.** We run it on our own workspace
while you watch. Nothing is required from Lucie's team, and there is no token to
set up.

## Why it is here

Lucie raised Genie herself on the August call. Rather than leave it as a
mention, we put **the same data-quality question into both tools** and look at
the two answers together — on the first day, not the second.

## The point is not which one wins

They are trustworthy in **different ways**, and knowing which to reach for is
the actual skill.

| | Databricks Genie | Claude Code |
|---|---|---|
| Knows your schema | Yes, automatically | No — you tell it, or it reads the files |
| Where the data is | Stays in the warehouse | Wherever you point it: files, CSVs, a warehouse |
| What it produces | A SQL query and a result, in the browser | A query, a result, *and* a file it writes for you |
| Sees the rest of your work | No | Yes — the reports, the pipeline JSON, your notes |
| Curated definitions | You configure them in the Genie space | You write them in `CLAUDE.md` |
| Who can use it | Anyone with warehouse access | Anyone with the folder on their laptop |

The honest summary: **Genie is better when the question is entirely inside a
warehouse you have already curated. Claude Code is better when the answer needs
context that is not in the warehouse** — the pipeline that produced the column,
the definition another team uses, the report that disagrees.

Today's data-quality question is a good example of the second kind, because half
of what makes a defect a defect lives in *how the data is used*, not in the
data.

## What we run

The same question, in both:

> Which columns in the supporter table have values that do not belong to the
> column's vocabulary, and how many rows are affected?

Watch two things:

1. **Do they get the same number?** Not always — and where they differ, ask
   which one made an assumption.
2. **What did each need to be told first?** Genie needs a curated space.
   Claude Code needed us to say "use SQL, not Python" and to point it at the
   files.

## The transferable idea

Both tools are answering by **writing a query**. Neither is reading your rows
into a model. The difference is what each one already knows about your world —
and both of them let you fix that, in the same way: by writing the definitions
down where the tool will find them.

Which is exactly what the next part of the session does.

## Note for the room

There is no exercise file for this part because there is nothing for you to run.
Watch, ask questions, and tell us if it changes where you would use which. If
you want Genie properly — as a hands-on session on your own workspace — say so
in the close, and we will scope it.
