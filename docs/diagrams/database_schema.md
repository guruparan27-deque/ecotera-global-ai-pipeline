# Database / Schema Diagram

```text
┌─────────────────────┐
│       SOURCES       │
├─────────────────────┤
│ PK source_id        │
│ source_name         │
└──────────┬──────────┘
           │
           │ 1
           │
           │ many
           ▼
┌─────────────────────────────┐
│        MEASUREMENTS         │
├─────────────────────────────┤
│ PK measurement_id           │
│ FK source_id                │
│ FK location_id              │
│ sample_date                 │
│ parameter                   │
│ value                       │
│ unit                        │
│ quality                     │
└──────────────┬──────────────┘
               │
               │ many
               │
               │ 1
               ▼
┌─────────────────────┐
│      LOCATIONS      │
├─────────────────────┤
│ PK location_id     │
│ country            │
│ latitude           │
│ longitude          │
└─────────────────────┘