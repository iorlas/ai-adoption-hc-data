# Project: Bookshop orders warehouse (example)

A small analytics warehouse over an online bookshop's orders. Example repo for the workshop — all data
is synthetic. This file is what a *good* CLAUDE.md looks like: thin, pointers and hard rules only.

## Stack

- SQL Server (T-SQL) — schema and reporting procs in `sql/`.
- dbt models in `models/`; a nightly load job in `jobs/`.

## Knowledge base (read the relevant file when a task needs it)

- **Data dictionary:** `docs/data-dictionary.md` — `order` columns, types, valid ranges.
- **Glossary:** `docs/glossary.md` — domain terms (GMV, net vs gross, fulfilment).
- **Decisions (ADRs):** `docs/decisions/` — read before re-solving anything; don't re-propose rejected options.
- **Reference implementations:** `docs/reference/` — copy these patterns for new work.

## Hard rules

- Money is stored and computed in **integer minor units (pence)** — never float or `DECIMAL`. See `docs/decisions/0001-*`.
- `order.status` joins the `order_status` lookup — never compare against free-text strings. See `docs/decisions/0002-*`.
- Prefer set-based T-SQL over row-by-row.

## Data safety (PII)

Treat `customer_email` and `ship_address` as real PII: never paste them into an external service, and
**mask before anything leaves the machine.** Work through queries and scripts, not bulk reads of the raw
source, and check what you opened.
