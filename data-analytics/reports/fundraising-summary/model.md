# Fundraising Summary — model notes

**Owner:** Fundraising · **Built:** 2024 · **Last touched:** last month, by
someone who no longer works here · **Documentation:** this file, written for the
workshop. In real life there was none.

## What it is for

The monthly income pack. Goes to the Director of Fundraising. The two headline
tiles are **Active supporters** and **Total income**, with income broken down by
campaign and by channel underneath.

## Tables

| Table | Source | Notes |
|---|---|---|
| `supporters` | `data/supporters.csv` | Loaded whole, no filtering |
| `donations` | `data/donations.csv` | Loaded whole, **including refunded gifts** |
| `campaigns` | `data/campaigns.csv` | Used for the campaign breakdown |
| `Date` | generated | `CALENDARAUTO()` |

## Relationships

- `supporters[supporter_id]` 1 → * `donations[supporter_id]`
- `campaigns[campaign_code]` 1 → * `donations[campaign_code]`
- `Date[Date]` 1 → * `donations[donation_date]`

## What the person who built it was trying to show

"How many supporters do we have, and what did they give us." Active supporters
is read straight off the `status` column, because that is what the CRM calls it
and the CRM is the system of record.

## Known quirks, as far as anyone remembers

- The campaign breakdown has an "unknown campaign" bucket that nobody has ever
  explained.
- The supporter count has drifted away from the Supporter Care dashboard's
  number, and there has been an unresolved email thread about it since March.
