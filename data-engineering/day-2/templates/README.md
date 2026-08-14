# Reference example — a finished knowledge layer

This folder is **not** part of today's exercise. It is a complete, worked example of the knowledge layer
you build in Stage 04, on a **different** small project (a bookshop's orders warehouse) — deliberately a
different domain so it shows you the *shape* without handing you the answers to the donor-proc exercise.

Study it to see four things wired together, all pointers actually resolving:

1. **A good CLAUDE.md** (`example-orders/CLAUDE.md`) — thin: stack, pointers, hard rules, PII policy.
   Loaded on every prompt, so it holds no depth, only signposts.
2. **How documentation is linked** — CLAUDE.md points *into* `docs/`; nothing deep is inlined. The docs
   cross-reference the ADRs by number.
3. **How ADRs are stored** — `docs/decisions/` is a numbered log; each ADR records the decision *and* the
   rejected options, so nobody (human or a fresh Claude session) re-litigates a settled call.
4. **A reference implementation** — `docs/reference/` holds the canonical query pattern to copy, and it
   embodies the two ADRs so the decisions are visible in code.

**Copy the structure, not the content.** Your CLAUDE.md should be this thin; your `docs/` this
shallow-but-linked. (This example ships only the knowledge layer — the `sql/`, `models/` code dirs its
CLAUDE.md names are illustrative.)

```
example-orders/
  CLAUDE.md
  docs/
    data-dictionary.md
    glossary.md
    decisions/
      0001-money-as-minor-units.md
      0002-order-status-lookup-table.md
    reference/
      daily-revenue.sql
```

How this differs from Stage 04: there you fill *skeletons* on the donor repo and feel the build; here you
read a *finished* one end to end. Build first, then compare — same idea as the take-home best-practices.
