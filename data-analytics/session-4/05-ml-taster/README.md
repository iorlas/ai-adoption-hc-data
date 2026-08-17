# 5 — A first look at machine learning

**30 minutes, watch only · Databricks AutoML**

**Nobody needs access.** We run this on our own Databricks while you watch.
Our workspace is not yours — different catalogs, names and permissions — so
there is nothing to follow along in. Nothing is required from your team for this.

Deliberately **one** example rather than five — Lauren asked for *"a view of the
art of the possible"*, not a tour. Lucie asked for *"some very high level intro
for how we could use it to do a similar very simple ML."*

## The example

The example: **which supporters are most likely to give again in the
next six months.** Built on the same shared dataset you have used all week, so
you can see exactly which columns went in.

## The three things this half hour is about

### 1. What the data has to look like

More than half of any real machine-learning project is this, and demos skip it.

You need one row per supporter, one column per thing you know about them, and one
column that is the answer you are trying to predict — known historically for the
rows you train on. Getting to that table from five CSVs is the work.

Watch for **leakage**: if an input column quietly contains the answer, the model
looks brilliant and is worthless. We put one in on purpose.

### 2. What the tool actually does for you

AutoML tries a range of model types, tunes them, and hands you the best one plus
the notebook that produced it.

> AutoML removes the part that used to need a specialist. It does not remove
> deciding what to predict, assembling the table, knowing whether the answer is
> any good, or deciding what to do about it.

### 3. How you would know whether to believe it

- **Accuracy is usually a misleading number.** If 5% of supporters give again, a
  model that says "nobody will" is 95% accurate and useless.
- **What you actually want to know:** of the people it flags, how many really do
  give? Of the people who do give, how many did it find? Where you sit on that
  trade-off is a business decision.
- **A model trained on the past assumes the future resembles it.** After a change
  in strategy, it quietly stops being right.
- **Test it on data it has never seen.** A model evaluated on its own training
  data always looks good.

## What we are not going to say

Not AI magic, and not a replacement for a judgement your team currently makes.

One distinction that gets blurred everywhere:

> This is a trained statistical model. That is a different thing from the
> language model in Claude. Both get called AI, they fail in completely
> different ways, and they are trustworthy under completely different
> conditions. Knowing which one you are looking at is genuinely useful to walk
> away with.

## This is a taster

Doing it properly — your data, your question, your validation, and whether to act
on it — is a separate session. If you want it, say so in the close.

## Nothing to run

Watch, interrupt, ask. The most useful question here is *"how would we know if
that were wrong?"* — at any point.

And the one we will ask you at the end:

> **"If I showed you this model's output next month, what would you ask me
> before acting on it?"**
