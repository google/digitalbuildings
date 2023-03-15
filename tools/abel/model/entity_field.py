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
"""Module to hold EntityField class."""

from typing import Dict, List, Optional

from model.constants import BC_GUID
from model.constants import ENTITY_CODE
from model.constants import METADATA
from model.constants import MISSING
from model.constants import MISSING_FALSE
from model.constants import MISSING_TRUE
from model.constants import NO_UNITS
from model.constants import RAW_FIELD_NAME
from model.constants import RAW_UNIT_PATH
from model.constants import RAW_UNIT_VALUE
from model.constants import REPORTING_ENTITY_CODE
from model.constants import REPORTING_ENTITY_FIELD_NAME
from model.constants import REPORTING_ENTITY_GUID
from model.constants import STANDARD_FIELD_NAME
from model.constants import STANDARD_UNIT_VALUE
from model.guid_to_entity_map import GuidToEntityMap
from model.state import State
from model.units import Units
from validate import field_translation


# TODO(b/264897818) Refactor inits to EntityField base class and implement dual
# inheritance.
class MissingField(field_translation.UndefinedField):
  """Class for a single field that is missing in a device payload.

  Extends Instance Validator's UndefinedField class.

  Attributes:
    std_field_name: Standard field name.
    entity_guid: Parent entity GUID.
    reporting_entity_guid: Parent reporting entity GUID.
    reporting_entity_field_name: Translation field name.
    metadata: Contextual metadata coming from a physical device. e.g. {
        location: 'fake-location-string',
        control_programs: ['control 1', 'control 2'],
        name: 'fake name',
        object_name: 'fake_object_name' }
  """

  def __init__(
      self,
      std_field_name: str,
      entity_guid: str,
      reporting_entity_guid: Optional[str] = None,
      reporting_entity_field_name: Optional[str] = None,
      metadata: Optional[Dict[str, str]] = None,
  ):
    """Init.

    Args:
      std_field_name: Standard field name.
      entity_guid: Parent entity GUID.
      reporting_entity_guid: [Optional] Parent reporting entity GUID.
      reporting_entity_field_name: [Optional] Translation field name.
      metadata: [Optional] Contextual metadata coming from a physical device.
    """
    super().__init__(std_field_name=std_field_name)
    self.reporting_entity_field_name = reporting_entity_field_name
    self.reporting_entity_guid = reporting_entity_guid
    self.entity_guid = entity_guid
    self.metadata = metadata
    self.guid_to_entity_map = GuidToEntityMap()

  @classmethod
  def FromDict(cls, missing_field_dict: Dict[str, str]):
    missing_field_instance = cls(
        std_field_name=missing_field_dict[STANDARD_FIELD_NAME],
        reporting_entity_field_name=missing_field_dict[
            REPORTING_ENTITY_FIELD_NAME
        ],
        entity_guid=missing_field_dict[BC_GUID],
        reporting_entity_guid=missing_field_dict[REPORTING_ENTITY_GUID],
    )
    missing_field_instance.metadata = {
        k[len(METADATA) + 1 :]: v
        for k, v in missing_field_dict.items()
        if k[: len(METADATA)] == METADATA
    }
    return missing_field_instance

  def GetSpreadsheetRowMapping(self) -> Dict[str, str]:
    """Returns a dictionary of spreadsheet headers to MissingField attributes."""
    missing_field_row_map = {
        STANDARD_FIELD_NAME: self.std_field_name,
        RAW_FIELD_NAME: '',
        REPORTING_ENTITY_FIELD_NAME: self.reporting_entity_field_name,
        ENTITY_CODE: self.guid_to_entity_map.GetEntityCodeByGuid(
            self.entity_guid
        ),
        BC_GUID: self.entity_guid,
        REPORTING_ENTITY_CODE: self.guid_to_entity_map.GetEntityCodeByGuid(
            self.reporting_entity_guid
        ),
        REPORTING_ENTITY_GUID: self.reporting_entity_guid,
        MISSING: MISSING_TRUE,
    }
    return missing_field_row_map


class MultistateValueField(field_translation.DefinedField):
  """A class to store information on a multi-state field.

  Extends Instance Validator's Definedfield class.

  Attributes:
    states: A list of State instances associated with a MultiStateValueField
      instance.
  """

  def __init__(
      self,
      std_field_name: str,
      raw_field_name: str,
      entity_guid: str,
      reporting_entity_guid: Optional[str] = None,
      reporting_entity_field_name: Optional[str] = None,
      metadata: Optional[Dict[str, str]] = None,
  ):
    """Init.

    Args:
      std_field_name: Standard field name.
      raw_field_name: Raw data point name. e.g.
        `points.run_command.present_value`
      entity_guid: Parent entity GUID.
      reporting_entity_guid: [Optional] Parent reporting entity GUID.
      reporting_entity_field_name: [Optional] Translation field name.
      metadata: [Optional] Contextual metadata coming from a physical device.
    """
    super().__init__(
        std_field_name=std_field_name, raw_field_name=raw_field_name
    )
    self.entity_guid = entity_guid
    self.reporting_entity_guid = reporting_entity_guid
    self.reporting_entity_field_name = reporting_entity_field_name
    self.metadata = metadata
    self._states = []
    self.guid_to_entity_map = GuidToEntityMap()

  def __eq__(self, other: ...) -> bool:
    if not isinstance(other, MultistateValueField):
      raise TypeError(f'{str(other)} must be an MultistateValueField instance')
    standard_field_name_eq = self.std_field_name == other.std_field_name
    raw_field_name_eq = self.raw_field_name == other.raw_field_name
    entity_guid_eq = self.entity_guid == other.entity_guid
    return standard_field_name_eq and raw_field_name_eq and entity_guid_eq

  def __repr__(self) -> str:
    return f'{self.entity_guid}: {self.std_field_name}'

  @classmethod
  def FromDict(cls, multistate_field_dict: Dict[str, str]):
    """Class method to construct a MultistateValueField instance from a dictionary of device data points by entity field attribute names.

    Args:
      multistate_field_dict: Dictionary mapping field attribute names to values
        from an abel spreadsheet.

    Returns:
      An instance of MultistateValueField class.
    """
    multi_state_value_field_instance = cls(
        std_field_name=multistate_field_dict[STANDARD_FIELD_NAME],
        raw_field_name=multistate_field_dict[RAW_FIELD_NAME],
        reporting_entity_field_name=multistate_field_dict[
            REPORTING_ENTITY_FIELD_NAME
        ],
        entity_guid=multistate_field_dict[BC_GUID],
        reporting_entity_guid=multistate_field_dict[REPORTING_ENTITY_GUID],
    )
    multi_state_value_field_instance.metadata = {
        k[len(METADATA) + 1 :]: v
        for k, v in multistate_field_dict.items()
        if k[: len(METADATA)] == METADATA
    }
    return multi_state_value_field_instance

  @property
  def states(self) -> List[State]:
    """Returns a collection of State instances associated with a MultistateValueField instance."""
    return self._states

  @states.setter
  def states(self, new_states: List[State]) -> None:
    """Sets a collection of State instances associated with a MultistateValueField instance."""
    for new_state in new_states:
      self.AddState(new_state)

  def AddState(self, new_state: State) -> None:
    """Appends a State instance to self.states."""
    if not isinstance(new_state, State):
      raise TypeError(f'{new_state} must be a State instance.')
    self.states.append(new_state)

  def GetSpreadsheetRowMapping(self) -> Dict[str, str]:
    """Returns a dictionary of MultistateValueField attributes by spreadsheet headers."""
    result_dictionary = {
        STANDARD_FIELD_NAME: self.std_field_name,
        RAW_FIELD_NAME: self.raw_field_name,
        REPORTING_ENTITY_FIELD_NAME: self.reporting_entity_field_name,
        ENTITY_CODE: self.guid_to_entity_map.GetEntityCodeByGuid(
            self.entity_guid
        ),
        BC_GUID: self.entity_guid,
        REPORTING_ENTITY_CODE: self.guid_to_entity_map.GetEntityCodeByGuid(
            self.reporting_entity_guid
        ),
        REPORTING_ENTITY_GUID: self.reporting_entity_guid,
        MISSING: MISSING_FALSE,
    }
    return result_dictionary


class DimensionalValueField(field_translation.DefinedField):
  """A class to store information for a dimensional-valued field.

  Extends the Instance Validator's DefinedField class.

  Attributes:
    std_field_name: Standard field name.
    raw_field_name: Raw data point name. e.g. `points.run_command.present_value`
    reporting_entity_guid: [Optional] Parent reporting entity GUID.
    reporting_entity_field_name: [Optional] Translation field name.
    entity_guid: Parent entity GUID.
    units: Units instance containing data point unit path and a mapping of
      standard unit names to raw unit names.
    metadata: Contextual metadata coming from a physical device. e.g. {
        location: 'fake-location-string',
        control_programs: ['control 1', 'control 2'],
        name: 'fake name',
        object_name: 'fake_object_name' }
    guid_to_entity_map: Global mapping of entity guids to Entity instances.
  """

  def __init__(
      self,
      std_field_name: str,
      raw_field_name: str,
      entity_guid: str,
      reporting_entity_guid: Optional[str] = None,
      reporting_entity_field_name: Optional[str] = None,
      metadata: Optional[Dict[str, str]] = None,
  ):
    """Init.

    Args:
      std_field_name: Standard field name.
      raw_field_name: Raw data point name.
      entity_guid: Parent entity GUID for a field.
      reporting_entity_guid: [Optional] Parent reporting entity GUID.
      reporting_entity_field_name: [Optional] Translation field name.
      metadata: [Optional] Contextual metadata coming from a physical device.
    """
    super().__init__(
        std_field_name=std_field_name, raw_field_name=raw_field_name
    )
    self.reporting_entity_field_name = reporting_entity_field_name
    self.reporting_entity_guid = reporting_entity_guid
    self.entity_guid = entity_guid
    self._units = None
    self.metadata = metadata
    self.guid_to_entity_map = GuidToEntityMap()

  def __eq__(self, other: ...) -> bool:
    if not isinstance(other, DimensionalValueField):
      raise TypeError(f'{str(other)} must be an DimensionalValueField instance')
    standard_field_name_eq = self.std_field_name == other.std_field_name
    raw_field_name_eq = self.raw_field_name == other.raw_field_name
    entity_guid_eq = self.entity_guid == other.entity_guid
    unit_eq = self.units == other.units
    return (
        standard_field_name_eq
        and raw_field_name_eq
        and entity_guid_eq
        and unit_eq
    )

  def __repr__(self) -> str:
    return f'{self.entity_guid}: {self.std_field_name}'

  @classmethod
  def FromDict(cls, dimensional_field_dict: Dict[str, str]):
    """Returns DimensionalValueField instance.

    Constructs a DimensionalValueField instance from a map of device data points
    by entity field attribute names.

    Args:
      dimensional_field_dict: Dictionary mapping field attribute names to values
        from an abel spreadsheet.

    Returns:
      An instance of DimensionalValueField class.
    """
    dimensional_value_field_instance = cls(
        std_field_name=dimensional_field_dict[STANDARD_FIELD_NAME],
        raw_field_name=dimensional_field_dict[RAW_FIELD_NAME],
        reporting_entity_field_name=dimensional_field_dict[
            REPORTING_ENTITY_FIELD_NAME
        ],
        entity_guid=dimensional_field_dict[BC_GUID],
        reporting_entity_guid=dimensional_field_dict[REPORTING_ENTITY_GUID],
    )
    # If an entity field in the ABEL spreadsheet is not blank is not no-units
    # then create a Units instance.
    if (
        dimensional_field_dict[STANDARD_UNIT_VALUE]
        and dimensional_field_dict[RAW_UNIT_VALUE]
    ):
      if (
          dimensional_field_dict[STANDARD_UNIT_VALUE] != NO_UNITS
          and dimensional_field_dict[RAW_UNIT_VALUE] != NO_UNITS
      ):
        # Create a Units instance from ABEL spreadsheet values.
        units_from_dict = Units(
            raw_unit_path=dimensional_field_dict[RAW_UNIT_PATH],
            standard_to_raw_unit_map={
                dimensional_field_dict[
                    STANDARD_UNIT_VALUE
                ]: dimensional_field_dict[RAW_UNIT_VALUE]
            },
        )
        dimensional_value_field_instance.units = units_from_dict
    dimensional_value_field_instance.metadata = {
        k[len(METADATA) + 1 :]: v
        for k, v in dimensional_field_dict.items()
        if k[: len(METADATA)] == METADATA
    }
    return dimensional_value_field_instance

  @property
  def units(self) -> Units:
    """Returns Units instance associated with self."""
    return self._units

  @units.setter
  def units(self, new_units: Units) -> None:
    """Sets self.units."""
    if not isinstance(new_units, Units):
      raise TypeError(f'{new_units} must be a Units instance.')
    elif self._units is not None:
      raise ValueError(
          f'Units have already been set for {self.std_field_name} and cannot'
          ' be overwritten'
      )
    else:
      self._units = new_units

  def GetSpreadsheetRowMapping(self) -> Dict[str, str]:
    """Returns a dictionary of DimensionalValueField attributes by spreadsheet headers."""
    result_dictionary = {
        STANDARD_FIELD_NAME: self.std_field_name,
        RAW_FIELD_NAME: self.raw_field_name,
        REPORTING_ENTITY_FIELD_NAME: self.reporting_entity_field_name,
        ENTITY_CODE: self.guid_to_entity_map.GetEntityCodeByGuid(
            self.entity_guid
        ),
        BC_GUID: self.entity_guid,
        REPORTING_ENTITY_CODE: self.guid_to_entity_map.GetEntityCodeByGuid(
            self.reporting_entity_guid
        ),
        REPORTING_ENTITY_GUID: self.reporting_entity_guid,
        MISSING: MISSING_FALSE,
    }
    if self.units:
      result_dictionary.update(self.units.GetSpreadsheetRowMapping())
    return result_dictionary
