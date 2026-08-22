# Data Flow Diagram

```text
SDG 6 ───────┐
             │
WQP ─────────┼──→ Raw Data
             │
GEMStat ─────┘
                  ↓
              Cleaning
                  ↓
             Quality Check
                  ↓
           Harmonization
                  ↓
          Master Dataset
                  ↓
          ┌───────┴───────┐
          ↓               ↓
       Database       CSV Export
          ↓
   ┌──────┴──────┐
   ↓             ↓
Dashboard       AI/ML
(Future)       (Future)