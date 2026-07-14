# Project: Donor Registry (synthetic workshop data)

A synthetic data-engineering dataset shaped like a stem-cell donor registry. All data is synthetic
and fictional. There is no real personal data here.

## The data

- `data/donor.csv` — about 5,000 donor rows. Read it with pandas.
- `data/donor.db` — the same rows in SQLite, for running SQL queries (no server needed).
- Prefer **verifying claims against the actual rows** over trusting a summary.

## Working in this repo

- The day is organised into numbered section folders (`01-hands-on-basics/` first). Each has a README.
- Scope Claude to the files that matter for the section you are on.

## Data safety

Even though this data is synthetic, treat the donor columns (name, DOB, email, phone, postcode,
`nhs_number`) as if they were real PII: **never paste them into an external service.** Anonymise or
mask before anything leaves the machine.

## Where things live

- Our stored procedures are kept in `01-hands-on-basics/stored_procedure.sql`.
