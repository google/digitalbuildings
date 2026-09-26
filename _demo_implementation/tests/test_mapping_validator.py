"""Tests for the offline mapping checks.

Each test builds the smallest site that exercises one rule, so a failure names
the rule rather than the fixture.
"""

from __future__ import annotations

import pytest

from bms_dbo.mapping_validator import Severity, error_count, validate_site
from bms_dbo.models import Connection, Device, PointMapping, Site, Space

FCU_TYPE = "HVAC/FCU_DFSS_CSP_CHWDC"
FCU_REQUIRED = {
    "chilled_water_valve_percentage_command": ("percent", "%"),
    "discharge_air_temperature_sensor": ("degrees_celsius", "degC"),
    "discharge_air_temperature_setpoint": ("degrees_celsius", "degC"),
    "zone_air_cooling_temperature_setpoint": ("degrees_celsius", "degC"),
    "zone_air_temperature_sensor": ("degrees_celsius", "degC"),
}
FCU_MULTISTATE = ("discharge_fan_run_command", "discharge_fan_run_status")


def _fcu_site(**overrides) -> Site:
    """A minimal, fully valid single-FCU site that tests then perturb."""
    mappings = [
        PointMapping(
            device_code="FCU-1",
            dbo_field=name,
            native_path=f"points.{name}.present_value",
            dbo_unit=unit,
            native_unit=raw,
        )
        for name, (unit, raw) in FCU_REQUIRED.items()
    ]
    mappings += [
        PointMapping(
            device_code="FCU-1",
            dbo_field=name,
            native_path=f"points.{name}.present_value",
            native_states={"ON": "true", "OFF": "false"},
        )
        for name in FCU_MULTISTATE
    ]
    site = Site(
        building_code="AU-TST-DEMO",
        spaces=[Space(code="AU-TST-DEMO-1-101", entity_type="FACILITIES/ROOM")],
        devices=[
            Device(
                code="FCU-1",
                entity_type=FCU_TYPE,
                is_reporting=True,
                cloud_device_id="1234567890",
            )
        ],
        mappings=mappings,
        connections=[
            Connection("AU-TST-DEMO", "CONTAINS", "AU-TST-DEMO-1-101"),
            Connection("AU-TST-DEMO-1-101", "CONTAINS", "FCU-1"),
        ],
    )
    for key, value in overrides.items():
        setattr(site, key, value)
    return site


def _messages(findings, severity=Severity.ERROR):
    return [f.format() for f in findings if f.severity is severity]


class TestBaseline:
    def test_the_reference_site_is_clean(self, ontology):
        findings = validate_site(ontology, _fcu_site())
        assert _messages(findings) == []

    def test_the_shipped_sample_site_has_no_errors(self, ontology, site):
        findings = validate_site(ontology, site)
        assert _messages(findings) == []


class TestFieldNames:
    def test_rejects_a_field_that_is_not_in_the_ontology(self, ontology):
        site = _fcu_site()
        site.mappings.append(
            PointMapping(
                device_code="FCU-1",
                dbo_field="room_temp",  # a native name, not a DBO field
                native_path="points.room_temp.present_value",
            )
        )
        assert any(
            "not a standard field" in m for m in _messages(validate_site(ontology, site))
        )


class TestUnits:
    def test_rejects_a_unit_from_the_wrong_family(self, ontology):
        site = _fcu_site()
        site.mappings[0].dbo_unit = "degrees_celsius"  # a percentage field
        assert any(
            "is not valid for a percentage field" in m
            for m in _messages(validate_site(ontology, site))
        )

    def test_requires_a_unit_on_a_dimensional_field(self, ontology):
        site = _fcu_site()
        site.mappings[0].dbo_unit = ""
        assert any(
            "has no dbo_unit" in m
            for m in _messages(validate_site(ontology, site))
        )

    def test_warns_when_the_raw_unit_string_is_absent(self, ontology):
        site = _fcu_site()
        site.mappings[0].native_unit = ""
        findings = validate_site(ontology, site)
        assert any(
            "no native_unit recorded" in m
            for m in _messages(findings, Severity.WARNING)
        )


class TestStates:
    def test_rejects_a_state_the_field_does_not_define(self, ontology):
        site = _fcu_site()
        site.mappings[-1].native_states = {"OPEN": "1", "CLOSED": "0"}
        assert any(
            "is not valid for this field" in m
            for m in _messages(validate_site(ontology, site))
        )

    def test_requires_a_state_map_on_a_multistate_field(self, ontology):
        site = _fcu_site()
        site.mappings[-1].native_states = {}
        assert any(
            "has no state map" in m
            for m in _messages(validate_site(ontology, site))
        )

    def test_a_field_cannot_be_both_multistate_and_dimensional(self, ontology):
        site = _fcu_site()
        site.mappings[-1].dbo_unit = "percent"
        assert any(
            "must not declare a unit" in m
            for m in _messages(validate_site(ontology, site))
        )


class TestRequiredFields:
    def test_an_undeclared_required_field_is_an_error(self, ontology):
        site = _fcu_site()
        site.mappings = [
            m
            for m in site.mappings
            if m.dbo_field != "zone_air_temperature_sensor"
        ]
        assert any(
            "required by" in m and "not declared" in m
            for m in _messages(validate_site(ontology, site))
        )

    def test_missing_required_field_is_only_a_warning(self, ontology):
        """Recommendation #4: MISSING is valid DBO, not a failure."""
        site = _fcu_site()
        for mapping in site.mappings:
            if mapping.dbo_field == "discharge_air_temperature_setpoint":
                mapping.missing = True
                mapping.native_path = ""
                mapping.dbo_unit = ""
                mapping.native_unit = ""
                mapping.missing_justification = "No such object on the panel."
        findings = validate_site(ontology, site)
        assert error_count(findings) == 0

    def test_the_missing_field_is_still_reported(self, ontology):
        site = _fcu_site()
        for mapping in site.mappings:
            if mapping.dbo_field == "discharge_air_temperature_setpoint":
                mapping.missing = True
                mapping.native_path = ""
                mapping.dbo_unit = ""
                mapping.native_unit = ""
                mapping.missing_justification = "No such object on the panel."
        findings = validate_site(ontology, site)
        assert any(
            "declared MISSING" in m
            for m in _messages(findings, Severity.WARNING)
        )

    def test_a_missing_field_must_not_carry_raw_data(self, ontology):
        site = _fcu_site()
        site.mappings[0].missing = True  # keeps its native_path and unit
        assert any(
            "MISSING field must not set" in m
            for m in _messages(validate_site(ontology, site))
        )

    def test_rejects_a_field_the_type_cannot_declare(self, ontology):
        site = _fcu_site()
        site.mappings.append(
            PointMapping(
                device_code="FCU-1",
                dbo_field="supply_air_flowrate_sensor",  # a VAV point
                native_path="points.flow.present_value",
                dbo_unit="liters_per_second",
                native_unit="L/s",
            )
        )
        assert any(
            "cannot declare this field" in m
            for m in _messages(validate_site(ontology, site))
        )

    def test_rejects_an_abstract_type(self, ontology):
        site = _fcu_site()
        site.devices[0].entity_type = "HVAC/FCU"
        assert any(
            "is abstract" in m for m in _messages(validate_site(ontology, site))
        )


class TestValueRange:
    @pytest.mark.parametrize(
        "low,high,expected_fragment",
        [
            (78.0, 60.0, "is not below value_max"),
            (10.0, 200.0, "above the ontology maximum"),
            (-100.0, 40.0, "below the ontology minimum"),
        ],
    )
    def test_flags_implausible_ranges(self, ontology, low, high, expected_fragment):
        site = _fcu_site()
        for mapping in site.mappings:
            if mapping.dbo_field == "zone_air_temperature_sensor":
                mapping.value_min, mapping.value_max = low, high
        findings = validate_site(ontology, site)
        assert any(expected_fragment in f.format() for f in findings)

    def test_a_plausible_range_passes(self, ontology):
        site = _fcu_site()
        for mapping in site.mappings:
            if mapping.dbo_field == "zone_air_temperature_sensor":
                mapping.value_min, mapping.value_max = 10.0, 40.0
        assert _messages(validate_site(ontology, site)) == []


class TestLocationGraph:
    def test_a_device_with_no_contains_edge_is_flagged(self, ontology):
        """Recommendation #5: location is an edge, and it is required."""
        site = _fcu_site()
        site.connections = [c for c in site.connections if c.target_code != "FCU-1"]
        assert any(
            "no CONTAINS edge" in m
            for m in _messages(validate_site(ontology, site))
        )

    def test_rejects_an_unknown_connection_type(self, ontology):
        site = _fcu_site()
        site.connections.append(Connection("AU-TST-DEMO-1-101", "SERVES", "FCU-1"))
        assert any(
            "unknown connection type" in m
            for m in _messages(validate_site(ontology, site))
        )

    def test_rejects_an_edge_to_an_entity_that_does_not_exist(self, ontology):
        site = _fcu_site()
        site.connections.append(Connection("AHU-99", "FEEDS", "FCU-1"))
        assert any(
            "unknown entity AHU-99" in m
            for m in _messages(validate_site(ontology, site))
        )


class TestGatewayWiring:
    def test_a_virtual_device_needs_a_reporting_field(self, ontology, site):
        for mapping in site.mappings:
            if mapping.device_code == "VAV-L1-01":
                mapping.reporting_field = ""
        assert any(
            "no reporting_field to link from" in m
            for m in _messages(validate_site(ontology, site))
        )

    def test_link_to_a_field_the_gateway_lacks_is_rejected(self, ontology, site):
        for mapping in site.mappings:
            if mapping.device_code == "VAV-L1-01":
                mapping.reporting_field = "zone_air_temperature_sensor_99"
        assert any(
            "which that device does not translate" in m
            for m in _messages(validate_site(ontology, site))
        )

    def test_a_reporting_device_needs_a_native_path(self, ontology):
        site = _fcu_site()
        site.mappings[0].native_path = ""
        assert any(
            "no native_path on a reporting device" in m
            for m in _messages(validate_site(ontology, site))
        )

    def test_virtual_device_must_not_carry_a_cloud_device_id(self, ontology, site):
        site.device("VAV-L1-01").cloud_device_id = "999"
        assert any(
            "must not have a cloud_device_id" in m
            for m in _messages(validate_site(ontology, site))
        )


class TestFacilitiesNaming:
    """Rules the ontology YAML does not state -- only the validator does.

    Sourced from tools/validators/instance_validator/validate/entity_instance.py
    """

    def test_rejects_a_floor_code_that_is_not_a_floor_designator(self, ontology):
        site = _fcu_site()
        site.spaces.append(Space(code="AU-TST-DEMO-L1", entity_type="FACILITIES/FLOOR"))
        assert any(
            "floor code convention" in m
            for m in _messages(validate_site(ontology, site))
        )

    def test_accepts_conventional_floor_codes(self, ontology):
        site = _fcu_site()
        for code in ("AU-TST-DEMO-1", "AU-TST-DEMO-G", "AU-TST-DEMO-B2", "AU-TST-DEMO-3M"):
            site.spaces.append(Space(code=code, entity_type="FACILITIES/FLOOR"))
        assert not [m for m in _messages(validate_site(ontology, site)) if "convention" in m]

    def test_rejects_a_lowercase_room_code(self, ontology):
        site = _fcu_site()
        site.spaces.append(Space(code="AU-TST-DEMO-1-lobby", entity_type="FACILITIES/ROOM"))
        assert any(
            "room code convention" in m
            for m in _messages(validate_site(ontology, site))
        )


class TestMissingJustification:
    """DBO rejects MISSING translations that carry no explanation."""

    def test_missing_without_justification_is_an_error(self, ontology):
        site = _fcu_site()
        for mapping in site.mappings:
            if mapping.dbo_field == "discharge_air_temperature_setpoint":
                mapping.missing = True
                mapping.native_path = ""
                mapping.dbo_unit = ""
                mapping.native_unit = ""
        assert any(
            "no justification" in m
            for m in _messages(validate_site(ontology, site))
        )

    def test_the_sample_site_justifies_its_missing_field(self, ontology, site):
        justified = [
            m for m in site.mappings if m.missing and m.missing_justification
        ]
        assert len(justified) == 1


class TestMissingFieldCarriesNoData:
    """A MISSING field has nothing to report -- including which gateway field
    it would have linked from, on either kind of device."""

    def test_missing_field_must_not_set_reporting_field_on_virtual_device(self):
        mapping = PointMapping(
            "D", "f", missing=True, missing_justification="why",
            reporting_field="ghost_field_1",
        )
        assert any("must not set reporting_field" in p for p in mapping.validate())

    def test_missing_field_must_not_set_reporting_field_on_reporting_device(self, ontology):
        site = _fcu_site()
        site.mappings[0].missing = True
        site.mappings[0].missing_justification = "why"
        site.mappings[0].native_path = ""
        site.mappings[0].native_unit = ""
        site.mappings[0].dbo_unit = ""
        site.mappings[0].reporting_field = "ghost_field_1"
        findings = _messages(validate_site(ontology, site))
        assert any("must not set reporting_field" in m for m in findings)

    def test_the_mistake_is_reported_exactly_once_not_twice(self, ontology):
        """Before the fix, a reporting device got this as a WARNING from the
        reporting-mapping check *and* nothing from the model; a virtual
        device got nothing at all. Now both get exactly one ERROR."""
        site = _fcu_site()
        site.mappings[0].missing = True
        site.mappings[0].missing_justification = "why"
        site.mappings[0].native_path = ""
        site.mappings[0].native_unit = ""
        site.mappings[0].dbo_unit = ""
        site.mappings[0].reporting_field = "ghost_field_1"
        findings = [
            f for f in validate_site(ontology, site)
            if "reporting_field" in f.message
        ]
        assert len(findings) == 1


class TestDuplicateConnections:
    def test_a_repeated_connection_row_is_a_warning(self, ontology):
        site = _fcu_site()
        site.connections.append(Connection("AU-TST-DEMO-1-101", "CONTAINS", "FCU-1"))
        findings = _messages(validate_site(ontology, site), Severity.WARNING)
        assert any("declared 2 times" in m for m in findings)

    def test_a_repeated_row_is_a_warning_not_an_error(self, ontology):
        site = _fcu_site()
        site.connections.append(Connection("AU-TST-DEMO-1-101", "CONTAINS", "FCU-1"))
        assert error_count(validate_site(ontology, site)) == 0

    def test_two_distinct_edge_types_are_not_flagged_as_duplicates(self, ontology):
        site = _fcu_site()
        site.connections.append(Connection("AU-TST-DEMO-1-101", "HAS_RANGE", "FCU-1"))
        findings = _messages(validate_site(ontology, site), Severity.WARNING)
        assert not [m for m in findings if "declared" in m and "times" in m]
# AI:E87M claude-code 2026-08-27 s:2a846146
