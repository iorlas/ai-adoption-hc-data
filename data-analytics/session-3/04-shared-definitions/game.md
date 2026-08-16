# Game — where does this knowledge live?

**5 minutes, out loud, as a room.** Before you write anything down.

## Why this comes first

Once you know Claude reads `CLAUDE.md`, the instinct is to put everything in it.

Do that and within a month it is four hundred lines, every conversation is
slower, and nobody reads it — because **it is read on every single message.**
So it holds signposts and hard rules, and the depth lives elsewhere, read only
when a task needs it.

Getting this wrong is the most common way a team's first `CLAUDE.md` becomes
useless within a quarter. It costs five minutes to avoid.

## The four homes

| Home | What goes here | What it costs |
|---|---|---|
| **`CLAUDE.md`** | Short, always-true, always-useful. Pointers and hard rules | Paid on every message — keep it small |
| **A referenced document** | Anything big or occasional: definitions in full, a data dictionary, pipeline documentation. `CLAUDE.md` *points* at it | Free until something needs it |
| **A decision record** | A choice, its reasoning, and the options rejected | Free until read — and stops the same argument happening again |
| **Nowhere** | One-off questions, today's noise | Nothing |

Eight things. For each: **which home?** Call it, then read the answer.

---

**1.** *"Our reports live in `reports/`, one folder each."*

→ **`CLAUDE.md`.** One line, always true, saves a hunt every conversation.

**2.** *"The full definition of every measure we report, with the SQL, the DAX,
and what each one excludes — all fourteen of them."*

→ **A referenced document.** Too big to sit in context all day. `CLAUDE.md`
carries a pointer and the two or three measures that come up constantly.

**3.** *"We define active supporters by behaviour, not by the CRM status field —
and we rejected the status version because it counts people who last gave in
2019."*

→ **A decision record.** It has a rejected alternative and a reason. Without it,
the argument restarts every six months and Claude re-proposes the version you
threw out.

**4.** *"How many active supporters were there in July?"*

→ **Nowhere.** Ephemeral. Writing it down only adds noise.

**5.** *"`Activ` is a typo in the status column, not a real status. Treat it as
Active until the source is fixed."*

→ **`CLAUDE.md`.** Tiny, always true, and it prevents a whole class of wrong
answers. This is the highest-value line you will write all day.

**6.** *"Every column in the supporter table, what it means, and what makes a
value valid."*

→ **A referenced document** — a data dictionary. Point at it, do not inline it.

**7.** *"Refunded gifts are excluded from income, and the Fundraising Summary
report does not do this."*

→ **`CLAUDE.md` for the rule** ("refunds are excluded from income"), **a
decision record for why**, and a line in the documentation of that report saying
it disagrees. Three homes, because it is three different pieces of knowledge
wearing one sentence.

**8.** *"The supporter export landed two hours late this morning."*

→ **Nowhere.** Operational noise. It will not be true tomorrow.

---

## The lesson

**Match the knowledge to its home.** Tiny and always true → `CLAUDE.md`. Big or
occasional → a document it points at. A decision → a decision record. A one-off
→ nowhere.

Your `CLAUDE.md` should be short enough to read in a minute. If it is not, the
depth has leaked into it, and everything you do afterwards is slower for it.


Full page, if you want it again later:
[`reference/where-knowledge-lives.md`](../../reference/where-knowledge-lives.md).
