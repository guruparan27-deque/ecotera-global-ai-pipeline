# Changelog

## Week 1 — Project Setup & Architecture

### Completed
- Created the `ecotera-global-ai-pipeline` GitHub repository.
- Set up the project folder structure.
- Reviewed the project requirements and selected the Global Public Water Data Pipeline architecture.
- Identified the three initial data sources:
  - SDG 6 Data Portal
  - Water Quality Portal
  - GEMStat
- Defined the initial common data schema.
- Added initial project documentation.

---

## Week 2 — Data Ingestion & Cleaning

### Completed
- Implemented SDG 6 API ingestion.
- Retrieved and filtered SDG indicator `6.1.1`.
- Implemented SDG 6 cleaning and generated the cleaned dataset.
- Implemented Water Quality Portal ingestion for dissolved oxygen measurements.
- Implemented Water Quality Portal cleaning.
- Accessed the GEMStat GFQA v3 archive.
- Extracted the GEMStat Arsenic dataset.
- Implemented GEMStat cleaning.
- Added handling for missing values, invalid values, and duplicate records.

---

## Week 3 — Harmonization & Quality Control

### Completed
- Harmonized SDG 6 data into the common schema.
- Harmonized Water Quality Portal data into the common schema.
- Harmonized GEMStat data into the common schema.
- Combined the three harmonized datasets into a master dataset.
- Implemented automated data-quality checks.
- Checked missing values, duplicates, invalid coordinates, and invalid numerical values.
- Investigated suspicious GEMStat values.
- Removed GEMStat records marked as `Pending review`.

### Current Master Dataset
- Total records: `476,320`
- Standardized columns: `10`

---

## Week 4 — Architecture, Database Design & Documentation

### Completed
- Created the proposed database schema.
- Created the database/schema diagram.
- Created the system architecture diagram.
- Created the data-flow diagram.
- Created the pipeline workflow diagram.
- Created the future integration diagram.
- Added the data dictionary.
- Added the data source documentation.
- Prepared the project for final testing and GitHub submission.

### Next Steps
- Final pipeline testing.
- Documentation review.
- GitHub repository cleanup.
- Final project handover.