# Two reports that disagree

Two Power BI reports, built by different people at different times, both
reporting **active supporters** and **total income** off the same data. They do
not agree, and neither of them is lying.

| Report | Who owns it | Active supporters | Total income |
|---|---|---|---|
| `fundraising-summary/` | Fundraising | 2,447 | £947,088 |
| `supporter-engagement/` | Supporter Care | 1,832 | £930,093 |

This is the situation Lucie described: the last thing she does before a
dashboard goes live is hunt the service for other dashboards carrying the same
measure, to check the numbers match. And the situation Lauren described with
"active members" across bespoke dashboards.

Session 3 works this to the bottom: find where they differ, decide which
definition you actually want, write it down where both Claude and your
colleagues will find it.

## What is in each folder

- **`model.md`** — how that report is built: the tables, the relationships, the
  filters applied at the model level, and what the person who built it was
  trying to show.
- **`measures.dax`** — the DAX measures, as text.

## Why not `.pbix` files?

Because Claude cannot read one. A `.pbix` is a binary — Claude can open a text
file and reason about it, but a `.pbix` is a zip of compressed model data, and
pointing Claude at one gets you nothing useful.

This is a real boundary and it is worth knowing precisely where it sits:

| Claude can read | Claude cannot read |
|---|---|
| DAX measures, as text | The `.pbix` itself |
| Power Query M, as text | Your report canvas — the visuals, the layout |
| A model description you write or export | Anything you have not shown it |

So the working habit is: **copy the measure out, ask about it, paste the answer
back.** It sounds primitive. It is also the whole of what makes Claude useful on
Power BI work, and the reason these two folders are markdown and `.dax` rather
than two `.pbix` files.

If you are thinking *"but July said a dashboard is text you can diff"* — you
remembered correctly, and it is squared off properly in
`session-3/04-build-and-verify/README.md`. Short version: that was PBIP, PBIP is
real, you are on `.pbix` today, and nobody is asking you to migrate.

Your facilitators will also have both reports open in Power BI Desktop, so you
can see the actual visuals as we go.
