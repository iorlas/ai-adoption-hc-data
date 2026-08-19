# 1 — Take-home debrief, and a look at what you built

**15 minutes, out loud · nothing to type**

> **Who does what:** **▸ Together.** You talk, I take notes on the board. I
> have nothing prepared here that beats what you brought.

## Why it is first

Take-home 2 asked you to point Claude at a repo you actually maintain, fix one
real thing, and capture what it was missing into a `CLAUDE.md` plus a `docs/`
file. Whatever happened there is more useful than anything I can stage, for one
reason: **it is the only part of these four days that met your real code.**

You were asked to bring back three things and no data: your `CLAUDE.md`, the
shape of your `docs/`, and two or three takeaways.

## Round the room — three questions, in this order

**▸ Together.** Everyone answers 1. Answer 2 if you have one. Answer 3 if you
got that far.

1. **Where did it stumble?** Not "was it good." What did it get wrong, or ask
   for twice, or confidently invent?
2. **What did you write down because of that?** The line, file or ADR that came
   out of the stumble.
3. **Did the second run get better?** You were asked to run the same question
   before and after. Did the difference show?

Question 3 is the one that matters. Everything on Day 2 was an argument that
context compounds; you either saw it or you did not, and both are worth saying
out loud.

## The knowledge-base review

**▸ Together.** Two or three volunteers put their `CLAUDE.md` on screen —
**not** their code, and nothing with a real identifier in it.

What I will be looking at, and what you should look at in each other's:

| Look for | The question behind it |
|---|---|
| Is it **facts**, or is it **manners**? | "Be concise" changes nothing. "The `donor` table is keyed on `registry_id`, not `donor_id`" changes everything |
| Does it point at `docs/`, or try to contain everything? | A `CLAUDE.md` that grows past a screen stops being read — by people and by the model |
| Is there anything **it must not touch**? | Deny-listed paths, the raw data directory, the production connection |
| Would a **new joiner** learn something from it? | If yes, it is a real knowledge layer. If no, it is prompt decoration |

## Carry it into today

Whatever gaps this turns up, today's parts 2 and 4 both end by writing something
into `docs/`. That is not a ritual. It is the same move you just described,
applied to two artifacts none of you documented either.

---

**A note on the honest answer.** If your take-home did not happen — the week ran
away, or you were blocked — say so plainly and take the fifteen minutes as
someone else's demo. Nobody is graded here, and a room where only the wins get
reported teaches nothing.
