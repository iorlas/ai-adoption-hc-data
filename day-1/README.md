# Claude Code Workshop — Day 1

Welcome. Day 1 is about two things: **getting Claude Code working on real data-engineering artifacts**,
and building the one habit that carries the whole week: **AI can be confidently wrong, so you verify.**

Everything today needs only **Python + pandas** (and a SQLite file). No cloud, no Databricks, no Azure.

## Start here

```bash
uv sync           # one-time: installs pandas + jupyterlab
uv run verify.py  # green = you are ready
```
Green? Open **`01-hands-on-basics/`** and follow its README. Then work through the sections in order.

## The day, section by section

| # | Section | You will |
|---|---------|----------|
| **01** | Hands-on basics | get the tool working: open a notebook, read a stored procedure, run a query |
| **02** | LLM essentials | tokens, context window, statelessness, and why context management is the skill |
| **03** | The boundary | where AI wins and loses — hunt the data's defects and **verify every claim** |
| **05** | Directing Claude Code | `CLAUDE.md`, permissions, slash commands, MCP vs Skills (+ a live SQL-MCP demo) |
| **06** | Prompting discipline | a good and a bad prompt on the same task, side by side |
| **07** | Governance + take-home | anonymise-before-AI, verification as discipline, Take-home 1 |

Each folder is self-contained: a `README.md` plus whatever that section needs. The shared dataset
lives once in `data/` (`donor.csv` and the same rows in `donor.db`).

## The data

A synthetic stem-cell donor registry (~5,000 donors). **Every row is synthetic and fictional** — but
treat the PII-shaped columns as if they were real (see `CLAUDE.md`).

## No `uv`?

`pip install pandas jupyterlab`, then `python verify.py` and `jupyter lab`.
