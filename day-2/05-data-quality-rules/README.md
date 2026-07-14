# Exercise — Data-quality rules from a schema: meaningful vs noise

Claude will happily generate thirty data-quality rules from a schema. The skill isn't generating them —
it's **keeping the six that matter and rejecting the noise.** A rule that fires on healthy data is worse
than no rule: it trains everyone to ignore the alerts.

## Steps

1. **Generate.** With your data dictionary (or the schema) in scope:
   > `From this data dictionary for the donor table, propose data-quality rules — one per line, each`
   > `with the column, the check, and why it matters.`

2. **Sort every rule into meaningful or noise.** Ask of each: *does violating this rule mean the data is
   actually wrong for how we use it — or is it just variation?*

3. **Keep the meaningful, in `docs/data-quality-rules.md`.** Write each as something you could run
   (a SQL predicate or a plain assertion), so it's a check, not a wish.

## The tests

**Meaningful** (real defects, tied to compliance or use):
- `nhs_number` must be 10 digits **and** pass the Modulus-11 checksum.
- `status` must be one of {Active, Suspended, Withdrawn, Deferred} — catches the `Activ` typo.
- age at `registered_date` within 16–30 (per ADR 0001, completed years).
- `registered_date` not in the future.
- no duplicate person (same `nhs_number` + `date_of_birth`, different `donor_id`).

**Noise** (fires on healthy data — reject, and be able to say why):
- "postcodes must be uppercase / consistently spaced" — realistic messiness, not a defect.
- "phone numbers must match one format" — several valid formats exist by design.
- "every donor must have `consent_research = 1`" — that's a business choice, not a quality rule; `0` is valid.
- "names must be title-cased" — cosmetic; not a data-quality failure.

## What you're really learning

- A DQ rule is only worth having if a violation means **wrong for your use**, not merely *different*.
- The generator is cheap; the **judgement** is the value — and it comes from the domain (glossary,
  compliance), which is exactly why the KB you're building matters.
