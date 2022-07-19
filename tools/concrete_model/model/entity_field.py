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

from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import BC_GUID
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import ENTITY_CODE
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import METADATA
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import NO_UNITS
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import RAW_FIELD_NAME
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import RAW_UNIT_PATH
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import RAW_UNIT_VALUE
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import REPORTING_ENTITY_CODE
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import REPORTING_ENTITY_FIELD_NAME
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import REPORTING_ENTITY_GUID
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import STANDARD_FIELD_NAME
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import STANDARD_UNIT_VALUE
from google3.third_party.digitalbuildings.tools.concrete_model.model.guid_to_entity_map import GuidToEntityMap
from google3.third_party.digitalbuildings.tools.concrete_model.model.state import State
from google3.third_party.digitalbuildings.tools.concrete_model.model.units import Units


# TODO(b/229631364) Extend to telemetry field and metadata field classes
class EntityField(object):
  """A class to store information on an entity field.

  Attributes:
    standard_field_name: A field's standardized name.
    raw_field_name: A field's raw data point value.
    reporting_entity_field_name: Enumerated standard field name for fields that
      map to a passthrough reporting entity.
    reporting_entity_guid: Not None if field is linked to a virtual entity.
    entity_guid: Parent entity GUID for a field.
    units: Units instance containing data point unit path and a mapping of
      standard unit names to raw unit names.
    states: A list of State instances associate with an EntityField.
    device_id: Physical device id for this field's device.
    metadata: Contextual metadata coming from a physical device. e.g. {
        location: '/Sif-Solo/Site 1 - Sif/Charleston Road North/B13 - 1875
          Charleston/Roof',
        control_programs: ['Trane AC-1', '1875 Charleston'],
        name: 'Duct Static Pressure',
        object_name: 'stat_press_1' }
    guid_to_entity_map: Global mapping of entity guids to Entity instances.
  NOTE: Only units or states can be set. If both are set, then the EntityField
    instance will raise an Attribute Error.
  """

  def __init__(self,
               standard_field_name: str,
               raw_field_name: str,
               entity_guid: str,
               reporting_entity_guid: Optional[str] = None,
               reporting_entity_field_name: Optional[str] = None,
               metadata: Optional[Dict[str, str]] = None):
    """Init.

    Args:
      standard_field_name: Standardized name of the field.
      raw_field_name: A field's raw data point value.
      entity_guid: Parent entity GUID for a field.
      reporting_entity_guid: [Optional] guid of the reporting entity the field
        is translated on.
      reporting_entity_field_name: Enumerated standard field name for fields
        that map to a passthrough reporting entity.
      metadata: [Optional] Contextual metadata coming from a physical device.
    """
    self.standard_field_name = standard_field_name
    self.raw_field_name = raw_field_name
    self.reporting_entity_field_name = reporting_entity_field_name
    self.reporting_entity_guid = reporting_entity_guid
    self.entity_guid = entity_guid
    self._states = []
    self._units = None
    self.metadata = metadata
    self.guid_to_entity_map = GuidToEntityMap()

  def __eq__(self, other: ...) -> bool:
    if not isinstance(other, EntityField):
      raise TypeError(f'{str(other)} must be an EntityField instance')
    standard_field_name_eq = self.standard_field_name == other.standard_field_name
    raw_field_name_eq = self.raw_field_name == other.raw_field_name
    entity_guid_eq = self.entity_guid == other.entity_guid
    return standard_field_name_eq and raw_field_name_eq and entity_guid_eq

  def __repr__(self) -> str:
    return f'{self.entity_guid}: {self.standard_field_name}'

  @classmethod
  def FromDict(cls, entity_field_dict: Dict[str, str]):
    """Class method to construct an EntityField from a dictionary of device data points by entity field attribute names.

    Args:
      entity_field_dict: Dictionary mapping field attribute names to values from
        a concrete model spreadsheet.

    Raises:
      AttributeError: If both or neither states and units are set.

    Returns:
      An instance of EntityField class.
    """
    entity_field_instance = cls(
        standard_field_name=entity_field_dict[STANDARD_FIELD_NAME],
        raw_field_name=entity_field_dict[RAW_FIELD_NAME],
        reporting_entity_field_name=entity_field_dict[
            REPORTING_ENTITY_FIELD_NAME],
        entity_guid=entity_field_dict[BC_GUID],
        reporting_entity_guid=entity_field_dict[REPORTING_ENTITY_GUID])
    if entity_field_dict[STANDARD_UNIT_VALUE] and entity_field_dict[
        RAW_UNIT_VALUE]:
      if entity_field_dict[
          STANDARD_UNIT_VALUE] != NO_UNITS and entity_field_dict[
              RAW_UNIT_VALUE] != NO_UNITS:
        units_from_dict = Units(
            raw_unit_path=entity_field_dict[RAW_UNIT_PATH],
            standard_to_raw_unit_map={
                entity_field_dict[STANDARD_UNIT_VALUE]:
                    entity_field_dict[RAW_UNIT_VALUE]
            })
        entity_field_instance.units = units_from_dict
    entity_field_instance.metadata = {
        k[len(METADATA) + 1:]: v
        for k, v in entity_field_dict.items()
        if k[:len(METADATA)] == METADATA
    }
    return entity_field_instance

  @property
  def states(self) -> List[State]:
    """Returns the a collection of State instances associated with self."""
    return self._states

  @states.setter
  def states(self, new_states: List[State]) -> None:
    """Checks that self does not have associated units and sets."""
    if self.units:
      error_string = f'{self.raw_field_name} already has associated units.'
      error_string += ' A field cannot have both units and states.'
      raise AttributeError(error_string)
    for new_state in new_states:
      self.AddState(new_state)

  @property
  def units(self) -> Units:
    """Returns Units instance associated with self."""
    return self._units

  @units.setter
  def units(self, new_units: Units) -> None:
    """Checks that self does not already have an associated State and sets."""
    if self.states:
      error_string = f'{self.raw_field_name} already has associated states.'
      error_string += ' A field cannot have both units and states.'
      raise AttributeError(error_string)
    self._units = new_units

  def AddState(self, new_state: State) -> None:
    """Appends a State instance to self.states."""
    if not isinstance(new_state, State):
      raise TypeError(f'{new_state} must a State instance.')
    self.states.append(new_state)

  def GetSpreadsheetRowMapping(self) -> Dict[str, str]:
    """Returns a dictionary of EntityField attributes by spreadsheet headers."""
    result_dictionary = {
        STANDARD_FIELD_NAME:
            self.standard_field_name,
        RAW_FIELD_NAME:
            self.raw_field_name,
        REPORTING_ENTITY_FIELD_NAME:
            self.reporting_entity_field_name,
        ENTITY_CODE:
            self.guid_to_entity_map.GetEntityCodeByGuid(self.entity_guid),
        BC_GUID:
            self.entity_guid,
        REPORTING_ENTITY_CODE:
            self.guid_to_entity_map.GetEntityCodeByGuid(
                self.reporting_entity_guid),
        REPORTING_ENTITY_GUID:
            self.reporting_entity_guid
    }
    if self.units:
      result_dictionary.update(self.units.GetSpreadsheetRowMapping())
    return result_dictionary
