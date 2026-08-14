# The shared dataset

Five CSVs. Everyone in the room uses these, so that when you follow a step you
can check you got the same answer we did.

**All of it is synthetic and fictional.** No real supporter, donor or patient
data is used. Names, emails, postcodes and dates are generated.

| File | Rows | What it is |
|---|---|---|
| `supporters.csv` | 4,022 | People on the supporter database |
| `donations.csv` | 12,376 | Individual gifts |
| `campaigns.csv` | 192 | Appeals and mailings |
| `campaign_activity.csv` | 22,591 | Email sends, opens, clicks |
| `fulfilment_tasks.csv` | 6,000 | Supporter-care and operations work items |

The first three are the fundraising shape. `fulfilment_tasks.csv` is the
operational shape — throughput, backlogs, who is doing what — for the work that
looks less like income and more like process.

---

## supporters.csv

| Column | Type | Notes |
|---|---|---|
| `supporter_id` | integer | Unique per **row**. Not necessarily unique per person — see below |
| `first_name`, `last_name` | text | |
| `date_of_birth` | date | |
| `email` | text | Sometimes blank |
| `postcode` | text | Formatting is inconsistent |
| `region` | text | Sometimes blank |
| `sign_up_date` | date | When they joined |
| `source_channel` | text | Web, Direct Mail, Event, Telephone, Partner, Social |
| `marketing_consent` | integer | 1 or 0. Mostly |
| `status` | text | Active, Lapsed, Inactive, Deceased. Mostly |
| `last_activity_date` | date | Any contact, not just a gift |

## donations.csv

| Column | Type | Notes |
|---|---|---|
| `donation_id` | integer | Unique per row |
| `supporter_id` | integer | Joins to `supporters.csv`. Usually |
| `donation_date` | date | |
| `amount_gbp` | decimal | |
| `campaign_code` | text | Joins to `campaigns.csv`. Usually |
| `payment_method` | text | |
| `gift_aid` | integer | 1 or 0 |
| `refunded` | integer | 1 if the gift was later refunded |

## campaigns.csv

| Column | Type | Notes |
|---|---|---|
| `campaign_code` | text | `CMPnnnn` |
| `campaign_name` | text | Free text, entered by hand over several years |
| `category_raw` | text | Free text. **This is the messy one** |
| `channel` | text | Email, Direct Mail, SMS, Social, Phone |
| `start_date`, `end_date` | date | |
| `owner_team` | text | |

`category_raw` is the shape of the real problem Lauren described: the same eight
or so campaign types, typed differently by different people over several years,
with no agreed list. There is no lookup table. That is the point.

## campaign_activity.csv

| Column | Type | Notes |
|---|---|---|
| `activity_id` | integer | |
| `campaign_code` | text | |
| `supporter_id` | integer | |
| `sent_date` | date | |
| `opened`, `clicked`, `unsubscribed` | integer | 1 or 0 |

## fulfilment_tasks.csv

| Column | Type | Notes |
|---|---|---|
| `task_id` | integer | |
| `task_type` | text | Welcome pack, swab kit dispatch, complaint, … |
| `assigned_team` | text | |
| `assigned_to` | text | Sometimes blank |
| `created_date`, `due_date`, `completed_date` | date | `completed_date` blank if not done |
| `status` | text | |
| `priority` | text | Low, Normal, High, Urgent |

---

## Please do not fix the data

It contains deliberate defects. Some of them matter and some of them do not, and
telling those apart is Session 3's first exercise. If you clean the CSVs, the
exercise stops working for everyone else.

## Querying it without a database

There is no database to install. DuckDB reads the CSVs in place:

```bash
uv run python -c "import duckdb; print(duckdb.sql(\"SELECT status, count(*) FROM 'data/supporters.csv' GROUP BY status ORDER BY 2 DESC\"))"
```

Claude Code will do this for you — you write the question, it writes the SQL.
You still read the SQL before you believe the answer.
