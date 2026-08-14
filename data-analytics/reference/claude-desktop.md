# The Claude desktop app — five minutes before Monday

July ran in the terminal. The prerequisites asked for the **desktop app**,
because a normal Windows window is a better place to spend two days than a black
screen. It is the **same tool** — same model, same `CLAUDE.md`, same everything.
Only the window around it changed.

Read this before Session 3. It is the only thing in these two days you are
expected to have picked up on your own, and it takes five minutes.

## The four things you need

### 1. Open a project folder

Claude works *inside a folder*. Point it at the workshop folder once and it can
read everything in it — the data, the reports, the pipeline JSON, `CLAUDE.md`.

Open the app → open the workshop folder as your project. If you have it open and
Claude says it cannot find `data/supporters.csv`, you have the wrong folder —
it should be the one containing `README.md` and `verify.py`.

### 2. Ask in plain English

Type the question. That is the whole interface.

No brackets, no tags, no special syntax. If you remember the notation from July
that nobody liked — you do not need it. Plain sentences work, and everything
written in these exercises is a plain sentence you can copy.

### 3. See what it changed, before you keep it

Claude edits files. **Read the change before you accept it.** The app shows you
what it is about to do; the habit worth building this week is not clicking
through that.

This matters more than it sounds. In one exercise you will deliberately ask
Claude to edit one section of a file and watch whether it quietly rewrites the
rest.

### 4. Start a new conversation when the subject changes

A conversation carries everything said in it. That is usually helpful and
occasionally not — twice in these two sessions you are asked to start a **fresh**
conversation so that an earlier answer cannot contaminate a later one.

There is a button for it. That is all you need to know.

## The three surfaces, if anyone asks

| | **Desktop app** | Terminal (CLI) | VS Code extension |
|---|---|---|---|
| What it is | A normal window | The black screen from July | A sidebar inside VS Code |
| Best for | Everything in these two sessions | Power users, scripting | Quick edits while already editing |
| Image / screenshot paste | Reliable | Fiddly | Via the editor |
| Seeing changes | In-app | `/diff` | In the editor gutter |

**Use the desktop app for these two sessions.** If your team already got
comfortable in the terminal in July, that is completely fine and everything in
these exercises works there unchanged — the prompts are the same. Do not switch
on Monday morning just to match the room.

## Things you do not need to know

Genuinely. They will not come up:

- Any command starting with a slash
- Git commands — you will not type one
- Python — you will not write any
- Anything about tokens, models, or settings

## If something is wrong on Monday morning

Tell us at the start rather than working around it quietly. Pairing up is a
perfectly good outcome, and the person **without** a working machine writes every
prompt while the other only types. Writing the prompt is the skill being taught,
so that is the better seat, not the consolation one.
