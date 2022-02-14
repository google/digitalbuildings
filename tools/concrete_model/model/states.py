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
"""Module for concrete model states."""

from typing import Dict, List


class States(object):
  """Class for concrete model states.

  Attributes:
    standard_to_raw_state_map: A mapping from standard states to a list of
      raw_states coming from the payload device.
  """

  def __init__(self, standard_to_raw_state_map: Dict[str, List[str]]) -> None:
    """Init.

    Args:
      standard_to_raw_state_map: A mapping from standard states to a list of
        raw_states coming from the payload device.
    """
    self.standard_to_raw_state_map = standard_to_raw_state_map

  def AddState(self, standard_state: str, raw_states: List[str]) -> None:
    """Adds a new state mapping to self.standard_to_raw_state_map.

    Args:
      standard_state: A standardized state, i.e. "ON"
      raw_states: A list of raw states coming from the payload device.
    """
