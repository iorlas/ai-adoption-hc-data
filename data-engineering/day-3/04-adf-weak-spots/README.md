# 4 — Find the weak spots

**20 minutes, hands-on**
*3 min we run it · 12 min you drive · 5 min the worst one you found, out loud.*

> **Who does what:** **▸ We run it first, then you** on step 1, **▸ Your turn**
> for steps 2 and 4, **▸ Together** for step 3.

## The question

You have just read the pipeline. Now the narrower question, and the one that
actually costs money:

> **What happens when something upstream changes, and how would anyone find
> out?**

> The pipelines that hurt are not the ones that fail — a failure sends an alert.
> The ones that hurt are the ones that **succeed while producing the wrong
> answer.**

## Three grades of failure, worst last

1. **It fails loudly.** Someone gets paged, someone fixes it. Annoying, fine.
2. **It fails and nobody is told.** The warehouse holds last week's numbers and
   everyone believes them.
3. **It succeeds with the wrong data.** Worst by a long way. Nothing alerts, the
   numbers look plausible, and it may be months before anyone notices.

Spend the twenty minutes on category 3. **This pipeline has several, and they
are not where you would look first.**

Ask of every step: **if this went wrong, would anybody know?**

## Why Claude is genuinely useful here

Not because it knows more about ADF than you do — it does not. Because this is
tedious, mechanical, and easy to lose your place in.

> **It enumerates. You judge.**

---

# The exercise

## Step 1 — enumerate

**▸ We run it first, then you.**

**Scene.** **Same conversation as part 3.** You are now two steps into one
thread about one pipeline, and that accumulated context is exactly what makes
this step cheap. Same files in play — nothing new to open.

> Go through `PL_Supporter_Weekly_Load` and the data flow activity by activity.
> For each, tell me what happens if the input is wrong or missing: a source
> column renamed or removed, a file that arrives empty, a value that changes
> type, a run that starts before the upstream export has finished.
>
> For each risk say: does the pipeline fail loudly, fail silently, or succeed
> with wrong data? Rank them, worst first.

**If it ranks by likelihood, make it re-rank by consequence.** A rare silent
corruption beats a frequent loud failure every time.

## Step 2 — chase the silent ones

**▸ Your turn.**

> For each silent failure: describe the exact sequence of events, what the
> output table would contain afterwards, and what a person looking at the
> warehouse would see. Would anything alert?

Then the question that turns this into work you can hand to someone:

> What is the smallest change that would turn each silent failure into a loud
> one?

Usually a validation step, a schema assertion, or a row-count gate. Cheap — and
it converts the worst category into the least bad one.

## Step 3 — the two worth finding yourself

**▸ Together, out loud.** Easy to skim past, so ask directly:

> `Truncate Staging` empties the table, and then `Copy1` reads from a folder
> named after today's date. Two cases: the copy *fails*, and the copy *succeeds
> finding no files*. Which one does the pipeline notice, and what is in
> `dw.dim_supporter_enriched` at the end of each?

> The data flow replaces missing values with defaults. Which columns, what
> defaults, and what does that do to any data-quality report run downstream?

## Step 4 — the part that connects back to Tuesday

**▸ Your turn.** This is the point of the segment.

On Day 2 you generated data-quality rules and kept the meaningful ones in
`docs/data-quality-rules.md`. Those rules are about the donor table, and this
pipeline is somebody else's. So ask the transferable question:

> Here are the data-quality rules I wrote in `docs/data-quality-rules.md`. This
> pipeline is a different domain, so ignore the column names and answer
> structurally: for each rule, if a pipeline shaped like this one stood between
> the source and the report, could the rule still detect its defect? There are
> four ways a pipeline hides one — a default value fills the blank, an aggregate
> sums the rows away, the column is never carried through to the sink, or the
> row is filtered out entirely. Say which mechanism applies, and show me where
> in this data flow it happens.

**Expect most of your rules to be defeated.** Not by anything dramatic — by a
left join, a `sum()`, and a column that simply is not in the output. The quality
report shows a perfect score because the evidence never reached it.

Count how many of the flow's twelve output columns still carry row-level
donation detail. The answer is the argument:

> **You can do Tuesday's work perfectly and still be wrong, because the thing
> that broke the data also hid the break. Data quality and pipelines are not two
> problems.**

## Step 5 — write it down

**▸ Your turn.**

> Write `data-engineering/docs/pipelines/supporter-weekly.md`: what the pipeline
> does, then a **Known weaknesses** section ranked by consequence. For each: the
> failure mode, whether it is silent, and the smallest change that would make it
> loud.

## Step 6 — confirm ready

Name two things:

1. **The weak spot you would fix first, and why that one.** The reason is what
   matters, not the pick.
2. **One failure this pipeline would not tell anybody about.**

---

## What you leave with

A ranked list of weak spots, in a document that did not exist an hour ago — and
a set of questions to ask of the next inherited pipeline, which is the part that
transfers.

## If it goes wrong

**It gives you generic best-practice advice.** "Add error handling", "use Key
Vault". True and useless. Push: *"be specific to this pipeline — name the
activity and describe what actually happens."*

**It finds fifty problems.** Ask for the top five by consequence. A list of
fifty is the same as a list of none.

**It misses the truncate-then-copy problem.** Ask directly, as in step 3 — it is
the clearest example of a step that is individually sensible and collectively
dangerous.
