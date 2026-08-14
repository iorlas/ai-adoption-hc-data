# 2 — Document it, for the colleague who inherits it next

**30 minutes, hands-on · Claude Code + Azure Data Factory pipeline definitions**

## The gap you described

> "Some of them are enormous and none of us made them and the documentation is
> very weak."

The reason pipeline documentation does not get written is not laziness. It is
that writing it requires understanding the pipeline first, and understanding it
takes half a day, and by the time you have understood it you have solved the
problem you actually came for and moved on.

You just did the understanding part in twenty-five minutes. So the documentation
is now nearly free — it is the **residue of the work you already did**, not a
separate task.

## What makes documentation worth having

Not a diagram nobody updates. Not a paragraph saying "this pipeline loads
supporter data" — anyone can see that from the name.

The test: **could a colleague, at 3am, with this document and no access to you,
work out what is wrong?**

That means it has to contain the things that are not obvious from the JSON:

- What it is *for*, in business terms
- The order, and what breaks if a step fails partway
- Every baked-in decision, named, with the date and reason where known — and
  "reason unknown" written explicitly where it is not
- Where each output column comes from
- What it depends on upstream, and what depends on it downstream
- What to do when it fails at 2am on a Monday

## Where it lives

Next to the pipeline, in the same repository, in version control. Not in
Confluence where it will rot separately from the thing it describes, and not in
a document in someone's OneDrive.

Two reasons. The obvious one: it is where the next person will look. The less
obvious one: **it is where Claude will look.** Documentation next to the code is
context for every future conversation about that code. You are not just writing
for humans — you are building the thing that makes the next question cheaper to
answer.

That is the same mechanism as yesterday's `CLAUDE.md`, applied to a pipeline
instead of a measure.

## The honest caveat

Claude will write documentation that is fluent and mostly right, and will state
inferences as facts. **You must read it before it is committed.** A confident
wrong sentence in documentation is worse than no documentation, because the next
person will believe it.

The prompt that mitigates most of this is in the exercise: make it mark what it
inferred.

→ **`exercise.md`**
