# The ADF pipeline — the full catalogue

**FACILITATOR ONLY.** The complete list of everything planted in `adf/`.

The five that the sessions are actually about are summarised in
`session-4/01-adf-explain/answers.md` and
`session-4/03-adf-weak-spots/answers.md`. This file is the long reference
for when someone in the room finds something unexpected and you want to know
whether it was deliberate.

The two analysis hypotheses moved to
`session-4/04-better-questions/answers.md`.

---

## Everything planted in it

Nineteen things. They will not find all of them and should not try to. The five
marked ★ are the ones the session is actually about; make sure the room leaves
having seen those.

## Category 3 — succeeds, with wrong data (the worst kind)

**★ 1. The `ForEach` race.** `ForEach Campaign File` runs with
`isSequential: false` and `batchCount: 50`, and *every* iteration's copy carries
`preCopyScript: "TRUNCATE TABLE stg.campaign"`. Fifty parallel iterations each
truncate the table the others are writing into. The pipeline succeeds. The
staging table ends up holding some nondeterministic subset — often one file's
worth. Nothing alerts, ever, and the row count changes week to week for no
visible reason.

This is the best single artifact in the file. If the room finds nothing else,
find this.

**★ 2. `iifNull` masks the data-quality defects.** In the data flow:
`status = iifNull(trim(status), 'Active')` and `region = iifNull(region,
'Unknown')`. A supporter with a missing status silently becomes **Active** and
is counted in every downstream number. Tie this straight back to Monday: every
defect they spent an hour finding could be quietly patched over here, and the
quality report downstream would show a perfect score.

**★ 3. The undocumented regional exclusion.** `ExcludeRegion: "Northern
Ireland"` is passed to `usp_MergeSupporterDim`, *and* the data flow separately
filters `region != 'Northern Ireland'`. Applied twice, documented nowhere,
traceable to nobody. Anyone reading the output has no way to know a whole region
is missing. Ask: *"who signed this off, and when?"* — the honest answer is that
the file cannot tell you, which is the point.

**4. Schema drift is on everywhere.** Datasets carry `"schema": []`, the data
flow sources use `allowSchemaDrift: true, validateSchema: false`, and the sink
uses `tableOption: autoCreate`. A renamed or reordered upstream column produces
no error at all.

**5. `allowDataTruncation: true`** in the copy translator. Over-long values are
silently cut rather than failing.

**6. `isolationLevel: READ_UNCOMMITTED`** on the supporter source — dirty reads
from a table that may be mid-write.

**7. The `utcnow()` folder path.** `wildcardFolderPath` is
`supporters/@{formatDateTime(utcnow(), 'yyyy/MM/dd')}`. It always reads *today*.
A missed or re-run execution can never pick up the day it missed, and during BST
the folder written in local time may not be the folder it looks in. Combined
with `Truncate Staging` running first, a re-run on the wrong day empties the
table and loads nothing.

**8. `marketing_consent` conversion.** Handles `'Y'` and `'N'`, then
`toInteger()` on everything else — which is where Monday's 15 text rows meet
this pipeline. Anything unexpected becomes null.

**And then the column never reaches the warehouse at all** — `marketing_consent`
is not in `selectFinal`'s `mapColumn` list, so no consent report can be built
from `dw.dim_supporter_enriched`. Same for `email` and `postcode`. Worth knowing
before you claim in the room that consent counts are affected downstream.

## Category 2 — fails, and nobody is told

**★ 9. The watermark advances on failure.** `Update Watermark` depends on
`DF_Enrich_Supporters` with `dependencyConditions: ["Completed"]`, not
`Succeeded`. The data flow fails, the watermark moves forward anyway, and next
week's run starts after data that was never loaded. **This is the question in
the exercise, and most people will read past it.**

**10. `Notify Failure` covers one activity out of ten.** It fires only on
`Copy1` failing. The data flow, the merge proc, the Power BI refresh and the
`ForEach` can all fail in silence.

**11. It notifies someone who left.** `r.byrne@example-charity.org` — and the
`Wait1` comment is signed "RB 2022". The alert has been going to an unmonitored
mailbox for years.

**12. Stale dashboards on failure.** `Refresh Power BI Dataset` depends on
`Stored procedure1` succeeding. If the merge fails, the refresh never runs and
the dashboard shows last week's numbers with a current-looking timestamp. No
alert.

## Category 1 — fails loudly (the least bad kind)

**★ 13. Truncate-then-copy with no safety net.** `Truncate Staging` empties the
table, then `Copy1` runs with `retry: 0`. If the copy fails, staging is empty
and stays empty. The smallest fix is to load into a new table and swap, or to
copy first and truncate inside the same transaction.

**14. Retries are backwards.** `retry: 3` on the trivial watermark lookup,
`retry: 0` on both copies. Exactly inverted.

**15. Seven-day timeouts** (`"timeout": "7.00:00:00"`) on activities that take
minutes. A hung run blocks the next week's schedule.

## Not failure modes, but wrong

**16. A plaintext password in source control.** `LS_AzureSql_Warehouse` has
`Password=Wint3r2022!` in its connection string, while `LS_Blob_Landing` right
underneath it correctly uses Key Vault. The contrast is deliberate — one team
knew, the other did not.

**17. `Wait1`, a 300-second sleep** used to synchronise with another pipeline,
with a comment admitting it. It works until the other pipeline gets slower.

**18. Default activity names.** `Copy1`, `Stored procedure1`, `Wait1`. Every
log line and every alert is unreadable as a result.

**19. Trigger in UTC** for an organisation operating in London, compounding the
`utcnow()` folder issue twice a year.

---

## Tracing `value_band` (exercise 1, step 2)

`aggGiving` sums `amount_gbp` per supporter → `deriveFlags` builds
`value_band` from `total_given` via a `case()` with breaks at 100 / 1,000 /
5,000 → `filterOut` **drops the row entirely** if the region is Northern Ireland
or the status is Deceased → `selectFinal` → sink, which truncates and reloads.

Two things worth drawing out:

- The banding uses `total_given` from `dw.fact_donation` with **no refund
  filter** — the same disagreement they resolved on Monday, reappearing inside
  a pipeline.
- Because `iifNull` defaults a blank status to `'Active'`, the "drop Deceased"
  filter never removes a record whose status was missing. The two rules
  interact, and neither is written down.

## "A supporter is missing from the dashboard" — the full list

In order down the pipeline: wrong folder date (7) · truncate-then-failed-copy
(13) · schema drift dropping the column that identifies them (4) · the Northern
Ireland filter (3) · the Deceased filter · the `ForEach` race, for anything
campaign-related (1) · the merge proc's own `ExcludeRegion` parameter (3 again)
· a failed refresh showing an older dataset (12).

Eight places. By hand, that is most of an afternoon.

---
