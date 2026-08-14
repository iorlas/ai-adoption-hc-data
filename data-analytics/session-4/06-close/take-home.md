# After Tuesday — the part that decides whether any of this mattered

Read part 1 now. Do part 2 over the next two to four weeks. Read part 3 only
after you have done part 2 — build first, compare second.

---

## Part 1 — what this actually looks like on a normal Tuesday

Not "AI does your analysis while you watch". Four sessions were building toward
a specific working style, and it is worth naming it in one place.

- **Picking something up.** You inherit a report, a query, a pipeline. Point
  Claude at it and ask what it does — then verify the answer with one cheap
  question rather than taking it on trust. Minutes, not an afternoon.

- **Doing the work.** You describe the outcome; Claude drafts the SQL, the DAX,
  the M. You read it before you keep it. The judgement stayed yours the whole
  time; the typing did not.

- **Hitting a real decision.** When you settle something — a definition, an
  exclusion, a rule — write it down once, where both your colleagues and the
  next conversation will find it. That is the difference between a decision and
  an opinion someone will re-litigate.

- **When Claude gets it wrong.** That is the signal, not the failure. A wrong
  answer usually means it was missing something a colleague would have known.
  Add that thing to `CLAUDE.md` or a document next to the work, and the next
  attempt is better — for everyone, not just you.

- **Verification is constant and cheap.** One question a wrong answer cannot
  survive. Show me the query. List the failing rows. Which data did you run
  against.

- **The measure, over weeks:** you find yourself telling it **less** while
  getting the **same or more** — because the context now lives in your files.
  That declining-instruction curve is the whole point, and it is the only real
  test of whether this stuck.

---

## Part 2 — the task, on your own work

Over the next two to four weeks, on **one** report or pipeline you actually
maintain:

1. **Explain it.** Ask Claude what it does; verify the answer.
2. **Do one real thing** with it — a measure you would have written by hand,
   documentation that does not exist, a cross-check you have been putting off.
3. **When Claude stumbles** — wrong answer, missing context, or it re-proposes
   something you already rejected — capture what it was missing into a short
   `CLAUDE.md` plus one document. Then re-run and watch it improve.
4. **Note the before and after.** Same question, before your `CLAUDE.md`
   existed and after.

That fourth step is the whole exercise. Everything before it is setup.

### Because this is real data now

The synthetic rule stops applying here, so:

- **Claude reads your code and your schema, not your rows.** When it answers a
  question about data, it does it by writing a query that runs on your machine.
  Keep it that way.
- **Anything that lands in a document is masked.** Never a real supporter's
  name, email or record in a file you commit or share.
- **You can see everything it opened.** That is your audit trail; it is worth
  glancing at.
- Follow whatever your own governance says. Nothing here overrides it.

---

## Part 3 — read this after, not before

Compare what you built against these.

**`CLAUDE.md` is read on every message.** So keep it short — pointers and hard
rules, nothing with depth. A four-hundred-line `CLAUDE.md` is a tax paid on
every prompt for context that is mostly irrelevant to the question at hand. If
yours is longer than a page, the depth has leaked in.

**Depth goes one pointer away**, in a document read on demand. Definitions,
dictionaries, pipeline documentation.

**Decisions go in their own records**, with the options you rejected. Without
the rejected options it is an assertion, and it will be re-argued.

**Write for two readers at once.** Everything you write for a colleague is also
context for every future conversation. That is not a happy accident — it is the
reason this compounds instead of being one more documentation task nobody does.

**A wrong answer is a missing-context report.** Treat it as a bug in your files
rather than a flaw in the tool, and the files get better every time.

There is a worked example of all four in `templates/example-library/`.

---

## The one ask

**Tell us in two to four weeks what did and did not work.**

Honestly: we can tell whether a session went well in the room. We cannot tell
whether it was **worth your time** until you have tried to use it on a Tuesday
afternoon with something actually due.

"I have not used it once" is a real answer and a useful one. It is more useful
than silence, and considerably more useful than politeness.
