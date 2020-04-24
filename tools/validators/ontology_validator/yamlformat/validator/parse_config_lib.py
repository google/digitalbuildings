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
"""Library for parsing config files for subfields, fields, entity types."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import os

import yaml

from validation.validator import base_lib
from validation.validator import entity_type_lib
from validation.validator import field_lib
from validation.validator import findings_lib
from validation.validator import state_lib
from validation.validator import subfield_lib
from validation.validator import unit_lib


class ParseError(Exception):

  def __init__(self, finding):
    super(ParseError, self).__init__(finding)
    self.finding = finding


class UniqueKeyLoader(yaml.SafeLoader):
  """Version of the SafeLoader that rejects duplicate map keys."""

  # Override the mapping from strings to boolean values. The base mapping
  # contains entries for 'yes', 'no', 'on', and 'off', which we do not want
  # to resolve to booleans.
  bool_values = {
      'true': True,
      'false': False,
  }

  def construct_yaml_bool(self, node):
    """Returns a string if the node doesn't match a configured boolean value."""
    value = self.construct_scalar(node)
    return self.bool_values.get(value.lower(), value)

  def construct_mapping(self, node, deep=False):
    """Overrides default mapper with a version that detects duplicate keys."""

    if not isinstance(node, yaml.nodes.MappingNode):
      raise yaml.constructor.ConstructorError(
          None,
          None,
          'Expected a mapping node, but found %s' % node.id,
          node.start_mark)
    mapping = {}
    for key_node, value_node in node.value:
      key = self.construct_object(key_node, deep=deep)
      try:
        hash(key)
      except TypeError:
        m1 = node.start_mark
        m2 = key_node.start_mark
        ctx = findings_lib.FileContext(m1.name, m1.line, m2.line)
        raise ParseError(findings_lib.BadKeyError(key, ctx))
      # check for duplicate keys
      if key in mapping:
        m1 = node.start_mark
        m2 = key_node.start_mark
        ctx = findings_lib.FileContext(m1.name, m1.line, m2.line)
        raise ParseError(findings_lib.DuplicateKeyError(key, ctx))
      value = self.construct_object(value_node, deep=deep)
      mapping[key] = value
    return mapping


UniqueKeyLoader.add_constructor('tag:yaml.org,2002:bool',
                                UniqueKeyLoader.construct_yaml_bool)


def _ParseFoldersFromFiles(files, component_type, create_folder_fn):
  """Returns a list of ConfigFolder objects parsed from the given files.

  Args:
    files: list of absolute paths to config files.
    component_type: the component associated with the created folders.
    create_folder_fn: function to create an instance of a ConfigFolder subclass.
  """

  if not files:
    return []
  folders = []
  files_by_folder = _OrganizeConfigFilesByFolder(files)

  # Create the global folder first. The global field folder is created even if
  # there are no field files in the global namespace to ensure that fields can
  # be up-leveled.
  global_namespace = None
  global_path = base_lib.SUBFOLDER_NAMES[component_type]
  if (global_path in files_by_folder or
      component_type == base_lib.ComponentType.FIELD):
    global_folder = _CreateFolder(global_path, None, create_folder_fn,
                                  files_by_folder.get(global_path, []))
    folders.append(global_folder)
    global_namespace = global_folder.local_namespace
    files_by_folder.pop(global_path, None)

  for folderpath in files_by_folder:
    folders.append(
        _CreateFolder(folderpath, global_namespace, create_folder_fn,
                      files_by_folder.get(folderpath)))
  return folders


def _CreateFolder(folderpath, global_namespace, create_folder_fn, file_tuples):
  """Creates a ConfigFolder for the given folderpath."""
  folder = create_folder_fn(folderpath, global_namespace)
  for ft in file_tuples:
    with open(os.path.join(ft.root, ft.relative_path), 'r') as f:
      try:
        documents = yaml.load_all(f, Loader=UniqueKeyLoader)
        folder.AddFromConfig(documents, ft.relative_path)
      except ParseError as e:
        folder.AddFinding(e.finding)
  folder.Finalize()
  return folder


def ParseFieldFoldersFromFiles(field_files,
                               subfield_universe=None,
                               state_universe=None):
  """Returns list of FieldFolder objects parsed from field_files.

  Args:
    field_files: list of absolute paths to field files.
    subfield_universe: optional SubfieldUniverse object for validation. If not
      given, validation of subfields is not performed.
    state_universe: optional StateUniverse object for validation. If not
      given, validation of states is not performed.
  """

  def CreateFieldFolder(folderpath, parent_namespace):
    field_folder = field_lib.FieldFolder(folderpath, parent_namespace)
    namespace = field_folder.local_namespace.namespace
    if subfield_universe:
      field_folder.local_namespace.subfields = (
          subfield_universe.GetSubfieldsMap(namespace))
    if state_universe:
      field_folder.local_namespace.states = (
          state_universe.GetStatesMap(namespace))
    return field_folder

  return _ParseFoldersFromFiles(field_files, base_lib.ComponentType.FIELD,
                                CreateFieldFolder)


def ParseTypeFoldersFromFiles(types_files, fields_universe=None):
  """Returns list of EntityTypeFolder objects parsed from types_files.

  Args:
    types_files: list of absolute paths to entity type files.
    fields_universe: optional FieldsUniverse object for field validation. If not
      given, validation of fields is not performed.
  """

  def CreateEntityTypeFolder(folderpath, parent_namespace):
    del parent_namespace  # Unused by EntityTypeFolder.
    return entity_type_lib.EntityTypeFolder(folderpath, fields_universe)

  return _ParseFoldersFromFiles(types_files, base_lib.ComponentType.ENTITY_TYPE,
                                CreateEntityTypeFolder)


def ParseSubfieldFoldersFromFiles(subfield_files):
  """Returns list of SubfieldFolder objects parsed from subfield_files.

  Args:
    subfield_files: list of absolute paths to subfield files.
  """

  def CreateSubfieldFolder(folderpath, parent_namespace):
    del parent_namespace  # Unused by SubfieldFolder.
    return subfield_lib.SubfieldFolder(folderpath)

  return _ParseFoldersFromFiles(subfield_files, base_lib.ComponentType.SUBFIELD,
                                CreateSubfieldFolder)


def ParseStateFoldersFromFiles(state_files):
  """Returns list of StateFolder objects parsed from state_files.

  Args:
    state_files: list of absolute paths to state files.
  """

  def CreateStateFolder(folderpath, parent_namespace):
    del parent_namespace  # Unused by StateFolder.
    return state_lib.StateFolder(folderpath)

  return _ParseFoldersFromFiles(state_files, base_lib.ComponentType.MULTI_STATE,
                                CreateStateFolder)


def ParseUnitFoldersFromFiles(unit_files, subfield_universe=None):
  """Returns list of UnitFolder objects parsed from unit_files.

  Args:
    unit_files: list of absolute paths to unit files.
    subfield_universe: optional SubfieldUniverse object for validation. If not
      given, validation of subfields is not performed.
  """

  def CreateUnitFolder(folderpath, parent_namespace):
    unit_folder = unit_lib.UnitFolder(folderpath, parent_namespace)
    if subfield_universe:
      unit_folder.local_namespace.subfields = (
          subfield_universe.GetSubfieldsMap(
              unit_folder.local_namespace.namespace))
    return unit_folder

  return _ParseFoldersFromFiles(unit_files, base_lib.ComponentType.UNIT,
                                CreateUnitFolder)


def _OrganizeConfigFilesByFolder(config_tuples):
  """Returns dict mapping folder paths to a list of config files.

  Keys are relative paths from ontology root to the config folders.
  Values are lists of base_lib.PathParts referencing config files.

  Args:
    config_tuples: A list of PathParts tuples for config files.
  """
  files_by_folder = collections.defaultdict(list)
  for file_tuple in config_tuples:
    folderpath = os.path.dirname(file_tuple.relative_path)
    files_by_folder[folderpath].append(file_tuple)

  return files_by_folder
