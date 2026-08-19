# Answers — 2 · Claude Code against a real workspace

**FACILITATOR ONLY. Never on screen.**

## Before the day — this part does not exist unless you build it

See `facilitator/prep-denis.md`. In short: a workspace, a serverless SQL
warehouse, a `training` catalog with a schema holding the `donor` table, a
service principal, and **the whole sequence rehearsed and screen-recorded.**
The recording is the fallback and you will be glad of it.

## What is actually being taught

Not "here is how to log into Databricks." Two things:

1. **The myth kill.** Half of this room believes Claude Code needs MCP to touch
   Databricks. It does not; it needs a shell. If they leave with only this, the
   twenty minutes paid for itself, because it unblocks work they think is
   blocked.
2. **The boundary shift.** Every other part of these four days keeps rows away
   from the model structurally. This one does not. Say it plainly.

## The three prompts — what to watch for live

**Prompt one.** It may try `databricks catalogs list --profile an-workshop` or
set `DATABRICKS_CONFIG_PROFILE` first. Both are fine. If it invents a flag,
**let it fail on screen and say so** — that is a Day-1 tell landing on Day-3
material, and it is worth more than a clean run.

**Prompt two.** Statement execution is the fiddly one. If it stalls, the shape
that works is:

```bash
databricks api post /api/2.0/sql/statements --profile an-workshop --json '{
  "warehouse_id": "<id>",
  "statement": "select status, count(*) as n from training.<schema>.donor group by status order by n desc",
  "wait_timeout": "30s"
}'
```

Have that in a scratch file. If it has not produced a result by minute 6 of the
live block, paste it yourself, narrate it as *"this is the one I had ready"*,
and move on. **Do not debug the CLI in front of the room** — you lose part 3.

**Prompt three is the one that must happen.** If the clock is tight, cut prompt
two and keep prompt three: it is the only one that connects this part to Day 2.

## The number they will ask about

If the seeded `donor` table in the workspace matches `day-1/data/donor.csv`, the
status counts are:

| status | rows |
|---|---|
| Active | 2,885 |
| Withdrawn | 728 |
| Suspended | 702 |
| Deferred | 670 |
| **Activ** | **20** |

The `Activ` typo will show up on screen. **Do not explain it here** — part 4
turns on someone noticing that a filter written as `status == 'Active'`
silently drops those twenty rows. If somebody spots it now, credit them and say
"hold that thought, it comes back after the break."

## What goes wrong

**Somebody with access tries to follow along and gets stuck.** Expect it. The
line is: *"leave it, nothing later today needs it."* Meant literally — parts 3,
4 and 6 are all local.

**"Can we get a workspace like yours?"** Adrian's team administers ADB
themselves; Shankar's does not. The honest answer is that a training schema plus
a service principal is a small ask internally, and it is Adrian who can grant
it. Say that out loud with Adrian in the room; it is a decision that can be made
in ten seconds and otherwise takes a month.

**Someone asks about MCP for Databricks.** It exists, and it is not what this
part is arguing against. The point is that the CLI path needs no approval,
because it is the same shell access they already have.
