# 4 — One definition, shared across the team

**40 minutes, hands-on · Claude Code + a shared Markdown file (`CLAUDE.md`) + SQL**
*6 min we demo · 12 min you work · 5 min sorting drill, out loud · 8 min we
decide as a room · 9 min you write it up.*

The middle two matter most. The tool work is the easy half.

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

Same problem, two teams.

## The situation you are walking into

Two reports in `reports/`. Both real, both in use, both report **active
supporters**, and they disagree:

| Report | Active supporters |
|---|---|
| Fundraising Summary | 2,447 |
| Supporter Engagement | 1,832 |

A gap of 615 people, unresolved on an email thread since March.

**Neither report is lying.** They answer different questions, both reasonable,
neither written down. There is a third number neither reports, and a fourth that
only appears once you have done part 2.

## Why writing it down is the fix

Resolve it in a meeting and it drifts again in a month, because the definition
lives in someone's memory and someone else's DAX. A shared file does three
things at once:

1. **Your colleagues** can read it — the documentation that did not exist.
2. **Claude reads it too**, so it uses your definition rather than inventing a
   plausible one.
3. **It is versioned.** When it changes, you see when and why.

## Keeping AI honest, generally

**A thin `CLAUDE.md` is the reason Claude guesses.** Thin, it picks a definition
and sounds confident. Filled in, it uses yours and says which rule it applied.

That is the whole mechanism behind "stopping it inventing business rules". Not a
clever prompt — the rule was written where it could find it.

**The tell:** an answer that uses a business term without saying which
definition it used. That is your cue to ask.

## One warning before you write anything

Everything-in-`CLAUDE.md` is the instinct. Do that and in a month it is four
hundred lines that slow every conversation — because **it is read on every
single message.**

So: a five-minute sorting game, **[`game.md`](game.md)**. Getting this split
wrong is the most common way a team's first `CLAUDE.md` dies within a quarter.

---

# The exercise

**Find the disagreement, agree a definition, write it down.**

## Step 0 — The "before" answer (2 min, do not skip)

**▸ Everyone, us included — you need your own saved answer, not ours.**

**Scene.** Claude Code, in the `data-analytics` folder. **Start a new
conversation** — a fresh one, not the data-quality thread. That matters: this
step is about what Claude does when it has been told nothing.

Before you tell Claude anything, ask it:

> How many active supporters are there in this dataset?

**Save its answer.** Note which definition it chose and — more importantly —
whether it told you it was choosing one. Skip this and the end loses its point.

## Step 1 — Find where the two reports differ (~7 min)

**▸ We run it first, then you.**

**Scene.** Same conversation as step 0 — Claude needs to still be holding its own
"before" answer. Files in play: the two folders under `reports/`, each holding a
`measures.dax` and a `README.md`, plus the CSVs in `data/`.

> Read `reports/fundraising-summary/` and `reports/supporter-engagement/`.
> Both report a measure called Active Supporters and they give different
> numbers. Explain exactly why, in terms of the definitions each one uses.
> Then write the DuckDB SQL that reproduces each number from `data/`.

**What you should get.**

- Fundraising Summary counts rows where `status = 'Active'`. **2,447.**
- Supporter Engagement counts distinct supporters with a non-refunded donation
  in the last 12 months. **1,832.**

Run both. If the numbers do not come out, read the SQL Claude wrote rather than
the sentence above it — tell 3 in
[`reference/checking-the-answer.md`](../../reference/checking-the-answer.md).

Then push further:

> Are there any other differences between these two reports that would make
> other numbers disagree, not just Active Supporters?

There is at least one more, worth about £17,000, and it is **one line of Power
Query buried in one report's applied steps** — a headline figure moved by a step
three clicks deep that nobody outside that team knows exists.

## Step 2 — Find the numbers neither report gives you (~5 min)

**▸ Your turn.**

> Using the definitions you just found, what other reasonable definitions of
> "active supporter" could this data support? Give me each one, the SQL, and the
> number it produces.

**Four different numbers**, all defensible. One depends on part 2:

> Does the `status` column have any data-quality problem that changes the
> Fundraising Summary number?

That is the join between the two exercises. The typo is costing the headline
figure eighteen real people.

---

## Step 3 — Where does this knowledge live? (~5 min)

**▸ Together, out loud.**

Stop typing. Before you write anything down, the question is *where*.

Run **[`game.md`](game.md)** together. Eight items, four homes, answers out loud
before the reveal.

Item 7 is worth arguing about — the same refund step from step 1 wearing a
different hat, and it splits across more than one home.

## Step 4 — Decide (~8 min)

**▸ Together, out loud.**

Not Claude's part, and the reason the session exists. Put the four numbers on
screen:

1. When someone asks *"how many active supporters do we have?"*, what are they
   actually asking?
2. Which of the four answers **that**?
3. What do we call the others, so people stop using one name for two things?

You will probably land on **two named measures**, not one:

> The problem was never that there were two definitions. It was that there were
> two definitions with the same name.

---

## Step 5 — Write it up (~9 min)

**▸ Your turn.**

Three homes, from the drill.

**Scene.** Same conversation. Three files that already exist in the repo, each
with its headings in place and its content blank: `docs/measure-definitions.md`,
`CLAUDE.md` (top level), `reports/*/README.md`. **Open each one before you prompt
so you can see it change.**

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

Read it before you accept it:

- Is the SQL the SQL you agreed?
- **Did it quietly change something you did not ask it to touch?** It was told
  not to. This is what the desktop app's change view is for.

**5c — the decision, into a decision record (~2 min)**

> Draft `docs/decisions/0001-active-supporter.md` from this conversation, using
> the shape in `docs/decisions/0000-template.md`. You have the context: the two
> reports, the four candidate definitions, what we chose and what we set aside.
> Mark anything you are unsure we actually said, rather than inventing it.

Read it and correct it. Two minutes, and it is the difference between a decision
that holds and one re-litigated in March.

**You did not write a document. The document was the residue of work you had
already done.** Session 4 makes the same move with the pipeline.

**5d — the payoff (~2 min)**

Start a **new conversation** and ask exactly what you asked in step 0:

> How many active supporters are there in this dataset?

Side by side. It should now use your definition, name it, and say what it
excludes.

*You did not make the model smarter. You wrote down what your team means — and
because it is in a file, every future conversation inherits it.*

## Step 6 — Confirm ready

Tell us when you can show:

1. `docs/measure-definitions.md`, filled in
2. `CLAUDE.md` with a short Definitions section — a pointer, not the content
3. The before answer and the after answer, side by side

---

## What you leave with

| Artifact | Where | Why there |
|---|---|---|
| The full definitions, with SQL and DAX | `docs/measure-definitions.md` | Depth. Read only when a task needs it |
| A short pointer plus the hard rules | `CLAUDE.md` | Paid for on every message — keep it small |
| The decision, and what you rejected | `docs/decisions/0001-*.md` | Stops the argument restarting in March |

Plus the before-and-after answer, which is the part that lands.

---

## If it goes wrong

**The numbers do not match.** Ask whether it joined `supporters` — distinct
`supporter_id` in `donations.csv` alone gives 1,843, because some donations
point at supporters not on file. And check the reference date: "last 12 months"
means twelve months back from today.

**It rewrites the whole of `CLAUDE.md`.** It was told not to. Undo, ask again
more narrowly. Worth seeing: it is why you read a change before accepting it.

**It puts the full definitions in `CLAUDE.md` anyway.** Very common. Tell it to
move them to `docs/measure-definitions.md` and leave a pointer. Notice how much
shorter `CLAUDE.md` got, and that nothing was lost.

**The "after" answer is no better.** Either the conversation was not restarted,
or the definition went somewhere Claude does not read. Check it edited the
`CLAUDE.md` at the root of the project.

**You run out of time.** Drop 5c — the decision record moves to the close, or to
your own time. Do not drop 5d.
