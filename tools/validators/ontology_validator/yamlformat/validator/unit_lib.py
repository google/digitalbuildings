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
"""Classes and methods for working with units in the ontology."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import re

from validation.validator import base_lib
from validation.validator import config_folder_lib
from validation.validator import findings_lib

UNIT_NAME_VALIDATOR = re.compile(r'^[a-z]+(_[a-z]+)*$')

STANDARD_UNIT_TAG = 'STANDARD'


class UnitUniverse(findings_lib.FindingsUniverse):
  """Helper class to represent the defined universe of units."""

  def _GetNamespaceMapValue(self, namespace):
    """Helper method for FindingsUniverse._MakeNamespaceMap.

    Used to create a map from namespace names to unit maps.

    Args:
      namespace: UnitNamespace

    Returns:
      The units map from the namespace.
    """
    return namespace.units

  def GetUnitsMap(self, namespace_name):
    """Returns a map from unit names to Unit objects in the namespace.

    If there are no defined units in the namespace, returns an empty dict.

    Args:
      namespace_name: string.
    """
    return self._namespace_map.get(namespace_name, {})


class UnitFolder(config_folder_lib.ConfigFolder):
  """Class representing a folder of Units.

  Class contains all the context information and methods to validate units.

  Args:
    folderpath: required string with full path to the folder containing units.
      Path should be relative to google3/ and have no leading or trailing /.
    parent_namespace:
      object containing global namepsace information. When working in the global
          namespace folder, this should be None.
    local_subfields:
      required map of subfield keys to Subfields for the local namespace.
  Attributes:
    local_namespace: object representing the contents of the local namespace
    parent_namespace: object representing the contents of the global namespace
  """

  def __init__(self, folderpath, parent_namespace=None, local_subfields=None):
    super(UnitFolder, self).__init__(folderpath, base_lib.ComponentType.UNIT)
    self.local_namespace = UnitNamespace(self._namespace_name, parent_namespace,
                                         local_subfields)
    self.parent_namespace = parent_namespace

  def AddUnit(self, unit):
    """Validates a unit and adds it to the correct namespace.

    Findings will be added to the UnitFolder if validation finds any problems.
    Use AddFromConfig for validation of input file. The unit will not be added
    if validation fails.

    Args:
      unit: Unit object to add.
    """
    if not unit.IsValid():
      self.AddFindings(unit.GetFindings())
      return
    self.local_namespace.InsertUnit(unit)

  def _AddFromConfigHelper(self, document, context):
    """Helper method that reads a single yaml document and adds all units found.

    Args:
      document: yaml document
      context: config file context
    """
    for measurement in document:
      standard_tag_count = 0
      units = document[measurement]
      for unit in units:
        is_standard = False
        unit_name = ''
        if isinstance(unit, dict):
          try:
            [(unit_name, tag)] = unit.items()
          except ValueError:
            self.AddFinding(
                findings_lib.InvalidUnitFormatError(document, context))
            continue
          if tag == STANDARD_UNIT_TAG:
            is_standard = True
            standard_tag_count += 1
          else:
            self.AddFinding(
                findings_lib.UnknownUnitTagError(unit_name, tag, context))
        else:
          unit_name = unit
        self.AddUnit(Unit(unit_name, measurement, is_standard, context))
      if standard_tag_count != 1:
        self.AddFinding(
            findings_lib.StandardUnitCountError(measurement, standard_tag_count,
                                                context))


class UnitNamespace(findings_lib.Findings):
  """Class representing a namespace of units.

  Args:
    namespace: required string representing the name of the namespace.
    parent_namespace: global UnitNamespace, or None if this is the
      global namespace.
    subfields: optional map of subfield names to Subfields. No validation
      of subfields will be performed if this is None.
  Attributes:
    namespace: string name of this namespace.
    parent_namespace: global UnitNamespace, or None if this is the
      global namespace.
    subfields: map of subfield names to Subfields defined in this namespace.
    units: a map from unit names to Unit objects defined in this namespace.
  """

  def __init__(self, namespace, parent_namespace=None, subfields=None):
    super(UnitNamespace, self).__init__()
    self.namespace = namespace
    self.parent_namespace = parent_namespace
    self.subfields = subfields
    self.units = {}

  def _GetDynamicFindings(self, filter_old_warnings):
    findings = []
    for unit in self.units.values():
      findings += unit.GetFindings(filter_old_warnings)
    return findings

  def SubfieldsAreDefined(self):
    """Indicates whether subfields are defined.

    Returns:
      True if subfields have been populated for this namespace. Subfields may be
      populated with an empty map and this will still return true.
    """
    return self.subfields is not None

  def ValidateMeasurementType(self, unit):
    """Validates that the unit corresponds to a measurement type subfield.

    Subfields defined in either the local namespace or global namespace are
    valid. If a match is not found, a finding is added to the unit.

    Args:
      unit: Unit object to validate.
    """
    pns = self.parent_namespace
    if (not self.SubfieldsAreDefined() or
        (pns and not pns.SubfieldsAreDefined())):
      # If subfields are undefined on any relevant namespace, proper validation
      # is impossible. An empty subfield list counts as being defined.
      return
    if (unit.measurement_type not in self.subfields and
        (pns is None or unit.measurement_type not in pns.subfields)):
      unit.AddFinding(findings_lib.UnknownMeasurementTypeError(unit))

  def InsertUnit(self, unit):
    """Inserts a unit into this namespace.

    If the unit already exists in the namespace, adds a
    DuplicateUnitDefinitionError to the findings and the duplicate is not
    inserted.

    Args:
      unit: unit object to attempt to insert.
    """
    self.ValidateMeasurementType(unit)
    if unit.name in self.units:
      self.AddFinding(
          findings_lib.DuplicateUnitDefinitionError(unit, self.namespace))
      return
    self.units[unit.name] = unit


class Unit(findings_lib.Findings):
  """Namespace-unaware class representing an individual unit definition.

  Args:
    name: required string name for the unit
    measurement_type: required string indicating the unit measurement type
    is_standard: whether this is the standard unit for the measurement type
    context: optional object with the config file location of this unit.
  Attributes:
    name: the full name (without namespace) of this unit
    measurement_type: the unit measurement type
    is_standard: whether this is the standard unit for the measurement type
    context: the config file context for where this unit was defined
  """

  def __init__(self, name, measurement_type, is_standard=False, context=None):
    super(Unit, self).__init__()
    self.name = name
    self.measurement_type = measurement_type
    self.is_standard = is_standard
    self.context = context

    if not isinstance(name, str):
      self.AddFinding(findings_lib.IllegalKeyTypeError(name, context))
    elif not UNIT_NAME_VALIDATOR.match(name):
      self.AddFinding(findings_lib.IllegalCharacterError(name, context))

  def __eq__(self, other):
    if isinstance(other, Unit):
      return (self.name == other.name and
              self.measurement_type == other.measurement_type and
              self.is_standard == other.is_standard)
    return False

  def __ne__(self, other):
    return not self.__eq__(other)

  __hash__ = None
