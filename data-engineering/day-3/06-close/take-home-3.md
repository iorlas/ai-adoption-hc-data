# Take-home 3 — one of your own flows

Twenty minutes if you pick a small one. Do it on a Mapping Data Flow you
actually maintain.

## The task

1. **Point Claude at the flow's JSON.** Ask it to walk the transformations in
   order, and verify the walk against `scriptLines` yourself. As on Day 1: do
   not take the description on trust.

2. **Sort it into the three buckets** from part 5:
   - **(a)** converts to a view cleanly
   - **(b)** converts, but something is lost — say what
   - **(c)** no equivalent in a view — say what you would build instead, and
     where it would run

3. **Write the one-line verdict.** *"This flow is 80% bucket (a); the upsert and
   the surrogate key need a MERGE and a sequence on the target."* That sentence,
   for one flow, is the unit a migration plan is built from.

4. **Note anything the conversion would inherit.** Part 5 had twenty rows
   silently dropped by a filter written years ago. Yours will have something
   too. Log it as its own item — do not fix it inside the conversion.

## If you want the longer version

Do all of your flows, not one. Ask Claude to produce the bucket table across the
whole folder, then **spot-check three of them by hand.** The spot-check is the
work; the table is just the output.

That is the deliverable that makes a bulk-conversion estimate credible, and it
is a morning, not a project.

## What to bring back to Day 4

**Not your JSON, not your data, not your code.** Bring:

- the bucket counts (how many flows, what fraction is bucket (a))
- the most surprising bucket-(c) item you found
- one sentence on what Claude got wrong about your flow

That is enough to compare, and nothing sensitive leaves your machine.

## Governance, since this is real now

- **Code, not rows.** An ADF JSON is code. Keep it that way — do not paste
  sample data in to "help it understand."
- **Mask before it is written down.** If a `docs/` page needs an example value,
  invent one.
- **You can see what it read.** That list is your audit trail.
