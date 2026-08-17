# The inherited pipeline

Five JSON files. Together they are one Azure Data Factory pipeline that loads
supporter and campaign data into the warehouse every Monday at 02:00, and then
refreshes a Power BI dataset off the back of it.

| File | What it is |
|---|---|
| `pipeline_supporter_weekly_load.json` | The pipeline — eleven activities (twelve, counting the one inside the ForEach) |
| `dataflow_supporter_enrich.json` | The Mapping Data Flow it calls |
| `datasets.json` | The eight datasets it reads and writes |
| `linked_services.json` | The connections |
| `trigger_weekly.json` | The schedule |

**There is no documentation, and that is deliberate.** It was last published in
November 2024 by someone who has left. Its folder is `Legacy/Supporter` and it
is annotated `do-not-touch`. One activity is called `Copy1` and another is
called `Stored procedure1`. One has a comment that just says *"leave this in -
fixes the timing issue with the CRM pipeline (RB 2022)"*.

This is the shape you described: enormous, inherited, nobody in the room made
it, and the documentation is very weak.

## You do not need an ADF instance

This is the useful part. These are **text files**. Claude reads JSON perfectly
well, so everything in Session 4 — understanding it, documenting it, finding its
weak spots — happens without connecting to Azure, without a workspace, and
without touching anything that runs.

If you want to see it in the ADF interface, you can paste the JSON into a
factory later. Nothing today requires it.

## What Session 4 does not do

We are **not** moving your work out of ADF's interface, and we are not asking
you to hand-edit pipeline files as a way of working. You keep building the way
you build. Your words were *"it's not that we want to bypass using ADF, it's
that we want to make ourselves using ADF easier"* — this is that, and only that.
