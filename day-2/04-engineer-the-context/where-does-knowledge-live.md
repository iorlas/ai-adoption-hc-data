# Mini-game — Where does this knowledge live?

You learned something about the project. **Where do you put it so Claude uses it — without bloating
every session?** This is Day 1's "context is a budget" and "progressive disclosure" turned into a
sorting drill.

## The five homes

| Home | What goes here | Cost |
|---|---|---|
| **CLAUDE.md** | Short, always-true, always-useful pointers. Loaded *every* session. | Paid on every prompt — keep it tiny. |
| **Referenced doc** | Big or occasional knowledge (glossary, data dictionary, semantic model). CLAUDE.md *points* to it; Claude reads it on demand. | Free until read. |
| **ADR** | A decision + the alternatives you rejected and why. | Free until read; stops re-litigating settled calls. |
| **Reference implementation** | The canonical "this is what good looks like" file to copy. | Free until read. |
| **Just prompt it / nowhere** | One-off questions and ephemeral notes. Don't persist. | Zero. |

For each item below, pick a home before you read the answer.

---

1. **"Our stored procedures live in `/procs`."**
   → **CLAUDE.md.** One line, always true, saves a filesystem hunt every session.

2. **"Every column's meaning + valid range (all 14 of them)."**
   → **Referenced doc** (a data dictionary), pointed to from CLAUDE.md. Too big to sit in-context all day.

3. **"We fix DQ issues by snapshot-then-correct, never in-place `UPDATE` — and we rejected in-place."**
   → **ADR.** It's a decision with a rejected alternative. Next session won't re-propose in-place edits.

4. **"The canonical shape of a new Databricks ingestion notebook."**
   → **Reference implementation.** Point new work at it as a template. (Keep it maintained — a stale
   "best in show" file teaches the wrong pattern.)

5. **"What's the average donor age right now?"**
   → **Just prompt it.** Ephemeral. Persisting it only adds noise.

6. **"`Drag Race` is a real campaign name, not a typo — don't 'fix' it."**
   → **Referenced doc (glossary).** This is the war story from Day 1: a glossary line stops Claude
   flagging false problems on domain vocabulary.

7. **"The 20-row seed is a sample; the real `donor` table has 5,005 rows."**
   → **CLAUDE.md caveat** (or a short data-doc line). Cheap, and it heads off the exact wrong-scope
   answer from *Spot the wrong answer*, Card C.

8. **"Heads up — today's export landed two hours late."**
   → **Nowhere.** Operational noise with no lasting value. Don't commit it.

---

## The lesson

The instinct to "write it all in CLAUDE.md" is how CLAUDE.md becomes a 400-line tax paid on every
prompt. **Match the knowledge to its home:** tiny-and-always-true → CLAUDE.md; big-or-occasional →
a referenced doc; a decision → an ADR; a pattern → a reference implementation; a one-off → nowhere.
That is progressive disclosure — Claude reads deep only when the task needs it.
