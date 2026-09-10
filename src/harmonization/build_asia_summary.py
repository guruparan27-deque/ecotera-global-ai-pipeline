import json
import pandas as pd

INPUT_FILE = "data/asia_subset.csv"
OUTPUT_FILE = "data/asia_subset_summary.json"

df = pd.read_csv(INPUT_FILE, low_memory=False)

summary = {
    "total_records": len(df),

    "records_by_country": (
        df["country"]
        .value_counts()
        .to_dict()
    ),

    "records_by_parameter": (
        df["parameter"]
        .value_counts()
        .to_dict()
    ),

    "records_by_year": (
        df["year"]
        .value_counts()
        .sort_index()
        .to_dict()
    ),

    "records_by_source": (
        df["source"]
        .value_counts(dropna=False)
        .to_dict()
    )
}

with open(OUTPUT_FILE, "w") as file:
    json.dump(summary, file, indent=2)

print("Asia summary created!")
print("Total records:", summary["total_records"])
print("Saved to:", OUTPUT_FILE)