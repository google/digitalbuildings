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

from collections import Counter

from score.dimensions.dimension import Dimension
from score.types_ import DeserializedFilesDict
from score.constants import FileTypes

PROPOSED, SOLUTION = FileTypes


class EntityIdentification(Dimension):
  """
  Quantifies whether the correct entities
  were included in the proposed file.
  """
  def __init__(self, *, deserialized_files: DeserializedFilesDict):
    super().__init__(deserialized_files=deserialized_files)

    proposed, solution = map(deserialized_files.get, (PROPOSED, SOLUTION))

    # Lists of `cloud_device_id`s representing
    # reporting entities with canonical types
    solution_reporting = [
        entity.cloud_device_id for entity in filter(
            self.is_entity_canonical,
            filter(self.is_entity_reporting, solution.values()))
    ]
    proposed_reporting = [
        entity.cloud_device_id for entity in filter(
            self.is_entity_canonical,
            filter(self.is_entity_reporting, proposed.values()))
    ]

    # Lists of `cloud_device_id`s representing
    # reporting entities with canonical types that
    # are linked to by virtual entities
    solution_virtual = [
        cloud_device_id for source_list in ((
            solution[link.source].cloud_device_id
            for link in entity.links) for entity in filter(
                self.is_entity_canonical,
                filter(self.is_entity_virtual, solution.values())))
        for cloud_device_id in source_list
    ]
    proposed_virtual = [
        cloud_device_id for source_list in ((
            proposed[link.source].cloud_device_id
            for link in entity.links) for entity in filter(
                self.is_entity_canonical,
                filter(self.is_entity_virtual, proposed.values())))
        for cloud_device_id in source_list
    ]

    self.correct_reporting = sum(
        (Counter(proposed_reporting) & Counter(solution_reporting)).values())
    self.correct_ceiling_reporting = len(solution_reporting)
    self.incorrect_reporting = (self.correct_ceiling_reporting -
                                self.correct_reporting)

    self.correct_virtual = sum(
        (Counter(proposed_virtual) & Counter(solution_virtual)).values())
    self.correct_ceiling_virtual = len(solution_virtual)
    self.incorrect_virtual = self.correct_ceiling_virtual - self.correct_virtual
