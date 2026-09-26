"""Suggest DBO entity types from a device's mapped point set.

Recommendation #3. A commissioning engineer should not have to choose between
40-odd ``VAV_SD_DSP_*`` variants from a dropdown. Once the points are mapped,
the candidate types are computable: a type fits if every field it *requires* is
declared, and it fits *well* if it can also express everything else that was
mapped.

This mirrors the "what are the types associated with a given set of fields?"
query offered by tools/explorer, with ranking added so a UI can lead with one
recommendation instead of a list.
"""

from __future__ import annotations

from dataclasses import dataclass

from .ontology import Ontology, ResolvedType, field_set


@dataclass(frozen=True)
class TypeCandidate:
    """One possible type for a device, with the evidence for and against it."""

    qualified_name: str
    is_canonical: bool
    description: str
    matched_required: frozenset[str]
    matched_optional: frozenset[str]
    missing_required: frozenset[str]
    undeclarable: frozenset[str]
    slack: int

    @property
    def is_complete(self) -> bool:
        """Every required field is accounted for."""
        return not self.missing_required

    @property
    def is_exact(self) -> bool:
        """Complete, and the type can express every mapped point."""
        return self.is_complete and not self.undeclarable

    @property
    def sort_key(self) -> tuple:
        # Fewest unrepresentable points first -- an unrepresentable point is
        # data the model would silently drop. Then fewest gaps in required
        # fields, then prefer canonical types, then the tightest fit.
        return (
            len(self.undeclarable),
            len(self.missing_required),
            0 if self.is_canonical else 1,
            self.slack,
            self.qualified_name,
        )

    def summary(self) -> str:
        marks = []
        if self.is_exact:
            marks.append("exact")
        elif self.is_complete:
            marks.append(f"{len(self.undeclarable)} point(s) unrepresentable")
        else:
            marks.append(f"{len(self.missing_required)} required field(s) absent")
        if self.is_canonical:
            marks.append("canonical")
        return ", ".join(marks)


def _evaluate(
    resolved: ResolvedType, declared: frozenset[str]
) -> TypeCandidate:
    entity = resolved.entity_type
    declarable = resolved.declarable
    undeclarable = (
        frozenset() if entity.allow_undefined_fields else declared - declarable
    )
    return TypeCandidate(
        qualified_name=entity.qualified_name,
        is_canonical=entity.is_canonical,
        description=entity.description,
        matched_required=declared & resolved.required,
        matched_optional=declared & resolved.optional,
        missing_required=resolved.required - declared,
        undeclarable=undeclarable,
        slack=len(declarable - declared),
    )


def suggest_types(
    ontology: Ontology,
    declared_fields: frozenset[str] | set[str],
    namespace: str | None = None,
    general_type: str | None = None,
    limit: int = 5,
    complete_only: bool = True,
) -> list[TypeCandidate]:
    """Rank the types that could describe *declared_fields*.

    Args:
      declared_fields: the standard fields the device will declare, including
        any marked ``MISSING`` -- they still satisfy the type structurally.
      namespace: restrict to one DBO namespace, e.g. ``HVAC``.
      general_type: restrict to one equipment class, e.g. ``VAV``.
      complete_only: drop types with unmet required fields. Turn this off to
        see near-misses when nothing fits, which is the usual signal that a
        point is unmapped or the ontology needs an extension.
    """
    declared = field_set(declared_fields)
    candidates: list[TypeCandidate] = []

    for entity in ontology.concrete_types(namespace):
        if general_type and entity.general_type != general_type:
            continue
        if entity.allow_undefined_fields:
            # The *_INITIAL escape hatches accept any field, so they match
            # every point set and rank first on every metric. They are a
            # deliberate "not modelled yet" marker, never a suggestion.
            continue
        resolved = ontology.resolve(entity.qualified_name)
        if not resolved.required and not resolved.optional:
            # Types with no fields at all (ROOM, FLOOR, ...) match everything
            # and tell us nothing; a space is chosen by hand, not inferred.
            continue
        candidate = _evaluate(resolved, declared)
        if complete_only and not candidate.is_complete:
            continue
        candidates.append(candidate)

    candidates.sort(key=lambda c: c.sort_key)
    return candidates[:limit]


def explain_choice(
    ontology: Ontology, entity_type: str, declared_fields: frozenset[str] | set[str]
) -> TypeCandidate:
    """Score one specific type -- used to justify a type already on a device."""
    resolved = ontology.resolve(entity_type)
    return _evaluate(resolved, field_set(declared_fields))
# AI:E87M claude-code 2026-08-27 s:2a846146
