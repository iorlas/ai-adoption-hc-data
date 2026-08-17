# Setup — six minutes, and then we start properly

**▸ Everyone, right now.** The workshop folder did not go out ahead of today, so
we do it together at the start rather than assuming it happened.

Good news: it is public, it is one command, and there is nothing to install that
you were not already asked for.

## 1. Get the folder

```bash
git clone https://github.com/iorlas/ai-adoption-hc-data.git
```

If you already have it from earlier, get the latest instead — it has moved on:

```bash
cd ai-adoption-hc-data && git pull
```

## 2. Check it works

```bash
cd ai-adoption-hc-data/data-analytics
uv run verify.py
```

You want every line to say `OK`, ending with:

```
OK   supporters.csv — 4022 rows
...
Green. Nothing else to do before Session 3.
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
on the files. During the break, load the five CSVs from `data/` into Power BI
Desktop — Get Data → Text/CSV, five times — and you are ready for the afternoon.

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

**Everything works but the row count is not 4,022.** Stale copy. `git pull`.
