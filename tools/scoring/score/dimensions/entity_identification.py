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

from collections import Counter

from score.dimensions.dimension import Dimension
from score.constants import FileTypes, DimensionCategories
from score.scorer_types import DeserializedFile, CloudDeviceId

from typing import List

PROPOSED, SOLUTION = FileTypes


class EntityIdentification(Dimension):
  """Quantifies whether the correct entities
  were included in the proposed file."""

  # COMPLEX category indicates this dimension receives `deserialized_files`
  # rather than `translations` to do its calculations
  category = DimensionCategories.COMPLEX

  def _list_ids_reporting(self, *, file: DeserializedFile,
                          exclude_noncanonical: bool) -> List[CloudDeviceId]:
    """Generates list of `cloud_device_id`s representing reporting entities."""
    reporting_entities = filter(self.is_entity_reporting, file.values())
    filtered = filter(
        self.is_entity_canonical,
        reporting_entities) if exclude_noncanonical else reporting_entities
    return [entity.cloud_device_id for entity in filtered]

  def _list_ids_virtual(self, *, file: DeserializedFile,
                        exclude_noncanonical: bool) -> List[CloudDeviceId]:
    """Generates list of `cloud_device_id`s representing
    reporting entities that are linked to by virtual entities."""
    virtual_entities = filter(self.is_entity_virtual, file.values())
    filtered = filter(
        self.is_entity_canonical,
        virtual_entities) if exclude_noncanonical else virtual_entities
    return [
        cloud_device_id for source_list in ((file[link.source].cloud_device_id
                                             for link in entity.links)
                                            for entity in filtered)
        for cloud_device_id in source_list
    ]

  def evaluate(self):
    """Calculates and assigns properties necessary for generating a score."""

    proposed_file, solution_file = map(self.deserialized_files.get,
                                       (PROPOSED, SOLUTION))

    proposed_reporting_ids = self._list_ids_reporting(
        file=proposed_file, exclude_noncanonical=False)
    solution_reporting_ids = self._list_ids_reporting(file=solution_file,
                                                      exclude_noncanonical=True)

    proposed_virtual_ids = self._list_ids_virtual(file=proposed_file,
                                                  exclude_noncanonical=False)
    solution_virtual_ids = self._list_ids_virtual(file=solution_file,
                                                  exclude_noncanonical=True)

    self.correct_reporting = sum((Counter(proposed_reporting_ids)
                                  & Counter(solution_reporting_ids)).values())
    self.correct_ceiling_reporting = len(solution_reporting_ids)
    self.incorrect_reporting = (self.correct_ceiling_reporting -
                                self.correct_reporting)

    self.correct_virtual = sum((Counter(proposed_virtual_ids)
                                & Counter(solution_virtual_ids)).values())
    self.correct_ceiling_virtual = len(solution_virtual_ids)
    self.incorrect_virtual = self.correct_ceiling_virtual - self.correct_virtual

    return self
