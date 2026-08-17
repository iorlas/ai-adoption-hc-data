# 3 — Find the weak spots

**20 minutes, hands-on · Claude Code + Azure Data Factory pipeline definitions**
*4 min we demo · 12 min you do it · 4 min share the worst one you found.*

> **Who does what:** **▸ We run it first, then you** — watch, then repeat it ·
> **▸ Your turn** — you drive, we are on the floor · **▸ Together** — whole room,
> out loud. Nothing here is a test.

This is the *"finding places where they might not be robust"* part of your ask.

## The question

Not "is this good code". Narrower:

> **What happens when something upstream changes, and how would we find out?**

> The pipelines that hurt are not the ones that fail — a failure sends an alert.
> The ones that hurt are the ones that **succeed while producing the wrong
> answer.**

## Three grades of failure, worst last

1. **It fails loudly.** Someone gets paged, someone fixes it. Annoying, fine.
2. **It fails and nobody is told.** The dashboard shows last week's numbers and
   everyone believes them.
3. **It succeeds with the wrong data.** Worst by a long way. Nothing alerts, the
   numbers look plausible, and it may be months before anyone notices.

Spend the twenty minutes on category 3. **This pipeline has several, and they
are not where you would look first.**

Ask of every step: **if this went wrong, would anybody know?**

## Why Claude is genuinely useful here

Not because it knows more about ADF than you do — because this is tedious,
mechanical, and easy to lose your place in.

> It enumerates. You judge.

---

# The exercise

Where will this break, and would anyone notice?

## Step 1 — Enumerate (~3 min)

**▸ We run it first, then you.**

**Scene.** **Same conversation as parts 1 and 2** — you are now three steps into
one thread about one pipeline, and that accumulated context is exactly what makes
this step cheap. Same two files in play:
`adf/pipeline_supporter_weekly_load.json` and `adf/dataflow_supporter_enrich.json`.
Nothing new to open.

> Go through `PL_Supporter_Weekly_Load` and the data flow activity by activity.
> For each, tell me what happens if the input is wrong or missing: a source
> column renamed or removed, a file that arrives empty, a value that changes
> type, a run that starts before the upstream export has finished.
>
> For each risk say: does the pipeline fail loudly, fail silently, or succeed
> with wrong data? Rank them, worst first.

**Rank by "succeeds with wrong data" first.** If Claude ranks by likelihood, tell
it to re-rank by consequence — a rare silent corruption beats a frequent loud
failure every time.

## Step 2 — Chase the silent ones (~3 min)

**▸ Your turn.**

> For each silent failure: describe the exact sequence of events, what the
> output table would contain afterwards, and what a person looking at the
> dashboard would see. Would anything alert?

Then the question that turns this into work you can hand over:

> What is the smallest change that would turn each silent failure into a loud
> one?

Usually a validation step, a schema assertion, or a row-count check. Cheap — and
it converts the worst category into the least bad one.

## Step 3 — The two specific ones worth finding yourself (~4 min)

**▸ Together, out loud.**

Easy to skim past, so ask directly:

> `Truncate Staging` empties the table, and then `Copy1` reads from a folder
> named after today's date. Two cases: the copy *fails*, and the copy *succeeds
> finding no files*. Which one does the pipeline notice, and what is in
> `dw.dim_supporter_enriched` at the end of each?

> The data flow replaces missing values with defaults. Which columns, what
> defaults, and what does that do to a data-quality report run downstream?

The second connects back to Monday. Open the rules you wrote yesterday:

> Here are the data-quality rules we wrote yesterday, in
> `docs/data-quality-rules.md`. For each one, tell me whether a report built on
> `dw.dim_supporter_enriched` could still detect it — or whether this pipeline
> hides it first. Four ways it can hide one: a default value fills the blank,
> the aggregate sums the rows away, the column is not carried through to the
> sink, or the row is filtered out entirely.

**Expect most of your rules to be defeated.** Not by anything dramatic — by a
left join, a `sum()`, and a column that simply is not in the output. The quality
report shows a perfect score because the evidence never reached it.

The strongest argument either session makes:

> **You can do yesterday's work perfectly and still be wrong, because the thing
> that broke the data also hid the break. Data quality and pipelines are not two
> problems.**

## Step 4 — Write it down (~2 min)

**▸ Your turn.**

> Fill in the **Known weaknesses** section of
> `adf/PL_Supporter_Weekly_Load.md` — the heading is already there. Rank them by
> consequence, and for each give the failure mode, whether it is silent, and the
> smallest change that would make it loud.

## Step 5 — Confirm ready

Show us the **Known weaknesses** section in `adf/PL_Supporter_Weekly_Load.md` on
screen, and name:

1. The weak spot you would fix first, and why that one
2. One failure this pipeline would not tell anybody about

---

## What you leave with

A ranked list of weak spots inside the documentation you wrote twenty minutes
ago — and a set of questions to ask of the next inherited pipeline.

---

## If it goes wrong

**It gives you generic best-practice advice.** "Add error handling", "use Key
Vault". True but useless. Push: *"be specific to this pipeline — name the
activity and describe what actually happens."*

**It finds fifty problems.** Ask it to rank by consequence and give the top five.
A list of fifty is the same as a list of none.

**It misses the truncate-then-copy problem.** Ask directly, as in Step 3 — the
clearest example of a step that is individually sensible and collectively
dangerous.
