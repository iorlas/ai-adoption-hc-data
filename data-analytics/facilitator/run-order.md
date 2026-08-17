# Running order — who owns what

**FACILITATOR ONLY. Generated — do not hand-edit.**
Regenerate with `uv run facilitator/build-run-order.py`. The stage clock
tables come from the same source, so they cannot drift from this page.

## The rule

**Whole stages belong to one person.** Nothing is co-presented and nobody
cuts in during someone else's block. If you have something to add, hold it
for the handoff or the break — the room hears one voice at a time, and each
of you gets a long enough run to actually build something.

The person not presenting is **on the floor**: unblocking, reading over
shoulders, spotting who is stuck. That is a real job and it is silent.

What forces the split: **Power BI Desktop is Windows-only and Databricks is
Mykola's trial**, so build-and-verify, Genie and the ML taster have to be
his. Every other stage could go either way.

---

# Session 3 — the blocks

| Clock | Min | Owner | Covers |
|---|---|---|---|
| 0:00–0:52 | 52 | **Denis** | Opening · Setup, then the prompt refresher · Data quality |
| 0:52–1:00 | 8 | **Mykola** | Genie vs Claude Code (watch only) |
| 1:00–1:10 | 10 | — | *Break* |
| 1:10–2:45 | 95 | **Mykola** | One definition, shared across the team · Build a report, then prove it is right |
| 2:45–3:00 | 15 | **Denis** | Close |

**3 handoffs.** Longest block: 95 min.

## Session 3 — beat by beat

### 0:00–0:05 · Opening — **Denis**
`session-3/00-opening/`

| Clock | Min | Beat |
|---|---|---|
| 0:00–0:03 | 3 | July in one sentence, and what the August call changed |
| 0:03–0:05 | 2 | Shape of the day, the rhythm, "stop us" |

### 0:05–0:22 · Setup, then the prompt refresher — **Denis**
`session-3/01-prompt-refresher/`

| Clock | Min | Beat |
|---|---|---|
| 0:05–0:11 | 6 | **Everyone clones and runs `verify.py`** — the repo was not sent ahead |
| 0:11–0:13 | 2 | Two windows — **both open on your own machine**, no handover |
| 0:13–0:16 | 3 | The shape: situation · question · task, and *you rarely need all three* |
| 0:16–0:18 | 2 | **Game** — five prompt cards, call-and-response |
| 0:18–0:22 | 4 | They run the real prompt; collect the row count — 4,022 |

### 0:22–0:52 · Data quality — **Denis**
`session-3/02-data-quality/`

| Clock | Min | Beat |
|---|---|---|
| 0:22–0:30 | 8 | Demo — steps 1–2, **including the deliberate `Activ` mistake** |
| 0:30–0:47 | 17 | They repeat steps 1–3; Mykola on the floor, weighted to Lauren's team |
| 0:47–0:52 | 5 | **Game** — keep it or bin it |

### 0:52–1:00 · Genie vs Claude Code (watch only) — **Mykola**
`session-3/03-genie-vs-claude-code/`

| Clock | Min | Beat |
|---|---|---|
| 0:52–0:54 | 2 | Framing — and that nobody needs Databricks access |
| 0:54–0:57 | 3 | The same question into both, on our workspace |
| 0:57–1:00 | 3 | **Game** — five questions, which tool would you reach for |

### 1:00 · Break

### 1:10–1:50 · One definition, shared across the team — **Mykola**
`session-3/04-shared-definitions/`

| Clock | Min | Beat |
|---|---|---|
| 1:10–1:16 | 6 | Demo — steps 0–1, both numbers and the Power Query line on screen |
| 1:16–1:28 | 12 | They work steps 1–2; Denis on the floor |
| 1:28–1:33 | 5 | **Game** — where does this knowledge live |
| 1:33–1:41 | 8 | **The decision, as a room** — four numbers on the whiteboard |
| 1:41–1:50 | 9 | They write it up, steps 5a–5d |

### 1:50–2:45 · Build a report, then prove it is right — **Mykola**
`session-3/05-build-and-verify/`

| Clock | Min | Beat |
|---|---|---|
| 1:50–2:00 | 10 | Part A demo — model and two measures live in Power BI Desktop |
| 2:00–2:15 | 15 | Part A — they build; Denis on the floor |
| 2:15–2:21 | 6 | Part B demo — the copy-out / paste-back loop |
| 2:21–2:40 | 19 | Part B — they interrogate and cross-check |
| 2:40–2:45 | 5 | **Game** — what do you say to the stakeholder |

### 2:45–3:00 · Close — **Denis**
`session-3/06-close/`

| Clock | Min | Beat |
|---|---|---|
| 2:45–2:55 | 10 | Retro — three questions, answers written down |
| 2:55–3:00 | 5 | The practice ask before Tuesday |

---

# Session 4 — the blocks

| Clock | Min | Owner | Covers |
|---|---|---|---|
| 0:00–0:40 | 40 | **Denis** | Opening · ADF — explain it |
| 0:40–1:30 | 50 | **Mykola** | ADF — document it · ADF — find the weak spots |
| 1:30–1:40 | 10 | — | *Break* |
| 1:40–2:15 | 35 | **Denis** | Asking better questions of your data |
| 2:15–2:45 | 30 | **Mykola** | A first look at machine learning (watch only) |
| 2:45–3:00 | 15 | **Denis** | Close |

**4 handoffs.** Longest block: 50 min.

## Session 4 — beat by beat

### 0:00–0:15 · Opening — **Denis**
`session-4/00-opening/`

| Clock | Min | Beat |
|---|---|---|
| 0:00–0:06 | 6 | Practice check-in — "I did not get to it" said *before* asking |
| 0:06–0:09 | 3 | What we changed from last night's retro |
| 0:09–0:13 | 4 | Frame the day, and the ADF boundary in Lucie's words |
| 0:13–0:15 | 2 | Hand out `fallback/` quietly, while the room settles |

### 0:15–0:40 · ADF — explain it — **Denis**
`session-4/01-adf-explain/`

| Clock | Min | Beat |
|---|---|---|
| 0:15–0:20 | 5 | Demo — step 1, then **the watermark question**, and let them get it |
| 0:20–0:35 | 15 | They work steps 1–4; Mykola on the floor |
| 0:35–0:40 | 5 | Share what you found |

### 0:40–1:10 · ADF — document it — **Mykola**
`session-4/02-adf-document/`

| Clock | Min | Beat |
|---|---|---|
| 0:40–0:45 | 5 | Demo — step 1, with the `[inferred]` instruction visible |
| 0:45–1:05 | 20 | They work steps 1–4; watch for invented business reasons |
| 1:05–1:10 | 5 | Share-back |

### 1:10–1:30 · ADF — find the weak spots — **Mykola**
`session-4/03-adf-weak-spots/`

| Clock | Min | Beat |
|---|---|---|
| 1:10–1:14 | 4 | Demo — step 1, and the re-rank-by-consequence correction |
| 1:14–1:26 | 12 | They work; **the rules handover is called out loud** |
| 1:26–1:30 | 4 | "The worst one you found" |

### 1:30 · Break

### 1:40–2:15 · Asking better questions of your data — **Denis**
`session-4/04-better-questions/`

| Clock | Min | Beat |
|---|---|---|
| 1:40–1:46 | 6 | Demo — one hypothesis, up to the change-my-mind step |
| 1:46–2:10 | 24 | They work one hypothesis; **stop the room on the reversal** |
| 2:10–2:15 | 5 | Share-back |

### 2:15–2:45 · A first look at machine learning (watch only) — **Mykola**
`session-4/05-ml-taster/`

| Clock | Min | Beat |
|---|---|---|
| 2:15–2:20 | 5 | What the data has to look like |
| 2:20–2:33 | 13 | Building the table, and AutoML running |
| 2:33–2:41 | 8 | **How you would know whether to believe it** |
| 2:41–2:45 | 4 | The leakage demonstration |

### 2:45–3:00 · Close — **Denis**
`session-4/06-close/`

| Clock | Min | Beat |
|---|---|---|
| 2:45–2:49 | 4 | Everyone writes their one sentence |
| 2:49–2:55 | 6 | Retro across all four sessions |
| 2:55–2:58 | 3 | The backlog — named, including MCP, and **get an answer** |
| 2:58–3:00 | 2 | The feedback ask |

---

# Denis — your blocks

## Session 3 — 67 min, 2 blocks

**0:00–0:52  ·  52 min**

- Opening
- Setup, then the prompt refresher
- Data quality

**2:45–3:00  ·  15 min**

- Close

On the floor for 103 min — unblocking, not talking.

## Session 4 — 90 min, 3 blocks

**0:00–0:40  ·  40 min**

- Opening
- ADF — explain it

**1:40–2:15  ·  35 min**

- Asking better questions of your data

**2:45–3:00  ·  15 min**

- Close

On the floor for 80 min — unblocking, not talking.

---

# Mykola — your blocks

## Session 3 — 103 min, 2 blocks

**0:52–1:00  ·  8 min**

- Genie vs Claude Code (watch only)

**1:10–2:45  ·  95 min**

- One definition, shared across the team
- Build a report, then prove it is right

On the floor for 67 min — unblocking, not talking.

## Session 4 — 80 min, 2 blocks

**0:40–1:30  ·  50 min**

- ADF — document it
- ADF — find the weak spots

**2:15–2:45  ·  30 min**

- A first look at machine learning (watch only)

On the floor for 90 min — unblocking, not talking.

---

# Airtime

| | Denis | Mykola | Break |
|---|---|---|---|
| Session 3 | 67 min | 103 min | 10 min |
| Session 4 | 90 min | 80 min | 10 min |
