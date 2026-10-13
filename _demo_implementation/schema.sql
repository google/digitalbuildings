-- Relational shape for DBO support inside a BMS.
--
-- This is the same model as bms_dbo/models.py, written the way it would live
-- in a real product database. Portable SQL; adjust types for your engine.
--
-- The three ideas worth copying:
--
--   1. dbo_point_mapping keeps the native point AND its DBO meaning on one
--      row. The native side stays authoritative for polling; the DBO side is
--      what analytics and the exported building config read. (rec #1)
--
--   2. is_missing is a column, not an absent row. A field a type requires but
--      the device cannot supply is declared MISSING, which is valid DBO.
--      Deleting the row instead fails instance validation. (rec #4)
--
--   3. There is no floor_id or room_id on dbo_device. Location is an edge in
--      dbo_connection, the same table that carries FEEDS and HAS_PART. A
--      device's location and its duct topology are the same kind of fact.
--      (rec #5)

-- ---------------------------------------------------------------------------
-- Which ontology revision this database was validated against.  (rec #2)
-- ---------------------------------------------------------------------------
CREATE TABLE dbo_ontology_pin (
    id              INTEGER      PRIMARY KEY,
    pinned_digest   CHAR(64)     NOT NULL,   -- sha256 of ontology/yaml/resources
    pinned_on       DATE         NOT NULL,
    source_url      VARCHAR(255) NOT NULL,
    CONSTRAINT dbo_ontology_pin_single_row CHECK (id = 1)
);

-- ---------------------------------------------------------------------------
-- Sites and spaces. One building configuration file per site.
-- ---------------------------------------------------------------------------
CREATE TABLE dbo_site (
    site_id         INTEGER      PRIMARY KEY,
    building_code   VARCHAR(64)  NOT NULL UNIQUE,  -- e.g. AU-MEL-DEMO
    display_name    VARCHAR(255)
);

CREATE TABLE dbo_space (
    space_id        INTEGER      PRIMARY KEY,
    site_id         INTEGER      NOT NULL REFERENCES dbo_site(site_id),
    code            VARCHAR(64)  NOT NULL,
    -- Fully qualified FACILITIES type: BUILDING, FLOOR, ROOM, CORRIDOR, ...
    entity_type     VARCHAR(128) NOT NULL,
    display_name    VARCHAR(255),
    entity_guid     CHAR(36)     NOT NULL,
    UNIQUE (site_id, code),
    UNIQUE (entity_guid)
);

-- ---------------------------------------------------------------------------
-- Devices. Reporting devices emit telemetry; virtual devices are linked to a
-- reporting device (usually a gateway) or, for zones, to nothing at all.
-- ---------------------------------------------------------------------------
CREATE TABLE dbo_device (
    device_id           INTEGER      PRIMARY KEY,
    site_id             INTEGER      NOT NULL REFERENCES dbo_site(site_id),
    code                VARCHAR(64)  NOT NULL,
    entity_type         VARCHAR(128) NOT NULL,   -- e.g. HVAC/VAV_SD_DSP
    is_reporting        BOOLEAN      NOT NULL,
    cloud_device_id     VARCHAR(32),             -- numeric string, reporting only
    display_name        VARCHAR(255),
    reporting_device_id INTEGER      REFERENCES dbo_device(device_id),
    entity_guid         CHAR(36)     NOT NULL,
    UNIQUE (site_id, code),
    UNIQUE (entity_guid),
    -- A reporting device owns a cloud id and links from nothing.
    CONSTRAINT dbo_device_reporting_shape CHECK (
        (is_reporting AND cloud_device_id IS NOT NULL
                      AND reporting_device_id IS NULL)
        OR
        (NOT is_reporting AND cloud_device_id IS NULL)
    )
);

CREATE INDEX dbo_device_site_idx ON dbo_device (site_id);
CREATE INDEX dbo_device_gateway_idx ON dbo_device (reporting_device_id);

-- ---------------------------------------------------------------------------
-- The point mapping table. One row per (device, DBO field).           (rec #1)
-- ---------------------------------------------------------------------------
CREATE TABLE dbo_point_mapping (
    mapping_id      INTEGER      PRIMARY KEY,
    device_id       INTEGER      NOT NULL REFERENCES dbo_device(device_id),

    -- The DBO side.
    dbo_field       VARCHAR(128) NOT NULL,   -- standard field, may be enumerated
    dbo_unit        VARCHAR(64),             -- from units.yaml; NULL if multistate
    is_missing      BOOLEAN      NOT NULL DEFAULT FALSE,          -- rec #4

    -- The native side. Authoritative for polling; never overwritten by DBO.
    native_path     VARCHAR(255),            -- points.<name>.present_value
    native_unit     VARCHAR(64),             -- the raw unit string, e.g. 'degC'

    -- Link wiring: which gateway field carries this virtual device's data.
    reporting_field VARCHAR(128),

    -- Device-specific expected range, expressed in dbo_unit. Optional. DBO
    -- uses it for telemetry data quality and to validate writeback requests.
    value_min       DOUBLE PRECISION,
    value_max       DOUBLE PRECISION,

    UNIQUE (device_id, dbo_field),

    -- A MISSING field carries no raw name, no raw unit and no range.
    CONSTRAINT dbo_mapping_missing_is_empty CHECK (
        NOT is_missing
        OR (native_path IS NULL AND native_unit IS NULL
            AND dbo_unit IS NULL AND value_min IS NULL AND value_max IS NULL)
    ),
    CONSTRAINT dbo_mapping_range_ordered CHECK (
        value_min IS NULL OR value_max IS NULL OR value_min < value_max
    )
);

CREATE INDEX dbo_point_mapping_device_idx ON dbo_point_mapping (device_id);
CREATE INDEX dbo_point_mapping_field_idx ON dbo_point_mapping (dbo_field);

-- State maps for multistate fields: DBO state name -> raw device value.
-- Values are text because DBO casts every state value to a string.
CREATE TABLE dbo_point_state (
    mapping_id      INTEGER      NOT NULL REFERENCES dbo_point_mapping(mapping_id),
    dbo_state       VARCHAR(64)  NOT NULL,   -- ON, OFF, ACTIVE, OPEN, ...
    native_value    VARCHAR(64)  NOT NULL,   -- '1', 'true', 'active', ...
    PRIMARY KEY (mapping_id, dbo_state)
);

-- ---------------------------------------------------------------------------
-- The relationship graph: location AND topology in one table.        (rec #5)
-- ---------------------------------------------------------------------------
CREATE TABLE dbo_connection (
    connection_id   INTEGER      PRIMARY KEY,
    site_id         INTEGER      NOT NULL REFERENCES dbo_site(site_id),
    -- Entity codes rather than FKs, because an edge may join a space to a
    -- device. Enforce referential integrity in the application layer, or add
    -- a shared dbo_entity supertype if your schema allows it.
    source_code     VARCHAR(64)  NOT NULL,
    target_code     VARCHAR(64)  NOT NULL,
    connection_type VARCHAR(32)  NOT NULL,
    UNIQUE (site_id, source_code, target_code, connection_type),
    CONSTRAINT dbo_connection_no_self_edge CHECK (source_code <> target_code),
    CONSTRAINT dbo_connection_known_type CHECK (connection_type IN (
        'CONTAINS',
        'CONTROLS',
        'FEEDS',
        'FULLY_AGGREGATES',
        'HAS_PART',
        'HAS_RANGE',
        'MEASURES',
        'MEASURES_TYPE',
        'PARIALLY_AGGREGATES',   -- spelled this way in the ontology
        'PARTIALLY_AGGREGATES'
    ))
);

CREATE INDEX dbo_connection_target_idx ON dbo_connection (site_id, target_code);
CREATE INDEX dbo_connection_source_idx ON dbo_connection (site_id, source_code);

-- ---------------------------------------------------------------------------
-- Two queries the model is designed to make cheap.
-- ---------------------------------------------------------------------------

-- Every device on a floor, however deeply nested the spaces are.
-- (Recursive CTE syntax varies; this is the ANSI form.)
--
-- WITH RECURSIVE contained(code) AS (
--     SELECT target_code FROM dbo_connection
--      WHERE site_id = :site AND source_code = :floor_code
--        AND connection_type = 'CONTAINS'
--     UNION ALL
--     SELECT c.target_code FROM dbo_connection c
--       JOIN contained ON c.source_code = contained.code
--      WHERE c.site_id = :site AND c.connection_type = 'CONTAINS'
-- )
-- SELECT d.* FROM dbo_device d JOIN contained ON d.code = contained.code;

-- Every zone temperature in the building, regardless of equipment type --
-- the portability DBO exists to provide.
--
-- SELECT d.code, m.native_path, m.dbo_unit
--   FROM dbo_point_mapping m
--   JOIN dbo_device d ON d.device_id = m.device_id
--  WHERE m.dbo_field LIKE 'zone_air_temperature_sensor%'
--    AND NOT m.is_missing
--    AND d.site_id = :site;
-- AI:E87M claude-code 2026-08-27 s:2a846146
