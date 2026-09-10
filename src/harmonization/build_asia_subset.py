import pandas as pd

INPUT_FILE = "data/raw/sdg6_asia_raw.csv"
OUTPUT_FILE = "data/asia_subset.csv"

TARGET_COUNTRIES = {
    "Singapore",
    "Malaysia",
    "Indonesia",
    "Brunei Darussalam",
    "Thailand",
    "Viet Nam",
    "Cambodia",
    "Lao People's Democratic Republic",
    "Myanmar",
    "Philippines"
}

df = pd.read_csv(INPUT_FILE, low_memory=False)

# Keep only the 10 countries requested by the mentor
df = df[df["GeoAreaName"].isin(TARGET_COUNTRIES)].copy()

# Rename fields for the website
df = df.rename(columns={
    "GeoAreaName": "country",
    "GeoAreaCode": "country_code",
    "TimePeriod": "year",
    "Value": "value",
    "Units": "unit",
    "Source": "source",
    "SeriesDescription": "parameter"
})

# Keep only useful website fields
df = df[
    [
        "country",
        "country_code",
        "year",
        "parameter",
        "value",
        "unit",
        "source"
    ]
]

# Remove rows where the actual value is missing
df = df.dropna(subset=["value"])

df.to_csv(OUTPUT_FILE, index=False)

print("Asia subset created!")
print("Rows:", len(df))

print("\nRecords by country:")
print(df["country"].value_counts())

print("\nSaved to:", OUTPUT_FILE)