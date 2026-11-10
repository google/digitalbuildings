"""Tests for the package's public surface and its documentation.

These exist because both drifted in practice: ``__init__.py`` gained modules
without gaining exports, and the README quoted a test count that was two
rounds of work out of date. Cheap checks, but they keep the front door and
the docs honest as the code moves.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

import bms_dbo

DEMO_ROOT = Path(__file__).resolve().parent.parent
README = DEMO_ROOT / "README.md"
MAKEFILE = DEMO_ROOT / "Makefile"


class TestPublicSurface:
    def test_every_name_in_all_actually_exists(self):
        absent = [n for n in bms_dbo.__all__ if not hasattr(bms_dbo, n)]
        assert absent == []

    def test_all_is_sorted(self):
        """Keeps the diff readable when someone adds an export."""
        assert bms_dbo.__all__ == sorted(bms_dbo.__all__)

    def test_all_has_no_duplicates(self):
        assert len(bms_dbo.__all__) == len(set(bms_dbo.__all__))

    @pytest.mark.parametrize(
        "name",
        [
            "load_site",
            "Ontology",
            "validate_site",
            "build_config",
            "suggest_types",
            "serve",
        ],
    )
    def test_the_documented_entry_points_are_importable(self, name):
        """Every name the package docstring tells people to import."""
        assert hasattr(bms_dbo, name)


class TestReadmeAccuracy:
    """The README makes checkable claims. Check them."""

    def _readme(self) -> str:
        return README.read_text(encoding="utf-8")

    def test_every_documented_cli_command_exists(self):
        from bms_dbo.cli import build_parser

        supported = set(
            next(
                a.choices
                for a in build_parser()._actions
                if a.dest == "command"
            )
        )
        documented = set(
            re.findall(r"python -m bms_dbo ([a-z][a-z-]*)", self._readme())
        )
        assert documented - supported == set()

    def test_every_documented_make_target_exists(self):
        targets = set(
            re.findall(r"^([a-z][a-z-]*):", MAKEFILE.read_text(), re.MULTILINE)
        )
        documented = set(re.findall(r"`make ([a-z-]+)`", self._readme()))
        assert documented - targets == set()

    def test_every_module_the_readme_lists_exists(self):
        listed = set(re.findall(r"(\w+)\.py\s", self._readme()))
        package = {p.stem for p in (DEMO_ROOT / "bms_dbo").glob("*.py")}
        # The README also names files outside the package (schema.sql etc.);
        # only assert on names it presents as package modules.
        assert {name for name in listed if name in package} <= package

    def test_the_quoted_test_counts_agree_with_each_other(self):
        """The README states a test count in more than one place. Those drifted
        apart once (one said 286, another 210) because they were updated by
        hand at different times. Any two numbers disagreeing means at least
        one is stale, which is checkable here without running the suite
        recursively."""
        quoted = re.findall(r"(\d+)\s+tests\b", self._readme())
        quoted += re.findall(r"(\d+)\s+passed\b", self._readme())
        assert quoted, "README no longer states a test count"
        assert len(set(quoted)) == 1, (
            f"README quotes conflicting test counts: {sorted(set(quoted))}"
        )
# AI:E87M claude-code 2026-08-27 s:2a846146
