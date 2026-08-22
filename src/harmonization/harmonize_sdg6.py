import pandas as pd

INPUT_FILE = "data/cleaned/sdg6_cleaned.csv"
OUTPUT_FILE = "data/harmonized/sdg6_harmonized.csv"

df = pd.read_csv(INPUT_FILE)

# Rename SDG 6 columns to our common schema
df = df.rename(columns={
    "GeoAreaCode": "location_id",
    "GeoAreaName": "country",
    "TimePeriod": "sample_date",
    "SeriesDescription": "parameter",
    "Value": "value",
    "Units": "unit",
    "Source": "source"
})

# Add fields not available in SDG 6
df["latitude"] = None
df["longitude"] = None
df["quality"] = None

# Arrange columns in our common order
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

print("SDG 6 harmonization complete!")
print("Rows:", len(df))
print("Saved to:", OUTPUT_FILE)