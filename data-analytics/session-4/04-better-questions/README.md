# 4 — Asking better questions of your data

**35 minutes, hands-on · Claude Code + SQL**
*6 min we demo · 24 min you do it · 5 min share-back.*

> **Who does what:** **▸ We run it first, then you** — watch, then repeat it ·
> **▸ Your turn** — you drive, we are on the floor · **▸ Together** — whole room,
> out loud. Nothing here is a test.

## The line, and we agree with it

Lauren:

> "We'd prefer to use Claude more for the coding side of things, and the
> analysis should be primarily done by analysts themselves."

So this is **not** AI doing your analysis. It is you having a hypothesis and
getting to a trustworthy answer with less typing. The judgement stays yours. The
typing does not.

## What the division of labour actually is

| You | Claude |
|---|---|
| Decide what is worth asking | Writes the SQL |
| Say what would change your mind | Runs it, shows the result |
| Read the query and check it answers your question | Reshapes it when you say it did not |
| Decide whether the answer is real or an artefact | Enumerates the alternatives you have not tried |
| Say what it means | — |

The row that matters is the fourth. **"Is this real, or is it an artefact of how
I asked?"** is the question that separates an analyst from a query.

## The failure mode to watch

You ask a question, get a number, and it confirms what you expected. You move
on.

> Nobody checks a comfortable answer. That is the whole failure mode. So say out
> loud what would make you disbelieve it, before you look.

Then check that thing first.

This session's data gives you plenty of material — after Monday you know the
duplicates, the orphans, the impossible dates and the typo are all in there, and
every one of them can produce a comfortable-looking wrong answer.

## The specific trap in this dataset

Anything you compute per-supporter is affected by the duplicate people. Anything
you compute per-campaign is affected by the donations pointing at campaigns that
do not exist. Anything time-based is affected by the impossible dates.

None of those will make an answer look obviously wrong. They will make it look
slightly different from the truth, which is much harder to catch — and is why
the first move on any real question is *"what in this data could make this
answer wrong?"*

---

# The exercise

Hypothesis, query, answer you trust.

Two hypotheses to test. **The first is fundraising-shaped, the second is
operational-shaped** — pick whichever is closer to your team's work and do that
one properly rather than both badly. If you have time, do the other.

---

# Hypothesis A — fundraising

> **"Supporters who came in through Events give more over their lifetime than
> supporters who came in through Direct Mail."**

## A1. Before you ask, say what would change your mind (~3 min)

**▸ We run it first, then you.**

Write it down first — one line. Something like: *"if the difference is under
10%, or if it disappears once I account for how long each group has been on the
database, I do not believe it."*

Then hand Claude the whole thing:

> Test this hypothesis against `data/`: supporters acquired through Events have
> a higher lifetime donation total than those acquired through Direct Mail.
> Write the SQL, run it, and show me both. Use the definitions in `CLAUDE.md`.
>
> Before you give me the answer, tell me what in this data could make the result
> misleading.

That last line changes the answer materially. Try it once without it if you want
to see the difference.

## A2. Read the query, not the number (~5 min)

**▸ Your turn.**

Three things to check in the SQL it wrote:

- Did it exclude refunded donations? Does that match what you agreed on Monday?
- What did it do about supporters who appear twice?
- Did it compare lifetime totals without accounting for **how long** each group
  has been on the database? Someone who joined in 2016 has had longer to give.

If it did not handle those, that is not a failure of the tool. It is the part
that was always yours.

## A3. Attack your own result (~8 min)

**▸ Your turn.**

> Now control for time on the database — compare average giving per year since
> sign-up rather than lifetime total. Does the conclusion hold?

> Is the difference driven by a small number of large gifts? Show me the
> distribution, not the mean.

> Do the duplicate supporter records affect this result? Quantify it.

At least one of these should change your picture. If none of them does, you have
a robust finding — which is worth knowing with confidence rather than assuming.
Not every check overturns something, and knowing a finding is robust is also a
result.

## A4. The sentence (~3 min)

**▸ Your turn.**

> Write two sentences I could say in a meeting: what we found, and what it does
> not tell us.

The second sentence is the one that makes it defensible. A finding without its
limits is not defensible, and defensibility is the through-line of both days.

---

# Hypothesis B — operational

> **"Complaints take longer to resolve than other task types, and it is getting
> worse."**

Same shape, using `data/fulfilment_tasks.csv`.

## B1. Say what would change your mind (~3 min)

**▸ We run it first, then you.**

Then:

> Test this against `data/fulfilment_tasks.csv`: complaints take longer to
> resolve than other task types, and resolution time is getting worse over time.
> Write the SQL, run it, show me both.
>
> Before the answer: what in this data could make this result misleading?

## B2. The specific traps in this table (~5 min)

**▸ Your turn.**

Ask each of these directly:

> How are you treating tasks with `status` = 'Complete' versus 'Completed'?

> How are you treating tasks marked complete with no `completed_date`? Does
> excluding them bias the result, and in which direction?

> Are there tasks completed before they were created? What did you do with them?

The second one is the interesting one and it is genuinely subtle. If unfinished
work is more likely to have a missing completion date, dropping those rows makes
your average resolution time look **better** than it is — the slowest cases
quietly leave the sample.

## B3. Push on the trend (~5 min)

**▸ Your turn.**

> Is the trend real, or is it an artefact of recent tasks not having been
> completed yet? Show me how you would tell the difference.

That is survivorship bias, and it is the single most common way an operational
"it's getting worse / better" finding turns out to be nothing.

## B4. The sentence (~3 min)

**▸ Your turn.**

Same as A4: what we found, and what it does not tell us.

---

## Confirm ready

Tell us when you can show:

1. Your hypothesis, and the thing you said in advance would change your mind
2. One check that changed your answer
3. The two sentences

---

## What you leave with

Working queries against the shared dataset, a clearer sense of where that line
between your judgement and the tool sits, and the habit of asking the one
question a wrong answer cannot survive.

---

## If it goes wrong

**It answers before you finish asking.** Long prompts get partial answers. Break
it into steps; the exercise is written as steps for that reason.

**The answer is confident and you cannot see the query.** Ask for it. Every
time. An answer without a query is not checkable, and unchecked is unusable.

**It refuses to give a number and hedges instead.** Usually means the question
was ambiguous. Say what you meant more precisely — which is itself the lesson.
