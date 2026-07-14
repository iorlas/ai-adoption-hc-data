# Exercise — SQL optimisation through MCP: several candidates, compared

One problem statement, several candidate queries, judged on **readability** *and* **plan** (actual
`STATISTICS IO/TIME`, not a guess). This is how you optimise honestly: you measure, you don't assume.

## The problem statement

`usp_DonorRegistryReport` builds an eligibility report by opening a **cursor** over candidate donors and
running three correlated subqueries **per row** (loci typed, times matched, donations made). It works —
and it does not scale. Your job: produce a faster query that returns the *same* result set.

## Steps

1. **Ask for candidates — more than one.**
   > `@day-1/01-hands-on-basics/stored_procedure.sql rewrite usp_DonorRegistryReport without the cursor.`
   > `Give me two or three different set-based approaches (e.g. a single multi-join with COUNT(DISTINCT),`
   > `and pre-aggregated CTEs). For each, note the readability trade-off.`

2. **Compare on readability.** Which reads clearly? A multi-join with `COUNT(DISTINCT ...)` corrects for
   fan-out but hides *why*; pre-aggregated CTEs name each metric once and are easy to verify. Pick with
   your eyes first.

3. **Compare on plan — measure, don't assume.** Run each candidate against the database (through the
   MCP connection / your SQL tool) wrapped in:
   ```sql
   SET STATISTICS IO ON; SET STATISTICS TIME ON;
   -- candidate here
   ```
   Read off **logical reads** and **elapsed time**. Run the original cursor version the same way (bound
   it to a recent window like `@registered_since = '2025-01-01'` so it finishes).

4. **Decide, and write down why.** The winner becomes your reference implementation (Exercise: capture
   the KB). Record the decision — including the numbers — so nobody re-litigates it.

## What you're really learning

- **"Optimise it" is not one answer** — it's candidates you compare on evidence.
- **The plan is the evidence.** Logical reads and elapsed time turn "feels faster" into a number.
- **Readability is a real axis**, weighed alongside speed — the query a human can verify is worth points.
- The model reads and runs SQL through a tool; the **donor rows never enter the model.**
