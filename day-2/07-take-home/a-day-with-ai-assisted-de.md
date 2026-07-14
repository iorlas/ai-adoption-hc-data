# A day of an AI-assisted data engineer

Not "AI writes your pipelines while you watch." The model does the reading, drafting, and grunt work;
**you own the outcome and the context.** Here is what the two days were building toward — the working
style, beat by beat.

## Pick up a task — orient in minutes, not an hour

Point Claude at the repo: *"what does this proc do, and what changed since I last touched it?"* You get
oriented without an hour of code archaeology. Then you **verify** the summary against the code — you never
take the explanation on trust.

## Do the work — describe the outcome, own the diff

You describe the outcome, not the keystrokes; Claude drafts. Then **nothing ships unseen**: read the
`/diff`, run `/code-review`, run the tests. The data rows never enter the model — Claude reads code and
schema, the data stays on your machine.

## Hit a decision — write it down once

Which age rule? Money as minor units? When you settle a real trade-off, capture it as an **ADR** — so next
week's session (yours or a teammate's) doesn't re-propose the option you already rejected. Decisions
compound instead of evaporating.

## When Claude stumbles — that's the signal, not a failure

A wrong answer or a missing-context moment is the cue to **improve the knowledge layer**: add the fact to
CLAUDE.md or a `docs/` file. The next attempt is better — for everyone — because it lives in Git.

## Verification is constant

You never accept an all-clear at face value. You ask the one cheap question a wrong answer can't survive
(the five tells). Owning the outcome is a habit, not a heroic double-check.

## Governance is a habit, not a gate

Code, not rows. Mask before commit. You can see what Claude read. At scale the model never touches the data
anyway — bulk anonymisation is your pipeline's job, not Claude's.

## The measure, over weeks

You find yourself telling Claude **less** while it does the **same or more** — because the context now lives
in the repo and compounds. That declining-instruction curve is the whole point of Day 2.
