# Answers — 4 · Asking better questions of your data

**FACILITATOR ONLY. Never on screen.** Everything you present is in
`README.md` — read that with the room. This page is what you cannot show them.

Clock and ownership: `session-4/facilitator/run-sheet.md`.

## Let people choose A or B

Expect Lauren's team on A (fundraising) and Lucie's on B (operational), but **do
not assign it** — say "pick the one closer to your work." One done properly
beats two done badly.

## The moment to hold the room for — Hypothesis A reverses

The naive answer says Event supporters give 2.1× what Direct Mail supporters
give. Controlling for how long each group has been on the database, Direct Mail
gives **71% more per year** and Event comes *last*.

Whoever hits it first, **stop the room and put both tables on screen.** The
first query was not a bad query. It was a good query answering a question nobody
meant to ask.

Do the same with B's survivorship column if anyone gets there.

**Make sure the pre-commitment happens.** Everyone writes down what would change
their mind *before* they see the answer. Skipping it turns the exercise into
running queries, which they can already do.

## Gate — three things

1. Their hypothesis, and the thing they said **in advance** would change their
   mind
2. **One check that changed their answer**
3. The two sentences: what we found, and what it does not tell us

Item 3 is the deliverable.

## Answer key

### Hypothesis A — the naive answer says yes, emphatically

Average lifetime giving:

| Channel | Avg lifetime | Avg tenure |
|---|---|---|
| Partner | £299 | 5.9 yrs |
| Event | £289 | 7.0 yrs |
| Telephone | £282 | 5.0 yrs |
| Web | £230 | 3.2 yrs |
| Social | £139 | 2.4 yrs |
| Direct Mail | £136 | 1.7 yrs |

Anyone stopping here writes a recommendation to move budget into events.

### Controlling for tenure reverses it completely

| Channel | Per year |
|---|---|
| **Direct Mail** | **£70** |
| Web | £65 |
| Telephone | £55 |
| Social | £52 |
| Partner | £50 |
| **Event** | **£41** |

The entire original finding was tenure. Event was the acquisition channel years
ago; Direct Mail is where the recent supporters came from.

The duplicate-supporter check is a real but small effect (22 people) and does
**not** change the conclusion. Worth noting out loud: not every check overturns
something, and knowing a finding is robust is also a result.

### Hypothesis B — part one is true

| Task type | Days |
|---|---|
| **Complaint** | **30.7** |
| Data request | 24.0 |
| Consent follow-up | 18.3 |
| Gift Aid declaration | 16.0 |
| Address change | 12.2 |
| Welcome pack | 11.1 |
| Swab kit dispatch | 9.1 |
| Thank-you letter | 7.9 |

### Part two is where it gets interesting

| Quarter | Avg days (completed) | % still open |
|---|---|---|
| 2025 Q1 | 15.5 | 8.7% |
| 2025 Q2 | 15.7 | 7.7% |
| 2025 Q3 | 15.5 | 6.1% |
| 2025 Q4 | 15.1 | 8.4% |
| 2026 Q1 | 15.7 | 7.0% |
| 2026 Q2 | **17.7** | 9.5% |
| 2026 Q3 | 15.4 | **53.3%** |

Read the middle column alone and the story is "a blip in Q2, back to normal in
Q3." **That is wrong.** More than half of Q3 has not finished, and the fast ones
finish first — the slow half has not entered the average yet.

The truth in the data: resolution times really are **55% worse** for recent
work. Survivorship bias, and it is the most common way an operational trend
finding is wrong. **Make sure the room sees this one.**

### The two smaller traps in B
- `status` is `'Complete'` (190) and `'Completed'` (5,149). Filter on one and
  you drop 190 tasks.
- 46 tasks are marked complete with a blank `completed_date`; 11 have a
  completion before their creation. What was done with those, and which
  direction does it bias?

## What goes wrong

**It answers before they finish asking.** Long prompts get partial answers. The
exercise is written as steps for exactly this reason.

**A confident answer with no visible query.** Ask for it, every time. Unchecked
is unusable.

**It hedges instead of giving a number.** Usually means the question was
ambiguous — which is itself the lesson. Have them say what they meant more
precisely.

**Nobody reaches the reversal.** Ask directly at minute 18: *"how long has each
of these groups been on the database?"* The reversal is the segment; do not let
it be missed for the sake of discovery.
