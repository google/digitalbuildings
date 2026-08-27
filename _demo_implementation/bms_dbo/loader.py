"""Load a :class:`~bms_dbo.models.Site` from CSV.

The four CSVs stand in for four tables in your BMS database -- see
``schema.sql`` for the relational equivalent. The column names deliberately
track ABEL's spreadsheet tabs (Site / Entities / Entity Fields / Connections)
so that a config produced here and one produced by ABEL are comparable.

Note what is *not* here: there is no ``floor`` or ``room`` column on a device.
Location is an edge in ``connections.csv`` (recommendation #5).
"""

from __future__ import annotations

import csv
from pathlib import Path

from .models import Connection, Device, PointMapping, Site, Space
from .ontology import load_yaml

SPACES_CSV = "spaces.csv"
DEVICES_CSV = "devices.csv"
MAPPINGS_CSV = "point_mappings.csv"
CONNECTIONS_CSV = "connections.csv"
SITE_YAML = "site.yaml"


class LoaderError(RuntimeError):
    """Raised when the site export is missing files or columns."""


def _is_comment_row(row: dict[str, str]) -> bool:
    """A row whose first non-empty cell starts with '#'.

    Column names differ per table (``code``, ``device_code``,
    ``source_code``, ...), so checking a fixed column name misses tables that
    don't have it -- ``connections.csv`` has none of ``code``/``device_code``,
    which let a '#'-prefixed row through as a real connection. Checking
    "whatever the first cell is" works for every table uniformly.
    """
    first_value = next(
        (v.strip() for v in row.values() if v and v.strip()), ""
    )
    return first_value.startswith("#")


def _read_csv(path: Path, required_columns: set[str]) -> list[dict[str, str]]:
    if not path.is_file():
        raise LoaderError(f"missing site file: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        columns = set(reader.fieldnames or [])
        absent = required_columns - columns
        if absent:
            raise LoaderError(
                f"{path.name} is missing column(s): {sorted(absent)}"
            )
        rows = [
            {key: (value or "").strip() for key, value in row.items() if key}
            for row in reader
        ]
        # Skip blank lines and '#' comment rows.
        return [
            row
            for row in rows
            if any(row.values()) and not _is_comment_row(row)
        ]


def _as_float(value: str) -> float | None:
    value = value.strip()
    if not value:
        return None
    try:
        return float(value)
    except ValueError as error:
        raise LoaderError(f"expected a number, got {value!r}") from error


def _as_bool(value: str) -> bool:
    return value.strip().upper() in {"TRUE", "T", "YES", "Y", "1"}


def parse_states(encoded: str) -> dict[str, str]:
    """``ON=true;OFF=false`` -> ``{"ON": "true", "OFF": "false"}``.

    Raw values stay strings on purpose. DBO casts every state value to a
    string internally, and keeping ``"true"`` quoted stops YAML 1.1 from
    reinterpreting it on the way out.
    """
    states: dict[str, str] = {}
    for pair in encoded.split(";"):
        pair = pair.strip()
        if not pair:
            continue
        if "=" not in pair:
            raise LoaderError(
                f"malformed state map entry {pair!r}; expected STATE=raw_value"
            )
        state, raw = pair.split("=", 1)
        states[state.strip()] = raw.strip()
    return states


def _load_spaces(site_dir: Path) -> list[Space]:
    return [
        Space(
            code=row["code"],
            entity_type=row["entity_type"],
            display_name=row.get("display_name", ""),
        )
        for row in _read_csv(site_dir / SPACES_CSV, {"code", "entity_type"})
    ]


def _load_devices(site_dir: Path) -> list[Device]:
    return [
        Device(
            code=row["code"],
            entity_type=row["entity_type"],
            is_reporting=_as_bool(row["is_reporting"]),
            cloud_device_id=row.get("cloud_device_id", ""),
            display_name=row.get("display_name", ""),
            reporting_device_code=row.get("reporting_device_code", ""),
        )
        for row in _read_csv(
            site_dir / DEVICES_CSV, {"code", "entity_type", "is_reporting"}
        )
    ]


def _load_mappings(site_dir: Path) -> list[PointMapping]:
    return [
        PointMapping(
            device_code=row["device_code"],
            dbo_field=row["dbo_field"],
            native_path=row.get("native_path", ""),
            native_unit=row.get("native_unit", ""),
            dbo_unit=row.get("dbo_unit", ""),
            native_states=parse_states(row.get("native_states", "")),
            missing=_as_bool(row.get("missing", "")),
            reporting_field=row.get("reporting_field", ""),
            value_min=_as_float(row.get("value_min", "")),
            value_max=_as_float(row.get("value_max", "")),
            missing_justification=row.get("missing_justification", ""),
        )
        for row in _read_csv(site_dir / MAPPINGS_CSV, {"device_code", "dbo_field"})
    ]


def _load_connections(site_dir: Path) -> list[Connection]:
    return [
        Connection(
            source_code=row["source_code"],
            connection_type=row["connection_type"].strip().upper(),
            target_code=row["target_code"],
        )
        for row in _read_csv(
            site_dir / CONNECTIONS_CSV,
            {"source_code", "connection_type", "target_code"},
        )
    ]


def load_site(site_dir: Path) -> Site:
    """Read the four CSVs plus ``site.yaml`` into one :class:`Site`."""
    site_dir = Path(site_dir)
    meta = load_yaml(site_dir / SITE_YAML)
    building_code = meta.get("building_code")
    if not building_code:
        raise LoaderError(f"{SITE_YAML} does not define building_code")

    return Site(
        building_code=building_code,
        spaces=_load_spaces(site_dir),
        devices=_load_devices(site_dir),
        mappings=_load_mappings(site_dir),
        connections=_load_connections(site_dir),
    )
# AI:E87M claude-code 2026-08-27 s:2a846146
