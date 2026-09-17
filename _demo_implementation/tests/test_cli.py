"""Tests for the command line entry point.

Exit codes are the contract CI depends on, so they are what these assert:
0 means the gate passed, non-zero means it did not.
"""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest

from bms_dbo.cli import build_parser, main
from bms_dbo.ontology import load_yaml

DEMO_ROOT = Path(__file__).resolve().parent.parent
SAMPLE = DEMO_ROOT / "sample_site"
PIN = DEMO_ROOT / "ontology_pin.yaml"


@pytest.fixture()
def workspace(tmp_path: Path) -> Path:
    """A writable copy of the site and pin, so tests can perturb them."""
    shutil.copytree(SAMPLE, tmp_path / "site")
    shutil.copy(PIN, tmp_path / "ontology_pin.yaml")
    return tmp_path


def _args(workspace: Path, command: str, out: str = "out.yaml") -> list[str]:
    return [
        command,
        "--site", str(workspace / "site"),
        "--pin", str(workspace / "ontology_pin.yaml"),
        "--out", str(workspace / out),
    ]


class TestArgumentParsing:
    def test_rejects_an_unknown_command(self):
        with pytest.raises(SystemExit):
            build_parser().parse_args(["frobnicate"])

    def test_defaults_point_at_the_shipped_sample(self):
        args = build_parser().parse_args(["validate"])
        assert args.site == SAMPLE


class TestOntologyInfo:
    def test_passes_when_the_digest_matches(self, workspace, capsys):
        assert main(_args(workspace, "ontology-info")) == 0

    def test_reports_the_counts_it_loaded(self, workspace, capsys):
        main(_args(workspace, "ontology-info"))
        assert "entity types" in capsys.readouterr().out

    def test_fails_when_the_ontology_has_drifted(self, workspace, capsys):
        pin = workspace / "ontology_pin.yaml"
        pin.write_text(pin.read_text().replace(
            load_yaml(pin)["pinned_digest"], "deadbeef" * 8
        ))
        assert main(_args(workspace, "ontology-info")) == 1

    def test_says_why_it_failed(self, workspace, capsys):
        pin = workspace / "ontology_pin.yaml"
        pin.write_text(pin.read_text().replace(
            load_yaml(pin)["pinned_digest"], "deadbeef" * 8
        ))
        main(_args(workspace, "ontology-info"))
        assert "has changed since it" in capsys.readouterr().out


class TestValidate:
    def test_passes_on_the_sample_site(self, workspace, capsys):
        assert main(_args(workspace, "validate")) == 0

    def test_still_reports_the_intentional_warning(self, workspace, capsys):
        main(_args(workspace, "validate"))
        assert "declared MISSING" in capsys.readouterr().out

    def test_fails_when_a_mapping_is_broken(self, workspace, capsys):
        path = workspace / "site" / "point_mappings.csv"
        path.write_text(path.read_text().replace(
            "degrees_celsius", "liters_per_second", 1
        ))
        assert main(_args(workspace, "validate")) == 1


class TestSuggestTypes:
    def test_succeeds(self, workspace, capsys):
        assert main(_args(workspace, "suggest-types")) == 0

    def test_names_the_canonical_type_for_a_vav(self, workspace, capsys):
        main(_args(workspace, "suggest-types"))
        assert "HVAC/VAV_SD_DSP" in capsys.readouterr().out

    def test_declines_to_infer_for_a_passthrough_gateway(self, workspace, capsys):
        main(_args(workspace, "suggest-types"))
        assert "nothing to infer" in capsys.readouterr().out


class TestExport:
    def test_writes_the_config(self, workspace, capsys):
        main(_args(workspace, "export"))
        assert (workspace / "out.yaml").is_file()

    def test_the_output_is_loadable_yaml(self, workspace, capsys):
        main(_args(workspace, "export"))
        assert "CONFIG_METADATA" in load_yaml(workspace / "out.yaml")

    def test_refuses_to_export_an_invalid_site(self, workspace, capsys):
        path = workspace / "site" / "point_mappings.csv"
        path.write_text(path.read_text().replace(
            "degrees_celsius", "liters_per_second", 1
        ))
        assert main(_args(workspace, "export", out="bad.yaml")) == 1

    def test_writes_nothing_when_it_refuses(self, workspace, capsys):
        path = workspace / "site" / "point_mappings.csv"
        path.write_text(path.read_text().replace(
            "degrees_celsius", "liters_per_second", 1
        ))
        main(_args(workspace, "export", out="bad.yaml"))
        assert not (workspace / "bad.yaml").exists()


class TestDemo:
    def test_runs_every_step(self, workspace, capsys):
        assert main(_args(workspace, "demo")) == 0

    def test_covers_all_four_sections(self, workspace, capsys):
        main(_args(workspace, "demo"))
        out = capsys.readouterr().out
        headings = [n for n in ("1.", "2.", "3.", "4.") if n in out]
        assert headings == ["1.", "2.", "3.", "4."]

    def test_fails_when_ontology_drifted_though_mapping_is_clean(self, workspace, capsys):
        """A caller checking demo's exit code alone must see ontology drift,
        not just mapping errors -- section 1 failing should fail the whole
        walkthrough even when section 3 (validate) is clean."""
        pin = workspace / "ontology_pin.yaml"
        pin.write_text(pin.read_text().replace(
            load_yaml(pin)["pinned_digest"], "deadbeef" * 8
        ))
        assert main(_args(workspace, "demo")) == 1


class TestPinCoercion:
    """A digest is a string, even when it happens to look like a number."""

    def test_an_all_digit_digest_is_not_read_as_unset(self, workspace, capsys):
        pin = workspace / "ontology_pin.yaml"
        pin.write_text(pin.read_text().replace(
            load_yaml(pin)["pinned_digest"], "1" * 64
        ))
        main(_args(workspace, "ontology-info"))
        assert "(not pinned)" not in capsys.readouterr().out

    def test_an_all_digit_digest_still_detects_drift(self, workspace, capsys):
        pin = workspace / "ontology_pin.yaml"
        pin.write_text(pin.read_text().replace(
            load_yaml(pin)["pinned_digest"], "1" * 64
        ))
        assert main(_args(workspace, "ontology-info")) == 1
# AI:E87M claude-code 2026-08-27 s:2a846146
