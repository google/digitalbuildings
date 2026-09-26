"""Tests for the BMS-side data model.

These checks need no ontology: they are the structural invariants a site must
satisfy before it is worth asking the ontology anything.
"""

from __future__ import annotations

import pytest

from bms_dbo.models import (
    CONNECTION_TYPES,
    Connection,
    Device,
    PointMapping,
    Site,
    Space,
    stable_guid,
    unique,
)


def _site() -> Site:
    return Site(
        building_code="AU-TST-DEMO",
        spaces=[Space(code="AU-TST-DEMO-1-101", entity_type="FACILITIES/ROOM")],
        devices=[
            Device(
                code="GW-1",
                entity_type="GATEWAYS/PASSTHROUGH",
                is_reporting=True,
                cloud_device_id="111",
            ),
            Device(
                code="VAV-1",
                entity_type="HVAC/VAV_SD_DSP",
                is_reporting=False,
                reporting_device_code="GW-1",
            ),
        ],
        mappings=[
            PointMapping(
                device_code="GW-1",
                dbo_field="zone_air_temperature_sensor_1",
                native_path="points.t.present_value",
                native_unit="degC",
                dbo_unit="degrees_celsius",
            ),
            PointMapping(
                device_code="VAV-1",
                dbo_field="zone_air_temperature_sensor",
                reporting_field="zone_air_temperature_sensor_1",
            ),
        ],
        connections=[
            Connection("AU-TST-DEMO", "CONTAINS", "AU-TST-DEMO-1-101"),
            Connection("AU-TST-DEMO-1-101", "CONTAINS", "GW-1"),
            Connection("AU-TST-DEMO-1-101", "CONTAINS", "VAV-1"),
        ],
    )


class TestStableGuid:
    def test_is_deterministic(self):
        assert stable_guid("S", "AHU-1") == stable_guid("S", "AHU-1")

    def test_differs_per_entity_code(self):
        assert stable_guid("S", "AHU-1") != stable_guid("S", "AHU-2")

    def test_differs_per_site(self):
        assert stable_guid("S1", "AHU-1") != stable_guid("S2", "AHU-1")

    def test_has_the_uuid4_version_nibble(self):
        assert stable_guid("S", "AHU-1")[14] == "4"

    def test_has_uuid_shape(self):
        guid = stable_guid("S", "AHU-1")
        assert len(guid) == 36 and guid.count("-") == 4


class TestDeviceInvariants:
    def test_a_valid_reporting_device_has_no_problems(self):
        device = Device("AHU-1", "HVAC/AHU", True, cloud_device_id="123")
        assert device.validate() == []

    def test_a_reporting_device_needs_a_cloud_device_id(self):
        device = Device("AHU-1", "HVAC/AHU", True)
        assert any("no cloud_device_id" in p for p in device.validate())

    def test_a_reporting_device_must_not_also_link(self):
        device = Device("AHU-1", "HVAC/AHU", True, "123", reporting_device_code="GW-1")
        assert any("must not also point at" in p for p in device.validate())

    def test_a_virtual_device_must_not_have_a_cloud_device_id(self):
        device = Device("VAV-1", "HVAC/VAV_SD_DSP", False, cloud_device_id="123")
        assert any("must not have a cloud_device_id" in p for p in device.validate())

    def test_derives_namespace_and_general_type_from_the_type(self):
        device = Device("VAV-1", "HVAC/VAV_SD_DSP", False, reporting_device_code="GW-1")
        assert (device.namespace, device.general_type) == ("HVAC", "VAV")


class TestPointMappingInvariants:
    def test_a_plain_mapping_is_valid(self):
        mapping = PointMapping("D", "zone_air_temperature_sensor", "points.t.present_value")
        assert mapping.validate() == []

    @pytest.mark.parametrize(
        "attribute,value",
        [("native_path", "points.t"), ("native_unit", "degC"), ("dbo_unit", "kelvin")],
    )
    def test_a_missing_field_must_not_carry_raw_data(self, attribute, value):
        mapping = PointMapping("D", "f", missing=True, missing_justification="why")
        setattr(mapping, attribute, value)
        assert any(f"must not set {attribute}" in p for p in mapping.validate())

    def test_a_missing_field_must_not_carry_states(self):
        mapping = PointMapping(
            "D", "f", missing=True, missing_justification="why",
            native_states={"ON": "1"},
        )
        assert any("must not set native_states" in p for p in mapping.validate())

    def test_a_missing_field_needs_a_justification(self):
        mapping = PointMapping("D", "f", missing=True)
        assert any("no justification" in p for p in mapping.validate())

    def test_a_justified_missing_field_is_valid(self):
        mapping = PointMapping("D", "f", missing=True, missing_justification="No object.")
        assert mapping.validate() == []

    def test_a_field_cannot_be_both_multistate_and_dimensional(self):
        mapping = PointMapping(
            "D", "f", "points.t", dbo_unit="percent", native_states={"ON": "1"}
        )
        assert any("never both" in p for p in mapping.validate())

    def test_has_range_needs_both_bounds(self):
        assert PointMapping("D", "f", value_min=1.0).has_range is False

    def test_has_range_is_true_with_both_bounds(self):
        assert PointMapping("D", "f", value_min=1.0, value_max=2.0).has_range is True


class TestConnectionInvariants:
    def test_a_known_type_is_valid(self):
        assert Connection("A", "FEEDS", "B").validate() == []

    def test_an_unknown_type_is_rejected(self):
        assert any("unknown connection type" in p for p in Connection("A", "SERVES", "B").validate())

    def test_a_self_edge_is_rejected(self):
        assert any("connected to itself" in p for p in Connection("A", "FEEDS", "A").validate())

    def test_the_ontology_misspelling_is_accepted(self):
        """The ontology really does spell it PARIALLY_AGGREGATES."""
        assert "PARIALLY_AGGREGATES" in CONNECTION_TYPES


class TestSiteLookups:
    def test_finds_a_device_by_code(self):
        assert _site().device("VAV-1").entity_type == "HVAC/VAV_SD_DSP"

    def test_returns_none_for_an_unknown_device(self):
        assert _site().device("NOPE") is None

    def test_finds_a_space_by_code(self):
        assert _site().space("AU-TST-DEMO-1-101") is not None

    def test_entity_codes_include_the_building(self):
        assert "AU-TST-DEMO" in _site().entity_codes()

    def test_connections_into_selects_by_target(self):
        edges = _site().connections_into("VAV-1")
        assert [e.source_code for e in edges] == ["AU-TST-DEMO-1-101"]

    def test_declared_fields_include_missing_ones(self):
        site = _site()
        site.mappings.append(
            PointMapping("VAV-1", "supply_air_flowrate_sensor", missing=True,
                         missing_justification="No flow ring fitted.")
        )
        declared = site.declared_fields("VAV-1")
        mapped = site.mapped_fields("VAV-1")
        assert "supply_air_flowrate_sensor" in declared - mapped


class TestSiteInvariants:
    def test_the_reference_site_is_structurally_sound(self):
        assert _site().validate() == []

    def test_duplicate_entity_codes_are_reported(self):
        site = _site()
        site.spaces.append(Space(code="VAV-1", entity_type="FACILITIES/ROOM"))
        assert any("duplicate entity code" in p for p in site.validate())

    def test_a_mapping_for_an_unknown_device_is_reported(self):
        site = _site()
        site.mappings.append(PointMapping("GHOST-1", "f", "points.t"))
        assert any("unknown device GHOST-1" in p for p in site.validate())

    def test_an_edge_to_an_unknown_entity_is_reported(self):
        site = _site()
        site.connections.append(Connection("AHU-9", "FEEDS", "VAV-1"))
        assert any("unknown entity AHU-9" in p for p in site.validate())

    def test_a_device_with_no_contains_edge_is_reported(self):
        site = _site()
        site.connections = [c for c in site.connections if c.target_code != "VAV-1"]
        assert any("no CONTAINS edge" in p for p in site.validate())

    def test_a_virtual_device_carrying_points_needs_a_gateway(self):
        site = _site()
        site.device("VAV-1").reporting_device_code = ""
        assert any("names no reporting device" in p for p in site.validate())

    def test_a_zone_style_entity_needs_no_gateway(self):
        """Zones are virtual entities with no links, which is valid DBO."""
        site = _site()
        site.devices.append(Device("ZONE-1", "HVAC/ZONE_HVAC", False))
        site.connections.append(Connection("AU-TST-DEMO-1-101", "CONTAINS", "ZONE-1"))
        assert not [p for p in site.validate() if "ZONE-1" in p]

    def test_a_gateway_that_is_itself_virtual_is_reported(self):
        site = _site()
        site.device("GW-1").is_reporting = False
        site.device("GW-1").cloud_device_id = ""
        assert any("is itself virtual" in p for p in site.validate())


class TestUnique:
    def test_preserves_first_seen_order(self):
        assert unique(["b", "a", "b", "c", "a"]) == ["b", "a", "c"]

    def test_handles_an_empty_sequence(self):
        assert unique([]) == []
# AI:E87M claude-code 2026-08-27 s:2a846146
