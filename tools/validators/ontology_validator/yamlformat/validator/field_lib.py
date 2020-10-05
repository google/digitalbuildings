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

"""Classes and methods for working with Carson Fields."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import re

import typing

from yamlformat.validator import base_lib
from yamlformat.validator import config_folder_lib
from yamlformat.validator import findings_lib
from yamlformat.validator import state_lib
from yamlformat.validator import subfield_lib

# We currently are enforcing that fields are lower case only.
FIELD_CHARACTER_REGEX = re.compile(
    r'^[a-z]+[a-z0-9]*(?:_[a-z]+[a-z0-9]*)*$')

# We currently are enforcing that fields are lower case only.
FIELD_ALPHANUMERIC_PATTERN = re.compile('_([0-9]+)')

def SplitFieldName(field):
  """Splits the field name on '/' and returns the parts separately.

  Args:
    field: the possibly fully qualified field name

  Returns:
    tuple with namespace and field name.  Defaults to global for no namespace.
  """

  field_only = field
  namespace = ''
  split = field.split('/')
  if len(split) == 2:
    namespace = split[0]
    field_only = split[1]
  return namespace, field_only


class FieldUniverse(findings_lib.FindingsUniverse):
  """Helper class to represent the defined universe of fields.

  Only contains valid fields.
  """

  def _GetNamespaceMapValue(self, namespace):
    """Helper method for FindingsUniverse._MakeNamespaceMap.

    Used to create a map from namespace names to field name lists.

    Args:
      namespace: FieldNamespace

    Returns:
      A list of field names from the namespace.
    """
    return {field.name for field in namespace.fields.values()}

  def IsFieldDefined(self, fieldname, namespace_name):
    """Returns true if fieldname is defined within namespace.
       If the field ends with a digit, it is removed to check if it exists without it

    Args:
      fieldname: string. Name of a field, with namespace and increment removed.
      namespace_name: string.
    """
    fieldname = re.sub(FIELD_ALPHANUMERIC_PATTERN, '', fieldname)
    return fieldname in self._namespace_map.get(namespace_name, set())

  def GetFieldsMap(self, namespace_name):
    """Returns the fields defined within namespace.

    Args:
      namespace_name: string.
    """
    if self.folders:
      return self.folders[0].local_namespace.fields
  
class FieldFolder(config_folder_lib.ConfigFolder):
  """Class representing a folder of Fields.

  Class contains all the context information and methods to validate and handle
  namespace up-leveling of fields. Fields are up-leveled (pushed up to the
  global namespace) if we can guarantee that they will not conflict with other
  fields defined there.

  Args:
    folderpath: required string with full path to the folder containing fields.
        Path should be relative to google3/ and have no leading or trailing /.
    parent_namespace:
      object containing global namepsace information. When working in the global
          namespace folder, treat it as local and leave this blank.
    local_subfields:
      required map of subfield keys to Subfields for the local namespace.
    local_states:
      required map of state keys to States for the local namespace.

  Attributes:
    local_namespace: object representing the contents of the local namespace
    parent_namespace: object representing the contents of the global namespace

  Returns:
    An instance of the FieldFolder class.
  """

  def __init__(self,
               folderpath,
               parent_namespace=None,
               local_subfields=None,
               local_states=None):
    super().__init__(folderpath, base_lib.ComponentType.FIELD)
    self.local_namespace = FieldNamespace(self._namespace_name, local_subfields,
                                          local_states, parent_namespace)
    self.parent_namespace = parent_namespace

  def AddField(self, field):
    """Attempts to insert a field into a namespace.

    Additional validation will be performed in the context of the namespace.
    The field will not be added if validation fails.

    Use AddFromConfig instead for validation of the YAML input file.

    Args:
      field: Field object to add.
    """
    self.local_namespace.InsertField(field)

  def _AddFromConfigHelper(self, document, context):
    """Helper method that reads a single yaml document and adds all fields found.

    Also adds any findings to the field.

    Args:
      document: yaml document
      context: config file context
    """
    if 'literals' not in document:
      self.AddFinding(findings_lib.UnrecognizedFormatError(document, context))
      return
    field_list = document['literals']
    if field_list is None:
      self.AddFinding(findings_lib.EmptyBlockWarning(document, context))
      return
    for field_spec in field_list:
      field_name = ''
      states = None
      if isinstance(field_spec, dict):
        # If the field has a list of states, field_spec must be a dict with
        # a single entry.
        try:
          [(field_name, states)] = field_spec.items()
        except ValueError:
          self.AddFinding(
              findings_lib.InvalidFieldFormatError(document, context))
          continue
      else:
        field_name = field_spec
      field = Field(field_name, states, context)
      self.AddField(field)


class _FieldValidationStateMachine(object):
  """State machine used to validate the construction of a field from subfields.

  For each field create this class and call ValidateNext() for each successive
  subfield's category.  Call IsFieldComplete() at the end to get a final result.

  Returns:
    An instance of the _FieldValidationStateMachine class.
  """

  def __init__(self):
    self._category_index = 0
    self._instance_count = 0
    self._has_measurement = False
    self._has_required_fields = False

  _POINT_TYPES_NEEDING_MEASUREMENTS = ['setpoint', 'sensor', 'accumulator']

  _CAT_SPEC = typing.NamedTuple(
      'CAT_SPEC', [('cat', str), ('required', bool), ('max', int)])

  # Represents parameters for each subfield category.
  # Subfields are in the array in the order they should appear in the field.
  _CATEGORIES_IN_ORDER = [
      _CAT_SPEC(
          cat=subfield_lib.SubfieldCategory.AGGREGATION,
          required=False,
          max=1),
      _CAT_SPEC(
          cat=subfield_lib.SubfieldCategory.DESCRIPTOR,
          required=False,
          max=10),
      _CAT_SPEC(
          cat=subfield_lib.SubfieldCategory.COMPONENT,
          required=False,
          max=1),
      _CAT_SPEC(
          cat=subfield_lib.SubfieldCategory.MEASUREMENT_DESCRIPTOR,
          required=False,
          max=1),
      _CAT_SPEC(
          cat=subfield_lib.SubfieldCategory.MEASUREMENT,
          required=False,
          max=1),
      _CAT_SPEC(
          cat=subfield_lib.SubfieldCategory.POINT_TYPE,
          required=True,
          max=1)
      ]

  def ValidateNext(self, subfield):
    """Validates if appending a subfield of category can make a valid field.

    Args:
      subfield: the next subfield to add.

    Returns:
      True if adding a field of category meets field naming rules
    """
    category = subfield.category
    while self._category_index < len(self._CATEGORIES_IN_ORDER):
      cat_spec = self._CATEGORIES_IN_ORDER[self._category_index]
      if category == cat_spec.cat:
        if self._instance_count < cat_spec.max:
          self._instance_count += 1
          if category == subfield_lib.SubfieldCategory.MEASUREMENT:
            self._has_measurement = True
          if category == subfield_lib.SubfieldCategory.POINT_TYPE:
            self._has_required_fields = True
            if not self._has_measurement:
              if subfield.name in self._POINT_TYPES_NEEDING_MEASUREMENTS:
                return False
          return True
        else:
          return False
      if cat_spec.required and self._instance_count < 1:
        return False
      self._category_index += 1
      self._instance_count = 0
    return False

  def IsFieldComplete(self):
    """Indcates if the state machine has seen a completed field.

    Returns:
      True if the subfield categories presented represent a complete field.
    """
    return self._has_required_fields


class FieldNamespace(findings_lib.Findings):
  """Class representing a namespace of fields.

  Args:
    namespace: required string representing the name of the namespace. The
      global namespace is represented by the empty string.
    subfields: optional map of subfield names to Subfields. No validation of
      subfields is performed if this is left empty
    states: optional map of state names to States. No validation of states
      is performed if this isn't provided
    parent_namespace: global FieldNamespace object, if this is not it.

  Attributes:
    fields: a dictionary of Field keys to field objects for fields added to
      this namespace.  NB: a field key is a permutation of the field name with
        subfields alpha-ordered (and-de-duped, but fields with dup-fields are
        invalid)
    subfields: a dictionary of subfield strings to Subfield objects defined in
      this namespace.
    states: a map from state names to State objects defined in this namespace
    namespace: string name of this namespace
    parent_namespace: reference to the parent namespace, or None if this is
      the global namespace

  Returns:
    An instance of the FieldNamespace class.
  """

  def __init__(self,
               namespace,
               subfields=None,
               states=None,
               parent_namespace=None):
    super(FieldNamespace, self).__init__()
    self.namespace = namespace
    self.subfields = subfields
    self.states = states
    self.fields = {}
    self.parent_namespace = parent_namespace
    if self.subfields is not None:
      if self.parent_namespace and self.parent_namespace.subfields is None:
        raise RuntimeError(
            'Subfields are defined for the child, but not the parent')

  def _GetDynamicFindings(self, filter_old_warnings):
    findings = []
    for field in self.fields.values():
      findings += field.GetFindings(filter_old_warnings)
    return findings

  def StatesAreDefined(self):
    """Indicates whether states are defined.

    Returns:
      True if states have been populated for this namespace. States may be
      populated with an empty map and this will return true.
    """
    return self.states is not None

  def ValidateStates(self, field):
    """Checks that a list of state values for a multistate field is valid.

    Adds any findings to the field.

    Args:
      field: reference to the Field object for state validation

    Returns:
      True if the field uses any states from the local namespace.
    """
    if field.states is None:
      return False

    pns = self.parent_namespace
    if not self.StatesAreDefined() or (pns and not pns.StatesAreDefined()):
      # If states are undefined on any relevant namespace, proper state
      # validation is impossible. Note that an empty state list is still a
      # defined state list.
      return False

    uses_local_states = False
    for state in field.states:
      if state in self.states:
        uses_local_states = True
      elif pns is None or state not in pns.states:
        if not state_lib.STATE_NAME_VALIDATOR.match(state):
          field.AddFinding(findings_lib.InvalidStateFormatError(state, field))
        else:
          field.AddFinding(findings_lib.MissingStateError(state, field))

    return uses_local_states

  def SubfieldsAreDefined(self):
    """Indicates whether subfields are defined.

    Returns:
      True if subfields have been populated for this namespace. Subfields may be
      populated with an empty map and this will still return true.
    """
    return self.subfields is not None

  def _IsValidConstruction(self, field):
    """Checks if the field has been constructed with properly ordered subfields.

    Args:
      field: the field to validate

    Returns:
      True if the field is constructed properly.
    """
    pns = self.parent_namespace
    construction_validator = _FieldValidationStateMachine()
    for subfield_name in field.subfields:
      if subfield_name in self.subfields:
        subfield = self.subfields[subfield_name]
      elif pns and subfield_name in pns.subfields:
        subfield = pns.subfields[subfield_name]
      if not subfield:
        return False
      if not construction_validator.ValidateNext(subfield):
        return False
    return construction_validator.IsFieldComplete()

  def ValidateSubfields(self, field):
    """Validates that the subfields that compose the field are valid.

    Adds any findings to the field.

    Args:
      field: reference to the Field object for subfield validation

    Returns:
      True if the field uses any subfields from the local namespace.
    """
    pns = self.parent_namespace
    if not self.SubfieldsAreDefined() or (pns is not None and
                                          not pns.SubfieldsAreDefined()):
      # If subfields are undefined on any relevant namespace, proper subfield
      # validation is impossible. Note that an empty subfield list is still a
      # defined subfield list.
      return False

    missing_fields = False
    uses_local_subfields = False
    for subfield in field.subfields:
      if subfield in self.subfields:
        uses_local_subfields = True
      elif pns is None or subfield not in pns.subfields:
        missing_fields = True
        field.AddFinding(findings_lib.MissingSubfieldError(subfield, field))

    if not missing_fields and not self._IsValidConstruction(field):
      field.AddFinding(findings_lib.InvalidFieldConstructionError(field))

    return uses_local_subfields

  def PutIfAbsent(self, field):
    """Puts the field into the field map if its key is absent from the map.

    Args:
      field: field to attempt to insert into the map

    Returns:
      The existing field with a matching key, or None.
    """
    if field.key in self.fields:
      return self.fields[field.key]
    self.fields[field.key] = field
    return None

  def InsertField(self, field):
    """Validates and inserts a field into the appropriate namespace.

    Validates the subfields and states of the field, and checks whether the
    field can be up-leveled to the global namespace. Up-leveling is possible
    if the field does not use any subfields or states specific to the local
    namespace.

    If any validation errors are found, the findings are added to the field
    and the local namespace, and the field will not be inserted.

    Args:
      field: field to attempt to insert.
    """

    # Immediately stop validation if the field is already invalid.
    if not field.IsValid():
      self.AddFindings(field.GetFindings())
      return

    # Validate subfields and states in the namespace context. The field could
    # become invalid after this validation is performed.

    uses_local_subfields = self.ValidateSubfields(field)
    uses_local_states = self.ValidateStates(field)
    if not field.IsValid():
      self.AddFindings(field.GetFindings())
      return
    field_can_uplevel = not (uses_local_subfields or uses_local_states)

    insert_ns = self
    if self.parent_namespace is not None and field_can_uplevel:
      insert_ns = self.parent_namespace
    old_field = insert_ns.PutIfAbsent(field)
    if old_field is not None:
      insert_ns.AddFinding(
          findings_lib.DuplicateFieldDefinitionError(old_field, field))


class Field(findings_lib.Findings):
  """Namespace-unaware class representing an individual field definition.

  Args:
    name: required string representing the field.
    states: optional list of strings representing valid states for a
      multistate field. Should be None for non-multistate fields.
    context: optional object with the config file location of this field.

  Attributes:
    context: the config file context for where this field was defined
    name: the full name (without namespace) of this field
    subfields: a list of subfield keys for this field
    key: a hashable object representing the field's subfield set.
    states: a list of valid states for this field, or None

  Returns:
    An instance of the Field class.
  """

  def __init__(self, name, states=None, context=None):
    super(Field, self).__init__()
    self.context = context
    self.name = name
    self.subfields = []
    self.states = states

    if not isinstance(name, str):
      self.AddFinding(findings_lib.IllegalKeyTypeError(name, context))
    elif not FIELD_CHARACTER_REGEX.match(name):
      self.AddFinding(findings_lib.IllegalCharacterError(name, context))
    else:
      self.InitAndValidateSubfields()
      self.ValidateStates()

  def InitAndValidateSubfields(self):
    subfield_list = self.name.split('_')
    subfield_set = set()
    for subfield in subfield_list:
      if subfield in subfield_set:
        self.AddFinding(findings_lib.DuplicateSubfieldError(subfield, self))
        continue
      subfield_set.add(subfield)
      self.subfields.append(subfield)
    self.key = frozenset(self.subfields)

  def ValidateStates(self):
    if self.states is None:
      return
    unique_states = set()
    for state in self.states:
      if state in unique_states:
        self.AddFinding(findings_lib.DuplicateStateError(state, self))
      else:
        unique_states.add(state)

  def __eq__(self, other):
    if isinstance(other, Field):
      return self.name == other.name
    return False

  def __ne__(self, other):
    return not self.__eq__(other)

  __hash__ = None
