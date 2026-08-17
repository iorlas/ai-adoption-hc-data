# Answers — 1 · Prompt refresher (and two windows)

**FACILITATOR ONLY. Never on screen.** Everything you present is in
`README.md` — read that with the room. This page is what you cannot show them.

Clock and ownership: `session-3/facilitator/run-sheet.md`.

## Read this first — the repo and dataset were never sent

Nobody arrives with it, nobody has run `verify.py`, and nobody has loaded Power
BI. The first six minutes of this stage are setup — `setup.md` is written for
the room and tells them exactly what to run.

**`setup.md` is inside the repo they do not have yet**, so it is no use to them
until after this beat. Paste these two blocks into the meeting chat instead, and
read the first one out.

```
git clone https://github.com/iorlas/ai-adoption-hc-data.git
```

```
cd ai-adoption-hc-data/data-analytics
uv run verify.py
```

**Do not apologise for the folder not arriving earlier.** Same rule as
everything else about July — no audit, no explanation. *"Right, first thing:
let's get the workshop folder onto your machines."* Matter-of-fact, thirty
seconds, move.

**Say straight away that Power BI is not needed until after the break.** Only
stage 5 needs it, at 1:50, and that load moves to the break. Otherwise half of
them open Desktop and stop listening — they agreed to preload a dataset that
never reached them, so someone will be looking for it.

**Work the room hard during the clone.** This is where a proxy block or a
missing `uv` surfaces, and it is the one thing that can cost the morning. Anyone
stuck pairs immediately — do not let someone fail quietly for six minutes.

**If a proxy blocks the clone**, hand over the folder from a memory stick and
carry on. Have one ready.

## Two windows — what not to say

**Open both windows on your own machine**, same folder, nothing typed. No
handover, no second screen: you show both yourself in thirty seconds.

**Two minutes, not five.** This is housekeeping, not a segment. Do not sell the
app; someone in the room will check and it is not more capable.

**Say nothing about how prompts were written in July.** Just teach this shape.
Raising it puts a shadow over our own previous work in front of the people who
attended it, and invites *"if July was wrong, why is today right?"* — asked of
the same two facilitators. If someone asks directly about the angle brackets,
one light sentence and keep moving; the line is already in `README.md`.

## The game — the beat that does the teaching

Read the card, **wait**, let the room call it, then reveal. Do not fill the
silence; this group answers when given room, and that call-and-response format
was the strongest twenty minutes of July.

The two cards that carry the lesson:

- **Card B** (`how many rows are in supporters.csv?`) — **fine as it is.**
  Expect someone to want to add to it. That instinct is the thing being
  corrected, so name it warmly when it appears.
- **Card D** (the four-times-too-long one) — works fine, just bloated. Filling
  in all the parts is not the goal.

**Card E** plants Session 3's spine: a well-formed prompt that is still
unanswerable, because "active" is undefined. Do not resolve it — say *"hold that
one, we come back to it after the break"* and move on. It pays off in part 4.

## The real prompt

They type. You run the same prompt in each of your two windows and narrate only
what actually differs — layout, where output lands. **Do not invent
differences.**

## Gate

1. **A row count on screen reading 4,022**, said out loud by three or more
   people. This is the earliest possible check that the whole room is on the
   same data, and it is worth more than the tool comparison.
2. **Everyone can name which window they are in for the rest of the day.**

The game is its own check: who calls Card B correctly tells you who has actually
taken "short is fine" on board, versus who is still filling in boxes.

## Answer key

`supporters.csv` = **4,022 rows.** The others if anyone goes further: campaigns
192 · donations 12,376 · campaign_activity 22,591 · fulfilment_tasks 6,000.

Game verdicts: **A** send-with-a-fix (no task, you get prose) · **B** send as-is
· **C** do not send (no location → Python; "summary" → uncheckable) · **D** send
as-is, just bloated · **E** do not send (undefined term, not a structural gap).

## What goes wrong

**Nobody calls out on the first card.** Normal. Answer Card A yourself, then ask
Card B — by the third they will be calling. Do not abandon the format after one
silence.

**Someone argues Card B needs more.** Perfect. Ask what they would add and what
it would buy. Usually the honest answer is nothing, and hearing themselves say
that lands better than being told.

**Someone says the terminal is "proper" and the app is for beginners.** Correct
it flatly — same engine, and plenty of daily users are in the app for the
file-review view.

**A row count is wrong.** Stop the room. Stale clone or wrong folder. Ten times
cheaper here than at 11:30.

**You over-run.** Cut the window narration in the last beat to thirty seconds.
**Keep the game and keep the row count.** The game is the stage; the window
comparison is housekeeping.

## If someone asks "which should I use?"

Answer without hedging:

> "If you are not already a terminal person, use the desktop app. If you are,
> stay in the terminal. Same Claude, same answers. Just do not switch mid-day."

The plan we sent named the desktop app, so leading with it is consistent. Do not
turn this into a comparison — the page in `reference/` covers it for anyone who
wants the detail.

## Setup failures — verified remediations

`verify.py` was run cold against an empty package cache and works: it carries
PEP 723 inline metadata, so `uv run verify.py` fetches DuckDB into its own
environment regardless of what is installed on the machine. Nobody needs
DuckDB, and nobody needs the right Python — uv downloads a 3.11+ build if the
laptop only has an old one. **Plain `python verify.py` will fail** for everyone;
insist on `uv run`.

**Tell the room to use Git Bash, not PowerShell**, at the same moment you paste
the clone commands. VS Code's terminal dropdown has it. Two things in the
material assume it, and PowerShell fails both.

### The TLS-interception fix — the one worth memorising

If anyone's `git clone` says **`SSL certificate problem: unable to get local
issuer certificate`**, the network is inspecting encrypted traffic. `uv` will
fail on the same machine for the same reason, because it ships its own
certificate list rather than using Windows'. In Git Bash:

```bash
export UV_SYSTEM_CERTS=true      # newer uv
export UV_NATIVE_TLS=true        # older uv — harmless to set both
```

Set both if you do not know their `uv --version`. For git on that machine, the
proxy variable fixes it and fixes uv at once:

```bash
export HTTPS_PROXY=http://their.proxy:port
```

**Never suggest `http.sslVerify=false`.** Wrong habit to teach a charity's data
team, and the memory stick is the better answer anyway.

Other signatures, which mean different things:

- `Could not resolve host: github.com` — DNS blocked, or a proxy is required
  and not configured.
- `Failed to connect ... port 443: Timed out` — egress firewall.
- `Received HTTP code 403 from proxy after CONNECT` — proxy refusing github.com.

All four are memory-stick moments if the fix is not immediate. Do not debug a
network in front of ten people.

**A browser that works proves nothing.** `uv` does not read Windows' system
proxy settings, so a laptop where Chrome sails through can still fail here.

### Hosts that must be reachable — and the two we never asked for

| Host | Needed for | Was it in the letter? |
|---|---|---|
| `github.com` | the clone | **yes** |
| `objects.githubusercontent.com` | managed Python download | **no** |
| `pypi.org` | package index lookup | **yes** |
| `files.pythonhosted.org` | the DuckDB wheel itself | **no** |
| `python.org`, `astral.sh`, `anthropic.com` | installers | yes |

**The prerequisites letter asked IT for four domains. The download chain needs
six.** If a team's IT allowlisted literally what we wrote, `uv` will resolve the
package index and then fail fetching DuckDB — on a machine where the browser,
git and everything else works perfectly.

**The signature: the error names `files.pythonhosted.org`, not `pypi.org`.**
That is an allowlist gap, not a broken install. The memory stick does not fix it
either — the stick carries the repo, not the DuckDB wheel. That person pairs
with a neighbour, and IT gets a two-line email at the break.

These hosts are often allowlisted separately, so pypi can work while GitHub is
blocked, or the reverse.
