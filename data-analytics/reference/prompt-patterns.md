# Writing the prompt

## The shape that is usually enough

Most working prompts are some combination of three things:

| | | |
|---|---|---|
| **Situation** | What is going on, and what it should look at | *"I have a supporter export in `data/supporters.csv`"* |
| **Question** | What you actually want to know | *"which columns have values that don't belong?"* |
| **Task** | What you want it to do, or hand back | *"write the SQL, run it, show me both"* |

Three parts, plain sentences, no notation.

## You do not need all three

This is the part worth internalising, because the instinct is to fill in every
box every time.

- **Situation is free when it can already see it.** If the file is in the
  project and the name is obvious, do not describe it. *"How many rows in
  `supporters.csv`?"* is a complete prompt.
- **Question and task are often the same sentence.** *"Show me every distinct
  status with its row count"* is both at once. Splitting them would be padding.
- **A short prompt is not a lazy prompt.** *"What does this pipeline do?"* is a
  genuinely good prompt when the pipeline is the only thing in the folder.

**Add a part when the answer came back wrong in a way that part would have
prevented.** That is the whole rule, and it is worth more than any template.

## The fuller anatomy, for when a prompt is not working

In July we took a prompt apart into four named pieces — **request · target ·
location · actions**. That is the complete anatomy, and it is what to reach for
when a prompt keeps producing the wrong *shape* of answer:

| Part | The question it answers | You are missing it when… |
|---|---|---|
| **Request** | What am I asking it to do? | the answer wanders |
| **Target** | On what, exactly? | it answered about the wrong thing |
| **Location** | Where, or by what means? | it wrote Python and you wanted SQL |
| **Actions** | What should come back? | you got prose instead of a query |

**It is a diagnostic, not a template.** Filling in all four for a question you
could have asked in eight words makes the prompt longer and the answer no
better. Reach for it when something is going wrong, not by default.

## Four moves that carry these two days

### 1. Ask for the working, not just the answer

> *"…show me the SQL you ran, then the result."*

The highest-value clause in the workshop. It turns an answer you have to trust
into one you can check, and it costs six words.

### 2. Ask what it assumed

> *"Before you answer, tell me what in this data could make this result
> misleading."*
>
> *"List every decision you made that I did not ask for."*

Changes the answer materially. Worth running a question once with and once
without, just to see the size of the difference.

### 3. Make it separate fact from inference

> *"Mark anything you inferred rather than read directly from the files with
> [inferred]."*

For anything undocumented — a pipeline, someone else's report, an inherited
query. A confident explanation of undocumented work is **partly guesswork,
always.** This makes the guesswork visible rather than pretending to remove it.

### 4. Name the boundary

> *"Do not change anything else in the file."*
>
> *"Use SQL over the CSVs, not Python."*
>
> *"If a term is ambiguous, ask rather than choosing a definition for me."*

The third is worth having permanently. It converts a silent wrong assumption
into a question.

## When a rule belongs somewhere other than the prompt

If you find yourself typing the same constraint every time, it does not belong
in the prompt — it belongs in `CLAUDE.md`, where it applies to every
conversation your whole team has.

Session 3 does exactly that with your measure definitions. What belongs there
and what does not:
[`where-knowledge-lives.md`](where-knowledge-lives.md).
