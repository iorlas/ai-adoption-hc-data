# Take-home 1 — Direct AI at the data, and verify it

_After Day 1. Budget ~30 minutes._

## Task

Pick **one** column or relationship in `../data/donor.csv` that you did not fully
explore in the session (for example: `ethnicity`, `postcode` formatting, the
`consent_research` flag, or how `status` relates to `registered_date`).

Working **through Claude Code**, produce a short, trustworthy description of it:
what it holds, what "good" looks like, and anything surprising or dirty.

## Deliverable

- A few lines of description you would be happy to hand a new joiner.
- A completed verification log (`verification-log-template.md`).

## The verification that matters

Do not stop at the model's description. **Check it against the data in pandas.**
Are the categories really what it claimed? Are there blanks or odd values it
missed? Find at least one place where the first answer was wrong, vague, or
overconfident, and note how you caught it. If everything looked perfect on the
first try, you probably did not check hard enough.

## Hint

A good prompt is specific about the check: "What values does `ethnicity` take, and
how often? Verify by counting in pandas, do not guess from the column name."
