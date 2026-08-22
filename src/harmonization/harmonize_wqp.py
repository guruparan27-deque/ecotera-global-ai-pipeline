import pandas as pd

INPUT_FILE = "data/cleaned/wqp_cleaned.csv"
OUTPUT_FILE = "data/harmonized/wqp_harmonized.csv"

df = pd.read_csv(INPUT_FILE)

# Rename WQP columns to our common schema
df = df.rename(columns={
    "location_id": "location_id",
    "location_name": "location_name",
    "country": "country",
    "latitude": "latitude",
    "longitude": "longitude",
    "sample_date": "sample_date",
    "parameter": "parameter",
    "value": "value",
    "unit": "unit",
    "source": "source"
})

# Add quality column
df["quality"] = None

# Keep our common fields
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

print("WQP harmonization complete!")
print("Rows:", len(df))
print("Saved to:", OUTPUT_FILE)