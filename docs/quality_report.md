# Data Quality Report

## Dataset

Master dataset: `data/harmonized/master_water_quality.csv`

Total records: **476,311**

## Quality Checks

| Check | Result |
|---|---:|
| Total records | 476,311 |
| Duplicate records | 0 |
| Invalid/missing numerical values | 0 |
| Invalid latitude values | 0 |
| Invalid longitude values | 0 |

## Missing Values

| Column | Missing records |
|---|---:|
| `source` | 0 |
| `location_id` | 0 |
| `country` | 476,203 |
| `latitude` | 473,977 |
| `longitude` | 473,977 |
| `sample_date` | 0 |
| `parameter` | 0 |
| `value` | 0 |
| `unit` | 108 |
| `quality` | 2,442 |

## Value Statistics

- Minimum value: `0`
- Maximum value: `112.6`
- Mean value: approximately `0.1087`

## Data Quality Decisions

- GEMStat records marked `Pending review` were removed during cleaning.
- WQP records containing `-99.9` were removed because the source explicitly identifies `-99.9` as a null value.
- Missing country and geographic coordinates were retained as missing when the selected source data did not provide them.
- Missing values were not replaced with invented values.

## Conclusion

The current pipeline successfully produces a harmonized dataset with no duplicate records, invalid coordinates, or missing numerical measurement values. Some geographic and metadata fields remain incomplete because the source datasets do not provide the same information.