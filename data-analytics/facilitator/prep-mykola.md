# Mykola — everything you need to prep

**FACILITATOR ONLY.** This is your page. Denis's prep is in
`prep-checklist.md`; you do not need the rest of it.

You own **six stages** across the two days, and **four of them need something
built in advance**. Roughly a day of prep in total.

| Day | Stage | Minutes | Needs building first |
|---|---|---|---|
| S3 | `03-genie-vs-claude-code` | 8 | **Yes — Databricks + Genie space** |
| S3 | `04-shared-definitions` | 40 | No |
| S3 | `05-build-and-verify` | 55 | **Yes — the two `.pbix`** |
| S4 | `02-adf-document` | 30 | No, but dry-run it |
| S4 | `03-adf-weak-spots` | 20 | No, but dry-run it |
| S4 | `05-ml-taster` | 30 | **Yes — AutoML run + the leakage column** |

Read each stage's `README.md` **and** its `answers.md` before you touch any of
the below. The README is what the room sees; the answers page is what you cannot
show them.

---

## 1. Databricks + Genie — the only live external system in either day

**About 20 minutes, and none of it exists yet.** Full steps are in
[`../session-3/03-genie-vs-claude-code/answers.md`](../session-3/03-genie-vs-claude-code/answers.md),
under **Pre-flight**. In short:

1. Schema **`an_workshop`** in our own workspace — not the client's, and nobody
   in the room needs access.
2. Upload `data/supporters.csv` and `data/donations.csv` as
   `an_workshop.supporters` and `an_workshop.donations`.
3. **Confirm 4,022 and 12,376** before going further. A different count means the
   upload re-typed or truncated something, and the whole side-by-side falls apart
   on screen.
4. Genie space named **AN Workshop**, those two tables only, no curated
   instructions.
5. Run the comparison question once and **screen-record it**.

**The recording is not optional.** This is the one segment that depends on a
system that can be slow or down at 10am, and it is also the least load-bearing
thing in the day. If Databricks misbehaves, play the recording and move on — no
apology, no troubleshooting in front of ten people.

**If none of this is built by Monday morning, say so and we cut the live half.**
The table on screen carries the segment by itself. That is a decision, not a
failure.

## 2. The two `.pbix`

Steps: [`build-the-two-pbix.md`](build-the-two-pbix.md). The one thing that
silently ruins them:

> Use `Date = CALENDAR(DATE(2016, 1, 1), DATE(2026, 8, 17))`.
> **Never `CALENDARAUTO()`** — it scans `date_of_birth` back to 1946 and the
> future sign-up dates forward to 2027, giving you an eighty-year axis on every
> by-month visual.

**Check before you save:** `MAX('Date'[Date])` reads `2026-08-17`, and the four
numbers are **2,447 / £947,087.50** and **1,832 / £930,092.50**.

## 3. The ML taster — the other thing that does not exist yet

**Nothing in the repo backs this stage.** No notebook, no feature table, no
model, no column list. It is 30 minutes of watch-only Databricks and it is
entirely on you to build. Budget half a day.

1. **A feature table from the five CSVs in `data/`** — one row per supporter,
   joined to their giving. Save the column list somewhere you can put on screen:
   `05-ml-taster/README.md` promises the room they will "see exactly which
   columns went in", and right now nothing shows them.
2. **An AutoML run** predicting something the room cares about — lapse in the
   next twelve months is the obvious one, using `status` and `last_gift_date`.
3. **The leakage column, ready to add live.** This is the memorable beat of the
   stage, not the model. Something that trivially gives the answer away — a
   `months_since_last_gift` when predicting lapse — added on screen so the
   accuracy jumps and everyone sees why that is bad news, not good.
4. **Screen-record the whole thing.** Same rule as Genie: this is a live
   external system in front of ten people.

**Same cut rule.** Not built by Tuesday morning, and the stage becomes the
conversation without the demo. Say that early rather than improvising.

## 4. Your machine, on Windows

Everything the participants need, plus the two extras:

- Claude desktop app **and** a terminal, signed in
- Power BI Desktop
- Python, `uv`, Git, VS Code
- The repo cloned, and `uv run verify.py` green **from a clean clone**
- Databricks reachable in a browser you can screen-share

You are the only person who will run this material on Windows before the room
does. **Anything that surprises you belongs in `../quirks.md`** — that is what
the page is for.

## 5. Dry runs — timed, with the written prompts

Not a read-through. Actually type the prompts from the README and see what comes
back.

- **S3 stage 05** first. It is 55 minutes, it is the protected block, and it is
  the one where a live Power BI stall costs the most.
- **S3 stage 04** — check the two numbers really come out, 2,447 and 1,832.
- **S4 stages 02 and 03** — confirm the five starred issues in the answer key are
  findable with the prompts as written, not with better prompts you invent.

## 6. Handoffs

Three on Monday, four on Tuesday. **Whole stages are yours** — Denis is on the
floor and silent, and the same in reverse. No co-presenting, no cutting in.

Agree the one sentence each of you says when passing over, and say it the same
way both days, so it does not sound improvised.

## The one thing that is not a demo

**S3 stage 04, the 8-minute decision.** You are not showing anything there. You
are chairing an argument between two teams about what "active supporter" means,
and letting it run is the point. The output is two named measures, not one
agreed number.
