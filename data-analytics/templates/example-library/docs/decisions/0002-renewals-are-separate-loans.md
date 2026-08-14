# 0002 — A renewal counts as a loan

- **Status:** Accepted
- **Date:** 2026-03-24
- **Decided by:** Library Insight team

## Context

"Issues" appeared in four reports and meant three different things. Renewals
were included in two of them and excluded in the others, and nobody could say
which was intended because it had never been decided — each report had simply
inherited whatever its author assumed.

The gap is not small: renewals are **31%** of all loan events. Any two reports
that differ on this differ by roughly a third.

The trigger was a funding submission where two figures from the same team,
covering the same period, differed by 28% and had to be reconciled in a hurry.

## Decision

> In the context of every measure that counts loans,
> facing four reports using one word for three different things,
> we chose to count a renewal as a loan event, and to name any measure that
> excludes them explicitly (`Loans issued (first issue only)`),
> and set aside excluding renewals by default,
> to achieve one default that every report shares,
> accepting that our headline figure is higher than the DCMS statutory return,
> which counts renewals separately.

## Options we rejected

**Exclude renewals by default.** Genuinely arguable — a renewal is not a new
borrower choosing a new item, and for stock-selection purposes that distinction
matters. Rejected because the majority of uses are activity-and-demand
reporting, where a renewal is real usage, and because it would leave our
headline further from the DCMS return rather than closer.

**Report both everywhere.** Rejected for the same reason as in decision 0001:
publishing two numbers moves the decision onto the reader.

**Leave it to each report.** This was the status quo, and the status quo cost a
day of reconciliation during a funding submission.

## Consequences

- All four reports were changed to the common default, in one release.
- Two 2025 figures already published externally used the other definition. They
  were not restated; the difference is noted where they appear.
- `Loans issued (first issue only)` exists for stock selection and is the only
  measure permitted to exclude renewals.

## How anyone would know this was applied

Only from the measure name. There is no marker on the number itself.

This is a known weakness. If someone lifts the figure into a slide, nothing
travels with it. The mitigation we chose is the naming convention rather than a
technical control, and it depends on people using the measure rather than
writing their own — which is exactly what happened last time.
