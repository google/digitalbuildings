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

# from collections import Counter

from score.dimensions.dimension import Dimension
from score.constants import FileTypes, DimensionCategories
from score.scorer_types import DeserializedFile, ConnectionsList

from typing import Set
from collections import namedtuple

PROPOSED, SOLUTION = FileTypes


class EntityConnectionIdentification(Dimension):
  """Quantifies whether connections between entities were
  correctly and completely defined in the proposed file."""

  # COMPLEX category indicates this dimension receives `deserialized_files`
  # rather than `translations` to do its calculations
  category = DimensionCategories.COMPLEX

  @staticmethod
  def _isolate_connections(file: DeserializedFile) -> ConnectionsList:
    """Distill individual connections from each entity
    prior to inclusion in sets for global comparison."""
    Connection = namedtuple('Connection', ['target', 'connection'])

    all_connections = []
    for entity in file.values():
      if entity.connections is not None:
        for connection in entity.connections:
          all_connections.append(Connection(entity.code, connection))
    return all_connections

  @staticmethod
  def _get_cdid(code_or_guid: str, *, file: DeserializedFile) -> str:
    """Returns an entity's `cloud_device_id` if available
    to increase the likelihood of connections matching between files"""
    for entity in file.values():
      if code_or_guid in [entity.code, entity.guid]:
        return entity.cloud_device_id or entity.code

  def _condense_connections(self, connections: ConnectionsList, *,
                            file: DeserializedFile) -> Set[str]:
    """Condense connections into sets of strings
    for easy comparison using intersection."""
    condensed = set()
    for cn in connections:
      # e.g. "THAT_ENTITY CONTAINS THIS_ENTITY"
      condensed.add(
          f'{self._get_cdid(cn.connection.source, file=file)} '
          f'{cn.connection.ctype} {self._get_cdid(cn.target, file=file)}')
    return condensed

  def evaluate(self):
    """Calculate and assign properties necessary for generating a score."""

    proposed_file, solution_file = map(self.deserialized_files.get,
                                       (PROPOSED, SOLUTION))

    proposed_connections, solution_connections = map(
        self._isolate_connections, (proposed_file, solution_file))

    proposed_connections_condensed = self._condense_connections(
        proposed_connections, file=proposed_file)
    solution_connections_condensed = self._condense_connections(
        solution_connections, file=solution_file)

    # Compare them
    correct = proposed_connections_condensed.intersection(
        solution_connections_condensed)

    # Set attributes which allow for result to be calculated
    # independent of "virtual" and "reporting" buckets
    self.correct_total_override = len(correct)
    self.correct_ceiling_override = len(solution_connections_condensed)
    self.incorrect_total_override = (self.correct_ceiling_override -
                                     self.correct_total_override)

    return self
