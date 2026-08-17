# Session 4 run sheet — ADF, and a look at what's next

**FACILITATOR ONLY. Does not ship.** Tuesday 18 August 2026, 180 min.
**Denis 90 min · Mykola 80 min · 4 handoffs.** Blocks in `facilitator/run-order.md`.

This is the spine: the clock, the rules, and the cut order. **The detail for each
stage — what you do, what to say, how to assert, the answer key — is in that
stage's own `README.md`, and the keys are in its `answers.md`.**

## The one job

They must leave with **documentation they wrote for a pipeline nobody had ever
documented, containing weak spots they found themselves** — and the recognition
that the half-hour that produced it is now spent permanently, for everyone.

**Success signal:** every participant has `adf/PL_Supporter_Weekly_Load.md`
written, has corrected or deleted at least one `[inferred]` claim, and can name
one failure this pipeline would not tell anybody about.

## Who runs what

| Time | Min | Stage | **Owner** | On the floor | |
|---|---|---|---|---|---|
| 0:00 | 15 | `00-opening/` | **DENIS** | Mykola | |
| 0:15 | 25 | `01-adf-explain/` | **DENIS** | Mykola | **protected** |
| 0:40 | 30 | `02-adf-document/` | **MYKOLA** | Denis | **protected** |
| 1:10 | 20 | `03-adf-weak-spots/` | **MYKOLA** | Denis | |
| 1:30 | 10 | *break* | — | both | |
| 1:40 | 35 | `04-better-questions/` | **DENIS** | Mykola | |
| 2:15 | 30 | `05-ml-taster/` | **MYKOLA** | Denis | **cut first** |
| 2:45 | 15 | `06-close/` | **DENIS** | Mykola | **protected** |

**Denis 90 min · Mykola 80 min · 4 handoffs.** Longest block: 50 min.

## What the files are

| File | Who reads it | When |
|---|---|---|
| `README.md` | **both of you** | share your screen, read it with them, top to bottom. This is the stage |
| `answers.md` | **you only** | keys, gate answers, demo tricks. **Never on screen** |

**You and the room read the same page.** No separate script to drift out of step
with what they can see.

## Stage by stage — the one thing to know

Run each stage straight down its `README.md`. Read `answers.md` beforehand.

| Stage | Owner | Before you present, know this |
|---|---|---|
| `00-opening/` | **DENIS** | **Hand out `fallback/` quietly and individually** — nobody announces they missed Monday. Say Lucie's ADF line |
| `01-adf-explain/` | **DENIS** | The watermark question. **Let them get it** — do not answer it for them |
| `02-adf-document/` | **MYKOLA** | The `[inferred]` instruction must be visible on screen. Watch for invented business reasons |
| `03-adf-weak-spots/` | **MYKOLA** | **Call the rules handover out loud** — it is the payoff of the whole ADF block |
| *break* | both | |
| `04-better-questions/` | **DENIS** | **Stop the room on the reversal.** That is the segment |
| `05-ml-taster/` | **MYKOLA** | Watch only. Say twice nobody needs access. Recorded fallback ready |
| `06-close/` | **DENIS** | **MCP — decide what you are saying before you start**, not during |

## Two hard time calls

- **1:30** — start the break wherever stage 3 got to.
- **2:15** — hand to Mykola for the ML taster wherever stage 4 got to.

Neither is negotiable. The close is protected.

## Cut order, when behind

1. **ML taster 30 → 18 min.** Drop the leakage demonstration; keep "how would
   you know whether to believe it".
2. **Better questions 35 → 29 min.** Nobody chooses; everyone does hypothesis A
   as a guided group exercise. Saves 6.
3. **Weak spots 20 → 14 min**, group discussion off one screen — but **keep the
   rules handover**, which is the payoff.

**Explain and document are never cut.** They are 55 of the 180 minutes and they
are what the client said they wanted most: *"ADF is our biggest pain. Everyone
hates it."*

## Standing rules

- **Whole stages belong to one person.** Nothing is co-presented and nobody cuts
  in mid-block. Hold your addition for the handoff or the break — the room hears
  one voice at a time, and each of you gets a run long enough to build something.
  The one not presenting is **on the floor**: unblocking, reading over shoulders,
  silent. Blocks and handoffs: `facilitator/run-order.md`.

Monday's other rules all carry — including **continuity, not correction**: never
audit or apologise for July or for yesterday in the room. Everything that
changed is framed as *you asked, so we did*.

Plus two specific to today:

- **Do not let this become a pitch to move their work into Git.** When Mykola
  raised the Git/JSON-file route on the August call, Lucie said *"that sounds a
  little bit too complicated already, I'm a little bit lost"* and then drew the
  line: *"it's not that we want to bypass using ADF, it's that we want to make
  ourselves using ADF easier."* Say her line in the opening. If Git comes up,
  park it into the proposed Git session.
- **Hand out `fallback/` quietly and individually.** Anyone who missed Monday
  needs it for stages 3 and 4. Nobody should have to announce in front of both
  teams that they were not there.

## Pre-flight

- [ ] Monday's retro notes read, and anything you are changing named out loud in
      the opening
- [ ] Mykola: full dry run of stages 1–3 against `adf/`, using the actual
      prompts from the exercise files, confirming the five starred issues are
      findable
- [ ] Mykola: AutoML example built and rehearsed end to end, with the leakage
      column ready to add live, **and a recorded fallback**
- [ ] Both facilitators have read every stage's `README.md` and `answers.md`, and the full
      `adf-issue-catalogue.md`
- [ ] Decide what to say about **MCP** before the close, not during it. It was
      promised verbally at 44:12 on the August call and never raised with AN IT
- [ ] Fallback copies to hand, on paper or ready to send
- [ ] **Handoffs rehearsed** — 4 today. Agree the one sentence each of you says
      when passing over, so it does not sound improvised
- [ ] **Cut order agreed out loud**, so mid-session neither of you is deciding
      alone what to drop
- [ ] **Clone the published repo into an empty folder and check it there** — the
      master copy being right proves nothing about what the room gets

## Reference

`adf-issue-catalogue.md` — the complete list of everything planted in the
pipeline, for when someone finds something unexpected and you want to know
whether it was deliberate. All nineteen, with the five that matter marked.
