"""
Green check.

Day 1 (local files):        uv run verify.py
Day 2+ (MSSQL ready):       uv run --with pyodbc verify.py --conn "<connection string>"

Day 1 needs only Python + pandas + data/donor.csv + data/donor.db. The --conn
checks come later in the week once the shared MSSQL database exists.
"""
import argparse
import sys
from pathlib import Path

OK = "\033[92mOK\033[0m"
FAIL = "\033[91mFAIL\033[0m"

HERE = Path(__file__).resolve().parent


def day1_check() -> int:
    problems = []

    if sys.version_info < (3, 11):
        print(f"[{FAIL}] Python {sys.version.split()[0]} (need 3.11+)")
        problems.append("python")
    else:
        print(f"[{OK}] Python {sys.version.split()[0]}")

    try:
        import pandas as pd
        print(f"[{OK}] pandas {pd.__version__}")
    except ImportError:
        print(f"[{FAIL}] pandas not importable (run with: uv run setup/verify.py)")
        return 1

    csv = HERE / "data" / "donor.csv"
    if not csv.exists():
        print(f"[{FAIL}] data/donor.csv missing")
        problems.append("data")
    else:
        df = pd.read_csv(csv, dtype=str, keep_default_na=False)
        if len(df) > 4000:
            print(f"[{OK}] data/donor.csv loads: {len(df)} rows, {df.shape[1]} columns")
        else:
            print(f"[{FAIL}] data/donor.csv only {len(df)} rows (expected ~5000)")
            problems.append("data")

    db = HERE / "data" / "donor.db"
    if not db.exists():
        print(f"[{FAIL}] data/donor.db missing")
        problems.append("db")
    else:
        import sqlite3
        n = sqlite3.connect(db).execute("SELECT COUNT(*) FROM donor").fetchone()[0]
        if n > 4000:
            print(f"[{OK}] data/donor.db query works: {n} rows in donor")
        else:
            print(f"[{FAIL}] data/donor.db only {n} rows (expected ~5000)")
            problems.append("db")

    print()
    if problems:
        print(f"{FAIL}: {len(problems)} issue(s). See messages above.")
        return 1
    print(f"{OK}: ready for Day 1. Start with 01-hands-on-basics/README.md.")
    return 0


def db_check(conn: str) -> int:
    try:
        import pyodbc
    except ImportError:
        raise SystemExit("pyodbc is required for the --conn check. Run with: uv run --with pyodbc setup/verify.py --conn ...")
    expected = ["centre", "donor", "hla_typing", "patient",
                "search_request", "match_result", "workup", "donation"]
    problems = []
    try:
        cur = pyodbc.connect(conn, timeout=5).cursor()
        print(f"[{OK}] connected to the database")
    except Exception as e:
        print(f"[{FAIL}] could not connect: {e}")
        return 1
    for t in expected:
        try:
            cur.execute(f"SELECT COUNT(*) FROM dbo.{t}")
            n = cur.fetchone()[0]
            print(f"[{OK}] dbo.{t}: {n} rows" if n else f"[{FAIL}] dbo.{t}: 0 rows")
            if not n:
                problems.append(t)
        except Exception:
            print(f"[{FAIL}] dbo.{t}: missing")
            problems.append(t)
    print()
    if problems:
        print(f"{FAIL}: {len(problems)} issue(s).")
        return 1
    print(f"{OK}: database is in place.")
    return 0


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--conn", help="ODBC connection string (Day 2+). Omit for the Day 1 check.")
    args = ap.parse_args()
    sys.exit(db_check(args.conn) if args.conn else day1_check())


if __name__ == "__main__":
    main()
