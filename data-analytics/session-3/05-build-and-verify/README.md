# 4 — Build a report, then prove it is right

**55 minutes, hands-on · Claude Code + Power BI Desktop — DAX, Power Query M,
your normal `.pbix`**

One continuous piece of work, not two. Build first, then interrogate what you
built.

## Why both halves

Lauren, on the August call:

> "If we take the concept of being able to ease out either some of the query
> writing or some of the building of the dashboard, then I think that's where I
> see an AI tool like Claude being helpful."

Lucie, on the same call:

> "What I would want the training to focus on would be not necessarily how to
> get AI to make the dashboard, but what would we need to do to make sure it was
> all correct and accurate and appropriate? … I need to be able to stand up in
> front of my stakeholder and explain how it works and how the numbers are
> derived."

Those are not in conflict. They are one segment: **if it builds, teach me how to
know it is right.** A first pass you cannot defend is worth nothing.

## Two things we will not do

Both because they did not work in July, and both worth saying out loud so you
know we heard it:

- **We will not pitch this on speed.** You do not have clients, you do not have
  short deadlines, and you want to do things thoughtfully and correctly. "It's
  faster" is not an argument that means anything to you.
- **We will not demonstrate anything by recolouring charts.** You have locked
  custom branding. That demo was never about your work.

Where this does earn its keep: when a dataset is wide enough that nobody can
hold it all in their head, and the boring part is not deciding what to show, it
is writing the twelfth measure correctly.

## First — squaring this with July

In July the hinge of the whole first day was **PBIX versus PBIP**: the idea that
a dashboard can be *text* you can read, edit and diff. It landed, it went
unchallenged, and everything else that day hung off it.

Then in Session 4 we say plainly that Claude cannot open your `.pbix`. Those two
things sound like a contradiction, so here is the honest version, in one place:

**July was right.** PBIP is a real format, it is genuinely text, and everything
demonstrated on it was real. Nothing about that has been withdrawn.

**You are on `.pbix` today, and we are not asking you to migrate.** Moving a
team's reporting to PBIP is a decision with real costs — source control,
process, everybody's habits — and it is not this workshop's decision to make.
It is a door, not a requirement, and it is still open whenever you want it.

**So the loop that works on Monday morning is copy out, ask, paste back.** Less
elegant than "point it at the project folder", and it is what actually works
with the files you have today. Everything in this segment is built for the
format you are actually on.

## The boundary, precisely

**Claude cannot open a `.pbix`.** It is a binary — a zip of compressed model
data. Pointing Claude at one gets you nothing.

What it *can* do is everything in the layer underneath:

| Claude does this | You do this |
|---|---|
| Writes the Power Query M | Pastes it into the Advanced Editor |
| Writes the DAX measures | Pastes them in, checks them |
| Proposes the model — tables, relationships, direction | Builds it |
| Says which visual answers the question, and why | Places the chart |
| Reads a measure you paste back and tells you what it actually computes | Decides whether that is what you wanted |

Knowing what to hand it is part of the skill, and it is part of this exercise.
The working loop is: **copy out, ask, paste back.** Unglamorous, and it is the
whole of what makes this useful on Power BI work.

## What you leave with

A first-pass report you built, and then verified — against the definition you
agreed before the break, and against the two reports that already exist. Plus a
pre-launch check you can repeat.

→ **`exercise.md`**
