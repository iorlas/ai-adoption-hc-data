# Answers — 4 · One definition, shared across the team

**FACILITATOR ONLY. Never on screen.** Everything you present is in
`README.md` — read that with the room. This page is what you cannot show them.

Clock and ownership: `session-3/facilitator/run-sheet.md`.

The centrepiece of the day, and **protected**.

## Running it

**Step 0 matters far more than it looks.** Make everyone actually save the
"before" answer before they tell Claude anything. If they skip it, step 5d's
payoff evaporates and the whole segment loses its ending. Walk the room and
check.

**The demo (6 min).** Run step 0, then step 1, and get both numbers on screen:
2,447 and 1,832. Then find the second disagreement — the income gap — and **open
`reports/supporter-engagement/model.md` and point at the single line of Power
Query**: `Table.SelectRows(Typed, each [refunded] = 0)`.

Sit on that for a second. A headline figure is being moved by £16,995 by a step
buried three clicks into the Advanced Editor that nobody outside that team knows
exists. It is the most persuasive artifact in the repository.

**The sorting drill (5 min).** Run `game.md` out loud: read the item, let the
room answer, then reveal. That format was the strongest twenty minutes of July —
asked what a prompt was missing, Declan, Lucie and Sarah each supplied a piece
unprompted. It works far better with this group than a walkthrough.

**Item 7 is the one to slow down on.** It is the refund step they found ten
minutes ago, wearing a different hat, and it splits into three homes. Do not
resolve it quickly.

The drill also exists to stop them putting everything into `CLAUDE.md`. Without
it, that is exactly what the room does, and their file is useless within a
quarter.

**The decision (8 min).** All four numbers on the whiteboard. **Do not let the
loudest voice settle it.** Expect to land on two named measures.

**The write-up (9 min).** If you are short, drop the ADR (5c). Never the payoff
(5d).

## Gate — three things on screen

1. `docs/measure-definitions.md`, filled in
2. `CLAUDE.md` with a Definitions section that is **a pointer, not the content**
3. The before answer and the after answer, side by side

Number 2 is the graded one. If someone has pasted the full definitions into
`CLAUDE.md`, the drill did not land — have them move it and watch how much
shorter the file gets, and that nothing was lost.

## Answer key

### The four answers to "how many active supporters?"

| Definition | Number |
|---|---|
| `status = 'Active'` — **Fundraising Summary** | **2,447** |
| `status IN ('Active','Activ')` — same, once you see the typo | **2,465** |
| Gave, refunds excluded, last 12 months — **Supporter Engagement** | **1,832** |
| Any activity in the last 12 months | **1,405** |

Gap between the two live reports: **615 people.** The typo alone: **18.**

### The second disagreement — income

| Definition | Amount |
|---|---|
| Every row — Fundraising Summary | **£947,087.50** |
| Refunds excluded — Supporter Engagement | **£930,092.50** |
| Refunds and negative/zero excluded | **£930,910.00** |

**£16,995** between the two live reports, from one undocumented Power Query
step.

### Reproducing them

```sql
-- Fundraising Summary
SELECT count(*) FROM 'data/supporters.csv' WHERE status = 'Active';

-- Supporter Engagement
-- The join matters: without it you get 1,843, because 11 donations in the
-- window carry a supporter_id that is not in supporters.csv.
SELECT count(DISTINCT d.supporter_id)
FROM 'data/donations.csv' d
JOIN 'data/supporters.csv' s USING (supporter_id)
WHERE d.refunded = 0 AND CAST(d.donation_date AS DATE) >= DATE '2026-08-17' - INTERVAL 12 MONTH;

-- income, both ways
SELECT sum(amount_gbp) FROM 'data/donations.csv';
SELECT sum(amount_gbp) FROM 'data/donations.csv' WHERE refunded = 0;
```

### Where the room should land

- **Supporters on file (Active)** — `status IN ('Active','Activ')`. Answers "how
  big is the database". Says nothing about engagement.
- **Actively giving supporters** — a non-refunded gift in the last 12 months.
  Answers "who is still with us".
- Plus a third they will find and should **name rather than adopt**: Engaged
  supporters, 1,405.

### What else belongs in `CLAUDE.md`

- `Activ` is a defect; treat as Active until the source is fixed
- Duplicate people inflate every count using `supporter_id`
- Orphan `supporter_id`s mean `DISTINCTCOUNT(donations[supporter_id])` and a
  count of supporters are never the same number

## What goes wrong

**Numbers reproduce but do not match.** Two causes, in this order. **The join**
— without joining `supporters`, the distinct count is 1,843, not 1,832. **The
reference date** — "last 12 months" means the twelve months back from today,
2026-08-17. Do not say "the latest date in the data": that is 2026-11-30, a
deliberate bad row, and it gives 1,481.

**Claude rewrites the whole of `CLAUDE.md`.** It was told not to. **Let this
happen and point at it** rather than preventing it — it is a live demonstration
of why you read a change before accepting it.

**It puts full definitions in `CLAUDE.md`.** Very common. Have them move it. The
"look how much shorter that got" moment does more than the drill did.

**The after-answer is no better.** Either the conversation was not restarted, or
the definition went somewhere Claude does not read. Check it edited the
`CLAUDE.md` at the project root.
