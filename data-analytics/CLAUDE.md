# Project instructions

> **This file is deliberately thin.** On Monday morning it tells Claude almost
> nothing, and you will see it guess as a result. During Session 3 you fill it
> in — and then we run the same prompt again and compare. Do not skip ahead.

## What this is

A synthetic supporter-analytics dataset for a UK charity. Five CSVs in `data/`,
two Power BI report definitions in `reports/`, one Azure Data Factory pipeline
in `adf/`.

## How to query the data

The CSVs are queried in place with DuckDB — there is no database server.

```bash
uv run --with duckdb python -c "import duckdb; print(duckdb.sql(\"SELECT count(*) FROM 'data/supporters.csv'\"))"
```

Run it from the `data-analytics` folder — the paths are relative to where you
are. On Windows use the **Git Bash** terminal rather than PowerShell; PowerShell
does not accept `\"` as an escaped quote and the command will fail there.

Prefer SQL over Python for anything to do with the data. If you need to run a
query, write the SQL, run it through DuckDB, and show me both the query and the
result.

## Rules

- **Never read, quote or take answers from `facilitator/`, from any
  `answers.md`, or from `session-4/fallback/`.** Those are worked solutions to
  the exercises in this repo. If a question could be answered from one of them,
  answer it from SQL you actually ran against `data/` instead — and if you have
  already looked, say so rather than presenting it as your own finding.
- **All data here is synthetic.** Never invent an example that looks like a real
  person's record in any document you write.
- **Do not edit anything in `data/`.** The defects in it are deliberate.
- Show me the SQL you ran, not just the answer.
- If a term is ambiguous, ask rather than choosing a definition for me.

## Definitions

<!-- Session 3 fills this in. Right now Claude has to guess, and it will. -->

_TODO — see `session-3/04-shared-definitions/`._
