# /// script
# requires-python = ">=3.11"
# dependencies = ["duckdb"]
# ///
"""
Generates the two inputs Stage 04 converts:

    day-3/05-adf-to-sql/data/donor_import.csv   the "weekly export" the Mapping Data Flow reads
    day-3/05-adf-to-sql/data/ethnicity_ref.csv  the cached lookup it joins to

Source of truth is day-1/data/donor.csv. The messiness added here is deliberate
and is what the flow's CleanNames / BuildPostcode / KeepActive / LookupEthnicity
steps exist to handle. Deterministic: no randomness, everything is row-index
arithmetic, so the gate numbers in answers.md never move.

Re-running this overwrites both files. Changing it invalidates every number in
05-adf-to-sql/answers.md and in parity.py.
"""
import csv
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
DAY3 = HERE.parent
SRC = DAY3.parent / "day-1" / "data" / "donor.csv"
OUT = DAY3 / "05-adf-to-sql" / "data"

UNKNOWN_CODE = "Z99"  # in the export, absent from the lookup


def main() -> None:
    rows = list(csv.DictReader(SRC.open(newline="", encoding="utf-8")))

    labels = sorted({r["ethnicity"] for r in rows})
    code_of = {label: f"E{i + 1:02d}" for i, label in enumerate(labels)}

    OUT.mkdir(parents=True, exist_ok=True)

    with (OUT / "ethnicity_ref.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["ethnicity_code", "ethnicity_label"])
        for label, code in sorted(code_of.items(), key=lambda kv: kv[1]):
            w.writerow([code, label])

    cols = [
        "registry_id", "first_name", "last_name", "date_of_birth", "sex",
        "email", "phone", "postcode", "nhs_number", "ethnicity_code",
        "registered_date", "status",
    ]
    with (OUT / "donor_import.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for i, r in enumerate(rows):
            # names arrive lower-cased from the source system -> initCap earns its place
            first = r["first_name"].lower()
            last = r["last_name"].lower()
            # every third row has a lower-case sex -> upper() earns its place
            sex = r["sex"].lower() if i % 3 == 0 else r["sex"]
            # postcode spacing is ragged in one row in four
            pc = r["postcode"]
            if i % 4 == 0:
                pc = re.sub(r"\s+", "  ", pc).lower()
            elif i % 4 == 1:
                pc = pc.replace(" ", "")
            # one row in a hundred carries a code the lookup does not have
            code = UNKNOWN_CODE if i % 100 == 0 else code_of[r["ethnicity"]]
            w.writerow([
                r["registry_id"], first, last, r["date_of_birth"], sex,
                r["email"], r["phone"], pc, r["nhs_number"], code,
                r["registered_date"], r["status"],
            ])

    print(f"wrote {OUT/'donor_import.csv'} ({len(rows)} rows)")
    print(f"wrote {OUT/'ethnicity_ref.csv'} ({len(code_of)} codes)")


if __name__ == "__main__":
    main()
