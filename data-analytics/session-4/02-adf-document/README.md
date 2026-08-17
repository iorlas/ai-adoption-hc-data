# 2 — Document it, for the colleague who inherits it next

**30 minutes, hands-on · Claude Code + Azure Data Factory pipeline definitions**
*5 min we demo · 20 min you do it · 5 min share-back.*

> **Who does what:** **▸ We run it first, then you** — watch, then repeat it ·
> **▸ Your turn** — you drive, we are on the floor · **▸ Together** — whole room,
> out loud. Nothing here is a test.

## The gap you described

> "Some of them are enormous and none of us made them and the documentation is
> very weak."

Documentation does not get written because writing it needs understanding first —
half a day — and by then you have solved the problem you came for.

You did the understanding in twenty-five minutes. The documentation is now the
**residue of work you already did**, not a separate task.

## What makes documentation worth having

The test: **could a colleague, at 3am, with this document and no access to you,
work out what is wrong?** So it must hold what the JSON does not show:

- What it is *for*, in business terms
- The order, and what breaks if a step fails partway
- Every baked-in decision, named, with date and reason where known — and
  "reason unknown" written explicitly where it is not
- Where each output column comes from
- What it depends on upstream, and what depends on it downstream
- What to do when it fails at 2am on a Monday

## Where it lives

Next to the pipeline, in version control. Not Confluence, where it rots
separately from the thing it describes. It is where the next person will look —
and **it is where Claude will look.**

> You are writing for two readers, and that is why this compounds instead of
> being one more documentation task nobody does.

Same mechanism as yesterday's `CLAUDE.md`, applied to a pipeline.

## The honest caveat

Claude writes fluent, mostly-right documentation and states inferences as facts.
**You must read it before it is committed.** A confident wrong sentence is worse
than no documentation — the next person will believe it.

---

# The exercise

Write the documentation that does not exist: `adf/PL_Supporter_Weekly_Load.md`,
good enough to hand a colleague in their first week.

`adf/PL_Supporter_Weekly_Load.md` already exists with the headings in place —
you are filling it in, not starting from a blank page.

A finished example, for a different organisation, is in
`templates/example-library/pipelines/`. **After you write yours, not before.**

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

*At 3am, does this help?* Check:

- Is every **[inferred]** claim one you agree with? Delete or correct the rest.
- Does the failure section say what to actually do, or just "check the logs"?
- Does the hardcoded-decisions section include the regional exclusion? Without
  it, the document hides the most consequential line in the pipeline.
- Does it mention that one dependency is not on `Succeeded`?
- Does "reason not recorded" appear where the files genuinely do not say why?
  That tells the next person the question is open rather than closed.

## Step 3 — Make it answer the questions you actually get asked (~5 min)

**▸ Your turn.**

> Add a section called "Questions people ask about this pipeline" with the five
> most likely questions a stakeholder or an analyst would ask about the data it
> produces, and the answer, with a pointer to where in the pipeline the answer
> comes from.

Start with the two real ones: *why is this supporter missing?* and *why does this
number not match the other report?*

## Step 4 — Make it work as context (~4 min)

**▸ Your turn.**

> Add a pointer to this documentation from `CLAUDE.md`, in a Pipelines section.
> One or two lines — enough that a future conversation knows the document exists
> and what it covers.

Then test it. **New conversation:**

> What does the weekly supporter load do about supporters in Northern Ireland?

**What you should see:** the answer comes back immediately and correctly, without
Claude re-reading five JSON files. That is the compounding part — the half-hour
is now spent for everyone, permanently.

## Step 5 — Confirm ready

Tell us when you have `adf/PL_Supporter_Weekly_Load.md` written, at least one
**[inferred]** claim that you corrected or deleted, and the new-conversation
test working.

---

## If it goes wrong

**It writes 4,000 words.** Ask for it shorter and say who for: *"rewrite this
for someone who has fifteen minutes and is on call tonight."*

**Everything is marked [inferred].** Over-corrected. Say: *"only mark things you
could not read directly from the files."*

**It invents a business reason.** Stop on this one — a live example of the thing
the whole workshop is about. Name it, and fix the prompt.
