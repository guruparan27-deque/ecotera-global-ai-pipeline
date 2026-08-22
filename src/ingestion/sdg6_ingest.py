import requests
import pandas as pd

URL = "https://sdg6data.org/api/indicator/all?_format=json&per_page=500"

response = requests.get(URL)

print("Status:", response.status_code)

data = response.json()

records = data[1]

df = pd.DataFrame(records)

# Keep only SDG indicator 6.1.1
df = df[df["Indicator"] == "6.1.1"]
df = df[
    [
        "Indicator",
        "SeriesDescription",
        "GeoAreaName",
        "GeoAreaCode",
        "TimePeriod",
        "Value",
        "Units",
        "Source"
    ]
]

print("\nRows found:", len(df))
print(df[["Indicator", "SeriesDescription", "GeoAreaName", "TimePeriod", "Value"]].head())

df.to_csv("data/raw/sdg6_raw.csv", index=False)

print("\nSaved to data/raw/sdg6_raw.csv")