# Claude Code Workshop — Data Engineering

> The analytics teams' material is in [`../data-analytics/`](../data-analytics/)
> — different data, different exercises, nothing shared between them. This
> folder is the one for people who build and maintain pipelines, procedures and
> warehouses.

A hands-on workshop. **Each day is a self-contained folder.** Start with Day 1:

```bash
cd day-1
uv sync            # creates .venv + installs this day's dependencies
uv run verify.py   # green = you are ready
```

Then open **`day-1/README.md`** and work the sections in order.

All data in this repo is **synthetic and fictional**. There is no real or
personal data anywhere. Even so, treat the PII-shaped columns — name, date of
birth, email, phone, postcode, `nhs_number` — as if they were real: never paste
one into an external service, and mask anything that lands in a document. The
habit is the point.

## Days

| Day | Folder | Topic |
|-----|--------|-------|
| 1 | [`day-1/`](day-1/) | Hands-on basics, the boundary, directing Claude Code |
| 2 | [`day-2/`](day-2/) | Engineer the context: tame an inherited stored procedure, and build the knowledge layer that makes the next person's version easier |
| 3 | [`day-3/`](day-3/) | The artifacts nobody documented: an inherited notebook, an inherited pipeline, and a Mapping Data Flow converted to SQL with a parity check |
| 4 | [`day-4/`](day-4/) | The connection: a real Databricks workspace, Genie, and the AI moving inside the pipeline. **Partly built** |
| — | [`later-days/`](later-days/) | The two ADF pipelines and the Databricks notebook Days 3–4 work against |

`later-days/` is not a day of its own — it holds the artifacts Days 3 and 4 read
(two ADF pipelines and a profiling notebook). Day 2's final stage points at them
as a bridge; Day 3 works on them.

## The through-line

Day 1: *the model can be confidently wrong, so you verify.*

Day 2: *the cure for wrongness is context you engineer — and because it lives in
Git, it compounds.*

Day 3: *the same two habits reach the artifacts nobody documented — a notebook
grown by copy-paste, a pipeline published by someone who has left.*

Day 4: *the connection, and then the AI moving inside the pipeline itself — at
which point you are the one deciding what it must never touch.*

## A note on the deliberate defects

The seed data contains planted data-quality problems — duplicates, nulls,
inconsistent formats, out-of-range values — and the stored procedure contains a
real latent bug. Finding and reasoning about them is the exercise. **Do not
"fix" the seed data.**
