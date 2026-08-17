#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["duckdb"]
# ///
"""Green check for Analytics Sessions 3 & 4.

Run this at the start of Session 3:

    uv run verify.py

It checks Python, DuckDB, and that all five CSVs are readable, then prints the
row counts. If every line says OK, you are ready.
"""

import sys
from pathlib import Path

EXPECTED = {
    "supporters.csv": 4022,
    "campaigns.csv": 192,
    "donations.csv": 12376,
    "campaign_activity.csv": 22591,
    "fulfilment_tasks.csv": 6000,
}

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"


def main() -> int:
    problems: list[str] = []

    if sys.version_info < (3, 11):
        problems.append(f"Python {sys.version.split()[0]} — 3.11 or newer needed")
    else:
        print(f"OK   Python {sys.version.split()[0]}")

    try:
        import duckdb
    except ImportError:
        print("FAIL DuckDB could not be imported.")
        print("     Run this with `uv run verify.py`, not `python verify.py` —")
        print("     uv fetches DuckDB for you.")
        return 1
    print(f"OK   DuckDB {duckdb.__version__}")

    for name, expected in EXPECTED.items():
        path = DATA / name
        if not path.exists():
            problems.append(f"{name} is missing from data/")
            print(f"FAIL {name} — not found")
            continue
        try:
            n = duckdb.sql(f"SELECT count(*) FROM '{path.as_posix()}'").fetchone()[0]
        except Exception as exc:  # noqa: BLE001 — we want the message verbatim
            problems.append(f"{name} could not be read: {exc}")
            print(f"FAIL {name} — {exc}")
            continue
        if n != expected:
            problems.append(f"{name} has {n} rows, expected {expected}")
            print(f"WARN {name} — {n} rows, expected {expected}")
        else:
            print(f"OK   {name} — {n} rows")

    print()
    if problems:
        print("Not ready yet:")
        for p in problems:
            print(f"  - {p}")
        print()
        print("Show us this output and we will sort it now.")
        return 1

    print("Green. Nothing else to do.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
