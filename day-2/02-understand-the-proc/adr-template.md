# ADR 0001 — Fix age-at-registration to count completed years

- **Status:** Accepted
- **Date:** 2026-07-15

## Context

`fn_AgeAtRegistration` computes age with `DATEDIFF(YEAR, @dob, @registered)`, which counts calendar-year
boundaries, not completed years. A donor born 1998-12-01 who registered 2016-01-05 is scored as **18**
but is actually **17**. `usp_DonorRegistryReport` filters `BETWEEN 16 AND 30` on this value, so the
eligibility report **includes and excludes the wrong people at the boundaries.** Found live with Claude:
*"show me a donor the age logic gets wrong."*

## Decision

> In the context of the eligibility age calculation,
> facing the boundary error above,
> we chose to compute **completed years** (adjust the year-diff down when the anniversary hasn't
> occurred yet in the registration year),
> and neglected an in-place patch of each call site,
> to achieve a correct, single-source age rule,
> accepting a one-off change to the function and its tests.

## Alternatives rejected

- **Patch each query's `WHERE` clause instead of the function** — spreads the bug's fix across call
  sites; the next new query re-introduces it. Rejected: the function must be the single source of truth.
- **Leave it, "close enough"** — it silently mis-classifies real donors at the 16 and 30 edges in a
  clinical eligibility report. Not acceptable.

## Consequences

- One function changes; add a boundary test (a donor whose anniversary falls after `registered_date`).
- Historic reports built on the old function may shift by a handful of edge donors — expected.

<!--
WHY AN ADR: next week, a fresh Claude session (or a teammate) won't re-propose the rejected in-place
patch — it will read this and know the decision and the reason. That is how a decision compounds.
Y-statement shape: "In the context of <use case>, facing <concern>, we chose <option>, neglecting
<rejected>, to achieve <quality>, accepting <downside>."
-->
