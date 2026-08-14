# Supporter Engagement — model notes

**Owner:** Supporter Care · **Built:** 2025 · **Documentation:** this file,
written for the workshop.

## What it is for

The quarterly engagement review. The question behind it is not "how many people
are on the database" but "how many people are actually still with us" — so it
deliberately ignores the CRM status field and looks at behaviour instead.

## Tables

| Table | Source | Notes |
|---|---|---|
| `supporters` | `data/supporters.csv` | Loaded whole |
| `donations` | `data/donations.csv` | **Refunded gifts filtered out in Power Query** |
| `campaign_activity` | `data/campaign_activity.csv` | Opens and clicks |
| `campaigns` | `data/campaigns.csv` | |
| `Date` | generated | |

## The Power Query step that matters

```m
let
    Source = Csv.Document(File.Contents("data\donations.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {
        {"donation_id", Int64.Type}, {"supporter_id", Int64.Type},
        {"donation_date", type date}, {"amount_gbp", type number},
        {"campaign_code", type text}, {"payment_method", type text},
        {"gift_aid", Int64.Type}, {"refunded", Int64.Type}
    }),
    // refunds are not income
    NoRefunds = Table.SelectRows(Typed, each [refunded] = 0)
in
    NoRefunds
```

This one line is the reason this report's income figure is £16,995 lower than
Fundraising Summary's, and nobody outside this team knows it is there.

## What the person who built it was trying to show

"Who is still engaged." Someone with `status = 'Active'` who last gave in 2019
is not engaged in any useful sense, so this report defines active by behaviour:
gave money in the last twelve months.
