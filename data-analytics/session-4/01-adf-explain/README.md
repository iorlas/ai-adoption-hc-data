# 1 — Explain it: what does this thing actually do?

**25 minutes, hands-on · Claude Code + Azure Data Factory pipeline definitions**

## The situation

`adf/` holds one pipeline. Eleven activities, a Mapping Data Flow, eight datasets,
three linked services, a weekly trigger. Last published November 2024 by someone
who has left. Its folder is `Legacy/Supporter`, it is annotated `do-not-touch`,
and one activity is called `Copy1`.

Nobody in this room has seen it before. That is on purpose — this is the exact
position you are in with the ones you inherited.

## What makes this possible without ADF

The pipeline is **JSON**. Claude reads JSON as well as it reads anything. So the
whole of today's ADF work happens on text files on your laptop: no factory, no
Azure connection, no permissions, nothing that could run by accident.

This is worth internalising because it generalises. Anything in your world that
is stored as text — pipeline definitions, DAX, M, SQL, config, YAML — is
readable. Anything stored as a binary or that lives only inside a GUI is not.
That single distinction tells you in advance which of your problems this will
help with.

## What "explain it" actually means

Not a summary. Four specific questions a maintainer needs answered:

1. **What is the order of operations, and what depends on what?** Including
   which dependencies are on success and which are not — that distinction is
   where the surprises live.
2. **Where does a given number come from?** Pick a column in the output table
   and trace it back to its source. This is the question you get asked when a
   figure looks wrong, and it is the one that takes half a day by hand.
3. **What decisions are baked in?** Filters, defaults, exclusions. Things
   somebody decided once, for a reason nobody remembers.
4. **What is the schedule and what happens if a run is missed?**

## The thing that will actually happen

Claude will give you a fluent, confident, mostly-correct explanation. Some of it
will be wrong, because it is inferring intent from JSON with no comments.

So the skill here is not getting the explanation. It is **interrogating it**:
picking the claims that matter and checking them against the JSON yourself. You
know what ADF activities do. You are the one who can tell whether the
explanation is right — Claude is doing the reading, not the judging.

→ **`exercise.md`**
