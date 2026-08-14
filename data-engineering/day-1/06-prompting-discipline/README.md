# Section 6 — Prompting & context discipline (2:25, ~20 min)

Same data-engineering task, two prompts. Run both against the donor data and feel the difference. This
is Section 2's "context management" turned into a concrete habit.

## The task

*"Check the `registered_date` column for data-quality problems."*

## Run the bad one, then the good one

`bad-prompt.md` and `good-prompt.md` are matched lists — most good prompts are the direct fix of a
bad one. Pick a bad prompt, run it, then run its good counterpart against Claude Code (with
`../data/donor.csv` in scope) and compare what comes back.

- The **bad** prompts are vague: no file named, no rule stated, no evidence asked for. You get a
  plausible essay you then have to fact-check from scratch.
- The **good** prompts name the file, state the business rule, and demand **row-level evidence**.
  You get a checkable answer — and checking it is trivial because it points at the rows.

## The lesson

A good prompt does the model's scoping *for* it: **which data, which rule, what evidence.** That is
not politeness, it is context management — you are deciding what goes in the box and what "done" looks
like. Every hour it saves you in re-checking is the whole return on this section.

> Rule of thumb: if you can't verify the answer from what the prompt asked for, the prompt was too vague.
