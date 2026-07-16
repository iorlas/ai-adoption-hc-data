# Day 2 — Engineer the context

Day 1: *the model can be confidently wrong, so you verify.*
**Day 2: the cure for wrongness is context you engineer — and because it lives in Git, it compounds.**

Today you take an inherited stored procedure (no docs, a cursor, a latent bug), use Claude Code to
understand and safely improve it, and — as a by-product — build the **knowledge layer** (`docs/` +
a CLAUDE.md that points at it) that makes the next person's version of that job easier. At the end you
re-run the *same* prompt you started with and watch the answer get visibly better.

Work through the stages in order — each folder is self-contained. **Data and the proc are reused from
`day-1/`** (no `uv sync` needed today — reuse Day-1's environment).

## The ladder

| Stage | Folder | You do |
|---|---|---|
| 0 | `00-claude-code-surfaces/` | Orientation: same engine, three cockpits (CLI vs Desktop vs VS Code extension) + know your cost (`/usage`, `/context`). |
| 1 | `01-spot-the-wrong-answer/` | Own the outcome: five tells for dismissing wrong answers fast, the game, and the commands that help (`/diff`, `/code-review`, `/security-review`, `/simplify`, `/usage`). |
| 2 | `02-understand-the-proc/` | Reverse-engineer a README for the proc, find its bug, fix it + test. |
| 3 | `03-sql-optimisation/` | Rewrite the cursor: several candidates compared on readability + plan. |
| 4 | `04-engineer-the-context/` | Build the KB — CLAUDE.md + data dictionary + glossary + reference impl. |
| 5 | `05-data-quality-rules/` | Generate DQ rules from the schema; keep the meaningful, cut the noise. |
| 6 | `06-bridge-databricks-adf/` | The bridge to Days 3–4: Databricks + ADF as more access paths. |
| 7 | `07-take-home/` | One self-contained take-home: a day of AI-assisted DE, the practical task on your *own* data, and CLAUDE.md best-practices to compare against. |

A complete, worked example of the knowledge layer you build in Stage 04 lives in
`templates/example-orders/` (a different domain, so it shows the shape without spoiling the exercise).

Facilitator conductor's score, answer key, and the payoff prompt live in `facilitator/` (never ships).

## Governance — the three rules that let you point this at real data (cross-cutting)

A healthcare team *can* use this on a PII-laden system because **Claude reads code, not rows.**
1. **Code, not data.** Taming the proc, Claude reads the SQL — the donor rows never enter the model.
2. **Mask before it's committed.** Any sample in a doc is synthetic/redacted — never a real NHS number.
3. **You can see what it read.** Claude shows every file it opens (your audit trail); deny-list the raw
   data directory so it can't read bulk PII by accident.

Dataset anonymisation *at scale* is your pipeline's job (ADF/Databricks masking), not Claude's — at
scale the model never touches the data anyway. Today's governance is only about the AI boundary.
