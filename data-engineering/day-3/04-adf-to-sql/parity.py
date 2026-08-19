# /// script
# requires-python = ">=3.11"
# dependencies = ["duckdb"]
# ///
"""
Parity check for the ADF -> SQL conversion.

    uv run parity.py            checks view.sql in this folder
    uv run parity.py mine.sql   checks a different file

Write your conversion as a single SELECT in `view.sql`. Two tables are already
registered for you:

    imp   data/donor_import.csv    the weekly export the Mapping Data Flow reads
    ref   data/ethnicity_ref.csv   the cached lookup it joins to

Your SELECT must return these columns, named exactly:

    registry_id first_name last_name date_of_birth sex email phone
    postcode nhs_number ethnicity registered_date status

`donor_id` is not in that list on purpose. The surrogate key is one of the three
things in the flow that a view cannot do — Stage 04 is where you find out which
three and why.
"""
import sys
from pathlib import Path

import duckdb

HERE = Path(__file__).resolve().parent
OK, FAIL = "\033[92mOK\033[0m", "\033[91mFAIL\033[0m"

COLUMNS = [
    "registry_id", "first_name", "last_name", "date_of_birth", "sex", "email",
    "phone", "postcode", "nhs_number", "ethnicity", "registered_date", "status",
]

# Gates. Every one of these comes from the flow's own script lines.
EXPECT_ROWS = 2885          # status == 'Active' survives KeepActive
EXPECT_NULL_ETHNICITY = 23  # codes the lookup has no row for; a left join keeps them
EXPECT_CHECKSUM = "e3708f512cf67c6947c45c433bbee824"

CHECKSUM_SQL = """
select md5(string_agg(
    concat_ws('|',
        coalesce(registry_id, ''), coalesce(first_name, ''), coalesce(last_name, ''),
        coalesce(date_of_birth, ''), coalesce(sex, ''), coalesce(email, ''),
        coalesce(phone, ''), coalesce(postcode, ''), coalesce(nhs_number, ''),
        coalesce(ethnicity, ''), coalesce(registered_date, ''), coalesce(status, '')),
    chr(10) order by registry_id))
from result
"""


def main() -> int:
    target = HERE / (sys.argv[1] if len(sys.argv) > 1 else "view.sql")
    if not target.exists():
        print(f"[{FAIL}] {target.name} not found — write your SELECT into it first")
        return 1

    sql = target.read_text(encoding="utf-8").strip().rstrip(";")
    body = "\n".join(
        line for line in sql.splitlines() if line.strip() and not line.strip().startswith("--")
    ).strip()
    if not body:
        print(f"[{FAIL}] {target.name} has no query in it yet — write your SELECT into it")
        return 1

    con = duckdb.connect()
    con.execute(f"create view imp as select * from read_csv_auto('{HERE/'data'/'donor_import.csv'}', all_varchar=true)")
    con.execute(f"create view ref as select * from read_csv_auto('{HERE/'data'/'ethnicity_ref.csv'}', all_varchar=true)")

    try:
        con.execute(f"create view result as {sql}")
        got_columns = [c.lower() for c in con.sql("select * from result limit 0").columns]
    except Exception as exc:  # noqa: BLE001 — the message is the useful part
        print(f"[{FAIL}] the query did not run:\n{exc}")
        return 1

    problems = []

    missing = [c for c in COLUMNS if c not in got_columns]
    extra = [c for c in got_columns if c not in COLUMNS]
    if missing or extra:
        print(f"[{FAIL}] columns — missing {missing or 'none'}, unexpected {extra or 'none'}")
        problems.append("columns")
    else:
        print(f"[{OK}] all twelve columns present, named correctly")

    rows = con.sql("select count(*) from result").fetchone()[0]
    if rows == EXPECT_ROWS:
        print(f"[{OK}] {rows} rows")
    else:
        print(f"[{FAIL}] {rows} rows, expected {EXPECT_ROWS}")
        problems.append("rows")

    if "ethnicity" in got_columns:
        nulls = con.sql("select count(*) from result where ethnicity is null").fetchone()[0]
        if nulls == EXPECT_NULL_ETHNICITY:
            print(f"[{OK}] {nulls} rows with no ethnicity label")
        else:
            hint = " (an inner join drops them; the flow's lookup does not)" if nulls == 0 else ""
            print(f"[{FAIL}] {nulls} rows with no ethnicity label, expected {EXPECT_NULL_ETHNICITY}{hint}")
            problems.append("lookup")

    if not problems:
        digest = con.sql(CHECKSUM_SQL).fetchone()[0]
        if digest == EXPECT_CHECKSUM:
            print(f"[{OK}] every value matches the reference conversion")
        else:
            print(f"[{FAIL}] counts match but values differ — every column is checked, including\n       the ones the flow passes through untouched")
            problems.append("values")

    print()
    print("green" if not problems else f"not yet: {', '.join(problems)}")
    return 0 if not problems else 1


if __name__ == "__main__":
    raise SystemExit(main())
