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
from typing import NamedTuple

from yamlformat.validator import base_lib
from yamlformat.validator import config_folder_lib
from yamlformat.validator import findings_lib

UNIT_NAME_VALIDATOR = re.compile(r'^[a-z]+(_[a-z]+)*$')

STANDARD_UNIT_TAG = 'STANDARD'


_MeasurementAlias = NamedTuple('MeasurementAlias',
                               [('alias_name', str), ('base_name', str),
                                ('file_context', findings_lib.FileContext)])


class UnitUniverse(findings_lib.FindingsUniverse):
  """Helper class to represent the defined universe of units."""

  def _GetNamespaceMapValue(self, namespace):
    """Helper method for FindingsUniverse._MakeNamespaceMap.

    Used to create a map from namespace names to namespaces.

    Args:
      namespace: UnitNamespace

    Returns:
      The namespace.
    """
    return namespace

  def GetUnitsForMeasurement(self, measurement_type, namespace_name=''):
    """Returns the collection of units that are defined for the given measurement type as a dictionary from unit names to Unit objects, or None if there are no units for that measurement type.

    Args:
      measurement_type: Name of the measurement subfield.
      namespace_name: Name of the namespace.
    """
    return self._namespace_map[namespace_name].GetUnitsForMeasurement(
        measurement_type)

  def GetMeasurementTypes(self, namespace_name=''):
    """Returns the list of measurement type names that have units defined in the namespace.

    Args:
      namespace_name: Name of the namespace.
    """
    return self._namespace_map[namespace_name].GetMeasurementTypes()


class UnitFolder(config_folder_lib.ConfigFolder):
  """Class representing a folder of Units.

  Class contains all the context information and methods to validate units.

  Attributes:
    local_namespace: object representing the contents of the local namespace
    parent_namespace: object representing the contents of the global namespace
  """

  def __init__(self, folderpath, parent_namespace=None, local_subfields=None):
    """Init.

    Args:
      folderpath: required string with full path to the folder containing units.
        Path should be relative to google3/ and have no leading or trailing /.
      parent_namespace: object containing global namepsace information. When
        working in the global namespace folder, this should be None.
      local_subfields: required map of subfield keys to Subfields for the local
        namespace.
    """
    super(UnitFolder, self).__init__(folderpath, base_lib.ComponentType.UNIT)
    self.local_namespace = UnitNamespace(self._namespace_name, parent_namespace,
                                         local_subfields)
    self.parent_namespace = parent_namespace

  def AddUnit(self, measurement_type, unit):
    """Validates a unit and adds it to the correct namespace.

    Findings will be added to the UnitFolder if validation finds any problems.
    Use AddFromConfig for validation of input file. The unit will not be added
    if validation fails.

    Args:
      measurement_type: Name of the measurement subfield.
      unit: Unit object to add.
    """
    if not unit.IsValid():
      self.AddFindings(unit.GetFindings())
      return
    self.local_namespace.InsertUnit(measurement_type, unit)

  def _AddFromConfigHelper(self, document, context):
    """Helper method that reads a single yaml document and adds all units found.

    Args:
      document: yaml document
      context: config file context
    """
    for measurement in document:
      standard_tag_count = 0
      content = document[measurement]
      if isinstance(content, str):
        self.local_namespace.InsertMeasurementAlias(
            _MeasurementAlias(measurement, content, context))
      else:
        for unit in content:
          is_standard = False
          unit_name = ''
          if isinstance(unit, dict):
            if len(unit) == 1:
              unit_name, tag = next(iter(unit.items()))
            else:
              unit_name = next(iter(unit), '(Blank)')
              self.AddFinding(
                  findings_lib.InvalidUnitFormatError(unit_name, context))
              continue
            if tag == STANDARD_UNIT_TAG:
              is_standard = True
              standard_tag_count += 1
            else:
              self.AddFinding(
                  findings_lib.UnknownUnitTagError(unit_name, tag, context))
          else:
            unit_name = unit
          self.AddUnit(measurement, Unit(unit_name, is_standard, context))
        if standard_tag_count != 1:
          self.AddFinding(
              findings_lib.StandardUnitCountError(measurement,
                                                  standard_tag_count, context))
    self.local_namespace.ResolveMeasurementAliases()


class UnitNamespace(findings_lib.Findings):
  """Class representing a namespace of units.

  Attributes:
    namespace: string name of this namespace.
    parent_namespace: global UnitNamespace, or None if this is the global
      namespace.
    subfields: map of subfield names to Subfields defined in this namespace.
    units: a map from namespace-unique unit identifiers to Unit objects defined
      in this namespace.
  """

  def __init__(self, namespace, parent_namespace=None, subfields=None):
    """Init.

    Args:
      namespace: required string representing the name of the namespace.
      parent_namespace: global UnitNamespace, or None if this is the global
        namespace.
      subfields: optional map of subfield names to Subfields. No validation of
        subfields will be performed if this is None.
    """
    super(UnitNamespace, self).__init__()
    self.namespace = namespace
    self.parent_namespace = parent_namespace
    self.subfields = subfields
    self.units = {}
    self._units_by_name = {}
    self._units_by_measurement = {}
    self._measurement_aliases = {}

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

  def ValidateMeasurementType(self, measurement_type, unit):
    """Validates that the unit corresponds to a measurement type subfield.

    Subfields defined in either the local namespace or global namespace are
    valid. If a match is not found, a finding is added to the unit.

    Args:
      measurement_type: Name of the measurement subfield.
      unit: Unit object to validate.
    """
    pns = self.parent_namespace
    if (not self.SubfieldsAreDefined() or
        (pns and not pns.SubfieldsAreDefined())):
      # If subfields are undefined on any relevant namespace, proper validation
      # is impossible. An empty subfield list counts as being defined.
      return
    if (measurement_type not in self.subfields and
        (pns is None or measurement_type not in pns.subfields)):
      unit.AddFinding(
          findings_lib.UnknownMeasurementTypeError(unit, measurement_type))

  def InsertUnit(self, measurement_type, unit):
    """Inserts a unit into this namespace.

    If the unit already exists in the global namespace, adds a
    DuplicateUnitDefinitionError to the findings and the duplicate is not
    inserted. If the unit is being inserted into a namespace other than the
    global namespace, an InvalidUnitNamespaceError will be added to findings.

    Args:
      measurement_type: Name of the measurement subfield.
      unit: unit object to attempt to insert.
    """
    if unit.name != 'no_units' and unit.name in self._units_by_name:
      self.AddFinding(
          findings_lib.DuplicateUnitDefinitionError(
              self, unit, self._units_by_name[unit.name].file_context))
      return
    # Assert namespace is global namespace otherwise add finding.
    elif self.parent_namespace is not None:
      self.AddFinding(
          findings_lib.InvalidUnitNamespaceError(
              self.namespace, unit.file_context))
    self._InsertEffectiveUnit(measurement_type, unit)

  def _InsertEffectiveUnit(self, measurement_type, unit):
    """Inserts a unit into this namespace.

    Does not check for uniqueness
    within the namespace.

    If the unit already exists in the measurement, adds a
    DuplicateUnitDefinitionError to the findings and the duplicate is not
    inserted.

    Args:
      measurement_type: Name of the measurement subfield.
      unit: unit object to attempt to insert.
    """
    self.ValidateMeasurementType(measurement_type, unit)
    measurement_units = self._units_by_measurement.setdefault(
        measurement_type, {})
    if unit.name in measurement_units:
      self.AddFinding(
          findings_lib.DuplicateUnitDefinitionError(
              self, unit, measurement_units[unit.name].file_context))
      return
    measurement_units[unit.name] = unit
    self._units_by_name[unit.name] = unit
    # unit_key is an opaque ID that is unique within the namespace. It is only
    # used by the backward compatibility checking, which needs all of the units
    # to be in a single dict.
    unit_key = '{0}-{1}'.format(measurement_type, unit.name)
    self.units[unit_key] = unit

  def InsertMeasurementAlias(self, alias):
    """Inserts a measurement alias into this namespace.

    If the alias already exists in the namespace, adds a
    DuplicateMeasurementAliasError to the findings and the duplicate is not
    inserted.

    Args:
      alias: _MeasurementAlias object to insert.
    """
    if alias.alias_name in self._measurement_aliases:
      prev_instance = self._measurement_aliases[alias.alias_name]
      self.AddFinding(
          findings_lib.DuplicateMeasurementAliasError(
              self, alias, prev_instance.file_context))
      return
    self._measurement_aliases[alias.alias_name] = alias

  def ResolveMeasurementAliases(self):
    """Validates all measurement alias references and populates the collections of units for all aliased measurement types."""
    for alias in self._measurement_aliases.values():
      if alias.base_name in self._measurement_aliases:
        self.AddFinding(findings_lib.MeasurementAliasIsAliasedError(alias))
      elif alias.base_name not in self._units_by_measurement:
        self.AddFinding(
            findings_lib.UnrecognizedMeasurementAliasBaseError(alias))
      else:
        for unit in self._units_by_measurement[alias.base_name].values():
          self._InsertEffectiveUnit(alias.alias_name, unit)

  def GetUnitsForMeasurement(self, measurement_type):
    """Returns the collection of units that are defined for the given measurement type as a dictionary from unit names to Unit objects, or None if there are no units for that measurement type.

    Args:
      measurement_type: Name of the measurement subfield.
    """
    return self._units_by_measurement.get(measurement_type)

  def GetMeasurementTypes(self):
    """Returns the list of measurement type names that have units defined in the namespace."""
    return self._units_by_measurement.keys()


class Unit(findings_lib.Findings):
  """Namespace-unaware class representing an individual unit definition.

  Attributes:
    name: the full name (without namespace) of this unit
    is_standard: whether this is the standard unit for the measurement type
    file_context: the config file context for where this unit was defined
  """

  def __init__(self, name, is_standard=False, file_context=None):
    """Init.

    Args:
      name: required string name for the unit
      is_standard: whether this is the standard unit for the measurement type
      file_context: optional object with the config file location of this unit.

    Returns:
      Instance of Unit class.
    """
    super(Unit, self).__init__()
    self.name = name
    self.is_standard = is_standard
    self.file_context = file_context

    if not isinstance(name, str):
      self.AddFinding(findings_lib.IllegalKeyTypeError(name, file_context))
    elif not UNIT_NAME_VALIDATOR.match(name):
      self.AddFinding(findings_lib.InvalidUnitNameError(name, file_context))

  def __eq__(self, other):
    if isinstance(other, Unit):
      return (self.name == other.name and
              self.is_standard == other.is_standard)
    return False

  def __ne__(self, other):
    return not self.__eq__(other)

  __hash__ = None
