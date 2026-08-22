import pandas as pd

files = [
    "data/harmonized/sdg6_harmonized.csv",
    "data/harmonized/wqp_harmonized.csv",
    "data/harmonized/gemstat_harmonized.csv"
]

dataframes = [pd.read_csv(file) for file in files]

master = pd.concat(dataframes, ignore_index=True)

master.to_csv(
    "data/harmonized/master_water_quality.csv",
    index=False
)

print("Master dataset created!")
print("Total rows:", len(master))
print("Columns:", master.columns.tolist())