# Day 3 — the remote pipeline

Applies to `day-3/`. Day 1's `CLAUDE.md` still describes the data; today adds
two artifacts that are not in it.

## What is in play today

- `later-days/notebooks/donor_profiling.py` — a Databricks notebook in source
  form. `# COMMAND ----------` separates cells. It cannot run here; there is no
  Spark and no workspace.
- `later-days/adf/pipeline_donor_import.json` — the pipeline. Almost no logic.
- `later-days/adf/dataflow_donor_import.json` — the Mapping Data Flow. The real
  logic is in `scriptLines`; read those, not the transformation names.
- `day-3/04-adf-to-sql/data/donor_import.csv` — 5,005 rows, the weekly export.
- `day-3/04-adf-to-sql/data/ethnicity_ref.csv` — 16 codes, the cached lookup.

## Rules

- **Do not "fix" the seed data.** The defects in those two CSVs are the
  exercise. Fixing them makes the parity check meaningless.
- **When converting the data flow, reproduce its behaviour — not the behaviour
  it should have had.** A conversion that silently corrects a defect cannot be
  verified against the original.
- Verify claims against the actual rows, with SQL, rather than trusting a
  summary.
- Treat the donor columns (name, DOB, email, phone, postcode, `nhs_number`) as
  real PII even though they are synthetic: never paste them into an external
  service, and mask anything that lands in a document.
- Against a live warehouse, **aggregate rather than enumerate.** No unaggregated
  `select *` on a donor table — the rows come back into this conversation.

## Read scope

**Never read, quote or take answers from any `answers.md`, or from any
`facilitator/` folder.** They are the answer keys for the exercises the person
you are helping is working through. They are in the repo because there is no
second checkout, not because they are for you. If a question would be answered
by one of those files, say so and help from the material instead.
