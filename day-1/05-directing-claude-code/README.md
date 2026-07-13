# Section 5 — Directing Claude Code (1:55, ~30 min)

Four levers for steering the tool. The first three you do hands-on now, on the repo you already have.
The fourth (MCP) is a live demo you watch.

## 1. `CLAUDE.md` — standing context

Open this repo's `CLAUDE.md`. It is a thin starter: what the project is, the stack, the data-safety
rule. It rides in the context box on **every** turn, so it is where standing facts belong (instead of
re-typing them each prompt). Later in the week you grow it into a proper project brief.

**Try:** add one line to `CLAUDE.md` (for example, a naming convention you want followed) and watch
Claude honour it without being reminded.

## 2. Permissions

Claude Code asks before it does anything consequential (edits, shell commands). You decide what to
allow once versus every time. The habit: **read what it wants to do before you approve it** — approval
is a verification point, not a rubber stamp.

## 3. Slash commands

Reusable prompts you invoke with `/`. They package a repeatable task so you (and the team) run it the
same way every time. Skim the built-ins; later you can author your own.

## 4. MCP vs Skills (watch the demo)

- **MCP** connects Claude to an **external capability** through a server (a database, an API, a
  filesystem). It is *plumbing*.
- **Skills** are **authored methodology** the agent follows — a repeatable way of working. It is
  *know-how*.

**The demo:** schema-aware SQL through the official **Microsoft SQL MCP Server** (Data API Builder)
against a live SQL Server. Watch Claude first ask the database to *describe itself*, then read and
aggregate data through **typed, deterministic tools** — not by writing raw SQL it might get wrong.

> That is the point that ties back to Section 3: MCP is how you give an agent database access
> **without** letting it hallucinate SQL. The guardrail is built into the plumbing.

**Optional stretch** (only if your own SQL Server is already running): you can point an `.mcp.json` at
your database and try the same thing. Not required — the concept is the goal today, not the setup.
