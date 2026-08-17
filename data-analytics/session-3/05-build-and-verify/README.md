# 5 — Build a report, then prove it is right

**55 minutes, hands-on · Claude Code + Power BI Desktop — DAX, Power Query M,
your normal `.pbix`**
*Part A 25 · Part B 25 · 5 min the game. Our demo is inside each part, not
before it — this segment is too long to front-load.*

> **Who does what:** **▸ We run it first, then you** — watch, then repeat it ·
> **▸ Your turn** — you drive, we are on the floor · **▸ Together** — whole room,
> out loud. Nothing here is a test.

One continuous piece of work. Build first, then interrogate what you built.

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

Not in conflict — one segment: **if it builds, teach me how to know it is
right.** A first pass you cannot defend is worth nothing.

## Two things we will not do

- **Not pitched on speed.** No clients, no short deadlines, and you want to work
  thoughtfully. "It's faster" means nothing to you.
- **No recolouring charts.** Your branding is locked, so the time goes on
  something that touches your actual work.

Where it does earn its keep: when a dataset is wide enough that nobody holds it
all in their head, and the boring part is writing the twelfth measure correctly.

## PBIX and PBIP, in one place

**PBIP is a real format and genuinely text.** Everything demonstrated on it in
July stands.

**You are on `.pbix` today, and we are not asking you to migrate.** PBIP costs
source control, process and habits — a door, not a requirement.

**So the loop that works on Monday morning is copy out, ask, paste back.**

## The boundary, precisely

**Claude cannot open a `.pbix`.** It is a binary — a zip of compressed model
data. The layer underneath is all available:

| Claude does this | You do this |
|---|---|
| Writes the Power Query M | Pastes it into the Advanced Editor |
| Writes the DAX measures | Pastes them in, checks them |
| Proposes the model — tables, relationships, direction | Builds it |
| Says which visual answers the question, and why | Places the chart |
| Reads a measure you paste back and tells you what it actually computes | Decides whether that is what you wanted |

Knowing what to hand it is part of the skill.

---

# The exercise

**Build a campaign performance report, then prove it.**

Which campaigns brought in money, from how many supporters, and how the email
campaigns performed. Neither report in `reports/` covers it.

Keep Power BI Desktop and Claude side by side — moving text between them is the
working pattern, not a workaround.

---

# Part A — Build (about 25 minutes)

## A1. Ask for the model, not the report (~6 min)

**▸ We run it first, then you.**

**Scene — set this up before you prompt anything.** Two windows, side by side.

- **Left: Power BI Desktop**, with the five tables from `data/` already loaded in
  the break — `supporters`, `campaigns`, `donations`, `campaign_activity`,
  `fulfilment_tasks`. No relationships, no measures yet. If yours is empty, the
  three-minute load is in
  [`01-prompt-refresher/setup.md`](../01-prompt-refresher/setup.md); do it now,
  do not wait. If something misbehaves,
  [`quirks.md`](../../quirks.md) has the fix.
- **Right: Claude Code**, in the `data-analytics` folder, **same conversation as
  part 4** — it must still be holding the definitions you just wrote into
  `CLAUDE.md`.

**Nothing moves between the two windows on its own.** You copy DAX out of Claude
and paste it into Desktop by hand, and back again. That is the whole working
pattern for the next hour.

> I want to build a campaign performance report in Power BI from the five CSVs
> in `data/`. Propose the model first: which tables, which relationships and in
> which direction, which columns I do not need, and where I will need a date
> table. Use the definitions in `CLAUDE.md`. Explain the reasoning, do not just
> give me a diagram.

Read the answer before you build any of it. Three checks:

- Is `campaigns` the dimension and `donations` the fact? If the relationship
  points the other way, ask why.
- Has it noticed `campaign_activity` joins to campaigns *and* to supporters, and
  said what that does to your filters?
- Has it silently dropped a table you will need?

Build the model in Desktop. Arguing with it is usually where the learning is. If
it proposes bidirectional filtering to "make it work", ask what that does to the
supporter count first.

## A2. The measures (~10 min)

**▸ We run it first, then you.**

**Scene.** Desktop on the **Model** view with the relationships from A1 in place,
and a **Date table** created — otherwise the time-based measures have nothing to
sit on. Create it in Desktop with **Modeling → New table**:

```dax
Date = CALENDAR(DATE(2016, 1, 1), DATE(2026, 8, 17))
```

Then mark it as a date table and join `Date[Date]` to `donations[donation_date]`.
Each measure below goes in via **Modeling → New measure**, one at a time.

> Write the DAX for: total income by campaign, number of distinct supporters who
> gave to each campaign, average gift, email open rate, and click-through rate.
> Use the Active Supporters definition from `CLAUDE.md` where it applies. Give
> me each measure with a one-line comment saying exactly what it counts and what
> it excludes.

Paste them one at a time. **Read each one first.** Two things to catch:

- Does the income measure exclude refunds? Which did you agree it should?
- Is click-through rate clicks over *opens*, or over *sends*? Different numbers
  with the same name — the whole theme of today.

## A3. The visuals (~9 min)

**▸ Your turn.**

> For each of these measures, tell me which visual answers the question best and
> why. If a table is the right answer, say so rather than proposing a chart.

Then place them yourself — Claude does not do this part, and it takes about four
minutes.

One more:

> What question does this report not answer that someone will ask in the first
> meeting?

**We call time at 25 minutes whatever state the report is in.** A half-finished
report you can interrogate teaches more than a finished one you cannot.

---

# Part B — Prove it (about 25 minutes)

A first pass you cannot defend is worth nothing. Now break it.

## B1. Check it against your own definition (~6 min)

**▸ We run it first, then you.**

**Scene.** In Desktop, open the **Model** view, click each measure you created,
and copy the formula out of the formula bar. Paste the lot into Claude in one
message. **Your measures, not the ones it gave you** — they have drifted, and the
drift is the point.

> Here are the measures as they now exist in my report. Check each one against
> the definitions in `CLAUDE.md`. Where does it not match? Where did you make an
> assumption I did not ask for?

The copy-out-ask-paste-back loop — the single most useful habit from today.

## B2. Cross-check against the reports that already exist (~12 min)

**▸ Your turn.**

The check you described as the last thing before anything goes live:

> "Go and hunt around in the service for every other dashboard that might have a
> similar measure and make sure that your number is reporting the same one… if
> you could drop 2 dashboards in and say, are there any things that look the
> same that are reporting different numbers?"

**Scene.** Claude only — Desktop can sit idle for this one. The two files it will
read are `reports/fundraising-summary/measures.dax` and
`reports/supporter-engagement/measures.dax`, both already in the repo. **Open
them yourself first**, so you are checking Claude rather than trusting it.

> Compare my measures against `reports/fundraising-summary/measures.dax` and
> `reports/supporter-engagement/measures.dax`. List every measure that appears
> in more than one report under the same or a similar name, and say whether they
> compute the same thing. Where they differ, say which is right for which
> question — do not just pick one.

**What you should find.** Your income measure and Fundraising Summary's will
disagree by about **£17,000** if you excluded refunds and it did not. Your
supporter count and Supporter Engagement's may or may not agree, depending on
what you did with duplicates. **Explaining the differences is the deliverable.**

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

Expect a longer list than you are comfortable with. The assumptions were always
there; now you can accept or reject each on purpose.

## B4. Then the game

**▸ Together, out loud.** [`game.md`](game.md) — five stakeholders holding two
numbers each, and what you say to them.

The wrong answer available every time is *"let me go and check"*. You already
know.

Tell us when you can show:

1. A working report with at least four measures
2. One disagreement with an existing report, and the sentence you would say
   to a stakeholder about it
3. One assumption Claude made that you rejected

---

## What you leave with

A first-pass report you built and then verified — against the definition you
agreed before the break, and against the two reports that already exist. Plus a
pre-launch check you can repeat.

Number 2 is the real deliverable. **A number without the sentence is half the
exercise.**

---

## If it goes wrong

**The DAX errors on paste.** Paste the error message straight back — usually a
column name it guessed. Do not retype by hand; make it fix its own output.

**Relationships will not create.** Almost always duplicate values on the
one-side — part 2's data-quality problem in a new form. Ask: *"why can I not
make this a one-to-many relationship?"*

**You run out of time in Part A.** Part B is the half that matters. Stop
building at the 25-minute mark even if the report is unfinished.

**Someone has no Power BI Desktop.** Pair up. The person without Desktop writes
every prompt; the other types and pastes. Prompt-writing is the skill being
taught, so this is genuinely the better seat.
