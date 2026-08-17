# Data-quality rules

*Fallback copy of what Session 3 produced. Copy this over
`docs/data-quality-rules.md` if you were not there.*

> A rule belongs here only if breaking it means the data is **wrong for how we
> use it** — not merely different from how someone would have typed it.

**Last reviewed:** 2026-08-17 · **Owner:** Analytics

## Rules we keep

| # | Table | Rule | SQL predicate | Failing now | Why it matters |
|---|---|---|---|---|---|
| 1 | supporters | Status is a known value | `status NOT IN ('Active','Lapsed','Inactive','Deceased')` | 18 | The `Activ` typo removes 18 people from every report filtering on Active |
| 2 | supporters | No person appears twice | same `first_name` + `last_name` + `date_of_birth`, different `supporter_id` | 22 | Inflates every count of people and breaks any per-supporter average |
| 3 | supporters | Sign-up date is not in the future | `sign_up_date > current_date` | 13 | Silently breaks any cohort or tenure calculation |
| 4 | supporters | Last activity is not before sign-up | `last_activity_date < sign_up_date` | 34 | Produces negative tenure; the row is wrong, not merely odd |
| 5 | donations | Donation references a supporter who exists | `supporter_id NOT IN (SELECT supporter_id FROM supporters)` | 30 | These gifts cannot be attributed; supporter-level totals are understated |
| 6 | donations | No duplicated gift | identical `supporter_id` + `donation_date` + `amount_gbp`, different `donation_id` | 44 | Overstates income and per-supporter giving |
| 7 | donations | Amount is positive | `amount_gbp <= 0` | 20 | Zero and negative rows are corrections entered as gifts; they distort averages |
| 8 | donations | Gift is not dated before the supporter existed | `donation_date < sign_up_date` | 60 | Either the gift or the sign-up date is wrong; both matter for attribution |

## Rules we rejected, and why

| Proposed rule | Why it is noise |
|---|---|
| Postcodes must be consistently formatted | 300 rows are lowercase and unspaced. Realistic messiness — normalise on read. An alert here fires constantly and teaches everyone to ignore alerts |
| Every supporter must have an email | 146 do not. Plenty of people legitimately give no email address |
| `marketing_consent` must be 1 | Consent set to 0 is a lawful choice, not a data defect |
| Every supporter must have at least one donation | About 29% have none. Entirely normal |
| Names must be title-cased | Cosmetic |

## Things that look like defects and are not

- **`refunded = 1`** — 213 real refunds. Valid data. The disagreement about
  whether to *count* them is a definitions question, not a quality one, and it
  is settled in `docs/decisions/0001-*`.
- **`status = 'Deceased'`** — real, correct, and about 2%.
- **Supporters with no donations** — see above. Not everyone gives.

## What we are not checking yet, and should

- **Nothing checks that `marketing_consent` is a number.** 15 rows hold `'Y'`
  or `'N'` as text. Anything casting that column silently drops those rows.
- Nothing checks `campaign_activity` for `clicked = 1` where `opened = 0` — 77
  impossible rows, which is why click-through rate can exceed 100%.
- Nothing reconciles donation totals against finance.
