import pandas as pd

INPUT_FILE = "data/raw/wqp_raw.csv"
OUTPUT_FILE = "data/cleaned/wqp_cleaned.csv"

df = pd.read_csv(INPUT_FILE)

df = df[
    [
        "MonitoringLocationIdentifier",
        "MonitoringLocationName",
        "MonitoringLocationCountryName",
        "MonitoringLocationLatitudeMeasure",
        "MonitoringLocationLongitudeMeasure",
        "ActivityStartDate",
        "CharacteristicName",
        "ResultMeasureValue",
        "ResultMeasureUnitCode",
        "ProviderName"
    ]
]

df = df.rename(columns={
    "MonitoringLocationIdentifier": "location_id",
    "MonitoringLocationName": "location_name",
    "MonitoringLocationCountryName": "country",
    "MonitoringLocationLatitudeMeasure": "latitude",
    "MonitoringLocationLongitudeMeasure": "longitude",
    "ActivityStartDate": "sample_date",
    "CharacteristicName": "parameter",
    "ResultMeasureValue": "value",
    "ResultMeasureUnitCode": "unit",
    "ProviderName": "source"
})

df["value"] = pd.to_numeric(df["value"], errors="coerce")

df = df.dropna(subset=["value"])
df = df.drop_duplicates()

df.to_csv(OUTPUT_FILE, index=False)

print("WQP cleaning complete!")
print("Rows after cleaning:", len(df))
print("Saved to:", OUTPUT_FILE)