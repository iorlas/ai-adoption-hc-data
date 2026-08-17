# Game — which one would you reach for?

**3 minutes, out loud.**

Five questions. For each: **Genie, Claude Code, or either?**

The rule underneath: **Genie is stronger when the whole answer lives inside a
warehouse someone has already curated. Claude Code is stronger when the answer
needs context that is not in the warehouse.**

---

## The cards

**1.** *"How many donations came in last month, by campaign?"*

**2.** *"Why does this dashboard's supporter count differ from that one's?"*

**3.** *"Which of our campaign codes have no matching campaign record?"*

**4.** *"What does the weekly supporter pipeline do to records with a missing
region?"*

**5.** *"Give me the same figures as last quarter's board pack, refreshed."*

---
---
---

# STOP

**Call all five first.** Everything below is the answers.

---
---
---

## Verdicts

**1.** *"How many donations came in last month, by campaign?"*

→ **Either.** One clean question against curated tables. Genie is probably
faster because it knows the schema; Claude Code wants to be told where things
are. Neither is wrong.

**2.** *"Why does this dashboard's supporter count differ from that one's?"*

→ **Claude Code.** The answer is not in the warehouse — it is in two reports'
measure definitions and a Power Query step. Genie cannot see any of that.

**3.** *"Which of our campaign codes have no matching campaign record?"*

→ **Either.** Pure warehouse question. Genie answers it in one line if the
tables are in its space.

**4.** *"What does the weekly supporter pipeline do to records with a missing
region?"*

→ **Claude Code.** That is a JSON file, not a table. Genie has no idea the
pipeline exists.

**5.** *"Give me the same figures as last quarter's board pack, refreshed."*

→ **Genie, if the definitions are curated in its space** — that is what a Genie
space is for. **Claude Code if they are not**, because then the definitions have
to come from a file you wrote.

---

## The lesson

Nobody won. Two questions went either way, and the deciding factor was never
which tool is cleverer — it was **where the answer lives.**

Question 5 is the real point: whichever tool you use, the definitions have to be
written down *somewhere* it can read. In Genie that is a curated space. In
Claude Code it is a file in your project.

Which is what we do straight after the break.
