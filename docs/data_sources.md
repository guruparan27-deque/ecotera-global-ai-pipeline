# Data Sources

## 1. SDG 6 Data Portal

**Source:** United Nations SDG 6 Data Portal

**Website:** https://www.sdg6data.org/

**Data used:** SDG indicator 6.1.1 — drinking-water data.

**Pipeline use:** The dataset was retrieved through the SDG 6 API, filtered for indicator `6.1.1`, cleaned, and harmonized into the common schema.

---

## 2. Water Quality Portal (WQP)

**Source:** Water Quality Portal (USGS / EPA)

**Website:** https://www.waterqualitydata.us/

**Data used:** Dissolved oxygen measurements.

**Pipeline use:** Sample-result data was downloaded through the WQP web service, cleaned, and harmonized into the common schema.

---

## 3. GEMStat

**Source:** GEMStat / UNEP Global Freshwater Quality Database

**Website:** https://gemstat.org/

**Archive:** GEMStat GFQA v3 archive hosted on Zenodo.

**Data used:** Arsenic measurements from `Arsenic.csv`.

**Pipeline use:** The parameter file was extracted from the GEMStat archive, cleaned, quality filtered, and harmonized into the common schema.

---

## Data Processing Note

Each source uses different field names and data structures. The pipeline converts the selected source data into a common schema so that records can be combined into a single master dataset.