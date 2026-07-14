# Claude Code, three surfaces — same engine, different cockpit

Claude Code is one tool with three front-ends. **Same model, same `CLAUDE.md`, same MCP** — what differs
is the cockpit around it. Run the *same* prompt through each and you feel the trade-offs.

| | **CLI** (terminal) | **Desktop app** | **VS Code extension** |
|---|---|---|---|
| Launch | `claude` in any repo | the Claude desktop app | the sidebar in VS Code |
| Feature completeness | **fullest, updated first** | close behind | usually a step behind the CLI |
| Image / screenshot paste | drag-drop works; terminal paste can be flaky | **native, reliable (`Ctrl/Cmd+V`)** | via the editor |
| Diff / file review | `/diff`, inline | in-app view | **inline in the editor gutter** |
| Editor context (open file, selection) | picks it up via the IDE integration | no | **tightest — grabs your open file/selection** |
| Dictation | spacebar to dictate | **native dictation** | — |
| Best for | day-to-day driving, full power, scripting | image-heavy work, a GUI when you want one | quick edits while already in VS Code |

## The same query, three ways (what to notice)

Ask each surface the *same* thing — e.g. *"explain this stored procedure and flag one risk"*:
- **CLI** gives you the full toolset and the fastest access to new features; it's where power users end up.
- **Desktop** shows the same answer in a GUI — nicer for pasting an image or when you want buttons, not
  keystrokes; it's the reliable home for screenshot paste.
- **Extension** is most convenient when you're already editing — it sees your open file and shows changes
  in the gutter — but it trails the CLI on features, and you drift to the terminal anyway.

## Rule of thumb

**Learn the CLI** — it's the fullest and it's where you'll spend most time. Reach for **Desktop** when
you want a GUI or reliable image paste, and the **extension** for quick edits mid-editing. None is
"wrong"; whichever gets you a verified result fastest is the right one.

> Versions drift between surfaces (the CLI updates first). If a feature is missing on one, check
> `claude --version` and try the CLI.

## Know what it's costing you

- **`/usage`** — your consumption against your plan (alias `/cost`). On the $20 Pro plan you each get a
  generous rolling window; light work like today sits well inside it, but it's good to know the command
  exists. (Enterprise seats bill per-token with no such window — a difference worth knowing.)
- **`/context`** — from Day 1: shows how your context window is being spent. Cheap habit, keeps sessions
  fast and cheap.
