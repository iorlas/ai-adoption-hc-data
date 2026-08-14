# Exercise — write the documentation that does not exist

**30 minutes.** 5 min we demo · 20 min you do it · 5 min share-back.

You are writing `adf/PL_Supporter_Weekly_Load.md`. By the end it should be
something you would be content to hand to a colleague on their first week.

---

## Step 1 — The first draft (~6 min)

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

## Step 3 — Make it answer the questions you actually get asked (~5 min)

> Add a section called "Questions people ask about this pipeline" with the five
> most likely questions a stakeholder or an analyst would ask about the data it
> produces, and the answer, with a pointer to where in the pipeline the answer
> comes from.

Start it with the two real ones: *why is this supporter missing?* and *why does
this number not match the other report?*

## Step 4 — Make it work as context (~4 min)

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
if it happens in the room it is worth stopping on — it is a live example of the
thing the whole workshop is about. Point at it, name it, and fix the prompt.
