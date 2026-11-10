"""Tests for reading a site out of CSV.

The failure paths matter more than the happy path here: a commissioning
engineer editing a spreadsheet will produce malformed input regularly, and a
silent misparse is worse than a loud refusal.
"""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest

from bms_dbo.loader import LoaderError, load_site, parse_states

DEMO_ROOT = Path(__file__).resolve().parent.parent
SAMPLE = DEMO_ROOT / "sample_site"


@pytest.fixture()
def site_dir(tmp_path: Path) -> Path:
    """A writable copy of the sample site, so tests can corrupt it."""
    target = tmp_path / "site"
    shutil.copytree(SAMPLE, target)
    return target


class TestParseStates:
    def test_parses_a_single_pair(self):
        assert parse_states("ON=1") == {"ON": "1"}

    def test_parses_several_pairs(self):
        assert parse_states("ON=1;OFF=0") == {"ON": "1", "OFF": "0"}

    def test_tolerates_surrounding_whitespace(self):
        assert parse_states(" ON = 1 ; OFF = 0 ") == {"ON": "1", "OFF": "0"}

    def test_an_empty_string_is_no_states(self):
        assert parse_states("") == {}

    def test_keeps_raw_values_as_strings(self):
        """'true' must not become a bool on the way in or out."""
        assert parse_states("ON=true")["ON"] == "true"

    def test_a_value_may_contain_an_equals_sign(self):
        assert parse_states("ON=a=b") == {"ON": "a=b"}

    def test_a_pair_without_an_equals_sign_is_rejected(self):
        with pytest.raises(LoaderError, match="malformed state map"):
            parse_states("ON")


class TestLoadSite:
    def test_reads_the_building_code(self, site_dir):
        assert load_site(site_dir).building_code == "AU-MEL-DEMO"

    def test_reads_every_table(self, site_dir):
        site = load_site(site_dir)
        counts = (
            len(site.spaces),
            len(site.devices),
            len(site.mappings),
            len(site.connections),
        )
        assert counts == (4, 5, 39, 14)

    def test_parses_reporting_flags(self, site_dir):
        site = load_site(site_dir)
        assert (site.device("AHU-1").is_reporting, site.device("VAV-L1-01").is_reporting) == (
            True,
            False,
        )

    def test_parses_a_state_map_column(self, site_dir):
        site = load_site(site_dir)
        mapping = next(
            m
            for m in site.mappings_for("AHU-1")
            if m.dbo_field == "discharge_fan_run_command"
        )
        assert mapping.native_states == {"ON": "active", "OFF": "inactive"}

    def test_parses_optional_numeric_ranges(self, site_dir):
        site = load_site(site_dir)
        mapping = next(
            m
            for m in site.mappings_for("AHU-1")
            if m.dbo_field == "discharge_air_temperature_sensor"
        )
        assert (mapping.value_min, mapping.value_max) == (10.0, 30.0)

    def test_leaves_absent_ranges_as_none(self, site_dir):
        site = load_site(site_dir)
        mapping = next(
            m
            for m in site.mappings_for("AHU-1")
            if m.dbo_field == "chilled_water_valve_percentage_sensor"
        )
        assert (mapping.value_min, mapping.value_max) == (None, None)

    def test_reads_the_missing_flag_and_its_justification(self, site_dir):
        site = load_site(site_dir)
        mapping = next(m for m in site.mappings if m.missing)
        assert mapping.missing_justification.startswith("Controller exposes no")

    def test_uppercases_connection_types(self, site_dir):
        path = site_dir / "connections.csv"
        path.write_text(
            path.read_text().replace("AU-MEL-DEMO,CONTAINS", "AU-MEL-DEMO,contains")
        )
        assert load_site(site_dir).connections[0].connection_type == "CONTAINS"


class TestLoaderFailures:
    def test_a_missing_directory_is_reported(self, tmp_path):
        with pytest.raises((LoaderError, OSError)):
            load_site(tmp_path / "nope")

    def test_a_missing_csv_is_reported(self, site_dir):
        (site_dir / "devices.csv").unlink()
        with pytest.raises(LoaderError, match="missing site file"):
            load_site(site_dir)

    def test_a_missing_required_column_is_reported(self, site_dir):
        path = site_dir / "spaces.csv"
        path.write_text(path.read_text().replace("entity_type", "type"))
        with pytest.raises(LoaderError, match="missing column"):
            load_site(site_dir)

    def test_a_site_yaml_without_a_building_code_is_reported(self, site_dir):
        (site_dir / "site.yaml").write_text("display_name: nameless\n")
        with pytest.raises(LoaderError, match="building_code"):
            load_site(site_dir)

    def test_a_non_numeric_range_is_reported(self, site_dir):
        path = site_dir / "point_mappings.csv"
        path.write_text(path.read_text().replace(",10,30,", ",ten,30,"))
        with pytest.raises(LoaderError, match="expected a number"):
            load_site(site_dir)


class TestRowFiltering:
    def test_blank_lines_are_skipped(self, site_dir):
        path = site_dir / "spaces.csv"
        path.write_text(path.read_text() + "\n\n")
        assert len(load_site(site_dir).spaces) == 4

    def test_comment_rows_are_skipped(self, site_dir):
        path = site_dir / "spaces.csv"
        path.write_text(path.read_text() + "# a note,FACILITIES/ROOM,ignored\n")
        assert len(load_site(site_dir).spaces) == 4

    def test_comment_rows_are_skipped_in_connections_csv(self, site_dir):
        """connections.csv has neither a 'code' nor 'device_code' column --
        the column the loader used to check for a leading '#'. A comment row
        here used to slip through as a real, malformed connection."""
        path = site_dir / "connections.csv"
        path.write_text(
            path.read_text() + "# disabled for now,CONTAINS,AHU-1\n"
        )
        site = load_site(site_dir)
        assert not any(c.source_code.startswith("#") for c in site.connections)

    def test_connections_csv_row_count_is_unaffected_by_a_comment(self, site_dir):
        path = site_dir / "connections.csv"
        before = len(load_site(site_dir).connections)
        path.write_text(path.read_text() + "# disabled for now,CONTAINS,AHU-1\n")
        after = len(load_site(site_dir).connections)
        assert after == before

    def test_comment_rows_are_skipped_in_point_mappings_csv(self, site_dir):
        path = site_dir / "point_mappings.csv"
        before = len(load_site(site_dir).mappings)
        path.write_text(
            path.read_text() + "# disabled,zone_air_temperature_sensor,,,,,,FALSE,,,\n"
        )
        after = len(load_site(site_dir).mappings)
        assert after == before
# AI:E87M claude-code 2026-08-27 s:2a846146
