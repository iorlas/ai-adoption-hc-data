# Game — keep it or bin it?

**5 minutes, out loud, as a room.**

Six rules Claude proposed for this dataset. For each: **keep it, or is it
noise?**

The test, every time:

> Does breaking this rule mean the data is **wrong for how we use it** — or just
> different from how I would have typed it?

A rule that fires on healthy data is worse than no rule. In a month nobody reads
the alerts, and the real failure walks past.

---

## The cards

### 1. `status` must be one of Active, Lapsed, Inactive, Deceased

### 2. Postcodes must be consistently formatted

### 3. Every supporter must have an email address

### 4. A donation must reference a supporter who exists

### 5. `marketing_consent` must be 1

### 6. No two rows should be the same person

---
---
---

# STOP

**Call all six first.** Everything below is the answers.

---
---
---

## Verdicts

### 1. `status` must be one of Active, Lapsed, Inactive, Deceased

**Keep.** 18 rows say `Activ`. Those 18 people are missing from every report
that filters on Active, and nobody has noticed. Highest-value rule on the page.

### 2. Postcodes must be consistently formatted

**Bin it.** 300 rows are lowercase and unspaced — realistic messiness, not a
defect. Normalise on read. Keep it and you have an alert firing 300 times that
teaches everyone to ignore alerts.

### 3. Every supporter must have an email address

**Bin it.** 146 do not, and plenty of people legitimately never give one. A fact
about your supporters, not a fault in the data.

### 4. A donation must reference a supporter who exists

**Keep.** 30 do not. Those gifts cannot be attributed to anyone, so every
supporter-level total is quietly understated — and it will never look wrong.

### 5. `marketing_consent` must be 1

**Bin it, and notice why this one is different.** Not messy data — a lawful
choice recorded correctly. A rule like this does not just create noise; it
implies the answer should have been yes.

### 6. No two rows should be the same person

**Keep.** 22 people appear twice, same name and date of birth, different
`supporter_id`. Every count of *people* is wrong by 22, and every per-supporter
average is wrong by more.

---

## The lesson

Three kept, three binned, and the binned ones took just as long to think about.

**The generator is cheap. The judgement is the value** — and the judgement comes
from knowing how the data is used, which is exactly what Claude does not have
and you do.

If your list has twenty rules on it, you have a document nobody will read. Six
is a good number.
