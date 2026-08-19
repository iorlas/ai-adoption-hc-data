# Answers — 2 · Genie, from the builder side

**FACILITATOR ONLY. Never on screen.**

## This part does not exist unless you build it

`facilitator/prep-denis.md` has the full list. The short version: a Genie space
over a schema holding the donor table, **and a way to show it both undocumented
and documented within eight minutes.**

The reliable way to do that is **two spaces**, not one edited live: `AN Donor
(raw)` with no comments and no definitions, and `AN Donor` with all three fixes
applied. Editing metadata live in front of a room, waiting for it to take
effect, and hoping the second answer differs is a way to lose the segment.

**Screen-record both halves the day before.** If the workspace is slow or the
warehouse is cold, play the recording and narrate it. Nobody in the room cares
whether it is live; they care whether the point lands.

## The moment the segment is built around

The first answer — undocumented space, *"how many active donors do we have?"* —
should come back around **2,885**, from `where status = 'Active'`, with no
mention that 20 rows say `Activ`.

The second answer, with the column comment in place, should either come back
2,905 with the caveat, or 2,885 *and say why*. **Either is a win.** The claim is
not "Genie became correct"; it is "Genie became honest, because somebody wrote
down what the column means."

If the second answer is identical and adds nothing, do not pretend otherwise.
Say: *"the metadata did not change the answer here — it changed what Genie could
tell me about the answer, and on a real question that is the difference."* Then
move to the comparison, which does not depend on this.

## The comparison — what actually happens

Genie is confined to the warehouse. Claude Code, pointed at the repo, can reach
`later-days/adf/dataflow_donor_import.json` and explain **why** the twenty rows
are missing. That asymmetry is the whole segment and it is worth stating
directly.

Do not stage a contest. The framing is *different kinds of trustworthy*, and the
room contains people who will use both.

## Game answers

| | Verdict | Why |
|---|---|---|
| **1** "donors registered in Manchester last quarter" | **Genie** | Entirely inside the warehouse, aggregate, repeatable. This is exactly what a curated space is for — and it is a question you want off your team's desk |
| **2** "why did the count drop by twenty" | **Claude Code** | The answer is not in the warehouse. It is in a filter in a JSON file. Genie can tell you *that* it dropped, never *why* |
| **3** "what does `consent_research` mean" | **Neither — argue about it** | See below |
| **4** "rewrite this notebook" | **Claude Code** | Genie does not write files. This is yesterday's part 2 |
| **5** "which flows can be converted" | **Claude Code** | It reads fourteen JSON files and sorts them. This is yesterday's part 4, in bulk, and it is the single most valuable thing in the four days for Adrian's team |

**Number 3, the one to hold.** Genie will answer, fluently, from the column name.
Claude Code will answer, fluently, from the column name. **Both are guessing,
and neither will say so unless the answer is written down somewhere.** The real
answer is a person, or a data dictionary written by that person — which is Day
2's whole argument arriving from a new direction. If the room says "Genie",
push: *"where would Genie have learned that?"*

## Time

25 minutes. If the part in front of it overran, cut in this order: **the game first** (they get the idea without it), **then the
bad-metadata half** (open on the documented space and describe the contrast).
Never cut the side-by-side — it is a question the client asked for by name.
