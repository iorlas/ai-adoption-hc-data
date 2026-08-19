# Two inherited pipelines

Neither of these came from your team, and that is the point — this is the
position you are in with most of the ADF in your estate.

## `donor_import/` — the small one, the one you convert

Two files. A weekly Mapping Data Flow that loads a donor CSV export into the
`donor` table: standardise, filter, look up an ethnicity code, generate a key,
upsert. The interesting logic is entirely in `scriptLines`.

**Day 3 part 4 converts it to SQL, with a parity check.**

## `supporter_weekly/` — the big one, the one you read

Five files, and it belongs to the fundraising side rather than to you. Eleven
activities (twelve, counting the one inside the `ForEach`), a Mapping Data Flow,
eight datasets, three linked services, a weekly trigger at 02:00 Monday.

**There is no documentation, and that is deliberate.** Last published November
2024 by someone who has left. Its folder is `Legacy/Supporter`, annotated
`do-not-touch`. One activity is called `Copy1` and another `Stored procedure1`.
At least one carries a comment written by somebody who knew they were leaving a
problem behind.

**Day 3 part 3 reads it.**

| File | What it is |
|---|---|
| `pipeline_supporter_weekly_load.json` | The pipeline |
| `dataflow_supporter_enrich.json` | The Mapping Data Flow it calls |
| `datasets.json` | The eight datasets it reads and writes |
| `linked_services.json` | The connections |
| `trigger_weekly.json` | The schedule |

## You do not need an ADF instance for either

They are **text files**, and Claude reads JSON as well as it reads anything.
Understanding them, documenting them and converting them all happen with no
Azure connection, no factory, and nothing that could run by accident.

This generalises, and it is the sentence worth keeping: **anything in your world
stored as text is readable — pipeline JSON, DAX, M, SQL, YAML, Terraform.
Anything binary, or living only inside a GUI, is not.** That distinction tells
you in advance which of your problems AI will help with.
