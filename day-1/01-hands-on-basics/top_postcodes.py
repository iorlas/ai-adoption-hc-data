from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parent.parent / "data" / "donor.csv"
df = pd.read_csv(csv_path)
print(df["postcode"].value_counts().head(10))
