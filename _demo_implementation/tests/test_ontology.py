"""Tests for the pinned-ontology reader."""

from __future__ import annotations

import pytest

from bms_dbo.ontology import (
    Ontology,
    OntologyError,
    ontology_digest,
    strip_enumeration,
)


class TestYamlBooleanTrap:
    """YAML 1.1 folds ON/OFF into booleans. DBO uses them as state names."""

    def test_on_and_off_survive_as_states(self, ontology: Ontology):
        assert "ON" in ontology.states
        assert "OFF" in ontology.states

    def test_no_booleans_leak_into_the_state_vocabulary(self, ontology):
        leaked = [s for s in ontology.states if isinstance(s, bool)]
        assert leaked == []

    def test_run_command_keeps_its_on_off_states(self, ontology: Ontology):
        definition = ontology.get_field("discharge_fan_run_command")
        assert definition is not None
        assert {"ON", "OFF"} <= set(definition.states)

    def test_real_booleans_are_still_parsed(self, ontology: Ontology):
        # is_abstract: true must remain a bool, not the string "true".
        assert ontology.get_type("HVAC/VAV").is_abstract is True


class TestEnumeration:
    @pytest.mark.parametrize(
        "given,expected",
        [
            ("zone_air_temperature_sensor", "zone_air_temperature_sensor"),
            ("zone_air_temperature_sensor_1", "zone_air_temperature_sensor"),
            ("zone_air_temperature_sensor_2_1", "zone_air_temperature_sensor"),
        ],
    )
    def test_strips_trailing_increments(self, given, expected):
        assert strip_enumeration(given) == expected

    def test_enumerated_field_is_still_a_valid_field(self, ontology: Ontology):
        assert ontology.is_valid_field("zone_air_temperature_sensor_2")


class TestTypeResolution:
    def test_every_type_in_the_ontology_resolves(self, ontology: Ontology):
        """Guards the loader against structures it has not seen."""
        failures = []
        for name in ontology.types:
            try:
                ontology.resolve(name)
            except OntologyError as error:
                failures.append((name, str(error)))
        assert failures == []

    def test_flattens_the_implements_chain(self, ontology: Ontology):
        resolved = ontology.resolve("HVAC/VAV_SD_DSP")
        # SD contributes airflow control, DSP contributes dual setpoints.
        assert "supply_air_flowrate_sensor" in resolved.required
        assert "zone_air_heating_temperature_setpoint" in resolved.required
        assert "zone_air_cooling_temperature_setpoint" in resolved.required

    def test_required_beats_optional_across_the_chain(self, ontology: Ontology):
        resolved = ontology.resolve("HVAC/VAV_SD_DSP")
        assert not (resolved.required & resolved.optional)

    def test_leading_slash_means_global_namespace(self, ontology: Ontology):
        """HVAC/PMP_SS implements '- /PMP # inherits from global namespace'."""
        resolved = ontology.resolve("HVAC/PMP_SS")
        assert "PMP" in resolved.ancestry

    def test_unknown_type_raises(self, ontology: Ontology):
        with pytest.raises(OntologyError):
            ontology.resolve("HVAC/NOT_A_REAL_TYPE")


class TestUnits:
    def test_measurement_subfield_selects_the_unit_family(self, ontology):
        temperature = ontology.measurement_of("zone_air_temperature_sensor")
        flowrate = ontology.measurement_of("supply_air_flowrate_sensor")
        assert (temperature, flowrate) == ("temperature", "flowrate")

    def test_converts_to_the_standard_unit(self, ontology: Ontology):
        kelvin = ontology.convert_to_standard(
            22.0, "degrees_celsius", "zone_air_temperature_sensor"
        )
        assert kelvin == pytest.approx(295.15)

    def test_conversion_round_trips(self, ontology: Ontology):
        field = "supply_air_flowrate_sensor"
        standard = ontology.convert_to_standard(250.0, "liters_per_second", field)
        assert ontology.convert_from_standard(
            standard, "liters_per_second", field
        ) == pytest.approx(250.0)

    def test_range_is_expressed_in_the_requested_unit(self, ontology: Ontology):
        low, high = ontology.range_in_unit(
            "zone_air_temperature_sensor", "degrees_celsius"
        )
        # The stored envelope is kelvin; in celsius it must look like weather.
        assert low == pytest.approx(-17.22, abs=0.01)
        assert high == pytest.approx(48.89, abs=0.01)

    def test_rejects_a_unit_from_another_family(self, ontology: Ontology):
        with pytest.raises(OntologyError):
            ontology.convert_to_standard(
                1.0, "liters_per_second", "zone_air_temperature_sensor"
            )


class TestDigest:
    def test_digest_is_stable_across_reads(self, ontology: Ontology):
        assert ontology_digest(ontology.root) == ontology_digest(ontology.root)

    def test_digest_is_a_sha256(self, ontology: Ontology):
        digest = ontology_digest(ontology.root)
        assert len(digest) == 64
        assert set(digest) <= set("0123456789abcdef")
# AI:E87M claude-code 2026-08-27 s:2a846146
