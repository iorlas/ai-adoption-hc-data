# Where does this knowledge live?

The four homes, and the rule for choosing. The full sorting drill runs inside
Session 3 —
[`session-3/04-shared-definitions/game.md`](../session-3/04-shared-definitions/game.md).

## Why it matters

`CLAUDE.md` is read on **every single message** — a cost you pay constantly. So
it holds pointers and hard rules; depth lives elsewhere and is read only when a
task needs it.

Get the split wrong and your `CLAUDE.md` is four hundred lines within a month,
every conversation is slower, and nobody reads it.

## The four homes

| Home | What goes here | What it costs |
|---|---|---|
| **`CLAUDE.md`** | Short, always-true, always-useful. Pointers and hard rules | Paid on every message — keep it small |
| **A referenced document** | Anything big or occasional: definitions in full, a data dictionary, pipeline documentation. `CLAUDE.md` *points* at it | Free until something needs it |
| **A decision record** | A choice, its reasoning, and the options rejected | Free until read — and stops the same argument happening again |
| **Nowhere** | One-off questions, today's noise | Nothing |

## The rule

**Match the knowledge to its home.** Tiny and always true → `CLAUDE.md`. Big or
occasional → a document it points at. A decision → a decision record. A one-off
→ nowhere.

Your `CLAUDE.md` should be readable in a minute. If it is not, depth has leaked
into it.
