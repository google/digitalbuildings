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
from model.constants import DATA_TYPE
from model.constants import DEVICE_ID
from model.constants import LINKED_ENTITY_GUID
from model.constants import METADATA
from model.constants import RAW_FIELD_NAME
from model.constants import RAW_UNIT_PATH
from model.constants import RAW_UNIT_VALUE
from model.constants import STANDARD_FIELD_NAME
from model.constants import STANDARD_UNIT_VALUE
from model.state import State
from model.units import Units


# TODO(b/229631364) Extend to telemetry field and metadata field classes
class EntityField(object):
  """A class to store information on an entity field.

  Attributes:
    standard_field_name: A field's standardized name.
    raw_field_name: A field's raw data point value.
    linked_entity_guid: Not None if field is linked to a virtual entity.
    is_telemetry: Boolean marking if this field outputs telemetry data or
      metadata.
    entity_guid: Parent entity GUID for a field.
    units: Units instance containing data point unit path and a mapping of
        standard unit names to raw unit names.
    data_type: Denotes whether the data is formatted in UDMI, bitbox,
        or other.
    states: A list of State instances associate with an EntityField.
    device_id: Physical device id for this field's device.
    metadata: Contextual metadata coming from a physical device. i.e.
      {
        location: '/Sif-Solo/Site 1 - Sif/Charleston Road North/B13 - 1875
          Charleston/Roof',
        control_programs: ['Trane AC-1', '1875 Charleston'],
        name: 'Duct Static Pressure',
        object_name: 'stat_press_1'
      }

  NOTE: Only units or states can be set. If both or neither are set, then the
  EntityField instance will be considered invalid and model instantiation will
  fail.
  """

  def __init__(self,
               standard_field_name: str,
               raw_field_name: str,
               data_type: bool,
               entity_guid: str,
               linked_entity_guid: Optional[str] = None,
               device_id: Optional[str] = None,
               metadata: Optional[Dict[str, str]] = None):
    """Init.

    Args:
      standard_field_name: Standardized name of the field.
      raw_field_name: A field's raw data point value.
      data_type: This field is a telemetry or metadata data point.
      entity_guid: Parent entity GUID for a field.
      linked_entity_guid: [Optional] if field is linked to a virtual entity.
      device_id: [Optional] physical device id for device containing this data
        point.
      metadata: [Optional] Contextual metadata coming from a physical device.
    """
    self.standard_field_name = standard_field_name
    self.raw_field_name = raw_field_name
    self.linked_entity_guid = linked_entity_guid
    self.data_type = data_type
    self.entity_guid = entity_guid
    self._states = []
    self._units = None
    self.device_id = device_id
    self.metadata = metadata

  def __eq__(self, other: ...) -> bool:
    if not isinstance(other, EntityField):
      raise TypeError(f'{str(other)} must be an EntityField instance')
    standard_field_name_eq = self.standard_field_name == other.standard_field_name
    raw_field_name_eq = self.raw_field_name == other.raw_field_name
    device_id_eq = self.device_id == other.device_id
    return standard_field_name_eq and raw_field_name_eq and device_id_eq

  def __repr__(self) -> str:
    return f'{self.entity_guid}: {self.standard_field_name}'

  @classmethod
  def FromDict(cls, entity_field_dict: Dict[str, str]):
    """class method to create an instance of EntityField from a mapping of concrete model fields to device data points.

    Args:
      entity_field_dict: dictionary mapping field attributes to values from a
        loadsheet.

    Raises:
      AttributeError: If both or neither states and units are set.

    Returns:
      An instance of EntityField class.
    """
    entity_field_instance = cls(
        standard_field_name=entity_field_dict[STANDARD_FIELD_NAME],
        raw_field_name=entity_field_dict[RAW_FIELD_NAME],
        entity_guid=entity_field_dict[BC_GUID],
        linked_entity_guid=entity_field_dict[LINKED_ENTITY_GUID],
        data_type=entity_field_dict[DATA_TYPE],
        device_id=entity_field_dict[DEVICE_ID])
    if entity_field_dict[STANDARD_UNIT_VALUE] and entity_field_dict[
        RAW_UNIT_VALUE]:
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
    """Returns the a collection of state instances associated with self."""
    return self._states

  @states.setter
  def states(self, new_states: List[State]) -> None:
    """Checks that self does not have associated units and sets."""
    if self.units:
      raise AttributeError(
          f'{self.raw_field_name} already has associated units')
    for new_state in new_states:
      self.AddState(new_state)

  @property
  def units(self) -> Units:
    """Returns Units instance associated with self."""
    return self._units

  @units.setter
  def units(self, new_units: Units) -> None:
    """Checks that self does not already have an associated state and sets."""
    if self.states:
      raise AttributeError(
          f'{self.raw_field_name} already has associated states.')
    self._units = new_units

  def AddState(self, new_state: State) -> None:
    """Appends a State instance to self.states."""
    if not isinstance(new_state, State):
      raise TypeError(f'{new_state} must a State instance.')
    self.states.append(new_state)
