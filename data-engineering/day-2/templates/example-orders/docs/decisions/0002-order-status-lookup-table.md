# ADR 0002 — Model order status as a lookup table, not free text

- **Status:** Accepted
- **Date:** 2026-05-09

## Context

`order.status` was a free-text `VARCHAR`. Typos (`Shpped`), casing variants (`paid` / `Paid`), and
ad-hoc new values crept in on import, so status filters silently missed rows and every report
re-invented its own list of "valid" states.

## Decision

> In the context of representing order lifecycle state,
> facing free-text drift that made status filters unreliable,
> we chose a normalised `order_status` lookup table with `order.status` as a foreign key,
> neglecting a `CHECK` constraint on a free-text column,
> to achieve a closed, referable set of states,
> accepting that adding a state now means an insert into the lookup — a governed feature, not a cost.

## Alternatives rejected

- **`CHECK` constraint on the string column** — pins the values but still stores redundant text, and casing bugs re-appear on the next import. Rejected.
- **Leave it free text** — the status quo that caused the missed-rows bug. Not acceptable.

## Consequences

- `order.status TINYINT` FKs to `order_status(code)`; joins replace string comparisons.
- New states are governed: one reviewed row in the lookup, treated like a schema change.
