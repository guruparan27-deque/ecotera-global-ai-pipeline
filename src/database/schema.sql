-- ============================================
-- Ecotera Global Water Quality Pipeline
-- Database Schema
-- ============================================

-- 1. Data sources
CREATE TABLE sources (
    source_id INTEGER PRIMARY KEY,
    source_name VARCHAR(100) NOT NULL
);

-- 2. Sampling locations
CREATE TABLE locations (
    location_id VARCHAR(100) PRIMARY KEY,
    country VARCHAR(100),
    latitude DECIMAL(10, 6),
    longitude DECIMAL(10, 6)
);

-- 3. Water-quality measurements
CREATE TABLE measurements (
    measurement_id INTEGER PRIMARY KEY,
    source_id INTEGER NOT NULL,
    location_id VARCHAR(100),
    sample_date DATE,
    parameter VARCHAR(200) NOT NULL,
    value DECIMAL(20, 8),
    unit VARCHAR(50),
    quality VARCHAR(100),

    FOREIGN KEY (source_id) REFERENCES sources(source_id),
    FOREIGN KEY (location_id) REFERENCES locations(location_id)
);