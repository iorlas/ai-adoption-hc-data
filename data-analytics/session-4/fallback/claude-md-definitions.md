# Fallback — the Definitions block from Session 3

Paste everything below the line into your `CLAUDE.md`, replacing the `_TODO_`
under `## Definitions`.

This is close to what the room agreed on Monday. Your colleagues' wording will
differ slightly; the numbers will not.

---

## Definitions

Full definitions, with SQL and DAX, are in `docs/measure-definitions.md`. Read
that file before answering anything about a measure. The two below come up
constantly, so they are here.

**Supporters on file (Active)** — supporters whose record is marked active:
`status IN ('Active','Activ')`. **2,465.** Answers "how big is the database".
Says nothing about whether anyone is still engaged.

**Actively giving supporters** — supporters who made a gift, not later refunded,
in the last 12 months. **1,832.** Answers "who is still with us". Excludes
people who engage without giving.

These are two different measures. **Never call either of them just "active
supporters"** — that name is retired, and using it is what produced a
633-person disagreement between two live reports.

### Hard rules

- `status = 'Activ'` is a **typo**, not a status. It is 18 real supporters.
  Treat it as `Active` everywhere until the source system is fixed.
- **Refunded gifts are not income.** Exclude `refunded = 1` from any income
  measure. The Fundraising Summary report does not do this, which is why its
  income figure is about £17,000 higher than Supporter Engagement's.
- The supporters file contains **22 people twice** (same name and date of birth,
  different `supporter_id`). Any count of people, as opposed to records, has to
  deal with this.
- 30 donations reference a `supporter_id` that does not exist. A distinct count
  of supporters in the donations table and a count of supporters are therefore
  never the same number.
- If a measure name is ambiguous, ask which definition is meant rather than
  choosing one.
