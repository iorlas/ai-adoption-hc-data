# Answers — 1 · Explain it

**FACILITATOR ONLY. Never on screen.** Everything you present is in
`README.md` — read that with the room. This page is what you cannot show them.

Clock and ownership: `session-4/facilitator/run-sheet.md`.

**PROTECTED.** Parts 1 and 2 are 55 of the 180 minutes and they are what the
client said they wanted most. Neither gets cut.

## The watermark question — let them get it, do not tell them

Run step 1 on screen. Claude reads all five files in `adf/` and explains the
pipeline in order. Then ask:

> `Update Watermark` — what is its dependency condition, and what does that mean
> if the data flow fails?

The answer is `Completed`, not `Succeeded`. The data flow fails and the watermark
advances anyway.

**Be careful how you state the consequence, because the obvious version is
wrong.** Nothing in this pipeline actually *reads* the watermark:
`Lookup Watermark` runs, and no activity ever references its output. `Copy1`
selects files by `wildcardFolderPath: "supporters/@{formatDateTime(utcnow(),
'yyyy/MM/dd')}"` — today's date, every time — and the sink is `truncate: true`,
a full replace. So the watermark cannot cause a skipped load.

**What it actually does is worse in a quieter way: the only record of when the
data last loaded successfully is now a lie**, and the first person to build
incremental loading on top of that table inherits a silent bug from 2024.

**If someone in the room says "but nothing reads it" — that is the best possible
outcome.** They have read the JSON rather than the explanation, which is the
entire skill this segment teaches. Say so out loud and give them the credit.

**That one word sells the segment.** It has been there since 2024, and no amount
of staring at the ADF canvas would have shown it to you. Let the room get there
rather than telling them.

**During the 15 minutes**, watch for people accepting the first fluent
explanation. The skill is not getting the explanation — it is interrogating it.
They know what ADF activities do; Claude is doing the reading, they are doing
the judging.

## Gate — three questions, answered without looking

1. **What happens to the watermark if the data flow fails?**
2. **Which supporters never reach the output table?**
3. **Name one hardcoded value that should not be in the file.**

Answers: it advances anyway, and the watermark table starts lying — though
nothing downstream reads it · Northern Ireland and Deceased · the plaintext
password (or the Northern Ireland exclusion, or the 300-second `Wait1`).

## Answer key

### The watermark
`Update Watermark` depends on `DF_Enrich_Supporters` with
`dependencyConditions: ["Completed"]`. Silent data loss on the following run.

### Tracing `value_band`
`aggGiving` sums `amount_gbp` per supporter → `deriveFlags` builds `value_band`
via a `case()` at 100 / 1,000 / 5,000 → `filterOut` **drops the row entirely**
if region is Northern Ireland or status is Deceased → `selectFinal` → sink,
which truncates and reloads.

Two things worth drawing out:

- The banding uses `dw.fact_donation` with **no refund filter** — yesterday's
  disagreement reappearing inside a pipeline.
- Because `iifNull` defaults a blank status to `'Active'`, the "drop Deceased"
  filter never removes a record whose status was missing. Two rules interacting,
  neither written down.

### "A supporter is missing" — the full list
Wrong folder date · truncate-then-failed-copy · schema drift · the Northern
Ireland filter · the Deceased filter · the `ForEach` race · the merge proc's own
`ExcludeRegion` parameter · a failed refresh showing an older dataset.

**Eight places.** By hand, that is most of an afternoon.

### Hardcoded values they should find
- `ExcludeRegion: "Northern Ireland"` — applied twice, documented nowhere
- `Password=Wint3r2022!` in plaintext in `linked_services.json`, while the
  linked service directly below it correctly uses Key Vault
- `Wait1`, 300 seconds, with a comment admitting it is a workaround
- `r.byrne@example-charity.org` — the person the `Wait1` comment is signed by
- Seven-day timeouts on activities that take minutes

## What goes wrong

**It only reads one file.** Say: *"read all five files in `adf/`, including the
data flow script lines and the datasets."* The data flow holds most of the
logic and is the easiest to miss.

**The explanation is too shallow.** Push: *"explain it to someone who has to be
on call for it tonight."* Changes the answer considerably.

**Someone disagrees with Claude.** Excellent. Have them argue it in the
conversation, with their reason, and watch what happens. A well-argued
correction usually gets a real reconsideration — and occasionally they turn out
to be wrong. Both outcomes are the exercise.

**Nobody finds the watermark thing.** Ask directly. It is worth the room seeing
it more than it is worth them discovering it.
