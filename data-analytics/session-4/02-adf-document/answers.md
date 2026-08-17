# Answers — 2 · Document it

**FACILITATOR ONLY. Never on screen.** Everything you present is in
`README.md` — read that with the room. This page is what you cannot show them.

Clock and ownership: `session-4/facilitator/run-sheet.md`.

**PROTECTED.** Parts 1 and 2 are what the client said they wanted most.

## The three things you have to make sure happen

**The `[inferred]` instruction actually gets used.** Without it, Claude states
guesses as fact and the exercise teaches the wrong lesson — namely that AI can
document your pipelines for you.

**The new-conversation test at step 4 actually gets run.** That is the payoff of
the segment: fresh conversation, ask *"what does the weekly supporter load do
about supporters in Northern Ireland?"*, and get an immediate correct answer
without Claude re-reading five JSON files.

**Name the link to yesterday out loud when it lands.** This is the same
mechanism as Monday's `CLAUDE.md`, applied to a pipeline instead of a measure.
Saying that is what makes four sessions feel like one thing rather than four.

**Walk the room during the write-up** and read over shoulders for invented
business reasons. If you find one, stop the room and show it — it is a live
example of the thing this whole workshop is about, and it will not come around
again on cue.

## Gate — three things

1. `adf/PL_Supporter_Weekly_Load.md` written
2. **At least one `[inferred]` claim they corrected or deleted** — not just
   marked
3. The new-conversation test working

Item 2 is the graded one. Anyone whose document has no corrections either got a
perfect draft (unlikely) or did not read it (likely).

## Answer key — what a good document contains

Beyond the structure in the prompt, the things that separate a useful document
from a fluent one:

**The hardcoded-decisions section must include the Northern Ireland exclusion.**
If it does not, the document is hiding the single most consequential line in the
pipeline, and it is worse than no document because the next person will trust
it.

**It must mention that one dependency is not on `Succeeded`.**

**The failure section must say what to actually do**, not "check the logs".

**"Reason not recorded" should appear at least twice.** The `Wait1` workaround
and the regional exclusion both have reasons that are genuinely not in the
files.

### The five questions people ask, for step 3
Start them with the two real ones — *why is this supporter missing?* and *why
does this number not match the other report?* Both have answers in the pipeline,
and both are questions this team actually gets.

## What goes wrong

**It writes 4,000 words.** Ask for it shorter and say who for: *"rewrite this
for someone who has fifteen minutes and is on call tonight."* Long documentation
does not get read at 3am, which is the only time it matters.

**Everything is marked `[inferred]`.** Over-corrected. *"Only mark things you
could not read directly from the files."*

**It invents a business reason.** The failure mode to hope for, honestly. Point
at it, name it, fix the prompt in front of everyone.

**The new-conversation test is skipped for time.** Cut step 3 instead. Step 4 is
the segment's ending.
