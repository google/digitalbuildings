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
"""Outputs of the configuration scoring tool."""
from dataclasses import dataclass


@dataclass
class Result:
  """
    Container for floating-point results which
    quantify success in each dimension

    Attributes:
      correct_virtual: Number of attempts achieved within virtual devices
      correct_reporting: Number of attempts achieved within reporting devices
      correct_ceiling_virtual: Number of attempts possible to achieve
        within virtual devices
      correct_ceiling_reporting: Number of attempts possible to achieve
        within reporting devices
      incorrect_virtual: Number of attempts not achieved within virtual devices
      incorrect_reporting: Number of attempts not achieved
        within reporting devices

    Properties:
      result_composite: Calculated result for all devices
      result_virtual: Calculated result for virtual devices
      result_reporting: Calculated result for reporting devices
  """

  correct_virtual: int
  correct_reporting: int
  correct_ceiling_virtual: int
  correct_ceiling_reporting: int
  incorrect_virtual: int
  incorrect_reporting: int

  def correct(self) -> int:
    """ Number of attempts achieved within all devices """
    return self.correct_virtual + self.correct_reporting

  def correct_ceiling(self) -> int:
    """ Number of attempts possible to achieve within all devices """
    return self.correct_ceiling_virtual + self.correct_ceiling_reporting

  def incorrect(self) -> int:
    """ Number of attempts not achieved within all devices """
    return self.incorrect_virtual + self.incorrect_reporting

  @property
  def composite(self) -> float:
    """ Calculated result for all devices """
    return ((self.correct() - self.incorrect()) /
            self.correct_ceiling()) if self.correct_ceiling() != 0 else None

  @property
  def virtual(self) -> float:
    """ Calculated result for virtual devices """
    return ((self.correct_virtual - self.incorrect_virtual) /
            self.correct_ceiling_virtual
            ) if self.correct_ceiling_virtual != 0 else None

  @property
  def reporting(self) -> float:
    """ Calculated result for reporting devices """
    return ((self.correct_reporting - self.incorrect_reporting) /
            self.correct_ceiling_reporting
            ) if self.correct_ceiling_reporting != 0 else None

  def __str__(self) -> str:
    """ Human-readable representation of the calculated properties"""
    return (f'{{composite: {self.composite}, virtual: '
            f'{self.virtual}, reporting: {self.reporting}}}')
