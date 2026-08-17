# 2 — Document it, for the colleague who inherits it next

**30 minutes, hands-on · Claude Code + Azure Data Factory pipeline definitions**
*5 min we demo · 20 min you do it · 5 min share-back.*

> **Who does what:** **▸ We run it first, then you** — watch, then repeat it ·
> **▸ Your turn** — you drive, we are on the floor · **▸ Together** — whole room,
> out loud. Nothing here is a test.

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

> You are writing for two readers, and that is why this compounds instead of
> being one more documentation task nobody does.

That is the same mechanism as yesterday's `CLAUDE.md`, applied to a pipeline
instead of a measure.

## The honest caveat

Claude will write documentation that is fluent and mostly right, and will state
inferences as facts. **You must read it before it is committed.** A confident
wrong sentence in documentation is worse than no documentation, because the next
person will believe it.

The prompt that mitigates most of this is in step 1: make it mark what it
inferred. A confident explanation of undocumented work is **partly guesswork,
always**, and the useful move is making the guesswork visible rather than
pretending to remove it.

---

# The exercise

Write the documentation that does not exist.

You are writing `adf/PL_Supporter_Weekly_Load.md`. By the end it should be
something you would be content to hand to a colleague on their first week.

## Step 1 — The first draft (~6 min)

**▸ We run it first, then you.**

> Using everything you worked out in the last exercise, write
> `adf/PL_Supporter_Weekly_Load.md` documenting this pipeline. Structure it as:
> what it is for in business terms · schedule and trigger · the activities in
> order with their dependencies · the data flow's transformations · where each
> output column comes from · hardcoded decisions and exclusions · known
> weaknesses · what to do if it fails overnight.
>
> Mark anything you inferred rather than read directly from the JSON with
> **[inferred]**. Do not guess at business reasons — where the reason for a
> decision is not in the files, write "reason not recorded".

That last paragraph is the whole difference between documentation that helps and
documentation that misleads.

## Step 2 — Read it as the person who inherits it (~5 min)

**▸ Your turn.**

Read the draft with one question in mind: *at 3am, does this help?*

Specific things to check:

- Is every **[inferred]** claim one you agree with? Delete or correct the ones
  you do not.
- Does the failure section tell you what to actually do, or does it just say
  "check the logs"?
- Does the hardcoded-decisions section include the regional exclusion? If it
  does not, the document is hiding the single most consequential line in the
  pipeline.
- Does it mention that one dependency is not on `Succeeded`?
- Does "reason not recorded" appear where the files genuinely do not say why?
  That is the honest answer and the more useful one — it tells the next person
  the question is open rather than closed.

## Step 3 — Make it answer the questions you actually get asked (~5 min)

**▸ Your turn.**

> Add a section called "Questions people ask about this pipeline" with the five
> most likely questions a stakeholder or an analyst would ask about the data it
> produces, and the answer, with a pointer to where in the pipeline the answer
> comes from.

Start it with the two real ones: *why is this supporter missing?* and *why does
this number not match the other report?* Both have answers in the pipeline, and
both are questions this team actually gets.

## Step 4 — Make it work as context (~4 min)

**▸ Your turn.**

> Add a pointer to this documentation from `CLAUDE.md`, in a Pipelines section.
> One or two lines — enough that a future conversation knows the document exists
> and what it covers.

Then test that it worked. **New conversation:**

> What does the weekly supporter load do about supporters in Northern Ireland?

If your documentation is doing its job, the answer comes back immediately and
correctly, without Claude re-reading five JSON files and re-deriving it.

That is the compounding part. The half-hour you just spent is now spent for
everyone, permanently.

## Step 5 — Confirm ready

Tell us when you have `adf/PL_Supporter_Weekly_Load.md` written, at least one
**[inferred]** claim that you corrected or deleted, and the new-conversation
test working.

---

## If it goes wrong

**It writes 4,000 words.** Ask for it shorter and say who for: *"rewrite this
for someone who has fifteen minutes and is on call tonight."* Length is not
quality, and long documentation does not get read at 3am.

**Everything is marked [inferred].** It has over-corrected. Say: *"only mark
things you could not read directly from the files."*

**It invents a business reason.** This is the failure mode to look out for, and
it is worth stopping on — it is a live example of the
thing the whole workshop is about. Name it, and fix the prompt.
