# Copyright 2020 Google LLC
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
"""Types representing field translations."""

import enum

from typing import Dict


class PresenceMode(enum.Enum):
  """Presence modes for a field in a translation."""
  PRESENT = 'PRESENT'  # Typical mode for a field
  MISSING = 'MISSING'  # Use when a device is missing a required field


class FieldTranslation(object):
  """Base class for a translation of a field in an entity.

  Data provided for this class and its subclasses is expected to be entered as
  it would be seen in a valid building config file.  This means that there will
  be some ambiguity about what the data means without context (ex: one does not
  know if a field is local or global until one knows the namespace of the
  entity's type).  In the case of a partial update, validation will not
  necessarily be able to resolve all ambiguities (ex: if the user does not
  provide the entity's type).  This is an expected limitation.

  Attributes:
    std_field_name: string. Standard name of the field in the ontology.  Field
      should be fully qualified if it is not in the same namespace as the entity
      type or globally defined without a local override.
    mode: the PresenceMode of the field
  """

  def __init__(self, std_field_name: str, mode: PresenceMode):
    super().__init__()
    if not std_field_name:
      raise ValueError('std_field_name cannot be empty')
    self.std_field_name = std_field_name
    self.mode = mode


class UndefinedField(FieldTranslation):
  """A translation for a single field that is missing in the device payload.

  Attributes:
    std_field_name: string. Standard name of the field in the ontology. Field
      should be fully qualified if it is not in the same namespace as the entity
      type or globally defined without a local override.
  """

  def __init__(self, std_field_name: str):
    super().__init__(std_field_name, PresenceMode.MISSING)


class DefinedField(FieldTranslation):
  """A class for translation of a single field present in the device payload.

  Attributes:
    std_field_name: string. Standard name of the field in the ontology. Field
      should be fully qualified (namespace/field) if it is not in the same
      namespace as the entity type or in the global namespace without a local
      override.
    raw_field_name: string. Fully qualified json path to the field in the device
      payload.
  """

  def __init__(self, std_field_name: str, raw_field_name: str):
    super().__init__(std_field_name, PresenceMode.PRESENT)
    if not raw_field_name:
      raise ValueError('raw_field_name cannot be empty')
    self.raw_field_name = raw_field_name


class MultiStateValue(DefinedField):
  """A translation for a field with a multistate value.

  Attributes:
    std_field_name: string. Standard name of the field in the ontology. Field
      should be fully qualified (namespace/field) if it is not in the same
      namespace as the entity type or in the global namespace without a local
      override.
    raw_field_name: string. Fully qualified json path to the field in the device
      payload.
    states: Dictionary from standard states to expected telemetry states. States
      should be qualified like fields, as would be required in a valid building
      config file.
  """

  def __init__(self, std_field_name: str, raw_field_name: str,
               states: Dict[str, str]):
    super().__init__(std_field_name, raw_field_name)
    if not states:
      raise ValueError('states cannot be empty')
    self.states = states


class DimensionalValue(DefinedField):
  """A translation for field with a dimensional number value, ex: temperature.

  Attributes:
    std_field_name: string. Standard name of the field in the ontology.  Field
      should be fully qualified (namespace/field) if it is not in the same
      namespace as the entity type or in the global namespace without a local
      override.
    raw_field_name: string. Fully qualified json path to the field in the device
      payload.
    unit_field_name: string. Fully qualified json path to the unit in the device
      payload.
    unit_mappings: Dictionary from standard units to the text defining the unit
      in the payload.
  """

  def __init__(self, std_field_name: str, raw_field_name: str,
               unit_field_name: str, unit_mappings: Dict[str, str]):
    super().__init__(std_field_name, raw_field_name)
    if not unit_field_name:
      raise ValueError('unit_field_name cannot be empty')
    if not unit_mappings:
      raise ValueError('unit_mappings cannot be empty')
    # Note: I didn't go so far as to define a units object yet since the
    # structure of units is being worked on. It can be retrofitted later.
    self.unit_field_name = unit_field_name
    self.unit_mappings = unit_mappings


class NonDimensionalValue(DefinedField):
  """A translation for field with a non-dimensional value, ex: text or a gain.

  Use this translation for non-dimensional numbers or strings.

  Attributes:
    std_field_name: string. Standard name of the field in the ontology.  Field
      should be fully qualified (namespace/field) if it is not in the same
      namespace as the entity type or in the global namespace without a local
      override.
    raw_field_name: string. Fully qualified json path to the field in the device
      payload.
  """
