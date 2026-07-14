# CLAUDE.md best practices

> Read this **after** you've built your own CLAUDE.md + `docs/` today — compare what you did to it.
> Build-first, then calibrate; a checklist means more once you've felt the problem it prevents.

## The one idea

CLAUDE.md is loaded on **every** prompt — you pay for it on every message, and it shapes **everyone's**
sessions, not just yours. So the goal is not "put everything Claude should know in CLAUDE.md." It is:
**keep CLAUDE.md tiny — pointers and hard rules — and let the depth live in `docs/`, read on demand.**
That is progressive disclosure. A 400-line CLAUDE.md is a tax paid on every prompt for context most
prompts don't need.

## What goes where

| In CLAUDE.md (always loaded, keep tiny) | In `docs/` (read on demand) |
|---|---|
| Stack + where things live (pointers) | Full data dictionary, column ranges |
| Hard rules ("no cursors", "don't edit seed data") | Glossary of domain terms |
| PII / data-safety policy | ADRs (decisions + rejected options) |
| One-line pointers into `docs/` | Reference implementations (code to copy) |

If you're about to paste more than a few lines into CLAUDE.md, it belongs in a `docs/` file with a
one-line pointer instead.

## Rules of thumb

1. **Write for Claude first, humans second** — terse and concrete. Long, hedgy sentences dilute the
   signal and cost tokens. If you can't say it in a line, link a doc.
2. **Every edit is a shared blast radius.** CLAUDE.md is committed, so your change alters every
   teammate's sessions. That is its power *and* its risk — review CLAUDE.md changes like code.
3. **Pointers, not prose.** "Data dictionary: `docs/data-dictionary.md`" beats inlining the dictionary.
4. **Capture decisions as ADRs, not memory.** Without an ADR, a fresh session next week will happily
   re-propose the approach you already rejected. The ADR is what stops the loop. Point at `docs/decisions/`.
5. **Reference implementations must be owned.** A stale "best in show" file teaches the wrong pattern
   confidently. Update it the day the pattern changes, or delete the pointer.
6. **Stop writing giant prompts.** If you keep re-explaining the same context in prompts, that context
   wants to be a file. The good prompt you wrote twice is a `docs/` entry (or a skill).
7. **Never commit real PII.** Mask every sample in every doc — synthetic/redacted only.
8. **Follow the feedback loop.** When Claude can't find something, or repeats a rejected idea, that is
   the signal to add or restructure a doc. **Make a little mess first, then structure it** — don't try
   to design the perfect KB up front; grow it from where the tool actually stumbles.

## The measure of success

Over weeks, you should find yourself telling Claude **less** while it does the **same or more** — because
the context now lives in Git and compounds. That declining-instruction curve is how you know the
knowledge layer is working.
