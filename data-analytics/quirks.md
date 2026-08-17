# Quirks — when something does not behave

**Everything here is Windows.** Look up your symptom, apply the fix, carry on.
If a fix does not work in thirty seconds, **tell us and pair with a neighbour** —
nobody is spending a session watching someone else's laptop, and nothing here is
worth losing an exercise over.

Nothing on this page is your fault. Every single one of these is a known rough
edge in a tool, not a mistake you made.

---

## Which terminal

**Use Git Bash.** In VS Code it is in the terminal dropdown — the `∨` next to
the `+` at the top right of the terminal panel. Everything in these two days is
written for it.

You checked your installs in PowerShell and that was correct. From here on,
Git Bash.

> **Why it matters.** Some of the commands in the material contain quotes inside
> quotes. Git Bash handles them; PowerShell reads the same line differently and
> gives you a confusing error about `*` or an unterminated string. Nothing is
> broken — it is the wrong shell.

---

## Getting the folder

### `git` is not recognised

Git did not install, or the terminal was open before it did. Close the terminal,
open a new one, try again. Still nothing — pair up, and we will sort it at the
break.

### `SSL certificate problem: unable to get local issuer certificate`

Your network inspects encrypted traffic and the tools do not recognise its
certificate. **Tell us** — the same thing will stop `uv` a minute later, and we
fix both at once.

### `Could not resolve host: github.com` · `Timed out` · `403 from proxy`

Three different network blocks. All of them mean the same thing for you: **tell
us now.** We have the folder on a memory stick.

### `Your local changes would be overwritten by merge`

You edited a file and then pulled. Park your edits, pull, put them back:

```bash
git stash
git pull
git stash pop
```

---

## The green check

### `uv` is not recognised

Same as git above — usually a terminal that was open before `uv` was installed.
New terminal.

### `ModuleNotFoundError: No module named 'duckdb'`

You ran `python verify.py`. Run it the other way:

```bash
uv run verify.py
```

`uv` builds a small environment and fetches DuckDB for you. Plain Python does
not, and never will. **This is the single most common one.**

### The error mentions `files.pythonhosted.org`

This one is not yours to fix. Your IT allowlisted the package index but not the
place the packages actually download from. **Tell us** — you pair for now, and
it is a two-line email to IT.

### `python` opens the Microsoft Store

Windows ships a placeholder that pretends to be Python. Try `py --version`
instead — if that works, Python is installed and only the PATH is wrong.

You mostly do not care: everything today goes through `uv run`, which uses its
own Python regardless.

### It says WARN, or the row count is not 4,022

Almost always the wrong folder — an older copy of the repo from a previous
clone, or a `data-analytics` inside something else. Run `pwd` and check you are
in the folder you cloned this morning. If you are, `git pull`.

---

## Power BI

### It asks me to sign in

Dismiss it. **You never need to sign in to Power BI for anything in these two
days.** Everything is a file on your own laptop.

### Do I need a workspace? Do I need to ask IT?

No, and no. Workspaces belong to Power BI *Service*, which is for publishing
reports to other people. We never publish anything.

### Where do I create the report?

In the Power BI window. If it opens on the Home screen, **New → Report**.
Otherwise the blank canvas in front of you is already it.

Not in VS Code — a `.pbix` is a binary file and a text editor cannot make one.

### The save dialog offers "Power BI Project (.pbip)"

You have a preview feature switched on. Choose **Power BI report (.pbix)**.

### I am stuck on a dialog I cannot close

Almost always display scaling. Power BI draws some dialogs partly off-screen
above 100% text scaling, or below 1440×900. Set scaling to 100%, or drag the
window to a larger screen.

This one looks like a crash and is not one.

### Every column came in as Text

Type detection is switched off on your machine.
**File → Options and settings → Options → Global → Data load → Type detection.**

That setting only applies to *new* imports, so **remove the table and load the
file again** afterwards — toggling it alone changes nothing on screen.

### A date column is full of errors

First **Home → Transform data** to open the Power Query Editor — this fix does
not exist in the report view. Then right-click the column header →
**Change type → Using locale** → Date, and pick the locale. Plain "change type
to Date" re-runs the same failing read and fails the same way.

### I used Get Data → Folder and it looks like nonsense

Folder import assumes every file has the *same* columns, and ours do not — it
takes the first file's shape and forces it on the other four. Start again with
five separate **Text/CSV** imports.

---

## Claude

### It gave me a different number from everyone else

Good catch, and worth stopping for. Ask it to show you the SQL it ran. Nine
times out of ten the query answers a slightly different question from the one
you asked.

`reference/checking-the-answer.md` is the page for this.

### It cannot open my `.pbix`

Correct, and it never will — the file is binary. The working pattern all
afternoon is **copy the measure text out of Power BI, paste it into Claude, ask
your question, paste the answer back.** That is not a workaround; it is the job.

### It is confidently wrong about a column that does not exist

It is guessing because nothing told it otherwise. That is the entire point of
the `CLAUDE.md` you fill in during Session 3 — after which, ask it again.
