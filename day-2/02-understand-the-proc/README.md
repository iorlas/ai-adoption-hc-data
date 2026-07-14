# Stage 02 — Understand the proc: README, bug, fix, test

You've inherited `../../day-1/01-hands-on-basics/stored_procedure.sql` — `usp_DonorRegistryReport` and
`fn_AgeAtRegistration`. No docs, a cursor doing per-row subqueries, `SELECT *`, and a **latent bug**.
Make it legible, prove it's broken, fix it safely.

## Steps

1. **Reverse-engineer a README.** With the proc in scope:
   > `@../../day-1/01-hands-on-basics/stored_procedure.sql explain what this returns and how, then`
   > `draft a short README/header for it.`
   Stay sceptical: **does the README actually match the SQL?** This README seeds the reference-impl doc
   you'll capture in Stage 04.

2. **Find the bug.**
   > `is the age-at-registration logic correct at the boundaries? show me a donor it gets wrong.`
   `fn_AgeAtRegistration` uses `DATEDIFF(YEAR, …)`, ignoring month/day — a donor born 1998-12-01 who
   registered 2016-01-05 is scored **18** but is really **17**. The proc filters `BETWEEN 16 AND 30` on
   this, so the eligibility report admits/excludes the wrong donors at the edges.

3. **Fix it + write a test.** Ask for a **completed-years** expression *and a boundary test* that proves
   it (a donor whose birthday falls after the registration date in the year). Record the decision as an
   ADR — copy `adr-template.md` into `docs/decisions/0001-…` in Stage 04.

## Governance touch-point

The fix runs against data *via a tool* (a query/script); **the model sees the SQL, not the donor rows.**
That's the boundary that lets you do this on real, PII-laden systems.

## Done when

You have a proc README, can name the bug, and have a fix + a passing boundary test on screen.
