import pandas as pd

INPUT_FILE = "data/harmonized/master_water_quality.csv"

df = pd.read_csv(INPUT_FILE, low_memory=False)

print("=== DATA QUALITY REPORT ===")

# 1. Missing values
print("\nMissing values:")
print(df.isnull().sum())

# 2. Duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())

# 3. Check value column
df["value"] = pd.to_numeric(df["value"], errors="coerce")

print("\nInvalid/missing values:", df["value"].isnull().sum())

# 4. Check latitude
invalid_latitude = (
    df["latitude"].notna() &
    ((df["latitude"] < -90) | (df["latitude"] > 90))
)

print("Invalid latitude:", invalid_latitude.sum())

# 5. Check longitude
invalid_longitude = (
    df["longitude"].notna() &
    ((df["longitude"] < -180) | (df["longitude"] > 180))
)

print("Invalid longitude:", invalid_longitude.sum())

# 6. Basic statistics
print("\nValue statistics:")
print(df["value"].describe())

print("\nTotal rows:", len(df))