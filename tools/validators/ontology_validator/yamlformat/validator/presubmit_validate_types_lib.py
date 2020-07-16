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

"""Top level logic for Entity type validation.

Invoked automatically by PRESUBMIT on changes touching files that define
entity types.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import time

from six.moves import input
import typing

from yamlformat.validator import base_lib
from yamlformat.validator import entity_type_lib
from yamlformat.validator import entity_type_manager
from yamlformat.validator import field_lib
from yamlformat.validator import findings_lib
from yamlformat.validator import namespace_validator
from yamlformat.validator import parse_config_lib as parse
from yamlformat.validator import state_lib
from yamlformat.validator import subfield_lib
from yamlformat.validator import unit_lib

# Define namedtuple Config to store the different kinds of config files
# All attributes should be tuples.
# Each property is a tuple of base_lib.PathParts tuples
Config = typing.NamedTuple('Config', [('fields', tuple), ('subfields', tuple),
                                      ('states', tuple), ('type_defs', tuple),
                                      ('units', tuple)])


class ConfigUniverse(findings_lib.Findings):
  """Helper class to represent the defined universe of ontology configuration.

  Contains all valid components of the ontology

  Args:
    entity_type_universe: config for entity types
    field_universe: config for fields
    subfield_universe: config for subfields
    state_universe: config for states
    unit_universe: config for units
  """

  def __init__(self, entity_type_universe, field_universe, subfield_universe,
               state_universe, unit_universe):
    super(ConfigUniverse, self).__init__()
    self.entity_type_universe = entity_type_universe
    self.field_universe = field_universe
    self.subfield_universe = subfield_universe
    self.state_universe = state_universe
    self.unit_universe = unit_universe

  def _GetDynamicFindings(self, filter_old_warnings):
    findings = []
    if self.subfield_universe:
      findings += self.subfield_universe.GetFindings(filter_old_warnings)
    if self.field_universe:
      findings += self.field_universe.GetFindings(filter_old_warnings)
    if self.entity_type_universe:
      findings += self.entity_type_universe.GetFindings(filter_old_warnings)
    if self.state_universe:
      findings += self.state_universe.GetFindings(filter_old_warnings)
    if self.unit_universe:
      findings += self.unit_universe.GetFindings(filter_old_warnings)
    return findings

  def GetEntityTypeNamespaces(self):
    """Get the entity type namespace objects in this universe, if defined.

    Returns:
      A list of EntityTypeNamespaces or empty list if none are defined
    """
    if not self.entity_type_universe:
      return []
    return self.entity_type_universe.GetNamespaces()


def BuildUniverse(config):
  """Verifies that the ontology config is consistent and valid.

  Args:
    config: a Config namedtuple containing lists of localpaths to config files.

  Returns:
     A ConfigUniverse that is fully populated with all content specified in the
     config.
  """
  # Parse state files
  state_universe = None
  if config.states:
    state_folders = parse.ParseStateFoldersFromFiles(config.states)
    state_universe = state_lib.StateUniverse(state_folders)

  # Parse subfield files
  subfields_universe = None
  if config.subfields:
    subfield_folders = parse.ParseSubfieldFoldersFromFiles(config.subfields)
    subfields_universe = subfield_lib.SubfieldUniverse(subfield_folders)

  # Parse unit files
  unit_universe = None
  if config.units:
    unit_folders = parse.ParseUnitFoldersFromFiles(config.units,
                                                   subfields_universe)
    unit_universe = unit_lib.UnitUniverse(unit_folders)
    if subfields_universe:
      subfields_universe.ValidateUnits(unit_universe)

  # Parse fields files
  fields_universe = None
  if config.fields:
    field_folders = parse.ParseFieldFoldersFromFiles(config.fields,
                                                     subfields_universe,
                                                     state_universe)
    fields_universe = field_lib.FieldUniverse(field_folders)

  # Parse typedef files
  type_folders = parse.ParseTypeFoldersFromFiles(config.type_defs,
                                                 fields_universe)
  types_universe = entity_type_lib.EntityTypeUniverse(type_folders)

  # return findings_list, result_namespaces
  return ConfigUniverse(types_universe, fields_universe, subfields_universe,
                        state_universe, unit_universe)


def OrganizeFindingsByFile(findings_list):
  """Creates dict mapping filepath to all findings in that file.

  Args:
    findings_list: a list of Finding objects.

  Returns:
    A dict. Keys are filepath strings and values are a list of findings
      that are associated with that filepath.
  """
  file_findings_map = {}
  for finding in findings_list:
    filepath = finding.file_context.filepath
    file_list = file_findings_map.get(filepath)
    # not in map: add as new entry
    if file_list is None:
      file_findings_map[filepath] = [finding]
    # if already in map, append this finding to associated value
    else:
      file_findings_map[filepath].append(finding)

  return file_findings_map


def _AddPrefix(path, prefix):
  """Adds prefix to path if it does not start with prefix. Returns path."""
  return os.path.join(prefix, path) if not path.startswith(prefix) else path


def _RemovePrefix(path, prefix):
  """Removes prefix from path if path starts with prefix. Returns path."""
  return path[len(prefix):] if path.startswith(prefix) else path


def SeparateConfigFiles(path_tuples):
  """Separates list of config files into lists of different config file kinds.

  If the directory name is 'fields' the file is a field definition file,
    if it is 'subfields' the file is a subfield def file,
    if it is 'states' the file is a states def file,
    if it is 'units' the file is a units def file,
    if it is 'entity_types' the file is a entity types def file.
  Method retains relative order of paths in each list.

  Args:
    path_tuples: a list of PathParts tuples for config files.

  Returns:
    A Config namedtuple, which contains separate lists for fields, subfields,
      states, type_defs, and units config files.

  Raises:
    RuntimeError: if a file is found in a bad folder.
  """
  fields = []
  subfields = []
  states = []
  type_defs = []
  units = []

  # TODO(berkoben): make these checks handle folders under the component folder
  # All the file validation may be doable here
  for path_tuple in path_tuples:

    foldername = os.path.basename(os.path.dirname(path_tuple.relative_path))
    if foldername == base_lib.SUBFOLDER_NAMES[base_lib.ComponentType.FIELD]:
      fields.append(path_tuple)
    elif foldername == base_lib.SUBFOLDER_NAMES[
        base_lib.ComponentType.SUBFIELD]:
      subfields.append(path_tuple)
    elif foldername == base_lib.SUBFOLDER_NAMES[
        base_lib.ComponentType.MULTI_STATE]:
      states.append(path_tuple)
    elif foldername == base_lib.SUBFOLDER_NAMES[
        base_lib.ComponentType.ENTITY_TYPE]:
      type_defs.append(path_tuple)
    elif foldername == base_lib.SUBFOLDER_NAMES[base_lib.ComponentType.UNIT]:
      units.append(path_tuple)
    elif foldername == base_lib.SUBFOLDER_NAMES[
        base_lib.ComponentType.CONNECTION]:
      # TODO(b/153196944): don't skip these files when we support connections
      continue
    else:
      raise RuntimeError('File found outside of expected folder.')

  return Config(
      fields=tuple(fields),
      subfields=tuple(subfields),
      states=tuple(states),
      type_defs=tuple(type_defs),
      units=tuple(units))


def _ValidateConfigInner(unmodified,
                         modified_base,
                         modified_client,
                         interactive=False):
  """Runs config validation and finding filtration.

  Args:
    unmodified: unchanged file paths to include in validation
    modified_base: paths to original versions of changed files in validation
    modified_client: paths to changed files in validation
    interactive: Set true for timing log messages.

  Returns:
    A tuple with a list of findings from validation and the universe
  """

  # Separate different kinds of config files
  # Concatenate paths such that the changed files go last.  This is important
  # because we always want conflicts between new and old files to show as
  # being caused by new changes and files are processed in order.
  start_time = time.time()
  cl_paths = unmodified + modified_client
  cl_config = SeparateConfigFiles(cl_paths)
  new_universe = BuildUniverse(cl_config)
  end_time = time.time()

  if interactive:
    print('New universe build: {0} seconds.\n'.format(
        str(end_time - start_time)))
    start_time = end_time

  if not new_universe.IsValid():
    findings = [
        f for f in new_universe.GetFindings()
        if isinstance(f, findings_lib.ValidationError)
    ]
    return findings, new_universe

  # Validate across the type namespaces. Short-circuit if validation fails and
  # return any breaking findings.
  cl_validator = namespace_validator.NamespaceValidator(
      new_universe.GetEntityTypeNamespaces())
  if not cl_validator.IsValid():
    universe_errors = []
    universe_errors = [
        f for f in new_universe.GetFindings()
        if isinstance(f, findings_lib.ValidationError)
    ]
    # Technically there should never be universe errors if we get here. Better
    # to be safe than sorry though.
    return cl_validator.GetFindings() + universe_errors, new_universe

  if interactive:
    end_time = time.time()
    print('New ns check: {0} seconds.\n'.format(str(end_time - start_time)))
    start_time = end_time

  base_paths = unmodified + modified_base
  base_config = SeparateConfigFiles(base_paths)
  old_universe = BuildUniverse(base_config)

  if interactive:
    end_time = time.time()
    print('Old uverse build: {0} seconds.\n'.format(str(end_time - start_time)))
    start_time = end_time

  # Run validation on base universe to expand types.
  namespace_validator.NamespaceValidator(old_universe.GetEntityTypeNamespaces())

  if interactive:
    end_time = time.time()
    print('Old ns check: {0} seconds.\n'.format(str(end_time - start_time)))
    start_time = end_time

  mgr = entity_type_manager.EntityTypeManager(new_universe.entity_type_universe)
  mgr.Analyze()
  del mgr

  if interactive:
    end_time = time.time()
    print('Type analysis: {0} seconds.\n'.format(str(end_time - start_time)))
    start_time = end_time

  CheckBackwardsCompatibility(new_universe.entity_type_universe,
                              old_universe.entity_type_universe)

  if interactive:
    end_time = time.time()
    print('Backwards compat: {0} seconds.\n'.format(str(end_time - start_time)))
    start_time = end_time

  # TODO(berkoben) pass this to methods below when fixing b/116850383?
  # cl_path_set = set(cl_paths)
  if new_universe.entity_type_universe:
    _SetTypeFolderChanges(
        list(new_universe.entity_type_universe.namespace_folder_map.values()))
  _SetFieldChanges(new_universe.field_universe, old_universe.field_universe)
  _SetSubfieldChanges(new_universe.subfield_universe,
                      old_universe.subfield_universe)
  _SetStateChanges(new_universe.state_universe, old_universe.state_universe)
  _SetUnitChanges(new_universe.unit_universe, old_universe.unit_universe)

  filtered_findings = new_universe.GetFindings(True)
  all_findings = new_universe.GetFindings(False)
  diff = len(all_findings) - len(filtered_findings)
  if diff > 0:
    filtered_findings.append(findings_lib.SuppressedFindingsWarning(diff))

  return filtered_findings, new_universe


def _SetTypeFolderChanges(field_folders):
  """Marks entity type folders that changed in the latest CL.

  At this time all folders are marked as changed.

  Args:
    field_folders: list of field folders
  """
  if not field_folders:
    return
  for folder in field_folders:
    # TODO(berkoben) find a way to filter folder warnings b/116850383
    folder.SetChanged()


def _SetChanges(new_universe, old_universe, items_func):
  """Marks ontology items and folders/namespaces that changed in the latest CL.

  This is a helper method that should be called for each type of ontology item
  with different items_funcs provided.

  Args:
    new_universe: FindingsUniverse subclass representing the new config
    old_universe: FindingsUniverse subclass representing the old config
    items_func: A function that should return a map of ontology items contained
      in a namespace. Takes a namespace object as a parameter.
  """

  new_ns_map = {}
  old_ns_map = {}
  if not new_universe:
    return
  if old_universe:
    for folder in old_universe.folders:
      ns = folder.local_namespace
      old_ns_map[ns.namespace] = ns
  for folder in new_universe.folders:
    ns = folder.local_namespace
    new_ns_map[ns.namespace] = ns
    # TODO(berkoben) find a way to filter folder warnings b/116850383
    folder.SetChanged()
  for new_ns in new_ns_map.values():
    if new_ns.namespace not in old_ns_map:
      new_ns.SetChanged()
      for item in items_func(new_ns).values():
        item.SetChanged()
      continue
    old_ns = old_ns_map[new_ns.namespace]
    old_items = items_func(old_ns).copy()
    for new_item in items_func(new_ns).values():
      if new_item.name not in old_items:
        new_item.SetChanged()
        new_ns.SetChanged()
        continue
      old_item = old_items.pop(new_item.name)
      if new_item != old_item:
        new_item.SetChanged()
        new_ns.SetChanged()
    if old_items:
      new_ns.SetChanged()


def _SetFieldChanges(new_universe, old_universe):
  return _SetChanges(new_universe, old_universe, lambda ns: ns.fields)


def _SetSubfieldChanges(new_universe, old_universe):
  return _SetChanges(new_universe, old_universe, lambda ns: ns.subfields)


def _SetStateChanges(new_universe, old_universe):
  return _SetChanges(new_universe, old_universe, lambda ns: ns.states)


def _SetUnitChanges(new_universe, old_universe):
  return _SetChanges(new_universe, old_universe, lambda ns: ns.units)


def CheckBackwardsCompatibility(new_universe, old_universe):
  """Checks that non-abstract types are not removed or changed in new configs.

  Method expects types in passed universe to have inherited_fields_expanded.
  Method has the side effect of setting is_changed field on everything in this
  universe that has changes except folders at the entity type level.

  Args:
    new_universe: EntityTypeUniverse object for the new config
    old_universe: EntityTypeUniverse object for the old config

  Returns:
    A list of findings generated by the compatibility check.

  Raises:
    RuntimeError: if fields are not expanded for any types
  """
  # for every non-abstract type in the old universe, there should be a
  # corresponding type with the same fields in the new universe.
  old_ns_map = old_universe.type_namespaces_map
  new_ns_map = new_universe.type_namespaces_map.copy()

  findings = []
  for ns_name in old_ns_map:
    old_ns = old_ns_map[ns_name]
    if ns_name not in new_ns_map:
      old_types = list(old_ns.valid_types_map.keys())
      for old_type_name in old_types:
        if old_ns.valid_types_map[old_type_name].is_abstract:
          continue
        context = findings_lib.FileContext(
            old_universe.namespace_folder_map[ns_name].GetFolderpath())
        finding = findings_lib.RemovedNamespaceWarning(context, ns_name,
                                                       list(old_types))
        new_universe.AddFinding(finding)
        findings.append(finding)
        break
      continue

    # Remove namespace from new ns map so when we're done we'll only have newly
    # created namespaces left in it.
    new_ns = new_ns_map.pop(ns_name)
    new_ns_types = new_ns.valid_types_map.copy()
    for type_name in old_ns.valid_types_map:
      old_type = old_ns.valid_types_map[type_name]
      if old_type.uid:
        new_type_uid_entry = new_universe.type_ids_map.get(old_type.uid)
        if new_type_uid_entry:
          if (new_type_uid_entry.namespace == ns_name and
              new_type_uid_entry.typename == type_name):
            new_type = new_ns_types.pop(type_name)
          else:
            new_type = new_universe.GetEntityType(new_type_uid_entry.namespace,
                                                  new_type_uid_entry.typename)
        else:
          # type has been removed
          if not old_type.is_abstract:
            finding = findings_lib.RemovedTypeWarning(old_type)
            new_ns.AddFinding(finding)
            findings.append(finding)
          continue
      elif type_name not in new_ns_types:
        if not old_type.is_abstract:
          finding = findings_lib.RemovedTypeWarning(old_type)
          new_ns.AddFinding(finding)
          findings.append(finding)
        continue
      else:
        new_type = new_ns_types.pop(type_name)

      # Check to appease python type static analyzer
      if new_type is None:
        raise RuntimeError('new_type should never be None at this point.')

      old_fields = old_type.GetAllFields()
      new_fields = new_type.GetAllFields()
      if old_fields == new_fields:
        if (new_type.description != old_type.description or
            new_type.typename != old_type.typename or
            new_type.is_abstract != old_type.is_abstract or
            new_type.is_canonical != old_type.is_canonical):
          new_type.SetChanged()
          new_ns.SetChanged()
        continue

      new_type.SetChanged()
      new_ns.SetChanged()
      new_universe.namespace_folder_map[new_ns.namespace].SetChanged()

      if old_type.is_abstract:
        continue

      # Check added fields
      for field in old_fields:
        if field in new_fields:
          new_fields.pop(field)
          continue
        finding = findings_lib.RemovedFieldWarning(new_type, field)
        new_type.AddFinding(finding)
        findings.append(finding)

      for field in new_fields:
        if new_fields[field].optional:
          continue
        finding = findings_lib.AddedFieldWarning(new_type, field)
        new_type.AddFinding(finding)
        findings.append(finding)

    for new_type in new_ns_types.values():
      new_type.SetChanged()

  # Mark anything new as changed
  for ns_name in new_ns_map:
    new_ns = new_ns_map[ns_name]
    new_ns.SetChanged()
    new_universe.namespace_folder_map[new_ns.namespace].SetChanged()
    for new_type in new_ns.valid_types_map.values():
      new_type.SetChanged()

  return findings


def RunPresubmit(unmodified, modified_base, modified_client):
  """Top level runner for presubmit.

  Args:
    unmodified: unchanged file paths to include in validation
    modified_base: paths to original versions of changed files in validation
    modified_client: paths to changed files in validation

  Returns:
      findings: from the validate configuration results.

  """

  findings, _ = _ValidateConfigInner(unmodified, modified_base, modified_client, False)
  return findings


def _PrintType(ns, et):
  """Prints the contents of a type.

  Args:
    ns: namespace name
    et: entity type
  """
  print('\n' + ns + '/' + et.typename)
  print('description: ' + et.description)
  parents = et.parent_names
  local_fields = et.local_field_names.values()
  inherited_fields = et.inherited_field_names.values()
  overlap = set(et.local_field_names).intersection(et.inherited_field_names)
  lfl = list(local_fields)
  lfl.sort()
  ifl = list(inherited_fields)
  ifl.sort()
  print('  inherits:')
  for parent in parents:
    print('  - ' + parent)
  print('  inherited_fields:')
  for inherited in ifl:
    print('  - ' + findings_lib.MakeFieldString(inherited))
  print('  uses:')
  for field in lfl:
    print('  - ' + findings_lib.MakeFieldString(field))
  if overlap:
    print('  HAS REDUNDANT LOCAL FIELDS')


def PrintFindings(findings, filter_text):
  """Prints the findings of the ontology validation

  Args:
    findings: a list of Finding objects.
    filter_text: command line arguments. The only available argument is
      'match:<value>' which will simply perform a simple string 'contains' on
      the finding output and cause only matching findings to print.

  """
  findings_by_file = OrganizeFindingsByFile(findings)
  for filepath in findings_by_file:
    findings_for_file = findings_by_file[filepath]
    if not findings_for_file:
      print('no Findings in {0}'.format(filepath))
      continue
    print('Findings in {0}'.format(filepath))
    for finding in findings_for_file:
      if not filter_text or filter_text in str(finding):
        print(finding)

  print('\n' + str(len(findings)) + ' findings.\n')


def RunInteractive(filter_text, modified_base, modified_client):
  """Runs interactive mode when presubmit is run as a standalone application.

  This will run all files in the ontology as if they were new.

  Args:
    filter_text: command line arguments. The only available argument is
      'match:<value>' which will simply perform a simple string 'contains' on
        the finding output and cause only matching findings to print.
    modified_base: paths to original versions of changed files in validation.
    modified_client: the list of modified files to validate.


  Returns:
    zero.
  """
  print('Analyzing...')
  start_time = time.time()
  findings, universe = _ValidateConfigInner([], modified_base, modified_client,
                                            True)

  PrintFindings(findings, filter_text)

  end_time = time.time()
  print('Elapsed time: {0} seconds.\n'.format(str(end_time - start_time)))

  etu = universe.entity_type_universe
  print('Enter one or more fully qualified names <NS/TYPE> separated by spaces')
  print('Prefix command with "findings:" to get findings for each type')
  while True:
    user_input = str(input('what type do you want to see? <NS/type>: '))
    input_split = user_input.strip().split(':')
    type_input = user_input
    include_findings = False
    if len(input_split) == 2:
      mode = input_split[0].strip()
      if mode == 'findings':
        include_findings = True
      type_input = input_split[1].strip()
    type_name_list = type_input.split(' ')
    first_type = None
    first_type_name = ''
    type_dict = {}
    for fqn in type_name_list:
      ns, etn = field_lib.SplitFieldName(fqn)
      et = etu.GetEntityType(ns, etn)
      if not et:
        print('no type for ' + fqn)
        continue
      if not first_type:
        first_type = et
        first_type_name = ns + '/' + etn
      else:
        type_dict[ns + '/' + etn] = et

      _PrintType(ns, et)
      if include_findings:
        print('  findings:\n')
        findings = et.GetFindings()
        for finding in findings:
          print('\t' + str(finding))

    if not first_type or not type_dict:
      continue
    first_field_set = (
        set(first_type.inherited_field_names)
        | set(first_type.local_field_names))
    print('Checking fields against ' + first_type_name)
    for name in type_dict:
      et = type_dict[name]
      field_set = (set(et.inherited_field_names) | set(et.local_field_names))
      outer = first_field_set.symmetric_difference(field_set)

      if not outer:
        print('\n' + name + ' is matching')
        continue

      missing_from_first = sorted(field_set.difference(first_field_set))
      missing_from_other = sorted(first_field_set.difference(field_set))
      print('\n' + name)
      print('\tIs missing:\n\t\t' + str(list(missing_from_other)))
      print('\tHas added:\n\t\t' + str(list(missing_from_first)))

    print('\n')

  return 0
