# Data Dictionary

This document describes the common schema used by the harmonized water-quality datasets.

| Column | Description |
|---|---|
| `source` | The original dataset or organization from which the record came. |
| `location_id` | Identifier for the sampling location or station. |
| `country` | Country associated with the sampling location, when available. |
| `latitude` | Latitude of the sampling location, when available. |
| `longitude` | Longitude of the sampling location, when available. |
| `sample_date` | Date when the sample or observation was recorded. |
| `parameter` | Water-quality parameter or indicator being measured. |
| `value` | Numerical value of the observation. |
| `unit` | Measurement unit associated with the value, when available. |
| `quality` | Data-quality information provided by the source, when available. |

## Notes

- The three source datasets do not contain exactly the same information.
- Missing fields are left blank when the original source does not provide the information.
- Source-specific information is simplified into the common schema to support harmonization.
- The current GEMStat dataset used in this pipeline represents **Arsenic** measurements.
- The current Water Quality Portal dataset represents **Dissolved oxygen** measurements.
- The current SDG 6 dataset represents **indicator 6.1.1 drinking-water data**.