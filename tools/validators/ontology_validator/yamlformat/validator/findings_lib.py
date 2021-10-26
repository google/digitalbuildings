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
import copy
import operator

MAX_RANK = 1000000000  # A big number, but not so big it breaks sorting
MISSING_PARENT_VALIDATION_RANK = 60


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
  field_str += '{0}/{1}{2}'.format(field.field.namespace, field.field.field,
                                   field.field.increment)
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
  """Wrapper class to store file-related information.

  Args:
    filepath: string. relative path to the file with the issue.
    begin_line_number: optional int. Starting line number for the issue.
    end_line_number: optional int. Ending line number for the issue.
  """

  def __init__(self, filepath, begin_line_number=None, end_line_number=None):
    self.begin_line_number = begin_line_number
    self.end_line_number = end_line_number
    self.raw_filepath = filepath
    self.filepath = filepath

  def GetLineInfo(self):
    """Returns string containing the line number information.

    If no line number info, returns empty string.
    """
    if self.begin_line_number and self.end_line_number:
      return '(Lines {0} - {1})'.format(self.begin_line_number,
                                        self.end_line_number)
    if self.begin_line_number:
      return '(Line {0})'.format(self.begin_line_number)

    return ''


class Finding(object):
  """Virtual class for findings.

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

  def __init__(self,
               message: str,
               file_context: 'FileContext',
               type_rank: int = MAX_RANK,
               category_rank: int = MAX_RANK,
               inner_rank: int = MAX_RANK,
               equality_key: str = None,
               is_master: bool = False):
    super(Finding, self).__init__()

    if not isinstance(message, str):
      raise TypeError('Argument {0} is not a string'.format(message))
    if file_context is not None:
      if not isinstance(file_context, FileContext):
        raise TypeError(
            'Argument {0} is not a FileContext object.'.format(file_context))

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
      raise TypeError('Argument "{0}" is not an instance of the base classes '
                      'ValidationError or ValidationWarning.'.format(finding))

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

  def HasFindingTypes(self, finding_types):
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

  Args:
    folders: list of ConfigFolder objects parsed from field files.
  Attributes:
    folders: list of ConfigFolder objects parsed from field files.  Each
      universe corresponds to a particular type of ontology item.
  """

  def __init__(self, folders):
    super(FindingsUniverse, self).__init__()
    self.folders = folders
    self._namespace_map = self._MakeNamespaceMap(
        [folder.local_namespace for folder in folders])

  def _MakeNamespaceMap(self, namespaces):
    """Returns mapping from namespace strings to sets of valid ontology entities.

    Args:
      namespaces: list of namespace objects.
    """
    return {ns.namespace: self._GetNamespaceMapValue(ns) for ns in namespaces}

  def _GetNamespaceMapValue(self, namespace):
    """Override in the subclass to define how values in the namespace map are populated."""
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
    super(ValidationError,
          self).__init__('{0}: {1}\n'.format(error_info, message), file_context,
                         1, category_rank, inner_rank)


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
    super(ValidationWarning,
          self).__init__('{0}: {1}\n'.format(warning_info,
                                             message), file_context, 2,
                         category_rank, inner_rank, equality_key, is_master)


class DuplicateDefinitionError(ValidationError):
  """Base class for errors that represent the same component name being defined
  more than once.

  Args:
      component_type: The entity type of the component defined in DBO.
      namespace: Namespace for component_type.
      component_name: Component's name as a string.
      context: Instance of FileContext class for the duplicate item.
      prev_context: Instance of FileContext class for originally defined item.

  Returns:
    An instance of the DuplicateDefinitionError.
  """

  def __init__(self, component_type, namespace, component_name, context,
               prev_context):
    file_info = ''
    if prev_context:
      file_info = '<{0}> {1}'.format(prev_context.filepath,
          prev_context.GetLineInfo())
    super(DuplicateDefinitionError, self).__init__(
        '{0} "{1}/{2}" was already defined in:\n\t{3}'.format(
            component_type, namespace.namespace, component_name, file_info),
        context)


# TODO(berkoben): After migrating to yaml, need to add more context to locate
# errors, because line number info will be lost.


# ---------------------------------------------------------------------------- #
# Errors relating to files.
# ---------------------------------------------------------------------------- #
class InconsistentFileLocationError(ValidationError):
  """File not located within a subfolder inside resources."""

  def __init__(self, expected_path, file_context):
    fp = file_context.filepath
    super(InconsistentFileLocationError, self).__init__(
        'File "{0}" is not at the expected path "{1}".'.format(
            fp, expected_path), file_context)


# ---------------------------------------------------------------------------- #
# Errors relating to config text (typos)
# ---------------------------------------------------------------------------- #
class DuplicateKeyError(ValidationError):
  """Config contains two identical keys."""

  def __init__(self, key, context):
    super(DuplicateKeyError, self).__init__(
        'Key "{0}" cannot appear multiple times in the same mapping.'.format(
            key), context)


class IllegalKeyTypeError(ValidationError):
  """Config contains a key of an invalid non-string type."""

  def __init__(self, key, context):
    super(IllegalKeyTypeError, self).__init__(
        'Expected mapping key "{0}" to be a string; found {1}.'.format(
            key, type(key)), context)


class UnrecognizedKeyError(ValidationError):
  """Config contains an unexpected mapping key."""

  def __init__(self, content, context):
    super(UnrecognizedKeyError, self).__init__(
        '"{0}" is not recognized as a valid mapping key here.'.format(
            str(content)), context)


class EmptyBlockWarning(ValidationWarning):
  """Mapping value is empty."""

  def __init__(self, key, context):
    super(EmptyBlockWarning,
          self).__init__('Mapping for "{0}" has no content.'.format(str(key)),
                         context)


class EmptyFileWarning(ValidationWarning):
  """Validator found an empty YAML file."""

  def __init__(self, context):
    super(EmptyFileWarning,
          self).__init__('YAML file is empty.', context)


# ---------------------------------------------------------------------------- #
# Errors relating to Fields.
# ---------------------------------------------------------------------------- #
class InvalidFieldNameError(ValidationError):
  """An entity type name does not match the accepted format.

  Args:
    name: The field name.
    context: Instance of FileContext for the field defined in DBO.
  """

  def __init__(self, name, context):
    super(InvalidFieldNameError, self).__init__(
        'Field name "{0}" is not valid. It must contain only lowercase letters,'
        ' digits, and underscores. The first character of the name and the'
        ' first character after each underscore must be a letter.'.format(
            name), context)


class DuplicateSubfieldError(ValidationError):
  """Field has more than one identical subfield."""

  def __init__(self, subfield, field):
    super(DuplicateSubfieldError, self).__init__(
        'Field "{0}" is not allowed to contain subfield "{1}" more than once.'
        .format(field.name, subfield), field.file_context)


class UnrecognizedSubfieldError(ValidationError):
  """Field references an unrecognized subfield."""

  def __init__(self, subfield, field):
    super(UnrecognizedSubfieldError, self).__init__(
        'Field "{0}" references unrecognized subfield "{1}".'.format(
            field.name, subfield), field.file_context)


class InvalidFieldConstructionError(ValidationError):
  """One or more subfield in this field is in the wrong location / order."""

  def __init__(self, field):
    super(InvalidFieldConstructionError, self).__init__(
        'Field "{0}" contains subfields in an incorrect order or is missing a '
        'required subfield.'.format(field.name), field.file_context)


class DuplicateFieldDefinitionError(DuplicateDefinitionError):
  """Field is defined multiple times in a namespace.

     Args:
        namespace: Defined namespace of the duplciated field.
        current_instance: Instance of FileContext class for duplicate field.
        prev_context: Instance of FileContext class for duplicated field.
  """

  def __init__(self, namespace, current_instance, prev_context):
    super(DuplicateFieldDefinitionError, self).__init__('Field',
        namespace, current_instance.name, current_instance.file_context,
        prev_context)


class InvalidFieldFormatError(ValidationError):
  """The field's YAML specification is invalid.

  The complete YAML specification of a field and its properties does not have
  proper formatting and couldn't be parsed.
  """

  def __init__(self, key, context):
    super(InvalidFieldFormatError, self).__init__(
        'Field "{0}" definition has an invalid format; expected only a sequence'
        ' of state names.'.format(str(key)), context)


class InvalidStateFormatError(ValidationError):
  """A state string in a field's state list does not have proper formatting."""

  def __init__(self, state, field):
    super(InvalidStateFormatError, self).__init__(
        'State "{0}" in list for field "{1}" has an invalid format.'.format(
            state, field.name), field.file_context)


class DuplicateStateError(ValidationError):
  """A state appears multiple times in a field's state list."""

  def __init__(self, state, field):
    super(DuplicateStateError, self).__init__(
        'Field "{0}" references state "{1}" more than once.'.format(
            field.name, state), field.file_context)


class UnrecognizedStateError(ValidationError):
  """Field references an unrecognized state.

     Args:
        state: Instance of State class for unrecognized state.
        Field: Instance of Field class for field referencing unrecognized state.
  """

  def __init__(self, state, field):
    super(UnrecognizedStateError, self).__init__(
        'Field "{0}" references unrecognized state "{1}".'.format(
            field.name, state), field.file_context)


# ---------------------------------------------------------------------------- #
# Errors relating to Subfields.
# ---------------------------------------------------------------------------- #
class InvalidSubfieldNameError(ValidationError):
  """A subfield name does not match the accepted format.
  
     Args:
        name: Current name of the incorrectly named subfield.
        context: Instance of FileContext class for subfield.
  """

  def __init__(self, name, context):
    super(InvalidSubfieldNameError, self).__init__(
        'Subfield name "{0}" is not valid. It must contain only lowercase '
        'letters and digits, and it must begin with a letter.'.format(
            name), context)


class DuplicateSubfieldDefinitionError(DuplicateDefinitionError):
  """Subfield is defined multiple times in a namespace."""

  def __init__(self, namespace, current_instance, prev_context):
    super(DuplicateSubfieldDefinitionError, self).__init__('Subfield',
        namespace, current_instance.name, current_instance.file_context,
        prev_context)


class MissingSubfieldDescriptionWarning(ValidationWarning):
  """Subfield description is empty.
      
     Args:
        subfield_name: Name of subfield as a string.
        context: Instance of FileContext class for subfield.
  """

  def __init__(self, subfield_name, context):
    super(MissingSubfieldDescriptionWarning, self).__init__(
        'Subfield "{0}" description is empty.'.format(subfield_name),
        context, 10)


class MissingUnitError(ValidationError):
  """Measurement subfield has no corresponding unit definitions."""

  def __init__(self, subfield):
    super(MissingUnitError, self).__init__(
        'Measurement subfield "{0}" has no corresponding unit definitions in the same namespace.'
        .format(subfield.name), subfield.file_context)


# ---------------------------------------------------------------------------- #
# Errors relating to States.
# ---------------------------------------------------------------------------- #
class InvalidStateNameError(ValidationError):
  """A state name does not match the accepted format.

     Args:
        name: State name as a string.
        context: Instance of FileContext for invalid state name.
  """

  def __init__(self, name, context):
    super(InvalidStateNameError, self).__init__(
        'State name "{0}" is not valid. It must contain only uppercase '
        'letters and underscores, and it must begin with a letter.'.format(
            name), context)


class DuplicateStateDefinitionError(DuplicateDefinitionError):
  """A state is defined multiple times in a namespace."""

  def __init__(self, namespace, current_instance, prev_context):
    super(DuplicateStateDefinitionError, self).__init__('State',
        namespace, current_instance.name, current_instance.file_context,
        prev_context)


class MissingStateDescriptionWarning(ValidationWarning):
  """State description is empty."""

  def __init__(self, state):
    super(MissingStateDescriptionWarning, self).__init__(
        'State "{0}" description is empty.'.format(state.name),
        state.file_context, 10)


# ---------------------------------------------------------------------------- #
# Errors relating to Connections.
# ---------------------------------------------------------------------------- #
class InvalidConnectionNameError(ValidationError):
  """A connection name does not match the accepted format."""

  def __init__(self, name, context):
    super(InvalidConnectionNameError, self).__init__(
        'Connection name "{0}" is not valid. It must contain only uppercase '
        'letters and underscores, and it must begin with a letter.'.format(
            name), context)


class DuplicateConnectionDefinitionError(DuplicateDefinitionError):
  """A connection is defined multiple times in a namespace."""

  def __init__(self, namespace, current_instance, prev_context):
    super(DuplicateConnectionDefinitionError, self).__init__('Connection',
        namespace, current_instance.name, current_instance.file_context,
        prev_context)


class InvalidConnectionNamespaceError(ValidationError):
  """A connection is defined outside the global namespace."""

  def __init__(self, namespace_name, context):
    super(InvalidConnectionNamespaceError, self).__init__(
        'Namespace "{0}" contains connection definitions; connections are only '
        'allowed in the global namespace.'.format(namespace_name), context)


class MissingConnectionDescriptionWarning(ValidationWarning):
  """Connection description is empty.

     Args:
        connection: Instance of Connection class missing a description.
  """

  def __init__(self, connection):
    super(MissingConnectionDescriptionWarning, self).__init__(
        'Connection "{0}" description is empty.'.format(connection.name),
        connection.file_context, 10)


# ---------------------------------------------------------------------------- #
# Errors relating to Units.
# ---------------------------------------------------------------------------- #
class InvalidUnitNameError(ValidationError):
  """A unit name does not match the accepted format.
  
     Args:
        name: Invalid name as a string.
        context: Instance of FileContext for invalid unit name.
  """

  def __init__(self, name, context):
    super(InvalidUnitNameError, self).__init__(
        'Unit name "{0}" is not valid. It must contain only lowercase '
        'letters and underscores, and it must begin with a letter.'.format(
            name), context)


class DuplicateUnitDefinitionError(DuplicateDefinitionError):
  """A unit is defined multiple times in a namespace.

     Args:
        namespace: Defined namespace for unit as a string.
        current_instance: Instance of FileContext class for duplicate unit.
        prev_context: Instance of FileContext class for unit. 
  """

  def __init__(self, namespace, current_instance, prev_context):
    super(DuplicateUnitDefinitionError, self).__init__('Unit',
        namespace, current_instance.name, current_instance.file_context,
        prev_context)


class InvalidUnitFormatError(ValidationError):
  """A unit's YAML specification is invalid.

     Args:
       key: YAML specification for unit.
       context: Instance of FileContext class for unit.
  """

  def __init__(self, key, context):
    super(InvalidUnitFormatError, self).__init__(
        'Unit "{0}" definition has an invalid format; expected only a single '
        'unit name and tag.'.format(str(key)), context)


class UnknownUnitTagError(ValidationError):
  """A unit entry has an unknown tag."""

  def __init__(self, unit_name, tag, context):
    super(UnknownUnitTagError, self).__init__(
        'Unit "{0}" has an unrecognized tag "{1}".'.format(unit_name, tag),
        context)


class StandardUnitCountError(ValidationError):
  """A measurement type does not have exactly one unit tagged as standard."""

  def __init__(self, measurement_type, tag_count, context):
    super(StandardUnitCountError, self).__init__(
        'Measurement type "{0}" has {1} units tagged as standard. Expected 1.'
        .format(measurement_type, tag_count), context)


class UnknownMeasurementTypeError(ValidationError):
  """A unit has an unknown measurement type."""

  def __init__(self, unit):
    super(UnknownMeasurementTypeError, self).__init__(
        'Unit "{0}" is defined under the unrecognized measurement type "{1}".'
        .format(unit.name, unit.measurement_type), unit.file_context)


# ---------------------------------------------------------------------------- #
# Errors on the level of individual entity types.
# ---------------------------------------------------------------------------- #
class MissingTypenameError(ValidationError):
  """Typename is empty."""

  def __init__(self, entity_type):
    super(MissingTypenameError, self).__init__('Missing typename.',
                                               entity_type.file_context)


class InvalidTypenameError(ValidationError):
  """An entity type name does not match the accepted format.

     Args:
        name: Invalid type name as a string.
        context: Instance of FileContext class for type name.
  """

  def __init__(self, name, context):
    super(InvalidTypenameError, self).__init__(
        'Entity type name "{0}" is not valid. It must contain only letters, '
        'digits, and underscores, and it must begin with a letter.'.format(
            name), context)


class IllegalFieldIncrementError(ValidationError):
  """Field is incremented unnecessarily."""

  def __init__(self, entity_type, field_name):
    super(IllegalFieldIncrementError, self).__init__(
        'Field {0} of {1} is incremented but there are no other increments of '
        'the same base field on this entity.'.format(
            field_name, entity_type.typename), entity_type.file_context)


class IllegalFieldIncrementWarning(ValidationError):
  """Field is incremented unnecessarily."""

  def __init__(self, entity_type, field_name):
    super(IllegalFieldIncrementWarning, self).__init__(
        'Field {0} of {1} is incremented but there are no other increments of '
        'the same base field on this entity.'.format(
            field_name, entity_type.typename), entity_type.file_context)


class MissingEntityTypeDescriptionWarning(ValidationWarning):
  """Entity type description is empty."""

  def __init__(self, entity_type):
    super(MissingEntityTypeDescriptionWarning, self).__init__(
        'Entity type "{0}" description is empty.'.format(entity_type.typename),
        entity_type.file_context, 20)


class DuplicateFieldError(ValidationError):
  """Duplicate fields defined within an entity type."""

  def __init__(self, entity_type, field):
    super(DuplicateFieldError, self).__init__(
        'Entity type "{0}" defines field "{1}" multiple times.'.format(
            entity_type.typename, field), entity_type.file_context)


class UndefinedFieldError(ValidationError):
  """Field is undefined."""

  def __init__(self, entity_type, field):
    super(UndefinedFieldError, self).__init__(
      'Entity type "{0}" references unrecognized field "{1}".'.format(
        entity_type.typename, field), entity_type.file_context)


class UnrecognizedFieldFormatError(ValidationError):
  """Declared field has incorrect format."""

  def __init__(self, entity_type, field):
    super(UnrecognizedFieldFormatError, self).__init__(
        'Field name "{0}" has incorrect formatting. The format should be '
        'either "<fieldname>" or "<namespace>/<fieldname>".'.format(field),
        entity_type.file_context)


class UnrecognizedParentFormatError(ValidationError):
  """Declared parent has incorrect format."""

  def __init__(self, entity_type, parent_name):
    super(UnrecognizedParentFormatError, self).__init__(
        'Parent name "{0}" has incorrect formatting. The format should be '
        'either "<parent_name>" or "<namespace>/<parent_name>".'.format(
            parent_name), entity_type.file_context)


class DuplicateParentError(ValidationError):
  """Entity has duplicate parent ids defined."""

  def __init__(self, entity_type, parent_name):
    super(DuplicateParentError, self).__init__(
        'Entity type "{0}" references "{1}" as a parent type more than once.'
        .format(entity_type.typename, parent_name), entity_type.file_context)


class InheritedFieldsSetError(ValidationError):
  """The inherited_fields_set field is set."""

  def __init__(self, entity_type):
    super(InheritedFieldsSetError,
          self).__init__('Inherited_fields_expanded should not be set.',
                         entity_type.file_context)


# ---------------------------------------------------------------------------- #
# Errors on the level of namespaces.
# ---------------------------------------------------------------------------- #
class NonexistentParentError(ValidationError):
  """Parent id specified by a type does not exist."""

  def __init__(self, entity_type, parent_name):
    super(NonexistentParentError, self).__init__(
        'Entity type "{0}" references unrecognized parent type "{1}".'.format(
            entity_type.typename, parent_name), entity_type.file_context)


class InheritanceCycleError(ValidationError):
  """Cycle detected in the type inheritance graph."""

  def __init__(self, entity_type, parent_name):
    super(InheritanceCycleError, self).__init__(
        'Inheritance cycle detected between entity types "{0}" and "{1}".'
        .format(entity_type.typename, parent_name), entity_type.file_context)



class DuplicateEntityTypeDefinitionError(DuplicateDefinitionError):
  """Duplicate type names defined within the same namespace."""

  def __init__(self, namespace, current_instance, prev_context):
    super(DuplicateEntityTypeDefinitionError, self).__init__('Entity type',
        namespace, current_instance.typename, current_instance.file_context,
        prev_context)


class DuplicateIdsError(ValidationError):
  """Duplicate type IDs defined."""

  def __init__(self, namespace, entity_type, mapped_entity_type):
    super(DuplicateIdsError, self).__init__(
        'Duplicate type IDs are not allowed. Entity type name "{0}" '
        'within namespace "{1}" with ID "{4}" was already defined in \n'
        '\t<{2}> (Line {3}).'.format(
            entity_type.typename, namespace,
            mapped_entity_type.file_context.filepath,
            mapped_entity_type.file_context.begin_line_number, entity_type.uid),
        entity_type.file_context)


class DuplicateLocalFieldSetsWarning(ValidationWarning):
  """Two types declare the exact same local field sets."""

  def __init__(self, entity_type, dup_entity_types):
    field_list = list(entity_type.local_field_names)
    field_list.sort()
    fieldstr = ''
    for f in field_list:
      fieldstr += '\n\t\t' + f
    t = 'Entity type "{0}" has the same local {1} field set:{2}\n\tas:\n'.format(
        entity_type.typename, len(entity_type.local_field_names), fieldstr)

    for dup in dup_entity_types:
      t += '\t\t<{0}> in {1}\n'.format(dup.typename, dup.file_context.filepath)
    key_arr = dup_entity_types.copy()
    key_arr.append(entity_type)
    super(DuplicateLocalFieldSetsWarning,
          self).__init__(t, entity_type.file_context, 40,
                         MAX_RANK - len(field_list), frozenset(key_arr),
                         entity_type.is_canonical)


class DuplicateExpandedFieldSetsWarning(ValidationWarning):
  """Two types have the exact same expanded field sets."""

  def __init__(self, entity_type, dup_entity_typenames, equality_key):
    field_count = len(
        set(entity_type.local_field_names.keys())
        | set(entity_type.inherited_field_names.keys()))
    text = 'Entity type "{0}" has the same expanded set of {1} fields as:\n'.format(
        entity_type.typename, field_count)

    for typename in dup_entity_typenames:
      text += '\t<{0}> with {1} optionality changes\n'.format(
          typename, dup_entity_typenames[typename])

    text += '\tAre they the same type?'
    super(DuplicateExpandedFieldSetsWarning,
          self).__init__(text, entity_type.file_context, 30,
                         MAX_RANK - len(dup_entity_typenames), equality_key,
                         entity_type.is_canonical)


class OverlappingFlexTypeChildWarning(ValidationWarning):
  """A type can be represented by a larger, flexible type."""

  def __init__(self, entity_type, best_diff, dup_entity_typenames):
    field_count = len(
        set(entity_type.local_field_names.keys())
        | set(entity_type.inherited_field_names.keys()))
    text = 'Entity type "{0}" with {1} fields can be represented by flex-types:\n'.format(
        entity_type.typename, field_count)

    for typename in dup_entity_typenames:
      text += '\t<{0}>\n\t\tUnmatched Optional:\n'.format(typename)
      for field in dup_entity_typenames[typename]:
        text += '\t\t\t{0}\n'.format(field)

    super(OverlappingFlexTypeChildWarning,
          self).__init__(text, entity_type.file_context, 32,
                         MAX_RANK - field_count + best_diff)


class OverlappingFlexTypeParentWarning(ValidationWarning):
  """A flexible type can represent another, smaller type."""

  def __init__(self, entity_type, dup_entity_typenames):
    field_count = len(
        set(entity_type.local_field_names.keys())
        | set(entity_type.inherited_field_names.keys()))
    text = 'flex-type "{0}" with {1} fields can represent:\n'.format(
        entity_type.typename, field_count)

    for typename in dup_entity_typenames:
      text += '\t<{0}>\n\t\tUnmatched Optional:\n'.format(typename)
      for field in dup_entity_typenames[typename]:
        text += '\t\t\t{0}\n'.format(field)

    super(OverlappingFlexTypeParentWarning,
          self).__init__(text, entity_type.file_context, 31,
                         MAX_RANK - len(dup_entity_typenames))


class PossibleOverlappingFlexTypeChildWarning(ValidationWarning):
  """A type can ALMOST be represented by a larger, flexible type."""

  def __init__(self, entity_type, best_diff, dup_entity_typenames):
    field_count = len(
        set(entity_type.local_field_names.keys())
        | set(entity_type.inherited_field_names.keys()))
    text = 'Entity type "{0}" with {1} fields can ALMOST be represented by flex-types:\n'.format(
        entity_type.typename, field_count)

    for typename in dup_entity_typenames:
      text += '\t<{0}> \n\t\tUnmatched required:\n'.format(typename)
      for field in dup_entity_typenames[typename]:
        text += '\t\t\t{0}\n'.format(field)

    super(PossibleOverlappingFlexTypeChildWarning,
          self).__init__(text, entity_type.file_context, 34,
                         MAX_RANK - field_count + best_diff)


class PossibleOverlappingFlexTypeParentWarning(ValidationWarning):
  """A flexible type ALMOST can represent another, smaller type."""

  def __init__(self, entity_type, dup_entity_typenames):
    field_count = len(
        set(entity_type.local_field_names.keys())
        | set(entity_type.inherited_field_names.keys()))
    text = ('flex-type "{0}" with {1} fields can ALMOST represent:\n').format(
        entity_type.typename, field_count)

    for typename in dup_entity_typenames:
      text += '\t<{0}>\n\t\tUnmatched Required:\n'.format(typename)
      for field in dup_entity_typenames[typename]:
        text += '\t\t\t{0}\n'.format(field)

    super(PossibleOverlappingFlexTypeParentWarning,
          self).__init__(text, entity_type.file_context, 33,
                         MAX_RANK - len(dup_entity_typenames))


# ---------------------------------------------------------------------------- #
# Type Management Findings
# ---------------------------------------------------------------------------- #


class MissingParentWarning(ValidationWarning):
  """This type could use inhheritance to decrease its local field count.

  Args:
    typenames: list of typenames that contain the field subset.
    set)size: Number of fields in the subset.
    qualified_parents: list of qualified names of types that have exactly the
      fields in the subset.
    context: file context to attach this finding to (for sorting later).
    sum_match_quality: sum of match qualities for the subset to all types in
      typenames.
    curation_bonus: Set true if parents are curated types. Improves sort rank.
    key: comparison object to use when comparing to other findings for
      deduplication.
  """

  def __init__(self, typenames, set_size, qualified_parents, context,
               sum_match_quality, curation_bonus, key):
    text = 'Entity types {0} all contain {2}. Size: {1}. Average Quality: {3:0.2f}'.format(
        str(sorted(typenames)), set_size, str(sorted(qualified_parents)),
        sum_match_quality / len(typenames))

    rank = MISSING_PARENT_VALIDATION_RANK
    if curation_bonus:
      rank -= 1

    # Arbitrary score that attempts to rank results by a combination of: the
    # fraction of free fields they replace, the number of types that have the
    # replacement and how big the replacement is.
    match_score = sum_match_quality + len(typenames) * set_size / 25
    super(MissingParentWarning,
          self).__init__(text, context, rank, MAX_RANK - match_score, key,
                         False)


class UnusedParentWarning(ValidationWarning):
  """This type could be a parent of one or more other types."""

  def __init__(self, entity_type, qualified_children, sum_match_quality, key):
    field_count = len(entity_type.local_field_names) + len(
        entity_type.inherited_field_names)
    text = 'Entity type "{0}" with {1} fields is contained within {2} types:\n\t{3}'.format(
        entity_type.typename, field_count, len(qualified_children),
        str(sorted(qualified_children)))

    # Arbitrary score that attempts to rank results by a combination of: the
    # fraction of free fields they replace, the number of types that have the
    # replacement and how big the replacement is.
    match_score = sum_match_quality + len(qualified_children) * field_count / 25
    super(UnusedParentWarning, self).__init__(text, entity_type.file_context,
                                              MISSING_PARENT_VALIDATION_RANK,
                                              MAX_RANK - match_score, key, True)


class PotentialParentReplacementWarning(ValidationWarning):
  """The inheritance of this type could be simplified."""

  def __init__(self, entity_type, field_count, qualified_parents,
               replaced_parents):
    text = 'Entity type "{0}" can replace parents {1} with one of {2} ({3} fields).'.format(
        entity_type.typename, str(sorted(replaced_parents)),
        str(sorted(qualified_parents)), field_count)

    super(PotentialParentReplacementWarning,
          self).__init__(text, entity_type.file_context, 50,
                         MAX_RANK - field_count)


class ParentReplacementCandidateWarning(ValidationWarning):
  """This type could simplify the inheritance of another type(s)."""

  def __init__(self, entity_type, field_count, replacement_targets):
    field_count = len(entity_type.local_field_names) + len(
        entity_type.inherited_field_names)
    text = 'Entity type "{0}" replaces multiple parents in {1} ({2} fields).'.format(
        entity_type.typename, str(sorted(replacement_targets)), field_count)

    super(ParentReplacementCandidateWarning,
          self).__init__(text, entity_type.file_context, 48,
                         MAX_RANK - field_count)


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
    t = 'Entity types "{0}" ({1} fields) and "{2}" ({3} fields) differ by:\n\t\t{4}'.format(
        entity_type.typename,
        len(
            set(entity_type.local_field_names.keys())
            | set(entity_type.inherited_field_names.keys())),
        str(sorted(parents)), parent_size, str(sorted(diff_str)))

    super(SmallFieldDeviationWarning,
          self).__init__(t, entity_type.file_context, 49,
                         MAX_RANK - field_score, key, is_master)


class SuggestParentCreationWarning(ValidationWarning):
  """This set of fields could be turned into a common parent."""

  def __init__(self, entity_type, field_list, set_name, match_list):
    text = ('Entity type "{0}" and {1} other types contain {2} common fields\n'
            '\t{3}: {4}\n'
            '\tOther types are:\n'
            '\t{5}').format(entity_type.typename, len(match_list),
                            len(field_list), set_name, str(field_list),
                            str(match_list))
    super(SuggestParentCreationWarning,
          self).__init__(text, entity_type.file_context, 70)


# ---------------------------------------------------------------------------- #
# Backwards Compatibility Findings
# ---------------------------------------------------------------------------- #


class RemovedNamespaceWarning(ValidationWarning):
  """A namespace that used to have non-abstract types was removed."""

  def __init__(self, context, ns_name, disappearing_types):
    super(RemovedNamespaceWarning, self).__init__(
        'Namespace {0}, defined in\n'
        '\t<{1}>\n'
        'has been removed, causing the following types to disappear:\n'
        '\t[{2}]'.format(ns_name, context.filepath, str(disappearing_types)),
        context)


class RemovedTypeWarning(ValidationWarning):
  """A non-abstract type was removed."""

  def __init__(self, entity_type):
    super(RemovedTypeWarning, self).__init__(
        'Entity type {0}, defined in\n'
        '\t<{1}>\n'
        'has been removed.\n'.format(entity_type.typename,
                                     entity_type.file_context.filepath),
        entity_type.file_context, 7)


class RemovedFieldWarning(ValidationWarning):
  """A field was removed from a non-abstract type."""

  def __init__(self, entity_type, field_name):
    super(RemovedFieldWarning, self).__init__(
        'Field {0} of non-abstract type {1} has been removed.'.format(
            field_name, entity_type.typename), entity_type.file_context, 5)


class AddedFieldWarning(ValidationWarning):
  """A field was removed added to a non-abstract type."""

  def __init__(self, entity_type, field_name):
    super(AddedFieldWarning, self).__init__(
        'Field {0} of non-abstract type {1} has been added.'.format(
            field_name, entity_type.typename), entity_type.file_context, 6)


class SuppressedFindingsWarning(ValidationWarning):
  """Findings on unchanged types have been suppressed in the results."""

  def __init__(self, number_suppressed):
    super(SuppressedFindingsWarning, self).__init__(
        '{0} warnings from unchanged files were suppressed'.format(
            number_suppressed), FileContext(''), 1)


# ---------------------------------------------------------------------------- #
# Exceptions thrown inside the validation process logic.
# ---------------------------------------------------------------------------- #


class ProcessError(Exception):
  """Base level exception class."""
  pass


class ReadProcessError(ProcessError):
  """File can't be read."""

  def __init__(self, filepath):
    super(ReadProcessError,
          self).__init__("'{0}' can't be opened.".format(filepath))


class NonexistentEntityProcessError(ProcessError):
  """Entity type does not exist in configuration."""
  pass


class InheritanceCycleProcessError(ProcessError):
  """Cycle detected in the type inheritance graph."""
  pass
