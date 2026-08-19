# Answers — 4 · Mapping Data Flow to SQL

**FACILITATOR ONLY. Never on screen.**

## The reference conversion

This passes `parity.py` green. Keep it in a scratch buffer; do not put it on
screen before minute 30.

```sql
select
  i.registry_id,
  upper(substr(trim(i.first_name), 1, 1)) || lower(substr(trim(i.first_name), 2)) as first_name,
  upper(substr(trim(i.last_name), 1, 1))  || lower(substr(trim(i.last_name), 2))  as last_name,
  i.date_of_birth,
  upper(trim(i.sex)) as sex,
  i.email,
  i.phone,
  upper(regexp_replace(trim(i.postcode), '\s+', ' ', 'g')) as postcode,
  i.nhs_number,
  r.ethnicity_label as ethnicity,
  i.registered_date,
  i.status
from imp i
left join ref r on i.ethnicity_code = r.ethnicity_code
where i.status = 'Active'
```

## The gate numbers, and where each comes from

| Number | From | If they miss it |
|---|---|---|
| **5,005** source rows | `donor_import.csv` | — |
| **2,885** rows out | `filter(status == 'Active')` | Filtered on the cleaned column, or on `upper(status)`, or forgot the filter |
| **23** rows with no ethnicity label | code `Z99` appears in the export and not in the lookup; ADF's `lookup` is a **left** join | **0 means they wrote an inner join** — the most common error, and the most dangerous |
| checksum match | the four cleaning rules | Usually `initCap` applied to the whole string, or `upper` not applied to `sex` |

Other true numbers, if asked — **all of these are over the full 5,005-row
export, before `KeepActive`**, so they will not match a count run against a
green view (which holds 1,181 changed postcodes, not 2,036):
- 51 rows carry the unknown `Z99` code in total; 23 of them survive the filter
- 2,036 rows have a postcode the cleaning rules change
- 1,663 rows have a lower-case `sex`; 15 rows have no `sex` at all
- 200 rows have no email

## The three buckets

**(a) Converts cleanly**

| Transformation | Becomes |
|---|---|
| `CleanNames` — trim/initCap/upper | expressions in the SELECT |
| `BuildPostcode` — upper + collapse whitespace | an expression in the SELECT |
| `KeepActive` — `filter(status == 'Active')` | a WHERE clause |
| the two `source` readers | the FROM and the JOIN |

**(b) Converts, but the semantics need care**

| Transformation | The care |
|---|---|
| `LookupEthnicity` | It is a **left** join, not an inner one. And `multiple: false, pickup: 'any'` means that if the reference table ever gained a duplicate code, ADF would pick an arbitrary row and SQL would return both — a non-deterministic behaviour you cannot faithfully reproduce, only detect |
| `broadcast: 'auto'` | An execution hint with no meaning in a view. Harmless to drop, but say out loud that you dropped it |
| the cleaning expressions themselves | `initCap` and `regexReplace` are not T-SQL — see step 5 below |

**(c) No equivalent in a view** — there are three, and the third is the expensive one

1. **`AssignSurrogateKey` — `keyGenerate(output(donor_id as long), startAt: 1L)`.**
   A view has no state, so it cannot allocate a key. The replacement is an
   IDENTITY column or a SEQUENCE **on the target table**, which means the target
   table has to exist and be owned by something other than the view.
2. **`allowSchemaDrift: true`** on both source and sink. A view has a fixed
   column list by definition. Under drift, ADF carries a new column through to
   the sink; the view silently ignores it. Nothing errors, which is what makes
   it worth naming.
3. **`UpsertOnRegistryId` — `alterRow(upsertIf(true()))` plus the sink's
   `upsertable: true, keys: ['registry_id']`.** **A view cannot write.** This is
   the expensive one: the view is only ever half the migration. The other half
   is a `MERGE` on `registry_id`, and something that runs it on a schedule — a
   stored procedure and an ADF Copy activity, or a job. Anyone who says "we'll
   convert the flows to views" without this has not costed the work.

**If the room only finds two, it is almost always number 2 they miss** — schema
drift is invisible until it bites. Ask: *"what happens on Monday when the source
system adds a column?"* (Number 3 is the expensive one, but it is rarely the
missed one: a sink that upserts is hard to overlook.)

## Step 4 — the `Activ` defect

20 rows. The flow's filter drops them; a faithful conversion drops them too.

**Do not let the room "fix" it in the view.** The argument, if it comes up, is
the one on the participant page: a conversion that changes behaviour destroys
your only means of telling a migration bug from an intentional change, and it
makes parity unachievable by construction. Faithful first, ticket second.

The distinct-count cells in part 2's notebook show the same twenty rows. If
someone spotted them before the break, name them now — it is a good moment and
it costs nothing.

## Step 5 — the T-SQL re-target

Three changes; two have no straightforward equivalent.

| DuckDB | Azure SQL | |
|---|---|---|
| `\|\|` | `+` | Straight swap, but T-SQL's `+` yields NULL if either side is NULL, where `CONCAT()` does not. With names this is theoretical; with optional columns it is a live bug |
| `initcap`-style expression | **nothing** | T-SQL has no INITCAP. `UPPER(LEFT(x,1)) + LOWER(SUBSTRING(x,2,LEN(x)))` covers single-word names and gets `McDonald` and `O'Brien` wrong. ADF's `initCap` capitalises **every word**, so it gets them wrong differently. Two systems, two wrong answers, and they do not agree |
| `regexp_replace(x, '\s+', ' ')` | **nothing portable** | No regex in the classic T-SQL surface. The usual trick is a chain of `REPLACE` calls, which works for collapsing runs of spaces and is unreadable. Tabs and non-breaking spaces are not covered by it |

**The point to land:** for a bulk conversion, this table *is* the project plan.
Build it once across all the flows, and you know which ones are cheap.

## A finding worth surfacing if there is time

`BuildPostcode` collapses whitespace but cannot restore a missing one. Rows
where the export dropped the space come out as `G12BH`, not `G1 2BH` — the
cleaning rule looks like it normalises postcodes and only half does. About one
row in four in this export has ragged spacing.

This is the same shape as the `Activ` defect: a cleaning step that was written
against the data as it looked in 2019.

**The numbers:** 2,024 rows of 5,005 have no space at all — those are the ones
the rule cannot save — and another 994 have a doubled space, which it does fix.
Three rows in five arrive with ragged spacing.

**One thing this data does not test:** no postcode here has *two* separate runs
of whitespace, so a non-global `regexp_replace` passes parity even though it
only fixes the first run. The `'g'` is right and this dataset does not earn it.
Worth a sentence if someone asks why it is there.

## What goes wrong

**`Catalog Error: initcap does not exist`.** The expected first failure, and it
will be most of the room. The flow's first rule is `initCap`, everybody writes
`initcap(...)`, and DuckDB has no such function. **Do not hand over the fix
until they have named the problem** — it is a free preview of step 5, where the
same function turns out to be missing from T-SQL too. The shape that works:
`upper(substr(trim(x), 1, 1)) || lower(substr(trim(x), 2))`.

**They ask Claude to convert before reading the flow.** It will produce
plausible SQL with an inner join and no filter, and it will look right. If it
happens, let the parity check fail and use it — that is the entire Day-1 lesson
landing on Day-3 material.

**`uv run parity.py` fails with a module error.** They are running `python
parity.py`. Same as Day 1: `uv` builds the environment, plain Python does not.

**Someone edits the CSVs.** Same rule as every day: do not fix the seed data.
`uv run ../facilitator/generate_day3_data.py` regenerates both files exactly.

**It runs long.** It is the biggest part of the day and it is the client's
headline ask, so protect it: steps 1–3 are the part that must happen. If you are
at minute 38 with people still failing parity, put the reference SQL on screen,
walk the three gates, and hand steps 4 and 5 to the take-home. **Do not skip
step 4** — the "faithful, then ticket" principle is the most transferable thing
in the day; three minutes of talking covers it.

## The game — card answers

| Card | Verdict | The sentence |
|---|---|---|
| 1 `filter(status == 'Active')` | **(a)** | A WHERE clause. The only trap is the one they just met: it inherits whatever the source data does wrong |
| 2 `derive(email = lower(trim(email)))` | **(a)** | An expression in the SELECT. `lower` and `trim` both exist in T-SQL, which makes it cheaper than the name and postcode rules |
| 3 `alterRow(upsertIf(true()))` | **(c)** | A view cannot write. You need a `MERGE` on `registry_id` and something that runs it |
| 4 `lookup(..., multiple: false, pickup: 'any')` | **(b) — argue about it** | The join converts; the *arbitrary pick* does not. See below |
| 5 `keyGenerate(...)` | **(c)** | No state in a view. IDENTITY or a SEQUENCE on the target table |
| 6 `allowSchemaDrift: true` | **(c)** | A view has a fixed column list. New source columns are silently dropped, with no error |

**Card 4, why both sides are right.** One camp says (a): it is a left join, write
the left join, done. The other says (c): if the reference table ever holds two
rows for a code, ADF returns one arbitrary row and SQL returns two — the row
count changes, and no SQL construct reproduces "pick any one, I don't care."

The resolution worth landing: **it converts today and is not guaranteed to keep
converting.** The honest deliverable is the left join **plus a uniqueness
constraint or a check on the reference table**, so the case that would break
parity can never arise. That is the difference between converting a flow and
migrating one.
