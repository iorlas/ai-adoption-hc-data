# Curriculum design record — Analytics Sessions 3 & 4

**FACILITATOR ONLY.** Written 2026-08-14, after the v2.2 client pack was agreed
and both leads confirmed they will have prerequisites ready before Monday.

This is the design the materials are built from: what the room already knows,
what each section produces and consumes, what is reused from July, and what had
to be built new. Read this before changing anything in the repository — most of
the numbers and several of the segments are load-bearing for each other.

---

# A. Audience model — what is actually true about this room

Sourced from the July Day 1/2 recordings (`an-analytics-topics-covered.md`), the
August pre-call form, and the recovered 2026-08-06 Teams transcript. Not
inferred.

## A1. What they were taught in July and demonstrably absorbed

| Landed | Evidence | Design consequence |
|---|---|---|
| **Anatomy of a prompt** — request / target / location / actions | Lucie played it back accurately in her own words, D1 39:48 | **Shared vocabulary. Reuse it** rather than teaching prompt structure again |
| **Tightening a prompt, call-and-response** | Declan, Lucie and Sarah each supplied a missing element, D1 59:12–1:28:51 | **The single best-performing format of the two days.** Build one call-and-response beat into each session |
| **PBIX vs PBIP** — a dashboard as text you can diff | "the hinge everything else on Day 1 hung from", unchallenged | **Must be reconciled, not contradicted.** See D4 |
| **Recolouring a dashboard from a prompt** | Lucie reproduced it unprompted mid-session — the only exercise anyone completed unasked | Do not repeat it (branding), but it proves they *can* follow and reproduce |
| **Secrets in environment variables** | New to everyone; came back as Declan's closing question | Not needed in S3/S4 — no tokens anywhere |
| **Genie as an API, not a chat window** | Declan's question was the most technically engaged exchange of two days | stage 03 can assume Genie is a known word |

## A2. What did not land, and must not be repeated as-is

| Did not land | Evidence | Design consequence |
|---|---|---|
| **XML tags around the prompt parts** (`<request>`, `<target>`, …) | Sarah stopped the session: *"you were using brackets and specific commands, none of which I recognise"* | **Every prompt in these materials is plain English.** Retired explicitly in stage 02 — and framed as *right technique, wrong length*, not as an error, because it is a documented technique and someone will check |
| **Two tools in parallel** (Codex + Claude) | Sarah had to ask what Codex was; AN has no ChatGPT licences | **One tool only.** Claude, named consistently |
| **Unit tests / data tests as the answer to hallucination** | Zero questions across ~5 hours | Verification must be re-pitched as *"the one cheap question a wrong answer can't survive"*, never as testing |
| **Reflection / critic patterns, routers, sub-agents, RAG, semantic models, local models** | Zero engagement | Absent from S3/S4 entirely |

## A3. What they asked for, unresolved

| Ask | Who | Where it is answered |
|---|---|---|
| *"Are we watching, or doing?"* | Lauren D1 23:53, Sarah D1 1:13:47 | Every hands-on segment; the demo→repeat→confirm gate |
| *"Is there something written down?"* — asked twice, insistently; **read-and-do, not watch-and-do** | Sarah, D2 1:12:55 and 1:13:35 | **This entire repository is the answer.** Every exercise must be followable alone, without the facilitator |
| *"Where does this help the work we actually do?"* — recorded as **still unanswered in their terms** | Lucie, D1 2:27:06 | Every section README opens with the client's own words for the problem it solves |
| ADF is the biggest pain | Lucie, Aug 35:01 | 75 of Session 4's 180 minutes |
| Validate / cross-check across files for Power BI | Lucie, Aug 35:01 | stage 05 Part B |
| Not how to make the dashboard, but how to know it is right | Lucie, Aug 18:37 | stage 05 is one build-and-verify arc, not two segments |
| Shared MD files so everyone uses the same SQL | Lucie, Aug | stage 04 |
| Same definition across dashboards | Lauren, Aug | stage 04 |
| Avoid Python | Lucie, Aug 21:32 | No Python content; SQL throughout; Python is plumbing only |
| Same data for everyone, so outputs can be compared | Lucie, Aug 9:59 | `data/`, and `verify.py` proves it |

## A4. Skill floor

Uneven, and the friction was **concentrated on Lauren's team** (Sarah
specifically), not spread evenly. Lucie was the strongest performer in the room.
Floor support weights toward Lauren's team; the pacing gate exists for Sarah.

**Nobody has been taught the Claude desktop app.** July ran on the CLI and on
Codex. The prerequisites now ask for the desktop app. This is a real gap and
D3 below closes it.

---

# B. Design rules

Derived from section A. Every file in this repository is checked against these.

1. **Plain English prompts only.** No XML, no notation, no jargon that was not
   already landed in July.
2. **One tool.** Claude. Never a comparison of vendors.
3. **Written down, self-servable.** Every exercise is followable by a person who
   missed the demo. This is Sarah's ask and it is non-negotiable.
4. **Their words first.** Each section README opens with the client's own
   sentence describing the problem. This is the answer to Lucie's unresolved
   *"where does this help the work we actually do?"*
5. **Never pitch on speed.** They have no clients and no short deadlines.
   Pitch on **defensibility**.
6. **No recolouring.** Locked custom branding.
7. **Verification is "the one cheap question", never "testing".**
8. **One call-and-response beat per session**, because it outperformed every
   other format in July.
9. **Reuse July's vocabulary** — request / target / location / actions;
   `CLAUDE.md` as the agent's entry point; Genie. All three already landed.
10. **Every stated number is verified against the generated data**, not
    estimated. The room is being taught to check numbers; ours must survive it.
11. **Continuity, not correction.** ★ Never audit, disown or apologise for July
    in anything the room reads or hears. See B-note below — this one was got
    wrong twice and is the easiest to reintroduce by accident.

## B-note — on rule 11, because it was got wrong twice

The audience model in section A is built almost entirely on what did and did not
work in July. That makes it very easy to write materials that *narrate* those
findings back to the room — "the notation cost attention", "the speed pitch did
not land", "two tools was a mistake".

**Every one of those is a private design input, not a public line.** Said out
loud, they do three things, all bad:

1. **They shadow us.** We are the same two facilitators who ran July. If July
   was wrong, the fair question is why today is right — and we have handed it
   over for free.
2. **They re-stage someone's objection.** The notation finding exists because
   one person stopped a session. Naming it again, in front of the same room,
   makes a public event of something that should stay a design note.
3. **They spend credit we need elsewhere.** The room's willingness to try things
   is finite; burning it on an apology for a tool choice is a poor trade.

**The test for any sentence about July:** does it *affirm* or *inform*? Affirm
is fine — "July was right, PBIP is real" in stage 06 is doing useful work, because
it protects a thing they learned. Inform is fine — "you asked for more doing and
less watching, so here is the readiness check". **Contrast is not** — anything
of the shape "unlike July" or "that did not work last time" comes out.

What replaces it: **you asked, so we did.** Same change, same reasoning, credit
to them instead of blame to us.

This was got wrong twice — first as *"it was never required, it was one person's
habit"*, then, after a correction, as *"a real technique, wrong length"* framed
as a retraction to be delivered out loud. Both still put July on trial. The
third version simply does not raise it, and gives a one-sentence answer if asked.

---

# C. The spine

## Session 3 — one job

> Two live reports disagree about a headline number. Resolve it, write the
> resolution where both your team and Claude will find it, then build something
> new against it and prove it.

The disagreement has **three separate causes**, deliberately, and each is owned
by a different segment:

| Cause | Size | Found in |
|---|---|---|
| A data-quality defect — the `Activ` typo | 18 people | stage 02 |
| A definitional difference — status vs behaviour | 615 people | stage 04 |
| An undocumented Power Query step — refunds excluded in one report only | £16,995 | stage 04 / stage 05 |

This is why the segments cannot be reordered or run standalone. No single
segment resolves the disagreement.

## Session 4 — one job

> An undocumented pipeline can silently produce wrong answers. Understand one,
> document it, and find where it lies — using the same habit as Monday: write
> down what you worked out, where the next person and the next conversation will
> find it.

The two sessions share a mechanism, not just a tool. Monday writes definitions
into `CLAUDE.md`; Tuesday writes pipeline knowledge next to the pipeline. Both
are the same move, and **saying that out loud is what makes four sessions feel
like one thing.**

---

# D. Reconciliations — where this design contradicts July

Three places. All three must be said out loud rather than quietly changed,
because the room remembers July and half of them will notice.

## D1. "Testing is the answer to hallucination" → "the one cheap question"

July taught unit tests and data tests as the mechanical defence. It drew **zero
questions**. These sessions teach the same idea as a habit rather than a
practice: ask the one question a wrong answer cannot survive — show me the
failing rows, which dataset, define the term.

Not a contradiction, a re-pitch. Do not name it as a correction.

## D2. Two tools → one tool

July demonstrated Codex and Claude to show the method is vendor-independent. It
cost more than it bought: AN has no ChatGPT licences, so half of what was on
screen was not reproducible. **Say once, in Session 3's opening, that everything
from here is Claude**, and do not mention other vendors again.

## D3. CLI → desktop app

July ran on the CLI. The prerequisites now ask for the desktop app. Nobody has
been shown it.

**Closes with:** `reference/desktop-or-terminal.md` to read beforehand, plus a
**12-minute stage of its own** — `session-3/01-prompt-refresher/`.

**Revised 2026-08-16, on the facilitator's challenge.** The first version made
this a 3-minute beat inside the opening and framed the reference page as *"use
the desktop app for these two sessions"*. Both were wrong:

- **3 minutes is not enough** for a tool nobody in the room has opened, when the
  first hands-on exercise starts immediately after it.
- **It was selling Desktop.** The true statement is that they are the same
  Claude Code and, for everything in these two days, **equal**. Anyone who got
  comfortable in the terminal in July should stay there. Pushing the app would
  repeat July's two-tools mistake in a new form.

The stage now runs a deliberately vague prompt, tightens it with the room
(call-and-response, reusing July's request/target/location/actions), and runs
the tightened version in **both** cockpits side by side. It doubles as the
month-gap warm-up and produces the first dataset profile, which stage 2 picks
up. Its readiness gate is the row count — 4,022 — which is also the earliest
possible check that everyone is on the same data.

**Cost:** Session 3 goes 2:55 → 3:00, matching Session 4, and Genie drops 15 →
10. Build-and-verify is untouched.

## D4. "A dashboard is text you can diff" → "Claude cannot open a `.pbix`" ★

**The one that matters.** PBIX-vs-PBIP was recorded as *the hinge everything
else on Day 1 hung from*, and it went unchallenged. Then the format decision was
made to **stay on `.pbix`, no migration**.

So a participant who understood July correctly will arrive on Monday believing
their dashboards are editable text, and stage 05 tells them Claude cannot read their
file. Left unreconciled, that reads as either July having been wrong or as the
tool having been oversold.

**The honest reconciliation, and it must appear in `05-build-and-verify/`:**

- July was right. PBIP *is* text, and everything demonstrated on it was real.
- You are on `.pbix` today, and we are not asking you to migrate — that is a
  decision with real cost and it is not this workshop's to make.
- So the working loop on `.pbix` is **copy out, ask, paste back**. It is less
  elegant and it is what actually works on Monday morning.
- PBIP remains the door to the fuller version. Naming it as a door rather than
  as a requirement is what keeps July honest.

---

# E. Artifact dependency graph

What each segment consumes and produces. **This is the reason the sessions
cannot be resequenced**, and it is where the two required fallbacks come from.

```
data/ ──────────────┬─────────────┬──────────────┬─────────────┐
                    │             │              │             │
reports/ ───────┐   │             │              │             │
                v   v             v              v             v
              stage 02            stage 04            stage 05          S4-4
           data quality   definitions     build+verify   better questions
                │               │  ^           ^  ^            ^
                │  the 'Activ'  │  │           │  │            │
                └──────────────>│  │           │  │            │
                                │  └───────────┘  │            │
                                │  CLAUDE.md      │            │
                                │  definitions ───┼────────────┘
                                v                 │
                    docs/decisions/0001    reports/ cross-check
                                │
   docs/data-quality-rules.md ──┼──────────────────────┐
                                v                      v
                              (stage 06 close)           S4-3
                                                  weak spots
adf/ ──────> S4-1 ──────> S4-2 ──────> S4-3
           explain      document     weak spots
                            │            ^
                            └── the doc ─┘
```

## Hard dependencies

| Consumer | Requires | If missing |
|---|---|---|
| stage 04 step 2 | The `Activ` finding from stage 02 | Segment still works; the fourth number is just handed to them |
| stage 05 Part A | `CLAUDE.md` definitions from stage 04 | **Breaks the segment's point** — there is nothing to verify against |
| stage 05 Part B | `reports/` + their own measures | Ships with the repo, safe |
| S4-3 step 3 | `docs/data-quality-rules.md` from stage 02 | The `iifNull` payoff lands weakly |
| S4-4 | `CLAUDE.md` definitions from stage 04 | Queries still run; the "use our definition" beat is lost |

## The two fallbacks this graph requires

1. **`session-4/fallback/`** — a ready-made `CLAUDE.md` definitions block and a
   completed `data-quality-rules.md`, for anyone who missed Monday, or whose
   file got mangled, or who joins Tuesday only. Without this, two of Tuesday's
   segments silently degrade for that person and nobody notices until they are
   stuck.
2. **Recorded Genie comparison** — stage 03 is the only segment depending on a live
   external system. It is also the first cut-line. A recording removes the
   dependency entirely.

## Dangling output — resolved

`docs/data-quality-rules.md` was produced in stage 02 and consumed nowhere. It is
now an explicit input to **S4-3**: the pipeline's `iifNull` defaults silently
repair exactly the defects those rules catch, so a clean quality report can be
produced by a pipeline that is lying. That closes the loop across the two days
and is the strongest single argument that data quality and pipelines are one
problem, not two.

---

# F. Reuse audit

Against `deliverables/workshop-repo/` (the Data Engineering stream's repo — the
Analytics room has never seen it) and the existing analytics deliverables.

| Asset | Source | Verdict | Why |
|---|---|---|---|
| Repo shape: numbered self-contained stage folders, `facilitator/` never ships | DE `day-2/` | **Adopt wholesale** | Proven; matches the request exactly |
| `verify.py` green-check before the session | DE `day-1/` | **Adopt** | It is what bought back the hour July's Day 2 lost |
| Deliberate-defects dataset + facilitator defect manifest | DE `day-1/` | **Adopt, rebuild** | Same idea, supporter-analytics shape, own generator |
| **Meaningful vs noise** DQ rules exercise | DE `day-2/05` | **Adapt** | The judgement half is the value; reshaped onto supporter data |
| **Where does knowledge live** — five homes sorting drill | DE `day-2/04` | **Adapt — gap G5** | Prevents the 400-line `CLAUDE.md` failure. stage 04 currently teaches "write it in `CLAUDE.md`" with no such caution |
| **Doc skeletons to fill** (data dictionary, glossary) + a **finished worked example in a different domain** | DE `day-2/04` + `templates/` | **Adapt — gap G4** | Directly de-risks the doc-from-a-blank-page stall in stage 02 and S4-2. A different domain shows shape without spoiling the answer |
| **ADR template + Y-statement** | DE `day-2/02` | **Adapt — gap G6** | The definitions decision *is* a decision with rejected alternatives. An ADR is also Lucie's *"explain how the numbers are derived"* in durable form |
| **Take-home: picture / task on own work / best-practices-after** | DE `day-2/07` | **Adapt — gap G7** | S3's practice ask has no file; S4 has no take-home at all |
| Three-surfaces orientation | DE `day-2/00` | **Adapt, inverted — gap G3** | The DE version concludes "learn the CLI". Analytics is now on the desktop app. Reuse the table, invert the recommendation |
| Five tells for a wrong answer | DE `day-2/01` | **Rebuild small — gap G1** | **Analytics never saw this.** Current text references "Tell #1 from July" — a false reference to material this room does not have |
| Prompt anatomy: request/target/location/actions | July **analytics** D1 | **Reuse the vocabulary — gap G8** | Already landed and played back. Free continuity |
| PBIX vs PBIP | July **analytics** D1 | **Reconcile — gap G2** | See D4 |
| Governance: code-not-rows, mask before commit, you can see what it read | DE `day-2` | **Adopt, one paragraph** | Already in stage 02; keep it light — this room is synthetic-only |
| MSSQL + DAB/MCP substrate | DE repo | **Reject** | ADR-superseding decision: file-based DuckDB via `uv`. Installing a DB server on managed charity laptops is the likeliest way to lose hour zero |
| Stored-procedure / cursor-optimisation content | DE `day-2/02–03` | **Reject** | Wrong audience; analysts do not maintain procs |
| `ai_classify` / classification segment | v1 analytics design | **Reject, retain the raw material** | Cut when the transcript reordered priorities. `campaigns.csv` keeps the messy categories and the answer key so it is available for a follow-up session and Lauren's take-home — see G9 |

---

# G. Gap list

Everything section F and the dependency graph exposed, in build order.

| # | Gap | Severity | Closed by |
|---|---|---|---|
| G1 | "Tell #1 from July" was a **false reference** — the analytics room never saw the five tells | **Bug** | `reference/checking-the-answer.md`, written for this room; both references corrected |
| G2 | PBIP reconciliation missing; silently contradicted July's hinge idea | **High** | New opening section in `session-3/05-build-and-verify/README.md`, a pointer in `reports/README.md`, a 30-second script in the run sheet |
| G3 | Nobody had been taught the desktop app, and hands-on starts at 0:10 | **High** | `reference/desktop-or-terminal.md` + **`session-3/01-prompt-refresher/`, a 12-minute stage** (revised 2026-08-16 — the first fix was a 3-minute beat that also read as a Desktop pitch; see D3) |
| G4 | Doc skeletons + a finished example in another domain | Medium | `docs/` skeletons with headings in place; `templates/example-library/` — a library service, so no spoilers |
| G5 | No progressive-disclosure caution — the room would put everything in `CLAUDE.md` | Medium | `reference/where-knowledge-lives.md`, run as **Session 3's call-and-response beat** |
| G6 | The definitions decision was not recorded as a decision | Medium | `docs/decisions/` + template + step 5c; two worked ADRs in the library example |
| G7 | No take-home files for either session | Medium | `session-3/06-close/take-home.md`, `session-4/06-close/take-home.md` |
| G8 | July's prompt vocabulary not reused | Low | `reference/prompt-patterns.md` — request/target/location/actions, minus the notation |
| G9 | `campaigns.csv` messy categories orphaned | Low | Documented in `facilitator/README.md`: kept for Lauren's take-home and a follow-up session, **not mentioned in the room** |
| G10 | No cross-session fallback for anyone who missed Monday | **High** | `session-4/fallback/` — both artifacts, handed out individually |
| G11 | Exercise step timings never checked against segment budgets | Medium | All seven audited and re-timed; four over-ran. Run sheets updated to match |
| G12 | `docs/data-quality-rules.md` consumed nowhere | Medium | Wired into `session-4/03-adf-weak-spots/` step 3 — the pipeline's defaults defeat the rules they wrote. Now **Session 4's call-and-response beat** |

All twelve closed 2026-08-14. Two turned out better as beats than as documents:
G5 and G12 both became call-and-response moments, which is the format this room
responded to best in July.

---

# I. File convention — one folder per stage

**Revised twice: 2026-08-16 morning (games), 2026-08-16 evening (role markers).**

| File | Who reads it | Contains |
|---|---|---|
| `README.md` | Everyone | **The material.** What this is, why it matters. Read it, or we narrate it |
| `exercise.md` | Everyone | **The single description of what happens**, step by step, each step marked with who drives |
| `game.md` | Everyone | **Optional.** Cards with reveals, called out loud. Only where it earns its place |
| `facilitator.md` | Us | **Only what cannot be shown**: the clock, deliberate mistakes, exact words, how to assert, the answer key, what goes wrong |

## The role markers

Each step in an `exercise.md` carries one:

| Marker | Means |
|---|---|
| **▸ We run it first, then you** | We demonstrate, then they repeat the same thing |
| **▸ Your turn** | They drive; we are on the floor |
| **▸ Together, out loud** | Whole room — games, and decisions that are not Claude's |
| **▸ Watch** | Nothing for them to run |

**Why this matters more than it looks.** Before the markers existed, the same
activity was described twice — once in `exercise.md` as "you drive", once in
`facilitator.md` as "we demo steps 1 and 2, then they repeat". Those two
descriptions had **already drifted apart** in `02-data-quality` before anyone
ran the session. Two documents for one activity will always drift; one document
with markers cannot.

## The rule that follows

**`facilitator.md` never re-describes the steps.** If it is telling you what
happens, it belongs in `exercise.md` with a marker. The facilitator note carries
only the layer that cannot be participant-visible:

- the clock and the beat split
- deliberate mistakes to make on screen
- the exact words for the two or three lines that must land
- how to assert, with the expected answer
- the answer key
- what goes wrong and what to do

## Games are not mandatory

**Revised from the morning's version, which made a game standard for every
teaching stage.** They are used where they earn their place — where there is a
judgement to rehearse that a "show me your file" check would not catch.

Session 3 has five because five of its stages turn on judgement calls. Session 4
has fewer: the ADF stages produce a document you can look at, which is a better
check than any card set, and the strongest game in either session — the
rules-versus-pipeline handover in weak-spots — is already there.

The test: **would a card set catch a misunderstanding that looking at their
artifact would miss?** If not, do not build one.

---

# I-bis. Superseded: the earlier three-file convention

**Revised 2026-08-16** on the facilitator's observation that the read → do →
capture loop had been built twice by instinct and should be the standard shape.

Every teaching stage of both sessions is a self-contained folder:

| File | Audience | Answers |
|---|---|---|
| `README.md` | Everyone | **Read it.** What this is, why it matters, what to tell them |
| `exercise.md` | Participants | **Do it.** The prompts, the expected numbers, how to tell it worked |
| `game.md` | Everyone | **Capture it.** 3–5 min, out loud, cards with reveals |
| `facilitator.md` | Us | The clock · what you do · what to say · how to assert · answer key · what goes wrong |

## Why a game rather than a check

Three reasons, in order of weight:

1. **It is the format this room responds to.** The single strongest twenty
   minutes of July was tightening a prompt call-and-response, with three
   different people supplying a piece unprompted. Nothing else in two days
   performed close to it.
2. **It assesses better than the old gate did.** "Show me your file and answer
   two questions" tells you who finished. A card someone calls wrong tells you
   *what they misunderstood*, immediately, while there is still time to fix it.
3. **It is time-neutral.** Every game replaces a share-back or confirm-ready
   slot that already existed. Nothing was added to the clock to fit them.

**Consequence for the cut order: games are never the cut.** Cutting one saves
nothing and removes the only assessment that beat has. This is written into both
run sheets.

## What makes a good card set

- **5–6 cards, 3–5 minutes.** More than six and the room disengages.
- **At least one card is correct as it stands.** Otherwise it becomes
  find-the-flaw, and people learn to distrust everything rather than to judge.
  Card B in the prompt game and cards 2/3/5 in the data-quality game exist for
  this.
- **The reveal teaches, the card only asks.** Each answer says *why*, in a
  sentence or two, and connects forward or back to another stage.
- **One card plants the next stage.** Card E in the prompt game ("how many
  active supporters?") is deliberately unanswerable and is not resolved — it
  pays off after the break.

## The stages without a game

Both openings and both closes. They are framing and reflection, not knowledge to
capture, and a game there would be ceremony.

---

# I-bis. Superseded: the three-file convention

Settled 2026-08-14. Every stage of both sessions is a self-contained folder:

| File | Audience | Answers |
|---|---|---|
| `README.md` | Everyone | What this part is, why it matters, what to tell them |
| `exercise.md` | Participants | Exactly what to do — prompts, expected numbers, how to tell it worked |
| `facilitator.md` | Us | The clock · what you do · what to say · **how to assert** · the answer key for this stage · what goes wrong |

Stages with nothing to run — both openings, the Genie comparison, the ML taster,
both closes — have no `exercise.md`. They still have a `facilitator.md`, because
"there is no exercise" is not the same as "there is nothing to do", and those
five stages carry most of the framing that makes the rest land.

**Why the answer keys moved out of `session-*/facilitator/`.** They were written
at session level first, which meant running a stage required three documents
open at once — the run sheet for the clock, the answer key for the numbers, the
exercise for the prompts. On the day that is a paging problem, and paging is
where a facilitator loses the room. Each stage now holds everything needed to
run it.

The two run sheets survive as **spines only**: the clock, the standing rules,
the cut order, and the pre-flight. Nothing in them duplicates a stage file.

**The one exception** is `session-4/facilitator/adf-issue-catalogue.md` — all
nineteen planted pipeline issues. It spans three stages and is long, and its job
is different: it is what you consult when someone finds something unexpected and
you need to know whether it was deliberate. The five that the stages actually
teach are summarised in the stage files.

## The assertion discipline

Every `facilitator.md` has a **How to assert** section, and every one of them
names a **specific artifact on screen plus a question with a known answer**.
Never "is everyone ok?"

This is the mechanical form of the readiness gate, and it exists because of one
line of Lucie's July feedback: people got lost and could not pick back up. A gate
that can be passed by nodding is not a gate.

Where a stage is watch-only and has no artifact, the assert section carries a
comprehension question instead, and says what a good answer sounds like.

---

# H. Risks and their fallbacks

| Risk | Likelihood | Fallback |
|---|---|---|
| Live Power BI demo stalls in stage 05 | Medium | Mykola rehearses; measures pre-written in `reports/`; a pre-built `.pbix` with the data loaded is ready to hand |
| Genie or the Databricks workspace is slow | Medium | Recorded walkthrough; stage 03 is cut-line #1 |
| Someone's laptop is IT-blocked on the day | Medium | Pair; the blocked person writes every prompt. Prompt-writing is the skill, so this is the better seat |
| Someone missed Monday | Medium | `session-4/fallback/` |
| The room over-runs stage 05 Part A and never reaches Part B | **High** | Hard time call at 2:15 — written into the run sheet. Part B carries Lucie's entire ask |
| Claude writes Python despite instructions | Medium | Named in every exercise's "if it goes wrong"; `CLAUDE.md` says SQL; stage 04 fixes it properly |
| Numbers in the room do not match the answer key | Low | `verify.py` catches a wrong dataset before Monday; the manifest is generated, not typed |
| The data is regenerated and every number goes stale | Low, catastrophic | `facilitator/README.md` lists every file carrying a number |
