# Prep — Day 4

**FACILITATOR ONLY.** One facilitator. Everything below is yours.

## State of the day

| Part | Minutes | Built? | Needs building first |
|---|---|---|---|
| `00-opening` | 5 | **No** | No |
| `01-connect-databricks` | 20 | Yes | **Workspace, warehouse, service principal, seeded table** |
| `02-genie` | 25 | Yes | **Two Genie spaces, and a recording of both** |
| AI inside the pipeline | 45 | **No** | **AI Functions on a serverless warehouse, in region** |
| Keeping PII away from AI | 20 | **No** | No |
| Team skills | 25 | **No** | No |
| Rollout and close | 25 | **No** | No |

**Four of seven parts are unwritten.** This file covers the Databricks
dependency, which is the long-lead item and is shared by three of them.

## 1 · The workspace (parts 1, 2 and the AI-functions segment)

- A workspace in **West or North Europe**. Not UK South: AI Functions there need
  a cross-Geo flag that routes data out of the UK, which is not a conversation
  you want to have with a UK charity's security people. UK West is unsupported.
- A **serverless SQL warehouse**, DBR 18.2+. Note the warehouse id — the
  statement-execution call needs it.
- Catalog `training`, a schema in it, and `day-1/data/donor.csv` loaded as
  `donor` — **all 5,005 rows, defects intact.** Status counts must be
  2,885 / 728 / 702 / 670 / **20 `Activ`**.
- A **service principal** with read on that schema and use on the warehouse.
  Not a personal token: part 1 argues for service principals out loud, and
  demoing with a PAT undercuts it.
- `databricks auth login --profile an-workshop` working on the laptop you
  present from, verified that morning.
- **Confirm the AI Functions quota** on whichever workspace you use, before the
  day. That segment has no fallback that is worth running.

Rehearse part 1's three prompts end to end. Keep the working
statement-execution JSON in a scratch file — it is the difference between a
two-minute recovery and a lost segment.

## 2 · The two Genie spaces (part 2)

Build **two**, do not edit one live:

- **`AN Donor (raw)`** — the donor table, no table comment, no column comments,
  no curated definitions.
- **`AN Donor`** — same table plus a table comment with the grain, a comment on
  `status` naming the four valid values and the `Activ` defect, and one curated
  definition of "active donor" with its SQL.

Ask *"how many active donors do we have?"* in each. **Screen-record both.** If
the second answer is not visibly better, read the note in `02-genie/answers.md`
before the day — there is a line that saves the segment, and it lands far better
as a planned point than as a recovery.

## 3 · What is still to write

In the order they matter:

1. **AI inside the pipeline** — the client's own stated direction, and the one
   segment in four days that shows AI running at scale rather than at a prompt.
   One case: PII classify and mask with `ai_mask`, `ai_query` shown once as the
   general primitive underneath. Synthetic data, in-region model, and a
   verification pass on the AI-labelled output — the verification is what makes
   it a data-engineering segment rather than a demo.
2. **Rollout and close** — the last thing they hear, and the only part that
   speaks to what happens after we leave.
3. **Keeping PII away from AI** — mostly assembled already from Days 1–3; the
   new material is the deny-list and the `display(donor)` line.
4. **Team skills** — the most cuttable, and the easiest to write.

## 4 · The room, one facilitator

Same as Day 3: nobody is circulating, so say at the top that people must call
out when stuck. Parts 1 and 2 are watch-only and both can lose five minutes
without damage, which makes the morning your recovery slack — spend it early
rather than saving it.
