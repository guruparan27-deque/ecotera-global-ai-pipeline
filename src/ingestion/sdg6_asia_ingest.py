import requests
import pandas as pd

BASE_URL = (
    "https://www.sdg6data.org/api/indicator/"
    "6.1.1-1,6.1.1-2,6.1.1-3,6.1.1-4,6.1.1-7,"
    "6.1.1-11,6.1.1-15,6.1.1-19,6.1.1-23,6.1.1-27,"
    "6.1.1-31,6.1.1-35,6.1.1-401,6.1.1-402,6.1.1-403,"
    "6.1.1-404,6.1.1-405,6.1.1-406,6.1.1-407,6.1.1-408,"
    "6.1.1-409,6.1.1-410,6.1.1-411,6.1.1-412,6.1.1-413,"
    "6.1.1-414,6.1.1-415,6.1.1-416,6.1.1-417,6.1.1-418,"
    "6.1.1-419,6.1.1-420,6.1.1-421,6.1.1-422,6.1.1-423,"
    "6.1.1-424,6.1.1-425,6.1.1-426"
    "?_format=json"
    "&data=1eecb8e95a316529deb8755cf45f5a92"
    "&date=2000.00:2025.00"
    "&per_page=500"
)

target_countries = {
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

all_matches = []

for page in range(1, 26):

    print(f"Downloading page {page}/25...")

    url = BASE_URL + f"&page={page}"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    records = data[1]

    df = pd.DataFrame(records)

    if df.empty:
        continue

    df = df[df["GeoAreaName"].isin(target_countries)]

    if not df.empty:
        all_matches.append(df)

df = pd.concat(all_matches, ignore_index=True)

df.to_csv(
    "data/raw/sdg6_asia_raw.csv",
    index=False
)

print("\nTotal SE Asia rows:", len(df))

print("\nCountries found:")
print(df["GeoAreaName"].value_counts())

print("\nSaved to data/raw/sdg6_asia_raw.csv")