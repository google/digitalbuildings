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
"""Library defining different types of validation errors."""
from collections.abc import Iterable

import copy
import operator

MAX_RANK = 1000000000  # A big number, but not so big it breaks sorting
MISSING_PARENT_VALIDATION_RANK = 60

# TODO(b/254872070): Add type annotations


def MakeFieldString(field):
  """Represents OptWrapper as a string prepending '(opt)' for optional fields.

  Args:
    field: an OptWrapper for a field

  Returns:
    a string representation of the field
  """
  field_str = ''
  if field.optional:
    field_str += '(opt) '
  field_str += (
      f'{field.field.namespace}/{field.field.field}{field.field.increment}')
  return field_str


def _SortFindings(findings):
  return sorted(
      findings,
      key=operator.attrgetter('type_rank', 'category_rank', 'inner_rank',
                              'is_slave'))


def _DedupFindings(findings):
  finding_map = {}
  for finding in findings:
    if finding in finding_map:
      # Note: equality for map key != equality of finding contents
      # As a result, key and value are not interchangeable
      finding = _SortFindings([finding, finding_map.get(finding)])[0]
    finding_map[finding] = finding
  return finding_map.values()


# ---------------------------------------------------------------------------- #
# Base classes for findings.
# ---------------------------------------------------------------------------- #
class FileContext(object):
  """Wrapper class to store file-related information."""

  def __init__(self, filepath, begin_line_number=None, end_line_number=None):
    """Creates a FileContext.

    Args:
      filepath: string. relative path to the file with the issue.
      begin_line_number: optional int. Starting line number for the issue.
      end_line_number: optional int. Ending line number for the issue.
    """
    self.begin_line_number = begin_line_number
    self.end_line_number = end_line_number
    self.raw_filepath = filepath
    self.filepath = filepath

  def GetLineInfo(self):
    """Returns string containing the line number information.

    If no line number info, returns empty string.
    """
    if self.begin_line_number and self.end_line_number:
      return f'(Lines {self.begin_line_number} - {self.end_line_number})'
    if self.begin_line_number:
      return f'(Line {self.begin_line_number})'

    return ''


class Finding(object):
  """Virtual class for findings."""

  def __init__(self,
               message: str,
               file_context: 'FileContext',
               type_rank: int = MAX_RANK,
               category_rank: int = MAX_RANK,
               inner_rank: int = MAX_RANK,
               equality_key: str = None,
               is_master: bool = False):
    """Creates a finding.

    Args:
      message: string. the message associated with the finding.
      file_context: FileContext with file context info. Can be None.
      type_rank: first sort rank based on top level subclass (warning or error)
      category_rank: second sort rank based on the category of warning or error
      inner_rank: third sort rank based on ordering within category
      equality_key: object used to determine if this finding is a duplicate of
        another one.  Provide the same object to all the findings that should be
        considered equivalent.  If left blank, default object equality is used.
      is_master: set true if this finding should be the retained instance in the
        case of duplication.  Only one finding should be the master in a set.
        Defaults to false.
    """
    super().__init__()

    if not isinstance(message, str):
      raise TypeError(f'Argument {message} is not a string')
    if file_context is not None:
      if not isinstance(file_context, FileContext):
        raise TypeError(
            f'Argument {file_context} is not a FileContext object.')

    self.message = message
    self.file_context = file_context
    self.type_rank = type_rank
    self.inner_rank = inner_rank
    self.category_rank = category_rank
    self.equality_key = equality_key
    self.is_master = is_master
    self.is_slave = not is_master

  def __eq__(self, other):
    if isinstance(other, Finding):
      if self.equality_key is not None:
        return self.equality_key == other.equality_key
      return id(self) == id(other)
    return False

  def __ne__(self, other):
    return not self.__eq__(other)

  def __hash__(self):
    if self.equality_key is not None:
      return self.equality_key.__hash__()
    return hash(self.__repr__())

  def __str__(self):
    return self.message


class Findings(object):
  """Base class for validators to keep track of findings."""

  def __init__(self):
    self._findings_list = []
    self._is_changed = False

  def _GetDynamicFindings(self, filter_old_warnings):
    """Override this to include additional findings not in self._findings_list.

    Does nothing by default.  Override this method to add findings from
    subclasses for analysis without modifying _self._findings_list.

    Args:
      filter_old_warnings: Set True to filter warnings in unchanged components.

    Returns:
      A list of findings defined by the child class
    """
    # delete unused argument to thwart linter
    del filter_old_warnings
    return []

  def AddFindings(self, findings):
    """Add an error to errors_list.

    Args:
      findings: required list of Finding objects.

    Raises:
      TypeError: a finding is not a member of the Finding base class.
    """
    for finding in findings:
      self.AddFinding(finding)

  def AddFinding(self, finding):
    """Add an error to errors_list.

    Args:
      finding: Finding object.

    Raises:
      TypeError: error is not a member of the Finding base class.
    """
    if not isinstance(finding, Finding):
      raise TypeError(f'Argument "{finding}" is not an instance of the base '
                      'classes ValidationError or ValidationWarning.')

    self._findings_list.append(finding)

  def GetFindings(self, filter_old_warnings=False):
    """Get findings found under this object.

    Args:
      filter_old_warnings: Set True to filter warnings on unchanged components.

    Returns:
      A list of findings for this object and its children
    """
    dynamic_findings = self._GetDynamicFindings(filter_old_warnings)
    if not filter_old_warnings:
      return list(_DedupFindings(self._findings_list + dynamic_findings))

    filtered_findings = copy.copy(dynamic_findings)
    for finding in self._findings_list:
      if self._is_changed or not isinstance(finding, ValidationWarning):
        filtered_findings.append(finding)
    return _SortFindings(_DedupFindings(filtered_findings))

  def HasFindingTypes(self, finding_types: Iterable[Finding]):
    """Returns true if any finding is one of the types in findings_types.

    Args:
      finding_types: list of types of findings.
    """
    for finding in self.GetFindings():
      if isinstance(finding, tuple(finding_types)):
        return True
    return False

  def IsValid(self):
    """Returns true if there are no actionable errors in _findings_list."""
    for finding in self.GetFindings():
      if isinstance(finding, ValidationError):
        return False
    return True

  def SetChanged(self):
    """Marks this object as containing a change in the latest cl."""
    self._is_changed = True

  def IsChanged(self):
    """Returns True if this object contains a change in the latest cl."""
    return self._is_changed


class FindingsUniverse(Findings):
  """Base class for universes of ontology items.

  Attributes:
    folders: list of ConfigFolder objects parsed from field files.  Each
      universe corresponds to a particular type of ontology item.
  """

  def __init__(self, folders):
    """Init.

    Args:
      folders: list of ConfigFolder objects parsed from field files.
    """
    super().__init__()
    self.folders = folders
    self._namespace_map = self._MakeNamespaceMap(
        [folder.local_namespace for folder in folders])

  def _MakeNamespaceMap(self, namespaces):
    """Returns mapping from namespace strings to valid ontology entity sets.

    Args:
      namespaces: list of namespace objects.
    """
    return {ns.namespace: self._GetNamespaceMapValue(ns) for ns in namespaces}

  def _GetNamespaceMapValue(self, namespace):
    """Override in subclass to define how values in namespace map are populated.
    """
    # Delete the unused parameter so the linter doesn't complain.
    del namespace
    return []

  def _GetDynamicFindings(self, filter_old_warnings):
    findings = []
    for folder in self.folders:
      findings += folder.GetFindings(filter_old_warnings)
    return findings


# ---------------------------------------------------------------------------- #
# Base classes for types of findings.
# ---------------------------------------------------------------------------- #
class ValidationError(Finding):
  """Virtual class for blocking errors."""

  def __init__(self,
               message,
               file_context,
               category_rank=MAX_RANK,
               inner_rank=MAX_RANK):
    error_info = 'ERROR '
    if file_context is not None:
      error_info += file_context.GetLineInfo()
    super().__init__(f'{error_info}: {message}\n', file_context, 1,
                     category_rank, inner_rank)


class ValidationWarning(Finding):
  """Virtual class for all non-blocking warnings."""

  def __init__(self,
               message,
               file_context,
               category_rank=MAX_RANK,
               inner_rank=MAX_RANK,
               equality_key=None,
               is_master=False):
    warning_info = 'Warning '
    if file_context is not None:
      warning_info += file_context.GetLineInfo()
    super().__init__(f'{warning_info}: {message}\n', file_context, 2,
                     category_rank, inner_rank, equality_key, is_master)


class DuplicateDefinitionError(ValidationError):
  """Base class for error for same component name being defined more than once.

  Returns:
    An instance of the DuplicateDefinitionError.
  """

  def __init__(self, component_type, namespace, component_name, context,
               prev_context):
    """Init.

    Args:
      component_type: Type of connection, unit, field, etc.
      namespace: Namespace for component_type.
      component_name: Component's name as a string.
      context: Instance of FileContext class for the duplicate item.
      prev_context: Instance of FileContext class for originally defined item.
    """

    file_info = ''
    if prev_context:
      file_info = f'<{prev_context.filepath}> {prev_context.GetLineInfo()}'
    super().__init__(
        (f'{component_type} "{namespace.namespace}/{component_name}" was'
         f' already defined in:\n\t{file_info}'), context)


# TODO(berkoben): After migrating to yaml, need to add more context to locate
# errors, because line number info will be lost.


# ---------------------------------------------------------------------------- #
# Errors relating to files.
# ---------------------------------------------------------------------------- #
class InconsistentFileLocationError(ValidationError):
  """File not located within a subfolder inside resources."""

  def __init__(self, expected_path, file_context):
    fp = file_context.filepath
    super().__init__(
        f'File "{fp}" is not at the expected path "{expected_path}".',
        file_context)


# ---------------------------------------------------------------------------- #
# Errors relating to config text (typos)
# ---------------------------------------------------------------------------- #
class DuplicateKeyError(ValidationError):
  """Config contains two identical keys."""

  def __init__(self, key, context):
    super().__init__(
        f'Key "{key}" cannot appear multiple times in the same mapping.',
        context)


class IllegalKeyTypeError(ValidationError):
  """Config contains a key of an invalid non-string type."""

  def __init__(self, key, context):
    super().__init__(
        f'Expected mapping key "{key}" to be a string; found {1}.', context)


class UnrecognizedKeyError(ValidationError):
  """Config contains an unexpected mapping key."""

  def __init__(self, content, context):
    """Init.

    Args:
      content: Invalid mapping key
      context: instance of FileContext class for content
    """
    super().__init__(
        f'"{content}" is not recognized as a valid mapping key here.',
        context)


class EmptyBlockWarning(ValidationWarning):
  """Mapping value is empty."""

  def __init__(self, key, context):
    super().__init__(f'Mapping for "{key}" has no content.', context)


class EmptyFileWarning(ValidationWarning):
  """Validator found an empty YAML file."""

  def __init__(self, context):
    super().__init__('YAML file is empty.', context)


# ---------------------------------------------------------------------------- #
# Errors relating to Fields.
# ---------------------------------------------------------------------------- #
class InvalidFieldNameError(ValidationError):
  """An entity type name does not match the accepted format."""

  def __init__(self, name, context):
    """Init.

    Args:
      name: The field name.
      context: Instance of FileContext for the field defined in DBO.
    """
    super().__init__(
        f'Field name "{name}" is not valid. It must contain only lowercase '
        'letters, digits, and underscores. The first character of the name and '
        'the first character after each underscore must be a letter.', context)


class DuplicateSubfieldError(ValidationError):
  """Field has more than one identical subfield."""

  def __init__(self, subfield, field):
    super().__init__(
        f'Field "{field.name}" is not allowed to contain subfield "{subfield}" '
        'more than once.', field.file_context)


class UnrecognizedSubfieldError(ValidationError):
  """Field references an unrecognized subfield."""

  def __init__(self, subfield, field):
    super().__init__(
        f'Field "{field.name}" references unrecognized subfield "{subfield}".',
        field.file_context)


class InvalidFieldConstructionError(ValidationError):
  """One or more subfield in this field is in the wrong location / order."""

  def __init__(self, field):
    super().__init__(
        f'Field "{field.name}" contains subfields in an incorrect order or is '
        'missing a required subfield.', field.file_context)


class DuplicateFieldDefinitionError(DuplicateDefinitionError):
  """Field is defined multiple times in a namespace."""

  def __init__(self, namespace, current_instance, prev_context):
    """Init.

    Args:
       namespace: Defined namespace of the duplciated field.
       current_instance: Instance of FileContext class for duplicate field.
       prev_context: Instance of FileContext class for duplicated field.
    """
    super().__init__('Field', namespace, current_instance.name,
                     current_instance.file_context, prev_context)


class InvalidFieldFormatError(ValidationError):
  """The field's YAML specification is invalid.

  The complete YAML specification of a field and its properties does not have
  proper formatting and couldn't be parsed.
  """

  def __init__(self, key, context):
    super().__init__(
        f'Field "{key}" definition has an invalid format; expected only a '
        'sequence of state names.', context)


class InvalidStateFormatError(ValidationError):
  """A state string in a field's state list does not have proper formatting."""

  def __init__(self, state, field):
    super().__init__(
        f'State "{state}" in list for field "{field.name}" has an invalid '
        'format.', field.file_context)


class DuplicateStateError(ValidationError):
  """A state appears multiple times in a field's state list."""

  def __init__(self, state, field):
    super().__init__(
        f'Field "{field.name}" references state "{state}" more than once.',
        field.file_context)


class UnrecognizedStateError(ValidationError):
  """Field references an unrecognized state."""

  def __init__(self, state, field):
    """Init.

    Args:
      state: Unrecognized state name as a string.
      field: Instance of Field class for field referencing unrecognized state.
    """
    super().__init__(
        f'Field "{field.name}" references unrecognized state "{state}".',
        field.file_context)


class InvalidDefaultValueRangeError(ValidationError):
  """Field references an invalid default value range."""

  def __init__(self, default_value_range, field):
    """Init.

    Args:
      default_value_range: The invalid default value range map.
      field: Instance of Field class for field referencing the invalid value
        range.
    """
    super().__init__(
        f'Field "{field.name}" references invalid default value range '
        f'{default_value_range}. Numeric fields must define exactly one default'
        ' minimum value (with a key of either "flexible_min" or "fixed_min") '
        'and one default maximum value (with a key of either "flexible_max" or '
        '"fixed_max").', field.file_context)


class InvalidDefaultValueRangeValueError(ValidationError):
  """Field has a default value range with invalid values."""

  def __init__(self, min_value, max_value, field):
    """Init.

    Args:
      min_value: The min value in the default value range map.
      max_value: The max value in the default value range map.
      field: Instance of Field class for field referencing the invalid value
        range.
    """
    super().__init__(
        f'Field "{field.name}" references invalid default value range '
        f'[{min_value}, {max_value}]. The min  and max values must be numeric, '
        'and the min value must be less than the max value.',
        field.file_context)


class NumericFieldMissingValueRangeError(ValidationError):
  """Field has a measurement subfield but no default value range."""

  def __init__(self, field):
    """Init.

    Args:
      field: Instance of Field class for field missing a value range.
    """
    super().__init__(
        f'Field "{field.name}" is numeric (has a measurement subfield) but is '
        'missing a default value range.', field.file_context)


class NonNumericFieldWithValueRangeError(ValidationError):
  """Field has no measurement subfield but specifies a default value range."""

  def __init__(self, field):
    """Init.

    Args:
      field: Instance of Field class for field with a default value range.
    """
    super().__init__(
        f'Field "{field.name}" is not numeric (has no measurement subfield) but'
        ' specifies a default value range.', field.file_context)


# ---------------------------------------------------------------------------- #
# Errors relating to Subfields.
# ---------------------------------------------------------------------------- #
class InvalidSubfieldNameError(ValidationError):
  """A subfield name does not match the accepted format."""

  def __init__(self, name, context):
    """Init.

    Args:
      name: Current name of the incorrectly named subfield.
      context: Instance of FileContext class for subfield.
    """
    super().__init__(
        f'Subfield name "{name}" is not valid. It must contain only lowercase '
        'letters and digits, and it must begin with a letter.', context)


class DuplicateSubfieldDefinitionError(DuplicateDefinitionError):
  """Subfield is defined multiple times in a namespace."""

  def __init__(self, namespace, current_instance, prev_context):
    super().__init__('Subfield', namespace, current_instance.name,
                     current_instance.file_context, prev_context)


class MissingSubfieldDescriptionWarning(ValidationWarning):
  """Subfield description is empty."""

  def __init__(self, subfield_name, context):
    """Init.

    Args:
      subfield_name: Name of subfield as a string.
      context: Instance of FileContext class for subfield.
    """
    super().__init__(
        f'Subfield "{subfield_name}" description is empty.', context, 10)


class MissingUnitError(ValidationError):
  """Measurement subfield has no corresponding unit definitions."""

  def __init__(self, subfield):
    super().__init__(
        f'Measurement subfield "{subfield.name}" has no corresponding unit '
        'definitions in the same namespace.', subfield.file_context)


class MeasurementAliasIsAliasedError(ValidationError):
  """Measurement subfield is aliased to another aliased subfield."""

  def __init__(self, alias):
    """Init.

    Args:
      alias: The invalid MeasurementAlias object.
    """
    super().__init__(
        f'Measurement subfield "{alias.alias_name}" is not allowed to be an '
        'alias of "{alias.base_name}" because that subfield is also an alias.',
        alias.file_context)


class UnrecognizedMeasurementAliasBaseError(ValidationError):
  """A measurement subfield is an alias of an unrecognized subfield."""

  def __init__(self, alias):
    """Init.

    Args:
      alias: The invalid MeasurementAlias object.
    """
    super().__init__(
        f'The alias definition of measurement subfield "{alias.alias_name}" '
        f'references unrecognized subfield "{alias.base_name}".',
        alias.file_context)


class DuplicateMeasurementAliasError(DuplicateDefinitionError):
  """A measurement type alias has been defined more than once."""

  def __init__(self, namespace, alias, prev_context):
    """Init.

    Args:
      namespace: The UnitNamespace that the alias is defined in.
      alias: The invalid MeasurementAlias object.
      prev_context: FileContext of the previous definition of the alias.
    """
    super().__init__('measurement alias', namespace, alias.alias_name,
                     alias.file_context, prev_context)


class InvalidSubfieldNamespaceError(ValidationError):
  """A subfield incorrectly defined in a namespace."""

  def __init__(self, namespace, subfield):
    """init.

    Args:
      namespace: The subfield's defined namespace.
      subfield: instance of Subfield class which is incorrectly defined.
    """
    super().__init__(
        f'Subfield {subfield.name} cannot be defined in the namespace '
        f'{namespace}', subfield.file_context)


# ---------------------------------------------------------------------------- #
# Errors relating to States.
# ---------------------------------------------------------------------------- #
class InvalidStateNameError(ValidationError):
  """A state name does not match the accepted format."""

  def __init__(self, name, context):
    """Init.

    Args:
      name: State name as a string.
      context: Instance of FileContext for invalid state name.
    """
    super().__init__(
        f'State name "{name}" is not valid. It must contain only uppercase '
        'letters and underscores, and it must begin with a letter.', context)


class DuplicateStateDefinitionError(DuplicateDefinitionError):
  """A state is defined multiple times in a namespace."""

  def __init__(self, namespace, current_instance, prev_context):
    super().__init__('State', namespace, current_instance.name,
                     current_instance.file_context, prev_context)


class MissingStateDescriptionWarning(ValidationWarning):
  """State description is empty."""

  def __init__(self, state):
    super().__init__(
        f'State "{state.name}" description is empty.', state.file_context, 10)


# ---------------------------------------------------------------------------- #
# Errors relating to Connections.
# ---------------------------------------------------------------------------- #
class InvalidConnectionNameError(ValidationError):
  """A connection name does not match the accepted format."""

  def __init__(self, name, context):
    super().__init__(
        f'Connection name "{name}" is not valid. It must contain only uppercase'
        ' letters and underscores, and it must begin with a letter.', context)


class DuplicateConnectionDefinitionError(DuplicateDefinitionError):
  """A connection is defined multiple times in a namespace."""

  def __init__(self, namespace, current_instance, prev_context):
    super().__init__('Connection', namespace, current_instance.name,
                     current_instance.file_context, prev_context)


class InvalidConnectionNamespaceError(ValidationError):
  """A connection is defined outside the global namespace."""

  def __init__(self, namespace_name, context):
    super().__init__(
        f'Namespace "{namespace_name}" contains connection definitions; '
        'connections are only allowed in the global namespace.', context)


class MissingConnectionDescriptionWarning(ValidationWarning):
  """Connection description is empty."""

  def __init__(self, connection):
    """Init.

    Args:
      connection: Instance of Connection class missing a description.
    """
    super().__init__(
        f'Connection "{connection.name}" description is empty.',
        connection.file_context, 10)


# ---------------------------------------------------------------------------- #
# Errors relating to Units.
# ---------------------------------------------------------------------------- #
class InvalidUnitNameError(ValidationError):
  """A unit name does not match the accepted format."""

  def __init__(self, name, context):
    """Init.

    Args:
      name: Invalid name as a string.
      context: Instance of FileContext for invalid unit name.
    """
    super().__init__(
        f'Unit name "{name}" is not valid. It must contain only lowercase '
        'letters and underscores, and it must begin with a letter.', context)


class DuplicateUnitDefinitionError(DuplicateDefinitionError):
  """A unit is defined multiple times in a namespace."""

  def __init__(self, namespace, current_instance, prev_context):
    """Init.

    Args:
      namespace: Defined namespace for unit as a string.
      current_instance: Instance of FileContext class for duplicate unit.
      prev_context: Instance of FileContext class for unit.
    """
    super().__init__('Unit', namespace, current_instance.name,
                     current_instance.file_context, prev_context)


class InvalidMeasurementFormatError(ValidationError):
  """The content of a measurement is invalidly formatted."""

  def __init__(self, measurement, context):
    """Init.

    Args:
      measurement: Name of the measurement subfield.
      context: Instance of FileContext class for unit.
    """
    super().__init__(
        f'Measurement type "{measurement}" has an invalid format; each '
        'measurement type should map to either a string (another measurement '
        'type) or a map containing the units that belong to the measurement '
        'type.', context)


class InvalidUnitFormatError(ValidationError):
  """A unit's YAML specification is invalid."""

  def __init__(self, unit_name, context):
    """Init.

    Args:
      unit_name: The unit name.
      context: Instance of FileContext class for unit.
    """
    super().__init__(
        f'Unit "{unit_name}" definition has an invalid format; expected either '
        'the unit name and a "STANDARD" tag or the unit name and a map '
        'containing the conversion multiplier and offset.', context)


class InvalidUnitNamespaceError(ValidationError):
  """A unit defined outside of global namespace."""

  def __init__(self, namespace, context):
    """Init.

    Args:
      namespace: Namespace string for incorrectly defined unit.
      context: A FileContext Instance for incorrectly defined unit.
    """
    super().__init__(
        f'All units must be defined in global namespace instead of '
        f'{namespace}.', context)


class UnknownUnitTagError(ValidationError):
  """A unit entry has an unknown tag."""

  def __init__(self, unit_name, tag, context):
    super().__init__(
        f'Unit "{unit_name}" has an unrecognized tag "{tag}".', context)


class InvalidUnitConversionKeyError(ValidationError):
  """A unit entry has a conversion map with an invalid key."""

  def __init__(self, unit_name, key, context):
    """Init.

    Args:
      unit_name: The unit name.
      key: The key in the conversion map item.
      context: Instance of FileContext class for unit.
    """
    super().__init__(
        f'Unit "{unit_name}" has a conversion map with key "{key}". The '
        'conversion map for a non-standard unit must contain only the '
        '"multiplier" and "offset" keys.', context)


class InvalidUnitConversionValueError(ValidationError):
  """A unit entry has a conversion map with an invalid value."""

  def __init__(self, unit_name, key, value, context):
    """Init.

    Args:
      unit_name: The unit name.
      key: The key in the conversion map item.
      value: The value in the conversion map item.
      context: Instance of FileContext class for unit.
    """
    super().__init__(
        f'Unit "{unit_name}" has a conversion map with key "{key}" and invalid '
        f'value "{value}". The value must be numeric.', context)


class InvalidUnitConversionMapError(ValidationError):
  """A unit entry has a conversion map with an invalid size."""

  def __init__(self, unit_name, num_items, context):
    """Init.

    Args:
      unit_name: The unit name.
      num_items: The number of items in the conversion map.
      context: Instance of FileContext class for unit.
    """
    super().__init__(
        f'Unit "{unit_name}" has a conversion map with {num_items} items when '
        'there should be exactly 2. The conversion map for a non-standard unit '
        'must contain only the "multiplier" and "offset" keys.', context)


class StandardUnitCountError(ValidationError):
  """A measurement type does not have exactly one unit tagged as standard."""

  def __init__(self, measurement_type, tag_count, context):
    super().__init__(
        f'Measurement type "{measurement_type}" has {tag_count} units tagged as'
        ' standard. Expected 1.', context)


class UnknownMeasurementTypeError(ValidationError):
  """A unit has an unknown measurement type."""

  def __init__(self, unit, measurement_type):
    super().__init__(
        f'Unit "{unit.name}" is defined under the unrecognized measurement type'
        f' "{measurement_type}".', unit.file_context)


# ---------------------------------------------------------------------------- #
# Errors on the level of individual entity types.
# ---------------------------------------------------------------------------- #
class MissingTypenameError(ValidationError):
  """Typename is empty."""

  def __init__(self, entity_type):
    super().__init__('Missing typename.', entity_type.file_context)


class InvalidTypenameError(ValidationError):
  """An entity type name does not match the accepted format."""

  def __init__(self, name, context):
    """Init.

    Args:
      name: Invalid type name as a string.
      context: Instance of FileContext class for type name.
    """
    super().__init__(
        f'Entity type name "{name}" is not valid. It must contain only letters,'
        ' digits, and underscores, and it must begin with a letter.', context)


class InvalidTypeGuidError(ValidationError):
  """An entity type guid does not follow the UUID v4 format."""

  def __init__(self, entity_type):
    super().__init__(
        f'The GUID {entity_type.guid} for entity type name '
        f'"{entity_type.typename}" is missing or invalid. The GUID must have '
        f'the UUID v4 format.', entity_type.file_context)


class IllegalFieldIncrementError(ValidationError):
  """Field is incremented unnecessarily."""

  def __init__(self, entity_type, field_name):
    super().__init__(
        f'Field {field_name} of {entity_type.typename} is incremented but there'
        f' are no other increments of the same base field on this entity.',
        entity_type.file_context)


class IllegalFieldIncrementWarning(ValidationError):
  """Field is incremented unnecessarily."""

  def __init__(self, entity_type, field_name):
    super().__init__(
        f'Field {field_name} of {entity_type.typename} is incremented but there'
        f' are no other increments of the same base field on this entity.',
        entity_type.file_context)


class MissingEntityTypeDescriptionWarning(ValidationWarning):
  """Entity type description is empty."""

  def __init__(self, entity_type):
    super().__init__(
        f'Entity type "{entity_type.typename}" description is empty.',
        entity_type.file_context, 20)


class DuplicateFieldError(ValidationError):
  """Duplicate fields defined within an entity type."""

  def __init__(self, entity_type, field):
    super().__init__(
        f'Entity type "{entity_type.typename}" defines field "{field}" '
        f'multiple times.', entity_type.file_context)


class UndefinedFieldError(ValidationError):
  """Field is undefined."""

  def __init__(self, entity_type, field):
    super().__init__(
        f'Entity type "{entity_type.typename}" references unrecognized field '
        f'"{field}".', entity_type.file_context)


class UnrecognizedFieldFormatError(ValidationError):
  """Declared field has incorrect format."""

  def __init__(self, entity_type, field):
    super().__init__(
        f'Field name "{field}" has incorrect formatting. The format should be '
        'either "<fieldname>" or "<namespace>/<fieldname>".',
        entity_type.file_context)


class UnrecognizedParentFormatError(ValidationError):
  """Declared parent has incorrect format."""

  def __init__(self, entity_type, parent_name):
    super().__init__(
        f'Parent name "{parent_name}" has incorrect formatting. The format '
        f'should be either "<parent_name>" or "<namespace>/<parent_name>".',
        entity_type.file_context)


class DuplicateParentError(ValidationError):
  """Entity has duplicate parent ids defined."""

  def __init__(self, entity_type, parent_name):
    super().__init__(
        f'Entity type "{entity_type.typename}" references "{parent_name}" as a '
        f'parent type more than once.', entity_type.file_context)


class InheritedFieldsSetError(ValidationError):
  """The inherited_fields_set field is set."""

  def __init__(self, entity_type):
    super().__init__(
        'Inherited_fields_expanded should not be set.',
        entity_type.file_context)


class AbstractPassthroughTypeError(ValidationError):
  """The entity type is declared as both abstract and allowing undefined fields.
  """

  def __init__(self, entity_type):
    """Init.

    Args:
      entity_type: The invalid EntityType object.
    """
    super().__init__(
        f'Type "{entity_type.typename}" cannot be abstract while allowing '
        f'undefined fields.', entity_type.file_context)


# ---------------------------------------------------------------------------- #
# Errors on the level of namespaces.
# ---------------------------------------------------------------------------- #
class NonexistentParentError(ValidationError):
  """Parent id specified by a type does not exist."""

  def __init__(self, entity_type, parent_name):
    super().__init__(
        f'Entity type "{entity_type.typename}" references unrecognized parent '
        f'type "{parent_name}".', entity_type.file_context)


class PassthroughParentError(ValidationError):
  """Entity type has a parent that allows undefined fields."""

  def __init__(self, entity_type, parent_name):
    """Init.

    Args:
      entity_type: The invalid EntityType object.
      parent_name: Name of the parent entity type.
    """
    super().__init__(
        f'Entity type "{entity_type.typename}" is not allowed to implement '
        f'passthrough type "{parent_name}".', entity_type.file_context)


class InheritanceCycleError(ValidationError):
  """Cycle detected in the type inheritance graph."""

  def __init__(self, entity_type, parent_name):
    super().__init__(
        f'Inheritance cycle detected between entity types '
        f'"{entity_type.typename}" and "{parent_name}".',
        entity_type.file_context)


class DuplicateEntityTypeDefinitionError(DuplicateDefinitionError):
  """Duplicate type names defined within the same namespace."""

  def __init__(self, namespace, current_instance, prev_context):
    super().__init__(
        'Entity type', namespace, current_instance.typename,
        current_instance.file_context, prev_context)


class DuplicateGuidsError(ValidationError):
  """Duplicate type GUIDs defined within the ontology."""

  def __init__(self, namespace, entity_type, mapped_entity_type):
    """Init.

    Args:
      namespace: Entity type namespace as a string.
      entity_type: Instance of EntityType class for dupicate entity type
      mapped_entity_type: Instance of EntityType class mapped to namespace
    """
    super().__init__(
        f'Duplicate type GUIDs are not allowed. Entity type name '
        f'"{entity_type.typename}" within namespace "{namespace}" with GUID '
        f'"{entity_type.guid}" was already defined in \n\t'
        f'<{mapped_entity_type.file_context.filepath}> (Line '
        f'{mapped_entity_type.file_context.begin_line_number}). Please remove '
        'one of these GUIDs so that the GUID generator runs again.',
        entity_type.file_context)


class DuplicateLocalFieldSetsWarning(ValidationWarning):
  """Two types declare the exact same local field sets."""

  def __init__(self, entity_type, dup_entity_types):
    field_list = list(entity_type.local_field_names)
    field_list.sort()
    fieldstr = ''
    for f in field_list:
      fieldstr += '\n\t\t' + f
    t = (f'Entity type "{entity_type.typename}" has the same local'
         f' {len(entity_type.local_field_names)} field set:{fieldstr}\n\tas:\n')

    for dup in dup_entity_types:
      t += f'\t\t<{dup.typename}> in {dup.file_context.filepath}\n'
    key_arr = dup_entity_types.copy()
    key_arr.append(entity_type)
    super().__init__(t, entity_type.file_context, 40,
                     MAX_RANK - len(field_list), frozenset(key_arr),
                     entity_type.is_canonical)


class DuplicateExpandedFieldSetsWarning(ValidationWarning):
  """Two types have the exact same expanded field sets."""

  def __init__(self, entity_type, dup_entity_typenames, equality_key):
    field_count = len(
        set(entity_type.local_field_names.keys())
        | set(entity_type.inherited_field_names.keys()))
    text = (f'Entity type "{entity_type.typename}" has the same expanded set of'
            f' {field_count} fields as:\n')

    for typename in dup_entity_typenames:
      text += (f'\t<{typename}> with {dup_entity_typenames[typename]} '
               'optionality changes\n')

    text += '\tAre they the same type?'
    super().__init__(text, entity_type.file_context, 30,
                     MAX_RANK - len(dup_entity_typenames), equality_key,
                     entity_type.is_canonical)


class OverlappingFlexTypeChildWarning(ValidationWarning):
  """A type can be represented by a larger, flexible type."""

  def __init__(self, entity_type, best_diff, dup_entity_typenames):
    field_count = len(
        set(entity_type.local_field_names.keys())
        | set(entity_type.inherited_field_names.keys()))
    text = (f'Entity type "{entity_type.typename}" with {field_count} fields '
            'can be represented by flex-types:\n')

    for typename in dup_entity_typenames:
      text += f'\t<{typename}>\n\t\tUnmatched Optional:\n'
      for field in dup_entity_typenames[typename]:
        text += f'\t\t\t{field}\n'

    super().__init__(text, entity_type.file_context, 32,
                     MAX_RANK - field_count + best_diff)


class OverlappingFlexTypeParentWarning(ValidationWarning):
  """A flexible type can represent another, smaller type."""

  def __init__(self, entity_type, dup_entity_typenames):
    field_count = len(
        set(entity_type.local_field_names.keys())
        | set(entity_type.inherited_field_names.keys()))
    text = (f'flex-type "{entity_type.typename}" with {field_count} fields can '
            'represent:\n')

    for typename in dup_entity_typenames:
      text += f'\t<{typename}>\n\t\tUnmatched Optional:\n'
      for field in dup_entity_typenames[typename]:
        text += f'\t\t\t{field}\n'

    super().__init__(text, entity_type.file_context, 31,
                     MAX_RANK - len(dup_entity_typenames))


class PossibleOverlappingFlexTypeChildWarning(ValidationWarning):
  """A type can ALMOST be represented by a larger, flexible type."""

  def __init__(self, entity_type, best_diff, dup_entity_typenames):
    field_count = len(
        set(entity_type.local_field_names.keys())
        | set(entity_type.inherited_field_names.keys()))
    text = (f'Entity type "{entity_type.typename}" with {field_count} fields '
            'can ALMOST be represented by flex-types:\n')

    for typename in dup_entity_typenames:
      text += f'\t<{typename}> \n\t\tUnmatched required:\n'
      for field in dup_entity_typenames[typename]:
        text += f'\t\t\t{field}\n'

    super().__init__(text, entity_type.file_context, 34,
                     MAX_RANK - field_count + best_diff)


class PossibleOverlappingFlexTypeParentWarning(ValidationWarning):
  """A flexible type ALMOST can represent another, smaller type."""

  def __init__(self, entity_type, dup_entity_typenames):
    field_count = len(
        set(entity_type.local_field_names.keys())
        | set(entity_type.inherited_field_names.keys()))
    text = (f'flex-type "{entity_type.typename}" with {field_count} fields can '
            'ALMOST represent:\n')

    for typename in dup_entity_typenames:
      text += f'\t<{typename}>\n\t\tUnmatched Required:\n'
      for field in dup_entity_typenames[typename]:
        text += f'\t\t\t{field}\n'

    super().__init__(text, entity_type.file_context, 33,
                     MAX_RANK - len(dup_entity_typenames))


# ---------------------------------------------------------------------------- #
# Type Management Findings
# ---------------------------------------------------------------------------- #


class MissingParentWarning(ValidationWarning):
  """This type could use inhheritance to decrease its local field count."""

  def __init__(self, typenames, set_size, qualified_parents, context,
               sum_match_quality, curation_bonus, key):
    """Init.

    Args:
      typenames: list of typenames that contain the field subset.
      set_size: Number of fields in the subset.
      qualified_parents: list of qualified names of types that have exactly the
        fields in the subset.
      context: file context to attach this finding to (for sorting later).
      sum_match_quality: sum of match qualities for the subset to all types in
        typenames.
      curation_bonus: Set true if parents are curated types. Improves sort rank.
      key: comparison object to use when comparing to other findings for
        deduplication.
    """
    text = (f'Entity types {sorted(typenames)} all contain '
            f'{sorted(qualified_parents)}. Size: {set_size}. Average Quality: '
            f'{sum_match_quality / len(typenames):0.2f}')

    rank = MISSING_PARENT_VALIDATION_RANK
    if curation_bonus:
      rank -= 1

    # Arbitrary score that attempts to rank results by a combination of: the
    # fraction of free fields they replace, the number of types that have the
    # replacement and how big the replacement is.
    match_score = sum_match_quality + len(typenames) * set_size / 25
    super().__init__(text, context, rank, MAX_RANK - match_score, key, False)


class UnusedParentWarning(ValidationWarning):
  """This type could be a parent of one or more other types."""

  def __init__(self, entity_type, qualified_children, sum_match_quality, key):
    field_count = len(entity_type.local_field_names) + len(
        entity_type.inherited_field_names)
    text = (f'Entity type "{entity_type.typename}" with {field_count} fields is'
            f' contained within {len(qualified_children)} '
            f'types:\n\t{sorted(qualified_children)}')

    # Arbitrary score that attempts to rank results by a combination of: the
    # fraction of free fields they replace, the number of types that have the
    # replacement and how big the replacement is.
    match_score = sum_match_quality + len(qualified_children) * field_count / 25
    super().__init__(text, entity_type.file_context,
                     MISSING_PARENT_VALIDATION_RANK,
                     MAX_RANK - match_score, key, True)


class PotentialParentReplacementWarning(ValidationWarning):
  """The inheritance of this type could be simplified."""

  def __init__(self, entity_type, field_count, qualified_parents,
               replaced_parents):
    text = (f'Entity type "{entity_type.typename}" can replace parents '
            f'{sorted(replaced_parents)} with one of '
            f'{sorted(qualified_parents)} ({field_count} fields).')

    super().__init__(text, entity_type.file_context, 50, MAX_RANK - field_count)


class ParentReplacementCandidateWarning(ValidationWarning):
  """This type could simplify the inheritance of another type(s)."""

  def __init__(self, entity_type, field_count, replacement_targets):
    field_count = len(entity_type.local_field_names) + len(
        entity_type.inherited_field_names)
    text = (f'Entity type "{entity_type.typename}" replaces multiple parents in'
            f' {sorted(replacement_targets)} ({field_count} fields).')

    super().__init__(text, entity_type.file_context, 48, MAX_RANK - field_count)


class SmallFieldDeviationWarning(ValidationWarning):
  """Two types have similar field sets but don't inherit from each other."""

  def __init__(self,
               entity_type,
               parents,
               parent_size,
               field_diff,
               key,
               is_master=False):
    diff_str = [MakeFieldString(field) for field in field_diff]

    field_score = (len(entity_type.local_field_names) +
                   len(entity_type.inherited_field_names)) / len(field_diff)
    # pylint: disable=line-too-long
    t = (
        f'Entity types "{entity_type.typename}"'
        f' ({len(set(entity_type.local_field_names.keys()) | set(entity_type.inherited_field_names.keys()))} fields)'
        f' and "{sorted(parents)}" ({parent_size} fields) differ'
        f' by:\n\t\t{sorted(diff_str)}'
    )

    super().__init__(t, entity_type.file_context, 49, MAX_RANK - field_score,
                     key, is_master)


class SuggestParentCreationWarning(ValidationWarning):
  """This set of fields could be turned into a common parent."""

  def __init__(self, entity_type, field_list, set_name, match_list):
    text = (f'Entity type "{entity_type.typename}" and {len(match_list)} other '
            f'types contain {len(field_list)} common fields\n\t{set_name}: '
            f'{str(field_list)}\n\tOther types are:\n\t{match_list}')
    super().__init__(text, entity_type.file_context, 70)


# ---------------------------------------------------------------------------- #
# Backwards Compatibility Findings
# ---------------------------------------------------------------------------- #


class RemovedNamespaceWarning(ValidationWarning):
  """A namespace that used to have non-abstract types was removed."""

  def __init__(self, context, ns_name, disappearing_types):
    super().__init__(
        (f'Namespace {ns_name}, defined in\n\t<{context.filepath}>\nhas been'
         ' removed, causing the following types to'
         f' disappear:\n\t[{disappearing_types}]'), context)


class RemovedTypeWarning(ValidationWarning):
  """A non-abstract type was removed."""

  def __init__(self, entity_type):
    super().__init__(
        (f'Entity type {entity_type.typename}, defined in\n'
         f'\t<{entity_type.file_context.filepath}>\n'
         'has been removed.\n'), entity_type.file_context, 7)


class RemovedFieldWarning(ValidationWarning):
  """A field was removed from a non-abstract type."""

  def __init__(self, entity_type, field_name):
    super().__init__(
        f'Field {field_name} of non-abstract type {entity_type.typename} has '
        'been removed.', entity_type.file_context, 5)


class AddedFieldWarning(ValidationWarning):
  """A field was removed added to a non-abstract type."""

  def __init__(self, entity_type, field_name):
    super().__init__(
        f'Field {field_name} of non-abstract type {entity_type.typename} has '
        'been added.', entity_type.file_context, 6)


class SuppressedFindingsWarning(ValidationWarning):
  """Findings on unchanged types have been suppressed in the results."""

  def __init__(self, number_suppressed):
    super().__init__(
        f'{number_suppressed} warnings from unchanged files were suppressed',
        FileContext(''), 1)


# ---------------------------------------------------------------------------- #
# Exceptions thrown inside the validation process logic.
# ---------------------------------------------------------------------------- #


class ProcessError(Exception):
  """Base level exception class."""


class ReadProcessError(ProcessError):
  """File can't be read."""

  def __init__(self, filepath):
    super().__init__(f"'{filepath}' can't be opened.")


class NonexistentEntityProcessError(ProcessError):
  """Entity type does not exist in configuration."""


class InheritanceCycleProcessError(ProcessError):
  """Cycle detected in the type inheritance graph."""
