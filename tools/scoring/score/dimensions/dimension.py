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
"""Core component base class"""

from typing import Any, Dict, List, Tuple
from validate.entity_instance import EntityInstance


class Dimension:
  """
    Container for floating-point results which
    quantify success in each dimension

    Attributes:
      translations: Proposed and solution translations
        for all matched reporting entities. Assigned via argument
      deserialized_files: Parsed configuration files.  Assigned via argument

      correct_virtual: Number of successful attempts within virtual devices
      correct_reporting: Number of successful attempts within reporting devices
      correct_ceiling_virtual: Number of attempts possible
        within virtual devices
      correct_ceiling_reporting: Number of attempts possible
        within reporting devices
      incorrect_virtual: Number of failed attempts within virtual devices
      incorrect_reporting: Number of failed attempts within reporting devices

    Properties:
      result_composite: Calculated result for all devices
      result_virtual: Calculated result for virtual devices
      result_reporting: Calculated result for reporting devices
  """
  def __init__(self,
               *,
               translations: Dict[str, List[Tuple[str, Any]]] = None,
               deserialized_files: Dict[str, Dict[str, EntityInstance]] = None):
    self.translations = translations
    self.deserialized_files = deserialized_files
    # self.type: Literal['simple', 'complex'] = None

    self.correct_virtual: int = None
    self.correct_reporting: int = None
    self.correct_ceiling_virtual: int = None
    self.correct_ceiling_reporting: int = None
    self.incorrect_virtual: int = None
    self.incorrect_reporting: int = None

    if not translations and not deserialized_files:
      raise Exception(
          '`translations` xor `deserialized_files` argument is required')
    elif translations and deserialized_files:
      raise Exception(
          '`translations` or `deserialized_files` argument must be exclusive')

  def correct_total(self) -> int:
    """ Number of successful attempts within all devices """
    # Allow for value to be returned even if either is not set
    correct_virtual = self.correct_virtual or 0
    correct_reporting = self.correct_reporting or 0
    return correct_virtual + correct_reporting

  def correct_ceiling(self) -> int:
    """ Number of attempts possible within all devices """
    # Allow for value to be returned even if either is not set
    correct_ceiling_virtual = self.correct_ceiling_virtual or 0
    correct_ceiling_reporting = self.correct_ceiling_reporting or 0
    return correct_ceiling_virtual + correct_ceiling_reporting

  def incorrect_total(self) -> int:
    """ Number of failed attempts within all devices """
    # Allow for value to be returned even if either is not set
    incorrect_virtual = self.incorrect_virtual or 0
    incorrect_reporting = self.incorrect_reporting or 0
    return incorrect_virtual + incorrect_reporting

  @property
  def result_composite(self) -> float:
    """ Calculated result for all devices """
    return ((self.correct_total() - self.incorrect_total()) /
            self.correct_ceiling()) if self.correct_ceiling() != 0 else None

  @property
  def result_virtual(self) -> float:
    """ Calculated result for virtual devices """
    # Allow for value to be returned even if either is not set
    correct_virtual = self.correct_virtual or 0
    incorrect_virtual = self.correct_virtual or 0
    return (
        (correct_virtual - incorrect_virtual) /
        self.correct_ceiling_virtual) if self.correct_ceiling_virtual else None

  @property
  def result_reporting(self) -> float:
    """ Calculated result for reporting devices """
    # Allow for value to be returned even if either is not set
    correct_reporting = self.correct_reporting or 0
    incorrect_reporting = self.incorrect_reporting or 0
    return ((correct_reporting - incorrect_reporting) /
            self.correct_ceiling_reporting
            ) if self.correct_ceiling_reporting else None

  def __str__(self) -> str:
    """ Human-readable representation of the calculated properties"""
    return (
        f'{{result_composite: {self.result_composite}, result_virtual: '
        f'{self.result_virtual}, result_reporting: {self.result_reporting}}}')
