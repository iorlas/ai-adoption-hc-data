# Prep — Day 3

**FACILITATOR ONLY.** One facilitator this day. Everything below is yours.

## The shape of it

**Nothing on Day 3 needs Databricks.** The workspace, the CLI and Genie moved to
Day 4 so that one setup serves one day. What is left is the two things the
client asked for by name in June, plus the ADF arc that leads into the second of
them.

| Part | Minutes | Needs building first |
|---|---|---|
| `00-opening` | 5 | No |
| `01-take-home-debrief` | 10 | No — but see the "nobody did it" pivot in its `answers.md` |
| `02-notebook-patterns` | 40 | No. **Dry-run it** |
| `03-adf-explain` | 20 | No. Reused from the analytics stream, same five JSON files |
| `04-adf-weak-spots` | 20 | No. Also reused — and it is the designated cut |
| `05-adf-to-sql` | 55 | No — the data is generated and committed. **Dry-run it** |
| `06-close` | 15 | No |

## The clock

```
0:00   5   Opening                    watch
0:05  10   Take-home debrief          together
0:15  40   Notebook patterns          HANDS-ON    ← protected
0:55  20   ADF: explain it            hands-on    ┐ one conversation,
1:15  20   ADF: weak spots            hands-on    ┘ no break between them ← THE CUT
1:35  15   Break
1:50  55   ADF to SQL                 HANDS-ON    ← protected, the headline ask
2:45  15   Close
3:00       end
```

**Full three hours, and one designated cut.** Parts 3, 4 and 5 are an arc — read
a pipeline, find where it lies to you, then convert a different one — and part 4
is the segment that can shrink to twelve minutes or move to the take-home
without breaking the arc. Its `answers.md` says exactly how.

Parts 3 and 4 run back to back in **one conversation**, which is what makes part
4 cheap — do not put the break between them. Say the arc out loud at the start of
part 3, or it reads as three unrelated ADF segments.

**Two of the three ADF parts are reused verbatim from the analytics stream**,
over the same five JSON files. One thing genuinely differs: part 4's
rules-handover cannot run rule-by-rule here, because their Day-2 rules are
donor-shaped and this pipeline is not. It runs structurally instead — read that
section of `04-adf-weak-spots/answers.md` before the day.

## What to prepare

**1 · Your machine**

- `git pull`, then from `day-3/05-adf-to-sql/`: `uv run parity.py` should say
  *"has no query in it yet"*. If it goes green you left the reference SQL in
  `view.sql`.
- Day-1 environment intact (`day-1/.venv`). Today needs no `uv sync`.
- `day-3/05-adf-to-sql/data/` committed. Regenerate only if you must:
  `uv run day-3/facilitator/generate_day3_data.py` rewrites both CSVs
  deterministically and moves no number.

**2 · Dry-run both hands-on parts as a participant**

From a clean clone, doing exactly what the README says and nothing a facilitator
would know. That is what catches instructions pointing at files that do not
exist, and promises about what the room will see.

**3 · The reference SQL, in a scratch buffer, not on screen**

It is in `05-adf-to-sql/answers.md`. See the second rule below.

## The room, one facilitator

There is nobody circulating. Plan for it:

- **Say at the top that people must call out when stuck.** With two facilitators
  the floor gets swept; with one it does not.
- **Pair the blocked with the unblocked before part 2**, not at the point of
  failure. Three of Shankar's team had no Claude Code access in July — if that
  is still true, the pairing is the whole of their day.
- **Your recoverable time is part 3 and the ten minutes of slack.** Parts 2 and
  4 are protected. This is the trade for moving Databricks to Day 4: no
  watch-only segment to shorten mid-flight.

## The two things not to get wrong

1. **Do not resolve the `Activ` typo before part 5.** It surfaces in part 2's
   distinct-count cells. Credit whoever spots it and say it comes back after the
   break. It is the hinge of the biggest part of the day.

2. **Do not put the reference SQL up before minute 35 of part 5.** The parity
   check failing on an inner join is the most useful thing that happens all day,
   and it only happens if people write the join themselves.
