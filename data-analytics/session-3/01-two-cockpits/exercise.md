# Exercise — one question, two windows

**12 minutes.** 3 min we show the bad prompt · 4 min we fix it together · 4 min
you run it · 1 min pick your window and move on.

Have Claude open — terminal or desktop app, whichever you installed. If you have
both, open both.

---

## Step 1 — Watch a vague prompt underperform (~3 min, we drive)

We type this, on screen:

> tell me about the supporter data

You will get something fluent and close to useless: a description of the columns
with no numbers in it, or numbers with no query behind them, or a summary of a
file we did not ask about.

Nothing is wrong with Claude here. The question was vague, so the answer is.

## Step 2 — Fix it together (~4 min, out loud)

Same format as the prompt-tightening exercise in July, where the room supplied
the missing pieces. Four questions, and you answer them:

| | Question | |
|---|---|---|
| **Request** | What do we actually want it to *do*? | |
| **Target** | Which file, exactly? | |
| **Location / how** | What should it use to get the answer? | |
| **Actions** | What should it hand back? | |

Work it out as a room. You should end up somewhere close to:

> Profile `data/supporters.csv` using DuckDB SQL. For every column give me the
> row count, how many are blank, how many distinct values, and for the text
> columns the five most common values. Show me the SQL you ran, then the
> results.

Notice what it is not: no `<request>` or `<target>` tags. **Plain sentences.**
If you remember the angle-bracket style from July — it is a real technique, it
just earns its keep on prompts far longer than anything here. See
[`reference/prompt-patterns.md`](../../reference/prompt-patterns.md).

The clause doing the most work is the last one — *show me the SQL you ran*.
Four words, and they turn an answer you have to trust into one you can check.

## Step 3 — Run it, in your window (~4 min, you drive)

Type the tightened prompt into whichever cockpit you are using.

While you do, **we run the identical prompt in both** — one of us in the desktop
app, one in the terminal — on screen, side by side. Watch the two answers. They
will be the same answer, because it is the same Claude Code.

**What you should get:** **4,022** rows in `supporters.csv`.

If your number is different, say so now. It means you are not on the same data
as the rest of the room, and that is much cheaper to find out at 0:20 than at
11:30. This is exactly the failure the shared dataset exists to prevent.

**Keep this answer.** Part 2 starts from it.

## Step 4 — Pick your window (~1 min)

That is the whole comparison. Two windows, one Claude Code, same answer.

**Use whichever you will actually open.** If July's terminal clicked, stay
there — nothing this week needs the app. If the black screen was part of why it
did not stick, the app removes that and changes nothing else. Plenty of people
end up using both.

You do not have to decide permanently. You do have to pick one for the next
three hours.

---

## If it goes wrong

**The desktop app cannot find the file.** Wrong folder. It should be the one
containing `README.md` and `verify.py`. Reopen it there.

**It answers in Python instead of SQL.** Say *"use DuckDB SQL over the CSVs, not
pandas."* It will come up again in part 2, and part 4 is where we fix it
properly rather than repeating ourselves.

**It gives you a summary with no query.** Ask for the query. Every time. That is
tell 2 in [`reference/checking-the-answer.md`](../../reference/checking-the-answer.md)
— a number with no test named — and it is the habit the whole day rests on.

**Your row count is not 4,022.** Stop and tell us. Either the repo is stale, or
Claude read a different file. Both take a minute to fix now.
