# Setup — six minutes, and then we start properly

**▸ Everyone, right now.** Three commands, and you are running. Everything you
were asked to install is already on your machine; nothing new goes on it today.

**Open the Git Bash terminal**, not PowerShell — in VS Code it is in the
dropdown next to the `+` at the top of the terminal panel. Everything in these
two days is written for it.

## 1. Get the folder

```bash
git clone https://github.com/iorlas/ai-adoption-hc-data.git
```

## 2. Check it works

```bash
cd ai-adoption-hc-data/data-analytics
uv run verify.py
```

Every line should say `OK`, ending with:

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
`verify.py`. Desktop app or terminal, whichever you installed; they are the same
tool and either is fine.

---

## Not until the break — Power BI

**You do not need Power BI until after the break.** Everything this morning runs
on the files. In the break:

1. **Open Power BI Desktop.** Dismiss the sign-in form if you get one — you do
   not need to sign in for anything today. If it opens on the Home screen rather
   than a blank canvas, choose **New → Report**.
2. **Home ribbon → Get data → Text/CSV**, pick one file from `data/`, then
   **Load**. Repeat for all five. Three minutes, and the files are small.
3. **Save it somewhere you will find again** — any folder on your own machine.

**No new workspace, and nothing to ask IT for.** Workspaces belong to Power BI
*Service*, which is for publishing reports to other people. We never publish
anything; everything you build is a file on your own laptop.

**Stop after loading.** No relationships, no date table, no measures — building
the model is the first thing we do together at 1:50, and doing it early means
redoing it.

We will remind you. Nothing before 1:50 depends on it.

---

## If anything misbehaves

→ **[`quirks.md`](../../quirks.md)** — every rough edge we know about, with the
fix. `uv` and DuckDB, network and proxy blocks, the Power BI sign-in prompt, the
dialog you cannot close, dates that come in wrong.

**If a fix does not work in thirty seconds, say so and pair with a neighbour.**
Nobody spends this morning watching. The blocked person writes the prompts.
