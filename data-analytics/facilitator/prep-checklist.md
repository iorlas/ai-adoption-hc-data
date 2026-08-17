# Prep checklist — everything that must be true before Monday

**FACILITATOR ONLY.** Ordered by how much damage it does if it is missed.

## Blocking — the sessions do not work without these

- [x] **Prerequisites letter + Windows setup sheet sent, both teams confirmed**
      they would have it all working by Monday. Tools can be assumed present.
- [ ] **The repo and dataset were never sent and will not be** (decided
      2026-08-17). Consequences, all handled but all needing you to know them:
      setup is the first 6 minutes of stage 1; the two clone commands go in the
      meeting chat; **nobody has preloaded Power BI**, so that moves to the
      break; and `verify.py` green happens live rather than on Friday.
- [x] **Both teams replied and confirmed.** Tools assumed present. Still expect
      one or two IT-provisioning or install casualties on the day — three people
      on the DE stream were blocked in July and spent two days watching. Pair
      them instantly; the blocked person writes every prompt.
- [ ] **A memory stick with `data-analytics/` on it.** The likeliest single
      failure this morning is a proxy blocking `git clone`, and it turns one
      person into a spectator for three hours. Cheap insurance.
- [ ] **Nothing further is being sent** (decided 2026-08-17), so the two
      `reference/` pages cannot be pre-read. They are now in-session references —
      **point at them out loud** instead, especially
      `reference/checking-the-answer.md` during data quality. Sarah asked twice
      in July whether there was something written down; saying "yes, and it is in
      the folder you just cloned" is the answer.
- [ ] **Mykola's Windows machine**: Claude desktop app, Power BI Desktop,
      Python + `uv`, Git, the repo, and `verify.py` green.
- [ ] **The two `.pbix` files built and checked** — see
      `build-the-two-pbix.md`. Numbers must read 2,447 / £947,087.50 and
      1,832 / £930,092.50.
- [ ] **Full dry run of Session 3 stages 03, 04 and 05** — Mykola's, on Windows, timed, with
      the actual prompts from the exercise files. Segment 4 especially — a live
      Power BI stall in front of this room is expensive.
- [ ] **Full dry run of Session 4 stages 02 and 03** — Mykola's against `adf/`, confirming the
      five starred issues in the answer key are findable with the written
      prompts.

## Near-blocking — a segment degrades without these

- [ ] **Databricks workspace live**, with a **Genie space configured** over
      something resembling the supporter data.
- [ ] **The Genie comparison recorded as a fallback.** If the workspace is slow
      on the day, this segment must not eat the room's time.
- [ ] **AutoML example built and rehearsed**, with the leakage column ready to
      add live.
- [ ] **The Windows setup sheet validated end to end on a real Windows machine.**
      It has never been run by anyone. Three traps it claims to cover — the PATH
      checkbox, the App Execution Alias stub, and the PowerShell execution
      policy — are all untested as written.

## Worth doing

- [ ] Both facilitators have read both answer keys.
- [ ] Agree the cut-lines out loud, so that mid-session neither of you is
      deciding alone what to drop.
- [ ] Decide what to say about **MCP**. It was promised verbally to Lauren and
      Lucie on the August call at 44:12, and was never raised with AN IT. Either
      raise it this week or say plainly in Session 4's close that it is not
      happening yet. Do not let it sit.
- [ ] Confirm the dates with Bakhtior. The client offered to move 17–18 August
      (*"if we need to push it, let's push it"*) and a reply was promised early
      that week.

## Known and unmitigable

Write these down rather than being surprised by them:

- **Our Databricks is not their Databricks.** Catalogs, warehouse names and
  permissions differ. Both Databricks moments are watch-only precisely because
  of this, but do not narrate as though the room could follow along.
- **Lucie's team was never asked for their own real problems.** Session 3
  delivers her June asks wholesale (data quality was her #1, plus standardising
  queries and documentation), and the operational hypothesis in Session 4 is
  shaped for her team. Do not promise a Lucie-specific problem in the room that
  was never collected.
- **The room's literacy is uneven**, and the July friction was concentrated on
  Lauren's team, not spread evenly. Weight floor support accordingly.
