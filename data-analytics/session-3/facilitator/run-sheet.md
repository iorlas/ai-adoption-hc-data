# Session 3 run sheet — Numbers you can defend

**FACILITATOR ONLY.** Read this, then read your own stages' `README.md` and `answers.md`.
If you are presenting a stage, you own it end to end — the other person is on
the floor, silent, helping whoever is stuck.

## The one job

They must leave having **found two live reports disagreeing about a headline
number, resolved it themselves, written the resolution somewhere both their team
and Claude will read it, and then built and verified a report against it.**

Everything else is scaffolding for that.

**Success signal, measured live:** every participant can show (a) a
`docs/data-quality-rules.md` with a rule they *rejected*, (b) a Definitions
section in `CLAUDE.md` that is a pointer rather than the content, (c) a
before/after answer pair, and (d) one disagreement between their new report and
an existing one, with the sentence they would say about it.

## Who runs what

| Time | Min | Stage | **Owner** | On the floor |
|---|---|---|---|---|
| 0:00 | 5 | `00-opening/` | **DENIS** | Mykola |
| 0:05 | 17 | `01-prompt-refresher/` | **DENIS** | Mykola |
| 0:22 | 30 | `02-data-quality/` | **DENIS** | Mykola |
| 0:52 | 8 | `03-genie-vs-claude-code/` | **MYKOLA** | Denis |
| 1:00 | 10 | *break* | — | **both** — Power BI loads |
| 1:10 | 40 | `04-shared-definitions/` | **MYKOLA** | Denis |
| 1:50 | 55 | `05-build-and-verify/` | **MYKOLA** | Denis |
| 2:45 | 15 | `06-close/` | **DENIS** | Mykola |

**Denis 70 min · Mykola 100 min · 3 handoffs.**

---

## What the files are

| File | Who reads it | When |
|---|---|---|
| `README.md` | **both of you** | share your screen, read it with them, top to bottom. This is the stage |
| `game.md` | you read the cards out | the call-and-response beat |
| `answers.md` | **you only** | keys, gate answers, demo tricks. **Never on screen** |

**You and the room read the same page.** That is the design — no separate
facilitator script to drift out of step with what they can see.

## Stage by stage — the one thing to know

Run each stage straight down its `README.md`. Read `answers.md` beforehand.

| Stage | Owner | Before you present, know this |
|---|---|---|
| `00-opening/` | **DENIS** | No tools. Straight through |
| `01-prompt-refresher/` | **DENIS** | **Paste the clone commands into the meeting chat** — they are in `answers.md`. Then `setup.md` on screen for 6 min |
| `02-data-quality/` | **DENIS** | **The demo has a deliberate mistake. Do not skip it** — ask for a summary first, accept "four statuses", then ask properly. `answers.md` |
| `03-genie…/` | **MYKOLA** | Our Databricks. Say twice nobody needs access. **Read the Power BI break line before anyone stands up** |
| *break* | both | Mykola takes Power BI, Denis takes anything still broken |
| `04-shared-definitions/` | **MYKOLA** | Both numbers on screen: **2,447 and 1,832**. The 8-min room decision is chairing an argument, not demoing |
| `05-build-and-verify/` | **MYKOLA** | **Call time on Part A at 2:15 whatever happens** |
| `06-close/` | **DENIS** | Retro, write answers down. Point at `take-home.md`, do not read it out |

## If you are running late

Cut in this order, stop as soon as you are back on time:

1. **A game** — stage 1, 2, 4 or 5. 5 min each. Losing one costs nothing
2. **Stage 2 step 3** — do it as a group off one screen. Saves ~6 min
3. **Close backlog talk** — keep the retro, drop the rest. Saves 5 min

**Never cut:** setup, Genie, the room decision in stage 4, Part B of stage 5,
the retro.

## Two hard time calls

- **1:00** — start the break on time, and say the Power BI line *before* anyone
  stands up
- **2:15** — end Part A of stage 5 wherever it got to. Not negotiable

---

## Standing rules

- **Whole stages belong to one person.** Nothing is co-presented and nobody cuts
  in mid-block. Hold your addition for the handoff or the break — the room hears
  one voice at a time, and each of you gets a run long enough to build something.
  The one not presenting is **on the floor**: unblocking, reading over shoulders,
  silent. Blocks and handoffs: `facilitator/run-order.md`.
- **Demo → they repeat → they confirm ready → continue.** The confirm step is
  not rhetorical. Every stage file names the exact artifact and question to ask.
  Never "everyone ok?" Grounded in Lucie's July feedback that people got lost and
  could not pick back up.
- **Never pitch on speed.** They have no clients and no short deadlines, and
  they said so twice. Pitch on *defensibility*.
- **Continuity, not correction.** Never audit or apologise for July in the room
  — not the tooling, not the notation, not the pacing. We ran it; disowning it
  puts a shadow over today and invites *"so why is this right?"* Everything that
  changed is framed as **you asked, so we did**.
- **No recolouring demos.** Locked custom branding.
- **Plain English prompts**, and **no commentary on how they were written in
  July.** Just write them plainly. If asked directly, one light sentence — the
  wording is in stage 1's facilitator note.
- **One tool.** Claude. No second vendor on screen at any point.
- **Blocked tool = pair, and the blocked person writes every prompt.** The
  driver only types. Prompt-writing is the skill, so this is honest, not
  consolation.
- **Both teams present throughout.** No divergent blocks in either session.
- **Mykola: watch the pace.** Several of his interventions on the August call
  lost Lucie in the moment ("too complicated", "I'm a little bit lost"). Narrate
  before you do, and stop on the first lost face.
- **Weight floor support toward Lauren's team** — the July literacy friction was
  concentrated there, not spread evenly. Lucie was the strongest performer in
  the room.

## Pre-flight, the Friday before

- [x] **Prerequisites + Windows setup sheet sent; both teams confirmed** they
      would have everything installed by Monday. So assume Claude, Python, `uv`,
      Git and VS Code are present.
- [ ] **The repo and dataset were never sent, and are not being sent.** Setup is
      the first six minutes of stage 1. **Have the two commands ready to paste
      into the meeting chat** — they are in `01-prompt-refresher/answers.md`
- [ ] **A memory stick with the folder on it**, for whoever's proxy blocks the
      clone. This is the single likeliest way to lose someone this morning
- [ ] Nobody can have preloaded Power BI — the dataset they agreed to load never
      reached them. **The load moves to the break**; say so in the first minute
- [ ] `uv run verify.py` green from at least one person on each team
- [ ] Mykola: full dry run of stages 03, 04 and 05 on Windows, timed — the three he owns
- [ ] **Denis: both windows open on your own machine** for stage 1 — terminal
      and desktop app, same folder. No screen-share swap; you show both yourself
- [ ] **Handoffs rehearsed** — 3 on Monday, 4 on Tuesday. Agree the one sentence each of you
      says when passing over, so it does not sound improvised
- [ ] Mykola: Databricks live, Genie space configured, comparison prompt
      rehearsed **and recorded as a fallback**
- [ ] Both `.pbix` built and checked — `facilitator/build-the-two-pbix.md`
- [ ] Both facilitators have read every stage's `README.md` and `answers.md`
- [ ] **Cut order agreed out loud**, so mid-session neither of you is deciding
      alone what to drop
