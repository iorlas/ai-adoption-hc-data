# 3 — Find the weak spots

**20 minutes, hands-on · Claude Code + Azure Data Factory pipeline definitions**

This is the *"finding places where they might not be robust"* part of your ask,
and it is the one that pays off at 3am.

## The question

Not "is this good code". The question is narrower and much more useful:

> **What happens when something upstream changes, and how would we find out?**

Sources change. A column gets renamed, a file arrives empty, a type changes, a
supplier adds a field. The pipelines that hurt are not the ones that fail — a
failure sends an alert. The ones that hurt are the ones that **succeed while
producing the wrong answer.**

## Three grades of failure, worst last

1. **It fails loudly.** Someone gets paged, someone fixes it. Annoying, fine.
2. **It fails and nobody is told.** Worse: the dashboard shows last week's
   numbers and everyone believes them.
3. **It succeeds with the wrong data.** Worst by a long way. Nothing alerts,
   the numbers look plausible, and it may be months before anyone notices — if
   anyone ever does.

Category 3 is where you should spend the twenty minutes, and this pipeline has
several. Something that silently replaces a missing value with a default. A
schema setting that means an upstream column change reshapes the output without
complaint. A step that empties a table before it knows the replacement data is
good.

Ask of every step: **if this went wrong, would anybody know?**

## Why Claude is genuinely useful here

Not because it knows more about ADF than you do. Because this analysis is
tedious, mechanical and easy to lose your place in — ten activities, seven
datasets, a data flow, and you have to hold "what if this input were wrong" in
your head at each one.

It enumerates. You judge which ones matter for your data and your alerting.
Same division of labour as everything else this week.

## What you leave with

A ranked list of weak spots in a pipeline nobody had ever documented, in the
documentation you wrote twenty minutes ago — and a set of questions you can ask
of the next inherited pipeline.

→ **`exercise.md`**
