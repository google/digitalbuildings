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

from score.types_ import DeserializedFilesDict, TranslationsDict
from validate.entity_instance import EntityInstance


class Dimension:
  """
    Container for floating-point results which
    quantify success in each dimension

    Attributes:
      translations: Proposed and solution translations
        for all matched reporting entities. Assigned via argument
      deserialized_files: Parsed proposed and solution
        configuration files containing all entities.  Assigned via argument

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
               translations: TranslationsDict = None,
               deserialized_files: DeserializedFilesDict = None):
    self.translations = translations
    self.deserialized_files = deserialized_files

    self.correct_virtual: int = None
    self.correct_reporting: int = None
    self.correct_ceiling_virtual: int = None
    self.correct_ceiling_reporting: int = None
    self.incorrect_virtual: int = None
    self.incorrect_reporting: int = None

    self.correct_total_override: int = None
    self.correct_ceiling_override: int = None
    self.incorrect_total_override: int = None

    if not translations and not deserialized_files:
      # `translations` are used to score "simple" dimensions — those which
      # evaluate only reporting entities — in bulk, whereas `deserialized_files`
      # are passed to "complex" dimensions which build a multi-map
      # of virtual entities prior to calculating scores.
      raise Exception(
          '`translations` xor `deserialized_files` argument is required')
    elif translations and deserialized_files:
      raise Exception(
          '`translations` or `deserialized_files` argument must be exclusive')

  def correct_total(self) -> int:
    """ Number of successful attempts within all devices """
    if self.correct_total_override:
      # Allow for value to be set directly for dimensions which
      # don't separately tabulate virtual and reporting scores
      return self.correct_total_override
    else:
      # Allow for value to be returned even if either is not set
      correct_virtual = self.correct_virtual or 0
      correct_reporting = self.correct_reporting or 0
      return correct_virtual + correct_reporting

  def correct_ceiling(self) -> int:
    """ Number of attempts possible within all devices """
    if self.correct_ceiling_override:
      # Allow for value to be set directly for dimensions which
      # don't separately tabulate virtual and reporting scores
      return self.correct_ceiling_override
    else:
      # Allow for value to be returned even if either is not set
      correct_ceiling_virtual = self.correct_ceiling_virtual or 0
      correct_ceiling_reporting = self.correct_ceiling_reporting or 0
      return correct_ceiling_virtual + correct_ceiling_reporting

  def incorrect_total(self) -> int:
    """ Number of failed attempts within all devices """
    if self.incorrect_total_override:
      # Allow for value to be set directly for dimensions which
      # don't separately tabulate virtual and reporting scores
      return self.incorrect_total_override
    else:
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

  @staticmethod
  def is_entity_canonical(*, entity: EntityInstance) -> bool:
    """ Utility for determining whether an entity is canonical.
    Used in "complex" dimensions to filter sets for comparison.

    Args:
      entity: An entity instance which has been appended
      with a `type` attribute equal to its type from the universe

    Returns:
      Boolean indicating whether the entity's `type.is_canonical`
    """
    # NOTE: when passed to filter(), this will silently omit
    # entities whose appended type is `None` (e.g. it was not found)
    return getattr(entity.type, 'is_canonical', False)

  @staticmethod
  def is_entity_reporting(*, entity: EntityInstance) -> bool:
    """
    Utility for determining whether an entity is reporting.
    Used in "complex" dimensions to filter sets for comparison.

    Args:
      entity: A standard entity instance

    Returns:
      Boolean indicating whether the entity has a `cloud_device_id`
    """
    return entity.cloud_device_id is not None

  @staticmethod
  def is_entity_virtual(*, entity: EntityInstance) -> bool:
    """ Utility for determining whether an entity is virtual.
    Used in "complex" dimensions to filter sets for comparison.

    Args:
      entity: A standard entity instance

    Returns:
      Boolean indicating whether the entity has `links`
    """
    return entity.links is not None

  def __str__(self) -> str:
    """ Human-readable representation of the calculated properties """
    return (
        f'{{result_composite: {self.result_composite}, result_virtual: '
        f'{self.result_virtual}, result_reporting: {self.result_reporting}}}')
