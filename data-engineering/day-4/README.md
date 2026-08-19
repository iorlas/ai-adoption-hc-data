# Day 4 — The connection, and the AI inside the pipeline

Day 3 did everything that could be done with files on your own laptop. **Today
is the day that needs the workspace** — all of it in one place, so there is one
setup rather than four.

Two halves. The morning is the connection: what it takes for Claude Code to work
against a real Databricks workspace, and what Genie needs from you before it is
worth anything. The afternoon is the AI moving *inside* the pipeline, and the
boundary you draw around it.

## The day

| # | Folder | Min | What you do |
|---|---|---|---|
| 0 | `00-opening/` | 5 | Where Day 3 got to, and the shape of today |
| 1 | `01-connect-databricks/` | 20 | Claude Code against a real workspace: catalog, SQL, and the boundary |
| 2 | `02-genie/` | 25 | Curate a Genie space, then the same question to Genie and to Claude Code |
| — | *break* | 15 | |
| 3 | *AI inside the pipeline* | 45 | `ai_mask` / `ai_classify` / `ai_extract` as a step in SQL, and verifying AI-labelled output |
| 4 | *Keeping PII away from AI* | 20 | The boundary, the deny-list, and the `display(donor)` line from Day 3 |
| 5 | *Team skills* | 25 | Package Day 3's two jobs so nobody re-derives them |
| 6 | *Rollout and close* | 25 | A shared `CLAUDE.md`, who owns it, and the retro across four days |

**Parts 3 to 6 are not built yet.** Parts 0 to 2 are.

## What you need in front of you

- Claude Code working, as on Days 1–3
- This repo, pulled
- **No workspace of your own is required.** Parts 1 and 2 run on my workspace,
  and are watch-only. If you have access and want to follow along, the commands
  are all in part 1

## Files, same as every day

| | |
|---|---|
| **`README.md`** | **The part.** We read it together |
| **`answers.md`** | The answer key, for the parts that have one. Read it after the part, not before |
| **`game.md`** | A few cards, called out loud |
