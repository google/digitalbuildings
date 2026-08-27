"""Read-only access to a pinned copy of the Digital Buildings Ontology.

This module is the only place in the demo that knows how the ontology YAML is
laid out on disk. Everything else asks questions of an :class:`Ontology`
instance, which is what recommendation #2 ("vendor the ontology and version-pin
it") looks like in practice: one loader, one pinned revision, no ad-hoc YAML
reads scattered through the BMS.
"""

from __future__ import annotations

import functools
import hashlib
import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

import yaml

# Trailing enumeration on a field name, e.g. ``zone_air_temperature_sensor_1``
# or the sub-grouped form ``..._2_1``. See ontology/docs/ontology.md#enumeration.
_ENUMERATION_SUFFIX = re.compile(r"(_\d+)+$")

GLOBAL_NAMESPACE = "GLOBAL"

# A unit is either the literal "STANDARD" or a {multiplier, offset} mapping
# that converts it into its family's standard unit.
UnitSpec = str | dict[str, float]


class DboLoader(yaml.SafeLoader):
    """A SafeLoader that does not fold the YAML 1.1 ``ON``/``OFF`` booleans.

    DBO state names include ``ON``, ``OFF``, ``YES`` and ``NO``. Plain
    ``yaml.safe_load`` applies the YAML 1.1 boolean rules and silently turns
    those keys into Python ``True``/``False``, so ``states/states.yaml`` loses
    two states and every ``ON: "true"`` in a translation becomes ``True:
    "true"``. This loader keeps ``true``/``false`` as booleans (needed for
    ``is_abstract: true``) and leaves everything else a string.
    """


DboLoader.yaml_implicit_resolvers = {
    first_char: [
        (tag, regexp)
        for tag, regexp in resolvers
        if tag != "tag:yaml.org,2002:bool"
    ]
    for first_char, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}
DboLoader.add_implicit_resolver(
    "tag:yaml.org,2002:bool",
    re.compile(r"^(?:true|True|TRUE|false|False|FALSE)$"),
    list("tTfF"),
)


def load_yaml(path: Path):
    """Read a YAML file with DBO-safe boolean handling.

    Drives :class:`DboLoader` directly rather than going through ``yaml.load``,
    which keeps the safe-loader guarantee obvious to both readers and static
    analysers.
    """
    with Path(path).open(encoding="utf-8") as handle:
        loader = DboLoader(handle)
        try:
            return loader.get_single_data() or {}
        finally:
            loader.dispose()


class OntologyError(RuntimeError):
    """Raised when the pinned ontology cannot be loaded or queried."""


@dataclass(frozen=True)
class EntityType:
    """One entity type as declared in a ``*.yaml`` under ``entity_types/``."""

    namespace: str
    name: str
    guid: str
    description: str
    is_abstract: bool
    is_canonical: bool
    allow_undefined_fields: bool
    implements: tuple[str, ...]
    local_required: frozenset[str]
    local_optional: frozenset[str]
    source_file: str

    @property
    def qualified_name(self) -> str:
        if self.namespace == GLOBAL_NAMESPACE:
            return self.name
        return f"{self.namespace}/{self.name}"

    @property
    def general_type(self) -> str:
        """The leading ``<GENERALTYPE>_`` segment, e.g. ``VAV`` for VAV_SD_DSP."""
        return self.name.split("_", 1)[0]


@dataclass(frozen=True)
class FieldDefinition:
    """A standard field from ``fields/telemetry_fields.yaml``.

    A field is either numeric (it carries a min/max envelope and a measurement
    subfield that dictates its units) or multistate (it carries the set of
    states it may report). Never both.
    """

    name: str
    states: frozenset[str] = frozenset()
    fixed_min: float | None = None
    fixed_max: float | None = None
    flexible_min: float | None = None
    flexible_max: float | None = None

    @property
    def is_multistate(self) -> bool:
        return bool(self.states)

    @property
    def minimum(self) -> float | None:
        return self.fixed_min if self.fixed_min is not None else self.flexible_min

    @property
    def maximum(self) -> float | None:
        return self.fixed_max if self.fixed_max is not None else self.flexible_max


@dataclass(frozen=True)
class ResolvedType:
    """An entity type with its inheritance chain flattened."""

    entity_type: EntityType
    required: frozenset[str]
    optional: frozenset[str]
    ancestry: tuple[str, ...] = field(default=())

    @property
    def declarable(self) -> frozenset[str]:
        """Every field this type may legally declare in a translation."""
        return self.required | self.optional


def strip_enumeration(field_name: str) -> str:
    """``zone_air_temperature_sensor_2_1`` -> ``zone_air_temperature_sensor``."""
    return _ENUMERATION_SUFFIX.sub("", field_name)


def _unqualify(reference: str) -> str:
    """Drop a ``NAMESPACE/`` prefix from a field or type reference."""
    return reference.split("/")[-1]


class Ontology:
    """A pinned, in-memory view of the DBO YAML resources."""

    def __init__(self, resources_root: Path, revision: str | None = None):
        self.root = Path(resources_root)
        if not self.root.is_dir():
            raise OntologyError(f"ontology resources not found at {self.root}")
        self.revision = revision
        self.subfields: dict[str, dict[str, str]] = self._load_subfields()
        self.states: frozenset[str] = self._load_states()
        self.units: dict[str, dict[str, UnitSpec]] = self._load_units()
        self.fields: dict[str, FieldDefinition] = self._load_fields()
        self.types: dict[str, EntityType] = self._load_entity_types()

    # ------------------------------------------------------------------ load

    def _read(self, relative: str) -> dict:
        path = self.root / relative
        if not path.is_file():
            raise OntologyError(f"expected ontology file missing: {path}")
        return load_yaml(path)

    def _load_subfields(self) -> dict[str, dict[str, str]]:
        return self._read("subfields/subfields.yaml")

    def _load_states(self) -> frozenset[str]:
        return frozenset(self._read("states/states.yaml"))

    def _load_units(self) -> dict[str, dict[str, UnitSpec]]:
        return self._read("units/units.yaml")

    def _load_fields(self) -> dict[str, FieldDefinition]:
        raw = self._read("fields/telemetry_fields.yaml")
        definitions: dict[str, FieldDefinition] = {}
        for entry in raw.get("literals", []):
            # Entries are either a bare string, or a single-key mapping whose
            # value is a state list (multistate) or a min/max mapping (numeric).
            if isinstance(entry, str):
                definitions[entry] = FieldDefinition(name=entry)
                continue
            for name, spec in entry.items():
                if isinstance(spec, list):
                    definitions[name] = FieldDefinition(
                        name=name, states=frozenset(spec)
                    )
                elif isinstance(spec, dict):
                    definitions[name] = FieldDefinition(
                        name=name,
                        fixed_min=spec.get("fixed_min"),
                        fixed_max=spec.get("fixed_max"),
                        flexible_min=spec.get("flexible_min"),
                        flexible_max=spec.get("flexible_max"),
                    )
                else:
                    definitions[name] = FieldDefinition(name=name)
        return definitions

    def _load_entity_types(self) -> dict[str, EntityType]:
        types: dict[str, EntityType] = {}
        for path in sorted(self.root.glob("**/entity_types/*.yaml")):
            # ``resources/entity_types/`` is the global namespace; anything
            # deeper is ``resources/<NAMESPACE>/entity_types/``.
            parent = path.parent.parent
            namespace = (
                GLOBAL_NAMESPACE if parent == self.root else parent.name
            )
            document = load_yaml(path)
            for name, body in document.items():
                if not isinstance(body, dict):
                    continue
                entity = EntityType(
                    namespace=namespace,
                    name=name,
                    guid=body.get("guid", ""),
                    description=body.get("description", ""),
                    is_abstract=bool(body.get("is_abstract", False)),
                    is_canonical=bool(body.get("is_canonical", False)),
                    allow_undefined_fields=bool(
                        body.get("allow_undefined_fields", False)
                    ),
                    implements=tuple(body.get("implements", []) or []),
                    local_required=frozenset(
                        _unqualify(f) for f in body.get("uses", []) or []
                    ),
                    local_optional=frozenset(
                        _unqualify(f) for f in body.get("opt_uses", []) or []
                    ),
                    source_file=str(path.relative_to(self.root)),
                )
                types[entity.qualified_name] = entity
        return types

    # ----------------------------------------------------------------- query

    def get_type(self, reference: str) -> EntityType:
        """Look up a type by ``NAMESPACE/NAME`` or by bare name."""
        entity = self.find_type(reference)
        if entity is None:
            raise OntologyError(f"unknown entity type: {reference!r}")
        return entity

    def find_type(
        self, reference: str, default_namespace: str | None = None
    ) -> EntityType | None:
        if reference.startswith("/"):
            # A leading slash means "explicitly the global namespace", e.g.
            # HVAC/PMP_SS implements "- /PMP # inherits from global namespace".
            return self.types.get(reference[1:])
        if reference in self.types:
            return self.types[reference]
        if "/" not in reference:
            # Unqualified references resolve against the referring namespace
            # first, then fall back to the global namespace.
            for namespace in (default_namespace, GLOBAL_NAMESPACE):
                if namespace and f"{namespace}/{reference}" in self.types:
                    return self.types[f"{namespace}/{reference}"]
        return None

    @functools.lru_cache(maxsize=None)
    def resolve(self, reference: str) -> ResolvedType:
        """Flatten a type's ``implements`` chain into required/optional sets.

        A field required anywhere in the chain is required on the result, even
        if another ancestor lists it as optional.
        """
        entity = self.get_type(reference)
        required: set[str] = set()
        optional: set[str] = set()
        ancestry: list[str] = []
        seen: set[str] = set()

        def walk(current: EntityType) -> None:
            if current.qualified_name in seen:
                return
            seen.add(current.qualified_name)
            ancestry.append(current.qualified_name)
            required.update(current.local_required)
            optional.update(current.local_optional)
            for parent_ref in current.implements:
                parent = self.find_type(parent_ref, current.namespace)
                if parent is None:
                    raise OntologyError(
                        f"{current.qualified_name} implements unknown type "
                        f"{parent_ref!r}"
                    )
                walk(parent)

        walk(entity)
        return ResolvedType(
            entity_type=entity,
            required=frozenset(required),
            optional=frozenset(optional - required),
            ancestry=tuple(ancestry),
        )

    def concrete_types(self, namespace: str | None = None) -> list[EntityType]:
        """Types that may be assigned to a real entity (i.e. not abstract)."""
        return [
            entity
            for entity in self.types.values()
            if not entity.is_abstract
            and (namespace is None or entity.namespace == namespace)
        ]

    def get_field(self, field_name: str) -> FieldDefinition | None:
        return self.fields.get(strip_enumeration(field_name))

    def is_valid_field(self, field_name: str) -> bool:
        return strip_enumeration(field_name) in self.fields

    def measurement_of(self, field_name: str) -> str | None:
        """The measurement subfield of a field, which fixes its unit family.

        Measurement subfield names and ``units.yaml`` quantity-kind keys are
        the same vocabulary, so this doubles as the units lookup key.
        """
        measurements = self.subfields.get("measurement", {})
        for token in strip_enumeration(field_name).split("_"):
            if token in measurements:
                return token
        return None

    def units_for_field(self, field_name: str) -> dict[str, UnitSpec]:
        measurement = self.measurement_of(field_name)
        if measurement is None:
            return {}
        return self.units.get(measurement, {})

    def standard_unit_for_field(self, field_name: str) -> str | None:
        for unit, spec in self.units_for_field(field_name).items():
            if spec == "STANDARD":
                return unit
        return None

    def convert_to_standard(
        self, value: float, unit: str, field_name: str
    ) -> float:
        """Convert *value* from *unit* into the field's standard unit.

        Field min/max envelopes in ``telemetry_fields.yaml`` are expressed in
        the standard unit (kelvin, cubic_meters_per_second, ...), so a raw
        BMS value must be converted before it can be range-checked.
        """
        spec = self.units_for_field(field_name).get(unit)
        if spec is None:
            raise OntologyError(f"{unit!r} is not a valid unit for {field_name}")
        if not isinstance(spec, dict):
            return float(value)
        return float(value) * spec.get("multiplier", 1) + spec.get("offset", 0)

    def convert_from_standard(
        self, value: float, unit: str, field_name: str
    ) -> float:
        """Inverse of :meth:`convert_to_standard`."""
        spec = self.units_for_field(field_name).get(unit)
        if spec is None:
            raise OntologyError(f"{unit!r} is not a valid unit for {field_name}")
        if not isinstance(spec, dict):
            return float(value)
        multiplier = spec.get("multiplier", 1) or 1
        return (float(value) - spec.get("offset", 0)) / multiplier

    def range_in_unit(
        self, field_name: str, unit: str
    ) -> tuple[float | None, float | None]:
        """The field's sanity envelope expressed in *unit*, for display."""
        definition = self.get_field(field_name)
        if definition is None:
            return (None, None)
        low, high = definition.minimum, definition.maximum
        if low is not None:
            low = self.convert_from_standard(low, unit, field_name)
        if high is not None:
            high = self.convert_from_standard(high, unit, field_name)
        return (low, high)

    def subfields_of(self, field_name: str) -> frozenset[str]:
        """The subfield set of a field. Equivalence is by set, not by string.

        See ontology/docs/ontology.md#equivalence -- applications are told to
        depend on the field set rather than the assembled name.
        """
        return frozenset(strip_enumeration(field_name).split("_"))

    def describe_field(self, field_name: str) -> str:
        """Human-readable gloss assembled from the subfield descriptions."""
        parts: list[str] = []
        for token in strip_enumeration(field_name).split("_"):
            for category, entries in self.subfields.items():
                if token in entries:
                    parts.append(f"{token} ({category})")
                    break
        return ", ".join(parts)


def default_resources_root(start: Path | None = None) -> Path:
    """Locate ``ontology/yaml/resources`` by walking up from *start*."""
    here = (start or Path(__file__)).resolve()
    for candidate in here.parents:
        resources = candidate / "ontology" / "yaml" / "resources"
        if resources.is_dir():
            return resources
    raise OntologyError("could not locate ontology/yaml/resources")


def read_pin(pin_file: Path) -> dict:
    return load_yaml(pin_file)


def ontology_digest(resources_root: Path) -> str:
    """A content hash of every ontology resource file.

    Pinning to a git revision is the obvious move and the wrong one when the
    ontology is vendored inside the consuming repository -- the pin then drifts
    on every unrelated commit. What a BMS actually needs to know is whether the
    *vocabulary* changed, so hash the vocabulary.
    """
    digest = hashlib.sha256()
    for path in sorted(Path(resources_root).rglob("*.yaml")):
        digest.update(str(path.relative_to(resources_root)).encode("utf-8"))
        digest.update(path.read_bytes())
    return digest.hexdigest()


def current_ontology_revision(repo_root: Path) -> str | None:
    """The git revision of the vendored ontology, if this is a checkout."""
    try:
        result = subprocess.run(
            ["git", "-C", str(repo_root), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
            timeout=10,
        )
    except (subprocess.SubprocessError, OSError):
        return None
    return result.stdout.strip() or None


def load_pinned_ontology(pin_file: Path) -> tuple[Ontology, dict]:
    """Load the ontology named by *pin_file* and report any pin drift.

    The demo deliberately does not fail on drift -- it reports it. A real BMS
    build should decide its own policy (warn in dev, fail in CI).
    """
    pin = read_pin(pin_file)
    # Anchor on the package, not on the pin file. Where the pin happens to
    # live says nothing about where the ontology is vendored, and resolving
    # from it breaks as soon as the pin moves. A pin may still name an
    # explicit `resources_root`, relative to itself.
    configured = pin.get("resources_root")
    resources = (
        (Path(pin_file).parent / configured).resolve()
        if configured
        else default_resources_root()
    )
    actual_digest = ontology_digest(resources)
    ontology = Ontology(resources, revision=actual_digest)
    # YAML types a bare all-digit value as a number (and a leading-zero one as
    # octal), so a digest of "000..." would arrive as int 0 and read as unset.
    if pin.get("pinned_digest") is not None:
        pin["pinned_digest"] = str(pin["pinned_digest"])
    pin.setdefault("pinned_digest", None)
    pin["actual_digest"] = actual_digest
    pin["actual_revision"] = current_ontology_revision(resources.parents[2])
    pin["drifted"] = bool(
        pin.get("pinned_digest") and pin["pinned_digest"] != actual_digest
    )
    return ontology, pin


def field_set(fields: Iterable[str]) -> frozenset[str]:
    """Normalise a collection of field names for set comparison."""
    return frozenset(strip_enumeration(f) for f in fields)
# AI:E87M claude-code 2026-08-27 s:2a846146
