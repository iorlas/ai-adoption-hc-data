# 0001 — Overdue is counted in branch open days, not calendar days

- **Status:** Accepted
- **Date:** 2026-02-11
- **Decided by:** Library Insight team, with the Head of Branch Services

## Context

The Branch Scorecard and the LMS's built-in overdue report disagreed. In
December the gap reached **6.1 percentage points** (LMS 19.4%, Scorecard 13.3%),
and a branch manager raised it at a service meeting as evidence the Scorecard
was wrong.

Neither figure was wrong. The LMS counts calendar days from the due date. Over
the Christmas period branches are closed for up to nine consecutive days, and a
borrower who physically cannot return an item is recorded as increasingly
overdue throughout. Smaller branches with more closure days looked worse than
larger ones for a reason that had nothing to do with their borrowers.

## Decision

> In the context of overdue reporting across 14 branches with different opening
> patterns,
> facing a measure that penalised branches for being closed,
> we chose to count overdue in **branch open days**, using the branch calendar,
> and set aside adopting the LMS's calendar-day figure,
> to achieve a measure that compares branches fairly,
> accepting that our number will never match the LMS's and that the branch
> calendar becomes a reporting dependency we have to maintain.

## Options we rejected

**Adopt the LMS's calendar-day figure.** It is the system of record and it would
have ended the argument immediately. Rejected because it makes branch comparison
meaningless, and branch comparison is the Scorecard's entire purpose. Ending an
argument by adopting the wrong number is not a resolution.

**Report both figures side by side.** Rejected after trying it for one month:
every reader asked which one to use, so we had moved the decision onto fourteen
branch managers instead of making it once.

**Exclude December.** Rejected — the problem is not December, it is every bank
holiday, every refurbishment and every staff-training closure. December was
merely where it got large enough to notice.

## Consequences

- The branch calendar (`ref.branch_open_days`) is now a reporting dependency. If
  it is not maintained, the measure silently drifts. Ownership sits with Branch
  Services and it is on their annual checklist.
- Historic Scorecards before 2026-02 used calendar days and are not comparable.
  They are marked as such in the archive.
- We will permanently disagree with the LMS report. That is intended.

## How anyone would know this was applied

The Scorecard carries a footnote — *"Overdue counted in branch open days; see
decision 0001"* — and the measure is named `Overdue Rate (open days)` in the
model, not `Overdue Rate`.

That naming is doing most of the work. The footnote gets skipped; the measure
name does not.
