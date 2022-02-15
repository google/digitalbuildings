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

"""Module to hold entity field class and helper classes."""
from typing import Dict, Optional

from model.model_utils import TelemetryFormat
from model.states import States
from model.units import Units


class EntityField(object):
  """A class to store information on an entity field.

  Attributes:
    standard_field_name: A field's DBO standard field name.
    raw_field_name: A fields raw name coming from a reporting device.
    is_telemetry: boolean marking if this field outputs telemetry data or
      metadata.
    telemetry_format: Denotes whether the data is formatted in UDMI, bitbox,
        or other.
    states: States instance containing a mapping of standard state names to raw
      state values.
    units: A mapping from device unit path to a mapping of standard unit names
      to raw unit names.
    device_id: physical device id for the field.
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
               is_telemetry: bool,
               telemetry_format: TelemetryFormat,
               states: Optional[States] = None,
               units: Optional[Units] = None,
               device_id: Optional[str] = None,
               metadata: Optional[Dict[str, str]] = None) -> None:
    """Init.

    Args:
      standard_field_name: Standard name of the field.
      raw_field_name: A field's raw field name
      is_telemetry: differentiates between whether this field is a telemetry or
        metadata field.
      telemetry_format: Denotes whether the data is formatted in UDMI, bitbox,
        or other.
      states: [Optional] States instance containing a mapping of standard state
        names to raw state values.
      units: [Optional] A mapping from device unit path to a mapping of standard
        unit names to raw unit names.
      device_id: [Optional] physical device id for the field.
      metadata: [Optional] Contextual metadata coming from a physical device.
    """
    self.standard_field_name = standard_field_name
    self.raw_field_name = raw_field_name
    self.is_telemetry = is_telemetry
    self._states = states
    self._telemetry_format = telemetry_format
    self._units = units
    self.device_id = device_id
    self.metadata = metadata

  @classmethod
  def FromDict(cls, entity_field_dict: Dict[str, str]):
    """class method to create an instance of EntityField from a mapping of concrete model fields to device data.

    Args:
      entity_field_dict: dictionary mapping field attributes to values from a
        loadsheet.

    Returns:
      An instance of EntityField class.
    """

  @property
  def telemetry_format(self) -> TelemetryFormat:
    """Returns telemetry format as an enum.Enum instance."""
    return self._telemetry_format

  @telemetry_format.setter
  def telemetry_format(self, new_telemetry_format: TelemetryFormat) -> None:
    """Validates new_telemetry_format is an instance of TelemetryFormat and sets."""

  @property
  def states(self) -> States:
    """Returns the instance of States associated with self."""
    return self._states

  @states.setter
  def states(self, new_state: States) -> None:
    """Checks that new_state is a valid instance of States class, checks that self does not have associated units and sets."""

  @property
  def units(self) -> Units:
    """Returns unit(s) associated with self."""
    return self._units

  @units.setter
  def units(self, new_units: Units) -> None:
    """Checks that new_units is a valid Units instance, checks that self does not already have an associated state and sets."""
