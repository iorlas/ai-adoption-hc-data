# Answers — 5 · Build a report, then prove it is right

**FACILITATOR ONLY. Never on screen.** Everything you present is in
`README.md` — read that with the room. This page is what you cannot show them.

Clock and ownership: `session-3/facilitator/run-sheet.md`.

The longest run of either day, and it carries both leads' stated asks.
**Part B is protected** — it is Lucie's entire ask. Part A is the half that gets
cut.

## Running it

The demo sits **inside** each part, not in front of the whole segment.
Fifty-five minutes is too long to front-load, and Part B needs its own short
demo — the copy-out/paste-back loop has to be shown, not described.

**Call the time at 2:15 regardless of where Part A got to.** Not negotiable —
Part B is the reason the segment exists.

### Before you say anything about `.pbix`, square it with July

Thirty seconds, and it matters. PBIX-vs-PBIP was recorded as *the hinge
everything else on Day 1 hung from*, and it went unchallenged. A participant who
understood July correctly walks in believing their dashboards are editable text.
If we say "Claude cannot read your `.pbix`" and stop there, it reads as July
having been oversold. The four beats, in order, are written out in `README.md` —
say them in that order.

### Part A

You build the model and two measures live in Desktop. **This is the segment that
most needs rehearsal** — a live Power BI stall in front of this room is
expensive.

Show the loop physically: copy the measure out of Desktop, paste into Claude,
read the answer, paste back. Unglamorous on purpose. Say so.

### Part B

Demo B1 and B2, then let them run. The moment worth engineering the room
towards is **click-through rate** — clicks over opens, or clicks over sends. Two
different numbers with the same name, arriving spontaneously in a measure nobody
planned. It is the whole theme of the day showing up uninvited.

### The game — replaces share-back

Five situations, someone holding two numbers, and the question is not *what did
you find* but **what do you say to them?**

Card 2 is the one to slow down on: never say *"it's a data issue"* about the
615-supporter gap. It is a definition issue, and calling it data sends someone
off to fix something that is not broken.

### Do not demonstrate anything by recolouring charts

Locked custom branding; that demo was never about their work.

## Gate — three things

1. A working report with at least four measures
2. **One disagreement with an existing report, plus the sentence they would say
   to a stakeholder about it**
3. **One assumption Claude made that they rejected**

Number 2 is the deliverable of the segment. A number without the sentence is
half the exercise.

## Answer key

### What the model should look like

`campaigns` (dim) 1→* `donations` (fact); `supporters` (dim) 1→* `donations`;
`campaign_activity` joins to **both** `campaigns` and `supporters` — a second
fact table, not a bridge. A generated `Date` table.

Watch for Claude proposing bidirectional filtering to "make it work". Ask what
that does to the supporter count.

### Disagreements they should surface

1. **Income differs from Fundraising Summary by ~£17,000** if they excluded
   refunds and it did not.
2. **Distinct supporters ≠ Supporter Engagement's count** if they did not handle
   the 30 orphan `supporter_id`s or the 22 duplicate people.
3. **Click-through rate** — the dataset makes this vivid: 77 rows have
   `clicked = 1` with `opened = 0`, so clicks-over-opens can exceed 100%.

### Assumptions Claude typically makes unasked

- Filters refunds, or does not — either way silently
- Treats blank region as a category rather than missing
- Picks `DISTINCTCOUNT` over `COUNTROWS`
- Picks a date grain
- Casts `marketing_consent` and silently drops the 15 `'Y'`/`'N'` rows

Any of these is a good answer to gate item 3.

## What goes wrong

**DAX errors on paste.** Have them paste the error straight back rather than
retyping by hand. Usually a guessed column name. The loop is the lesson.

**Relationships will not create.** Duplicate values on the one-side — a
data-quality problem from segment 2 arriving in a new costume. Let them ask
*"why can I not make this one-to-many?"* and find the duplicates themselves.

**Power BI stalls on the demo machine.** Fall back to the pre-built `.pbix` and
the measures already written in `reports/`. Keep talking; do not debug on
screen.

**Someone has no Power BI Desktop.** Pair. The person without it writes every
prompt.

**Part A runs long.** Call it at 2:15 anyway.
