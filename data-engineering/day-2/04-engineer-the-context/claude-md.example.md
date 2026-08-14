<!--
This is the TARGET shape for the repo's CLAUDE.md after today — the "consolidator" pair edits the real
CLAUDE.md to look like this. It stays THIN: it is loaded on every prompt, so it holds pointers and hard
rules, never the content itself. The content lives in docs/ and is read on demand.
Copy the structure, not the prose — point at the docs your room actually built.
-->

# Project: Stem Cell Register (synthetic workshop repo)

Synthetic data-engineering codebase modelled on a stem-cell donor registry. All data is synthetic.

## Stack

- Azure SQL / SQL Server (T-SQL) — schema + data in `later-days/sql/`, proc in `day-1/01-hands-on-basics/`.
- Databricks notebooks (Python) in `later-days/notebooks/`; a legacy ADF Mapping Data Flow in `later-days/adf/`.

## Knowledge base (read the relevant file when a task needs it)

- **Data dictionary:** `docs/data-dictionary.md` — donor columns, types, valid ranges.
- **Glossary:** `docs/glossary.md` — domain terms (locus, workup, HLA) + not-a-typo rules.
- **Decisions (ADRs):** `docs/decisions/` — read before re-solving anything; don't re-propose rejected options.
- **Reference implementations:** `docs/reference/` — copy these patterns for new work.

## Hard rules

- Prefer set-based T-SQL over row-by-row (no cursors in reporting procs — see `docs/reference/`).
- Do **not** edit `later-days/sql/02_seed_data.sql` to "fix" data — the defects are teaching material.
- Age eligibility uses **completed years** — see `docs/decisions/0001-*`.

## Data safety (PII)

Treat `donor` PII columns (name, DOB, email, phone, postcode, `nhs_number`) as real: never paste them
into an external service; **anonymise or mask before anything leaves the machine.** Do not read the raw
data directory in bulk — work through queries/scripts, and check what you opened.
