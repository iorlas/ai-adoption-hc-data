# Section 3 — The boundary (1:20, ~20 min)

Where AI **wins**, and where it **loses**. This is the heart of Day 1.

## Wins and losses

| AI tends to win | AI tends to lose |
|---|---|
| Bounded translation (SQL ↔ prose, one format ↔ another) | Correctness you can't see (silent wrong answers) |
| Pattern detection across many rows/files | Business context it was never told |
| Scaffolding (a first draft to react to) | Anything where "plausible" ≠ "true" |
| Explaining unfamiliar code | Judgement calls with real consequences |

The dangerous quadrant is **bottom-left of your attention**: answers that are fluent, confident, and
wrong. The registry data is full of traps for exactly this.

## Your turn — hunt the defects, then verify

Go back to `../01-hands-on-basics/explore.ipynb`, to the **"Your turn"** section. Working *through
Claude Code*, answer its six questions about the data (completeness, status vocabulary, age window,
impossible dates, duplicates, NHS validity).

**The rule that makes this Section 3 and not Section 1:** after every answer, **open the raw rows and
confirm it yourself.** Do not accept a summary. You are looking for the moment the model is confidently
wrong, vague, or incomplete — and you catch it because you looked at the data.

Remember the `Activ` value you noticed in Section 1? That kind of thing is why a report can quietly
under-count and no one notices for months.

## Done when

You can name **one specific claim** the model made and say exactly how you verified it — and, ideally,
one place where its first answer was wrong or incomplete and how you caught it. That is the deliverable,
not the profiling output. You will write it up as a verification log in Section 7.
