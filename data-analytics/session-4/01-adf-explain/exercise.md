# Exercise — understand an inherited pipeline

**25 minutes.** 5 min we demo · 15 min you do it · 5 min share what you found.

> **Who does what:** **▸ We run it first, then you** — watch, then repeat it ·
> **▸ Your turn** — you drive, we are on the floor · **▸ Together** — whole room,
> out loud. Nothing here is a test.
---

## Step 1 — The overview (~5 min)

**▸ We run it first, then you.**

> Read everything in `adf/`. Explain what `PL_Supporter_Weekly_Load` does, in
> order. For each activity: what it does, what it depends on, and whether that
> dependency is on success or on something else. Write it as prose a colleague
> could read, not a bullet list of activity names.

Read it. Then check **one** thing yourself against the JSON, before you believe
any of the rest:

> `Update Watermark` — what is its dependency condition, and what does that mean
> if the data flow fails?

The answer is not `Succeeded`. Work out what follows from that. It is the kind
of detail that survives in a pipeline for years because nobody has ever read the
JSON.

## Step 2 — Trace one number back (~4 min)

**▸ Your turn.**

Pick a column in the output and follow it all the way home:

> The output table `dw.dim_supporter_enriched` has a column `value_band`. Trace
> it back to source: which transformation creates it, what it is derived from,
> and which rows never reach it at all.

That last clause is the one that matters. Something is filtered out before the
sink, and if you were asked "why is this supporter missing from the report?"
this is where the answer lives.

Then the same question in the form you actually get asked it:

> A colleague says a supporter is missing from the dashboard. Given this
> pipeline, list every place they could have been dropped, in order.

## Step 3 — Find the baked-in decisions (~4 min)

**▸ Your turn.**

> List every hardcoded value, filter, default and exclusion in this pipeline.
> For each: where it is, what it does, and what would break if it were wrong.

Expect several. At least one is a business rule that somebody typed once and
that is still silently shaping every number downstream. At least one is a
comment that admits it is a workaround. At least one should not be in the file
at all.

When you find the business rule, ask the real question:

> Is this filter documented anywhere in the pipeline, and how would anyone
> reading the output know it was applied?

## Step 4 — Interrogate the explanation (~2 min)

**▸ Your turn.**

> Which parts of your explanation are things the JSON states directly, and which
> are things you inferred? List the inferences separately.

This is the habit worth taking away from the whole session. A confident
explanation of undocumented code is **partly inference**, always. Making it
separate the two is a ten-second question that tells you which half needs a
human to check it.

## Step 5 — Confirm ready

Tell us when you can answer these three without looking:

1. What happens to the watermark if the data flow fails?
2. Which supporters never reach the output table?
3. Name one hardcoded value that should not be in the file.

---

## If it goes wrong

**It only reads one file.** Say: *"read all five files in `adf/`, including the
data flow script lines and the datasets."* The data flow is where most of the
logic is, and it is easy to miss because it is a separate file.

**The explanation is too shallow.** Push: *"explain it to someone who has to be
on call for it tonight."* Changes the answer considerably.

**You disagree with it.** Good. Say so, in the conversation, with your reason.
Watch what it does — a well-argued correction usually gets a real reconsideration,
and occasionally you turn out to be the one who was wrong. Both outcomes are the
exercise.
