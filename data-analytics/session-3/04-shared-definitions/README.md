# 4 — One definition, shared across the team

**40 minutes, hands-on · Claude Code + a shared Markdown file (`CLAUDE.md`) + SQL**

## The problem, in your words

Lucie:

> "Are there shared prompts, or MD files we could share as a team, so
> everyone's using the same SQL?"

Lauren:

> "Say I have active members — making sure I'm using the same definition across
> different dashboards."

Same problem, two teams. This part builds the answer.

## The situation you are walking into

There are two reports in `reports/`. Both are real, both are in use, both report
**active supporters**, and they disagree:

| Report | Active supporters |
|---|---|
| Fundraising Summary | 2,447 |
| Supporter Engagement | 1,832 |

A gap of 615 people. There has been an unresolved email thread about it since
March.

**Neither report is lying.** They are answering different questions, both of
which are reasonable, and neither of which is written down anywhere. And there
is a third number available that neither of them reports, and a fourth that only
appears once you have done part 2 of this session.

## Why writing it down is the fix

You could resolve this in a meeting, and in a month it would drift again,
because the definition would live in someone's memory and someone else's DAX.

Writing it into a file the whole team shares does three things at once:

1. **Your colleagues** can read it — it is the documentation that did not exist.
2. **Claude reads it too.** Next time anyone in your team asks Claude for
   "active supporters", it uses your definition rather than inventing a
   plausible one.
3. **It is versioned.** When it changes, you can see when and why.

This is the same idea as curating definitions in a Genie space, except that it
lives in your own files, costs nothing, and works for both teams.

## Keeping AI honest, generally

This part is also where we cover the general case. A thin `CLAUDE.md` is the
reason Claude guesses. Watch what happens: with the file thin, ask it for active
supporters and it will pick a definition and sound confident. With the file
filled in, it uses yours and says which rule it applied.

That is the whole mechanism behind "stopping it inventing business rules". It is
not a clever prompt. It is that the rule was written down where it could find
it.

**And the tell to watch for:** an answer that uses a business term without
saying which definition it used. Every time. That is your cue to ask.

## One warning before you write anything

Once you know Claude reads `CLAUDE.md`, the instinct is to put everything in it.
Do that and within a month it is four hundred lines, every conversation is
slower, and nobody reads it — because **it is read on every single message.**

So this segment includes a five-minute sorting game, out loud, on what belongs
in `CLAUDE.md` and what belongs one pointer away: **[`game.md`](game.md)**.

Getting that split wrong is the most common way a team's first `CLAUDE.md`
becomes useless within a quarter, and it costs five minutes to avoid.

## What you leave with

Three things, in three different places on purpose:

| Artifact | Where | Why there |
|---|---|---|
| The full definitions, with SQL and DAX | `docs/measure-definitions.md` | Depth. Read only when a task needs it |
| A short pointer plus the hard rules | `CLAUDE.md` | Paid for on every message — keep it small |
| The decision, and what you rejected | `docs/decisions/0001-*.md` | Stops the argument restarting in March |

Plus the before-and-after answer, side by side, which is the part that makes the
whole thing land.

→ **`exercise.md`**
