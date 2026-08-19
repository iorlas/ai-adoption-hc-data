# Answers — 2 · An inherited notebook

**FACILITATOR ONLY. Never on screen.**

The file: `later-days/notebooks/donor_profiling.py`, 120 lines, 18 cells.

## The clusters that are really there

| Cluster | Cells | Varies | Constant |
|---|---|---|---|
| **Null counts** | 4 (`email`, `phone`, `postcode`, `nhs_number`) | the column | count total, count nulls, print a percentage rounded to 1dp |
| **Distinct counts** | 3 (`status`, `ethnicity`, `sex`) | the column | `groupBy().count().orderBy(desc)` and show |
| **Text standardisation** | 3 (`postcode`, `status`, `ethnicity`) | the column **and the rule** | `withColumn` of a trim/case/collapse expression |
| **Business rule** | 1 (age at registration) | nothing — it is a one-off | — |

A good answer is **four functions, not three.** The trap is in row 3.

## The trap in row 3 — the one to hold the room for

The three standardisation cells look identical and are not:

```
postcode    upper + trim + collapse inner whitespace
status      initcap + trim                              <- different case rule
ethnicity   trim + collapse whitespace                  <- no case rule at all
```

Claude will very often propose a single `standardise(df, col)` with a `mode=`
flag, or worse, apply one rule to all three. **That is a behaviour change
hidden inside a refactor**, and it is precisely the class of bug that makes
teams distrust AI refactoring.

The good shapes are either three small named functions
(`normalise_postcode`, `normalise_status`, `normalise_label`) or one function
taking the transformation as an argument. Both are defensible. A boolean flag is
not.

**If nobody hits this, ask directly at minute 20:** *"are those three cells
doing the same thing?"*

## The other findings, in the order they usually surface

**1. `display(donor)` on the last line.** This is the PII line the README hints
at. It renders every column of every row — names, dates of birth, emails,
phones, postcodes, NHS numbers — into notebook output, which is **saved with the
notebook, versioned in Git, and visible to anyone with workspace read access.**
Nobody flags it in review because every notebook ends this way.

This is Day-4's governance segment arriving early. Take it: *the model was never
the risk here; the notebook was.*

**2. `n_total = donor.count()` recomputed in every null cell.** Four full scans
where one would do. On 5,000 synthetic rows it is invisible; on the real table
it is the reason the notebook takes forty minutes.

**3. `donor` is rebound cell by cell.** Cells 13–15, and again in cell 17, each
do `donor = donor.withColumn(...)`. Run them out of order, or twice, and you get a
different DataFrame — the classic notebook hazard. Moving to functions that
return a new frame fixes it as a side effect, which is worth naming out loud.

**4. The `_clean` columns are never consumed.** `postcode_clean`, `status_clean`
and `ethnicity_clean` are computed and then ignored — the age check uses the raw
columns, and the final `display` just dumps everything it is handed. Somebody
meant to come back.

**5. The distinct-count cells will show `Activ` next to `Active`** if run against
the real table — 20 rows. **Do not resolve it here.** Part 4 turns on somebody
noticing that a filter written as `status == 'Active'` silently drops them; if
it surfaces now, credit whoever spotted it and say it comes back after the
break.

**6. Age at registration: `floor(datediff(...) / 365.25)`.** Close enough to be
defensible, wrong for a handful of rows near a birthday, and *different* from
Day 2's `DATEDIFF(YEAR, ...)` bug in the stored procedure — which was wrong by
up to a year. Worth a sentence if it comes up: the registry has a real 16–30
rule, and two systems disagree about who is 30.

## Why there is no green check, and what to say about it

Nobody can run Spark. If someone objects that an unverifiable refactor is
exactly what these three days told them not to trust — **agree with them,
loudly.** Then make the real point: this is the situation they are in at work
whenever the notebook runs for forty minutes against production. The
professional answer is not "run it and see", it is a written equivalence
argument plus a review, which is what step 4 produces.

If you want a stronger close, offer the honest next step: *the version of this
you take home runs the old and new notebook on one day of data and diffs the
outputs.* That is the real gate; today's is the argument that earns you
permission to try it.

## Time

Step 3 is where it goes long — people start tuning docstrings. Call it at
minute 30 whether or not the module is finished; **step 4 is the deliverable
and it needs its five minutes.** The module being incomplete costs nothing; the
equivalence table never being written costs the whole part.
