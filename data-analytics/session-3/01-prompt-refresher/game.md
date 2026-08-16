# Game — would you send it?

**5 minutes, out loud, as a room.**

Five prompts. For each one: **would you send it as it is, or is something
missing?** Call it, then read the answer.

There is no trick. Two of the five are fine exactly as they are, and spotting
that is as much the point as spotting the gaps.

---

### Card A

> *"look at the donations file and tell me if there's anything wrong with it"*

**Send it? — Nearly.** The question is clear and the file is findable.

What you will get back is **prose**: a paragraph of plausible observations with
no numbers you can check. Missing the **task** — what you want handed back.

**Fix:** *"…show me the SQL you ran and how many rows fail each check."*

---

### Card B

> *"how many rows are in supporters.csv?"*

**Send it. Nothing is missing.**

Claude can see the file, the question is unambiguous, and the answer is a
number. Adding a situation paragraph or an output spec here would make it longer
and no better.

**A short prompt is not a lazy prompt.** If someone in the room wanted to add
something to this one, that is the instinct worth naming and dropping.

---

### Card C

> *"profile the supporter data and give me a summary of the data quality"*

**Do not send.** Two problems, and the second is the dangerous one.

It has no **location** — nothing says how to get the answer, so it may well
write Python. And "give me a summary" invites exactly the kind of answer you
cannot check: *"the data is largely clean with some minor issues."*

**Fix:** name the means and demand the exceptions. *"…using DuckDB SQL. For each
problem, the SQL, the row count, and five example rows."*

---

### Card D

> *"I have a CSV file called `supporters.csv` which lives in the data folder of
> this project. It contains supporter records. I would like you to look at the
> `status` column in that file. My question is: what values does it contain? For
> your task, please count how many times each value appears and then present
> the results to me in a table."*

**Send it — it will work fine.** It is just four times longer than it needs to
be.

Every part is filled in because the boxes were there, not because the answer
needed them. `"Show me every distinct status with its row count"` gets the same
result.

**Filling in all the parts is not the goal.** The goal is an answer you can
check.

---

### Card E

> *"how many active supporters do we have?"*

**Do not send** — and this is the interesting one, because nothing is
structurally missing. Situation, question and task are all there or implied.

It is unanswerable anyway, because **"active" is not defined.** You will get a
confident number, it will be one of at least four defensible answers, and
nothing in the reply will tell you which one you got.

**Fix, for today:** *"…and tell me which definition you used."* **Fix, for
good:** write the definition down where Claude will read it — which is what we
do after the break.

---

## The lesson

Three parts — **situation, question, task** — and you use the ones the answer
actually needs.

**Add a part when the answer came back wrong in a way that part would have
prevented.** Cards A and C were missing something real. Card D was missing
nothing and said it four times. Card B was already right.

Card E is the one to remember: **a well-formed prompt can still be
unanswerable**, and the fix is not a better prompt. It is a shared definition.
