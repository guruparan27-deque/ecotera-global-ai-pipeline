# Pipeline Workflow Diagram

```text
START
  ↓
Select Data Sources
  ↓
Extract / Download Data
  ↓
Store Raw Data
  ↓
Clean Data
  ├── Remove missing/invalid values
  ├── Remove duplicates
  └── Standardize data types
  ↓
Quality Checks
  ├── Missing values
  ├── Duplicate records
  ├── Invalid coordinates
  └── Suspicious values
  ↓
Harmonization
  ├── Standardize column names
  ├── Standardize fields
  └── Standardize data structure
  ↓
Combine Datasets
  ↓
Master Water Quality Dataset
  ↓
Database / CSV Export
  ↓
Future Dashboard / API / AI-ML
  ↓
END