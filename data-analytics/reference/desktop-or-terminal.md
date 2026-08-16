# Desktop or terminal — same Claude Code, two cockpits

In July you used Claude Code in the **terminal**. The prerequisites asked you to
install the **desktop app** as well.

That is not a correction and it is not an upgrade. It is the **same Claude
Code** — same model, same `CLAUDE.md`, same files, same everything that
matters. What changes is the window around it.

**For everything in these two sessions, the two are equal.** Every prompt in
every exercise works identically in both. Nobody is going to tell you which to
use, and we are not going to spend the day selling you a window.

We do spend twelve minutes on it on Monday morning, because half the room has
never opened the app and finding that out at 10:15 is expensive.

## The honest comparison

| | Terminal (what you used in July) | Desktop app |
|---|---|---|
| What it looks like | A black screen you type into | A normal window |
| Getting into the project | `cd` to the folder, run `claude` | Open the folder |
| Asking something | Type it | Type it |
| Seeing what it changed | `/diff`, as text | Side by side, laid out |
| Two things at once | A second terminal tab | A second conversation, in the app |
| Pasting a screenshot | Fiddly | Works properly |
| Long output | Scrolls past | Scrolls, and stays readable |
| New features | Arrive here first | Arrive shortly after |
| If you got comfortable in July | This is it, unchanged | New, but not difficult |

## So which one?

**Whichever you will actually open.** That is not a dodge — it is the only
criterion that matters, and it is different per person:

- If July's terminal clicked for you and you have used it since, **stay there.**
  Nothing in these two days needs the app.
- If the black screen was part of why it did not stick, **the app removes that**
  and changes nothing else.
- If you are reviewing a lot of edits, the app's side-by-side view is genuinely
  easier on the eye. That is the one real difference you will feel this week.

Some people end up using both — the app for reading and reviewing, the terminal
when they are moving fast. That is normal and it is not a decision you have to
make in advance.

## The four things worth knowing, whichever you pick

1. **Claude works inside a folder.** Point it at the workshop folder once. If it
   says it cannot find `data/supporters.csv`, you are in the wrong folder — you
   want the one containing `README.md` and `verify.py`.

2. **Plain English is the interface.** If you remember the angle-bracket style
   from July — `<request>…</request>` and so on — nothing in these materials
   uses it. It is a real technique for very long prompts; everything here is one
   to three sentences, so it would only add typing.

3. **Read the change before you accept it.** Claude edits files. Both cockpits
   show you what is about to happen, and the habit worth building this week is
   not clicking straight through. One exercise on Monday turns on noticing
   exactly this.

4. **Start a new conversation when the subject changes.** A conversation carries
   everything said in it — usually helpful, occasionally not. Twice on Monday
   you are asked to start a fresh one deliberately, so that an earlier answer
   cannot contaminate a later one.

## Things you do not need

Genuinely, in either cockpit. They will not come up:

- Any command starting with a slash
- Git commands — you will not type one
- Python — you will not write any
- Settings, models, tokens

## If something is broken on Monday

Tell us at the start rather than working around it quietly. Pairing is a fine
outcome, and the person **without** the working machine writes every prompt
while the other only types. Writing the prompt is the skill being taught, so
that is the better seat, not the consolation one.
