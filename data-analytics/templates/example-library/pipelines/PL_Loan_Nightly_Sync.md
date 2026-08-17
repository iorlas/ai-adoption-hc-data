# PL_Loan_Nightly_Sync

*A worked example, for a different organisation — a public library service. Read
it **after** you have written yours, not before.*

Documented 2026-03-04 by the team who inherited it. Original author left in 2023.

## What it is for

Moves yesterday's loans, returns and renewals from the branch system into the
reporting warehouse, so the morning dashboards are current by 07:00.

`[inferred]` The 07:00 target is not in the pipeline — it comes from the
dashboard refresh that runs at 07:15 and the trigger time chosen to clear it.

## Schedule and trigger

Nightly, 03:30 UTC. **The trigger is UTC, not local**, so through British Summer
Time it fires at 04:30 local. Nothing downstream depends on the exact minute.

No catch-up. A missed night is simply missed — see *If it fails overnight*.

## Activities, in order

| # | Activity | What it does | If it fails |
|---|---|---|---|
| 1 | `Lookup LastSync` | Reads the high-water mark from `etl.watermark` | Stops the run. Loud |
| 2 | `Truncate Staging` | Empties `stg.loan` | Stops the run. Loud |
| 3 | `Copy Loans` | Branch DB → `stg.loan`, rows newer than the watermark | Stops the run. Loud |
| 4 | `DF_Enrich_Loans` | The data flow, below | Stops the run |
| 5 | `Update Watermark` | Writes today's date into `etl.watermark` | Silent |

## The data flow

Joins `stg.loan` to `dim_member` and `dim_item`, derives `overdue_days` and a
`loan_band`, drops loans from staff accounts, and writes to `dw.fact_loan`.

The sink truncates. **There is no incremental merge** — every run replaces the
whole table from whatever staging holds.

## Where each output column comes from

| Output column | Source | Notes |
|---|---|---|
| `loan_id`, `member_id`, `item_id` | `stg.loan` | straight through |
| `branch_name` | `dim_branch` | left join; unknown branches arrive as null |
| `overdue_days` | derived | `daysBetween(due_date, returned_date)`, negative if returned early |
| `loan_band` | derived | `case()` at 7 / 21 / 60 days |
| `member_age_band` | `dim_member` | `[inferred]` bands look like the 2019 annual report's |

**Not carried through:** `member_postcode`, `item_cost`, `renewal_count`. They
exist in staging and stop there, so nothing downstream can report on them.

## Hardcoded decisions and exclusions

- **Staff accounts excluded** — `member_type != 'STAFF'`, in the data flow.
  `[inferred]` presumably so lending figures reflect the public. Not recorded.
- **Branch 14 excluded** — hardcoded by id, no comment. Branch 14 closed in 2021.
  `[inferred]`, from the closure date matching the last commit.
- **Null `returned_date` treated as "still out"** rather than "unknown".

## Known weaknesses

1. **`Lookup Active Members` has no `firstRowOnly: false` guard, and ADF caps a
   lookup at 5,000 rows.** Membership passed 5,000 in March. The run still
   succeeds; members past the cap are simply never enriched, and no count
   anywhere reveals it. **Succeeds with wrong data** — the worst category.
2. **The trigger is set in `Europe/London`, not UTC.** On the October clock
   change the 01:30 run fires twice, and `Copy Loans` is not idempotent, so
   `loan_event` gains one duplicated night per year. Someone reconciles it by
   hand each autumn; this page is the only place that is written down.
3. **`renewal_fee_pence` arrives as text and is cast with schema drift on**, so a
   value carrying a stray currency symbol becomes null instead of failing. The
   nulls are then summed as zero in branch revenue.
4. **The enrichment step has no alerting at all.** The copy is monitored; the
   transformation producing every derived column is not.

## If it fails overnight

The dashboards show **yesterday's** numbers with no warning banner — they do not
know the load failed.

Re-running is safe on any normal date — the sink is a full replace keyed on
`loan_date`, so a repeat run gives the same table. **Do not** re-run across the
October clock change without checking `loan_event` for duplicates first.
