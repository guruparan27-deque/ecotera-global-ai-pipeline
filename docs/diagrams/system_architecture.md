# System Architecture Diagram

```text
┌─────────────────────────────────────────────┐
│              EXTERNAL DATA SOURCES          │
│                                             │
│   SDG 6        Water Quality       GEMStat  │
│   Portal       Portal (WQP)                │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────┐
│               INGESTION LAYER               │
│                                             │
│       Python source-specific scripts        │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────┐
│              PROCESSING LAYER               │
│                                             │
│   Cleaning → Quality Checks → Harmonization │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────┐
│              DATA STORAGE                  │
│                                             │
│   Raw Data → Cleaned Data → Master Dataset │
│                                             │
│          Proposed SQL Database              │
└──────────────────────┬──────────────────────┘
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
┌─────────────────────┐   ┌───────────────────┐
│    API / Dashboard  │   │     AI / ML       │
│      (Future)       │   │      (Future)     │
└─────────────────────┘   └───────────────────┘