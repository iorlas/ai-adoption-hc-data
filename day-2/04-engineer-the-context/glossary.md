# Glossary — domain terms

> Terms Claude can't infer from code, and vocabulary it might "helpfully" flag as wrong when it isn't.
> One line each. This is the cheapest, highest-leverage doc you own — it stops a whole class of
> confident-but-wrong answers.

| Term | Means |
|---|---|
| **locus** (pl. loci) | A position on the genome that gets HLA-typed. `loci_typed` = how many distinct ones a donor has. |
| **workup** | The clinical work-up of a matched donor before donation (`dbo.workup`). |
| **match_result** | A record that a donor came up as a potential match for a patient search. |
| **HLA** | Human Leukocyte Antigen — the tissue-type system donors are matched on. |
| ... | *(add the terms your team uses that an outsider — or Claude — would not know)* |

## Not-a-typo rules

Vocabulary that looks wrong but is intentional — tell Claude so it stops "fixing" it:

- *(example)* **`registry_id` prefix `AN`** is deliberate, not a stray — do not "normalise" it away.
- *(the Day-1 war story: a `Drag Race` campaign name once got mistyped-flagged as `Drug Race`; a single
  glossary line would have prevented the false legal alarm. Add yours.)*

<!--
FILL ME: ask Claude "what terms in this repo would an outsider not understand?" then correct and trim.
Keep each entry to one line. Terse beats complete.
-->
