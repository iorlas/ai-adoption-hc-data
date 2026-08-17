# Answers — 2 · Data quality

**FACILITATOR ONLY. Never on screen.** Everything you present is in
`README.md` — read that with the room. This page is what you cannot show them.

Clock and ownership: `session-3/facilitator/run-sheet.md`.

## The demo has a deliberate mistake in it. Do not skip it.

Ask for a *summary* of the status column first. You will be told there are four
statuses. **Accept it out loud, the way anyone would.** Then ask for the full
value counts.

There are five. The fifth is `Activ`, 18 rows.

Landing that failure yourself, in front of them, is the whole demo. If you skip
straight to the right query, the segment teaches nothing.

## Before the game, ask two people for their status counts

If two people have different numbers, **stop everything** and find out why —
that is the entire argument for the shared dataset and it outranks the game.

## Gate

1. `docs/data-quality-rules.md` open, both sections filled
2. "Name one rule you rejected, and why keeping it would have been harmful."
3. "How many supporters have `status = 'Active'`? And how many should?"

Correct: **2,447** and **2,465**.

Question 2 is the graded one. Anyone who kept every rule Claude proposed has
missed the segment. Ask: *"what happens in six weeks when this alert fires three
hundred times a day?"*

## Status column

| status | rows |
|---|---|
| Active | 2,447 |
| Lapsed | 897 |
| Inactive | 589 |
| **Activ** | **18** |
| Deceased | 71 |

## Row counts

supporters **4,022** · campaigns **192** · donations **12,376** ·
campaign_activity **22,591** · fulfilment_tasks **6,000**

## Meaningful defects

| Defect | Rows |
|---|---|
| `status = 'Activ'` | 18 |
| Same person twice — same name + DOB, different `supporter_id` | 22 |
| `sign_up_date` in the future | 13 |
| `last_activity_date` before `sign_up_date` | 34 |
| `donation_date` before the supporter signed up | 60 |
| Donations referencing a supporter that does not exist | 30 |
| Donations referencing a campaign that does not exist | 17 |
| Duplicate donation rows | 44 |
| Negative amounts | 12 |
| Zero amounts | 8 |
| `marketing_consent` as `'Y'`/`'N'` text | 15 |
| Blank email | 146 |
| Malformed email, no `@` | 31 |
| Blank region | 40 |
| `clicked = 1` while `opened = 0` | 77 |
| `campaigns.end_date` before `start_date` | 6 |

## Noise they should reject — the graded half

- **Postcode formatting** (300 rows lowercase/unspaced) — realistic messiness
- **`marketing_consent = 0`** — a lawful choice
- **Supporters with no donations** (~29%) — normal
- **`status = 'Deceased'`** — correct data
- **`refunded = 1`** (213 rows) — real refunds. The *disagreement about whether
  to count them* is the lesson, and it arrives in part 4

## What goes wrong

**Claude writes pandas instead of SQL.** Correct it out loud rather than
quietly. Then flag that `CLAUDE.md` already says this and is being overridden —
**and that part 4 is where we fix that properly.** Free setup for the next hour.

**Date-cast errors.** Let them paste the error straight back to Claude — that is
the loop you want them fluent in, not something to rescue them from.

**Someone's numbers do not match.** Stop the room. Either a different dataset or
a query that silently sampled. Both are worth two minutes in front of everybody.

**You are behind.** Step 3 becomes a live group exercise off one screen instead
of individual work. Do not cut the compare.

**On the floor:** weight support toward Lauren's team — the July literacy
friction was concentrated there, not spread evenly.
