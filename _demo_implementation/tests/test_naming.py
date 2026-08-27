"""Tests for the FACILITIES entity code conventions.

The rules are not in the ontology YAML -- they live in the instance
validator's Python source. These tests pin our copy to the cases that
actually appear on site, so drift shows up here before it shows up in CI.
"""

from __future__ import annotations

import pytest

from bms_dbo.naming import check_code


class TestBuildingCodes:
    @pytest.mark.parametrize(
        "code", ["AU-MEL-DEMO", "US-SEA-BLDG1", "GB-LON-A1", "AU-SYD-1234567890"]
    )
    def test_accepts_conventional_building_codes(self, code):
        assert check_code(code, "FACILITIES/BUILDING") is None

    @pytest.mark.parametrize(
        "code,why",
        [
            ("AUS-MEL-DEMO", "country must be exactly two letters"),
            ("AU-M-DEMO", "city must be two to four letters"),
            ("AU-MEL-D", "building id must be at least two characters"),
            ("AU-MEL-DEMO-1", "a floor code is not a building code"),
            ("AU_MEL_DEMO", "separator must be a hyphen"),
        ],
    )
    def test_rejects_malformed_building_codes(self, code, why):
        assert check_code(code, "FACILITIES/BUILDING") is not None, why


class TestFloorCodes:
    @pytest.mark.parametrize(
        "code,shape",
        [
            ("AU-MEL-DEMO-1", "numbered floor"),
            ("AU-MEL-DEMO-12", "numbered floor, two digits"),
            ("AU-MEL-DEMO-G", "ground"),
            ("AU-MEL-DEMO-UG", "upper ground"),
            ("AU-MEL-DEMO-M2", "mezzanine, letter-number form"),
            ("AU-MEL-DEMO-3M", "mezzanine, number-letter form"),
            ("AU-MEL-DEMO-B1", "basement"),
            ("AU-MEL-DEMO-2B", "basement, permuted"),
            ("AU-MEL-DEMO-R", "roof"),
            ("AU-MEL-DEMO-LG", "lower ground"),
            ("AU-MEL-DEMO-SBA", "sub-basement A"),
        ],
    )
    def test_accepts_conventional_floor_codes(self, code, shape):
        assert check_code(code, "FACILITIES/FLOOR") is None, shape

    @pytest.mark.parametrize(
        "code,why",
        [
            ("AU-MEL-DEMO-L1", "L1 is the obvious guess and is not legal"),
            ("AU-MEL-DEMO-LEVEL1", "spelled-out levels are not legal"),
            ("AU-MEL-DEMO", "a building code is not a floor code"),
            ("AU-MEL-DEMO-1-101", "a room code is not a floor code"),
            ("AU-MEL-DEMO-g", "floor designators are case sensitive"),
        ],
    )
    def test_rejects_malformed_floor_codes(self, code, why):
        assert check_code(code, "FACILITIES/FLOOR") is not None, why

    def test_the_message_names_the_convention(self):
        problem = check_code("AU-MEL-DEMO-L1", "FACILITIES/FLOOR")
        assert "floor code convention" in problem


class TestRoomCodes:
    @pytest.mark.parametrize(
        "code", ["AU-MEL-DEMO-1-101", "AU-MEL-DEMO-1-PLANT", "AU-MEL-DEMO-G-A1"]
    )
    def test_accepts_conventional_room_codes(self, code):
        assert check_code(code, "FACILITIES/ROOM") is None

    @pytest.mark.parametrize(
        "code,why",
        [
            ("AU-MEL-DEMO-1-lobby", "room ids are digits and capitals only"),
            ("AU-MEL-DEMO-1-101-A", "no fourth segment"),
            ("AU-MEL-DEMO-1", "a floor code is not a room code"),
            ("AU-MEL-DEMO-L1-101", "the floor part must still be legal"),
        ],
    )
    def test_rejects_malformed_room_codes(self, code, why):
        assert check_code(code, "FACILITIES/ROOM") is not None, why


class TestUnconstrainedTypes:
    @pytest.mark.parametrize(
        "entity_type",
        ["FACILITIES/CORRIDOR", "FACILITIES/STAIRWELL", "HVAC/VAV_SD_DSP"],
    )
    def test_returns_none_rather_than_guessing(self, entity_type):
        """We only enforce the three patterns upstream actually documents."""
        assert check_code("anything at all", entity_type) is None
# AI:E87M claude-code 2026-08-27 s:2a846146
