# Prep — Day 3

**FACILITATOR ONLY.** One facilitator this day. Everything below is yours.

## What has to exist before the room opens

| Part | Minutes | Needs building first |
|---|---|---|
| `00-opening` | 5 | No |
| `01-take-home-debrief` | 15 | No — but see the "nobody did it" pivot in its `answers.md` |
| `02-connect-databricks` | 20 | **Yes — workspace, warehouse, service principal, seeded table** |
| `03-notebook-patterns` | 35 | No. Dry-run it |
| `04-adf-to-sql` | 45 | No — the data is generated and committed. Dry-run it |
| `05-genie` | 25 | **Yes — two Genie spaces, and a recording of both** |
| `06-close` | 10 | No |

**Two things to build. Both are Databricks. Both have a recorded fallback, and
you should make the recording even if you are confident.**

## 1 · The workspace (parts 2 and 5)

- A workspace in **West or North Europe** — this is the region constraint the
  Day-4 AI Functions segment inherits, so get it right now rather than twice.
- A **serverless SQL warehouse**. Note the warehouse id; you need it in the
  statement-execution call.
- A catalog `training` and a schema in it. Load `day-1/data/donor.csv` as
  `donor` — **all 5,005 rows, defects intact.** The status counts on the day
  must be 2,885 / 728 / 702 / 670 / **20 `Activ`**, because part 4 turns on
  those twenty.
- A **service principal** with read on that schema and use on the warehouse.
  Not a personal token — the part argues for service principals out loud, and
  demoing with a PAT undercuts it.
- `databricks auth login --profile an-workshop` working on the laptop you will
  present from, verified the morning of.

**Rehearse the three prompts in part 2's `answers.md` end to end** and keep the
working statement-execution JSON in a scratch file. That file is the difference
between a two-minute recovery and losing part 3.

## 2 · The two Genie spaces (part 5)

Build **two**, do not edit one live:

- **`AN Donor (raw)`** — the donor table, no table comment, no column comments,
  no curated definitions.
- **`AN Donor`** — same table, plus: a table comment with the grain, a comment
  on `status` naming the four valid values and the `Activ` defect, and one
  curated definition for "active donor" with its SQL.

Ask *"how many active donors do we have?"* in each. **Screen-record both.** If
the second answer is not visibly better, read the note in part 5's `answers.md`
before the day — there is a line that saves the segment, and it is better
delivered as a planned point than as a recovery.

Also rehearse the side-by-side question in both tools, and have Claude Code
already connected in the right window.

## 3 · Your machine

- Windows or Mac, whichever you present from — but present from the one you
  rehearsed on.
- `git pull` in the repo, then from `day-3/04-adf-to-sql/`: `uv run parity.py`
  should say *"has no query in it yet"*. That is the correct starting state; if
  it goes green, you have left the reference SQL in `view.sql`.
- Day-1 environment intact (`day-1/.venv`). Today needs no `uv sync`.
- **`day-3/04-adf-to-sql/data/` must be committed.** Regenerate with
  `uv run day-3/facilitator/generate_day3_data.py` only if you have to;
  it rewrites both CSVs deterministically and does not move any number.

## 4 · Dry-run parts 3 and 4 as a participant

The two hands-on parts, from a clean clone, doing exactly what the README says
and nothing a facilitator would know. That is what catches the defects worth
catching — instructions pointing at files that do not exist, and promises about
what the room will see.

## 5 · The room, one facilitator

There is nobody circulating. Consequences to plan for:

- **Say at the top that people must call out when stuck** — with two
  facilitators the floor gets swept, and with one it does not.
- **Pair the blocked with the unblocked** early rather than at the point of
  failure. Three of Shankar's team had no access in July; if that is still true,
  seat them next to someone who does *before* part 3.
- **Parts 2 and 5 are your recovery slack.** Both are watch-only and both can
  lose five minutes without damage. Parts 3 and 4 cannot.

## The clock

```
0:00  5   Opening                         watch
0:05 15   Take-home debrief               together
0:20 20   Claude Code on the workspace    watch          ← recoverable
0:40 35   Notebook patterns               HANDS-ON       ← protected
1:15 15   Break
1:30 45   ADF to SQL                      HANDS-ON       ← protected, the headline ask
2:15 25   Genie                           watch          ← recoverable
2:40 10   Close                           together
2:50      end, 10 minutes of slack
```

## The two things not to get wrong

1. **Do not resolve the `Activ` typo before part 4.** It shows up on screen in
   part 2 and again in part 3. Both times: credit whoever spots it, and say it
   comes back after the break. It is the hinge of the biggest part of the day.

2. **Do not put the reference SQL up before minute 30 of part 4.** The parity
   check failing on an inner join is the most useful thing that happens all day,
   and it only happens if people write the join themselves.
