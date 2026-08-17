# Answers — 3 · Genie and Claude Code, side by side

**FACILITATOR ONLY. Never on screen.** Everything you present is in
`README.md` — read that with the room. This page is what you cannot show them.

Clock and ownership: `session-3/facilitator/run-sheet.md`.

## If you are behind

It runs 8 minutes against the 15 the client plan promised — say so if asked. If
the session is behind it shrinks to the table alone — one prompt, then the
table. It is here because Lucie raised Genie herself and answering her on day
one beats making her wait.

## What you do

**Say it before you start and again at the end:** we run this on *our*
Databricks, nobody needs access, nothing is required from Lucie's team. The
prerequisites letter deliberately promised no Databricks setup, so without this
someone will quietly assume they missed a step and spend the segment worrying.

Run the same question in both, on screen, in parallel windows, and narrate the
two things `README.md` tells them to watch — same number or not, and what each
one had to be told first. Then land the table.

The bridge line — *both of them answered by writing a query* — is what stops
this segment being a Databricks advert. Say it deliberately; it is the way into
part 4.

## How to assert

Nothing to run, so no readiness gate. The check is a question to the room:

> **"Which of the two would you reach for on the thing you just did in data
> quality, and why?"**

If the answer is "Genie, because it already knows the schema" — good, they have
it. If nobody can answer, the segment did not land, and the fix is the table on
screen for one more minute, not a longer demo.

## What goes wrong

**The workspace is slow, or the Genie space misbehaves.** **Have the recording
ready and use it without apology.** This segment must not eat the room's time —
it is the one part of Session 3 depending on a live external system, and it is
also the least load-bearing.

**It turns into a Databricks pitch.** Half of the room has no Databricks and is
not getting any. Keep returning to the table: this is about *which tool for
which question*, and one of the two answers works on their laptop today.

**Someone asks for Genie hands-on.** Good — park it for the close, where the
follow-up sessions get named. Do not improvise a session in the room.

## Before you release them — the break instruction, 30 seconds

The Power BI load is announced here. Say it before anyone stands up, and put it
in the meeting chat as well. The wording, the three questions people always ask,
and the pointer to `quirks.md` are all in `README.md` — read them from there.

## What goes wrong in the break — verified against Microsoft docs

The participant-facing version of all of this is in `quirks.md`. This is what
you need to recognise it quickly from across the room.

**Display scaling hides dialogs.** Documented, and the single most likely thing
to strand someone: above 100% text scaling, or below 1440×900, some Power BI
dialogs render partly off-screen and cannot be dismissed. If a person is stuck
on a dialog they cannot close, that is this — 100% scaling, or a second screen.

**Get data → Folder instead of five Text/CSV imports.** Power BI takes the
*first* file as the schema for all five, so they get a wrong union plus a
"column not found" error. Microsoft's own Text/CSV page recommends the Folder
connector for multiple files — it means *files with the same schema*, which is
not us. Start again with five separate imports.

**Every column arrives as Text.** Not a locale problem — it means type detection
is switched off on that machine. Options → Global → Data load → Type detection.

**A date column shows errors** (not Text — errors). Right-click the column
header → **Change type → Using locale** → Date, and pick the locale. Plain
"change type to Date" re-runs the same failing parse. Unlikely for us: the dates
are ISO `yyyy-mm-dd` and the machines are en-GB, which is the safe combination.
Type detection reads only the first 200 rows, so if it does appear it will be a
stray value deep in a 22,000-row file, not the whole column.

Encoding is not a risk here — all five CSVs were checked and are pure ASCII, so
nobody needs to touch **File Origin**.
