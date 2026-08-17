# Setup — six minutes, and then we start properly

**▸ Everyone, right now.** The workshop folder did not go out ahead of today, so
we do it together at the start rather than assuming it happened.

Good news: it is public, it is one command, and there is nothing to install that
you were not already asked for.

## 1. Get the folder

```bash
git clone https://github.com/iorlas/ai-adoption-hc-data.git
```

If you already have it from earlier, `cd` into wherever you put it and get the
latest instead — it has moved on:

```bash
git pull
```

If that stops with *"your local changes would be overwritten"*, you have edited
something. Park the edits, pull, put them back:

```bash
git stash && git pull && git stash pop
```

**On Windows, use the Git Bash terminal** — in VS Code it is in the terminal
dropdown. Everything today is written for it, and a couple of commands behave
differently in PowerShell.

## 2. Check it works

```bash
cd ai-adoption-hc-data/data-analytics
uv run verify.py
```

You want every line to say `OK`, ending with:

```
OK   supporters.csv — 4022 rows
...
Green. Nothing else to do.
```

**Say the number out loud when you get it: 4,022.** If yours is different, or
anything says FAIL, tell us now — not at eleven o'clock. That number is the
whole reason everyone works from the same data.

## 3. Open it in Claude

Point Claude at the `data-analytics` folder — the one containing `README.md` and
`verify.py`. Terminal or desktop app, whichever you installed; they are the same
tool and either is fine.

## Not until the break — Power BI

**You do not need Power BI until after the break.** Everything this morning runs
on the files. In the break:

1. **Open Power BI Desktop.** If it offers you a sign-in form, dismiss it — you
   do not need to sign in for anything today. If it opens on the Home screen
   rather than a blank canvas, choose **New → Report**.
2. **Home ribbon → Get data → Text/CSV**, pick one file from `data/`, then
   **Load** (not Transform Data). Repeat for all five. Three minutes, and the
   files are small.
3. **Save it somewhere you will find again** — File → Save, any folder on your
   own machine. If the save dialog offers **Power BI Project (.pbip)**, choose
   **Power BI report (.pbix)**.

The report itself is made in the Power BI window, not in a text editor — a
`.pbix` is a binary file and nothing else can create one.

**No new workspace, and nothing to ask IT for.** Workspaces are a Power BI
*Service* thing — for publishing a report so other people can see it. We never
publish anything; every report you build lives as a file on your own laptop. You
do not need to sign in to Power BI for any of it.

**Stop after loading.** No relationships, no date table, no measures — building
the model is the first thing we do together at 1:50, and doing it early means
redoing it.

We will remind you. Nothing before 1:50 depends on it.

---

## If something fails

**`git` not found.** It was on the prerequisites list. Pair with a neighbour for
now and we will sort it at the break — you lose nothing this morning by working
on one machine between two.

**`uv` not found.** Same. Pair up.

**`uv run verify.py` cannot find DuckDB.** Make sure it is `uv run verify.py` and
not `python verify.py` — `uv` fetches DuckDB for you, plain Python will not.

**A proxy or IT block stops the clone.** Tell us immediately. We have the folder
on a memory stick and can hand it over — this is not a reason to spend the
morning watching.

**`SSL certificate problem: unable to get local issuer certificate`.** Your
network inspects encrypted traffic and the tools do not know its certificate.
Tell us — the same thing will stop `uv`, and there is a one-line fix for both.

**Everything works but the row count is not 4,022.** Stale copy. `git pull`.
