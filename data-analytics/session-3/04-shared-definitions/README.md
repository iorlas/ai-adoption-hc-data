# 4 — One definition, shared across the team

**40 minutes, hands-on · Claude Code + a shared Markdown file (`CLAUDE.md`) + SQL**
*6 min we demo · 12 min you work · 5 min sorting drill, out loud · 8 min we
decide as a room · 9 min you write it up.*

The middle two are the ones that matter. The tool work is the easy half.

> **Who does what:** **▸ We run it first, then you** — watch, then repeat it ·
> **▸ Your turn** — you drive, we are on the floor · **▸ Together** — whole room,
> out loud. Nothing here is a test.

## The problem, in your words

Lucie:

> "Are there shared prompts, or MD files we could share as a team, so
> everyone's using the same SQL?"

Lauren:

> "Say I have active members — making sure I'm using the same definition across
> different dashboards."

Same problem, two teams. This part builds the answer.

## The situation you are walking into

There are two reports in `reports/`. Both are real, both are in use, both report
**active supporters**, and they disagree:

| Report | Active supporters |
|---|---|
| Fundraising Summary | 2,447 |
| Supporter Engagement | 1,832 |

A gap of 615 people. There has been an unresolved email thread about it since
March.

**Neither report is lying.** They are answering different questions, both of
which are reasonable, and neither of which is written down anywhere. And there
is a third number available that neither of them reports, and a fourth that only
appears once you have done part 2 of this session.

## Why writing it down is the fix

You could resolve this in a meeting, and in a month it would drift again,
because the definition would live in someone's memory and someone else's DAX.

Writing it into a file the whole team shares does three things at once:

1. **Your colleagues** can read it — it is the documentation that did not exist.
2. **Claude reads it too.** Next time anyone in your team asks Claude for
   "active supporters", it uses your definition rather than inventing a
   plausible one.
3. **It is versioned.** When it changes, you can see when and why.

This is the same idea as curating definitions in a Genie space, except that it
lives in your own files, costs nothing, and works for both teams.

## Keeping AI honest, generally

This part is also where we cover the general case. A thin `CLAUDE.md` is the
reason Claude guesses. Watch what happens: with the file thin, ask it for active
supporters and it will pick a definition and sound confident. With the file
filled in, it uses yours and says which rule it applied.

That is the whole mechanism behind "stopping it inventing business rules". It is
not a clever prompt. It is that the rule was written down where it could find
it.

**And the tell to watch for:** an answer that uses a business term without
saying which definition it used. Every time. That is your cue to ask.

## One warning before you write anything

Once you know Claude reads `CLAUDE.md`, the instinct is to put everything in it.
Do that and within a month it is four hundred lines, every conversation is
slower, and nobody reads it — because **it is read on every single message.**

So this segment includes a five-minute sorting game, out loud, on what belongs
in `CLAUDE.md` and what belongs one pointer away: **[`game.md`](game.md)**.

Getting that split wrong is the most common way a team's first `CLAUDE.md`
becomes useless within a quarter, and it costs five minutes to avoid.

---

# The exercise

**Find the disagreement, agree a definition, write it down.**

## Step 0 — The "before" answer (2 min, do not skip)

**▸ Everyone, us included — you need your own saved answer, not ours.**

Before you tell Claude anything, ask it:

> How many active supporters are there in this dataset?

**Save its answer somewhere.** Note which definition it chose and — more
importantly — whether it told you it was choosing one.

We come back to this at the end. If you skip it now, the end of this exercise
loses its point entirely.

## Step 1 — Find where the two reports differ (~7 min)

**▸ We run it first, then you.**

> Read `reports/fundraising-summary/` and `reports/supporter-engagement/`.
> Both report a measure called Active Supporters and they give different
> numbers. Explain exactly why, in terms of the definitions each one uses.
> Then write the DuckDB SQL that reproduces each number from `data/`.

**What you should get.**

- Fundraising Summary counts rows where `status = 'Active'`. **2,447.**
- Supporter Engagement counts distinct supporters with a non-refunded donation
  in the last 12 months. **1,832.**

Run both queries. Check you get those numbers. If you do not, read the SQL
Claude wrote rather than trusting the sentence above it — that is tell 3 in
[`reference/checking-the-answer.md`](../../reference/checking-the-answer.md).

Then push it further:

> Are there any other differences between these two reports that would make
> other numbers disagree, not just Active Supporters?

There is at least one more, it is worth about £17,000, and it is **one line of
Power Query buried in one report's applied steps.** When you find it, sit with
it for a second: a headline figure is being moved by a step three clicks deep in
the Advanced Editor that nobody outside that team knows exists.

## Step 2 — Find the numbers neither report gives you (~5 min)

**▸ Your turn.**

> Using the definitions you just found, what other reasonable definitions of
> "active supporter" could this data support? Give me each one, the SQL, and the
> number it produces.

You should end up looking at **four different numbers**, all defensible. One of
them depends on something you found in part 2 of this session:

> Does the `status` column have any data-quality problem that changes the
> Fundraising Summary number?

That is the join between the two exercises. The typo is quietly costing the
headline figure eighteen real people.

---

## Step 3 — Where does this knowledge live? (~5 min)

**▸ Together, out loud.**

Stop typing for five minutes.

Before you write anything down, the question is *where*. The instinct, once you
know Claude reads `CLAUDE.md`, is to put everything in `CLAUDE.md` — and that is
how a `CLAUDE.md` becomes four hundred lines that slow down every conversation
and that nobody reads.

Run **[`game.md`](game.md)** together. Eight items, four homes, answers out loud
before the reveal.

Item 7 is the one worth arguing about. It is also, not coincidentally, the exact
thing you just found in step 1 — the same refund step wearing a different hat,
and it splits across more than one home.

## Step 4 — Decide (~8 min)

**▸ Together, out loud.**

This part is not Claude's, and it is the reason the session exists.

Put the four numbers on the screen and answer three questions:

1. When someone asks *"how many active supporters do we have?"*, what are they
   actually asking?
2. Which of these four definitions answers **that**?
3. What do we call the other ones, so that people stop using one name for two
   things?

You will probably land on **two named measures**, not one. That is the right
answer, and it is worth saying out loud why:

> The problem was never that there were two definitions. It was that there were
> two definitions with the same name.

---

## Step 5 — Write it up (~9 min)

**▸ Your turn.**

Three homes, from the drill you just did. All three files already exist with
their headings in place.

**5a — the depth, into the referenced document (~3 min)**

> Fill in `docs/measure-definitions.md` for the measures we agreed. For each:
> the plain-English sentence, what it deliberately excludes, the DuckDB SQL, the
> DAX equivalent, which reports use it, and any report that reports something
> similar under the same name. Also fill in the "Names we have retired" table.
> Leave the headings as they are.

**5b — the pointers and the hard rules, into `CLAUDE.md` (~2 min)**

> Add a Definitions section to `CLAUDE.md`. It should be **short**: a pointer to
> `docs/measure-definitions.md`, the one or two measures that come up
> constantly, and the hard rule that `status = 'Activ'` is a data-quality defect
> and must be treated as Active. Do not put the full definitions in this file.
> Do not change anything else in the file.

Read what it wrote before you accept it. Two things to check:

- Is the SQL the SQL you agreed?
- **Did it quietly change something you did not ask it to touch?** It was told
  not to. Watch whether it obeyed — this is the habit the desktop app's change
  view exists for.

**5c — the decision, into a decision record (~2 min)**

You just made a real decision with real rejected alternatives. That is the third
home from the drill.

> Draft `docs/decisions/0001-active-supporter.md` from this conversation, using
> the shape in `docs/decisions/0000-template.md`. You have the context: the two
> reports, the four candidate definitions, what we chose and what we set aside.
> Mark anything you are unsure we actually said, rather than inventing it.

Read it and correct it. Two minutes, and it is the difference between a decision
that holds and one that gets re-litigated in March.

Notice what just happened: **you did not write a document. The document was the
residue of work you had already done.** That is the same move Session 4 makes
with the pipeline.

**5d — the payoff (~2 min)**

Start a **new conversation** and ask exactly what you asked in step 0:

> How many active supporters are there in this dataset?

Put the two answers side by side. It should now use your definition, name it,
and say what it excludes.

Say it plainly to yourself: *you did not make the model smarter. You wrote down
what your team means. And because it is in a file, everyone — and every future
conversation — inherits it.*

## Step 6 — Confirm ready

Tell us when you can show:

1. `docs/measure-definitions.md`, filled in
2. `CLAUDE.md` with a short Definitions section — a pointer, not the content
3. The before answer and the after answer, side by side

---

## What you leave with

Three things, in three different places on purpose:

| Artifact | Where | Why there |
|---|---|---|
| The full definitions, with SQL and DAX | `docs/measure-definitions.md` | Depth. Read only when a task needs it |
| A short pointer plus the hard rules | `CLAUDE.md` | Paid for on every message — keep it small |
| The decision, and what you rejected | `docs/decisions/0001-*.md` | Stops the argument restarting in March |

Plus the before-and-after answer, side by side, which is the part that makes the
whole thing land.

---

## If it goes wrong

**It reproduces the numbers but they do not match.** Two usual causes. Ask
whether it joined `supporters` — counting distinct `supporter_id` in
`donations.csv` alone gives 1,843, because some donations point at supporters
who are not on file. And check the reference date: "last 12 months" means the
twelve months back from today.

**It rewrites the whole of `CLAUDE.md`.** It was told not to. Undo it and ask
again, more narrowly. This is worth seeing happen rather than avoiding: it is
exactly why you read a change before accepting it.

**It puts the full definitions in `CLAUDE.md` anyway.** Very common. Tell it to
move them into `docs/measure-definitions.md` and leave a pointer. Then notice
how much shorter `CLAUDE.md` got, and that nothing was lost.

**The "after" answer is no better.** Two usual causes: the conversation was
never restarted, so the old context is still in play; or the definition got
written somewhere Claude does not read. Check it edited the `CLAUDE.md` at the
root of the project.

**You run out of time.** Drop 5c — the decision record moves to the close, or to
your own time. Do not drop 5d.
