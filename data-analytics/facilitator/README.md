# Facilitator materials

**Not for attendees.** This repo is one repo, and it holds everything —
material, run sheets, answer keys. **It is public until it is made private
(planned: Friday 21 August 2026).** Until then, assume anyone who has the URL
can read the answers.

If it is ever handed over as-is, delete this folder, both
`session-*/facilitator/` folders, every `answers.md`, and `session-4/fallback/`.

| File | What it is |
|---|---|
| **`curriculum-design.md`** | **Read this first.** The design record: audience model, design rules, the artifact dependency graph, the reuse audit, and the three places this design deliberately reconciles against July |
| `generate_data.py` | Builds the five CSVs. Fixed seed — regenerating reproduces them exactly |
| `defect-manifest.md` | Every planted defect with its exact count, and the things that look wrong but are not |
| `campaign-category-key.csv` | The true category behind every messy `category_raw` value |
| `build-the-two-pbix.md` | How to build the two disagreeing reports in Desktop, and the numbers to check |
| `prep-checklist.md` | Everything that must be true before Monday |
| **`run-order.md`** | **Generated.** Who owns which block, beat by beat, plus a per-person view |
| `build-run-order.py` | Writes `run-order.md` from `BEATS`, the single source for the running order |
| `../session-3/facilitator/run-sheet.md` | Monday's spine — clock, standing rules, cut order, pre-flight |
| `../session-4/facilitator/run-sheet.md` | Tuesday's spine, same shape |
| `../session-4/facilitator/adf-issue-catalogue.md` | All nineteen planted pipeline issues, for when someone finds an unexpected one |

## Where the running detail lives

**In the stage folders, not here.** Every stage of both sessions has its own
`answers.md` alongside its `README.md`:

> what you do · what to say, in words · **how to assert** · the answer key for
> that stage · what goes wrong and what to do

So on the day you work from one folder at a time and never page between
documents. The two run sheets exist to tell you where you are in the clock and
what to cut — nothing else.

The answer keys used to sit at session level and were moved into the stages they
belong to. The only exception is the ADF issue catalogue, which spans three
stages and is genuinely long.

## Regenerating the data

```bash
uv run facilitator/generate_data.py
```

Seed 130, reference date 2026-08-17. **If you regenerate after changing the
script, every number in both answer keys, `verify.py`, `reports/`, and several
exercise files becomes wrong.** Re-check them against the new
`defect-manifest.md` before shipping. The numbers that appear in more than one
place:

- Row counts — `verify.py`, `data/README.md`, session-3 answer key,
  `02-data-quality/README.md`
- Active supporters (2,447 / 1,832) — `reports/README.md`, both `.dax` files,
  `04-shared-definitions/README.md`, session-3 answer key
- Income (£947,088 / £930,093, difference £16,995) — the same places, plus
  `05-build-and-verify/README.md`
- The channel and task-type tables — session-4 answer key

## Material in the repo that no segment uses

Deliberate, and worth knowing about rather than rediscovering.

**`campaigns.csv` → `category_raw`** carries 44 distinct free-text spellings of
8 real categories — the shape of Lauren's DotDigital and Google Worksheet
problem. `campaign-category-key.csv` holds the true category behind every one of
them, so a classification exercise is gradeable to the row.

**No segment in Sessions 3 or 4 uses it.** Classification was cut when the
August transcript reordered priorities to ADF and Power BI validation, and it
was the right cut. The material stays because:

- It is what Lauren's optional take-home points at, if she brings her export.
- A follow-up session on classification — `ai_classify`, or Claude over the
  categories — has a ready-made, graded dataset waiting.
- It costs nothing to leave in place, and the categories make `campaigns.csv`
  read like real data rather than a lookup table.

**Do not mention it in the room** unless someone asks what the column is for.
Naming a capability nobody is going to be taught is how a workshop ends with a
list of things it did not do.

## The design in one paragraph

Monday's spine is that **two live reports disagree about a headline number**,
and the disagreement has three separate causes — a definitional difference, a
Power Query step buried in one report, and a data-quality defect. Resolving it
requires all three sessions' worth of skill, which is why the segments feed each
other rather than standing alone. Tuesday's spine is that **an undocumented
pipeline can silently produce wrong answers**, and that the same habit —
write down what you worked out, where the next person and the next AI
conversation will find it — is the fix for both.
