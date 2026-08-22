import pandas as pd

INPUT_FILE = "data/raw/sdg6_raw.csv"
OUTPUT_FILE = "data/cleaned/sdg6_cleaned.csv"

df = pd.read_csv(INPUT_FILE)

# Remove rows where Value is missing
df = df.dropna(subset=["Value"])

# Convert Value to a number
df["Value"] = pd.to_numeric(df["Value"], errors="coerce")

# Remove rows that still have invalid values
df = df.dropna(subset=["Value"])

# Convert year to number
df["TimePeriod"] = pd.to_numeric(df["TimePeriod"], errors="coerce")

# Remove duplicate rows
df = df.drop_duplicates()

df.to_csv(OUTPUT_FILE, index=False)

print("Cleaning complete!")
print("Rows after cleaning:", len(df))
print("Saved to:", OUTPUT_FILE)