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

from score.constants import FileTypes
from score.dimensions.dimension import Dimension
from score.types_ import DeserializedFilesDict

PROPOSED, SOLUTION = FileTypes


class EntityConnectionIdentification(Dimension):
  """Quantifies whether connections between entities were correctly and completely defined in the proposed file."""

  # TODO(b/210741084): Figure out how to elegantly implement "facilities"
  # and "equipment" categories given current object model
  def __init__(self, *, deserialized_files: DeserializedFilesDict):
    super().__init__(deserialized_files=deserialized_files)

    proposed, solution = map(deserialized_files.get, (PROPOSED, SOLUTION))

    # Isolate the connections from each dictionary of entities
    solution_connections = []
    for cloud_device_id, entity in solution.items():
      for connection in entity.connections:
        solution_connections.append((cloud_device_id, connection))

    proposed_connections = []
    for cloud_device_id, entity in proposed.items():
      for connection in entity.connections:
        proposed_connections.append((cloud_device_id, connection))

    # Condense them into sets of strings for easy comparison using intersection
    solution_connections_condensed = set([
        fstring(target, connection)
        for target, connection in solution_connections
    ])
    proposed_connections_condensed = set([
        fstring(target, connection)
        for target, connection in proposed_connections
    ])

    # Compare them
    correct = proposed_connections_condensed.intersection(
        solution_connections_condensed)

    # Set attributes which allow for result to be calculated
    # independent of "virtual" and "reporting" buckets
    self.correct_total_override = len(correct)
    self.correct_ceiling_override = len(solution_connections_condensed)
    self.incorrect_total_override = (
        self.correct_ceiling_override - self.correct_total_override)


def fstring(target, connection):
  return f'{target} {connection.ctype} {connection.source}'
