# Section 7 — Governance, verification, and take-home (2:45, ~15 min)

The two disciplines that carry through the whole week, then your first take-home.

## Anonymise before AI

The donor data has real-shaped PII: `first_name`, `last_name`, `date_of_birth`, `email`, `phone`,
`postcode`, `nhs_number`. Even though every row here is **synthetic**, treat those columns as if they
were real: **the model must never see raw PII.** Mask, tokenise, or synthesise before anything leaves
the machine. (This is the same instinct behind your Purview work — classify first, then decide what
may travel.)

The mirror image for *actions* comes later in the week: read-only credentials are to actions what
anonymisation is to data.

## Verification is the through-line

Every exercise this week ends the same way: **not "the AI did it" but "I checked it."** The
deliverable is never the model's output alone — it is the output plus the evidence you verified it.
That is why every take-home closes with a verification log.

## Take-home 1

See `take-home-1.md`. In ~30 minutes: pick one column or relationship you did not fully explore,
document it through Claude Code, and **verify the description against the data**. Submit a completed
`verification-log-template.md`.

> **Day 2 opens with each person sharing their take-home for two minutes.** Come ready.
