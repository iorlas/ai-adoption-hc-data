#!/usr/bin/env python3
"""Single source of truth for the running order and who does what.

    uv run facilitator/build-run-order.py

Writes:
  * the `## Clock` table inside every stage's facilitator.md
  * facilitator/run-order.md — the whole two days, plus a per-person view

FACILITATOR ONLY. Edit BEATS below, re-run, and both stay in step. Do not hand-
edit a clock table — it will be overwritten.

Roles, from the 2026-08-09 decision:
  DENIS   leads, explains, runs the games and the room decisions, works the floor
  MYKOLA  drives every practical demo on screen, from his Windows machine
  BOTH    both on screen at once (only once, in S3 stage 1)
"""

import re
from pathlib import Path

DENIS, MYKOLA, ROOM = "Denis", "Mykola", "The room"
ROOT = Path(__file__).resolve().parent.parent

# Whole stages belong to one person. No stage is shared, and nobody cuts in
# during someone else's block — if you have something to add, hold it for the
# handoff or the break. The other person is on the floor, unblocking, silent.
#
# What forces the split: Power BI Desktop is Windows-only and Databricks is
# Mykola's trial, so build-and-verify, Genie and the ML taster are his. Every
# other stage could go either way; these are the ones that cannot.
#
# (session, folder, title, start, owner, [(minutes, beat), ...])
BEATS = [
 (3, "00-opening", "Opening", 0, DENIS, [
   (3, "July in one sentence, and what the August call changed"),
   (2, "Shape of the day, the rhythm, \"stop us\"")]),
 (3, "01-prompt-refresher", "Setup, then the prompt refresher", 5, DENIS, [
   (6, "**Everyone clones and runs `verify.py`** — the repo was not sent ahead"),
   (2, "Two windows — **both open on your own machine**, no handover"),
   (3, "The shape: situation · question · task, and *you rarely need all three*"),
   (2, "**Game** — five prompt cards, call-and-response"),
   (4, "They run the real prompt; collect the row count — 4,022")]),
 (3, "02-data-quality", "Data quality", 22, DENIS, [
   (8, "Demo — steps 1–2, **including the deliberate `Activ` mistake**"),
   (17, "They repeat steps 1–3; Mykola on the floor, weighted to Lauren's team"),
   (5, "**Game** — keep it or bin it")]),
 (3, "03-genie-vs-claude-code", "Genie vs Claude Code (watch only)", 52, MYKOLA, [
   (2, "Framing — and that nobody needs Databricks access"),
   (3, "The same question into both, on our workspace"),
   (3, "**Game** — five questions, which tool would you reach for")]),
 (3, "BREAK", "Break", 60, ROOM, [
   (10, "Break — **and load the five CSVs into Power BI**, needed at 1:50")]),
 (3, "04-shared-definitions", "One definition, shared across the team", 70, MYKOLA, [
   (6, "Demo — steps 0–1, both numbers and the Power Query line on screen"),
   (12, "They work steps 1–2; Denis on the floor"),
   (5, "**Game** — where does this knowledge live"),
   (8, "**The decision, as a room** — four numbers on the whiteboard"),
   (9, "They write it up, steps 5a–5d")]),
 (3, "05-build-and-verify", "Build a report, then prove it is right", 110, MYKOLA, [
   (10, "Part A demo — model and two measures live in Power BI Desktop"),
   (15, "Part A — they build; Denis on the floor"),
   (6, "Part B demo — the copy-out / paste-back loop"),
   (19, "Part B — they interrogate and cross-check"),
   (5, "**Game** — what do you say to the stakeholder")]),
 (3, "06-close", "Close", 165, DENIS, [
   (10, "Retro — three questions, answers written down"),
   (5, "The practice ask before Tuesday")]),

 (4, "00-opening", "Opening", 0, DENIS, [
   (6, "Practice check-in — \"I did not get to it\" said *before* asking"),
   (3, "What we changed from last night's retro"),
   (4, "Frame the day, and the ADF boundary in Lucie's words"),
   (2, "Hand out `fallback/` quietly, while the room settles")]),
 (4, "01-adf-explain", "ADF — explain it", 15, DENIS, [
   (5, "Demo — step 1, then **the watermark question**, and let them get it"),
   (15, "They work steps 1–4; Mykola on the floor"),
   (5, "Share what you found")]),
 (4, "02-adf-document", "ADF — document it", 40, MYKOLA, [
   (5, "Demo — step 1, with the `[inferred]` instruction visible"),
   (20, "They work steps 1–4; watch for invented business reasons"),
   (5, "Share-back")]),
 (4, "03-adf-weak-spots", "ADF — find the weak spots", 70, MYKOLA, [
   (4, "Demo — step 1, and the re-rank-by-consequence correction"),
   (12, "They work; **the rules handover is called out loud**"),
   (4, "\"The worst one you found\"")]),
 (4, "BREAK", "Break", 90, ROOM, [(10, "Break")]),
 (4, "04-better-questions", "Asking better questions of your data", 100, DENIS, [
   (6, "Demo — one hypothesis, up to the change-my-mind step"),
   (24, "They work one hypothesis; **stop the room on the reversal**"),
   (5, "Share-back")]),
 (4, "05-ml-taster", "A first look at machine learning (watch only)", 135, MYKOLA, [
   (5, "What the data has to look like"),
   (13, "Building the table, and AutoML running"),
   (8, "**How you would know whether to believe it**"),
   (4, "The leakage demonstration")]),
 (4, "06-close", "Close", 165, DENIS, [
   (4, "Everyone writes their one sentence"),
   (6, "Retro across all four sessions"),
   (3, "The backlog — named, including MCP, and **get an answer**"),
   (2, "The feedback ask")]),
]


def hhmm(m: int) -> str:
    return f"{m // 60}:{m % 60:02d}"


def write_clock_tables() -> None:
    for session, folder, _title, start, owner, beats in BEATS:
        if folder == "BREAK":
            continue
        path = ROOT / f"session-{session}" / folder / "facilitator.md"
        if not path.exists():
            # Stages now carry README.md + answers.md; the clock lives only in
            # the run sheet and run-order.md. Nothing to inject here.
            continue
        rows = [f"**This whole stage is {owner}'s.** The other one is on the floor,",
                "unblocking, and does not cut in.", "",
                "| Clock | Min | Beat |", "|---|---|---|"]
        t = start
        for mins, beat in beats:
            rows.append(f"| {hhmm(t)}–{hhmm(t + mins)} | {mins} | {beat} |")
            t += mins
        table = "## Clock\n\n" + "\n".join(rows) + "\n"
        text = path.read_text(encoding="utf-8")
        # The block runs from "## Clock" through the last table row. The two
        # ownership lines sit between the heading and the table and are also
        # generated, so they have to be inside the match — matching the table
        # alone silently no-ops, which is how these went stale once already.
        new, n = re.subn(
            r"## Clock\n\n(?:(?!\|)[^\n]*\n)*(\|[^\n]*\n)+", table, text, count=1
        )
        if not n and "## Clock" in text:
            print(f"  ! clock not replaced in {path.name}")
        # The one-line header under the title carries the same numbers.
        total = sum(m for m, _ in beats)
        end = start + total
        new = re.sub(
            r"^\*\*\d+ min · \d+:\d\d–\d+:\d\d · \w+'s block",
            f"**{total} min · {hhmm(start)}–{hhmm(end)} · {owner}'s block",
            new,
            count=1,
            flags=re.M,
        )
        path.write_text(new, encoding="utf-8")
    print("no clock tables to write — stages are README.md + answers.md")


def blocks(session):
    """Merge consecutive stages with the same owner into one contiguous block."""
    out = []
    for s, folder, title, st, owner, bs in BEATS:
        if s != session:
            continue
        span = sum(m for m, _ in bs)
        if out and out[-1]["owner"] == owner:
            out[-1]["end"] = st + span
            out[-1]["stages"].append(title)
        else:
            out.append({"owner": owner, "start": st, "end": st + span, "stages": [title]})
    return out


def write_index() -> None:
    out = ["# Running order — who owns what",
           "",
           "**FACILITATOR ONLY. Generated — do not hand-edit.**",
           "Regenerate with `uv run facilitator/build-run-order.py`. The stage clock",
           "tables come from the same source, so they cannot drift from this page.",
           "",
           "## The rule",
           "",
           "**Whole stages belong to one person.** Nothing is co-presented and nobody",
           "cuts in during someone else's block. If you have something to add, hold it",
           "for the handoff or the break — the room hears one voice at a time, and each",
           "of you gets a long enough run to actually build something.",
           "",
           "The person not presenting is **on the floor**: unblocking, reading over",
           "shoulders, spotting who is stuck. That is a real job and it is silent.",
           "",
           "What forces the split: **Power BI Desktop is Windows-only and Databricks is",
           "Mykola's trial**, so build-and-verify, Genie and the ML taster have to be",
           "his. Every other stage could go either way.",
           ""]

    for session in (3, 4):
        out += ["---", "", f"# Session {session} — the blocks", ""]
        bl = blocks(session)
        out += ["| Clock | Min | Owner | Covers |", "|---|---|---|---|"]
        for b in bl:
            if b["owner"] == ROOM:
                out.append(f"| {hhmm(b['start'])}–{hhmm(b['end'])} | {b['end']-b['start']} | — | *Break* |")
                continue
            out.append(f"| {hhmm(b['start'])}–{hhmm(b['end'])} | {b['end']-b['start']} | "
                       f"**{b['owner']}** | {' · '.join(b['stages'])} |")
        hand = len([b for b in bl if b["owner"] != ROOM]) - 1
        out += ["", f"**{hand} handoffs.** Longest block: "
                    f"{max(b['end']-b['start'] for b in bl if b['owner'] != ROOM)} min.", ""]

        out += [f"## Session {session} — beat by beat", ""]
        for s, folder, title, st, owner, bs in BEATS:
            if s != session:
                continue
            if folder == "BREAK":
                out += [f"### {hhmm(st)} · Break", ""]
                continue
            span = sum(m for m, _ in bs)
            out += [f"### {hhmm(st)}–{hhmm(st + span)} · {title} — **{owner}**",
                    f"`session-{session}/{folder}/`", "",
                    "| Clock | Min | Beat |", "|---|---|---|"]
            t = st
            for mins, beat in bs:
                out.append(f"| {hhmm(t)}–{hhmm(t + mins)} | {mins} | {beat} |")
                t += mins
            out.append("")

    for person in (DENIS, MYKOLA):
        out += ["---", "", f"# {person} — your blocks", ""]
        for session in (3, 4):
            mine = [b for b in blocks(session) if b["owner"] == person]
            out += [f"## Session {session} — {sum(b['end']-b['start'] for b in mine)} min, "
                    f"{len(mine)} block{'s' if len(mine) != 1 else ''}", ""]
            for b in mine:
                out += [f"**{hhmm(b['start'])}–{hhmm(b['end'])}  ·  {b['end']-b['start']} min**",
                        ""]
                for st in b["stages"]:
                    out.append(f"- {st}")
                out.append("")
            other = [b for b in blocks(session) if b["owner"] not in (person, ROOM)]
            out += [f"On the floor for {sum(b['end']-b['start'] for b in other)} min "
                    f"— unblocking, not talking.", ""]

    out += ["---", "", "# Airtime", "", "| | Denis | Mykola | Break |", "|---|---|---|---|"]
    for session in (3, 4):
        bl = blocks(session)
        d = sum(b["end"]-b["start"] for b in bl if b["owner"] == DENIS)
        m = sum(b["end"]-b["start"] for b in bl if b["owner"] == MYKOLA)
        r = sum(b["end"]-b["start"] for b in bl if b["owner"] == ROOM)
        out.append(f"| Session {session} | {d} min | {m} min | {r} min |")
    out.append("")

    (ROOT / "facilitator" / "run-order.md").write_text("\n".join(out), encoding="utf-8")
    print("facilitator/run-order.md written")


if __name__ == "__main__":
    write_clock_tables()
    write_index()
