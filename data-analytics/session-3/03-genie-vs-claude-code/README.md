# 3 — Genie and Claude Code, side by side

**5 minutes, watch only · Databricks Genie vs Claude Code**
*2 min framing · 3 min the same question into both, on our workspace.*

> **Who does what:** we run it, you watch — there is nothing for you to type.
> The one **▸ Together** moment is the game at the end. Questions out loud
> whenever you like.

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

> **Notice that both of them answered by writing a query.** Neither read your
> rows into a model. The difference is what each one already knows about your
> world — and both let you fix that the same way: by writing the definitions
> down where the tool will find them.

Which is exactly what the next part of the session does.

## The question to hold onto

**Which of the two would you reach for on the thing you just did in data
quality, and why?** Your reason matters more than your pick.

**▸ Together, out loud.** [`game.md`](game.md) — five questions, and which tool
you would point each one at.

## Note for the room

There is nothing for you to run in this part. Watch, ask questions, and tell us
if it changes where you would use which. If you want Genie properly — as a
hands-on session on your own workspace — say so in the close, and we will scope
it.

---

## Before the break — load Power BI

This part ends the morning, so this is the moment to get Power BI ready. The
full version is in [`setup.md`](../01-prompt-refresher/setup.md); the short one:

> Open Power BI Desktop — dismiss the sign-in form if you get one, you do not
> need to sign in. Then **Get data → Text/CSV** and **Load** the five files from
> `data/`, one at a time, about three minutes. Then stop. No relationships, no
> measures — we build the model together straight after.

Three questions come up almost every time:

- **"Do I need a new workspace?"** No. Workspaces are Power BI *Service*, for
  publishing. Everything today is a file on your own laptop, and you do not need
  to sign in to Power BI at all.
- **"Where do I create the file?"** In the Power BI window. If it opens on the
  Home screen, **New → Report**; otherwise the blank canvas is already the new
  report. Not in VS Code — a `.pbix` is a binary file, nothing else makes one.
- **"Which folder do I save it in?"** Anywhere you will find it again. If your
  save dialog offers **Power BI Project (.pbip)** you have the preview feature
  on — pick **.pbix**.

## If it goes wrong

Every rough edge we know about in the Power BI load — the sign-in prompt, a
dialog you cannot close, columns that all arrive as Text, a date column full of
errors, and why **Get data → Folder** gives you nonsense — is in
[`quirks.md`](../../quirks.md), with the fix.

**If a fix does not work in thirty seconds, say so and pair with a neighbour.**
