# Answers — 3 · Find the weak spots

**FACILITATOR ONLY. Never on screen.** Everything you present is in
`README.md` — read that with the room. This page is what you cannot show them.

Clock and ownership: `session-4/facilitator/run-sheet.md`.

Carries this session's call-and-response beat, and the strongest thirty seconds
of the four sessions.

## Engineer the room towards two things

The `ForEach` race and the `iifNull` defaults. If nobody has them by minute 12,
ask directly — `README.md` has the prompts.

**Correct the ranking if Claude ranks by likelihood.** Rank by *consequence*: a
rare silent corruption beats a frequent loud failure every time.

## The call-and-response beat — do not skip this

Step 3 has them hand yesterday's own `docs/data-quality-rules.md` to Claude and
ask which of their rules this pipeline defeats.

**Run it out loud.** Read their rules one at a time, let the room call
*survives* or *defeated*, then check. Most lose — and not to anything dramatic.

| Rule | Verdict | Why |
|---|---|---|
| 1 · `status` not in the vocabulary (18 `Activ`) | **survives** | `iifNull(trim(status), 'Active')` only fills nulls. `trim()` does not repair a typo, and there are no blank statuses |
| 2 · duplicate people | **survives** | untouched by the flow |
| 3 · malformed email | **survives the flow, but is moot** — `email` is not in `selectFinal`, so no report downstream can check it |
| 4 · `last_activity_date` before `sign_up_date` (34) | **defeated** | `last_activity_date` is not in `selectFinal`'s `mapColumn` list. The column ceases to exist |
| 5 · orphan donations (30) | **defeated** | `joinDonations` is a **left** join — orphan donation rows disappear on the null side |
| 6 · duplicate gifts (44) | **defeated** | `aggGiving` sums to `total_given`; individual rows never reach the output |
| 7 · amount ≤ 0 (20) | **defeated** | same `sum()` |
| 8 · gift before sign-up (60) | **defeated** | only `max(donation_date)` survives the aggregate |

**Rule 1 is the one to dwell on.** It survives *because* `trim()` cannot fix a
typo — the helpful default was not helpful enough to hide the real defect, and
was never aimed at it. That is worth saying out loud.

**Four of twelve output columns are all that remain of donations.** The pipeline
does not lie by filling blanks; it lies by *summarising* and by *dropping
columns*.

Then land it plainly:

> "You can do yesterday's work perfectly and still be wrong, because the thing
> that broke the data also hid the break. Data quality and pipelines are not two
> problems."

That is the single strongest argument either session makes, and it only works
because they wrote those rules themselves yesterday. Anyone using
`session-4/fallback/data-quality-rules.md` participates normally — those are the
rules the room actually wrote.

## Gate — two answers

1. **Which weak spot would you fix first, and why that one?**
2. **Name one failure this pipeline would not tell anybody about.**

Question 1 is graded on the *reason*. "The plaintext password" is a fine answer
if the reason is about exposure; it is a weak answer if the reason is "it looked
wrong". Consequence, not tidiness.

## Answer key — the five that matter

Nineteen things are planted. These five are what the segment is about.

**★ The `ForEach` race.** `isSequential: false`, `batchCount: 50`, and *every*
iteration carries `preCopyScript: "TRUNCATE TABLE stg.campaign"`. Fifty parallel
iterations each truncate the table the others are writing into. **The pipeline
succeeds.** The staging table holds a nondeterministic subset. Nothing ever
alerts, and the row count changes week to week for no visible reason.

**★ `iifNull` masks the defects.** `status = iifNull(trim(status), 'Active')`
and `region = iifNull(region, 'Unknown')`. A supporter with a missing status
silently becomes **Active** and is counted everywhere downstream. This is the
one that connects to Monday.

**★ The undocumented regional exclusion.** `ExcludeRegion: "Northern Ireland"`
passed to the merge proc, **and** a separate `region != 'Northern Ireland'`
filter in the data flow. Applied twice, documented nowhere. Anyone reading the
output has no way to know a whole region is missing.

**★ The watermark advances on failure.** `dependencyConditions: ["Completed"]`.
Already found in part 1 — it belongs on this list too.

**★ Truncate-then-copy with no safety net.** `Truncate Staging` empties the
table, then `Copy1` runs with `retry: 0`. If the copy fails, staging is empty
and stays empty. Smallest fix: load into a new table and swap.

### The rest, briefly
Schema drift on everywhere (`"schema": []`, `validateSchema: false`,
`autoCreate`) · `allowDataTruncation: true` · `READ_UNCOMMITTED` ·
the `utcnow()` folder path that can never backfill and breaks under BST ·
`marketing_consent` conversion that nulls anything unexpected ·
`Notify Failure` covering one activity out of ten · notifying someone who left ·
stale dashboards on a failed refresh · retries backwards (3 on the trivial
lookup, 0 on both copies) · seven-day timeouts · a plaintext password beside a
correctly-configured Key Vault · `Wait1` · default activity names · a UTC
trigger for a London organisation.

Full detail in `session-4/facilitator/adf-issue-catalogue.md`.

## What goes wrong

**Generic best-practice advice** — "add error handling", "use Key Vault". True
and useless. Push: *"be specific to this pipeline — name the activity and
describe what actually happens."*

**Fifty problems.** Ask for the top five by consequence. Fifty is the same as
none.

**Nobody finds the truncate-then-copy problem.** Ask directly, per step 3. It is
the clearest example of a step that is individually sensible and collectively
dangerous.

**You are behind.** This is cut #3, after the ML taster and Better Questions — drop to 14 minutes
and run it as a group discussion off one screen. **Keep the rules handover** even
then; it is the payoff.
