import pandas as pd

INPUT_FILE = "data/cleaned/gemstat_cleaned.csv"
OUTPUT_FILE = "data/harmonized/gemstat_harmonized.csv"

df = pd.read_csv(INPUT_FILE)

df = df.rename(columns={
    "location_id": "location_id",
    "sample_date": "sample_date",
    "value": "value",
    "unit": "unit",
    "quality": "quality"
})

# Add fields that GEMStat does not provide in our current dataset
df["source"] = "GEMStat"
df["parameter"] = "Arsenic"

# Fields not available in this GEMStat file
df["country"] = None
df["latitude"] = None
df["longitude"] = None

# Arrange into our common schema
df = df[
    [
        "source",
        "location_id",
        "country",
        "latitude",
        "longitude",
        "sample_date",
        "parameter",
        "value",
        "unit",
        "quality"
    ]
]

df.to_csv(OUTPUT_FILE, index=False)

print("GEMStat harmonization complete!")
print("Rows:", len(df))
print("Saved to:", OUTPUT_FILE)