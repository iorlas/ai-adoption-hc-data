# 2 — Genie, from the builder side

**25 minutes, watch only**
*5 min why it is your job · 8 min the space, badly and then well · 7 min the same question to both tools · 5 min the game.*

> **Who does what:** I run it, you watch — nothing to type. The **▸ Together**
> moment is the game at the end. Questions out loud whenever you like.

**Nobody needs Databricks access.** This runs on my workspace, with a schema of
the same synthetic donor data you have been working on all week.

## Why a data engineer should care about Genie

Genie answers plain-English questions over your warehouse. The demo is easy and
slightly boring, and it is not the point.

The point is this: **Genie's answers are only as good as the metadata you
maintain.** Table comments, column comments, the definitions someone curates in
the space. Which means that when an analyst asks Genie a question and gets a
wrong number, the fix is not in Genie.

```
   analyst asks a question
            │
            ▼
   Genie writes SQL  ◄──── reads: table + column comments, curated
            │                     definitions, example queries
            ▼                     ─── all of it maintained by YOU
   a number on a screen
```

That is a new kind of ticket for your team, and it is worth seeing before it
arrives.

## What we run

**Scene.** Two windows on my screen. **Left:** a browser on my Databricks
workspace, in a Genie space whose only tables are the donor registry ones you
have seen all week. **Right:** Claude Code in the `data-engineering/` folder,
fresh conversation, connected to the same workspace as in part 1.

Same data both sides. Only the tool differs.

### First, the space with bad metadata

One question, into a space where the tables are loaded and nothing is
documented:

> How many active donors do we have?

Watch what it does with `status`. There are five values in that column and one
of them is a typo — Genie has no way to know that, because nobody told it.

### Then, the same space with the metadata fixed

Three things change, and each one takes a minute:

1. **A table comment** — what `donor` is, and its grain (one row per registered
   donor).
2. **A column comment on `status`** — the four valid values, and the note that
   `Activ` is a known defect.
3. **A curated definition in the space** — "active donor" means
   `status = 'Active'`, and here is the SQL.

Then the same question again.

> **This is the whole segment.** The difference between the two answers was not
> made by Genie, or by a better prompt. It was made by three lines of metadata
> that a data engineer wrote.

## Genie and Claude Code, side by side

The same question, word for word, into both:

> Which columns in the donor table contain values that do not belong to the
> column's vocabulary, and how many rows are affected?

Two things to watch:

1. **Do they get the same number?** Where they differ, ask which one made an
   assumption it did not mention.
2. **What did each need to be told first?** Genie needed a curated space.
   Claude Code needed a pointer at the files — and it can also read the pipeline
   that *created* the bad values, which Genie cannot see at all.

## The honest comparison

| | Databricks Genie | Claude Code |
|---|---|---|
| Knows your schema | Yes, automatically | No — you point it at files, or at the CLI |
| Where the data is | Stays in the warehouse | Wherever you point it |
| What it produces | SQL and a result, in the browser | SQL, a result, **and files it writes for you** |
| Sees the rest of your work | No | Yes — the notebook, the pipeline JSON, your `docs/` |
| Curated definitions live in | the Genie space | `CLAUDE.md` and `docs/` |
| Who can use it | anyone with warehouse access | anyone with the repo on their laptop |
| Who maintains it | **you** | **you** |

**Genie is better when the question is entirely inside a warehouse you have
already curated. Claude Code is better when the answer needs something that is
not in the warehouse** — the pipeline behind the column, the flow that dropped
twenty rows, last week's decision record.

Today's question was the second kind. Yesterday's twenty `Activ` rows are
invisible from inside the warehouse; the reason for them is a filter in a JSON
file, and no amount of curating the warehouse would ever surface it.

## The transferable idea

> **Both tools answered by writing a query.** Neither read your rows into a
> model. The difference is what each one already knows about your world — and
> both are fixed the same way: **write the definitions down where the tool will
> find them.** For Genie that is metadata and a curated space. For Claude Code
> it is `CLAUDE.md` and `docs/`. It is the same job twice.

## The game

**▸ Together, out loud.** [`game.md`](game.md) — five questions, and which tool
you would point each one at.

## If you want it on your own workspace

Say so in the close. A Genie space over one curated schema is a small piece of
work and it is the fastest way to show your analysts what good metadata buys
them.
