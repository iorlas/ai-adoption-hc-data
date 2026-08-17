# Exercise — where will this break, and would anyone notice?

**20 minutes.** 4 min we demo · 12 min you do it · 4 min share the worst one
you found.

> **Who does what:** **▸ We run it first, then you** — watch, then repeat it ·
> **▸ Your turn** — you drive, we are on the floor · **▸ Together** — whole room,
> out loud. Nothing here is a test.
---

## Step 1 — Enumerate (~3 min)

**▸ We run it first, then you.**

> Go through `PL_Supporter_Weekly_Load` and the data flow activity by activity.
> For each, tell me what happens if the input is wrong or missing: a source
> column renamed or removed, a file that arrives empty, a value that changes
> type, a run that starts before the upstream export has finished.
>
> For each risk say: does the pipeline fail loudly, fail silently, or succeed
> with wrong data? Rank them, worst first.

**Rank by "succeeds with wrong data" first.** If Claude ranks by likelihood
instead, tell it to re-rank by consequence — a rare silent corruption beats a
frequent loud failure every time.

## Step 2 — Chase the silent ones (~3 min)

**▸ Your turn.**

Take the ones it graded "succeeds with wrong data" and make it be specific:

> For each silent failure: describe the exact sequence of events, what the
> output table would contain afterwards, and what a person looking at the
> dashboard would see. Would anything alert?

Then the question that turns this into work you can hand over:

> What is the smallest change that would turn each silent failure into a loud
> one?

Usually it is a validation step, a schema assertion, or a row-count check
against the previous run. Cheap, and it converts the worst category of failure
into the least bad one.

## Step 3 — The two specific ones worth finding yourself (~4 min)

**▸ Together, out loud.**

Two questions to ask directly, because they are the most instructive and it is
easy to skim past them:

> The `Truncate Staging` step runs before the copy. If the copy then fails, what
> is in the staging table? What does the next step do with that?

> The data flow replaces missing values with defaults. Which columns, what
> defaults, and what does that do to a data-quality report run downstream?

The second one connects straight back to Monday morning, and it is worth doing
properly rather than reading about. Open the rules you wrote yesterday and hand
them over:

> Here are the data-quality rules we wrote yesterday, in
> `docs/data-quality-rules.md`. For each one, tell me whether this pipeline
> would still let it fire — or whether one of the data flow's default values
> repairs the problem before the rule ever sees it.

**Expect several of your rules to be defeated.** A pipeline that helpfully fills
in blanks makes the data look clean while making it less true. The quality
report downstream shows a perfect score, produced by a pipeline that is lying.

That is the single strongest argument either session makes: **data quality and
pipelines are not two problems.** You can do yesterday's work perfectly and
still be wrong, because the thing that broke the data also hid the break.

## Step 4 — Write it down (~2 min)

**▸ Your turn.**

> Add a "Weak spots" section to `adf/PL_Supporter_Weekly_Load.md`. Rank them by
> consequence, and for each give the failure mode, whether it is silent, and the
> smallest change that would make it loud.

## Step 5 — Confirm ready

Tell us when you can name:

1. The weak spot you would fix first, and why that one
2. One failure this pipeline would not tell anybody about

---

## If it goes wrong

**It gives you generic best-practice advice.** "Add error handling", "use Key
Vault". True but useless. Push: *"be specific to this pipeline — name the
activity and describe what actually happens."*

**It finds fifty problems.** Ask it to rank by consequence and give you the top
five. A list of fifty is the same as a list of none.

**It misses the truncate-then-copy problem.** Ask about it directly, as in Step
3. Worth a close look — it is the clearest example
of a step that is individually sensible and collectively dangerous.
