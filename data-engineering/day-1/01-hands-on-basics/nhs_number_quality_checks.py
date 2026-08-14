from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parent.parent / "data" / "donor.csv"
df = pd.read_csv(csv_path, dtype={"nhs_number": str})


def is_valid_format(value: str) -> bool:
    value = str(value).strip()
    return value.isdigit() and len(value) == 10


def is_valid_mod11(value: str) -> bool:
    value = str(value).strip()
    if not is_valid_format(value):
        return False
    digits = [int(c) for c in value]
    total = sum(d * w for d, w in zip(digits[:9], range(10, 1, -1)))
    remainder = total % 11
    check_digit = 11 - remainder
    if check_digit == 11:
        check_digit = 0
    if check_digit == 10:
        return False  # invalid per NHS number spec
    return check_digit == digits[9]


format_ok = df["nhs_number"].apply(is_valid_format)
mod11_ok = df["nhs_number"].apply(is_valid_mod11)

total = len(df)
print(f"total rows: {total}")
print(f"format valid (10 digits): {format_ok.sum()} ({format_ok.mean() * 100:.1f}%)")
print(f"format invalid: {(~format_ok).sum()}")
print(f"mod11 valid: {mod11_ok.sum()} ({mod11_ok.mean() * 100:.1f}%)")
print(f"mod11 invalid: {(~mod11_ok).sum()}")

print("\nformat-invalid rows:")
print(df.loc[~format_ok, ["donor_id", "nhs_number"]].to_string(index=False))

print("\nmod11-invalid rows (format-valid but bad checksum):")
print(df.loc[format_ok & ~mod11_ok, ["donor_id", "nhs_number"]].to_string(index=False))
