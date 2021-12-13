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
"""Tests for parse_config_lib."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from os import path
import re

from absl import flags
from absl.testing import absltest

from yamlformat.tests import test_constants
from yamlformat.validator import base_lib
from yamlformat.validator import field_lib
from yamlformat.validator import findings_lib
from yamlformat.validator import parse_config_lib as parse
from yamlformat.validator import state_lib
from yamlformat.validator import subfield_lib
from yamlformat.validator import unit_lib

_F = field_lib.Field

FLAGS = flags.FLAGS

# Constant to point to test files.
RESOURCE_PATH = path.join(test_constants.TEST_RESOURCES)
field_lib.FIELD_TO_NAMESPACE_REGEX = re.compile(
    r'^' + RESOURCE_PATH.replace('\\', '\\\\') + r'(\w*)[/\\]?fields.*')


class ParseConfigLibTest(absltest.TestCase):

  def setUp(self):
    super(ParseConfigLibTest, self).setUp()
    self.base_dir = RESOURCE_PATH
    self.duplicate_types_file = base_lib.PathParts(
        root=self.base_dir,
        relative_path='BAD/entity_types/bad_duplicate_types.yaml')
    self.good_types_file = base_lib.PathParts(
        root=self.base_dir, relative_path='GOOD/entity_types/good1.yaml')
    self.good_types_file_2 = base_lib.PathParts(
        root=self.base_dir, relative_path='GOOD/entity_types/good2.yaml')
    self.empty_types_file = base_lib.PathParts(
        root=self.base_dir, relative_path='GOOD/entity_types/empty.yaml')

    self.global_fields_file = base_lib.PathParts(
        root=self.base_dir, relative_path='fields/global_fields.yaml')
    self.local_fields_file = base_lib.PathParts(
        root=self.base_dir, relative_path='GOOD/fields/local_fields.yaml')
    self.state_fields_file = base_lib.PathParts(
        root=self.base_dir, relative_path='GOOD/fields/state_fields.yaml')

    self.global_subfields_file = base_lib.PathParts(
        root=self.base_dir, relative_path='subfields/global_subfields.yaml')
    self.local_subfields_file = base_lib.PathParts(
        root=self.base_dir, relative_path='GOOD/subfields/local_subfields.yaml')

    self.global_states_file = base_lib.PathParts(
        root=self.base_dir, relative_path='states/global_states.yaml')
    self.local_states_file = base_lib.PathParts(
        root=self.base_dir, relative_path='GOOD/states/local_states.yaml')

    self.global_units_file = base_lib.PathParts(
        root=self.base_dir, relative_path='units/global_units.yaml')
    self.local_units_file = base_lib.PathParts(
        root=self.base_dir, relative_path='GOOD/units/local_units.yaml')

  def testParseTypeFoldersFromFilesNoFieldsUniverse(self):
    type_folders = parse.ParseTypeFoldersFromFiles(
        [self.good_types_file, self.good_types_file_2])
    # should have 1 folder for GOOD_TYPES namespace
    self.assertLen(type_folders, 1)
    # folder should have 4 types
    valid_types = list(type_folders[0].local_namespace.valid_types_map.values())
    self.assertLen(valid_types, 4)

  def testParseTypeFoldersFromFilesEmptyConfig(self):
    type_folders = parse.ParseTypeFoldersFromFiles([self.empty_types_file])
    self.assertLen(type_folders, 1)
    valid_types = list(type_folders[0].local_namespace.valid_types_map.values())
    self.assertEmpty(valid_types)

  def testParseTypeFoldersFromFilesDuplicateTypes(self):
    type_folders = parse.ParseTypeFoldersFromFiles([self.duplicate_types_file])
    self.assertTrue(type_folders[0].HasFindingTypes(
        [findings_lib.DuplicateKeyError]))

  def testParseTypeFoldersFromFilesWithFieldsUniverse(self):
    fields_universe = field_lib.FieldUniverse([])
    fields_universe._namespace_map = {
        '': [
            _F('current_sensor'),
            _F('fan_run_status'),
            _F('dryer_run_status'),
            _F('fan_run_command')
        ],
        'GOOD': [_F('zone_air_temperature_sensor')]
    }
    type_folders = parse.ParseTypeFoldersFromFiles(
        [self.good_types_file, self.good_types_file_2], fields_universe)
    # should have 1 folder for GOOD namespace
    self.assertLen(type_folders, 1)
    # folder should have 4 types
    valid_types = list(type_folders[0].local_namespace.valid_types_map.values())
    self.assertLen(valid_types, 4)

  def testParseTypeFoldersFromFileBadFormat(self):
    bad_types_file = base_lib.PathParts(
        root=self.base_dir, relative_path='BAD/entity_types/bad1.yaml')
    fields_universe = field_lib.FieldUniverse([])
    fields_universe._namespace_map = {
        '': ('dryer_run_status', 'fan_run_command')
    }
    type_folders = parse.ParseTypeFoldersFromFiles([bad_types_file],
                                                   fields_universe)
    # should have 1 folder
    self.assertLen(type_folders, 1)
    type_folder = type_folders[0]
    # Should find 4 errors
    self.assertLen(type_folder.GetFindings(), 3)
    self.assertTrue(
        type_folder.HasFindingTypes([findings_lib.DuplicateFieldError]))
    self.assertTrue(
        type_folder.HasFindingTypes([findings_lib.UnrecognizedFieldFormatError
                                    ]))
    self.assertTrue(
        type_folder.HasFindingTypes([findings_lib.DuplicateParentError]))

  def testParseTypeFoldersFromFileUndefinedFields(self):
    bad_type_file = base_lib.PathParts(
        root=self.base_dir, relative_path='BAD/entity_types/bad3.yaml')
    fields_universe = field_lib.FieldUniverse([])
    fields_universe._namespace_map = {
        '': [_F('current_sensor'), _F('fan_run_command')]
    }
    type_folders = parse.ParseTypeFoldersFromFiles([bad_type_file],
                                                   fields_universe)
    # should have 1 folder
    self.assertLen(type_folders, 1)

    self.assertTrue(type_folders[0].local_namespace.HasFindingTypes(
        [findings_lib.UndefinedFieldError]))
    valid_types = list(type_folders[0].local_namespace.valid_types_map.values())
    self.assertFalse(valid_types)

  def testParseFieldFoldersFromGoodFilesNoSubfieldUniverse(self):
    field_folders = parse.ParseFieldFoldersFromFiles(
        [self.global_fields_file, self.local_fields_file])
    # Should have two namespace objects
    self.assertLen(field_folders, 2)
    for folder in field_folders:
      self.assertFalse(folder.GetFindings())
      if folder.parent_namespace is None:
        # check global namespace
        # All the fields should be global. The field in local_fields_file is
        # upleveled
        # Should have 5 fields in global namespace
        global_fields = folder.local_namespace.fields
        self.assertLen(global_fields, 5)
        self.assertIn(frozenset({'fan', 'run', 'status'}), global_fields)
        self.assertIn(frozenset({'dryer', 'run', 'status'}), global_fields)
        self.assertIn(frozenset({'command', 'fan', 'run'}), global_fields)
        self.assertIn(
            frozenset({'air', 'sensor', 'temperature', 'zone'}), global_fields)
        self.assertIn(frozenset({'current', 'sensor'}), global_fields)

  def testParseFieldFoldersFromGoodFilesWithSubfieldUniverse(self):
    subfield_folders = parse.ParseSubfieldFoldersFromFiles(
        [self.global_subfields_file, self.local_subfields_file])
    subfield_universe = subfield_lib.SubfieldUniverse(subfield_folders)

    field_folders = parse.ParseFieldFoldersFromFiles(
        [self.global_fields_file, self.local_fields_file],
        subfield_universe=subfield_universe)
    # Should have two namespace objects
    self.assertLen(field_folders, 2)
    for folder in field_folders:
      self.assertEmpty(folder.GetFindings())
      if folder.parent_namespace is None:
        # check global namespace
        # Should have 4 fields in global namespace
        global_fields = folder.local_namespace.fields
        self.assertLen(global_fields, 4)
        self.assertIn(frozenset({'fan', 'run', 'status'}), global_fields)
        self.assertIn(frozenset({'dryer', 'run', 'status'}), global_fields)
        self.assertIn(frozenset({'command', 'fan', 'run'}), global_fields)
        self.assertIn(frozenset({'current', 'sensor'}), global_fields)
      else:
        # check local namespace
        self.assertIn(
            frozenset({'air', 'sensor', 'temperature', 'zone'}),
            folder.local_namespace.fields)

  def testParseFieldFoldersFromGoodFilesWithStateUniverse(self):
    state_folders = parse.ParseStateFoldersFromFiles(
        [self.global_states_file, self.local_states_file])
    state_universe = state_lib.StateUniverse(state_folders)

    field_folders = parse.ParseFieldFoldersFromFiles(
        [self.state_fields_file], state_universe=state_universe)
    self.assertLen(field_folders, 2)
    for folder in field_folders:
      self.assertEmpty(folder.GetFindings())
      if folder.parent_namespace is not None:
        # field_two uses local states and isn't up-leveled
        self.assertSameElements([frozenset({'field', 'two'})],
                                folder.local_namespace.fields)
      else:
        self.assertSameElements(
            [frozenset({'field', 'one'}),
             frozenset({'field', 'three'})], folder.local_namespace.fields)

  def testParseFieldFoldersFromBadFileWithStateUniverse(self):
    state_folders = parse.ParseStateFoldersFromFiles(
        [self.global_states_file, self.local_states_file])
    state_universe = state_lib.StateUniverse(state_folders)

    bad_fields = base_lib.PathParts(
        root=self.base_dir, relative_path='BAD/fields/bad_state_fields.yaml')
    field_folders = parse.ParseFieldFoldersFromFiles(
        [bad_fields], state_universe=state_universe)
    local_folder = field_folders[1]
    self.assertTrue(
        local_folder.HasFindingTypes([findings_lib.InvalidStateFormatError]))
    self.assertTrue(
        local_folder.HasFindingTypes([findings_lib.DuplicateStateError]))
    self.assertTrue(
        local_folder.HasFindingTypes([findings_lib.UnrecognizedStateError]))

  def testParseFieldFoldersFromBadFile(self):
    bad_fields = base_lib.PathParts(
        root=self.base_dir, relative_path='BAD/fields/bad_local_fields.yaml')
    field_folders = parse.ParseFieldFoldersFromFiles([bad_fields])
    # should have 2 folders. (global folder is created automatically)
    self.assertLen(field_folders, 2)
    # Field in bad_local will be upleveled to global ns
    global_folder = field_folders[0]
    self.assertTrue(
        global_folder.local_namespace.HasFindingTypes(
            [findings_lib.DuplicateFieldDefinitionError]))

  def testParseFieldFoldersFromBadFileDuplicateKeys(self):
    bad_fields = base_lib.PathParts(
        root=self.base_dir,
        relative_path='BAD/fields/duplicate_literal_fields.yaml')
    field_folders = parse.ParseFieldFoldersFromFiles([bad_fields])
    # Error is added to the folder it is found in, even if fields may uplevel
    local_folder = field_folders[1]
    self.assertTrue(
        local_folder.HasFindingTypes([findings_lib.DuplicateKeyError]))

  def testParseSubfieldFoldersFromGoodFiles(self):
    subfield_folders = parse.ParseSubfieldFoldersFromFiles(
        [self.global_subfields_file, self.local_subfields_file])
    # Should have two folder objects
    self.assertLen(subfield_folders, 2)
    for folder in subfield_folders:
      self.assertEmpty(folder.GetFindings())
      subfields_map = folder.local_namespace.subfields
      if not folder.local_namespace.namespace:
        # check global namespace
        self.assertIn('fan', subfields_map)
        self.assertIn('dryer', subfields_map)
        self.assertIn('current', subfields_map)
        self.assertIn('run', subfields_map)
        self.assertIn('sensor', subfields_map)
        self.assertIn('status', subfields_map)
        self.assertIn('command', subfields_map)
        self.assertIn('temperature', subfields_map)
      else:
        # check local namespace
        self.assertEqual(folder.local_namespace.namespace, 'GOOD')
        self.assertIn('zone', subfields_map)
        self.assertIn('air', subfields_map)

  def testParseSubfieldFoldersFromBadFile(self):
    bad_subfields = base_lib.PathParts(
        root=self.base_dir,
        relative_path='BAD/subfields/bad_local_subfields.yaml')
    subfield_folders = parse.ParseSubfieldFoldersFromFiles([bad_subfields])
    # should have 1 folder.
    self.assertLen(subfield_folders, 1)
    subfield_folder = subfield_folders[0]
    self.assertTrue(
        subfield_folder.local_namespace.HasFindingTypes(
            [findings_lib.DuplicateSubfieldDefinitionError]))

  def testParseSubfieldFoldersFromBadFileDuplicateFields(self):
    bad_subfields = base_lib.PathParts(
        root=self.base_dir,
        relative_path='BAD/subfields/duplicate_subfield_keys.yaml')
    subfield_folders = parse.ParseSubfieldFoldersFromFiles([bad_subfields])
    # should have 1 folder.
    self.assertLen(subfield_folders, 1)
    subfield_folder = subfield_folders[0]
    self.assertTrue(
        subfield_folder.HasFindingTypes([findings_lib.DuplicateKeyError]))

  def testParseStateFoldersFromGoodFiles(self):
    state_folders = parse.ParseStateFoldersFromFiles(
        [self.global_states_file, self.local_states_file])
    # Should have two folder objects
    self.assertLen(state_folders, 2)
    for folder in state_folders:
      self.assertEmpty(folder.GetFindings())
      states_map = folder.local_namespace.states
      if not folder.local_namespace.namespace:
        # check global namespace
        self.assertIn('ON', states_map)
        self.assertIn('OFF', states_map)
        self.assertIn('AUTO', states_map)
      else:
        # check local namespace
        self.assertEqual(folder.local_namespace.namespace, 'GOOD')
        self.assertIn('GOOD', states_map)
        self.assertIn('BETTER', states_map)
        self.assertIn('BEST', states_map)

  def testParseStateFoldersFromBadFile(self):
    bad_states = base_lib.PathParts(
        root=self.base_dir, relative_path='BAD/states/bad_states.yaml')
    state_folders = parse.ParseStateFoldersFromFiles([bad_states])

    self.assertLen(state_folders, 1)
    state_folder = state_folders[0]
    self.assertTrue(
        state_folder.HasFindingTypes(
            [findings_lib.MissingStateDescriptionWarning]))
    self.assertTrue(
        state_folder.HasFindingTypes([findings_lib.InvalidStateNameError]))
    self.assertTrue(
        state_folder.HasFindingTypes([findings_lib.IllegalKeyTypeError]))

  def testParseStateFoldersFromBadFileDuplicateKeys(self):
    bad_states = base_lib.PathParts(
        root=self.base_dir, relative_path='BAD/states/duplicate_states.yaml')
    state_folders = parse.ParseStateFoldersFromFiles([bad_states])

    self.assertLen(state_folders, 1)
    state_folder = state_folders[0]
    self.assertTrue(
        state_folder.HasFindingTypes([findings_lib.DuplicateKeyError]))

  def testParseUnitFoldersFromGoodFiles(self):
    subfield_folders = parse.ParseSubfieldFoldersFromFiles(
        [self.global_subfields_file, self.local_subfields_file])
    subfield_universe = subfield_lib.SubfieldUniverse(subfield_folders)

    unit_folders = parse.ParseUnitFoldersFromFiles(
        [self.global_units_file],
        subfield_universe=subfield_universe)
    self.assertTrue(unit_folders)
    for folder in unit_folders:
      self.assertEmpty(folder.GetFindings())
      current_units = folder.local_namespace.GetUnitsForMeasurement('current')
      temperature_units = folder.local_namespace.GetUnitsForMeasurement(
          'temperature')
      if not folder.local_namespace.namespace:
        # global namespace
        self.assertEqual(current_units['amperes'],
                         unit_lib.Unit('amperes', True))
        self.assertEqual(current_units['milliamperes'],
                         unit_lib.Unit('milliamperes'))
        self.assertEqual(temperature_units['kelvins'],
                         unit_lib.Unit('kelvins', True))
        self.assertEqual(temperature_units['degrees_celsius'],
                         unit_lib.Unit('degrees_celsius'))
        self.assertEqual(temperature_units['degrees_fahrenheit'],
                         unit_lib.Unit('degrees_fahrenheit'))

  def testParseUnitFoldersFromBadFile(self):
    bad_units = base_lib.PathParts(
        root=self.base_dir, relative_path='BAD/units/bad_units.yaml')
    unit_folders = parse.ParseUnitFoldersFromFiles([bad_units])

    self.assertLen(unit_folders, 1)
    unit_folder = unit_folders[0]
    self.assertTrue(
        unit_folder.HasFindingTypes([findings_lib.StandardUnitCountError]))
    self.assertTrue(
        unit_folder.HasFindingTypes([findings_lib.UnknownUnitTagError]))
    self.assertTrue(
        unit_folder.HasFindingTypes([findings_lib.DuplicateUnitDefinitionError
                                    ]))

  def testParseUnitFoldersFromBadFileWithSubfieldUniverse(self):
    subfield_folders = parse.ParseSubfieldFoldersFromFiles(
        [self.global_subfields_file, self.local_subfields_file])
    subfield_universe = subfield_lib.SubfieldUniverse(subfield_folders)

    bad_units = base_lib.PathParts(
        root=self.base_dir, relative_path='BAD/units/bad_units.yaml')
    unit_folders = parse.ParseUnitFoldersFromFiles(
        [bad_units], subfield_universe=subfield_universe)
    local_folder = unit_folders[0]
    self.assertTrue(
        local_folder.HasFindingTypes([findings_lib.UnknownMeasurementTypeError
                                     ]))

  def testParseSubfieldFoldersFromGlobalFileWithUnitValidation(self):
    unit_folders = parse.ParseUnitFoldersFromFiles([self.global_units_file])
    unit_universe = unit_lib.UnitUniverse(unit_folders)
    subfield_folders = parse.ParseSubfieldFoldersFromFiles(
        [self.global_subfields_file])
    local_folder = subfield_folders[0]

    local_folder.ValidateUnits(unit_universe)

    self.assertEmpty(local_folder.GetFindings())

  def testParseSubfieldFoldersFromBadFileWithUnitValidation(self):
    unit_folders = parse.ParseUnitFoldersFromFiles([self.global_units_file])
    unit_universe = unit_lib.UnitUniverse(unit_folders)
    bad_subfields = base_lib.PathParts(
        root=self.base_dir,
        relative_path='BAD/subfields/missing_unit_subfields.yaml')
    subfield_folders = parse.ParseSubfieldFoldersFromFiles([bad_subfields])
    local_folder = subfield_folders[0]

    local_folder.ValidateUnits(unit_universe)

    self.assertTrue(subfield_folders[0].HasFindingTypes(
        [findings_lib.MissingUnitError]))


if __name__ == '__main__':
  absltest.main()
