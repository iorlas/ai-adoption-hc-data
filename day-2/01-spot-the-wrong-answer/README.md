# Stage 01 — Own the outcome: verify, and dismiss wrong answers fast

## The principle (teach this before the game)

When you use AI, **you own the result** — not the model. If the report is wrong, it's your name on it.
So the one non-negotiable skill is being able to **verify what you're looking at**.

The good news: verifying is usually cheap. You almost never redo the work. You need **one small challenge
that would expose the answer if it were lying** — ask for the failing rows, the definition, the data
source. The reflex to build today is dismissing a dangerous or wrong answer *fast*, before it reaches a
pipeline.

## Five tells — what to look for

A confident-but-wrong answer almost always trips one of these:

1. **No exceptions shown.** An all-clear ("everything's valid") with no failing rows named. Real checks
   name their exceptions. → *"list the ones that failed."*
2. **A metric with no test named.** "99.6% valid" — valid by *what*? Format? Checksum? Both? → *"valid by
   which rule, exactly?"*
3. **Wrong scope or wrong source.** An `n` that reveals it ran on a sample, or the wrong dataset. →
   *"which data did you run against?"*
4. **Undefined terms.** "duplicates", "problems", "good" with no definition — so you can't check it. →
   *"define it, then run it again."*
5. **Too clean to be true.** A tidy vocabulary or a round result on messy real-world data. → *"give me the
   raw distribution (`value_counts`), not a summary."*

The meta-rule under all five: **you don't redo the work, you ask the one cheap question a wrong answer
can't survive.**

## The game — apply the tells

Five answers Claude might give about the donor data. For each: **would you ship it, and which tell (if
any) fires?** Read the card, let the room call it, then reveal.

> Ground truth: 5,005 donors. NHS defects = 30 (19 malformed + 11 wrong check digit) → 4,975 fully valid.
> Also ~200 blank emails, ~15 blank sex, 20 `Activ` typos, ~5 duplicate donors, a few future dates.

### Card A
> *"I checked all 5,005 NHS numbers — every one is valid."*

**Tell 1 (no exceptions).** Wrong — 30 fail. An all-clear with no failing rows shown. Ask: *"list the
ones that failed."*

### Card B
> *"99.6% of NHS numbers are valid."*

**Tell 2 (no test named).** Half-right, which is worse: 99.6% (4,986) is the *format* pass rate; format +
Modulus-11 checksum is 99.4% (4,975). Ask: *"valid by which test — format, or checksum too?"*

### Card C
> *"25% of donors have a data-quality issue (5 of 20)."*

**Tell 3 (wrong scope).** It ran against a 20-row sample, not the 5,005-row table. The `n` gives it away.
Ask: *"which dataset did you run against?"* — this is Monday's CSV-vs-MCP trap.

### Card D
> *"There are no duplicate donors in the file."*

**Tell 4 (undefined term).** Wrong — ~5 people appear twice. "Duplicate" was never defined. Ask:
*"duplicate by which columns? show me the pairs."*

### Card E
> *"The `status` column has four values: Active, Suspended, Withdrawn, Deferred."*

**Tell 5 (too clean).** Misses the fifth: `Activ` (~20 rows, a typo). Real data is rarely this tidy. Ask:
*"give me `value_counts`, not a summary."*

## The lesson

Every wrong answer had a tell, and every tell had a **ten-second challenge** that would have caught it.
Owning the outcome isn't heroic double-checking — it's the habit of asking the one question the answer
can't survive.

## Commands that do this for you

The tells are the habit; a few Claude Code commands operationalise it. **Check they're on your version
first** (`claude --version`) — some are recent.

- **`/diff`** — review exactly what changed before you commit. The first reflex; nothing ships unseen.
- **`/code-review low`** — a fast, high-confidence review of your changes (higher levels `medium` /
  `high` / `xhigh` cast a wider, noisier net). Catches correctness bugs the five tells won't.
  *(It's `/code-review low`, not `/review low` — plain `/review` is GitHub-PR-only.)*
- **`/simplify`** — a cleanup-only pass (reuse, simplify, efficiency; no bug-hunt) for taming
  overwrought AI output. *Needs a recent build — verify it's present.*
- **`/security-review`** — scan the diff for security issues before it ships. Our PII/compliance gate.

The point isn't the command list — it's that **owning the outcome has tooling.** Manual tells for the
answer in front of you; `/diff` + `/code-review` + `/security-review` before anything you keep.
