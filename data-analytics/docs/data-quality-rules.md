# Data-quality rules

<!--
SKELETON — you fill this in Session 3, part 2.

The headings are here so you are editing rather than starting. Keep the
"Rejected" section: it is the more interesting half, and it is what stops this
document becoming thirty rules nobody reads.
-->

> What a violation of each rule means, and the SQL that finds it. A rule belongs
> here only if breaking it means the data is **wrong for how we use it** — not
> merely different from how someone would have typed it.

**Last reviewed:** _(date)_ · **Owner:** _(team)_

## Rules we keep

| # | Table | Rule | SQL predicate | Failing now | Why it matters |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |

<!--
Six is a good target. If you have twenty, you have a list nobody will read;
if you have two, you probably have not looked at the donations table.

Ask Claude to fill this from what it found, then delete what does not survive
the test above. The deleting is the exercise.
-->

## Rules we rejected, and why

A rule that fires on healthy data is worse than no rule — it trains everyone to
ignore the alerts. These were proposed and thrown out on purpose.

| Proposed rule | Why it is noise |
|---|---|
| | |
| | |
| | |

## Things that look like defects and are not

<!--
Different from the section above: these are real properties of the data that a
newcomer will mistake for problems. Worth writing down once so nobody
re-discovers them every quarter.
-->

-
-

## What we are not checking yet, and should

<!-- Honest gaps. Better here than implied by omission. -->

-
