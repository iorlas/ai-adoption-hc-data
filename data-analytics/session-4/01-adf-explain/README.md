# 1 — Explain it: what does this thing actually do?

**25 minutes, hands-on · Claude Code + Azure Data Factory pipeline definitions**
*5 min we demo · 15 min you do it · 5 min share what you found.*

> **Who does what:** **▸ We run it first, then you** — watch, then repeat it ·
> **▸ Your turn** — you drive, we are on the floor · **▸ Together** — whole room,
> out loud. Nothing here is a test.

## The situation

`adf/` holds one pipeline:

- Eleven activities, a Mapping Data Flow, eight datasets, three linked services,
  a weekly trigger
- Last published November 2024 by someone who has left
- Folder `Legacy/Supporter`, annotated `do-not-touch`, one activity called
  `Copy1`

Nobody here has seen it before — on purpose. It is the exact position you are in
with the ones you inherited.

## What makes this possible without ADF

The pipeline is **JSON**, and Claude reads JSON as well as it reads anything. No
factory, no Azure connection, nothing that could run by accident. This
generalises:

> Anything in your world stored as text is readable — pipeline definitions, DAX,
> M, SQL, config, YAML. Anything that is a binary or lives only inside a GUI is
> not. That one distinction tells you in advance which of your problems this will
> help with.

## What "explain it" actually means

Not a summary. Four questions a maintainer needs answered:

1. **Order of operations, and what depends on what** — including which
   dependencies are on success and which are not. That is where the surprises
   live.
2. **Where does a given number come from?** Asked whenever a figure looks wrong,
   and half a day by hand.
3. **What decisions are baked in?** Filters, defaults, exclusions — decided once,
   for a reason nobody remembers.
4. **What is the schedule, and what happens if a run is missed?**

## The thing that will actually happen

> Claude will give you a fluent, confident, mostly-correct explanation. Some of
> it will be wrong, because it is inferring intent from JSON with no comments.
> You are the one who can tell which.

The skill is not getting the explanation — it is **interrogating it**.

---

# The exercise

Understand an inherited pipeline.

## Step 1 — The overview (~5 min)

**▸ We run it first, then you.**

**Scene.** Claude Code, in the `data-analytics` folder, **a new conversation** —
nothing from Session 3 should be in it. One folder in play, `adf/`, holding five
exported Azure Data Factory files:

```
adf/pipeline_supporter_weekly_load.json   the pipeline — the one we read
    dataflow_supporter_enrich.json        the mapping data flow it calls
    datasets.json  linked_services.json   what it reads and writes
    trigger_weekly.json                   when it runs
```

**Open `pipeline_supporter_weekly_load.json` yourself in a second tab** and leave
it there. Every claim Claude makes today gets checked against that file.

> Read everything in `adf/`. Explain what `PL_Supporter_Weekly_Load` does, in
> order. For each activity: what it does, what it depends on, and whether that
> dependency is on success or on something else. Write it as prose a colleague
> could read, not a bullet list of activity names.

**▸ Together — we ask, you answer from the JSON.**

Then check **one** thing against the JSON, before believing the rest:

> `Update Watermark` — what is its dependency condition, and what does that mean
> if the data flow fails?

**The answer is not `Succeeded`.** Details like this survive for years because
nobody has read the JSON.

## Step 2 — Trace one number back (~4 min)

**▸ Your turn.**

> The output table `dw.dim_supporter_enriched` has a column `value_band`. Trace
> it back to source: which transformation creates it, what it is derived from,
> and which rows never reach it at all.

That last clause matters. Something is filtered out before the sink — which is
where "why is this supporter missing from the report?" gets answered.

Then the same question as you actually get asked it:

> A colleague says a supporter is missing from the dashboard. Given this
> pipeline, list every place they could have been dropped, in order.

## Step 3 — Find the baked-in decisions (~4 min)

**▸ Your turn.**

> List every hardcoded value, filter, default and exclusion in this pipeline.
> For each: where it is, what it does, and what would break if it were wrong.

Expect several. One is a business rule silently shaping every number downstream.
One is a comment admitting it is a workaround. One should not be in the file.

When you find the business rule:

> Is this filter documented anywhere in the pipeline, and how would anyone
> reading the output know it was applied?

## Step 4 — Interrogate the explanation (~2 min)

**▸ Your turn.**

> Which parts of your explanation are things the JSON states directly, and which
> are things you inferred? List the inferences separately.

The habit worth taking away. A confident explanation of undocumented code is
**partly inference, always** — and one ten-second question tells you which half
needs a human.

## Step 5 — Confirm ready

Tell us when you can answer these three without looking:

1. What happens to the watermark if the data flow fails?
2. Which supporters never reach the output table?
3. Name one hardcoded value that should not be in the file.

---

## If it goes wrong

**It only reads one file.** Say: *"read all five JSON files in `adf/`, including the
data flow script lines and the datasets."* The data flow holds most of the logic
and is a separate file.

**The explanation is too shallow.** Push: *"explain it to someone who has to be
on call for it tonight."*

**You disagree with it.** Good — say so, with your reason. A well-argued
correction usually gets a real reconsideration, and occasionally you turn out to
be wrong. Both outcomes are the exercise.
