
# Code to load data in Google Colab

import pandas as pd

# If file is on GitHub (raw URL):
# df = pd.read_csv("https://github.com/username/repo/raw/main/airbnb_complete.csv")

# If file is compressed:
# df = pd.read_csv("https://github.com/username/repo/raw/main/airbnb_complete.csv.gz")

# Verify data
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print(f"Cities: {df['city'].nunique()}")
print("\nFirst rows:")
df.head()
