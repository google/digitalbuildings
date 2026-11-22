"""Emit a DBO building configuration file from the BMS model.

The export is a pure function of the four tables. Nothing is invented here --
if a value is not in the model it does not appear in the config, which is what
makes the output reviewable and the process repeatable.

Shape produced (the "new format" from ontology/docs/building_config.md):

    CONFIG_METADATA:
      operation: INITIALIZE

    <entity-guid>:
      code: AHU-1
      type: HVAC/AHU_DFSS_DTC_CHWVM_RTM
      cloud_device_id: '...'
      connections: {<source-guid>: [CONTAINS, ...]}
      translation: {...}      # reporting entities
      links: {<source-guid>: {...}}   # virtual entities
"""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml

from .models import Device, PointMapping, Site
from .ontology import Ontology


class _ConfigDumper(yaml.SafeDumper):
    """Dumper that keeps block style and does not collapse short mappings."""

    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)


def _represent_str(dumper: yaml.SafeDumper, data: str):
    # Raw state values such as "true"/"1"/"ON" must survive a YAML round trip
    # as strings. Quoting them explicitly is what the DBO examples do.
    if data in {"true", "false", "True", "False", "TRUE", "FALSE"}:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="'")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


_ConfigDumper.add_representer(str, _represent_str)


def _translation_for(
    ontology: Ontology, mapping: PointMapping
) -> str | dict[str, Any]:
    """One entry of a reporting entity's ``translation`` block."""
    if mapping.missing:
        return "MISSING"

    entry: dict[str, Any] = {"present_value": mapping.native_path}
    definition = ontology.get_field(mapping.dbo_field)

    if definition is not None and definition.is_multistate:
        entry["states"] = dict(sorted(mapping.native_states.items()))
        return entry

    if mapping.dbo_unit:
        # Derive the units key from the present_value path the same way the
        # DBO examples do: points.<name>.present_value -> pointset.points.
        # <name>.units. Falls back to a literal path if the shape differs.
        entry["units"] = {
            "key": _units_key(mapping.native_path),
            "values": {mapping.dbo_unit: mapping.native_unit},
        }
        if mapping.has_range:
            # Only ever the engineer's device-specific range. Deriving one from
            # the ontology's sanity envelope would emit "0,94389" litres per
            # second for a VAV -- true, useless, and actively misleading for
            # the writeback validation DBO uses value_range for.
            entry["value_range"] = (
                f"{_trim(mapping.value_min)},{_trim(mapping.value_max)}"
            )
    return entry


def _units_key(present_value_path: str) -> str:
    if present_value_path.endswith(".present_value"):
        stem = present_value_path[: -len(".present_value")]
        return f"pointset.{stem}.units"
    return f"pointset.{present_value_path}.units"


def _trim(value: float) -> str:
    rounded = round(value, 4)
    return str(int(rounded)) if rounded == int(rounded) else str(rounded)


def _connections_block(site: Site, target_code: str) -> dict[str, list[str]]:
    """Connections keyed by *source* guid, as DBO expects on the target.

    A source may legitimately have several distinct connection types to the
    same target (FEEDS and CONTROLS, say). A duplicate *row* -- the same
    source/type/target declared twice in connections.csv -- is not that; it
    is repeated input, and must not surface as ``[CONTAINS, CONTAINS]``.
    """
    grouped: dict[str, set[str]] = defaultdict(set)
    for connection in site.connections_into(target_code):
        grouped[site.guid(connection.source_code)].add(connection.connection_type)
    return {guid: sorted(types) for guid, types in sorted(grouped.items())}


def _links_block(site: Site, device: Device) -> dict[str, dict[str, str]]:
    """``{source-guid: {this_field: source_field}}`` for a virtual entity."""
    links: dict[str, dict[str, str]] = defaultdict(dict)
    source_guid = site.guid(device.reporting_device_code)
    for mapping in site.mappings_for(device.code):
        if mapping.missing or not mapping.reporting_field:
            continue
        links[source_guid][mapping.dbo_field] = mapping.reporting_field
    return {guid: dict(sorted(fields.items())) for guid, fields in links.items()}


def _entity_for_device(
    ontology: Ontology, site: Site, device: Device
) -> dict[str, Any]:
    entity: dict[str, Any] = {
        "code": device.code,
        "type": device.entity_type,
    }
    connections = _connections_block(site, device.code)
    if connections:
        entity["connections"] = connections

    if device.is_reporting:
        entity["cloud_device_id"] = device.cloud_device_id
        translation = {
            mapping.dbo_field: _translation_for(ontology, mapping)
            for mapping in sorted(
                site.mappings_for(device.code), key=lambda m: m.dbo_field
            )
        }
        if translation:
            entity["translation"] = translation
    else:
        links = _links_block(site, device)
        if links:
            entity["links"] = links
        # A virtual entity has no translation, so it has nowhere to put
        # MISSING. The gap is reported by mapping_validator instead of being
        # smuggled into the config as a non-standard key.
    return entity


def build_config(
    ontology: Ontology, site: Site, operation: str = "INITIALIZE"
) -> dict[str, Any]:
    """Build the building-config document as a plain dict."""
    config: dict[str, Any] = {"CONFIG_METADATA": {"operation": operation}}

    config[site.guid(site.building_code)] = {
        "code": site.building_code,
        "type": "FACILITIES/BUILDING",
    }

    for space in site.spaces:
        entity: dict[str, Any] = {"code": space.code, "type": space.entity_type}
        connections = _connections_block(site, space.code)
        if connections:
            entity["connections"] = connections
        config[site.guid(space.code)] = entity

    for device in site.devices:
        config[site.guid(device.code)] = _entity_for_device(
            ontology, site, device
        )

    return config


def dump_config(config: dict[str, Any]) -> str:
    """Serialise a building config to YAML text."""
    return yaml.dump(
        config,
        Dumper=_ConfigDumper,
        default_flow_style=False,
        sort_keys=False,
        width=100,
        allow_unicode=True,
    )


def write_config(config: dict[str, Any], destination: Path) -> Path:
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(dump_config(config), encoding="utf-8")
    return destination


__all__ = ["build_config", "dump_config", "write_config"]
# AI:E87M claude-code 2026-08-27 s:2a846146
