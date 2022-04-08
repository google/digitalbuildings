# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the License);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an AS IS BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Core component base class."""

from score.scorer_types import DeserializedFilesDict, TranslationsDict, PointsVirtualList, RawFieldName, EntityType, FileType
from validate.entity_instance import EntityInstance
from typing import Tuple, Set, List, Dict, NamedTuple
from collections import defaultdict


class _VirtualEntityMatch(NamedTuple):
  """Reference for metrics by which subscores were
  calculated to find the closest corellating virtual entities."""
  # TODO:
  # https://trello.com/c/MBAeYiwI/31-pare-down-virtualentitymatch-attributes-following-implementation-of-entity-type-id
  correct: int
  correct_ceiling: int
  incorrect: int
  proposed: Tuple[Set[RawFieldName], EntityType]
  solution: Tuple[Set[RawFieldName], EntityType]
  types_correct: int
  types_correct_ceiling: int
  types_incorrect: int
  types_score: float


class _FieldsSubscore(NamedTuple):
  """Calculates a subscore which is used in finding
  the closest corellating virtual entities."""
  proposed_raw_field_names: Set[RawFieldName]
  solution_raw_field_names: Set[RawFieldName]

  @property
  def correct(self) -> int:
    return len(
        self.proposed_raw_field_names.intersection(
            self.solution_raw_field_names))

  @property
  def correct_ceiling(self) -> int:
    return len(self.solution_raw_field_names)

  @property
  def incorrect(self) -> int:
    return len(
        self.solution_raw_field_names.difference(self.proposed_raw_field_names))

  @property
  def tally(self) -> float:
    return ((self.correct - self.incorrect) /
            self.correct_ceiling) if self.correct_ceiling != 0 else 0


class _TypesSubscore(NamedTuple):
  """Calculates a type score which is used in finding
  the closest corellating virtual entities."""
  proposed_entity_type: EntityType
  solution_entity_type: EntityType

  @property
  def correct(self) -> int:
    return len(
        set(self.proposed_entity_type.parent_names.keys()).intersection(
            set(self.solution_entity_type.parent_names.keys()))
    ) if self.proposed_entity_type is not None else 0

  @property
  def correct_ceiling(self) -> int:
    return len(set(self.solution_entity_type.parent_names.keys()))

  @property
  def incorrect(self) -> int:
    return len(
        set(self.solution_entity_type.parent_names.keys()).difference(
            set(self.proposed_entity_type.parent_names.keys()))
    ) if self.proposed_entity_type is not None else self.correct_ceiling

  @property
  def tally(self) -> float:
    return ((self.correct - self.incorrect) /
            self.correct_ceiling) if self.correct_ceiling != 0 else 0


class Dimension:
  """Container for floating-point results which
  quantify success in each dimension.

  Attributes:
    translations: Proposed and solution translations
      for all matched reporting entities. Assigned via argument
    deserialized_files: Parsed proposed and solution
      configuration files containing all entities.  Assigned via argument

    correct_virtual: Number of successful attempts within virtual devices
    correct_reporting: Number of successful attempts within reporting devices
    correct_ceiling_virtual: Number of attempts possible
      within virtual devices
    correct_ceiling_reporting: Number of attempts possible
      within reporting devices
    incorrect_virtual: Number of failed attempts within virtual devices
    incorrect_reporting: Number of failed attempts within reporting devices

  Properties:
    result_all: Calculated result for all devices
    result_virtual: Calculated result for virtual devices
    result_reporting: Calculated result for reporting devices"""

  # `category` indicates which argument a dimension is invoked with:
  # "simple" dimensions receive translations whereas "complex" dimensions
  # receive deserialized files. As this is the base class, the `category`
  # is neither of the possible values (SIMPLE or COMPLEX) and both associated
  # arguments are specified with default values of `None`.
  category = None

  def __init__(self,
               *,
               translations: TranslationsDict = None,
               deserialized_files: DeserializedFilesDict = None):
    self.translations = translations
    self.deserialized_files = deserialized_files

    self.correct_virtual: int = None
    self.correct_reporting: int = None
    self.correct_ceiling_virtual: int = None
    self.correct_ceiling_reporting: int = None
    self.incorrect_virtual: int = None
    self.incorrect_reporting: int = None

    self.correct_total_override: int = None
    self.correct_ceiling_override: int = None
    self.incorrect_total_override: int = None

    # Allow for gate below to be passed in case of no matched reporting entities
    translations_truthy_or_empty = translations or isinstance(
        translations, dict)

    if not translations_truthy_or_empty and not deserialized_files:
      # `translations` are used to score "simple" dimensions — those which
      # evaluate only reporting entities — in bulk, whereas `deserialized_files`
      # are passed to "complex" dimensions which typically build a multi-map
      # of virtual entities prior to calculating scores.
      raise Exception(
          '`translations` xor `deserialized_files` argument is required')
    elif translations_truthy_or_empty and deserialized_files:
      raise Exception(
          '`translations` or `deserialized_files` argument must be exclusive')

  def correct_total(self) -> int:
    """Number of successful attempts within all devices."""
    if self.correct_total_override:
      # Allow for value to be set directly for dimensions which
      # don't separately tabulate virtual and reporting scores
      return self.correct_total_override
    else:
      # Allow for value to be returned even if either is not set
      correct_virtual = self.correct_virtual or 0
      correct_reporting = self.correct_reporting or 0
      return correct_virtual + correct_reporting

  def correct_ceiling(self) -> int:
    """Number of attempts possible within all devices."""
    if self.correct_ceiling_override:
      # Allow for value to be set directly for dimensions which
      # don't separately tabulate virtual and reporting scores
      return self.correct_ceiling_override
    else:
      # Allow for value to be returned even if either is not set
      correct_ceiling_virtual = self.correct_ceiling_virtual or 0
      correct_ceiling_reporting = self.correct_ceiling_reporting or 0
      return correct_ceiling_virtual + correct_ceiling_reporting

  def incorrect_total(self) -> int:
    """Number of failed attempts within all devices."""
    if self.incorrect_total_override:
      # Allow for value to be set directly for dimensions which
      # don't separately tabulate virtual and reporting scores
      return self.incorrect_total_override
    else:
      # Allow for value to be returned even if either is not set
      incorrect_virtual = self.incorrect_virtual or 0
      incorrect_reporting = self.incorrect_reporting or 0
      return incorrect_virtual + incorrect_reporting

  def _condense_translations(self, file_type: FileType):
    """Combines translations for all devices within the dictionary."""
    return [
        matched_translations[file_type]
        for matched_translations in self.translations.values()
        if matched_translations[file_type]
    ]

  @property
  def result_all(self) -> float:
    """Calculated result for all devices."""
    return ((self.correct_total() - self.incorrect_total()) /
            self.correct_ceiling()) if self.correct_ceiling() != 0 else None

  @property
  def result_virtual(self) -> float:
    """Calculated result for virtual devices."""
    # Allow for value to be returned even if either is not set
    correct_virtual = self.correct_virtual or 0
    incorrect_virtual = self.incorrect_virtual or 0
    return (
        (correct_virtual - incorrect_virtual) /
        self.correct_ceiling_virtual) if self.correct_ceiling_virtual else None

  @property
  def result_reporting(self) -> float:
    """Calculated result for reporting devices."""
    # Allow for value to be returned even if either is not set
    correct_reporting = self.correct_reporting or 0
    incorrect_reporting = self.incorrect_reporting or 0
    return ((correct_reporting - incorrect_reporting) /
            self.correct_ceiling_reporting
            ) if self.correct_ceiling_reporting else None

  @staticmethod
  def is_entity_canonical(entity: EntityInstance) -> bool:
    """Utility for determining whether an entity is canonical.
    Used in "complex" dimensions to filter sets for comparison.

    Args:
      entity: An entity instance which has been appended
      with a `type` attribute equal to its type from the universe

    Returns:
      Boolean indicating whether the entity's `type.is_canonical`"""
    # NOTE: when passed to filter(), this will silently omit
    # entities whose appended type is `None` (e.g. it was not found)
    return getattr(entity.type, 'is_canonical', False)

  @staticmethod
  def is_entity_reporting(entity: EntityInstance) -> bool:
    """Utility for determining whether an entity is reporting.
    Used in "complex" dimensions to filter sets for comparison.

    Args:
      entity: A standard entity instance

    Returns:
      Boolean indicating whether the entity has a `cloud_device_id`"""
    return entity.cloud_device_id is not None

  @staticmethod
  def is_entity_virtual(entity: EntityInstance) -> bool:
    """Utility for determining whether an entity is virtual.
    Used in "complex" dimensions to filter sets for comparison.

    Args:
      entity: A standard entity instance

    Returns:
      Boolean indicating whether the entity has `links`"""
    return entity.links is not None

  @staticmethod
  def _match_virtual_entities(
      *, solution_points_virtual: PointsVirtualList,
      proposed_points_virtual: PointsVirtualList,
      sort_candidates_by_key: str) -> Dict[float, List[_VirtualEntityMatch]]:
    """Finds the closest correlating virtual entities between two files
    by comparing the intersections of raw field names contained therein.

    Args:
      solution_points_virtual: Raw field names and entity types
        for all virtual entities in a file
      proposed_points_virtual: Raw field names and entity types
        for all virtual entities in a file
      sort_candidates_by_key: Parameter by which to "break a tie"
        if there are multiple matches with the same subscore.

    Returns:
      Dictionary whose keys are floats representing the extent to which the
      provided entities correlated and whose values are lists of
      _VirtualEntityMatch instances containing the metrics
      by which those floats were calculated."""
    # Final pairings
    matches_virtual = {None: []}

    for solution_parameters in solution_points_virtual:
      solution_raw_field_names, solution_entity_type = solution_parameters

      # Record of entities evaluated and associated metrics
      candidates = defaultdict(list)
      # Running tally of which entity most closely corellates;
      # even zero overlap will best the default at -1.0
      best: float = -1.1

      for proposed_parameters in proposed_points_virtual:
        proposed_raw_field_names, proposed_entity_type = proposed_parameters

        # Offload the quantification of intersection/difference
        # and resulting subscore
        subscore = _FieldsSubscore(
            proposed_raw_field_names=proposed_raw_field_names,
            solution_raw_field_names=solution_raw_field_names)

        # Meanwhile, calculate a similar metric for overlap of types
        types_score = _TypesSubscore(proposed_entity_type=proposed_entity_type,
                                     solution_entity_type=solution_entity_type)

        # If the current iteration matches better than the last,
        # take note of its score for later lookup
        if subscore.tally != 0 and subscore.tally > best:
          best = subscore.tally

        subscore_reference = _VirtualEntityMatch(
            correct=subscore.correct,
            correct_ceiling=subscore.correct_ceiling,
            incorrect=subscore.incorrect,
            proposed=proposed_parameters,
            solution=solution_parameters,
            types_correct=types_score.correct,
            types_correct_ceiling=types_score.correct_ceiling,
            types_incorrect=types_score.incorrect,
            types_score=types_score.tally)

        # Add record of the evaluation for sorting
        # after considering all the candidates
        candidates[subscore.tally].append(subscore_reference)

      # Choose the closest match
      selected = sorted(
          candidates[best],
          # Use `._asdict()` to reference index by string
          key=lambda params: params._asdict()[sort_candidates_by_key],
          reverse=True)[0] if len(candidates[best]) else None

      if selected:
        if best in matches_virtual:
          matches_virtual[best].append(selected)
        else:
          matches_virtual[best] = [selected]
        # Since a match was found, remove it from the pool
        proposed_points_virtual.remove(selected.proposed)
      else:
        correct_ceiling = len(solution_raw_field_names)
        none_subscore_reference = _VirtualEntityMatch(
            correct=0,
            correct_ceiling=correct_ceiling,
            incorrect=correct_ceiling,  # i.e. everything is incorrect
            proposed=set([]),
            solution=solution_parameters,
            types_correct=0,
            types_correct_ceiling=len(
                set(solution_entity_type.parent_names.keys())),
            types_incorrect=len(set(solution_entity_type.parent_names.keys())),
            types_score=-1.0)

        matches_virtual[None].append(none_subscore_reference)

    return matches_virtual

  def __str__(self) -> str:
    """Human-readable representation of the calculated properties."""
    return (
        f'{{result_all: {self.result_all}, result_virtual: '
        f'{self.result_virtual}, result_reporting: {self.result_reporting}}}')
