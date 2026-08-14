# Good prompts

Each names **which data**, states **which rule**, and demands **what evidence** — so the answer is
checkable. Several are the fixed version of a prompt in `bad-prompt.md`.

1. **Dates** (fixes bad #1)
   > Using `../data/donor.csv`, check the `registered_date` column for data-quality problems.
   > Rules: (a) not in the future, (b) on or after the donor's `date_of_birth`, (c) a real,
   > parseable date. For each rule, tell me how many rows violate it and show up to 5 example rows
   > (with `donor_id` and the offending values) so I can confirm each one. No summary without the rows.

2. **Completeness** (fixes bad #2)
   > In `../data/donor.csv`, count blanks and nulls per column. List the columns with any missing
   > values, the count and percentage for each, and 3 example `donor_id`s per column. Verify by
   > counting in pandas, do not estimate.

3. **Ages** (fixes bad #5)
   > The registration age rule is 16 to 30 inclusive, computed as `registered_date` minus
   > `date_of_birth`. In `../data/donor.csv`, how many donors fall outside that window? Show me up to
   > 10 with `donor_id`, `date_of_birth`, `registered_date`, and the computed age so I can check them.

4. **Ethnicity** (fixes bad #6)
   > What values does the `ethnicity` column take in `../data/donor.csv`, and how often? Give me the
   > full value_counts (including blanks). Do not judge whether it "looks fine" — just the counts.

5. **Duplicates** (fixes bad #10)
   > Find likely duplicate donors in `../data/donor.csv`: rows sharing the same `nhs_number` and
   > `date_of_birth` but a different `donor_id`. Report how many pairs, and show each pair's
   > `donor_id`, `first_name`, `last_name`, `nhs_number` so I can eyeball them. Ignore blank NHS numbers.

6. **NHS validity** (fixes bad #9)
   > Check `nhs_number` in `../data/donor.csv`. A valid one is exactly 10 digits AND passes the
   > NHS Modulus-11 checksum. Report the count of invalid numbers, broken down by reason (wrong
   > length / non-digit / failed checksum), with up to 5 example `donor_id`s each.

**The pattern:** every one is answerable *and* verifiable, because it fixes **which data · which rule ·
what evidence** up front. That is context management, made into a habit.
