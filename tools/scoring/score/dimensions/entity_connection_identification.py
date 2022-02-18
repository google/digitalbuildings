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

# from collections import Counter

from score.dimensions.dimension import Dimension
from score.types_ import DeserializedFilesDict
from score.constants import FileTypes

PROPOSED, SOLUTION = FileTypes


class EntityConnectionIdentification(Dimension):
  """
  Quantifies whether connections between entities were
  correctly and completely defined in the proposed file.
  """

  # TODO: Figure out how to elegantly implement "facilities"
  # and "equipment" categories given current object model
  def __init__(self, *, deserialized_files: DeserializedFilesDict):
    super().__init__(deserialized_files=deserialized_files)

    proposed, solution = map(deserialized_files.get, (PROPOSED, SOLUTION))

    # Isolate the connections from each dictionary of entities
    solution_connections = [
        tup for tup in (((cloud_device_id, connection)
                         for connection in entity.connections)
                        for cloud_device_id, entity in solution.items()
                        if entity.connections is not None) for tup in tup
    ]
    proposed_connections = [
        tup for tup in (((cloud_device_id, connection)
                         for connection in entity.connections)
                        for cloud_device_id, entity in proposed.items()
                        if entity.connections is not None) for tup in tup
    ]

    fstring = (lambda target, connection:
               f'{target} {connection.ctype} {connection.source}')

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
    self.incorrect_total_override = (self.correct_ceiling_override -
                                     self.correct_total_override)
