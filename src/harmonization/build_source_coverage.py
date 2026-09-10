import json
import pandas as pd

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

coverage = {}


# SDG 6
sdg = pd.read_csv("data/raw/sdg6_asia_raw.csv", low_memory=False)

sdg_in_scope = sdg["GeoAreaName"].isin(TARGET_COUNTRIES)
sdg_missing_value = sdg["Value"].isna()

coverage["SDG 6"] = {
    "total_records_checked": len(sdg),
    "in_scope_records": int((sdg_in_scope & ~sdg_missing_value).sum()),
    "out_of_scope_records": int((~sdg_in_scope).sum()),
    "missing_geography_records": int(sdg["GeoAreaName"].isna().sum()),
    "missing_value_records": int(
        (sdg_in_scope & sdg_missing_value).sum()
    )
}

# --------------------------------------------------
# 2. Water Quality Portal
# --------------------------------------------------

wqp = pd.read_csv(
    "data/raw/wqp_raw.csv",
    low_memory=False
)

lat = pd.to_numeric(
    wqp["MonitoringLocationLatitudeMeasure"],
    errors="coerce"
)

lon = pd.to_numeric(
    wqp["MonitoringLocationLongitudeMeasure"],
    errors="coerce"
)

missing_geo = lat.isna() | lon.isna()

# Our downloaded WQP sample is clearly US-based.
# Its coordinates are far outside Southeast Asia.
wqp_in_scope = pd.Series(False, index=wqp.index)

coverage["WQP"] = {
    "total_records_checked": len(wqp),
    "in_scope_records": int(wqp_in_scope.sum()),
    "out_of_scope_records": int(
        (~wqp_in_scope & ~missing_geo).sum()
    ),
    "missing_geography_records": int(
        missing_geo.sum()
    ),
    "note": "Downloaded WQP sample is US-based and is excluded from the Southeast Asia live page."
}


# --------------------------------------------------
# 3. GEMStat
# --------------------------------------------------

gem = pd.read_csv(
    "data/cleaned/gemstat_cleaned.csv",
    low_memory=False
)

gem_in_scope = gem["country"].isin(TARGET_COUNTRIES)

gem_missing_geo = (
    gem["country"].isna()
    | gem["latitude"].isna()
    | gem["longitude"].isna()
)

coverage["GEMStat"] = {
    "total_records_checked": len(gem),
    "in_scope_records": int(gem_in_scope.sum()),
    "out_of_scope_records": int(
        (~gem_in_scope & ~gem_missing_geo).sum()
    ),
    "missing_geography_records": int(
        gem_missing_geo.sum()
    ),
    "note": "No verified stations for the 10 target countries were found in the GEMStat Arsenic dataset."
}


# --------------------------------------------------
# Save summary
# --------------------------------------------------

OUTPUT_FILE = "data/asia_source_coverage.json"

with open(OUTPUT_FILE, "w") as file:
    json.dump(coverage, file, indent=2)

print("Source coverage report created!")
print(json.dumps(coverage, indent=2))
print(f"\nSaved to: {OUTPUT_FILE}")