# Writing the prompt — building on what you already have

In July you took apart the anatomy of a prompt: **request · target · location ·
actions**. Lucie played it back accurately, and the group's best twenty minutes
of the two days was tightening a prompt together, out loud, with Declan naming
the project type, Lucie naming the actions block and Sarah naming the path.

That vocabulary is still the vocabulary. This page is just it, applied to the
work in front of you — and with one thing dropped.

## The notation from July, and why it is gone

In July the four parts were written inside angle-bracket tags, like this:

```xml
<request>profile this file and tell me what is wrong with it</request>
<target>data/supporters.csv</target>
<location>use DuckDB SQL over the CSV</location>
<actions>show me the SQL, then the results</actions>
```

That is what the "brackets" were. The session stopped over it — *"you were using
brackets and specific commands, none of which I recognise"* — and nobody used it
afterwards.

**To be fair to it: the technique is real.** Tagging the parts of a prompt is
genuinely useful, and Anthropic recommend it, once a prompt gets long — several
paragraphs of background, a document pasted in, half a dozen instructions. The
tags stop the model losing track of which part is the instruction and which is
the material.

**And it is not what you need here.** Nothing in these two sessions is that
long. Every prompt in every exercise is one to three plain sentences, and at
that length the tags add typing and subtract nothing. So: same four parts, no
tags.

If you ever do find yourself writing a genuinely long prompt — a whole report
specification, or a document you want analysed against a checklist — the tags
are there and they work. That is a different day.

## The four parts, in a sentence

> *"**Profile** `data/supporters.csv` **using DuckDB SQL** — for every column
> give me the row count, blanks, distinct values and the five most common values.
> **Show me the SQL, then the results.**"*

| Part | In that prompt |
|---|---|
| **Request** | profile |
| **Target** | `data/supporters.csv` |
| **Location / how** | using DuckDB SQL |
| **Actions** | show me the SQL, then the results |

Drop any one and the answer gets worse in a predictable way. Drop the actions
and you get prose instead of a query. Drop the location and it writes Python.
Drop the target and it guesses which file you meant.

## Four patterns that carry these two days

### 1. Ask for the working, not just the answer

> *"…show me the SQL you ran, then the result."*

The single highest-value four words in the workshop. An answer you cannot see
the working for is not an answer you can defend.

### 2. Ask what it assumed

> *"…before you answer, tell me what in this data could make this result
> misleading."*
>
> *"List every decision you made that I did not ask for."*

Changes the answer materially. Try one question with it and without it once —
the difference is the exercise.

### 3. Make it separate fact from inference

> *"Mark anything you inferred rather than read directly from the files with
> [inferred]."*

For anything undocumented — a pipeline, someone else's report, an inherited
query. A confident explanation of undocumented work is **partly guesswork,
always**. This makes the guesswork visible instead of removing it, which is the
honest version.

### 4. Name the boundary

> *"Do not change anything else in the file."*
>
> *"Use SQL over the CSVs, not Python."*
>
> *"If a term is ambiguous, ask rather than choosing a definition for me."*

Constraints are the July "rules and guardrails" idea. The third one is worth
having permanently — it turns a silent wrong assumption into a question.

## Where a rule should live instead of a prompt

If you find yourself typing the same constraint every time, it does not belong
in the prompt. It belongs in `CLAUDE.md`, where it applies to every conversation
your whole team has.

Session 3 does exactly that with your measure definitions.
See `reference/where-knowledge-lives.md` for what belongs there and what does
not — the answer is "less than you think".
