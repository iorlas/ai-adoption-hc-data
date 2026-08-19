# 6 — Close

**10 minutes** · *5 min retro, out loud · 5 min the take-home and what Day 4 adds.*

> **Who does what:** **▸ Together** for the retro, then I talk for five minutes.

## The retro — three questions, quickly

Round the room, one sentence each:

1. **What worked today?**
2. **Where did it get in your way?**
3. **What is the one thing you would use on Monday?**

Say it even if it is negative. Day 4 is the last one and it is the only chance
to spend the time on what you actually want.

## What you built today

| | |
|---|---|
| `03-notebook-patterns/profiling.py` | a module, with an equivalence argument you would show a reviewer |
| `04-adf-to-sql/view.sql` | a conversion that passes a parity check, and a list of what did not convert |
| `docs/notebooks.md`, `docs/pipelines/donor-import.md` | the knowledge layer, reaching two surfaces it did not reach yesterday |

Everything on that list keeps working if you never see us again. That is
deliberate.

## The thread of the four days, in one line each

```
  Day 1   the model can be confidently wrong, so you verify
  Day 2   the cure for wrongness is context you engineer, and it compounds
  Day 3   the same habits reach things you cannot open in an editor
  Day 4   the AI moves inside the pipeline — and you decide what it must never touch
```

## Take-home 3

[`take-home-3.md`](take-home-3.md) — one flow of your own, sorted into the three
buckets. Twenty minutes if you pick a small one, and it is the only take-home
that produces something you can put in front of your team lead.

## What Day 4 adds

- **AI inside the pipeline.** Not a person prompting a model — `ai_mask`,
  `ai_classify` and `ai_extract` running as a step in SQL, over the whole table,
  on the platform's own in-region model. The obvious case for a registry is
  free-text consent and clinical notes.
- **Keeping PII away from AI**, properly: the boundary, the deny-list, and what
  you do about the `display(donor)` line from part 3.
- **Team skills** — packaging today's two jobs (profile a notebook, convert a
  flow) so nobody re-derives them.
- **Rollout**: a shared `CLAUDE.md`, who owns it, and how this survives contact
  with a busy quarter.

## One ask before Day 4

Bring the **bucket lists** from take-home 3 if you do them. If half the room
turns up with a real count of how many of their flows convert cleanly, the
rollout conversation stops being abstract.
