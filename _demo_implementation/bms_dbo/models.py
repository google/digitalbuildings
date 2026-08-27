"""The BMS-side data model.

This is the shape recommendations #1, #4 and #5 argue for:

* #1 -- a mapping row keeps the **native** point *and* its DBO meaning side by
  side. Neither replaces the other. ``native_path`` stays authoritative for
  polling; ``dbo_field`` is what analytics and the exported building config see.
* #4 -- ``PointMapping.missing`` is a real state, not an absent row. A field
  that a type requires but the device cannot supply is declared ``MISSING``,
  which is valid DBO. Dropping the row instead fails instance validation.
* #5 -- location is a :class:`Connection` edge (``CONTAINS``), not a column on
  the device. The same edge table carries ``FEEDS``, ``HAS_PART`` and friends.

These are plain dataclasses so the demo has no ORM dependency. ``schema.sql``
holds the equivalent relational definition.
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from typing import Iterable, Iterator

# The ten relationship types in ontology/yaml/resources/connections/.
CONNECTION_TYPES = frozenset(
    {
        "CONTAINS",
        "CONTROLS",
        "FEEDS",
        "FULLY_AGGREGATES",
        "HAS_PART",
        "HAS_RANGE",
        "MEASURES",
        "MEASURES_TYPE",
        "PARIALLY_AGGREGATES",  # spelled this way in the ontology
        "PARTIALLY_AGGREGATES",
    }
)

# DBO expects UUID4. uuid5 gives us a *stable* id for a given site+code, so
# regenerating a building config produces a reviewable diff instead of noise.
# Production onboarding should use tools/guid_generator instead.
_GUID_NAMESPACE = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")


def stable_guid(site_code: str, entity_code: str) -> str:
    """Deterministic, UUID4-shaped identifier for ``site_code:entity_code``."""
    derived = uuid.uuid5(_GUID_NAMESPACE, f"{site_code}:{entity_code}")
    # Force the version nibble to 4 so the value satisfies UUID4-shaped checks.
    as_int = (derived.int & ~(0xF << 76)) | (4 << 76)
    return str(uuid.UUID(int=as_int))


@dataclass
class Space:
    """A FACILITIES entity: building, floor, room, corridor, ..."""

    code: str
    entity_type: str  # e.g. "FACILITIES/ROOM"
    display_name: str = ""

    @property
    def namespace(self) -> str:
        return self.entity_type.split("/")[0]


@dataclass
class Device:
    """A piece of equipment, reporting or virtual.

    ``is_reporting`` decides how the exporter treats it:

    * reporting -- owns a ``cloud_device_id`` and emits a ``translation``
    * virtual   -- owns no telemetry; its fields arrive via ``links`` from
      ``reporting_device_code`` (typically a gateway)
    """

    code: str
    entity_type: str  # e.g. "HVAC/VAV_SD_DSP"
    is_reporting: bool
    cloud_device_id: str = ""
    display_name: str = ""
    reporting_device_code: str = ""

    @property
    def namespace(self) -> str:
        return self.entity_type.split("/")[0]

    @property
    def type_name(self) -> str:
        return self.entity_type.split("/")[-1]

    @property
    def general_type(self) -> str:
        return self.type_name.split("_", 1)[0]

    def validate(self) -> list[str]:
        problems: list[str] = []
        if self.is_reporting and not self.cloud_device_id:
            problems.append(
                f"{self.code}: reporting device has no cloud_device_id"
            )
        if self.is_reporting and self.reporting_device_code:
            problems.append(
                f"{self.code}: reporting device must not also point at a "
                f"reporting device ({self.reporting_device_code}); DBO advises "
                "against mixing translations and links on one entity"
            )
        if not self.is_reporting and self.cloud_device_id:
            problems.append(
                f"{self.code}: virtual device must not have a cloud_device_id"
            )
        return problems


@dataclass
class PointMapping:
    """One native BMS point bound to one DBO standard field.

    ``native_*`` is what the driver actually polls. ``dbo_*`` is what the
    ontology calls it. Keeping both on one row is the whole point of
    recommendation #1 -- the mapping is data, reviewable and re-exportable,
    not a transformation buried in an export script.
    """

    device_code: str
    dbo_field: str
    native_path: str = ""
    native_unit: str = ""
    dbo_unit: str = ""
    native_states: dict[str, str] = field(default_factory=dict)
    missing: bool = False
    # Set when the point is reported by a gateway on behalf of a virtual
    # device: the (enumerated) field name as the gateway publishes it.
    reporting_field: str = ""
    # Device-specific expected range, in ``dbo_unit``. Optional, but DBO uses
    # it for telemetry data-quality scoring and to validate writeback
    # requests, so it is worth capturing at commissioning time.
    value_min: float | None = None
    value_max: float | None = None
    # Why this required field cannot be supplied. The DBO instance validator
    # states plainly: "You must provide justification for all MISSING
    # translations ... otherwise your building config will be rejected."
    missing_justification: str = ""

    @property
    def has_range(self) -> bool:
        return self.value_min is not None and self.value_max is not None

    def validate(self) -> list[str]:
        problems: list[str] = []
        if self.missing:
            # ABEL is explicit: a MISSING field carries no raw name, no raw
            # unit path and no raw unit value. reporting_field belongs to the
            # same "no raw data at all" rule -- a field with nothing to
            # report has no gateway field to link from either.
            for attribute in ("native_path", "native_unit", "dbo_unit", "reporting_field"):
                if getattr(self, attribute):
                    problems.append(
                        f"{self.device_code}/{self.dbo_field}: MISSING field "
                        f"must not set {attribute}"
                    )
            if self.native_states:
                problems.append(
                    f"{self.device_code}/{self.dbo_field}: MISSING field must "
                    "not set native_states"
                )
            if not self.missing_justification:
                problems.append(
                    f"{self.device_code}/{self.dbo_field}: MISSING field has "
                    "no justification; DBO requires one or the config is "
                    "rejected on review"
                )
        if self.native_states and self.dbo_unit:
            problems.append(
                f"{self.device_code}/{self.dbo_field}: a field is either "
                "multistate or dimensional, never both"
            )
        return problems


@dataclass
class Connection:
    """A directed edge: *source* --<type>--> *target*.

    DBO declares connections on the target, listing sources. We store the edge
    in its natural direction and let the exporter invert it.
    """

    source_code: str
    connection_type: str
    target_code: str

    def validate(self) -> list[str]:
        if self.connection_type not in CONNECTION_TYPES:
            return [
                f"{self.source_code} -> {self.target_code}: unknown connection "
                f"type {self.connection_type!r}"
            ]
        if self.source_code == self.target_code:
            return [f"{self.source_code}: entity connected to itself"]
        return []


@dataclass
class Site:
    """Everything the BMS knows about one building."""

    building_code: str
    spaces: list[Space] = field(default_factory=list)
    devices: list[Device] = field(default_factory=list)
    mappings: list[PointMapping] = field(default_factory=list)
    connections: list[Connection] = field(default_factory=list)

    # ---------------------------------------------------------------- lookups

    def device(self, code: str) -> Device | None:
        return next((d for d in self.devices if d.code == code), None)

    def space(self, code: str) -> Space | None:
        return next((s for s in self.spaces if s.code == code), None)

    def entity_codes(self) -> set[str]:
        codes = {self.building_code}
        codes.update(s.code for s in self.spaces)
        codes.update(d.code for d in self.devices)
        return codes

    def mappings_for(self, device_code: str) -> list[PointMapping]:
        return [m for m in self.mappings if m.device_code == device_code]

    def declared_fields(self, device_code: str) -> set[str]:
        """Every field the device will declare, MISSING ones included.

        Type satisfaction is judged on what the translation *declares*, which
        is why MISSING counts here (recommendation #4).
        """
        return {m.dbo_field for m in self.mappings_for(device_code)}

    def mapped_fields(self, device_code: str) -> set[str]:
        """Fields with real telemetry behind them."""
        return {
            m.dbo_field for m in self.mappings_for(device_code) if not m.missing
        }

    def connections_into(self, target_code: str) -> list[Connection]:
        return [c for c in self.connections if c.target_code == target_code]

    def guid(self, entity_code: str) -> str:
        return stable_guid(self.building_code, entity_code)

    # ------------------------------------------------------------- invariants

    def _duplicate_codes(self) -> list[str]:
        seen: set[str] = set()
        problems: list[str] = []
        all_codes = (
            [self.building_code]
            + [s.code for s in self.spaces]
            + [d.code for d in self.devices]
        )
        for code in all_codes:
            if code in seen:
                problems.append(
                    f"duplicate entity code: {code} -- codes must be unique "
                    "within a building config"
                )
            seen.add(code)
        return problems

    def _device_problems(self, device: Device) -> list[str]:
        problems = list(device.validate())
        # A virtual device only needs a gateway once it actually carries
        # data. Zones and control groups are virtual entities with no links
        # at all, which is valid DBO.
        if (
            not device.is_reporting
            and not device.reporting_device_code
            and any(not m.missing for m in self.mappings_for(device.code))
        ):
            problems.append(
                f"{device.code}: virtual device carries mapped points but "
                "names no reporting device to link them from"
            )
        if device.reporting_device_code:
            gateway = self.device(device.reporting_device_code)
            if gateway is None:
                problems.append(
                    f"{device.code}: reporting device "
                    f"{device.reporting_device_code} is not in this site"
                )
            elif not gateway.is_reporting:
                problems.append(
                    f"{device.code}: reporting device "
                    f"{gateway.code} is itself virtual"
                )
        return problems

    def validate(self) -> list[str]:
        """Structural checks that need no ontology -- codes, edges, duplicates."""
        known = self.entity_codes()
        problems: list[str] = self._duplicate_codes()

        for device in self.devices:
            problems.extend(self._device_problems(device))

        for mapping in self.mappings:
            problems.extend(mapping.validate())
            if mapping.device_code not in known:
                problems.append(
                    f"mapping references unknown device {mapping.device_code}"
                )

        for connection in self.connections:
            problems.extend(connection.validate())
            for code in (connection.source_code, connection.target_code):
                if code not in known:
                    problems.append(f"connection references unknown entity {code}")

        problems.extend(self._unlocated_devices())
        return problems

    def _unlocated_devices(self) -> Iterator[str]:
        """Recommendation #5: every device should sit somewhere in the graph."""
        located = {
            c.target_code
            for c in self.connections
            if c.connection_type == "CONTAINS"
        }
        for device in self.devices:
            if device.code not in located:
                yield (
                    f"{device.code}: no CONTAINS edge -- device has no location "
                    "in the spatial graph"
                )


def unique(values: Iterable[str]) -> list[str]:
    """Order-preserving de-duplication, used when building report output."""
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result
# AI:E87M claude-code 2026-08-27 s:2a846146
