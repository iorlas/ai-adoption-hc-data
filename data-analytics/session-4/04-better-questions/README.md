# 4 — Asking better questions of your data

**35 minutes, hands-on · Claude Code + SQL**

## The line, and we agree with it

Lauren:

> "We'd prefer to use Claude more for the coding side of things, and the
> analysis should be primarily done by analysts themselves."

So this is **not** AI doing your analysis. It is you having a hypothesis and
getting to a trustworthy answer with less typing. The judgement stays yours. The
typing does not.

## What the division of labour actually is

| You | Claude |
|---|---|
| Decide what is worth asking | Writes the SQL |
| Say what would change your mind | Runs it, shows the result |
| Read the query and check it answers your question | Reshapes it when you say it did not |
| Decide whether the answer is real or an artefact | Enumerates the alternatives you have not tried |
| Say what it means | — |

The row that matters is the fourth. **"Is this real, or is it an artefact of how
I asked?"** is the question that separates an analyst from a query.

## The failure mode to watch

You ask a question, get a number, and it confirms what you expected. You move
on. Nobody checks a comfortable answer.

The habit that fixes it is cheap: before you look at the result, say out loud
what would make you disbelieve it. Then check that thing first.

This session's data gives you plenty of material — after Monday you know the
duplicates, the orphans, the impossible dates and the typo are all in there, and
every one of them can produce a comfortable-looking wrong answer.

## The specific trap in this dataset

Anything you compute per-supporter is affected by the duplicate people. Anything
you compute per-campaign is affected by the donations pointing at campaigns that
do not exist. Anything time-based is affected by the impossible dates.

None of those will make an answer look obviously wrong. They will make it look
slightly different from the truth, which is much harder to catch — and is why
the first move on any real question is *"what in this data could make this
answer wrong?"*

## What you leave with

Working queries against the shared dataset, a clearer sense of where that line
between your judgement and the tool sits, and the habit of asking the one
question a wrong answer cannot survive.

→ **`exercise.md`**
