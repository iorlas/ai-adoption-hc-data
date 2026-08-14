# Project: Borough Library Service — reporting

Loans, holds, and branch activity for 14 branches. Data in `data/` (CSV
extracts from the LMS, refreshed nightly). Reports in `reports/`.

## Knowledge base — read the relevant file when a task needs it

- **Measure definitions:** `docs/measure-definitions.md` — the agreed meaning of
  every reported measure, with SQL and DAX.
- **Data-quality rules:** `docs/data-quality-rules.md` — what we check, and what
  we deliberately do not.
- **Decisions:** `docs/decisions/` — read before re-solving anything. Do not
  re-propose an option recorded as rejected.

## Hard rules

- **A renewal is a separate loan event** (decision 0002). Any measure counting
  loans includes renewals unless it says otherwise in its name.
- **Overdue is measured in branch open days, not calendar days** (decision
  0001). Never `DATEDIFF` on raw dates for anything overdue-related.
- `branch_code` `ZZ` means "unknown branch", not a real branch. Exclude it from
  branch breakdowns and say so in the note.
- Prefer SQL. Show the query alongside any number.
- If a term is ambiguous, ask rather than choosing a definition.

## Data safety

Borrower records are personal data. Never write a real borrower name, card
number, or address into a document or a commit — mask every example.

<!--
NOTE FOR THE READER, not part of the file:
This is about 25 lines and it is meant to be. Every message pays for it.
Everything with depth is one pointer away, read only when needed.
-->
