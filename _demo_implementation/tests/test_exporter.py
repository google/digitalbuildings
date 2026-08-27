"""Tests for building-config generation."""

from __future__ import annotations

import yaml

from bms_dbo.exporter import build_config, dump_config
from bms_dbo.models import Connection, stable_guid
from bms_dbo.ontology import DboLoader


def _reload(config: dict) -> dict:
    """Round-trip through YAML the way a consumer would read it back."""
    text = dump_config(config)
    loader = DboLoader(text)
    try:
        return loader.get_single_data()
    finally:
        loader.dispose()


def _entity(config: dict, code: str) -> dict:
    return next(
        body
        for key, body in config.items()
        if key != "CONFIG_METADATA" and body.get("code") == code
    )


class TestDocumentShape:
    def test_declares_the_config_operation(self, ontology, site):
        config = build_config(ontology, site)
        assert config["CONFIG_METADATA"] == {"operation": "INITIALIZE"}

    def test_every_entity_is_keyed_by_guid(self, ontology, site):
        config = build_config(ontology, site)
        keys = [k for k in config if k != "CONFIG_METADATA"]
        assert all(len(k) == 36 and k.count("-") == 4 for k in keys)

    def test_entity_count_matches_the_site(self, ontology, site):
        config = build_config(ontology, site)
        expected = 1 + len(site.spaces) + len(site.devices)  # +1 building
        assert len(config) - 1 == expected

    def test_guids_are_stable_across_runs(self, ontology, site):
        first = build_config(ontology, site)
        second = build_config(ontology, site)
        assert list(first) == list(second)

    def test_guid_depends_on_both_site_and_code(self):
        assert stable_guid("SITE-A", "AHU-1") != stable_guid("SITE-B", "AHU-1")

    def test_guid_is_uuid4_shaped(self):
        assert stable_guid("SITE-A", "AHU-1")[14] == "4"


class TestReportingEntities:
    def test_carries_its_cloud_device_id(self, ontology, site):
        ahu = _entity(build_config(ontology, site), "AHU-1")
        assert ahu["cloud_device_id"] == "2599571827844401"

    def test_translation_is_keyed_by_standard_field(self, ontology, site):
        ahu = _entity(build_config(ontology, site), "AHU-1")
        assert "discharge_air_temperature_sensor" in ahu["translation"]

    def test_native_path_becomes_present_value(self, ontology, site):
        ahu = _entity(build_config(ontology, site), "AHU-1")
        entry = ahu["translation"]["discharge_air_temperature_sensor"]
        assert entry["present_value"] == "points.supply_air_temp.present_value"

    def test_units_block_maps_dbo_unit_to_the_raw_string(self, ontology, site):
        ahu = _entity(build_config(ontology, site), "AHU-1")
        entry = ahu["translation"]["discharge_air_temperature_sensor"]
        assert entry["units"]["values"] == {"degrees_celsius": "degC"}

    def test_units_key_is_derived_from_the_present_value_path(self, ontology, site):
        ahu = _entity(build_config(ontology, site), "AHU-1")
        entry = ahu["translation"]["discharge_air_temperature_sensor"]
        assert entry["units"]["key"] == "pointset.points.supply_air_temp.units"

    def test_value_range_is_emitted_only_when_supplied(self, ontology, site):
        ahu = _entity(build_config(ontology, site), "AHU-1")
        translation = ahu["translation"]
        supplied = translation["discharge_air_temperature_sensor"]["value_range"]
        # chilled_water_valve_percentage_sensor has no range in the CSV, so the
        # exporter must not invent one from the ontology envelope.
        derived = "value_range" in translation["chilled_water_valve_percentage_sensor"]
        assert (supplied, derived) == ("10,30", False)

    def test_multistate_field_emits_a_state_map(self, ontology, site):
        ahu = _entity(build_config(ontology, site), "AHU-1")
        entry = ahu["translation"]["discharge_fan_run_command"]
        assert entry["states"] == {"ON": "active", "OFF": "inactive"}

    def test_a_multistate_field_has_no_units(self, ontology, site):
        ahu = _entity(build_config(ontology, site), "AHU-1")
        assert "units" not in ahu["translation"]["discharge_fan_run_command"]


class TestMissingFields:
    def test_missing_is_the_literal_string(self, ontology, site):
        fcu = _entity(build_config(ontology, site), "FCU-1")
        assert fcu["translation"]["discharge_air_temperature_setpoint"] == "MISSING"

    def test_the_missing_field_is_present_not_dropped(self, ontology, site):
        """Recommendation #4 -- dropping the key would fail DBO validation."""
        fcu = _entity(build_config(ontology, site), "FCU-1")
        assert "discharge_air_temperature_setpoint" in fcu["translation"]


class TestVirtualEntities:
    def test_has_links_and_no_translation(self, ontology, site):
        vav = _entity(build_config(ontology, site), "VAV-L1-01")
        assert "links" in vav and "translation" not in vav

    def test_links_are_keyed_by_the_gateway_guid(self, ontology, site):
        config = build_config(ontology, site)
        vav = _entity(config, "VAV-L1-01")
        assert list(vav["links"]) == [stable_guid(site.building_code, "GW-1")]

    def test_link_maps_local_field_to_gateway_field(self, ontology, site):
        vav = _entity(build_config(ontology, site), "VAV-L1-01")
        links = next(iter(vav["links"].values()))
        assert links["zone_air_temperature_sensor"] == (
            "zone_air_temperature_sensor_1"
        )

    def test_a_virtual_entity_has_no_cloud_device_id(self, ontology, site):
        vav = _entity(build_config(ontology, site), "VAV-L1-01")
        assert "cloud_device_id" not in vav

    def test_a_virtual_entity_keeps_its_connections(self, ontology, site):
        vav = _entity(build_config(ontology, site), "VAV-L1-02")
        assert len(vav["connections"]) == 2  # CONTAINS from room, FEEDS from AHU


class TestConnections:
    def test_connections_are_declared_on_the_target(self, ontology, site):
        """DBO lists sources on the target entity, not the other way round."""
        config = build_config(ontology, site)
        vav = _entity(config, "VAV-L1-01")
        room_guid = stable_guid(site.building_code, "AU-MEL-DEMO-1-101")
        assert vav["connections"][room_guid] == ["CONTAINS"]

    def test_a_target_can_hold_several_edge_types(self, ontology, site):
        config = build_config(ontology, site)
        vav = _entity(config, "VAV-L1-01")
        ahu_guid = stable_guid(site.building_code, "AHU-1")
        assert vav["connections"][ahu_guid] == ["FEEDS"]

    def test_the_building_has_no_incoming_edges(self, ontology, site):
        building = _entity(build_config(ontology, site), site.building_code)
        assert "connections" not in building

    def test_a_floor_is_contained_by_the_building(self, ontology, site):
        config = build_config(ontology, site)
        floor = _entity(config, "AU-MEL-DEMO-1")
        building_guid = stable_guid(site.building_code, site.building_code)
        assert floor["connections"][building_guid] == ["CONTAINS"]

    def test_a_duplicate_connection_row_is_not_repeated_in_the_output(self, ontology, site):
        """A copy-pasted CSV row must not become [CONTAINS, CONTAINS]."""
        site.connections.append(
            Connection("AU-MEL-DEMO-1-101", "CONTAINS", "VAV-L1-01")
        )
        config = build_config(ontology, site)
        vav = _entity(config, "VAV-L1-01")
        room_guid = stable_guid(site.building_code, "AU-MEL-DEMO-1-101")
        assert vav["connections"][room_guid] == ["CONTAINS"]

    def test_two_distinct_types_on_the_same_edge_both_survive(self, ontology, site):
        """Distinct from the duplicate-row case: FEEDS and CONTROLS together
        on one source/target pair are two real facts, not a repeat."""
        site.connections.append(
            Connection("AHU-1", "CONTROLS", "VAV-L1-01")
        )
        config = build_config(ontology, site)
        vav = _entity(config, "VAV-L1-01")
        ahu_guid = stable_guid(site.building_code, "AHU-1")
        assert vav["connections"][ahu_guid] == ["CONTROLS", "FEEDS"]


class TestYamlRoundTrip:
    def test_on_and_off_keys_survive_serialisation(self, ontology, site):
        """The YAML 1.1 boolean trap, checked on the way out as well as in."""
        reloaded = _reload(build_config(ontology, site))
        ahu = _entity(reloaded, "AHU-1")
        assert set(ahu["translation"]["discharge_fan_run_command"]["states"]) == (
            {"ON", "OFF"}
        )

    def test_true_false_raw_values_stay_strings(self, ontology, site):
        reloaded = _reload(build_config(ontology, site))
        fcu = _entity(reloaded, "FCU-1")
        states = fcu["translation"]["discharge_fan_run_command"]["states"]
        assert states == {"ON": "true", "OFF": "false"}

    def test_numeric_cloud_device_id_stays_a_string(self, ontology, site):
        reloaded = _reload(build_config(ontology, site))
        assert isinstance(_entity(reloaded, "AHU-1")["cloud_device_id"], str)

    def test_output_is_valid_yaml_for_a_plain_safe_loader(self, ontology, site):
        """Consumers will not all use our loader; the file must still parse."""
        text = dump_config(build_config(ontology, site))
        assert isinstance(yaml.safe_load(text), dict)
# AI:E87M claude-code 2026-08-27 s:2a846146
