# Stage 06 — The bridge: Databricks + ADF

The throughline to Days 3–4: **nothing conceptually changes.** You've done the same job through two
access paths already — a CSV file and a database over MCP. Databricks and ADF are just **more access
paths and another knowledge home.** The context engineering and the verification habit transfer
unchanged.

```
CSV (file)  →  MCP (database)  →  Databricks + ADF (Wed/Thu)
        same understand → fix → capture → verify loop
```

## Try it now — no workspace needed

`../../later-days/notebooks/donor_profiling.py` is a Databricks notebook sitting locally.
> `@../../later-days/notebooks/donor_profiling.py document what this notebook does, and flag one thing`
> `you'd refactor.`

Same move as the proc in Stage 02 — understand an inherited artifact, then improve it.

## What Days 3–4 add

- **Databricks:** notebook refactoring against a live workspace + Genie (remote AI).
- **ADF ↔ Databricks coexistence:** read the ADF Mapping Data Flow (`../../later-days/adf/`) *and* the
  notebook, document both, and trace how data moves between them.

The `docs/` KB and the reference-implementation habit you built today are what make that tractable —
you'll point Claude at them, not re-explain the project each time.

## Reference illustration

Databricks, [What is medallion architecture?](https://www.databricks.com/blog/what-is-medallion-architecture) — the **Raw → Bronze → Silver → Gold → BI/ML** diagram. Reframes today's access-path ladder (CSV → MCP/DB → Databricks/ADF) as the same habits at each rung; sets up Days 3–4.
