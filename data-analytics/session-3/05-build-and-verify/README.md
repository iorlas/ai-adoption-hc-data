# 5 — Build a report, then prove it is right

**55 minutes, hands-on · Claude Code + Power BI Desktop — DAX, Power Query M,
your normal `.pbix`**
*Part A 25 · Part B 25 · 5 min the game. Our demo is inside each part, not
before it — this segment is too long to front-load.*

> **Who does what:** **▸ We run it first, then you** — watch, then repeat it ·
> **▸ Your turn** — you drive, we are on the floor · **▸ Together** — whole room,
> out loud. Nothing here is a test.

One continuous piece of work, not two. Build first, then interrogate what you
built.

## Why both halves

Lauren, on the August call:

> "If we take the concept of being able to ease out either some of the query
> writing or some of the building of the dashboard, then I think that's where I
> see an AI tool like Claude being helpful."

Lucie, on the same call:

> "What I would want the training to focus on would be not necessarily how to
> get AI to make the dashboard, but what would we need to do to make sure it was
> all correct and accurate and appropriate? … I need to be able to stand up in
> front of my stakeholder and explain how it works and how the numbers are
> derived."

Those are not in conflict. They are one segment: **if it builds, teach me how to
know it is right.** A first pass you cannot defend is worth nothing.

## Two things we will not do

Both are things you told us, and both are worth saying back so you know we
heard them:

- **We will not pitch this on speed.** You do not have clients, you do not have
  short deadlines, and you want to do things thoughtfully and correctly. "It's
  faster" is not an argument that means anything to you.
- **We will not demonstrate anything by recolouring charts.** You have locked
  custom branding, so we will spend the time on something that touches your
  actual work instead.

Where this does earn its keep: when a dataset is wide enough that nobody can
hold it all in their head, and the boring part is not deciding what to show, it
is writing the twelfth measure correctly.

## First — squaring this with July

In July the hinge of the whole first day was **PBIX versus PBIP**: the idea that
a dashboard can be *text* you can read, edit and diff. It landed, it went
unchallenged, and everything else that day hung off it.

Then in Session 4 we say plainly that Claude cannot open your `.pbix`. Those two
things sound like a contradiction, so here is the honest version, in one place:

**July was right.** PBIP is a real format, it is genuinely text, and everything
demonstrated on it was real. Nothing about that has been withdrawn.

**You are on `.pbix` today, and we are not asking you to migrate.** Moving a
team's reporting to PBIP is a decision with real costs — source control,
process, everybody's habits — and it is not this workshop's decision to make.
It is a door, not a requirement, and it is still open whenever you want it.

**So the loop that works on Monday morning is copy out, ask, paste back.** Less
elegant than "point it at the project folder", and it is what actually works
with the files you have today. Everything in this segment is built for the
format you are actually on.

## The boundary, precisely

**Claude cannot open a `.pbix`.** It is a binary — a zip of compressed model
data. Pointing Claude at one gets you nothing.

What it *can* do is everything in the layer underneath:

| Claude does this | You do this |
|---|---|
| Writes the Power Query M | Pastes it into the Advanced Editor |
| Writes the DAX measures | Pastes them in, checks them |
| Proposes the model — tables, relationships, direction | Builds it |
| Says which visual answers the question, and why | Places the chart |
| Reads a measure you paste back and tells you what it actually computes | Decides whether that is what you wanted |

Knowing what to hand it is part of the skill, and it is part of this exercise.
The working loop is: **copy out, ask, paste back.** Unglamorous, and it is the
whole of what makes this useful on Power BI work.

---

# The exercise

**Build a campaign performance report, then prove it.**

You are building a **campaign performance** report: which campaigns brought in
money, from how many supporters, and how the email campaigns performed. It does
not exist yet, and neither of the two reports in `reports/` covers it.

Keep Power BI Desktop and Claude side by side. You will be moving text
between them constantly — that is the working pattern, not a workaround.

---

# Part A — Build (about 25 minutes)

## A1. Ask for the model, not the report (~6 min)

**▸ We run it first, then you.**

> I want to build a campaign performance report in Power BI from the five CSVs
> in `data/`. Propose the model first: which tables, which relationships and in
> which direction, which columns I do not need, and where I will need a date
> table. Use the definitions in `CLAUDE.md`. Explain the reasoning, do not just
> give me a diagram.

Read the answer properly before you build any of it. Three things to check:

- Has it made `campaigns` the dimension and `donations` the fact? If it has the
  relationship pointing the other way, ask why.
- Has it noticed that `campaign_activity` joins to campaigns *and* to
  supporters, and said what that does to your filters?
- Has it silently dropped a table you will need?

Build the model in Desktop. Ask about anything you do not agree with — arguing
with it is allowed and is usually where the learning is. If it proposes
bidirectional filtering to "make it work", ask what that does to the supporter
count before you accept it.

## A2. The measures (~10 min)

**▸ We run it first, then you.**

> Write the DAX for: total income by campaign, number of distinct supporters who
> gave to each campaign, average gift, email open rate, and click-through rate.
> Use the Active Supporters definition from `CLAUDE.md` where it applies. Give
> me each measure with a one-line comment saying exactly what it counts and what
> it excludes.

Paste them in one at a time. **Read each one before you paste it.** Two specific
things to catch, both of which Claude may get wrong and both of which matter:

- Does the income measure exclude refunds? Which did you agree it should?
- Is click-through rate clicks over *opens*, or clicks over *sends*? Those are
  different numbers with the same name — which is the whole theme of today.

## A3. The visuals (~9 min)

**▸ Your turn.**

> For each of these measures, tell me which visual answers the question best and
> why. If a table is the right answer, say so rather than proposing a chart.

Then place them yourself. This is the part Claude does not do, and it takes
about four minutes, which is worth noticing.

Ask it one more thing:

> What question does this report not answer that someone will ask in the first
> meeting?

**We call time at the 25-minute mark whatever state the report is in.** A
half-finished report you can interrogate teaches more than a finished one you
cannot.

---

# Part B — Prove it (about 25 minutes)

A first pass you cannot defend is worth nothing. Now break it.

## B1. Check it against your own definition (~6 min)

**▸ We run it first, then you.**

Copy your measures out of Desktop and paste them back:

> Here are the measures as they now exist in my report. Check each one against
> the definitions in `CLAUDE.md`. Where does it not match? Where did you make an
> assumption I did not ask for?

This is the copy-out-ask-paste-back loop, and it is the single most useful habit
from today.

## B2. Cross-check against the reports that already exist (~12 min)

**▸ Your turn.**

This is the check Lucie described as the last thing she does before anything
goes live:

> "Go and hunt around in the service for every other dashboard that might have a
> similar measure and make sure that your number is reporting the same one… if
> you could drop 2 dashboards in and say, are there any things that look the
> same that are reporting different numbers?"

So do exactly that:

> Compare my measures against `reports/fundraising-summary/measures.dax` and
> `reports/supporter-engagement/measures.dax`. List every measure that appears
> in more than one report under the same or a similar name, and say whether they
> compute the same thing. Where they differ, say which is right for which
> question — do not just pick one.

**What you should find.** Your income measure and Fundraising Summary's will
disagree by about **£17,000** if you excluded refunds and it did not. Your
supporter count and Supporter Engagement's may agree or may not, depending on
what you did with duplicates. Both differences are explainable. Explaining them
is the deliverable.

Then the harder question:

> For each disagreement, what would I say to a stakeholder who has both numbers
> in front of them?

Write the answer down. That sentence is the actual output of this exercise.

## B3. Where did it guess? (~5 min)

**▸ Your turn.**

> Go back through everything you produced in this session. List every place you
> made a decision I did not explicitly ask for — a filter, a default, a data
> type, a definition. For each one, say what you assumed and what the
> alternative was.

Expect a longer list than you are comfortable with. That is the point: the
assumptions were always there, and now they are visible and you can accept or
reject each one on purpose.

## B4. Then the game

**▸ Together, out loud.** [`game.md`](game.md) — five stakeholders holding two
numbers each, and what you say to them.

The wrong answer available every time is *"let me go and check"*. You already
know — that is what the previous fifty minutes were for.

Tell us when you can show:

1. A working report with at least four measures
2. One disagreement with an existing report, and the sentence you would say
   to a stakeholder about it
3. One assumption Claude made that you rejected

---

## What you leave with

A first-pass report you built, and then verified — against the definition you
agreed before the break, and against the two reports that already exist. Plus a
pre-launch check you can repeat.

Number 2 above is the real deliverable of the segment. A number without the
sentence is half the exercise.

---

## If it goes wrong

**The DAX errors on paste.** Paste the error message straight back — it is
usually a column name it guessed. Do not retype it by hand; make it fix its own
output, because that is the loop you want to be fluent in.

**Relationships will not create.** Almost always duplicate values on the
one-side, which is a data-quality problem from part 2 arriving in a new form.
Ask: *"why can I not make this a one-to-many relationship?"* and let it find the
duplicates.

**You run out of time in Part A.** Part B is the half that matters. Stop
building at the 25-minute mark even if the report is unfinished — a
half-finished report you can interrogate teaches more than a finished one you
cannot.

**Someone has no Power BI Desktop.** Pair up. The person without Desktop writes
every prompt; the person with it only types and pastes. Prompt-writing is the
skill being taught, so this is genuinely the better seat, not a consolation.
