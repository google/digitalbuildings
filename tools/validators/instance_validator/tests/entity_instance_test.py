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
"""Tests for entity_instance.py."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from os import path
from typing import Dict, List
from unittest import mock

from absl.testing import absltest

from tests import test_constants
from validate import connection
from validate import entity_instance
from validate import field_translation
from validate import generate_universe
from validate import instance_parser
from validate import link
from yamlformat.validator import entity_type_lib
from yamlformat.validator import field_lib
from yamlformat.validator import presubmit_validate_types_lib

_DEFAULT_ONTOLOGY_LOCATION = test_constants.ONTOLOGY_ROOT
_TESTCASE_PATH = test_constants.TEST_INSTANCES

_INIT_CFG = instance_parser.ConfigMode.INITIALIZE
_UPDATE_CFG = instance_parser.ConfigMode.UPDATE

_ADD = instance_parser.EntityOperation.ADD
_UPDATE = instance_parser.EntityOperation.UPDATE
_DELETE = instance_parser.EntityOperation.DELETE

_CombValidator = entity_instance.CombinationValidator


def _ParserHelper(testpaths: List[str]) -> instance_parser.InstanceParser:
  parser = instance_parser.InstanceParser()
  for filepath in testpaths:
    parser.AddFile(filepath)
  parser.Finalize()
  return parser


def _Helper(testpaths: List[str]) -> Dict[str, entity_instance.EntityInstance]:
  return _ParserHelper(testpaths).GetEntities()


class EntityInstanceTest(absltest.TestCase):

  @classmethod
  def setUpClass(cls):
    super(cls, EntityInstanceTest).setUpClass()
    cls._universe = generate_universe.BuildUniverse(_DEFAULT_ONTOLOGY_LOCATION)
    cls._e_v_init = entity_instance.InstanceValidator(cls._universe, _INIT_CFG)
    cls._e_v_update = entity_instance.InstanceValidator(cls._universe,
                                                        _UPDATE_CFG)

  def testValidate_requiresEtagOnUpdate(self):
    config_u = presubmit_validate_types_lib.ConfigUniverse(
        # not validating against ontology so no universes setup
        entity_type_universe=None,
        field_universe=None,
        subfield_universe=None,
        state_universe=None,
        connection_universe=None,
        unit_universe=None)
    validator = entity_instance.InstanceValidator(config_u, _UPDATE_CFG)
    valid_instance = entity_instance.EntityInstance(
        _UPDATE,
        'FACILITIES/123456',
        etag='a12345',
        update_mask=['connections'])
    invalid_instance = entity_instance.EntityInstance(
        _UPDATE, 'FACILITIES/123456', update_mask=['connections'])

    is_valid = validator.Validate(valid_instance)

    self.assertFalse(validator.Validate(invalid_instance))
    self.assertTrue(is_valid)

  def testValidate_verifiesTypeAgainstNamespace(self):
    facilities_type_folder = entity_type_lib.EntityTypeFolder(
        folderpath='FACILITIES/entity_types')

    facilities_type_folder.AddFromConfig(
        documents=[{
            'BUILDING': {
                'id': '15204152342002794496',
                'description': 'This is a type for BUILDING facilities object'
            }
        }],
        # checks config path matches entity type folder but doesn't do file read
        config_filename='FACILITIES/entity_types/Facilities.yaml')

    config_u = presubmit_validate_types_lib.ConfigUniverse(
        entity_type_universe=entity_type_lib.EntityTypeUniverse(
            entity_type_folders=[facilities_type_folder]),
        field_universe=None,
        subfield_universe=None,
        state_universe=None,
        connection_universe=None,
        unit_universe=None)
    validator = entity_instance.InstanceValidator(config_u, _UPDATE_CFG)
    instance = entity_instance.EntityInstance(
        _UPDATE,
        'FACILITIES/123456',
        namespace='FACILITIES',
        type_name='BUILDING',
        etag='a12345',
        update_mask=['connections'])

    is_valid = validator.Validate(instance)

    self.assertTrue(is_valid)

  def testValidate_verifiesTypeAgainstNamespace_failsIfNotDefinedInUniverse(
      self):
    facilities_type_folder = entity_type_lib.EntityTypeFolder(
        folderpath='Carson/entity_types')

    facilities_type_folder.AddFromConfig(
        documents=[{
            'COORDINATE_BASIS': {
                'id': '17248142946209890304',
                'description': 'The coordinate basis for other entities'
            }
        }],
        # checks config path matches entity type folder but doesn't do file read
        config_filename='CARSON/entity_types/Carson.yaml')

    config_u = presubmit_validate_types_lib.ConfigUniverse(
        entity_type_universe=entity_type_lib.EntityTypeUniverse(
            entity_type_folders=[facilities_type_folder]),
        field_universe=None,
        subfield_universe=None,
        state_universe=None,
        connection_universe=None,
        unit_universe=None)
    validator = entity_instance.InstanceValidator(config_u, _UPDATE_CFG)
    instance = entity_instance.EntityInstance(
        _UPDATE,
        'FACILITIES/123456',
        namespace='FACILITIES',
        type_name='BUILDING',
        etag='a12345',
        update_mask=['connections'])

    is_valid = validator.Validate(instance)

    self.assertFalse(is_valid)

  def testValidate_verifiesTypeAgainstNamespace_badlyConfiguredUniverseFails(
      self):
    facilities_type_folder = entity_type_lib.EntityTypeFolder(
        folderpath='FOO/entity_types')

    facilities_type_folder.AddFromConfig(
        documents=[{
            'BUILDING': {
                'id': '15204152342002794496',
                'description': 'This is a type for BUILDING facilities object'
            }
        }],
        # file exists but does not match defined type folder
        # so validation will fail
        config_filename='FACILITIES/entity_types/Facilities.yaml')

    config_u = presubmit_validate_types_lib.ConfigUniverse(
        entity_type_universe=entity_type_lib.EntityTypeUniverse(
            entity_type_folders=[facilities_type_folder]),
        field_universe=None,
        subfield_universe=None,
        state_universe=None,
        connection_universe=None,
        unit_universe=None)
    validator = entity_instance.InstanceValidator(config_u, _UPDATE_CFG)
    instance = entity_instance.EntityInstance(
        _UPDATE,
        'FACILITIES/123456',
        namespace='FOO',
        type_name='BUILDING',
        etag='a12345',
        update_mask=['connections'])

    is_valid = validator.Validate(instance)

    self.assertFalse(is_valid)

  def testValidateBadEntityTypeFormat(self):
    parsed = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'bad_building_type.yaml')])
    parsed = dict(parsed)
    entity = dict(parsed[list(parsed)[0]])

    try:
      entity_instance.EntityInstance.FromYaml(entity)
    except TypeError as e:
      self.assertEqual(type(e), TypeError)
    else:
      self.fail('{0} was not raised'.format(TypeError))

  def testValidateBadEntityNamespace(self):
    parsed = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'bad_building_type_namespace.yaml')])
    parsed = dict(parsed)
    entity = dict(parsed[list(parsed)[0]])

    instance = entity_instance.EntityInstance.FromYaml(entity)

    self.assertFalse(self._e_v_init.Validate(instance))

  def testValidateRejectsUseOfAbstractType(self):
    parsed = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'bad_abstract_type.yaml')])
    parsed = dict(parsed)
    entity = dict(parsed[list(parsed)[0]])

    instance = entity_instance.EntityInstance.FromYaml(entity)

    self.assertFalse(self._e_v_init.Validate(instance))

  def testValidateBadEntityType(self):
    parsed = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'bad_building_type_entity.yaml')])
    parsed = dict(parsed)
    entity = dict(parsed[list(parsed)[0]])

    instance = entity_instance.EntityInstance.FromYaml(entity)

    self.assertFalse(self._e_v_init.Validate(instance))

  def testValidateMultipleTranslationWithFields(self):
    parsed = _Helper([
        path.join(_TESTCASE_PATH, 'GOOD',
                  'good_building_translation_fields.yaml')
    ])
    parsed = dict(parsed)
    entity = dict(parsed[list(parsed)[0]])

    instance = entity_instance.EntityInstance.FromYaml(entity)

    self.assertTrue(self._e_v_init.Validate(instance))

  def testValidateTranslationWithRequiredFieldMissing(self):
    parsed = _Helper([
        path.join(_TESTCASE_PATH, 'BAD',
                  'bad_translation_with_required_field_missing.yaml')
    ])
    parsed = dict(parsed)
    entity = dict(parsed[list(parsed)[0]])

    instance = entity_instance.EntityInstance.FromYaml(entity)

    self.assertFalse(self._e_v_init.Validate(instance))

  def testValidateTranslationWithRequiredFieldCloudDeviceIdMissing(self):
    try:
      _Helper([
          path.join(_TESTCASE_PATH, 'BAD',
                    'bad_translation_missing_cloud_device_id.yaml')
      ])
    except KeyError as e:
      self.assertEqual(type(e), KeyError)
    else:
      self.fail('{0} was not raised'.format(KeyError))

  def testValidateTranslation(self):
    parsed = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'good_translation.yaml')])

    parsed = dict(parsed)
    entity_hvac = dict(parsed[list(parsed)[0]])

    instance = entity_instance.EntityInstance.FromYaml(entity_hvac)

    self.assertTrue(self._e_v_init.Validate(instance))
    self.assertEqual(instance.cloud_device_id, 'foobar')

  def testValidateTranslationWithExplicitlyMissingField(self):
    parsed = _Helper([
        path.join(_TESTCASE_PATH, 'GOOD',
                  'good_translation_field_marked_missing.yaml')
    ])

    parsed = dict(parsed)
    entity_hvac = dict(parsed[list(parsed)[0]])
    instance = entity_instance.EntityInstance.FromYaml(entity_hvac)

    self.assertTrue(self._e_v_init.Validate(instance))

  def testValidateMultipleTranslationsWithIdenticalTypes(self):
    parsed = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'good_translation_identical.yaml')])
    parsed = dict(parsed)

    for entity_name in list(parsed):
      entity = dict(parsed[entity_name])
      instance = entity_instance.EntityInstance.FromYaml(entity)

      self.assertTrue(self._e_v_init.Validate(instance))

  def testValidateBadTranslationWithExtraField(self):
    parsed = _Helper([
        path.join(_TESTCASE_PATH, 'BAD',
                  'bad_translation_with_extra_field.yaml')
    ])

    parsed = dict(parsed)
    entity = dict(parsed[list(parsed)[0]])

    instance = entity_instance.EntityInstance.FromYaml(entity)

    self.assertFalse(self._e_v_init.Validate(instance))

  def testValidateTranslationUnits(self):
    parsed = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'good_translation_units.yaml')])
    parsed = dict(parsed)
    entity = dict(parsed[list(parsed)[0]])

    instance = entity_instance.EntityInstance.FromYaml(entity)

    self.assertTrue(self._e_v_init.Validate(instance))

  def testValidateTranslationUnitsAndStates(self):
    parsed = _Helper([
        path.join(_TESTCASE_PATH, 'GOOD',
                  'good_translation_units_and_states.yaml')
    ])
    parsed = dict(parsed)
    entity = dict(parsed[list(parsed)[0]])

    instance = entity_instance.EntityInstance.FromYaml(entity)

    self.assertTrue(self._e_v_init.Validate(instance))

  def testValidateBadTranslationStates(self):
    parsed = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'bad_translation_states.yaml')])
    parsed = dict(parsed)
    entity = dict(parsed[list(parsed)[0]])

    instance = entity_instance.EntityInstance.FromYaml(entity)

    self.assertFalse(self._e_v_init.Validate(instance))

  def testValidateBadLinkFields(self):
    parsed = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'bad_building_links_fields.yaml')])
    entity_instances = {}
    parsed = dict(parsed)
    for raw_entity in list(parsed):
      entity_parsed = dict(parsed[raw_entity])
      entity = entity_instance.EntityInstance.FromYaml(entity_parsed)
      entity_instances[raw_entity] = entity

    c_v = _CombValidator(self._universe, _INIT_CFG, entity_instances)
    self.assertFalse(c_v.Validate(entity_instances.get('ENTITY-NAME')))

  def testValidateBadLinkEntityName(self):
    parsed = _Helper([
        path.join(_TESTCASE_PATH, 'BAD', 'bad_building_links_entity_name.yaml')
    ])
    entity_instances = {}
    parsed = dict(parsed)
    for raw_entity in list(parsed):
      entity_parsed = dict(parsed[raw_entity])
      entity = entity_instance.EntityInstance.FromYaml(entity_parsed)
      entity_instances[raw_entity] = entity

    c_v = _CombValidator(self._universe, _INIT_CFG, entity_instances)
    self.assertFalse(c_v.Validate(entity_instances.get('ENTITY-NAME')))

  def testValidateBadLinkWrongField(self):
    parsed = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'bad_links_wrong_link.yaml')])
    entity_instances = {}
    parsed = dict(parsed)
    for raw_entity in list(parsed):
      entity_parsed = dict(parsed[raw_entity])
      entity = entity_instance.EntityInstance.FromYaml(entity_parsed)
      entity_instances[raw_entity] = entity

    c_v = _CombValidator(self._universe, _UPDATE, entity_instances)
    self.assertFalse(c_v.Validate(entity_instances.get('ENTITY-NAME')))

  @mock.patch.object(field_lib.FieldUniverse, 'IsFieldDefined')
  def testInstanceLinkSourceFieldValidation(self, mock_fn):
    field_u = field_lib.FieldUniverse([])
    config_u = presubmit_validate_types_lib.ConfigUniverse(
        None, field_u, None, None, None, None)
    mock_fn.side_effect = lambda f, ns: f == 'run_status'

    validator = entity_instance.InstanceValidator(config_u, _UPDATE_CFG)
    src_ok = entity_instance.EntityInstance(
        _UPDATE,
        'AHU-1',
        links=[link.Link('CTRL-1', {'run_status': 'run_status'})],
        etag='123')
    bad_src_field = entity_instance.EntityInstance(
        _UPDATE,
        'AHU-1',
        links=[link.Link('CTRL-1', {'nonexistent_status': 'run_status'})],
        etag='123')

    self.assertFalse(validator.Validate(bad_src_field))
    self.assertTrue(validator.Validate(src_ok))

  @mock.patch.object(presubmit_validate_types_lib, 'ConfigUniverse')
  def testGraphOrphanLinkOkOnUpdate(self, mock_universe):
    target = entity_instance.EntityInstance(
        _UPDATE,
        'AHU-1',
        links=[link.Link('CTRL-1', {'run_status_1': 'run_status'})],
        etag='123')
    validator = entity_instance.GraphValidator(mock_universe, _UPDATE_CFG,
                                               {'CTRL-1': target})

    self.assertTrue(validator.Validate(target))

  def testValidateBadLinkMissingField(self):
    parsed = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'bad_links_missing_field.yaml')])
    entity_instances = {}
    parsed = dict(parsed)
    for raw_entity in list(parsed):
      entity_parsed = dict(parsed[raw_entity])
      entity = entity_instance.EntityInstance.FromYaml(entity_parsed)
      entity_instances[raw_entity] = entity

    c_v = _CombValidator(self._universe, _INIT_CFG, entity_instances)
    self.assertFalse(c_v.Validate(entity_instances.get('ENTITY-NAME')))

  def testValidateGoodLinkEntityName(self):
    parsed = _Helper([path.join(_TESTCASE_PATH, 'GOOD', 'good_links.yaml')])
    entity_instances = {}
    parsed = dict(parsed)
    for raw_entity in list(parsed):
      entity_parsed = dict(parsed[raw_entity])
      entity = entity_instance.EntityInstance.FromYaml(entity_parsed)
      entity_instances[raw_entity] = entity

    c_v = _CombValidator(self._universe, _INIT_CFG, entity_instances)
    for _, instance in entity_instances.items():
      self.assertTrue(c_v.Validate(instance))

  def testValidateGoodLinkWithIncrementEntityName(self):
    parsed = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'good_links_increment.yaml')])
    entity_instances = {}
    parsed = dict(parsed)
    for raw_entity in list(parsed):
      entity_parsed = dict(parsed[raw_entity])
      entity = entity_instance.EntityInstance.FromYaml(entity_parsed)
      entity_instances[raw_entity] = entity

    c_v = _CombValidator(self._universe, _INIT_CFG, entity_instances)
    for _, instance in entity_instances.items():
      self.assertTrue(c_v.Validate(instance))

  def testValidateStates(self):
    parsed = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'good_translation_states.yaml')])
    parsed = dict(parsed)
    for raw_entity in list(parsed):
      entity_parsed = dict(parsed[raw_entity])
      entity = entity_instance.EntityInstance.FromYaml(entity_parsed)
      self.assertTrue(self._e_v_init.Validate(entity))

  def testGoodConnectionType(self):
    parsed = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'good_building_connections.yaml')])
    parsed = dict(parsed)
    entity_name = list(parsed)[0]
    entity = dict(parsed[entity_name])

    self.assertIn('connections', entity,
                  'entity does not have connections when expected')
    self.assertIsNotNone(self._universe.connection_universe,
                         'universe does not valid connections universe')

    instance = entity_instance.EntityInstance.FromYaml(entity)

    self.assertTrue(self._e_v_init.Validate(instance))

  def testBadConnectionType(self):
    parsed = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'bad_building_connections.yaml')])
    parsed = dict(parsed)
    entity_name = list(parsed)[0]
    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance.FromYaml(entity)

    self.assertFalse(self._e_v_init.Validate(instance))

  @mock.patch.object(presubmit_validate_types_lib, 'ConfigUniverse')
  def testGraphGoodConnection(self, mock_universe):
    target = entity_instance.EntityInstance(
        _ADD, 'VAV-123', connections=[connection.Connection('FEEDS', 'AHU-1')])
    source = entity_instance.EntityInstance(
        _ADD, 'AHU-1', connections=[connection.Connection('FEEDS', 'AHU-1')])
    instances = {'VAV-123': target, 'AHU-1': source}
    validator = entity_instance.GraphValidator(mock_universe, _INIT_CFG,
                                               instances)

    self.assertTrue(validator.Validate(target))

  @mock.patch.object(presubmit_validate_types_lib, 'ConfigUniverse')
  def testGraphOrphanConnection(self, mock_universe):
    target = entity_instance.EntityInstance(
        _ADD, 'VAV-123', connections=[connection.Connection('FEEDS', 'AHU-1')])
    validator = entity_instance.GraphValidator(mock_universe, _INIT_CFG,
                                               {'VAV-123': target})

    self.assertFalse(validator.Validate(target))

  @mock.patch.object(presubmit_validate_types_lib, 'ConfigUniverse')
  def testGraphOrphanConnectionOkOnUpdate(self, mock_universe):
    target = entity_instance.EntityInstance(
        _UPDATE,
        'VAV-123',
        connections=[connection.Connection('FEEDS', 'AHU-1')],
        etag='123')
    validator = entity_instance.GraphValidator(mock_universe, _UPDATE_CFG,
                                               {'VAV-123': target})

    self.assertTrue(validator.Validate(target))

  @mock.patch.object(presubmit_validate_types_lib, 'ConfigUniverse')
  @mock.patch.object(
      entity_instance.InstanceValidator, 'Validate', return_value=True)
  @mock.patch.object(
      entity_instance.GraphValidator, 'Validate', return_value=True)
  @mock.patch.object(entity_instance, 'EntityInstance')
  def testCombinedChecksInstanceAndGraph(self, mock_entity, mock_gv, mock_iv,
                                         mock_universe):
    validator = entity_instance.CombinationValidator(mock_universe, _UPDATE_CFG,
                                                     {})

    self.assertTrue(validator.Validate(mock_entity))
    mock_iv.assert_called_once_with(mock_entity)
    mock_gv.assert_called_once_with(mock_entity)

  @mock.patch.object(presubmit_validate_types_lib, 'ConfigUniverse')
  def testCombinedEtagRequirements(self, mock_universe):
    validator = entity_instance.CombinationValidator(mock_universe, _UPDATE_CFG,
                                                     {})
    no_tag = entity_instance.EntityInstance(_UPDATE, 'VAV-123')
    no_tag_delete = entity_instance.EntityInstance(_DELETE, 'VAV-123')

    self.assertFalse(validator.Validate(no_tag))
    self.assertTrue(validator.Validate(no_tag_delete))

  @mock.patch.object(presubmit_validate_types_lib, 'ConfigUniverse')
  def testInstanceBadOperationOnInit(self, mock_universe):
    entity = entity_instance.EntityInstance(_UPDATE, 'VAV-123', etag='1234')
    validator = entity_instance.InstanceValidator(mock_universe, _INIT_CFG)

    self.assertFalse(validator.Validate(entity))

  @mock.patch.object(
      entity_instance.InstanceValidator,
      '_FieldTranslationIsValid',
      return_value=True)
  @mock.patch.object(
      field_lib.FieldUniverse, 'IsFieldDefined', return_value=True)
  def testInstanceMultipleUnitsNotAllowed(self, mock_fn, mock_field_u):
    config_u = presubmit_validate_types_lib.ConfigUniverse(
        None, mock_field_u, None, None, None, None)
    mock_fn.side_effect = lambda f, ns: True
    entity = entity_instance.EntityInstance(
        _UPDATE,
        'VAV-123',
        etag='1234',
        translation={
            'foo_bar':
                field_translation.DimensionalValue(
                    std_field_name='foo/bar',
                    unit_field_name='foo/unit',
                    raw_field_name='foo/raw',
                    unit_mappings={'standard_unit_1': 'raw_unit_1'}),
            'foo_baz':
                field_translation.DimensionalValue(
                    std_field_name='foo/baz',
                    unit_field_name='bar/unit',
                    raw_field_name='bar/raw',
                    unit_mappings={'standard_unit_1': 'raw_unit_2'}),
        })
    validator = entity_instance.InstanceValidator(config_u, _UPDATE_CFG)

    self.assertFalse(validator.Validate(entity))


if __name__ == '__main__':
  absltest.main()
