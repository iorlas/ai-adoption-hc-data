# Game — converts, or does not

**▸ Together, out loud. Five minutes, no laptops.**

Six things you would find in a real Mapping Data Flow. For each one: **(a)
converts to a view cleanly, (b) converts but something is lost, or (c) does not
convert at all** — and in one sentence, what you would build instead.

Say your answer before the person next to you does. There is no prize.

---

**Card 1.** `filter(status == 'Active')`

**Card 2.** `derive(email = lower(trim(email)))`

**Card 3.** `alterRow(upsertIf(true()))` with a sink keyed on `registry_id`

**Card 4.** `lookup(a@code == b@code, multiple: false, pickup: 'any')`

**Card 5.** `keyGenerate(output(donor_id as long), startAt: 1L)`

**Card 6.** `source(..., allowSchemaDrift: true, ignoreNoFilesFound: false)`

---

## The one to argue about

Card 4 is the one people split on, and both sides are right, which is why it is
here. Hold it for last.
