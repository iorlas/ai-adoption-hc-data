# Answers — 4 · Find the weak spots

**FACILITATOR ONLY. Never on screen.**

Reused from the analytics stream's Session 4, same five JSON files. **One thing
is genuinely different here and you need to know it before the day:** the
rules-handover in step 4 cannot run rule-by-rule, because their Day-2 rules are
about the donor table and this pipeline is about supporters. It runs
structurally instead. See "Step 4" below — it still works, and for this room it
arguably works better.

Full defect list: `facilitator/adf-issue-catalogue.md` (nineteen planted).

## Engineer the room towards two things

The `ForEach` race and the `iifNull` defaults. If nobody has them by minute 12,
ask directly.

**Correct the ranking if Claude ranks by likelihood.** Rank by *consequence*: a
rare silent corruption beats a frequent loud failure every time.

## The five that matter

**★ The `ForEach` race.** `isSequential: false`, `batchCount: 50`, and *every*
iteration carries `preCopyScript: "TRUNCATE TABLE stg.campaign"`. Fifty parallel
iterations each truncate the table the others are writing into. **The pipeline
succeeds.** The staging table holds a nondeterministic subset, nothing alerts,
and the row count changes week to week for no visible reason.

**Someone in this room will notice `stg.campaign` feeds nothing.** They are
right — `srcCampaign` is declared in the data flow and never joined, so today
the race corrupts a table with no consumer. Say so first, then reframe: the bug
is latent, and the first person to wire a campaign column into the warehouse
inherits it silently. **Latent defects in shared staging tables are exactly the
kind nobody finds by testing the thing they just built** — which is a sentence
worth saying slowly to a room of engineers.

**★ `iifNull` masks the defects.** `region = iifNull(region, 'Unknown')` turns a
blank region into a value that looks deliberate, and `Unknown` then sails past
the `region != 'Northern Ireland'` filter. The same pattern sits on status:
`status = iifNull(trim(status), 'Active')` would silently make a missing status
**Active** everywhere downstream.

**Lead with region.** Do not quote row counts — the supporter data itself is not
in this repo, so any number you say is unverifiable in the room, and this room
will check. The mechanism is the point, and the mechanism is in the JSON.

**★ The undocumented regional exclusion.** `ExcludeRegion: "Northern Ireland"`
passed to the merge proc, **and** a separate `region != 'Northern Ireland'`
filter in the data flow. Applied twice, documented nowhere. Anyone reading the
output table has no way to know a whole region is missing.

**★ The watermark advances on failure.** `dependencyConditions: ["Completed"]`.
Found in part 3 — it belongs on this list too, and this is where its consequence
gets ranked rather than just noticed.

**★ Truncate-then-copy with no safety net.** `Truncate Staging` empties the
table, then `Copy1` runs with `retry: 0`. **Two branches, and step 3 asks about
both.**

*The copy **fails*** — staging is empty and stays empty. Bad, but **noticed**:
the pipeline fails and `Notify Failure` is wired to exactly this activity.

*The copy **succeeds and finds no files*** — the worse one, and the one that
gets skipped. Staging is empty, the data flow runs happily, and the sink is
`truncate: true`: **`dw.dim_supporter_enriched` is wiped.** The merge proc runs,
the Power BI dataset refreshes to zero, and `Update Watermark` advances because
it fires on `Completed`. Nothing alerts, because nothing failed.

**If Claude says the copy would error on a missing folder, accept it and move
on.** Nothing in this JSON decides — no `validateDataConsistency`, no row-count
check, `"schema": []` — and *that* is the answer worth landing: **the file does
not say, so nobody can know without running it.**

Smallest fix for both: load into a new table and swap, plus a row-count gate.

## Step 4 — the rules handover, adapted

The analytics room handed over their own rule list and got a verdict per rule.
This room cannot: their Day-2 rules are `donor`-shaped (NHS numbers, ethnicity,
age at registration) and this is a supporter pipeline.

**So run it on the mechanism, and make that explicit rather than hiding it.**
The prompt in the README asks for one of four hiding mechanisms per rule, plus
where in *this* data flow it happens. All four are demonstrably present:

| Mechanism | Where it is, in this flow |
|---|---|
| **A default fills the blank** | `iifNull` on `status`, `region` and `email` in `cleanSupporter` |
| **An aggregate sums the rows away** | `aggGiving` — individual donations become `total_given`, `gift_count`, `last_gift_date` |
| **The column never reaches the sink** | `mapColumn` in `selectFinal` lists twelve columns; `date_of_birth`, `last_activity_date` and every donation-level field are not among them |
| **The row is filtered out** | `filterOut` drops Northern Ireland and Deceased; `joinDonations` is a **left** join, so orphan donations vanish on the null side |

**The number to land: of the twelve output columns, three carry anything about
donations at all** — `total_given`, `gift_count`, `last_gift_date` — and none of
them at row level. A duplicate gift, a negative amount, a gift dated before
sign-up: all three are arithmetically invisible downstream, and a quality report
built on this table returns a perfect score.

Then land it plainly:

> "You can do Tuesday's work perfectly and still be wrong, because the thing
> that broke the data also hid the break. Data quality and pipelines are not two
> problems."

**If someone has no rules file** — they skipped or missed Day 2 — hand them the
list above and have them work backwards: which of their real tables would each
mechanism hide a defect in? Same lesson, no artifact needed.

## The rest, briefly

Schema drift everywhere (`"schema": []`, `validateSchema: false`, `autoCreate`) ·
`allowDataTruncation: true` · `READ_UNCOMMITTED` · a `utcnow()` folder path that
can never backfill and shifts under BST · a `marketing_consent` conversion that
nulls anything unexpected · `Notify Failure` covering one activity out of ten ·
notifying somebody who has left · retries backwards (3 on the trivial lookup, 0
on both copies) · seven-day timeouts on activities that take minutes · a
plaintext password beside a correctly-configured Key Vault · `Wait1` · default
activity names · a UTC trigger for a London organisation.

## Gate

1. **Which weak spot would you fix first, and why that one?** Graded on the
   reason. "The plaintext password" is a fine answer if the reason is exposure;
   a weak one if the reason is tidiness. **Consequence, not neatness.**
2. **Name one failure this pipeline would not tell anybody about.**

## What goes wrong

**Generic best-practice advice** — "add error handling", "use Key Vault". True
and useless. Push: *"be specific to this pipeline — name the activity and
describe what actually happens."*

**Fifty problems.** Ask for the top five by consequence. Fifty is the same as
none.

**Nobody finds the truncate-then-copy problem.** Ask directly, per step 3.

**This room out-diagnoses the exercise.** Likely, and it is the good outcome —
they maintain pipelines like this. If they are finding things faster than the
script, skip to step 4: the rules handover is the part they will not have
thought of, and it is the only part that changes how they work on Monday.

## Time — and this is the designated cut

**Part 4 is the give in the day.** If parts 2 or 3 overran, this is what shrinks
or goes, and it goes cleanly: drop to twelve minutes by running step 1 as a
group discussion off one screen and going straight to step 4, or move the whole
thing to the take-home. **Keep step 4 even in the twelve-minute version** — it is
the payoff, and it is the only beat that reaches back to Day 2.
