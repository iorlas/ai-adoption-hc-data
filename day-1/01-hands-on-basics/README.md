# Section 1 — Hands-on basics (0:00, ~60 min)

**Goal of this hour:** everyone leaves with **Claude Code working locally** on this
repository and a database, doing plain file- and-shell work on real
data-engineering artifacts. No slides. If your setup is not fully green, this is
the hour we fix it, so speak up early.

Everything here needs only **Python + pandas** (and the repo). No Azure, no
Databricks, no cloud today.

## The four things you will do

### 1. Confirm the tool is working
In your terminal, in the repo root:
```bash
claude --version      # prints a version
uv sync               # one-time: installs pandas + jupyterlab into .venv
uv run verify.py      # green = Python, pandas, and the data are all in place
```
If `verify.py` is green, you are ready. If not, flag it now.

### 2. Open a notebook
Either in JupyterLab:
```bash
uv run jupyter lab 01-hands-on-basics/explore.ipynb
```
Or in **VS Code**: open this folder, open `01-hands-on-basics/explore.ipynb`, click
**Select Kernel** (top-right) -> **Python Environments** -> pick **`.venv`**. If it
is not listed, run `Cmd/Ctrl-Shift-P` -> **Python: Select Interpreter** ->
`./.venv/bin/python`, then select the kernel again. (Needs the Python + Jupyter
extensions; `.venv` comes from `uv sync`.)

Run the first two cells (load + `head`). This is your working notebook for the
day; you will come back to it in Section 3.

### 3. Read a stored procedure
Open `01-hands-on-basics/stored_procedure.sql` and ask Claude Code, in plain
English: *"explain what this procedure returns and how."* You are only **reading**
here, not running it. Notice how fast the tool makes unfamiliar SQL legible, then
stay sceptical: does its explanation actually match the code?

### 4. Run a query
Back in the notebook, run the **"Run a query"** cell (cell 1b). It loads the exact
same donors into a database (`../data/donor.db`, a SQLite file, nothing to
install) and counts them by `status`. Change the query: filter to
`status = 'Active'`, count by `ethnicity`, whatever you like.

> You will notice `status` has an odd value in it. Hold that thought. We come back
> to why that matters in Section 3.

## Keep going — direct Claude Code at real work

The four steps above just get the tool running. The rest of the hour is for building the core habit:
**work in the terminal, direct Claude Code to do a task, then run what it produces and check it.** Do
as many of these as time allows; you do not need to finish them all. Everything is local (just
`data/donor.csv` and `data/donor.db`).

**Get oriented**
- *"Summarise every file and folder in this repo and what each one is for."*
- *"Describe each column in `data/donor.csv`: what it holds and its likely valid values."*

**Query, then translate** (a genuine strength of AI: bounded translation between formats)
- *"Write and run a SQL query against `data/donor.db` that counts donors by `status` and `ethnicity`. Show me the query you ran."*
- *"Now give me the equivalent in pandas and run it. Do the numbers match?"* — then confirm they match.

**Scaffold and run**
- *"Write a short Python script `top_postcodes.py` that prints the 10 most common postcodes in `data/donor.csv`, then run it."* Open the script and read it before you trust the output.
- *"Add a cell to `explore.ipynb` that tabulates registrations per year."* Then run the cell yourself.

**Explain unfamiliar code** (another strength)
- *"Explain `stored_procedure.sql` step by step, in plain English."* Then push on it: *"what is one thing about it you're unsure of?"*

**Finish every task the same way — verify.** Open the rows, re-run the number, or read the code Claude
wrote. If you cannot check it, you have not checked it. That reflex is the whole point of the week.

## You are done with this hour when

- `claude --version` and `uv run verify.py` are both green,
- you have opened the notebook and run a query, and
- Claude has explained the stored procedure to you.

That is the whole bar: **the tool works locally, on real DE artifacts.**
