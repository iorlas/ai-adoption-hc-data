# Measure definitions

> The agreed meaning of every measure we report. If two reports use the same
> word, they use the definition on this page — or they say clearly why not.

**Last reviewed:** 2026-06-02 · **Owner:** Library Insight team ·
**Decisions behind these:** `docs/decisions/`

---

## Loans issued

**In one sentence:** every time an item leaves a branch on a borrower's card,
including renewals.

**Deliberately excludes:** holds placed but never collected; inter-branch
transfers; staff loans (`borrower_type = 'STAFF'`).

**Includes something people assume it does not:** renewals. See decision 0002 —
this was contested and the reasoning is there.

**SQL**

```sql
SELECT count(*)
FROM loans
WHERE borrower_type <> 'STAFF'
  AND loan_type IN ('ISSUE', 'RENEWAL');
```

**DAX**

```dax
Loans Issued =
CALCULATE (
    COUNTROWS ( loans ),
    loans[borrower_type] <> "STAFF",
    loans[loan_type] IN { "ISSUE", "RENEWAL" }
)
```

**Where it is used:** Monthly Service Report, Branch Scorecard, the DCMS return.

**Known disagreements:** the DCMS statutory return counts renewals separately.
Our figure is therefore higher than the one we submit, on purpose. Anyone
comparing the two needs to know this, and the Monthly Service Report carries a
footnote saying so.

---

## Overdue rate

**In one sentence:** the share of current loans that are past their due date,
counted in **branch open days**.

**Deliberately excludes:** loans on items later marked lost or damaged; loans at
branches closed for refurbishment during the period.

**SQL**

```sql
SELECT
    count(*) FILTER (WHERE open_days_overdue > 0)::float / count(*) AS overdue_rate
FROM v_current_loans      -- open_days_overdue comes from the branch calendar,
WHERE status = 'ON_LOAN'; -- see decision 0001
```

**DAX**

```dax
Overdue Rate =
DIVIDE (
    CALCULATE ( COUNTROWS ( loans ), loans[open_days_overdue] > 0 ),
    CALCULATE ( COUNTROWS ( loans ), loans[status] = "ON_LOAN" )
)
```

**Where it is used:** Branch Scorecard, the quarterly stock review.

**Known disagreements:** the LMS's own built-in overdue report uses calendar
days and therefore always reports a higher figure, especially over Christmas.
**Do not compare the two.** Decision 0001 explains why we did not simply adopt
the LMS number.

---

## Collection turnover

**In one sentence:** loans per item held, over twelve months, by branch.

**Deliberately excludes:** reference stock, which cannot be borrowed and would
drag every branch's figure down.

**SQL**

```sql
SELECT b.branch_code,
       count(l.loan_id)::float / count(DISTINCT i.item_id) AS turnover
FROM items i
JOIN branches b ON b.branch_code = i.home_branch
LEFT JOIN loans l ON l.item_id = i.item_id
                AND l.loan_date >= current_date - INTERVAL '12 months'
WHERE i.is_reference = false
  AND b.branch_code <> 'ZZ'
GROUP BY b.branch_code;
```

**Where it is used:** the quarterly stock review.

**Known disagreements:** none currently. This measure exists in one place only,
which is the cheapest possible state and worth preserving.

---

## Names we have retired

| Do not say | Say instead | Because |
|---|---|---|
| "Issues" | Loans issued | Meant three different things across four reports |
| "Active borrower" | Borrowed in 12m / Card valid | Two different questions that shared one name — the exact failure this page exists to prevent |
| "Late rate" | Overdue rate | "Late" was calendar days in one report and open days in another |
