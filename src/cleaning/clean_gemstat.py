import pandas as pd

INPUT_FILE = "data/raw/Arsenic.csv"
OUTPUT_FILE = "data/cleaned/gemstat_cleaned.csv"

df = pd.read_csv(
    INPUT_FILE,
    encoding="latin1",
    low_memory=False
)

# Keep the columns we need
df = df[
    [
        "GEMS Station Number",
        "Sample Date",
        "Value",
        "Unit",
        "Data Quality",
        "License Information"
    ]
]

# Rename them to our common names
df = df.rename(columns={
    "GEMS Station Number": "location_id",
    "Sample Date": "sample_date",
    "Value": "value",
    "Unit": "unit",
    "Data Quality": "quality",
    "License Information": "license"
})

# Add information about this dataset
df["parameter"] = "Arsenic"
df["source"] = "GEMStat"

# Make Value numeric
df["value"] = pd.to_numeric(df["value"], errors="coerce")

# Remove missing values
df = df.dropna(subset=["value"])

# Remove duplicate rows
df = df.drop_duplicates()

df.to_csv(OUTPUT_FILE, index=False)

print("GEMStat cleaning complete!")
print("Rows after cleaning:", len(df))
print("Saved to:", OUTPUT_FILE)