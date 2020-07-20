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

"""Classes and methods for working with entity types in the ontology."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import re
import typing

from yamlformat.validator import base_lib
from yamlformat.validator import config_folder_lib
from yamlformat.validator import field_lib
from yamlformat.validator import findings_lib

ENTITY_TYPE_NAME_REGEX = re.compile(
    r'^[a-zA-Z]+[a-zA-Z0-9]*(?:_[a-zA-Z0-9]+)*$')
FIELD_INCREMENT_STRIPPER_REGEX = re.compile(
    r'(^[a-z]+[a-z0-9]*(?:_[a-z]+[a-z0-9]*)*)((?:_[0-9]+)+)$')

FieldParts = typing.NamedTuple(
    'FieldParts',
    [('namespace', str), ('field', str), ('increment', str)])
OptWrapper = typing.NamedTuple('OptWrapper', [('field', FieldParts),
                                              ('optional', bool)])
TypeParts = typing.NamedTuple('TypeParts', [('namespace', str),
                                            ('typename', str)])
EntityIdByEntry = typing.NamedTuple(
    'EntityIdByEntry', [('namespace', str), ('typename', str)])


class EntityTypeUniverse(findings_lib.Findings):
  """Helper class to represent the defined universe of EntityTypes.

  Only contains valid EntityTypes.

  Attributes;
    namespace_folder_map: a map of namespace names to EntityTypeFolders.
    type_namespaces_map: a map of type names to TypeNamespaces.
    type_ids_map: maps type IDs to entity types. Contains all valid types w/IDs

  Args:
    entity_type_folders: list of EntityTypeFolder objects parsed from files.
  """

  def __init__(self, entity_type_folders):
    super(EntityTypeUniverse, self).__init__()
    self.namespace_folder_map = {}
    self._BuildNamespaceFolderMap(entity_type_folders)
    self.type_namespaces_map = {}
    self.type_ids_map = {}
    self._BuildTypeMaps(
        [folder.local_namespace for folder in entity_type_folders])

  def GetEntityType(self, namespace_name, typename):
    """Finds entity_type by namespace and typename and returns it or None."""
    if namespace_name not in self.type_namespaces_map:
      return None
    return self.type_namespaces_map[namespace_name].GetType(typename)

  def GetNamespace(self, namespace_name):
    """Finds namespace in the universe by name and returns it or None."""
    return self.type_namespaces_map.get(namespace_name, None)

  def GetNamespaces(self):
    """Get the entity type namespace objects in this universe.

    Returns:
      A list of EntityTypeNamespace objects
    """
    return list(self.type_namespaces_map.values())

  def _GetDynamicFindings(self, filter_old_warnings):
    findings = []
    for folder in self.namespace_folder_map.values():
      findings += folder.GetFindings(filter_old_warnings)
    return findings

  def _BuildTypeMaps(self, type_namespaces):
    """Creates a dict mapping namespace strings to TypeNamespace objects.

    Sets the self.type_namespaces_map attribute of the class.

    Args:
      type_namespaces: a list of TypeNamespace objects.

    Raises:
      RuntimeError: if assumptions about internal data structures are violated.
    """
    for type_namespace in type_namespaces:
      self.type_namespaces_map[type_namespace.namespace] = type_namespace
      for entity_type in type_namespace.valid_types_map.values():
        if entity_type.uid:
          if entity_type.uid in self.type_ids_map:
            dup_id_entry = self.type_ids_map[entity_type.uid]
            dup_id_type = self.GetEntityType(
                dup_id_entry.namespace, dup_id_entry.typename)
            if dup_id_type is None:
              raise RuntimeError('Duplicate type should always be mapped')
            entity_type.AddFinding(findings_lib.DuplicateIdsError(
                type_namespace.namespace, entity_type, dup_id_type))
            dup_id_type.AddFinding(findings_lib.DuplicateIdsError(
                dup_id_entry.namespace, dup_id_type, entity_type))
          self.type_ids_map[entity_type.uid] = EntityIdByEntry(
              namespace=type_namespace.namespace, typename=entity_type.typename)

  def _BuildNamespaceFolderMap(self, type_folders):
    """Creates a dict mapping namespace strings to EntityTypeFolder objects.

    Sets the self.namespace_folder_map attribute of the class.

    Args:
      type_folders: a list of EntityTypeFolder objects.
    """
    for folder in type_folders:
      self.namespace_folder_map[folder.local_namespace.namespace] = folder


class EntityTypeFolder(config_folder_lib.ConfigFolder):
  """Class representing a namespace folder of entity types.

  Class fully validates all entity types defined within the namespace folder,
    collects issues found, and stores all valid entity types.

  Args:
    folderpath: required string with full path to the folder containing entity
      type files. Path should be relative to google3/ and have no leading or
      trailing /.
    fields_universe: optional FieldsUniverse object.
  Attributes:
    local_namespace: TypeNamespace object representing this namespace.
  """

  def __init__(self, folderpath, fields_universe=None):
    super(EntityTypeFolder, self).__init__(folderpath,
                                           base_lib.ComponentType.ENTITY_TYPE)
    self.local_namespace = TypeNamespace(self._namespace_name, fields_universe)

  def Finalize(self):
    """Call to complete entity creation after all types are added."""
    self.local_namespace.QualifyParentNames()

  def _AddFromConfigHelper(self, document, context):
    for type_name in document:
      new_type = self._ConstructType(type_name, document[type_name],
                                     context.filepath)
      self._AddType(new_type)

  def _ConstructField(self, local_field_names, optional, output_array):
    for field in local_field_names:
      field_ns, field_name = field_lib.SplitFieldName(field)
      increment = ''
      match = FIELD_INCREMENT_STRIPPER_REGEX.match(field_name)
      if match:
        field_name = match.group(1)
        increment = match.group(2)
      # Field will look local if undefined, but we'll catch the error later
      # Because we do explict existence checks and it will fail
      # TODO(berkoben) refactor so validation happens in an order that
      # prevents this logic lint
      field_ns = self.local_namespace.GetQualifiedNamespace(
          field_ns, field_name)
      output_array.append(
          OptWrapper(
              field=FieldParts(
                  namespace=field_ns, field=field_name, increment=increment),
              optional=optional))

  def _ConstructType(self, type_name, type_contents, filepath):
    """Reads a entity type config block and generates an EntityType object."""

    description = ''
    parents = None
    local_field_names = None
    opt_local_field_names = None
    is_abstract = False
    is_canonical = False
    uid = None

    expected_keys = set([
        'description', 'implements', 'uses', 'opt_uses', 'is_abstract', 'id',
        'is_canonical'
    ])

    if 'description' in type_contents:
      description = type_contents['description']
    if 'implements' in type_contents:
      parents = type_contents['implements']
    if 'uses' in type_contents:
      local_field_names = type_contents['uses']
    if 'opt_uses' in type_contents:
      opt_local_field_names = type_contents['opt_uses']
    if 'is_abstract' in type_contents:
      is_abstract = type_contents['is_abstract']
    if 'is_canonical' in type_contents:
      is_canonical = type_contents['is_canonical']
    if 'id' in type_contents:
      uid = type_contents['id']

    # Generate tuples to represent each field
    fq_lfn = []
    if local_field_names:
      self._ConstructField(local_field_names, False, fq_lfn)
    if opt_local_field_names:
      self._ConstructField(opt_local_field_names, True, fq_lfn)

    entity_type = EntityType(
        filepath=filepath,
        typename=type_name,
        description=description,
        parents=parents,
        local_field_tuples=fq_lfn,
        is_abstract=is_abstract,
        inherited_fields_expanded=False,
        is_canonical=is_canonical,
        uid=uid)

    # Add errors to type if there's anything extra in the block.  We add to the
    # entity type because an extra key here is likely a typo in a real key name
    # that would result in information being lost from the type.
    for key in type_contents:
      if key not in expected_keys:
        entity_type.AddFinding(
            findings_lib.UnrecognizedFormatError(key, entity_type.file_context))

    return entity_type

  def _AddType(self, entity_type):
    """Adds entity_type if it is fully valid.

    If formatting is correct, continues on to field validation.
    Records all findings in object.

    Args:
      entity_type: EntityType object.

    Returns:
      True if the entity type was successfully validated and added. False
        otherwise.
    """
    if not entity_type.IsValid():
      self.AddFindings(entity_type.GetFindings())
      return False
    return self.local_namespace.InsertType(entity_type)


class TypeNamespace(findings_lib.Findings):
  """Class representing a namespace of entity types.

  Attributes:
    namespace: string
    valid_types_map: Dict mapping typename strings to EntityType objects.
  """

  def __init__(self, namespace, fields_universe=None):
    super(TypeNamespace, self).__init__()
    self.namespace = namespace
    self._fields_universe = fields_universe
    self.valid_types_map = {}
    self._parents_qualified = False

  def _GetDynamicFindings(self, filter_old_warnings):
    findings = []
    for entity_type in self.valid_types_map.values():
      findings += entity_type.GetFindings(filter_old_warnings)
    return findings

  def GetType(self, typename):
    return self.valid_types_map.get(typename, None)

  def InsertType(self, entity_type):
    """Validate that declared fields are defined.

    Adds type if valid and unique.

    Findings for non-validated fields are applied to this TypeNamespace.

    Args:
      entity_type: entity to attempt to add.

    Returns:
      True if entity was added successfully.

    Raises:
      RuntimeError: if this is called after qualifying parent names
    """
    if self._parents_qualified:
      raise RuntimeError('Cannot add types after Qualifying parents')
    if self._ValidateFields(entity_type):
      typename = entity_type.typename
      mapped_entity_type = self.valid_types_map.get(typename)
      if mapped_entity_type is None:
        self.valid_types_map[typename] = entity_type
        return True
      # entity_type is a duplicate type
      self.AddFinding(
          findings_lib.DuplicateTypesError(self.namespace, entity_type,
                                           mapped_entity_type))
      return False

    return False

  def GetQualifiedNamespace(self, field_ns, field_name):
    """Returns the namespace name for this field.

    Args:
      field_ns: namespace of field as parsed from the config
      field_name: unqualified field name string

    Returns:
      The fully qualified field string.
    """

    if not field_ns and self.IsLocalField(field_name):
      return self.namespace
    return field_ns

  def _BuildQualifiedParentTuple(self, parent_name):
    """Creates the two-part parent tuple with a fully-qualified namespace.

    Args:
      parent_name: string as specified in the config file.
    Returns:
      A TypeParts tuple representing this parent.
    """

    namespace_name = self.namespace
    split = parent_name.split('/')
    if len(split) != 2:
      if not self.GetType(parent_name):
        # parent is in the global namespace
        namespace_name = ''
    else:
      namespace_name = split[0]
      parent_name = split[1]

    return TypeParts(namespace=namespace_name, typename=parent_name)

  def QualifyParentNames(self):
    """Sets parents attribute of this namespace with fully qualified names."""

    if self._parents_qualified:
      return
    for entity_type in self.valid_types_map.values():
      fq_tuplemap = {}
      for parent in entity_type.unqualified_parent_names:
        fq_tuple = self._BuildQualifiedParentTuple(parent)
        fq_name = '{0}/{1}'.format(fq_tuple.namespace, fq_tuple.typename)
        fq_tuplemap[fq_name] = fq_tuple
      entity_type.parent_names = fq_tuplemap
    self._parents_qualified = True

  def IsLocalField(self, fieldname):
    """Returns true if this unqualified field is defined in the namespace.

    Args:
      fieldname: an unqualified fieldname with no leading '/'
    """
    if not self._fields_universe:
      return False
    return self._fields_universe.IsFieldDefined(fieldname, self.namespace)

  def _ValidateFields(self, entity):
    """Validates that all fields declared by entity are defined."""
    # if fields_universe is not defined just return true
    if not self._fields_universe:
      return True

    valid = True
    for field_tuple in entity.local_field_names.values():
      if not self._ValidateField(field_tuple.field, entity):
        valid = False
    return valid

  def _ValidateField(self, field_tuple, entity):
    """Validates that field declared by entity is defined.

    Field formatting has already been validated.
    Findings are saved on the TypeNamespace.

    Args:
      field_tuple: tuple representing a fully qualified field
      entity: EntityType

    Returns:
      True if field is defined.
    """
    if not self._fields_universe.IsFieldDefined(field_tuple.field,
                                                field_tuple.namespace):
      self.AddFinding(findings_lib.UndefinedFieldError(entity,
                                                       field_tuple.field))
      return False
    return True


def _BuildQualifiedField(opt_tuple):
  field_tuple = opt_tuple.field
  return '{0}/{1}{2}'.format(
      field_tuple.namespace, field_tuple.field, field_tuple.increment)


class EntityType(findings_lib.Findings):
  """Creates an EntityType object from a set of values describing the type.

  Args:
    filepath: string. google3 path to the file defining the type.
    begin_line_number: int. Starting line number for the entity type definition.
    typename: required string.
    description: required string.
    parents: list of parent typename strings.
    local_field_tuples: list of OptWrapper tuples
    inherited_fields_expanded: boolean. Should be false at init.
    is_canonical: boolean indicating if this is a curated canonical type.
    uid: the database ID string of this type if uploaded
  Attributes:
    file_context: FileContext object containing file info.
    typename: string.
    description: string.
    parent_names: a list of parent typename strings.
    local_field_names: the local set of standard field names
    inherited_field_names: the set of inherited field names. Is always assigned
      to an empty set at init, to be expanded later.
    inherited_fields_expanded: boolean.
    is_canonical: boolean indicating if this is a curated canonical type.
    uid: the database ID string of this type if uploaded

  Returns:
    An instance of the EntityType class.
  """

  def __init__(self,
               begin_line_number=0,
               filepath='',
               typename='',
               description='',
               parents=None,
               local_field_tuples=None,
               is_abstract=False,
               inherited_fields_expanded=False,
               is_canonical=False,
               uid=None):

    super(EntityType, self).__init__()

    self.file_context = findings_lib.FileContext(
        begin_line_number=begin_line_number, filepath=filepath)
    self.typename = typename
    self.description = description

    self.local_field_names = {}
    local_field_names = []
    if local_field_tuples:
      local_field_names = [
          _BuildQualifiedField(opt_parts) for opt_parts in local_field_tuples
      ]

      for i, lfn in enumerate(local_field_names):
        self.local_field_names[lfn] = local_field_tuples[i]

    self.inherited_field_names = {}
    self.inherited_fields_expanded = inherited_fields_expanded

    if parents is None:
      parents = []
    self.parent_names = None
    self.parent_name_tuples = None
    self.unqualified_parent_names = parents

    self._all_fields = None
    self._has_optional_fields = None

    self.is_abstract = is_abstract
    self.is_canonical = is_canonical
    self.uid = uid

    # TODO(berkoben) update this method to use tuples if possible
    self._ValidateType(local_field_names)

  def HasOptionalFields(self, run_unsafe=False):
    if not (self.inherited_fields_expanded or run_unsafe):
      raise RuntimeError('Type has not been expanded')
    if self._has_optional_fields is not None:
      return self._has_optional_fields
    fields = self.GetAllFields()
    for field in fields.values():
      if field.optional:
        self._has_optional_fields = True
        return self._has_optional_fields
    self._has_optional_fields = False
    return self._has_optional_fields

  def GetAllFields(self, run_unsafe=False):
    """Returns the expanded set of fields for this type.

    Args:
      run_unsafe: set true to run against a type before fields are fully
        expanded.  Running in this mode does not memoize the result.
    Returns:
      A dictionary of fully qualified strings representing fields in the type to
      OptWrapper tuples representing the contents of the field.
    Raises:
      RuntimeError: if fields have not yet been expanded.
    """

    if not (self.inherited_fields_expanded or run_unsafe):
      raise RuntimeError('Type {0} has not been expanded'.format(self.typename))
    if self._all_fields is None:
      tmp = self.local_field_names.copy()
      tmp.update(self.inherited_field_names)
      if run_unsafe:
        return tmp
      self._all_fields = tmp
    return self._all_fields

  def _ValidateType(self, local_field_names):
    """Validates that the entity type is formatted correctly.

    Checks for formatting and duplicate fields and parents.

    Records any errors found.

    Args:
      local_field_names: list of local field names for the type.
    """
    # Make sure the typename is non-empty.
    if not self.typename:
      self.AddFinding(findings_lib.MissingTypenameError(self))
    elif not isinstance(self.typename, str):
      self.AddFinding(
          findings_lib.IllegalKeyTypeError(self.typename, self.file_context))
    elif not ENTITY_TYPE_NAME_REGEX.match(self.typename):
      self.AddFinding(
          findings_lib.IllegalCharacterError(self.typename, self.file_context))

    # Make sure the type description is non-empty.
    if not self.description:
      self.AddFinding(findings_lib.MissingDescriptionWarning(self))

    # Check for duplicate local fields.
    # this check is case insensitive to catch dupes earlier in the event that
    # we stop explicitly rejecting upper case characters
    check_fields = set()
    for field in local_field_names:
      field_lower = field.lower()
      if field_lower in check_fields:
        self.AddFinding(findings_lib.DuplicateFieldError(self, field))
        continue
      check_fields.add(field_lower)

      # TODO(berkoben): Add more checks to validate fields in isolation
      # (in case we don't have a field set to check against)
      # (i.e. check for chirality, formatting. Could use actual Field objects)

      # Check formatting of field name
      if len(field.split('/')) > 2:
        self.AddFinding(findings_lib.UnrecognizedFieldFormatError(self, field))

    # Check for duplicate parent names.
    parent_names_check = set()
    for parent_name in self.unqualified_parent_names:
      if parent_name in parent_names_check:
        self.AddFinding(findings_lib.DuplicateParentError(self, parent_name))
        continue
      parent_names_check.add(parent_name)

      # Check formatting of parent name
      if len(parent_name.split('/')) > 2:
        self.AddFinding(
            findings_lib.UnrecognizedParentFormatError(self, parent_name))

    # Enforce that the inherited_fields_expanded field is not set
    if self.inherited_fields_expanded:
      self.AddFinding(findings_lib.InheritedFieldsSetError(self))
