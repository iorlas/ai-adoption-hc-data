# Prep — Day 3

**FACILITATOR ONLY.** One facilitator this day. Everything below is yours.

## The shape of it

**Nothing on Day 3 needs Databricks.** The workspace, the CLI and Genie moved to
Day 4 so that one setup serves one day. What is left is the two things the
client asked for by name in June, with room to actually do them.

| Part | Minutes | Needs building first |
|---|---|---|
| `00-opening` | 5 | No |
| `01-take-home-debrief` | 15 | No — but see the "nobody did it" pivot in its `answers.md` |
| `02-notebook-patterns` | 40 | No. **Dry-run it** |
| `03-adf-explain` | 25 | No. Reused from the analytics stream, same five JSON files |
| `04-adf-to-sql` | 55 | No — the data is generated and committed. **Dry-run it** |
| `05-close` | 15 | No |

## The clock

```
0:00   5   Opening                    watch
0:05  15   Take-home debrief          together
0:20  40   Notebook patterns          HANDS-ON    ← protected
1:00  25   ADF: explain it            hands-on    ← compressible
1:25  15   Break
1:40  55   ADF to SQL                 HANDS-ON    ← protected, the headline ask
2:35  15   Close
2:50       end
```

**2:50 in a 3:00 slot, and part 3 is the give.** With one facilitator and no
watch-only segment, `03-adf-explain` is the only place to absorb an overrun: its
`answers.md` says exactly what to cut and in what order. Everything either side
of it is the client's June ask.

**Parts 3 and 4 are deliberately an arc** — read a pipeline, then convert one.
Say that out loud at the start of part 3, or it reads as two unrelated ADF
segments.

## What to prepare

**1 · Your machine**

- `git pull`, then from `day-3/04-adf-to-sql/`: `uv run parity.py` should say
  *"has no query in it yet"*. If it goes green you left the reference SQL in
  `view.sql`.
- Day-1 environment intact (`day-1/.venv`). Today needs no `uv sync`.
- `day-3/04-adf-to-sql/data/` committed. Regenerate only if you must:
  `uv run day-3/facilitator/generate_day3_data.py` rewrites both CSVs
  deterministically and moves no number.

**2 · Dry-run both hands-on parts as a participant**

From a clean clone, doing exactly what the README says and nothing a facilitator
would know. That is what catches instructions pointing at files that do not
exist, and promises about what the room will see.

**3 · The reference SQL, in a scratch buffer, not on screen**

It is in `04-adf-to-sql/answers.md`. See the second rule below.

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

1. **Do not resolve the `Activ` typo before part 4.** It surfaces in part 2's
   distinct-count cells. Credit whoever spots it and say it comes back after the
   break. It is the hinge of the biggest part of the day.

2. **Do not put the reference SQL up before minute 35 of part 4.** The parity
   check failing on an inner join is the most useful thing that happens all day,
   and it only happens if people write the join themselves.
