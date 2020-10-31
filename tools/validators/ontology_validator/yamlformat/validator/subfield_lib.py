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

"""Classes and methods for working with Carson Subfields."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import re



import enum

from yamlformat.validator import base_lib
from yamlformat.validator import config_folder_lib
from yamlformat.validator import findings_lib

_SUBFIELD_NAME_VALIDATOR = re.compile(r'^[a-z]+[a-z0-9]*$')


class SubfieldUniverse(findings_lib.FindingsUniverse):
  """Helper class to represent the defined universe of subfields.

  Only contains valid subfields.
  """

  def _GetNamespaceMapValue(self, namespace):
    """Helper method by FindingsUniverse._MakeNamespaceMap.

    Used to create a map from namespace names to subfield maps.

    Args:
      namespace: SubfieldNamespace

    Returns:
      The subfield map from the namespace.
    """
    return namespace.subfields

  def GetSubfieldsMap(self, namespace_name):
    """Returns a map from subfield names to Subfield objects in the namespace.

    If there are no defined subfields in the namespace, returns an empty dict.

    Args:
      namespace_name: string.
    """
    return self._namespace_map.get(namespace_name, {})

  def ValidateUnits(self, unit_universe):
    """Checks that all subfields in each folder have units.

    Args:
      unit_universe: UnitUniverse object used to look up units
    """
    for folder in self.folders:
      folder.ValidateUnits(unit_universe)


class SubfieldCategory(enum.Enum):
  AGGREGATION = 1
  DESCRIPTOR = 2
  COMPONENT = 3
  MEASUREMENT_DESCRIPTOR = 4
  MEASUREMENT = 5
  POINT_TYPE = 6


_SUBFIELD_CATEGORY_NAMES = {
    SubfieldCategory.AGGREGATION: 'aggregation',
    SubfieldCategory.COMPONENT: 'component',
    SubfieldCategory.DESCRIPTOR: 'descriptor',
    SubfieldCategory.MEASUREMENT_DESCRIPTOR: 'measurement_descriptor',
    SubfieldCategory.MEASUREMENT: 'measurement',
    SubfieldCategory.POINT_TYPE: 'point_type'
}


class SubfieldFolder(config_folder_lib.ConfigFolder):
  """Class representing a folder of Subfields.

  Class contains all the context information and methods to validate subfields.

  Args:
    folderpath: required string with full path to the subfield folder.
        Path should be relative to google3/ and have no leading or trailing /.

  Attributes:
    local_namespace: object representing the contents of the local namespace

  Returns:
    An instance of the SubfieldFolder class.
  """

  def __init__(self, folderpath):
    super(SubfieldFolder, self).__init__(folderpath,
                                         base_lib.ComponentType.SUBFIELD)
    self.local_namespace = SubfieldNamespace(self._namespace_name)

  def AddSubfield(self, subfield):
    """Adds the subfield object to the namespace, if valid.

    Findings will be added to the SubfieldFolder if validation finds problems.
    Method assumes origin of subfield is correct. Use AddFromConfig for
    validation of input file. The subfield will not be added if validation
    fails.

    Args:
      subfield: subfield to add.
    """
    if not subfield.IsValid():
      self.AddFindings(subfield.GetFindings())
      return
    self.local_namespace.InsertSubfield(subfield)

  def _AddFromConfigHelper(self, document, context):
    """Helper method that reads a single yaml document and adds all subfields found.

    Also adds any findings to the subfield.

    Args:
      document: yaml document
      context: config file context
    """
    for category in SubfieldCategory:
      category_name = _SUBFIELD_CATEGORY_NAMES[category]
      if category_name not in document:
        continue
      # TODO(berkoben): Add warnings for unrecognized fields

      subfield_map = document[category_name]
      if not subfield_map:
        self.AddFinding(findings_lib.EmptyBlockWarning(document, context))
        continue

      for subfield_name in subfield_map:
        # TODO(berkoben): Add handling for tagged measurement types
        description = subfield_map[subfield_name]
        self.AddSubfield(
            Subfield(subfield_name, category, description, context))

  def ValidateUnits(self, unit_universe):
    """Checks that all subfields in the folder's namespace have units.

    Args:
      unit_universe: UnitUniverse object used to look up units
    """
    self.local_namespace.ValidateUnits(unit_universe)


class SubfieldNamespace(findings_lib.Findings):
  """Class representing a namespace of subfields.

  Args:
    namespace: required string representing the name of the namespace.
  Attributes:
    subfields: a dictionary of subfield strings to subfield objects defined in
      this namespace.
    namespace: string name of this namespace

  Returns:
    An instance of the SubfieldNamespace class.
  """

  def __init__(self, namespace):
    super(SubfieldNamespace, self).__init__()
    self.namespace = namespace
    self.subfields = {}
    # maps lowered subfield name to literal one
    self._subfields_lower = {}

  def _GetDynamicFindings(self, filter_old_warnings):
    findings = []
    for subfield in self.subfields.values():
      findings += subfield.GetFindings(filter_old_warnings)
    return findings

  def _PutIfAbsent(self, subfield):
    lower_name = subfield.name.lower()
    if lower_name in self._subfields_lower:
      return self.subfields[self._subfields_lower[lower_name]]
    self._subfields_lower[lower_name] = subfield.name
    self.subfields[subfield.name] = subfield
    return None

  def InsertSubfield(self, subfield):
    """Inserts a subfield into this namespace.

    If the subfield already exists in the namespace, adds a
    DuplicateSubfieldDefinitionError to the findings and the duplicate is not
    inserted.

    Args:
      subfield: subfield object to attempt to insert.
    """
    # TODO(berkoben): Handle detection of duplicates within a category
    # (Currently yaml load automatically suppresses these duplicates)
    old_subfield = self._PutIfAbsent(subfield)
    if old_subfield is not None:
      self.AddFinding(
          findings_lib.DuplicateSubfieldDefinitionError(subfield,
                                                        self.namespace))

  def ValidateUnits(self, unit_universe):
    """Checks that all subfields in this namespace have corresponding units.

    The units for the subfield must be in the same namespace, not a parent
    namespace. If any subfield does not have units, adds a MissingUnitError
    to the findings.

    Args:
      unit_universe: UnitUniverse object used to look up units
    """
    unit_measurement_types = {
        unit.measurement_type
        for unit in unit_universe.GetUnitsMap(self.namespace).values()
    }
    for subfield in self.subfields.values():
      if (subfield.category == SubfieldCategory.MEASUREMENT and
          subfield.name not in unit_measurement_types):
        self.AddFinding(findings_lib.MissingUnitError(subfield))


class Subfield(findings_lib.Findings):
  """Namespace-unaware class representing an individual subfield definition.

  Args:
    name: required string representing the subfield.
    category: required SubfieldCategory value representing the subfield type.
    description: optional (for now) string semantic definition for the subfield.
    context: optional object with the config file location of this subfield.

  Attributes:
    context: the config file context for where this subfield was defined
    name: the full name (without namespace) of this subfield
    description: explanation of what this subfield represents
    category: the category of this subfield from SubfieldCategory enum

  Returns:
    An instance of the Subfield class.
  """

  def __init__(self, name, category, description=None, context=None):
    super(Subfield, self).__init__()
    self.context = context
    self.name = name
    self.description = description
    self.category = category

    if not isinstance(name, str):
      self.AddFinding(findings_lib.IllegalKeyTypeError(name, context))
    elif not _SUBFIELD_NAME_VALIDATOR.match(name):
      self.AddFinding(
          findings_lib.IllegalCharacterError(name, context))
    if not self.description:
      self.AddFinding(
          findings_lib.MissingSubfieldDescriptionWarning(
              self.name, self.context))

  def __eq__(self, other):
    if isinstance(other, Subfield):
      return (self.name == other.name and self.category == other.category and
              self.description == other.description)
    return False

  def __ne__(self, other):
    return not self.__eq__(other)

  __hash__ = None
