# Answers — 3 · Explain it

**FACILITATOR ONLY. Never on screen.**

Reused, near-verbatim, from the analytics stream's Session 4. Same five files,
same answers — the framing is different because this room has actually
maintained pipelines like it.

## The watermark question — let them get it, do not tell them

Run step 1 on screen. Claude reads all five files and explains the pipeline in
order. Then ask the dependency question.

The answer is **`Completed`, not `Succeeded`** — `Update Watermark` depends on
`DF_Enrich_Supporters` with `dependencyConditions: ["Completed"]`. The data flow
fails and the watermark advances anyway.

**Be careful how you state the consequence, because the obvious version is
wrong.** Nothing in this pipeline actually *reads* the watermark. `Lookup
Watermark` runs and no activity references its output. `Copy1` selects files by
`wildcardFolderPath: "supporters/@{formatDateTime(utcnow(), 'yyyy/MM/dd')}"` —
today's date, every time — and the sink is `truncate: true`, a full replace. So
the watermark cannot cause a skipped load.

**What it actually does is worse in a quieter way: the only record of when the
data last loaded successfully is now a lie**, and the first person to build
incremental loading on that table inherits a silent bug from 2024.

**If someone says "but nothing reads it" — that is the best possible outcome.**
They read the JSON rather than the explanation, which is the whole skill. Say so
out loud and give them the credit. This room is more likely to get there than
the analysts were; step 1's second prompt asks it directly for exactly that
reason.

## Answer key

### Tracing `value_band`

`aggGiving` sums `amount_gbp` per supporter → `deriveFlags` builds `value_band`
with a `case()` at 100 / 1,000 / 5,000 → `filterOut` **drops the row entirely**
if region is Northern Ireland or status is Deceased → `selectFinal` → sink,
which truncates and reloads.

Two things worth drawing out:

- The banding reads `dw.fact_donation` with **no refund filter**.
- Because `iifNull` defaults a blank status to `'Active'`, the "drop Deceased"
  filter never removes a record whose status was missing. **Two rules
  interacting, neither written down** — and this is the same class of thing as
  part 4's `Activ` typo, which is worth naming when you get there.

### "A supporter is missing" — the full list

Wrong folder date · truncate-then-failed-copy · schema drift · the Northern
Ireland filter · the Deceased filter · the `ForEach` race · the merge proc's own
`ExcludeRegion` parameter · a failed refresh serving an older dataset.

**Eight places.** By hand that is most of an afternoon, and it is the single
most persuasive number in the segment. Ask the room how long their version of
that list usually takes.

### Hardcoded values they should find

- `ExcludeRegion: "Northern Ireland"` — applied twice, documented nowhere
- **`Password=Wint3r2022!` in plaintext** in `linked_services.json`, while the
  linked service directly below it correctly uses Key Vault. This is the one
  that should not be in a file that lives in Git, and this room will react to it
- `Wait1`, 300 seconds, with a comment admitting it is a workaround
- The email address the `Wait1` comment is signed with
- Seven-day timeouts on activities that take minutes

### The gate answers

1. It advances anyway, and the watermark table starts lying — **though nothing
   downstream reads it**
2. Northern Ireland and Deceased
3. The plaintext password (or the Northern Ireland exclusion, or the 300-second
   `Wait1`)

## What goes wrong

**It only reads one file.** Say: *"read all five JSON files in
`later-days/adf/supporter_weekly/`, including the data flow script lines and the
datasets."* The data flow holds most of the logic and is the easiest to miss.

**The explanation is too shallow.** Push: *"explain it to someone who has to be
on call for it tonight."*

**Someone disagrees with Claude.** Excellent. Have them argue it in the
conversation, with their reason, and watch. A well-argued correction usually
gets a real reconsideration — and occasionally they turn out to be wrong. Both
outcomes are the exercise.

**Nobody finds the watermark thing.** Ask directly. It is worth the room seeing
it more than it is worth them discovering it.

**Somebody asks why we are reading a fundraising pipeline.** Because nobody in
the room built it, which is the only way to make the exercise honest — and
because it is far richer than the donor import: eleven activities against one.
Say that plainly rather than pretending it is theirs.

## Time

25 minutes, and it sits between the two hands-on parts. If part 2 overran, this
is the part to compress: **steps 1 and 3 are the segment**; step 2 can be cut to
the second prompt alone, and step 4 stated rather than run.
