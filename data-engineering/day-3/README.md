# Day 3 — The remote pipeline

Day 1: *the model can be confidently wrong, so you verify.*
Day 2: *the cure for wrongness is context you engineer, and it compounds in Git.*
**Day 3: the same two habits, pointed at the things you cannot open in a text
editor — a Databricks workspace, a notebook nobody documented, and a Mapping
Data Flow.**

Nothing conceptually new happens today. What changes is the **access path**. You
have already done this job over a CSV and over a database; Databricks and ADF
are two more ways in, and one more place your knowledge layer has to reach.

```
CSV (Day 1)  →  MSSQL over MCP (Day 2)  →  Databricks + ADF (today)
              same understand → change → verify loop, every time
```

## The day

| # | Folder | Min | What you do |
|---|---|---|---|
| 0 | `00-opening/` | 5 | Where Days 1–2 got to, and the shape of today |
| 1 | `01-take-home-debrief/` | 15 | What AI got wrong on your own work, and what caught it |
| 2 | `02-connect-databricks/` | 20 | Claude Code against a real workspace: catalog, SQL, and the boundary |
| 3 | `03-notebook-patterns/` | 35 | Cluster the repeated blocks in an inherited notebook into a module you would adopt |
| — | *break* | 15 | |
| 4 | `04-adf-to-sql/` | 45 | Convert a Mapping Data Flow to SQL, check parity, and find the wall |
| 5 | `05-genie/` | 25 | Curate a Genie space, then the same question to Genie and to Claude Code |
| 6 | `06-close/` | 10 | Take-home 3, and what Day 4 adds |

Each part is one folder, always the same files:

| | |
|---|---|
| **`README.md`** | **The part.** Why it matters, then every step. We read it together |
| **`answers.md`** | The answer key, for the parts that have one. It is right there in the folder; nothing is hidden from you — **read it after the part, not before** |
| **`game.md`** | A few cards, called out loud. Parts 4 and 5 have one |

`README.md` says who is driving each step:

> **▸ We run it first, then you** — watch, then repeat the same thing
> **▸ Your turn** — you drive, and I am on the floor
> **▸ Together** — whole room, out loud

One facilitator today. When you are stuck, say so out loud rather than waiting —
there is nobody circulating behind me.

## What you need in front of you

- Claude Code working, as on Days 1–2
- This repo, pulled: `git pull`
- `day-1/` untouched — today reuses its data and its environment, no `uv sync`
- **Databricks is optional for you.** Parts 2 and 5 run on my workspace. Parts
  3, 4 and 6 — the hands-on ones — need nothing but the folder on your laptop

## What you will have written by the end

| File | From |
|---|---|
| `day-3/03-notebook-patterns/profiling.py` | part 3 |
| `day-3/04-adf-to-sql/view.sql`, passing `parity.py` | part 4 |
| `docs/` entries for the notebook and the pipeline | parts 3 and 4 |
| A behaviour-equivalence argument you can show a reviewer | part 3 |

## The deliberate defects, again

The Day-3 inputs carry planted problems, same rule as Days 1–2: **do not "fix"
the seed data.** Finding them, and noticing which ones your conversion silently
inherits, is the exercise.
