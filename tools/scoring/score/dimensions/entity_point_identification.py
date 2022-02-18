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
""" Core component """

from score.dimensions.dimension import Dimension
from score.types_ import PointsVirtualList
from score.constants import FileTypes

PROPOSED, SOLUTION = FileTypes


class EntityPointIdentification(Dimension):
  """
  Quantifies whether the proposed file
  included the correct points in each entity.
  """
  def evaluate(self):
    proposed_file, solution_file = map(self.deserialized_files.get,
                                       (PROPOSED, SOLUTION))

    # Isolate canonically typed virtual entities
    entities_virtual = lambda file: set(
        filter(self.is_entity_canonical,
               filter(self.is_entity_virtual, file.values())))

    solution_entities_virtual = entities_virtual(solution_file)
    proposed_entities_virtual = entities_virtual(proposed_file)

    # For each canonically typed virtual entity
    # create a tuple containing a set and the entity's type.
    # (The type is required by the matching algo for a different dimension.)
    # For each link in the entity,
    # if the field exists at the source
    # add its raw field name to the set.
    # Filter out sets which have no items
    # and sort by number of fields represented in descending order.
    # TODO: move the filtering/sorting functionality to add clarity.
    points_virtual: PointsVirtualList = lambda file, entities_virtual: sorted(
        list(
            filter(
                lambda tup: len(tup[0]) > 0,  # (raw field names, entity type)
                [(set(file[link.source].translation[target_field].raw_field_name
                      for target_field, source_field in link.field_map.items()
                      for link in entity.links if target_field in file[
                          link.source].translation), entity.type)
                 for entity in entities_virtual for link in entity.links])),
        key=lambda tup: len(tup[0]),  # (raw field names, entity type)
        reverse=True)

    solution_points_virtual = points_virtual(solution_file,
                                             solution_entities_virtual)
    proposed_points_virtual = points_virtual(proposed_file,
                                             proposed_entities_virtual)

    # Rely on the black box to choose which virtual entities
    # correlate most closely in the respective files.
    matches_virtual = self.match_virtual_entities(
        solution_points_virtual=solution_points_virtual,
        proposed_points_virtual=proposed_points_virtual,
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

    ###

    # Isolate canonically typed reporting entities
    entities_reporting = lambda file: set(
        filter(self.is_entity_canonical,
               filter(self.is_entity_reporting, file.values())))

    solution_entities_reporting = entities_reporting(solution_file)
    proposed_entities_reporting = entities_reporting(proposed_file)

    # Aggregate IDs for entities which comprise the composites
    # evaluated above. These will be filtered out below so as to
    # not be scored again.
    source_ids = lambda file, entities_virtual: set(file[
        source].cloud_device_id for sublist in (
            (link.source
             for target_field, source_field in link.field_map.items()
             for link in entity.links
             if target_field in file[link.source].translation)
            for entity in entities_virtual for link in entity.links)
                                                    for source in sublist)

    solution_source_ids = source_ids(solution_file, solution_entities_virtual)
    proposed_source_ids = source_ids(proposed_file, proposed_entities_virtual)

    is_not_source = lambda source_ids: (lambda entity: entity.cloud_device_id
                                        not in source_ids)

    is_not_source_solution = is_not_source(solution_source_ids)
    is_not_source_proposed = is_not_source(proposed_source_ids)

    matches_reporting = []
    for solution_entity in filter(is_not_source_solution,
                                  solution_entities_reporting):
      # Reassigned below if there is an ID match
      proposed_raw_field_names = set([])
      solution_raw_field_names = (set(
          translation.raw_field_name
          for translation in solution_entity.translation.values()))

      for proposed_entity in filter(is_not_source_proposed,
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
        len(proposed_raw_field_names.difference(solution_raw_field_names)) for
        proposed_raw_field_names, solution_raw_field_names in matches_reporting
    ])

    return self
