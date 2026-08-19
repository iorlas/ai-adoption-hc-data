# 4 — A Mapping Data Flow, converted, and the wall behind it

**45 minutes, hands-on**
*5 min read the pipeline · 8 min what it does · 7 min what converts · 18 min write it and prove it · 7 min re-target and write it down.*

> **Who does what:** **▸ We run it first, then you** on step 1, **▸ Your turn**
> from step 2, **▸ Together** for the wall at the end. No workspace, no ADF
> instance, no Azure. Everything here is files on your laptop.

## Why it is here

Adrian's June ask, close to verbatim: *convert legacy ADF Mapping Data Flows to
Azure SQL views, in bulk.* This is one of them, end to end, with a check that
either goes green or does not.

And this part is where I stop being encouraging. **Some of that flow does not
convert.** Not "is harder to convert" — has no equivalent. Finding out *which*
parts, and being able to say so in a sentence, is worth more than a clean
conversion, because it is what makes a bulk-conversion plan credible instead of
optimistic.

## What is in play

**Scene.** Claude Code in the `data-engineering/` folder, fresh conversation.
Four files, and you will touch two of them:

```
later-days/adf/pipeline_donor_import.json     the pipeline — 20 lines, does almost nothing
later-days/adf/dataflow_donor_import.json     the Mapping Data Flow — the real logic
day-3/04-adf-to-sql/data/donor_import.csv     the weekly export it reads   (5,005 rows)
day-3/04-adf-to-sql/data/ethnicity_ref.csv    the lookup it joins to       (16 codes)
```

You write **`day-3/04-adf-to-sql/view.sql`** and check it with
**`uv run parity.py`**.

> **About the check.** `parity.py` runs your SQL over those two CSVs with DuckDB,
> because nobody in this room has an Azure SQL to hand at 2pm. The SQL dialect
> is nearly identical for what you are about to write, and **step 5 is where you
> re-target it to T-SQL and find the three functions that differ.** The check is
> real; the engine is a stand-in, and I would rather say so than pretend.

## Step 1 — the pipeline, then the flow

**▸ We run it first, then you.**

> @later-days/adf/pipeline_donor_import.json what does this pipeline do?

Twenty lines, one activity. **The pipeline is not where the logic is** — and
that is true of most of yours. Then:

> @later-days/adf/dataflow_donor_import.json walk me through this data flow one
> transformation at a time, in order. For each one: what it does to the data,
> and which script line does it. Do not suggest a SQL conversion yet.

Read `scriptLines` yourself alongside the answer. Six transformations, two
sources, one sink.

## Step 2 — which parts convert, and which do not

**▸ Your turn.** Before writing any SQL:

> Sort those transformations into three buckets: (a) converts to a SQL view
> cleanly, (b) converts but the semantics need care, (c) has no equivalent in a
> view at all. For every item in (b) and (c), say exactly what is lost.

Then challenge it, because a model asked to convert will convert:

> For each thing in bucket (c) — what would I have to build instead, and where
> would it run?

**Write the three lists down.** They are the deliverable of this step and they
are what a migration plan is actually made of. There are three items in bucket
(c). If you only found two, you are missing the expensive one.

## Step 3 — write the view

**▸ Your turn.**

> Write the bucket-(a) and bucket-(b) parts as a single SELECT into
> `day-3/04-adf-to-sql/view.sql`. Two tables are registered: `imp` (the weekly
> export) and `ref` (the ethnicity lookup). Return exactly these columns:
> registry_id, first_name, last_name, date_of_birth, sex, email, phone,
> postcode, nhs_number, ethnicity, registered_date, status. Match the flow's
> behaviour, not what you think the behaviour should be.

That last sentence is load-bearing. Come back to it in step 4.

Then, from `day-3/04-adf-to-sql/`:

```bash
uv run parity.py
```

Three gates, and the check tells you which one you missed:

| Gate | |
|---|---|
| **2,885 rows** | the filter |
| **23 rows with no ethnicity label** | the lookup |
| **every value matches** | the four cleaning rules |

**If you get 0 rows with no ethnicity label, you wrote an inner join.** ADF's
`lookup` is a left join — it keeps the row and leaves the label empty. Twenty-
three donors just disappeared from a registry and nothing told you. That is the
single most common way this conversion goes wrong in the wild.

## Step 4 — the defect you just inherited

**▸ Together, out loud.**

Your view is green. Now run this against the source data — you can ask Claude,
or write it yourself:

> How many rows in donor_import.csv have a status that is not one of the four
> valid statuses?

**Twenty rows say `Activ`.** The flow filters `status == 'Active'`, so those
twenty donors have been dropped from every weekly load, silently, for as long as
this pipeline has run.

Now the question worth the whole part:

> **Should your conversion fix it?**

The answer is **no, and yes.** A conversion that changes behaviour is not a
conversion — you would have no way to tell a migration bug from a data fix, and
your parity check could never go green. So: **convert faithfully, then log the
defect as its own piece of work.**

Say it in one line, because you will need this line in a real migration:

> *"The view reproduces the pipeline exactly, including a filter that drops 20
> mis-typed status values. That is a pre-existing defect, ticketed separately."*

## Step 5 — re-target, and write it down

**▸ Your turn.** Your view runs on DuckDB. Your stack is Azure SQL.

> Re-target this view to T-SQL for Azure SQL. List every function you had to
> change and why, and flag anything where the T-SQL version is not exactly
> equivalent.

Three things change, and **two of them have no straightforward T-SQL equivalent
at all.** That is not a footnote — it is the reason a bulk conversion needs a
function-mapping table before it needs a schedule.

Finally:

> Write `docs/pipelines/donor-import.md`: what the pipeline does, the converted
> view, the three things that did not convert and what would replace them, and
> the `Activ` defect with its row count.

## What you should have

- `view.sql`, green on `parity.py`
- The three buckets, written down, with three items in bucket (c)
- A T-SQL version and the function-mapping notes
- A `docs/` page that a colleague could act on without opening the JSON
- One sentence about the `Activ` defect that does not blame anyone

## The honest close

**▸ Together.** [`game.md`](game.md) — six cards, converts or does not.

Then the question I want you to leave with: **of your real Mapping Data Flows,
what fraction is bucket (a)?** If you do not know, that is the first week of the
migration, and it is a week of reading, not of writing SQL.
