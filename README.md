# AI adoption workshops — data teams

Workshop material for the Claude Code sessions run with the data teams. Two
streams, two folders. **Find yours and start there — you do not need the other
one.**

| Folder | Who | What it covers |
|---|---|---|
| **[`data-engineering/`](data-engineering/)** | The data engineering teams | Directing AI at everyday DE work: reading and documenting SQL, taming an inherited stored procedure, optimisation, building a knowledge layer that compounds, ADF and Databricks as further access paths |
| **[`data-analytics/`](data-analytics/)** | The analytics teams | Numbers you can defend: data quality, agreeing one definition across reports, building and then verifying a Power BI report, and reading an inherited ADF pipeline |

Each folder is self-contained — its own README, its own data, its own setup.
They do not share files and you never need to `cd` between them.

## Which one am I in?

If you build and maintain pipelines, procedures and warehouses: **data
engineering**. If you build reports, dashboards and analysis: **data
analytics**. If you have been to a session, you already know — it is the one
whose folder your facilitator sent you to.

## The one rule that applies to both

**Every row of data in this repository is synthetic and fictional.** No real
supporter, donor, patient or staff data appears anywhere in it, and none of the
exercises ask you to connect to a real system.

Even so, both streams treat PII-shaped columns — names, dates of birth, emails,
phone numbers, postcodes, NHS numbers — as if they were real, because the habit
is the point. Never paste one into an external service. Mask anything that lands
in a document.

## Setup, in one line

Neither stream needs a database server or a cloud account. Both run on a laptop
with Claude, Python and `uv`, and each folder's README tells you the rest.

```bash
git clone https://github.com/iorlas/ai-adoption-hc-data.git
```

Then open your folder's `README.md`.

## A note on the deliberate mistakes

Both streams' data and code contain **planted defects** — typos, impossible
dates, duplicates, orphan records, and in the analytics stream two reports that
disagree with each other about a headline number.

That is on purpose, all of it. Finding them, working out which ones actually
matter, and being able to say why is most of what the sessions teach. **Please
do not "fix" the sample data** — it stops the exercise working for everyone
else.
