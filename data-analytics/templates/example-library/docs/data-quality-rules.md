# Data-quality rules

> A rule belongs here only if breaking it means the data is **wrong for how we
> use it** — not merely different from how someone would have typed it.

**Last reviewed:** 2026-06-02 · **Owner:** Library Insight team

## Rules we keep

| # | Table | Rule | SQL predicate | Failing now | Why it matters |
|---|---|---|---|---|---|
| 1 | loans | Return date is not before loan date | `return_date < loan_date` | 4 | Produces negative loan durations, which silently drag the average down |
| 2 | loans | Loan type is a known value | `loan_type NOT IN ('ISSUE','RENEWAL','TRANSFER')` | 0 | A new value appearing means the LMS changed under us; decision 0002 depends on this vocabulary |
| 3 | items | Every item has a home branch | `home_branch IS NULL` | 61 | Items with no branch vanish from every branch breakdown without warning |
| 4 | items | Reference stock is never on loan | `is_reference AND status = 'ON_LOAN'` | 2 | Either the flag is wrong or the item left the building; both need a person |
| 5 | borrowers | Card expiry is not before registration | `expiry_date < registered_date` | 7 | Makes a borrower simultaneously new and expired; breaks any cohort analysis |
| 6 | loans | Loan references an item that exists | `item_id NOT IN (SELECT item_id FROM items)` | 23 | Loans that cannot be attributed to stock; turnover is understated by exactly this much |

## Rules we rejected, and why

| Proposed rule | Why it is noise |
|---|---|
| Borrower postcodes must be consistently formatted | Realistic messiness. We normalise on read; an alert here would fire thousands of times and teach everyone to ignore alerts |
| Every borrower must have an email | Plenty of borrowers legitimately have none. That is a service fact, not a data defect |
| Item titles must be title-cased | Cosmetic |
| Every loan must have a return date | Current loans do not have one. This rule would fire on every healthy row in the table |
| Branch codes must be two letters | `ZZ` is deliberate — see the note below |

## Things that look like defects and are not

- **`branch_code = 'ZZ'`** means "unknown branch". It is a real, intended value
  covering historic records migrated from the previous system. Excluded from
  branch breakdowns; not a defect.
- **Loans with a `NULL` return date** — those are the items currently out.
- **Borrowers with zero loans** — about 22%. Cards get made and not used.

## What we are not checking yet, and should

- Nothing validates the branch calendar that decision 0001 depends on. If a
  branch forgets to record a closure, the overdue rate for that branch shifts
  and nothing alerts. **This is the largest known gap.**
- No check that item counts reconcile against the annual stock take.
