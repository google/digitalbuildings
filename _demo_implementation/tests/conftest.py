"""Shared fixtures. The ontology load is session-scoped -- it reads 122 files."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

DEMO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(DEMO_ROOT))

from bms_dbo.loader import load_site  # noqa: E402
from bms_dbo.ontology import Ontology, default_resources_root  # noqa: E402


@pytest.fixture(scope="session")
def ontology() -> Ontology:
    return Ontology(default_resources_root(DEMO_ROOT / "bms_dbo"))


@pytest.fixture()
def site():
    return load_site(DEMO_ROOT / "sample_site")
# AI:E87M claude-code 2026-08-27 s:2a846146
