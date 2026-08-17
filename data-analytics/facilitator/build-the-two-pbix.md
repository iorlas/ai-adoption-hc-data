# Building the two `.pbix` files

**FACILITATOR ONLY.** For Mykola, on Windows, before Session 3.

The repository ships the two reports as `model.md` + `measures.dax` because
Claude cannot read a `.pbix` and because a binary in the repo would be a lie
about what participants can do with it.

But **you** need the actual reports open in Desktop during Session 3, so the
room can see two dashboards showing different numbers rather than two text
files describing them. That contrast is the segment.

## Report 1 — Fundraising Summary

1. Get Data → Text/CSV → `data/supporters.csv`, `data/donations.csv`,
   `data/campaigns.csv`. **Load all three whole. Do not filter anything.**
2. Relationships: `supporters[supporter_id]` 1→* `donations[supporter_id]`;
   `campaigns[campaign_code]` 1→* `donations[campaign_code]`.
3. Add a date table — **do not use `CALENDARAUTO()`**:

   ```dax
   Date = CALENDAR(DATE(2016, 1, 1), DATE(2026, 8, 17))
   ```

   related to `donations[donation_date]`.

   `CALENDARAUTO()` scans every date column in the model — `date_of_birth`
   starts in **1946**, the 13 deliberate future `sign_up_date` rows and the
   stray 2026-11-30 donation push the top to **2027-12-31** — so it builds a
   ~29,950-row table. Neither Active Supporters measure touches `'Date'`, so
   the four gate numbers below survive it; what it breaks is `Income This Year`
   (`DATESYTD`) and every by-month visual, which gain eighty years of empty axis.

   **Check before you go further: `MAX('Date'[Date])` must read 2026-08-17.**

   One row stays outside the range whatever you do: the 2026-11-30 donation
   lands in the blank date member and disappears from anything sliced by month.
   Deliberate, and harmless — the totals do not go through the Date table.
4. Add every measure from `reports/fundraising-summary/measures.dax` verbatim.
5. Canvas: two card visuals — **Active Supporters** and **Total Income** —
   then income by campaign and income by channel underneath.

**Check before you save:** Active Supporters reads **2,447** and Total Income
reads **£947,087.50**. If either is different, something got filtered.

## Report 2 — Supporter Engagement

1. Get Data → the same three CSVs plus `data/campaign_activity.csv`.
2. **On the donations query only**, add the filter step from
   `reports/supporter-engagement/model.md` — Advanced Editor, paste the M
   verbatim. This is the one line the whole segment turns on, so make sure it is
   in the applied-steps list where it can be pointed at on screen.
3. Same relationships, plus `campaign_activity` to `campaigns` and to
   `supporters`.
4. Add every measure from `reports/supporter-engagement/measures.dax`.
5. Canvas: the same two cards, plus open rate and click-through rate.

**Check before you save:** Active Supporters reads **1,832** and Total Income
reads **£930,092.50**.

## Have ready for the room

- Both reports **open in separate windows**, cards visible, side by side.
- The Supporter Engagement query's **Applied Steps pane open on the `NoRefunds`
  step**. When the room asks "why is the income different", you click one step
  rather than explaining it.
- A blank `.pbix` with the five CSVs loaded, for the build segment.

## If a number does not match

Almost always one of three things: a query filtered during load, the date table
running past 2026-08-17 (see step 3 — this one is deterministic, not bad luck),
or data types coming in as text. Check the applied steps before you change any
measure.

Do not "fix" a number by changing a measure. The measures are the teaching
artifact and they are correct as written.
