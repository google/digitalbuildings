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
from typing import Dict, List, NamedTuple, Optional

from yamlformat.validator import base_lib
from yamlformat.validator import config_folder_lib
from yamlformat.validator import entity_type_lib
from yamlformat.validator import findings_lib
from yamlformat.validator import state_lib
from yamlformat.validator import subfield_lib

# We currently are enforcing that fields are lower case only.
FIELD_CHARACTER_REGEX = re.compile(r'^[a-z][a-z0-9]*(?:_[a-z][a-z0-9]*)*$')
FIELD_INCREMENT_REGEX = re.compile(r'((?:_[0-9]+)*)$')


# pylint: disable=super-with-arguments
def SplitFieldName(qualified_field_name):
  """Splits the field name on '/' and returns the parts separately.

  Args:
    qualified_field_name: the possibly fully qualified field name

  Returns:
    tuple with namespace and raw field name.  Defaults to global for no
    namespace.
  """

  field_only = qualified_field_name
  namespace = ''
  split = qualified_field_name.split('/')
  if len(split) == 2:
    namespace, field_only = split
  return namespace, field_only


class FieldUniverse(findings_lib.FindingsUniverse):
  """Helper class to represent the defined universe of fields.

  Only contains valid fields.
  """

  def _GetNamespaceMapValue(self, namespace: str) -> List['Field']:
    """Helper method for FindingsUniverse._MakeNamespaceMap.

    Used to create a map from namespace names to field name lists.

    Args:
      namespace: FieldNamespace

    Returns:
      A list of field names from the namespace.
    """
    return list(namespace.fields.values())

  def IsFieldDefined(self, fieldname: str, namespace_name: str) -> bool:
    """Returns true if fieldname is defined within the namespace.

       If the field ends with a digit, it is removed to check if it exists
       without it

    Args:
      fieldname: string. Name of a field, optionally with increment.
      namespace_name: string.
    """
    fieldname_part, _ = entity_type_lib.SeparateFieldIncrement(fieldname)
    return fieldname_part in {
        field.name for field in self._namespace_map.get(namespace_name, [])
    }

  def GetFieldsMap(
      self, namespace_name: Optional[str] = None
  ) -> Dict[str, 'Field']:
    """Returns the fields defined within namespace, keyed by qualified std name.

    Args:
      namespace_name: string. Set to None to get all namespaces.
    """
    field_map = {}
    names = [namespace_name]
    if namespace_name is None:
      names = self._namespace_map.keys()

    for name in names:
      for field in self._namespace_map.get(name, []):
        field_map[name + '/' + field.name] = field

    return field_map


class FieldFolder(config_folder_lib.ConfigFolder):
  """Class representing a folder of Fields.

  Class contains all the context information and methods to validate and handle
  namespace up-leveling of fields. Fields are up-leveled (pushed up to the
  global namespace) if we can guarantee that they will not conflict with other
  fields defined there.

  Attributes:
    local_namespace: object representing the contents of the local namespace
    parent_namespace: object representing the contents of the global namespace

  Returns:
    An instance of the FieldFolder class.
  """

  def __init__(
      self,
      folderpath,
      parent_namespace=None,
      local_subfields=None,
      local_states=None,
  ):
    """Init.

    Args:
      folderpath: required string with full path to the folder containing
        fields. Path should be relative to google3/ and have no leading or
        trailing /.
      parent_namespace: object containing global namepsace information. When
        working in the global namespace folder, treat it as local and leave this
        blank.
      local_subfields: required map of subfield keys to Subfields for the local
        namespace.
      local_states: required map of state keys to States for the local
        namespace.
    """
    super().__init__(folderpath, base_lib.ComponentType.FIELD)
    self.local_namespace = FieldNamespace(
        self._namespace_name, local_subfields, local_states, parent_namespace
    )
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
    """Helper method that reads a yaml document and adds all fields found.

    Also adds any findings to the field.

    Args:
      document: yaml document
      context: config file context
    """
    if 'literals' not in document:
      self.AddFinding(findings_lib.UnrecognizedKeyError(document, context))
      return
    field_list = document['literals']
    if field_list is None:
      self.AddFinding(findings_lib.EmptyBlockWarning('literals', context))
      return
    for field_spec in field_list:
      field_name = ''
      states = None
      default_value_range = None
      if isinstance(field_spec, dict):
        # If the field has a list of states or a default value range, field_spec
        # must be a dict with a single entry.
        if len(field_spec) == 1:
          field_name, field_details = next(iter(field_spec.items()))
          # TODO(b/188242279) handle namespacing for states correctly.
          if isinstance(field_details, list):
            states = field_details
          elif isinstance(field_details, dict):
            default_value_range = field_details
          else:
            self.AddFinding(
                findings_lib.InvalidFieldFormatError(field_name, context)
            )
        else:
          field_name = next(iter(field_spec), '(Blank)')
          self.AddFinding(
              findings_lib.InvalidFieldFormatError(field_name, context)
          )
          continue
      else:
        field_name = field_spec
      field = Field(field_name, states, default_value_range, context)
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
    self._has_aggregation = False
    self._has_aggregation_descriptor = False
    self._has_required_fields = False

  _POINT_TYPES_NEEDING_MEASUREMENTS = ['setpoint', 'sensor', 'accumulator']

  _CAT_SPEC = NamedTuple(
      'CAT_SPEC', [('cat', str), ('required', bool), ('max', int)]
  )

  # Represents parameters for each subfield category.
  # Subfields are in the array in the order they should appear in the field.
  _CATEGORIES_IN_ORDER = [
      _CAT_SPEC(
          cat=subfield_lib.SubfieldCategory.AGGREGATION_DESCRIPTOR,
          required=False,
          max=1,
      ),
      _CAT_SPEC(
          cat=subfield_lib.SubfieldCategory.AGGREGATION, required=False, max=1
      ),
      _CAT_SPEC(
          cat=subfield_lib.SubfieldCategory.DESCRIPTOR, required=False, max=10
      ),
      _CAT_SPEC(
          cat=subfield_lib.SubfieldCategory.COMPONENT, required=False, max=1
      ),
      _CAT_SPEC(
          cat=subfield_lib.SubfieldCategory.MEASUREMENT_DESCRIPTOR,
          required=False,
          max=1,
      ),
      _CAT_SPEC(
          cat=subfield_lib.SubfieldCategory.MEASUREMENT, required=False, max=1
      ),
      _CAT_SPEC(
          cat=subfield_lib.SubfieldCategory.POINT_TYPE, required=True, max=1
      ),
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
      # TODO(tsodorff): Add individual warnings for each specific failure.
      cat_spec = self._CATEGORIES_IN_ORDER[self._category_index]
      if category == cat_spec.cat:
        if self._instance_count < cat_spec.max:
          self._instance_count += 1
          if category == subfield_lib.SubfieldCategory.MEASUREMENT:
            self._has_measurement = True
          if category == subfield_lib.SubfieldCategory.AGGREGATION:
            self._has_aggregation = True
          if category == subfield_lib.SubfieldCategory.AGGREGATION_DESCRIPTOR:
            self._has_aggregation_descriptor = True
          if category == subfield_lib.SubfieldCategory.POINT_TYPE:
            # Verify that any aggregation descriptor comes with an aggregation.
            # Since this is the last subfield to evaluate this is where it
            # would have seen agg and agg_desc subfields by here. If this block
            # doesnt exist, the field would fail anyway so the fact it didn't
            # run this check won't matter.
            if self._has_aggregation_descriptor and not self._has_aggregation:
              return False
            # Verify that, if there is no measurement, the point type specified
            # does not explicitly require one.
            if not self._has_measurement:
              if subfield.name in self._POINT_TYPES_NEEDING_MEASUREMENTS:
                return False
            self._has_required_fields = True
          return True
        else:
          return False
      if cat_spec.required and self._instance_count < 1:
        return False
      self._category_index += 1
      self._instance_count = 0
    return False

  def IsFieldComplete(self):
    """Indicates if the state machine has seen a completed field.

    Returns:
      True if the subfield categories presented represent a complete field.
    """
    return self._has_required_fields

  def HasMeasurementSubfield(self):
    """Indicates whether the field has a measurement subfield.

    Returns:
      True if the field has a measurement subfield.
    """
    return self._has_measurement


class FieldNamespace(findings_lib.Findings):
  """Class representing a namespace of fields.

  Attributes:
    fields: a dictionary of Field keys to field objects for fields added to this
      namespace.  NB: a field key is a permutation of the field name with
      subfields alpha-ordered (and-de-duped, but fields with dup-fields are
      invalid)
    subfields: a dictionary of subfield strings to Subfield objects defined in
      this namespace.
    states: a map from state names to State objects defined in this namespace
    namespace: string name of this namespace
    parent_namespace: reference to the parent namespace, or None if this is the
      global namespace

  Returns:
    An instance of the FieldNamespace class.
  """

  def __init__(
      self, namespace, subfields=None, states=None, parent_namespace=None
  ):
    """Init.

    Args:
      namespace: required string representing the name of the namespace. The
        global namespace is represented by the empty string.
      subfields: optional map of subfield names to Subfields. No validation of
        subfields is performed if this is left empty
      states: optional map of state names to States. No validation of states is
        performed if this isn't provided
      parent_namespace: global FieldNamespace object, if this is not it.

    Raises:
      RuntimeError: when subfields are defined on the child and not the parent.
    """
    super().__init__()
    self.namespace = namespace
    self.subfields = subfields
    self.states = states
    self.fields = {}
    self.parent_namespace = parent_namespace
    if self.subfields is not None:
      if self.parent_namespace and self.parent_namespace.subfields is None:
        raise RuntimeError(
            'Subfields are defined for the child, but not the parent'
        )

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
          field.AddFinding(findings_lib.UnrecognizedStateError(state, field))

    return uses_local_states

  def SubfieldsAreDefined(self):
    """Indicates whether subfields are defined.

    Returns:
      True if subfields have been populated for this namespace. Subfields may be
      populated with an empty map and this will still return true.
    """
    return self.subfields is not None

  def _IsValidConstruction(self, field, construction_validator):
    """Checks if the field has been constructed with properly ordered subfields.

    Args:
      field: the field to validate
      construction_validator: state machine used to validate the construction of
        a field from subfields

    Returns:
      True if the field is constructed properly.
    """
    pns = self.parent_namespace
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

  def ValidateSubfields(self, field, construction_validator):
    """Validates that the subfields that compose the field are valid.

    Adds any findings to the field.

    Args:
      field: reference to the Field object for subfield validation
      construction_validator: state machine used to validate the construction of
        a field from subfields

    Returns:
      True if the field uses any subfields from the local namespace.
    """
    pns = self.parent_namespace
    if not self.SubfieldsAreDefined() or (
        pns is not None and not pns.SubfieldsAreDefined()
    ):
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
        field.AddFinding(
            findings_lib.UnrecognizedSubfieldError(subfield, field)
        )

    if not missing_fields and not self._IsValidConstruction(
        field, construction_validator
    ):
      field.AddFinding(findings_lib.InvalidFieldConstructionError(field))

    return uses_local_subfields

  def PutIfAbsent(self, field: 'Field') -> Optional['Field']:
    """Puts the field into the field map if its key is absent from the map.

    Note: This method does NOT up-level.  Use it only for fields that should
    definitely be in the namespace, or for testing.

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

    construction_validator = _FieldValidationStateMachine()
    uses_local_subfields = self.ValidateSubfields(field, construction_validator)
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
          findings_lib.DuplicateFieldDefinitionError(
              insert_ns, field, old_field.file_context
          )
      )

    if self.SubfieldsAreDefined():
      is_numeric = field.IsNumeric(
          construction_validator.HasMeasurementSubfield()
      )
      if is_numeric and not field.HasDefaultValueRange():
        self.AddFinding(findings_lib.NumericFieldMissingValueRangeError(field))
      elif not is_numeric and field.HasDefaultValueRange():
        self.AddFinding(findings_lib.NonNumericFieldWithValueRangeError(field))


class Field(findings_lib.Findings):
  """Namespace-unaware class representing an individual field definition.

  Attributes:
    file_context: the config file context for where this field was defined
    name: the full name (without namespace) of this field
    subfields: a list of subfield keys for this field
    key: a hashable object representing the field's subfield set.
    states: a list of valid states for this field, or None
    default_value_range: a dictionary containing the default expected value
      range for this field if it is numeric, or None

  Returns:
    An instance of the Field class.
  """

  def __init__(
      self, name, states=None, default_value_range=None, file_context=None
  ):
    """Init.

    Args:
      name: required string representing the field.
      states: optional list of strings representing valid states for a
        multistate field. Should be None for non-multistate fields.
      default_value_range: optional dictionary containing the default expected
        value range for a numeric field. Should be None for non-numeric fields.
      file_context: optional object with the config file location of this field.
    """
    super().__init__()
    self.file_context = file_context
    self.name = name
    self.subfields = []
    self.states = states
    self.default_value_range = default_value_range

    if not isinstance(name, str):
      self.AddFinding(findings_lib.IllegalKeyTypeError(name, file_context))
    elif not FIELD_CHARACTER_REGEX.match(name):
      self.AddFinding(findings_lib.InvalidFieldNameError(name, file_context))
    else:
      self.InitAndValidateSubfields()
      self.ValidateStates()
      self.ValidateDefaultValueRange()

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

  def ValidateDefaultValueRange(self):
    if self.default_value_range is None:
      return
    if len(self.default_value_range) != 2:
      self.AddFinding(
          findings_lib.InvalidDefaultValueRangeError(
              self.default_value_range, self
          )
      )
    min_value = None
    max_value = None
    for range_key, range_value in self.default_value_range.items():
      if range_key in ('flexible_min', 'fixed_min'):
        min_value = range_value
      elif range_key in ('flexible_max', 'fixed_max'):
        max_value = range_value
      else:
        self.AddFinding(
            findings_lib.InvalidDefaultValueRangeError(
                self.default_value_range, self
            )
        )
    if min_value is None or max_value is None:
      self.AddFinding(
          findings_lib.InvalidDefaultValueRangeError(
              self.default_value_range, self
          )
      )
    if (
        (not isinstance(min_value, int) and not isinstance(min_value, float))
        or (not isinstance(max_value, int) and not isinstance(max_value, float))
        or float(min_value) >= float(max_value)
    ):
      self.AddFinding(
          findings_lib.InvalidDefaultValueRangeValueError(
              min_value, max_value, self
          )
      )

  def HasDefaultValueRange(self):
    return self.default_value_range is not None

  def IsNumeric(self, has_measurement_subfield: bool):
    """Returns a boolean indicating whether the field is numeric.

    Numeric fields:
    1. Do not end in "alarm", "mode", or "status". For fields that end with
       "command", only "scene_index_command" and fields that end with
       "percentage_command" or "frequency_command" are numeric.
    2. Either have a measurement subfield (e.g. percentage, temperature) or end
       in "count" or "counter".

    Args:
      has_measurement_subfield: A boolean indicating whether the field has a
        measurement subfield.

    Returns:
      A boolean indicating whether the field is numeric.
    """
    if 'count' in self.subfields or 'counter' in self.subfields:
      return True
    if any(sf in self.subfields for sf in ['alarm', 'mode', 'status']):
      return False
    if self.name == 'scene_index_command':
      return True
    if 'command' in self.subfields and not (
        'percentage_command' in self.name
        or 'frequency_command' in self.name
        or 'voltage_command' in self.name
    ):
      return False
    if has_measurement_subfield:
      return True
    return False

  def __eq__(self, other):
    if isinstance(other, Field):
      return self.name == other.name
    return False

  def __ne__(self, other):
    return not self.__eq__(other)

  __hash__ = None
