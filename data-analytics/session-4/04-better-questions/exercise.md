# Exercise — hypothesis, query, answer you trust

**35 minutes.** 6 min we demo · 24 min you do it · 5 min share-back.

Two hypotheses to test. **The first is fundraising-shaped, the second is
operational-shaped** — pick whichever is closer to your team's work and do that
one properly rather than both badly. If you have time, do the other.

---

# Hypothesis A — fundraising

> **"Supporters who came in through Events give more over their lifetime than
> supporters who came in through Direct Mail."**

## A1. Before you ask, say what would change your mind (~3 min)

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

Three things to check in the SQL it wrote:

- Did it exclude refunded donations? Does that match what you agreed on Monday?
- What did it do about supporters who appear twice?
- Did it compare lifetime totals without accounting for **how long** each group
  has been on the database? Someone who joined in 2016 has had longer to give.

If it did not handle those, that is not a failure of the tool. It is the part
that was always yours.

## A3. Attack your own result (~8 min)

> Now control for time on the database — compare average giving per year since
> sign-up rather than lifetime total. Does the conclusion hold?

> Is the difference driven by a small number of large gifts? Show me the
> distribution, not the mean.

> Do the duplicate supporter records affect this result? Quantify it.

At least one of these should change your picture. If none of them does, you have
a robust finding — which is worth knowing with confidence rather than assuming.

## A4. The sentence (~3 min)

> Write two sentences I could say in a meeting: what we found, and what it does
> not tell us.

The second sentence is the one that makes it defensible.

---

# Hypothesis B — operational

> **"Complaints take longer to resolve than other task types, and it is getting
> worse."**

Same shape, using `data/fulfilment_tasks.csv`.

## B1. Say what would change your mind (~3 min)

Then:

> Test this against `data/fulfilment_tasks.csv`: complaints take longer to
> resolve than other task types, and resolution time is getting worse over time.
> Write the SQL, run it, show me both.
>
> Before the answer: what in this data could make this result misleading?

## B2. The specific traps in this table (~5 min)

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

> Is the trend real, or is it an artefact of recent tasks not having been
> completed yet? Show me how you would tell the difference.

That is survivorship bias, and it is the single most common way an operational
"it's getting worse / better" finding turns out to be nothing.

## B4. The sentence (~3 min)

Same as A4: what we found, and what it does not tell us.

---

## Confirm ready

Tell us when you can show:

1. Your hypothesis, and the thing you said in advance would change your mind
2. One check that changed your answer
3. The two sentences

---

## If it goes wrong

**It answers before you finish asking.** Long prompts get partial answers. Break
it into steps; the exercise is written as steps for that reason.

**The answer is confident and you cannot see the query.** Ask for it. Every
time. An answer without a query is not checkable, and unchecked is unusable.

**It refuses to give a number and hedges instead.** Usually means the question
was ambiguous. Say what you meant more precisely — which is itself the lesson.
