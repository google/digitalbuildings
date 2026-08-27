"""Tests for inferring an entity type from a mapped point set."""

from __future__ import annotations

from bms_dbo.type_matcher import explain_choice, suggest_types

VAV_SD_DSP_POINTS = {
    "supply_air_damper_percentage_command",
    "supply_air_flowrate_sensor",
    "supply_air_flowrate_setpoint",
    "zone_air_cooling_temperature_setpoint",
    "zone_air_heating_temperature_setpoint",
    "zone_air_temperature_sensor",
}


class TestSuggestTypes:
    def test_leads_with_the_canonical_exact_match(self, ontology):
        best = suggest_types(
            ontology, VAV_SD_DSP_POINTS, namespace="HVAC", general_type="VAV"
        )[0]
        assert best.qualified_name == "HVAC/VAV_SD_DSP"

    def test_the_leading_candidate_is_exact_and_canonical(self, ontology):
        best = suggest_types(
            ontology, VAV_SD_DSP_POINTS, namespace="HVAC", general_type="VAV"
        )[0]
        assert (best.is_exact, best.is_canonical) == (True, True)

    def test_enumerated_points_match_the_same_type(self, ontology):
        """A gateway publishes zone_air_temperature_sensor_1; same meaning."""
        enumerated = {f"{name}_1" for name in VAV_SD_DSP_POINTS}
        best = suggest_types(
            ontology, enumerated, namespace="HVAC", general_type="VAV"
        )[0]
        assert best.qualified_name == "HVAC/VAV_SD_DSP"

    def test_incomplete_point_sets_are_dropped_by_default(self, ontology):
        partial = {"zone_air_temperature_sensor"}
        candidates = suggest_types(
            ontology, partial, namespace="HVAC", general_type="VAV"
        )
        assert all(c.is_complete for c in candidates)

    def test_near_misses_are_available_on_request(self, ontology):
        partial = {"zone_air_temperature_sensor"}
        candidates = suggest_types(
            ontology,
            partial,
            namespace="HVAC",
            general_type="VAV",
            complete_only=False,
        )
        assert candidates, "near-miss mode should still return candidates"

    def test_catch_all_types_are_never_suggested(self, ontology):
        """*_INITIAL sets allow_undefined_fields and matches everything."""
        names = {
            c.qualified_name
            for c in suggest_types(
                ontology,
                VAV_SD_DSP_POINTS,
                namespace="HVAC",
                general_type="VAV",
                limit=50,
            )
        }
        assert not [n for n in names if n.endswith("_INITIAL")]

    def test_general_type_filter_is_honoured(self, ontology):
        candidates = suggest_types(
            ontology, VAV_SD_DSP_POINTS, namespace="HVAC", general_type="VAV"
        )
        assert all(c.qualified_name.startswith("HVAC/VAV") for c in candidates)

    def test_limit_is_respected(self, ontology):
        candidates = suggest_types(
            ontology, VAV_SD_DSP_POINTS, namespace="HVAC", limit=2
        )
        assert len(candidates) <= 2


class TestExplainChoice:
    def test_scores_a_type_that_fits(self, ontology):
        scored = explain_choice(ontology, "HVAC/VAV_SD_DSP", VAV_SD_DSP_POINTS)
        assert scored.is_exact

    def test_reports_the_specific_missing_requirement(self, ontology):
        short = VAV_SD_DSP_POINTS - {"supply_air_flowrate_sensor"}
        scored = explain_choice(ontology, "HVAC/VAV_SD_DSP", short)
        assert scored.missing_required == frozenset(
            {"supply_air_flowrate_sensor"}
        )

    def test_reports_points_the_type_cannot_express(self, ontology):
        extra = VAV_SD_DSP_POINTS | {"chilled_water_valve_percentage_command"}
        scored = explain_choice(ontology, "HVAC/VAV_SD_DSP", extra)
        assert "chilled_water_valve_percentage_command" in scored.undeclarable

    def test_a_passthrough_gateway_can_express_anything(self, ontology):
        scored = explain_choice(
            ontology, "GATEWAYS/PASSTHROUGH", VAV_SD_DSP_POINTS
        )
        assert scored.undeclarable == frozenset()
# AI:E87M claude-code 2026-08-27 s:2a846146
