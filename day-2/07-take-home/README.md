# Stage 07 — Take-home 2 + feedback

## First, the picture

Read [`a-day-with-ai-assisted-de.md`](a-day-with-ai-assisted-de.md) — the working style the last two days
were building toward. The take-home below is a *slice* of that day, done on your own work.

## Take-home 2 — do real work on your own data (Claude Code CLI)

This week, on **one** proc, pipeline, or repo you actually maintain:

1. **Explain it.** Point Claude at it; ask what it does and to flag one risk. Verify the answer — the one
   cheap challenge a wrong answer can't survive (Day 1's five tells).
2. **Fix one real bug** (or make one real improvement), end to end in Claude Code — `/diff`, review, done.
3. **When Claude stumbles** — a wrong answer, missing context, or it repeats something you already
   rejected — *that's the signal.* Capture what it was missing into a thin CLAUDE.md + one `docs/` file
   (or an ADR for a decision), then re-run and watch it improve. Make a little mess first, then structure it.
4. **Before/after.** Run the same question before your CLAUDE.md existed and again after. Note the difference.

This is where today stops being a workshop and becomes your practice.

## Governance — because this is real data now

- **Code, not rows.** Claude reads your SQL, schema, and code — never bulk data rows. Deny-list the raw
  data directory so it can't read PII by accident.
- **Mask before it's written down.** Any sample that lands in a doc is redacted — never a real identifier.
- **You can see what it read** — that's your audit trail.

## What to bring back — and what NOT to

**Do not send me your real data or code.** Bring back only:
- your **CLAUDE.md**,
- your **`docs/` hierarchy** (the tree + one line on what each file is),
- **2–3 takeaways** — what worked, where Claude stumbled, what you'd change.

That's enough to compare and discuss on Wednesday; your data never leaves your machine.

Once you've built yours, read [`claude-md-best-practices.md`](claude-md-best-practices.md) and **compare
what you did to it** — build first, calibrate second.

## Feedback pulse

Two lines back to me:
- Too basic / about right / want Databricks sooner?
- One thing you'll try on real work this week.

Steers Days 3–4.
