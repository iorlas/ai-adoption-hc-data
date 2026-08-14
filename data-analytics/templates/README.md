# A finished knowledge layer, in a different organisation

`example-library/` is **not** an exercise. It is a complete, worked version of
the thing you build across Sessions 3 and 4 — for a public library service
rather than a charity, deliberately, so it shows you the *shape* without handing
you the answers to this week's questions.

**Read it after you have built your own, not before.** Build first, compare
second. That order matters: comparing a thing you made against a finished
example teaches something; copying a finished example teaches nothing.

## What to look at

Four things wired together, with every pointer actually resolving:

```
example-library/
  CLAUDE.md                     ← thin. Pointers and hard rules only
  docs/
    measure-definitions.md      ← the depth lives here
    data-quality-rules.md       ← kept AND rejected
    decisions/
      0001-overdue-in-open-days.md
      0002-renewals-are-separate-loans.md
```

1. **`CLAUDE.md` is short enough to read in under a minute.** That is the
   target. It is loaded on every message, so it carries signposts, not content.
2. **The definitions document holds the depth**, and `CLAUDE.md` points at it.
3. **Two decision records**, each naming what was rejected and why. Notice that
   both exist because *two reports disagreed about a number* — the same shape as
   your Monday.
4. **Every document says when it was last reviewed and who owns it.** Cheap, and
   it is the difference between a document people trust and one they suspect.

## The thing worth noticing

Both library decisions come down to the same sentence you will end up writing:

> The problem was never that there were two definitions. It was that there were
> two definitions with the same name.

Different organisation, different data, identical failure. It is close to
universal, which is why it is worth having a process for rather than an opinion
about.
