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
"""Core component."""

from score.dimensions.dimension import Dimension
from score.scorer_types import DeserializedFile, EntityInstance, CloudDeviceId, PointsVirtualList
from score.constants import FileTypes, DimensionCategories

from typing import Set
from collections import namedtuple

PROPOSED, SOLUTION = FileTypes


class EntityPointIdentification(Dimension):
  """Quantifies whether the proposed file
  included the correct points in each entity."""

  # COMPLEX category indicates this dimension receives `deserialized_files`
  # rather than `translations` to do its calculations
  category = DimensionCategories.COMPLEX

  def _isolate_entities_virtual(
      self, *, file: DeserializedFile,
      exclude_noncanonical: bool) -> Set[EntityInstance]:
    virtual_entities = filter(self.is_entity_virtual, file.values())
    return set(
        filter(self.is_entity_canonical, virtual_entities
               ) if exclude_noncanonical else virtual_entities)

  @staticmethod
  def _fetch_points_virtual(
      file: DeserializedFile,
      entities_virtual: Set[EntityInstance]) -> PointsVirtualList:
    # For each virtual entity
    # create a named tuple containing a set and the entity's type.
    # (The type is required by the matching algo for a different dimension.)
    # For each link in the entity,
    # if the field exists at the source
    # add its raw field name to the set.
    PointsVirtual = namedtuple('PointsVirtual',
                               ['raw_field_names', 'entity_type'])

    return [
        PointsVirtual(
            set(file[link.source].translation[target_field].raw_field_name
                for target_field, source_field in link.field_map.items()
                for link in entity.links
                if target_field in file[link.source].translation), entity.type)
        for entity in entities_virtual for link in entity.links
    ]

  @staticmethod
  def _sort_filter_points_virtual(
      points_virtual: PointsVirtualList) -> PointsVirtualList:
    # Filter out sets which have no items
    # and sort by number of fields represented in descending order.
    filtered = list(
        filter(lambda entry: len(entry.raw_field_names) > 0, points_virtual))

    return sorted(filtered,
                  key=lambda entry: len(entry.raw_field_names),
                  reverse=True)

  def _isolate_entities_reporting(
      self, *, file: DeserializedFile,
      exclude_noncanonical: bool) -> Set[EntityInstance]:
    reporting_entities = filter(self.is_entity_reporting, file.values())
    return set(
        filter(self.is_entity_canonical, reporting_entities
               ) if exclude_noncanonical else reporting_entities)

  @staticmethod
  def _fetch_source_ids_virtual(
      file: DeserializedFile,
      entities_virtual: Set[EntityInstance]) -> Set[CloudDeviceId]:
    # Aggregate IDs for entities which comprise the composites
    # evaluated above. These will be filtered out so as to
    # not be scored again.
    return set(file[source].cloud_device_id for sublist in (
        (link.source for target_field, source_field in link.field_map.items()
         for link in entity.links
         if target_field in file[link.source].translation)
        for entity in entities_virtual for link in entity.links)
               for source in sublist)

  def _evaluate_virtual(self, *, proposed_file: DeserializedFile,
                        solution_file: DeserializedFile):
    """Calculates and assigns properties necessary
    for generating an entity point identification score for virtual devices."""
    proposed_entities_virtual = self._isolate_entities_virtual(
        file=proposed_file, exclude_noncanonical=False)
    solution_entities_virtual = self._isolate_entities_virtual(
        file=solution_file, exclude_noncanonical=True)

    proposed_points_virtual = self._fetch_points_virtual(
        proposed_file, proposed_entities_virtual)
    solution_points_virtual = self._fetch_points_virtual(
        solution_file, solution_entities_virtual)

    # Rely on the black box to choose which virtual entities
    # correlate most closely in the respective files.
    matches_virtual = self._match_virtual_entities(
        solution_points_virtual=self._sort_filter_points_virtual(
            solution_points_virtual),
        proposed_points_virtual=self._sort_filter_points_virtual(
            proposed_points_virtual),
        sort_candidates_by_key='correct_ceiling')

    self.correct_virtual = sum([
        sum(match.correct for match in list)
        for list in matches_virtual.values()
    ])
    self.correct_ceiling_virtual = sum([
        sum(match.correct_ceiling for match in list)
        for list in matches_virtual.values()
    ])
    self.incorrect_virtual = sum([
        sum(match.incorrect for match in list)
        for list in matches_virtual.values()
    ])

  def _evaluate_reporting(self, *, proposed_file: DeserializedFile,
                          solution_file: DeserializedFile):
    """Calculates and assigns properties necessary
    for generating an entity point identification
    score for reporting devices."""
    proposed_entities_reporting = self._isolate_entities_reporting(
        file=proposed_file, exclude_noncanonical=False)
    solution_entities_reporting = self._isolate_entities_reporting(
        file=solution_file, exclude_noncanonical=True)

    proposed_entities_virtual = self._isolate_entities_virtual(
        file=proposed_file, exclude_noncanonical=False)
    solution_entities_virtual = self._isolate_entities_virtual(
        file=solution_file, exclude_noncanonical=True)

    proposed_source_ids = self._fetch_source_ids_virtual(
        proposed_file, proposed_entities_virtual)
    solution_source_ids = self._fetch_source_ids_virtual(
        solution_file, solution_entities_virtual)

    is_not_source = lambda source_ids: (lambda entity: entity.cloud_device_id
                                        not in source_ids)

    matches_reporting = []
    for solution_entity in filter(is_not_source(solution_source_ids),
                                  solution_entities_reporting):
      # Reassigned below if there is an ID match
      proposed_raw_field_names = set([])
      solution_raw_field_names = (set(
          translation.raw_field_name
          for translation in solution_entity.translation.values()))

      for proposed_entity in filter(is_not_source(proposed_source_ids),
                                    proposed_entities_reporting):
        if proposed_entity.cloud_device_id == solution_entity.cloud_device_id:
          proposed_raw_field_names = (set(
              translation.raw_field_name
              for translation in proposed_entity.translation.values()))
      matches_reporting.append(
          (proposed_raw_field_names, solution_raw_field_names))

    self.correct_reporting = sum([
        len(proposed_raw_field_names.intersection(solution_raw_field_names)) for
        proposed_raw_field_names, solution_raw_field_names in matches_reporting
    ])
    self.correct_ceiling_reporting = sum([
        len(solution_raw_field_names) for proposed_raw_field_names,
        solution_raw_field_names in matches_reporting
    ])
    self.incorrect_reporting = sum([
        len(solution_raw_field_names.difference(proposed_raw_field_names)) for
        proposed_raw_field_names, solution_raw_field_names in matches_reporting
    ])

  def evaluate(self):
    """Calculates and assigns properties necessary
    for generating an entity point identification score for all devices."""

    proposed_file, solution_file = map(self.deserialized_files.get,
                                       (PROPOSED, SOLUTION))

    self._evaluate_virtual(proposed_file=proposed_file,
                           solution_file=solution_file)
    self._evaluate_reporting(proposed_file=proposed_file,
                             solution_file=solution_file)

    return self
