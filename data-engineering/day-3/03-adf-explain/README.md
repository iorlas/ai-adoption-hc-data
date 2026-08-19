# 3 — Explain it: what does this thing actually do?

**20 minutes, hands-on**
*4 min we run it · 12 min you drive · 4 min what you found.*

> **Who does what:** **▸ We run it first, then you** on step 1, **▸ Your turn**
> from step 2. Nothing here is a test.

## The situation

You are about to convert a Mapping Data Flow after the break. Before that, the
job nobody schedules time for: **reading a pipeline you did not write, and
deciding which parts of the explanation you believe.**

Not yours, either — this one belongs to the fundraising side:

- Eleven activities (twelve, counting the one inside the `ForEach`), a Mapping
  Data Flow, eight datasets, three linked services, a weekly trigger
- Last published November 2024 by someone who has left
- Folder `Legacy/Supporter`, annotated `do-not-touch`, one activity called
  `Copy1` and another called `Stored procedure1`

Nobody in this room has seen it before, on purpose. It is the exact position you
are in with the ones you inherited.

## What makes this possible without ADF

The pipeline is **JSON**, and Claude reads JSON as well as it reads anything.
No factory, no Azure connection, nothing that could run by accident.

> Anything in your world stored as text is readable — pipeline definitions, DAX,
> M, SQL, config, YAML, Terraform. Anything binary, or living only inside a GUI,
> is not. That one distinction tells you in advance which of your problems this
> will help with.

## What "explain it" actually means

You know what ADF activities do. That is not the gap. Four questions a
maintainer needs answered, and all four take an afternoon by hand:

1. **Order of operations, and what depends on what** — including which
   dependencies are on success and which are not. That is where the surprises
   live.
2. **Where does a given output column come from?** Asked whenever a figure looks
   wrong.
3. **What decisions are baked in?** Filters, defaults, exclusions — decided once,
   for a reason nobody remembers.
4. **What is the schedule, and what happens if a run is missed?**

## The thing that will actually happen

> Claude will give you a fluent, confident, mostly-correct explanation. Some of
> it will be wrong, because it is inferring intent from JSON that has no
> comments. **You are the one who can tell which** — you have maintained
> pipelines like this.

The skill is not getting the explanation. It is interrogating it. Claude does
the reading; you do the judging.

---

# The exercise

## Step 1 — the overview

**▸ We run it first, then you.**

**Scene.** Claude Code, in the `data-engineering/` folder, **a new
conversation** — nothing from part 2 in it. One folder in play,
`later-days/adf/supporter_weekly/`, holding five exported ADF files:

```
pipeline_supporter_weekly_load.json    the pipeline — the one we read
dataflow_supporter_enrich.json         the mapping data flow it calls
datasets.json   linked_services.json   what it reads and writes
trigger_weekly.json                    when it runs
```

**Open `pipeline_supporter_weekly_load.json` yourself in a second tab** and
leave it there. Every claim Claude makes gets checked against that file.

> Read everything in `later-days/adf/supporter_weekly/`. Explain what
> `PL_Supporter_Weekly_Load` does, in order. For each activity: what it does,
> what it depends on, and whether that dependency is on success or on something
> else. Write it as prose a colleague could read, not a bullet list of activity
> names.

**▸ Together — I ask, you answer from the JSON.**

Then check **one** thing before believing the rest:

> `Update Watermark` — what is its dependency condition, and what does that mean
> if the data flow fails?

**The answer is not `Succeeded`.** Details like this survive for years because
nobody has read the JSON. Then push one step further, because the obvious
consequence is not the real one:

> Does anything in this pipeline actually read that watermark?

## Step 2 — trace one column back

**▸ Your turn.**

> The output table `dw.dim_supporter_enriched` has a column `value_band`. Trace
> it back to source: which transformation creates it, what it is derived from,
> and which rows never reach it at all.

That last clause is the one that matters. Something is filtered out before the
sink — which is where *"why is this record missing?"* gets answered.

Then the same question in the form you actually get it:

> Someone says a supporter is missing from the warehouse. Given this pipeline,
> list every place they could have been dropped, in order.

Count them. Then ask yourself how long that list takes by hand.

## Step 3 — the baked-in decisions

**▸ Your turn.**

> List every hardcoded value, filter, default and exclusion in this pipeline.
> For each: where it is, what it does, and what would break if it were wrong.

Expect several. One is a business rule silently shaping every number
downstream. One is a comment admitting it is a workaround. **One should not be
in a file that lives in Git**, and you will know it when you see it.

When you find the business rule:

> Is this filter documented anywhere in the pipeline, and how would anyone
> reading the output table know it had been applied?

## Step 4 — interrogate the explanation

**▸ Your turn.** Two minutes, and it is the habit worth taking away.

> Which parts of your explanation are stated directly in the JSON, and which did
> you infer? List the inferences separately.

An explanation of undocumented code is **partly inference, always.** One
ten-second question tells you which half needs a human.

## Step 5 — confirm ready

Say when you can answer these three without looking:

1. What happens to the watermark if the data flow fails — and does it matter?
2. Which supporters never reach the output table?
3. Name one hardcoded value that should not be in the file.

---

## Where this goes next

Part 4 asks one narrower question of the same pipeline: where does it succeed
while producing the wrong answer? Then part 5 converts a different flow to SQL.

Everything you just did — read the script lines, find the filter, separate fact
from inference — is step zero of both. **A conversion of a pipeline you have not
read is a rewrite with extra confidence.**

## If it goes wrong

**It only reads one file.** Say: *"read all five JSON files in
`later-days/adf/supporter_weekly/`, including the data flow script lines and the
datasets."* The data flow holds most of the logic and is the easiest to miss.

**The explanation is too shallow.** Push: *"explain it to someone who has to be
on call for it tonight."* It changes the answer considerably.

**You disagree with it.** Good — say so, with your reason. A well-argued
correction usually gets a real reconsideration, and occasionally you turn out to
be wrong. Both outcomes are the exercise.
