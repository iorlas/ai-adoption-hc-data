# Take-home 2 — AI-assisted data engineering, on your own work

One self-contained take-home. Read the picture, do the practical slice on a repo you actually maintain,
then compare what you built against the best-practices at the end. Build first, calibrate second.

---

## Part 1 — What a day of AI-assisted data engineering looks like

Not "AI writes your pipelines while you watch." The model does the reading, drafting, and grunt work;
**you own the outcome and the context.** This is the working style the two days were building toward.

- **Pick up a task — orient in minutes, not an hour.** Point Claude at the repo: *"what does this proc do,
  and what changed since I last touched it?"* Then **verify** the summary against the code — never take the
  explanation on trust.
- **Do the work — describe the outcome, own the diff.** You describe the outcome, not the keystrokes;
  Claude drafts. Nothing ships unseen: read the `/diff`, run `/code-review`, run the tests. The data rows
  never enter the model — Claude reads code and schema, the data stays on your machine.
- **Hit a decision — write it down once.** When you settle a real trade-off, capture it as an **ADR**, so
  next week's session (yours or a teammate's) doesn't re-propose the option you already rejected.
- **When Claude stumbles — that's the signal, not a failure.** A wrong answer or a missing-context moment
  is the cue to **improve the knowledge layer**: add the fact to CLAUDE.md or a `docs/` file. The next
  attempt is better, for everyone, because it lives in Git.
- **Verification is constant.** You ask the one cheap question a wrong answer can't survive (Day 1's five
  tells). Owning the outcome is a habit, not heroic double-checking.
- **Governance is a habit, not a gate.** Code, not rows. Mask before commit. You can see what Claude read.
- **The measure, over weeks:** you tell Claude **less** while it does the **same or more** — because the
  context now lives in the repo and compounds. That declining-instruction curve is the whole point.

---

## Part 2 — The task (Claude Code CLI, on a repo you maintain)

This week, on **one** proc, pipeline, or repo you actually maintain:

1. **Explain it.** Point Claude at it; ask what it does and to flag one risk. Verify the answer — the one
   cheap challenge a wrong answer can't survive.
2. **Fix one real bug** (or make one real improvement), end to end in Claude Code — `/diff`, review, done.
3. **When Claude stumbles** — a wrong answer, missing context, or it repeats something you already
   rejected — capture what it was missing into a thin CLAUDE.md + one `docs/` file (or an ADR for a
   decision), then re-run and watch it improve. Make a little mess first, then structure it.
4. **Before/after.** Run the same question before your CLAUDE.md existed and again after. Note the difference.

This is where today stops being a workshop and becomes your practice.

### Governance — because this is real data now

- **Code, not rows.** Claude reads your SQL, schema, and code — never bulk data rows. Deny-list the raw
  data directory so it can't read PII by accident.
- **Mask before it's written down.** Any sample that lands in a doc is redacted — never a real identifier.
- **You can see what it read** — that's your audit trail.

### What to bring back — and what NOT to

**Do not send anyone your real data or code.** Bring back only:
- your **CLAUDE.md**,
- your **`docs/` hierarchy** (the tree + one line on what each file is),
- **2–3 takeaways** — what worked, where Claude stumbled, what you'd change.

That is enough to compare and discuss; your data never leaves your machine.

---

## Part 3 — CLAUDE.md best practices (compare after you build)

Read this **after** you've built your own CLAUDE.md + `docs/` — compare what you did to it.

**The one idea:** CLAUDE.md is loaded on **every** prompt — you pay for it every message and it shapes
**everyone's** sessions. So keep it **tiny** (pointers and hard rules) and let depth live in `docs/`, read
on demand. That is progressive disclosure. A 400-line CLAUDE.md is a tax on every prompt for context most
prompts don't need.

**What goes where:**

| In CLAUDE.md (always loaded, keep tiny) | In `docs/` (read on demand) |
|---|---|
| Stack + where things live (pointers) | Full data dictionary, column ranges |
| Hard rules ("no cursors", "don't edit seed data") | Glossary of domain terms |
| PII / data-safety policy | ADRs (decisions + rejected options) |
| One-line pointers into `docs/` | Reference implementations (code to copy) |

**Rules of thumb:**

1. **Write for Claude first, humans second** — terse and concrete. If you can't say it in a line, link a doc.
2. **Every edit is a shared blast radius** — CLAUDE.md is committed, so your change alters every teammate's
   sessions. Review CLAUDE.md changes like code.
3. **Pointers, not prose.** "Data dictionary: `docs/data-dictionary.md`" beats inlining the dictionary.
4. **Capture decisions as ADRs, not memory** — without one, a fresh session re-proposes what you already rejected.
5. **Reference implementations must be owned** — a stale "best in show" file teaches the wrong pattern
   confidently. Update it the day the pattern changes, or delete the pointer.
6. **Stop writing giant prompts** — the good prompt you wrote twice wants to be a `docs/` entry (or a skill).
7. **Never commit real PII** — mask every sample; synthetic/redacted only.
8. **Follow the feedback loop** — when Claude can't find something or repeats a rejected idea, that is the
   signal to add or restructure a doc. Make a little mess first, then structure it.

**The measure of success:** over weeks you tell Claude *less* while it does the *same or more* — the
context now lives in Git and compounds.

---

## Feedback pulse

Two lines back to me:
- Too basic / about right / want Databricks sooner?
- One thing you'll try on real work this week.

Steers the remaining sessions.
