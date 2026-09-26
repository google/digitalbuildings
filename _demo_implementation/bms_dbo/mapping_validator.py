"""Validate point mappings against the pinned ontology.

This is the value the BMS adds over a spreadsheet: every mapping row is checked
while the engineer is still in front of the panel, not after the config reaches
the cloud. The checks are the ones the ontology can actually decide:

* is ``dbo_field`` a real standard field (allowing for enumeration suffixes)?
* can the device's type declare that field at all?
* dimensional field -> is a unit set, and is it in the field's unit family?
* multistate field -> are the declared states legal for that field?
* are all the type's required fields declared (mapped or MISSING)?

Everything here runs offline against the vendored ontology. It is deliberately
*not* a re-implementation of tools/validators/instance_validator -- that stays
the authority, and ci/validate.sh runs it. This is the fast inner loop.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .models import PointMapping, Site
from .naming import check_code
from .ontology import Ontology, strip_enumeration


class Severity(str, Enum):
    ERROR = "ERROR"
    WARNING = "WARNING"

    def __str__(self) -> str:  # pragma: no cover - display only
        return self.value


@dataclass(frozen=True)
class Finding:
    severity: Severity
    entity: str
    field_name: str
    message: str

    def format(self) -> str:
        where = f"{self.entity}/{self.field_name}" if self.field_name else self.entity
        return f"[{self.severity}] {where}: {self.message}"


def _check_field_exists(
    ontology: Ontology, mapping: PointMapping
) -> list[Finding]:
    if ontology.is_valid_field(mapping.dbo_field):
        return []
    base = strip_enumeration(mapping.dbo_field)
    hint = ""
    if base != mapping.dbo_field:
        hint = f" (enumeration stripped to {base!r})"
    return [
        Finding(
            Severity.ERROR,
            mapping.device_code,
            mapping.dbo_field,
            f"not a standard field in the pinned ontology{hint}",
        )
    ]


def _check_units_and_states(
    ontology: Ontology, mapping: PointMapping
) -> list[Finding]:
    """Unit and state checks, for reporting entities only.

    A virtual entity declares no units or states: it links to a field on the
    reporting entity, and the translation there already carries the unit and
    state maps. Checking a link for units would demand data DBO has no place
    to put.
    """
    definition = ontology.get_field(mapping.dbo_field)
    if definition is None or mapping.missing:
        return []

    findings: list[Finding] = []
    entity, name = mapping.device_code, mapping.dbo_field

    if definition.is_multistate:
        if mapping.dbo_unit:
            findings.append(
                Finding(
                    Severity.ERROR,
                    entity,
                    name,
                    "multistate field must not declare a unit",
                )
            )
        if not mapping.native_states:
            findings.append(
                Finding(
                    Severity.ERROR,
                    entity,
                    name,
                    "multistate field has no state map; expected one of "
                    f"{sorted(definition.states)}",
                )
            )
        for state in mapping.native_states:
            if state not in definition.states:
                findings.append(
                    Finding(
                        Severity.ERROR,
                        entity,
                        name,
                        f"state {state!r} is not valid for this field; "
                        f"allowed: {sorted(definition.states)}",
                    )
                )
            elif state not in ontology.states:
                findings.append(
                    Finding(
                        Severity.ERROR,
                        entity,
                        name,
                        f"state {state!r} is not defined in states.yaml",
                    )
                )
        return findings

    measurement = ontology.measurement_of(name)
    if measurement is None:
        # Countable or dimensionless point types carry no unit.
        if mapping.dbo_unit:
            findings.append(
                Finding(
                    Severity.WARNING,
                    entity,
                    name,
                    f"field has no measurement subfield but declares unit "
                    f"{mapping.dbo_unit!r}",
                )
            )
        return findings

    valid_units = ontology.units_for_field(name)
    if not mapping.dbo_unit:
        findings.append(
            Finding(
                Severity.ERROR,
                entity,
                name,
                f"dimensional field ({measurement}) has no dbo_unit; "
                f"expected one of {sorted(valid_units)}",
            )
        )
    elif mapping.dbo_unit not in valid_units:
        findings.append(
            Finding(
                Severity.ERROR,
                entity,
                name,
                f"unit {mapping.dbo_unit!r} is not valid for a {measurement} "
                f"field; expected one of {sorted(valid_units)}",
            )
        )
    if mapping.native_states:
        findings.append(
            Finding(
                Severity.ERROR,
                entity,
                name,
                "dimensional field must not declare a state map",
            )
        )
    if not mapping.native_unit and mapping.dbo_unit:
        findings.append(
            Finding(
                Severity.WARNING,
                entity,
                name,
                "no native_unit recorded; the raw unit string is needed to "
                "build the translation's units block",
            )
        )
    findings.extend(_check_value_range(ontology, mapping))
    return findings


def _check_value_range(
    ontology: Ontology, mapping: PointMapping
) -> list[Finding]:
    """A device-specific range must sit inside the ontology's envelope.

    The ontology envelope is the physically plausible range for the field;
    the engineer's range is what this device should actually produce. A range
    outside the envelope means the unit is wrong -- a Fahrenheit setpoint
    mapped as celsius, say -- which is exactly the mistake that is invisible
    until someone looks at a trend six months later.
    """
    if not mapping.has_range or not mapping.dbo_unit:
        return []
    entity, name = mapping.device_code, mapping.dbo_field
    if mapping.value_min >= mapping.value_max:
        return [
            Finding(
                Severity.ERROR,
                entity,
                name,
                f"value_min ({mapping.value_min}) is not below value_max "
                f"({mapping.value_max})",
            )
        ]
    try:
        low, high = ontology.range_in_unit(name, mapping.dbo_unit)
    except Exception:  # noqa: BLE001 - unit already reported as invalid above
        return []
    findings: list[Finding] = []
    if low is not None and mapping.value_min < low:
        findings.append(
            Finding(
                Severity.WARNING,
                entity,
                name,
                f"value_min {mapping.value_min} is below the ontology minimum "
                f"of {round(low, 4)} {mapping.dbo_unit}; check the unit",
            )
        )
    if high is not None and mapping.value_max > high:
        findings.append(
            Finding(
                Severity.WARNING,
                entity,
                name,
                f"value_max {mapping.value_max} is above the ontology maximum "
                f"of {round(high, 4)} {mapping.dbo_unit}; check the unit",
            )
        )
    return findings


def _check_against_type(
    ontology: Ontology, site: Site, device_code: str
) -> list[Finding]:
    device = site.device(device_code)
    if device is None:
        return []

    try:
        resolved = ontology.resolve(device.entity_type)
    except Exception as error:  # noqa: BLE001 - surfaced as a finding
        return [
            Finding(
                Severity.ERROR, device.code, "", f"unusable entity type: {error}"
            )
        ]

    findings: list[Finding] = []
    if resolved.entity_type.is_abstract:
        findings.append(
            Finding(
                Severity.ERROR,
                device.code,
                "",
                f"{device.entity_type} is abstract and cannot be assigned to "
                "an entity",
            )
        )

    declared = {strip_enumeration(f) for f in site.declared_fields(device_code)}
    mapped = {strip_enumeration(f) for f in site.mapped_fields(device_code)}

    for absent in sorted(resolved.required - declared):
        findings.append(
            Finding(
                Severity.ERROR,
                device.code,
                absent,
                f"required by {device.entity_type} but not declared; map it "
                "or declare it MISSING",
            )
        )

    for absent in sorted(resolved.required - mapped):
        if absent in declared:
            findings.append(
                Finding(
                    Severity.WARNING,
                    device.code,
                    absent,
                    f"required by {device.entity_type} and declared MISSING; "
                    "analytics depending on this type will not get this point",
                )
            )

    if not resolved.entity_type.allow_undefined_fields:
        for extra in sorted(declared - resolved.declarable):
            findings.append(
                Finding(
                    Severity.ERROR,
                    device.code,
                    extra,
                    f"{device.entity_type} cannot declare this field; pick a "
                    "type that covers it or drop the mapping",
                )
            )

    return findings


def _check_reporting_mapping(device, mapping: PointMapping) -> list[Finding]:
    """A reporting entity translates its own payload -- it needs a raw path.

    A MISSING mapping with a stray ``reporting_field`` is already caught by
    ``PointMapping.validate()`` (MISSING carries no raw data of any kind), so
    this warning is scoped to the non-missing case -- otherwise the same
    mistake reports twice, once as this WARNING and once as that ERROR.
    """
    findings: list[Finding] = []
    if mapping.reporting_field and not mapping.missing:
        findings.append(
            Finding(
                Severity.WARNING,
                device.code,
                mapping.dbo_field,
                "reporting device does not need a reporting_field; it "
                "translates its own payload",
            )
        )
    if not mapping.missing and not mapping.native_path:
        findings.append(
            Finding(
                Severity.ERROR,
                device.code,
                mapping.dbo_field,
                "no native_path on a reporting device -- map the point or "
                "declare the field MISSING",
            )
        )
    return findings


def _check_virtual_mapping(
    site: Site, device, mapping: PointMapping
) -> list[Finding]:
    """A virtual entity's data arrives by link, so the source must exist."""
    if mapping.missing:
        return []
    if mapping.dbo_unit or mapping.native_states or mapping.native_path:
        return [
            Finding(
                Severity.WARNING,
                device.code,
                mapping.dbo_field,
                "virtual device field carries raw path/unit/state data; those "
                "belong on the reporting entity's translation and are ignored "
                "here",
            )
        ]
    if not mapping.reporting_field:
        return [
            Finding(
                Severity.ERROR,
                device.code,
                mapping.dbo_field,
                "virtual device field has no reporting_field to link from",
            )
        ]
    gateway = site.device(device.reporting_device_code)
    if gateway is None:
        return []
    gateway_fields = {m.dbo_field for m in site.mappings_for(gateway.code)}
    if mapping.reporting_field not in gateway_fields:
        return [
            Finding(
                Severity.ERROR,
                device.code,
                mapping.dbo_field,
                f"links to {gateway.code}.{mapping.reporting_field}, which "
                "that device does not translate",
            )
        ]
    return []


def _check_link_wiring(site: Site) -> list[Finding]:
    """Check every mapping is wired the way its device kind requires."""
    findings: list[Finding] = []
    for device in site.devices:
        for mapping in site.mappings_for(device.code):
            if device.is_reporting:
                findings.extend(_check_reporting_mapping(device, mapping))
            else:
                findings.extend(
                    _check_virtual_mapping(site, device, mapping)
                )
    return findings


def _check_duplicate_connections(site: Site) -> list[Finding]:
    """Flag a (source, type, target) row declared more than once.

    The exporter deduplicates these before they reach the config, so a
    duplicate row is never wrong output -- but it usually means a copy-paste
    slip in connections.csv, so it is worth a warning rather than silence.
    """
    seen: dict[tuple[str, str, str], int] = {}
    for connection in site.connections:
        key = (
            connection.source_code,
            connection.connection_type,
            connection.target_code,
        )
        seen[key] = seen.get(key, 0) + 1
    return [
        Finding(
            Severity.WARNING,
            target,
            "",
            f"{source} {ctype} {target} is declared {count} times in "
            "connections.csv; duplicates are harmless (the exporter merges "
            "them) but usually mean a copy-paste mistake",
        )
        for (source, ctype, target), count in sorted(seen.items())
        if count > 1
    ]


def _check_locations(site: Site) -> list[Finding]:
    """Recommendation #5 -- location lives in the edge table."""
    findings: list[Finding] = list(_check_duplicate_connections(site))

    building_problem = check_code(site.building_code, "FACILITIES/BUILDING")
    if building_problem:
        findings.append(
            Finding(Severity.ERROR, site.building_code, "", building_problem)
        )
    for space in site.spaces:
        problem = check_code(space.code, space.entity_type)
        if problem:
            findings.append(Finding(Severity.ERROR, space.code, "", problem))

    for connection in site.connections:
        if connection.connection_type != "CONTAINS":
            continue
        if site.space(connection.source_code) is None and (
            connection.source_code != site.building_code
        ):
            findings.append(
                Finding(
                    Severity.WARNING,
                    connection.target_code,
                    "",
                    f"CONTAINS source {connection.source_code} is not a "
                    "FACILITIES space",
                )
            )
    return findings


def validate_site(ontology: Ontology, site: Site) -> list[Finding]:
    """Run every check and return findings, errors first."""
    findings: list[Finding] = [
        Finding(Severity.ERROR, "site", "", problem)
        for problem in site.validate()
    ]

    for mapping in site.mappings:
        findings.extend(_check_field_exists(ontology, mapping))
        device = site.device(mapping.device_code)
        # Units and states are a property of the translation, which only a
        # reporting entity has.
        if device is not None and device.is_reporting:
            findings.extend(_check_units_and_states(ontology, mapping))

    for device in site.devices:
        findings.extend(_check_against_type(ontology, site, device.code))

    findings.extend(_check_link_wiring(site))
    findings.extend(_check_locations(site))

    findings.sort(key=lambda f: (f.severity != Severity.ERROR, f.entity, f.field_name))
    return findings


def error_count(findings: list[Finding]) -> int:
    return sum(1 for f in findings if f.severity is Severity.ERROR)
# AI:E87M claude-code 2026-08-27 s:2a846146
