"""A reference implementation of Digital Buildings Ontology support in a BMS.

See ``../README.md``. The public surface is small on purpose:

    from bms_dbo import load_site, Ontology, validate_site, build_config

Everything else is an implementation detail of one of the six recommendations
the README walks through.
"""

from .exporter import build_config, dump_config
from .loader import load_site
from .mapping_validator import Finding, Severity, error_count, validate_site
from .models import Connection, Device, PointMapping, Site, Space
from .ontology import Ontology, OntologyError, load_pinned_ontology
from .type_matcher import TypeCandidate, explain_choice, suggest_types

__all__ = [
    "Connection",
    "Device",
    "Finding",
    "Ontology",
    "OntologyError",
    "PointMapping",
    "Severity",
    "Site",
    "Space",
    "TypeCandidate",
    "build_config",
    "dump_config",
    "error_count",
    "explain_choice",
    "load_pinned_ontology",
    "load_site",
    "suggest_types",
    "validate_site",
]
