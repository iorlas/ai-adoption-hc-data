# Reference implementation — "this is what good looks like"

A reference implementation is a **canonical example you point new work at** so Claude copies your
pattern instead of inventing its own each time. Today's: the **refactored** donor-report proc — cursor
replaced by a set-based join, `SELECT *` made explicit, age fixed per ADR 0001.

## How to register one

1. Put the exemplar **code** in `docs/reference/` (e.g. `docs/reference/donor-report-proc.sql`).
2. Add a one-line pointer to it here and from `CLAUDE.md`, saying *what pattern it demonstrates*:

| Pattern | Exemplar | Use it when |
|---|---|---|
| Set-based reporting proc (no cursors) | `docs/reference/donor-report-proc.sql` | writing or refactoring any reporting proc |
| ... | ... | *(add yours)* |

## The maintenance rule (say it out loud)

A reference implementation **degrades the moment it drifts from reality.** A stale "best in show" file
teaches Claude — and every new joiner — the *wrong* pattern, confidently. Own it: when the pattern
changes, update the exemplar the same day, or delete the pointer. An unmaintained reference is worse
than none.

<!--
FILL ME: ask Claude to produce the refactored proc (set-based, explicit columns, ADR-0001 age fix),
save it under docs/reference/, and add the pointer row above + a line in CLAUDE.md.
-->
