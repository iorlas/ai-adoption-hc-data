# ADR 0001 — Store and compute money as integer minor units

- **Status:** Accepted
- **Date:** 2026-05-02

## Context

Order totals were stored as `DECIMAL(10,2)` and summed in reporting. Rounding across large aggregations
produced pennies-off totals that would not reconcile with finance, and different tools (SQL, the export
job, the BI layer) rounded differently — so the same report disagreed with itself.

## Decision

> In the context of storing and aggregating order amounts,
> facing rounding drift that broke reconciliation with finance,
> we chose to store money as **integer minor units (pence)** and compute in integers,
> neglecting a `DECIMAL` type with enforced rounding rules,
> to achieve exact, tool-independent sums,
> accepting that reads divide by 100 for display and that mixed-currency math needs explicit conversion.

## Alternatives rejected

- **`DECIMAL(10,2)` everywhere** — still drifts across engines and export formats; the exact bug we had. Rejected.
- **Floating point** — never for money. Rejected outright.

## Consequences

- `total_minor INT` is the source of truth; display layers format `total_minor / 100.0`.
- A one-off migration converted existing rows; a check enforces `total_minor >= 0`.
