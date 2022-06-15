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

_TESTCASE_PATH = test_constants.TEST_INSTANCES

_INIT_CFG = instance_parser.ConfigMode.INITIALIZE
_UPDATE_CFG = instance_parser.ConfigMode.UPDATE

_ADD = instance_parser.EntityOperation.ADD
_UPDATE = instance_parser.EntityOperation.UPDATE
_DELETE = instance_parser.EntityOperation.DELETE


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
    super(EntityInstanceTest, cls).setUpClass()
    cls.config_universe = generate_universe.BuildUniverse(
        use_simplified_universe=True)
    cls.init_validator = entity_instance.InstanceValidator(
        cls.config_universe, _INIT_CFG)
    cls.update_validator = entity_instance.InstanceValidator(
        cls.config_universe, _UPDATE_CFG)

  @mock.patch.object(
      entity_instance.InstanceValidator, 'Validate', return_value=True)
  @mock.patch.object(
      entity_instance.GraphValidator, 'Validate', return_value=True)
  @mock.patch.object(entity_instance, 'EntityInstance')
  def testCombinedChecksInstanceAndGraph(self, mock_entity, mock_gv, mock_iv):
    validator = entity_instance.CombinationValidator(self.config_universe,
                                                     _UPDATE_CFG, {})

    self.assertTrue(validator.Validate(mock_entity))
    mock_iv.assert_called_once_with(mock_entity)
    mock_gv.assert_called_once_with(mock_entity)

  def testValidate_requiresEtagOnUpdate(self):
    valid_instance = entity_instance.EntityInstance(
        _UPDATE,
        entity_id='FACILITIES/123456',
        guid='ENTITY-GUID',
        code='ENTITY-NAME',
        etag='a12345',
        update_mask=['connections'])
    invalid_instance = entity_instance.EntityInstance(
        _UPDATE,
        entity_id='FACILITIES/123456',
        guid='ENTITY-GUID',
        code='ENTITY-NAME',
        update_mask=['connections'])

    self.assertTrue(self.update_validator.Validate(valid_instance))
    self.assertFalse(self.update_validator.Validate(invalid_instance))

  def testValidate_verifiesTypeAgainstNamespace(self):
    instance = entity_instance.EntityInstance(
        _UPDATE,
        entity_id='FACILITIES/123456',
        guid='ENTITY-GUID',
        code='ENTITY-NAME',
        namespace='FACILITIES',
        type_name='BUILDING',
        etag='a12345',
        update_mask=['connections'])

    self.assertTrue(self.update_validator.Validate(instance))

  def testValidate_verifiesTypeAgainstNamespace_failsIfNotDefinedInUniverse(
      self):
    instance = entity_instance.EntityInstance(
        _UPDATE,
        entity_id='NOT_A_NAMESPACE/123456',
        guid='ENTITY-GUID',
        code='ENTITY-NAME',
        namespace='NOT_A_NAMESPACE',
        type_name='BUILDING',
        etag='a12345',
        update_mask=['connections'])

    is_valid = self.update_validator.Validate(instance)

    self.assertFalse(is_valid)

  def testValidate_verifiesTypeAgainstNamespace_badlyConfiguredUniverseFails(
      self):
    instance = entity_instance.EntityInstance(
        _UPDATE,
        entity_id='FACILITIES/123456',
        guid='ENTITY-GUID',
        code='ENTITY-NAME',
        namespace='FOO',
        type_name='BUILDING',
        etag='a12345',
        update_mask=['connections'])

    is_valid = self.update_validator.Validate(instance)

    self.assertFalse(is_valid)

  def testValidateBadEntityTypeFormat(self):
    parsed = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'bad_building_type.yaml')])
    entity_code = next(iter(parsed))
    entity = parsed[entity_code]

    try:
      entity_instance.EntityInstance.FromYaml(
          entity_code, entity, code_to_guid_map={})
    except TypeError as e:
      self.assertEqual(type(e), TypeError)
    else:
      self.fail(f'{TypeError} was not raised')

  def testInstanceRequiresEntityTypeToExist(self):
    instance = entity_instance.EntityInstance(
        _UPDATE,
        entity_id='FACILITIES/123456',
        guid='ENTITY-GUID',
        code='ENTITY-NAME',
        namespace='FACILITIES',
        type_name='LIGHTING/NOT_A_LAMP',
        etag='a12345',
        update_mask=['connections'])

    self.assertFalse(self.update_validator.Validate(instance))

  def testValidateBadEntityNamespace(self):
    parsed = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'bad_building_type_namespace.yaml')])
    entity_code, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_code, entity, code_to_guid_map={})

    self.assertFalse(self.init_validator.Validate(instance))

  def testValidateRejectsUseOfAbstractType(self):
    parsed = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'bad_abstract_type.yaml')])
    entity_code, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_code, entity, code_to_guid_map={})

    self.assertFalse(self.init_validator.Validate(instance))

  def testValidateBadEntityType(self):
    parsed = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'bad_building_type_entity.yaml')])
    entity_code, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_code, entity, code_to_guid_map={})

    self.assertFalse(self.init_validator.Validate(instance))

  def testValidateMultipleTranslationWithFields(self):
    parsed = _Helper([
        path.join(_TESTCASE_PATH, 'GOOD',
                  'good_building_translation_fields.yaml')
    ])
    entity_code, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_code, entity, code_to_guid_map={})

    self.assertTrue(self.init_validator.Validate(instance))

  def testValidateTranslationWithRequiredFieldMissing(self):
    parsed = _Helper([
        path.join(_TESTCASE_PATH, 'BAD',
                  'bad_translation_with_required_field_missing.yaml')
    ])
    entity_code, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_code, entity, code_to_guid_map={})

    self.assertFalse(self.init_validator.Validate(instance))

  def testValidatePassthroughTranslationWithRequiredFieldMissing(self):
    parsed = _Helper([
        path.join(
            _TESTCASE_PATH, 'BAD',
            'bad_passthrough_translation_with_required_field_missing.yaml')
    ])
    entity_code, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_code, entity, code_to_guid_map={})

    self.assertFalse(self.init_validator.Validate(instance))

  def testValidateTranslationWithRequiredFieldCloudDeviceIdMissing(self):
    try:
      _Helper([
          path.join(_TESTCASE_PATH, 'BAD',
                    'bad_translation_missing_cloud_device_id.yaml')
      ])
    except KeyError as e:
      self.assertEqual(type(e), KeyError)
    else:
      self.fail(f'{KeyError} was not raised')

  def testValidateTranslation(self):
    parsed = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'good_translation.yaml')])
    entity_code, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_code, entity, code_to_guid_map={})

    self.assertTrue(self.init_validator.Validate(instance))
    self.assertEqual(instance.cloud_device_id, 'foobar')

  def testValidateTranslationWithExplicitlyMissingField(self):
    parsed = _Helper([
        path.join(_TESTCASE_PATH, 'GOOD',
                  'good_translation_field_marked_missing.yaml')
    ])
    entity_code, entity = next(iter(parsed.items()))
    instance = entity_instance.EntityInstance.FromYaml(
        entity_code, entity, code_to_guid_map={})

    self.assertTrue(self.init_validator.Validate(instance))

  def testValidateMultipleTranslationsWithIdenticalTypes(self):
    parsed = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'good_translation_identical.yaml')])

    for entity_code, entity in parsed.items():
      instance = entity_instance.EntityInstance.FromYaml(
          entity_code, entity, code_to_guid_map={})

      self.assertTrue(self.init_validator.Validate(instance))

  def testValidateBadTranslationWithExtraField(self):
    parsed = _Helper([
        path.join(_TESTCASE_PATH, 'BAD',
                  'bad_translation_with_extra_field.yaml')
    ])
    entity_code, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_code, entity, code_to_guid_map={})

    self.assertFalse(self.init_validator.Validate(instance))

  def testValidateTranslationUnits(self):
    parsed = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'good_translation_units.yaml')])
    entity_code, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_code, entity, code_to_guid_map={})

    self.assertTrue(self.init_validator.Validate(instance))

  def testValidateTranslationUnitsAndStates(self):
    parsed = _Helper([
        path.join(_TESTCASE_PATH, 'GOOD',
                  'good_translation_units_and_states.yaml')
    ])
    entity_code, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_code, entity, code_to_guid_map={})

    self.assertTrue(self.init_validator.Validate(instance))

  def testValidateBadTranslationStates(self):
    parsed = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'bad_translation_states.yaml')])
    entity_code, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_code, entity, code_to_guid_map={})

    self.assertFalse(self.init_validator.Validate(instance))

  def testValidateGoodTranslationStatesList(self):
    parsed = _Helper([
        path.join(_TESTCASE_PATH, 'GOOD', 'good_translation_states_list.yaml')
    ])
    entity_code, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_code, entity, code_to_guid_map={})

    self.assertTrue(self.init_validator.Validate(instance))

  def testValidateBadTranslationStatesListWithDuplicate(self):
    parsed = _Helper([
        path.join(_TESTCASE_PATH, 'BAD',
                  'bad_translation_states_list_with_duplicate.yaml')
    ])
    entity_code, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_code, entity, code_to_guid_map={})

    self.assertFalse(self.init_validator.Validate(instance))

  def testValidateBadLinkFields(self):
    parsed = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'bad_building_links_fields.yaml')])
    entity_instances = {}
    for entity_code, entity_parsed in parsed.items():
      entity = entity_instance.EntityInstance.FromYaml(
          entity_code,
          entity_parsed,
          code_to_guid_map={'A-FOURTH-ENTITY': 'A-FOURTH-ENTITY-guid'})
      entity_instances[entity.guid] = entity

    combination_validator = entity_instance.CombinationValidator(
        self.config_universe, _INIT_CFG, entity_instances)
    self.assertFalse(
        combination_validator.Validate(
            entity_instances.get('ENTITY-NAME-guid')))

  def testValidateBadLinkEntityName(self):
    parsed = _Helper([
        path.join(_TESTCASE_PATH, 'BAD', 'bad_building_links_entity_name.yaml')
    ])
    entity_instances = {}
    for entity_code, entity_parsed in parsed.items():
      try:
        entity = entity_instance.EntityInstance.FromYaml(
            entity_code,
            entity_parsed,
            code_to_guid_map={'A-FOURTH-ENTITY': 'A-FOURTH-ENTITY-guid'})
        entity_instances[entity.guid] = entity
      except ValueError:
        continue

    self.assertNotIn('ENTITY-NAME-guid', entity_instances)

  def testValidateBadLinkWrongField(self):
    parsed = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'bad_links_wrong_link.yaml')])
    entity_instances = {}
    for entity_code, entity_parsed in parsed.items():
      entity = entity_instance.EntityInstance.FromYaml(
          entity_code,
          entity_parsed,
          code_to_guid_map={'A-FOURTH-ENTITY': 'A-FOURTH-ENTITY-guid'})
      entity_instances[entity.guid] = entity

    combination_validator = entity_instance.CombinationValidator(
        self.config_universe, _UPDATE, entity_instances)
    self.assertFalse(
        combination_validator.Validate(
            entity_instances.get('ENTITY-NAME-guid')))

  def testValidateBadLinkMissingField(self):
    parsed = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'bad_links_missing_field.yaml')])
    entity_instances = {}
    for entity_code, entity_parsed in parsed.items():
      entity = entity_instance.EntityInstance.FromYaml(
          entity_code,
          entity_parsed,
          code_to_guid_map={'A-FOURTH-ENTITY': 'A-FOURTH-ENTITY-guid'})
      entity_instances[entity.guid] = entity

    combination_validator = entity_instance.CombinationValidator(
        self.config_universe, _INIT_CFG, entity_instances)
    self.assertFalse(
        combination_validator.Validate(
            entity_instances.get('ENTITY-NAME-guid')))

  def testValidateGoodLinkEntityName(self):
    parsed = _Helper([path.join(_TESTCASE_PATH, 'GOOD', 'good_links.yaml')])
    entity_instances = {}
    for entity_code, entity_parsed in parsed.items():
      entity = entity_instance.EntityInstance.FromYaml(
          entity_code,
          entity_parsed,
          code_to_guid_map={'PHYSICAL-ENTITY': 'PHYSICAL-ENTITY-guid'})
      entity_instances[entity.guid] = entity

    combination_validator = entity_instance.CombinationValidator(
        self.config_universe, _INIT_CFG, entity_instances)
    for _, instance in entity_instances.items():
      self.assertTrue(combination_validator.Validate(instance))

  def testValidateGoodLinkWithIncrementEntityName(self):
    parsed = _Helper(
        # KW: this one is a entity_franken-type it definitely won't make sense
        [path.join(_TESTCASE_PATH, 'GOOD', 'good_links_increment.yaml')])
    entity_instances = {}
    for entity_code, entity_parsed in parsed.items():
      entity = entity_instance.EntityInstance.FromYaml(
          entity_code,
          entity_parsed,
          code_to_guid_map={'PHYSICAL-ENTITY': 'PHYSICAL-ENTITY-guid'})
      entity_instances[entity.guid] = entity

    combination_validator = entity_instance.CombinationValidator(
        self.config_universe, _INIT_CFG, entity_instances)
    for _, instance in entity_instances.items():
      self.assertTrue(combination_validator.Validate(instance))

  def testValidateGoodLinkToPassthroughEntity(self):
    parsed = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'good_links_passthrough.yaml')])
    entity_instances = {}
    for entity_code, entity_parsed in parsed.items():
      entity = entity_instance.EntityInstance.FromYaml(
          entity_code,
          entity_parsed,
          code_to_guid_map={'GATEWAY-ENTITY': 'GATEWAY-ENTITY-guid'})
      entity_instances[entity.guid] = entity

    combination_validator = entity_instance.CombinationValidator(
        self.config_universe, _INIT_CFG, entity_instances)
    for _, instance in entity_instances.items():
      self.assertTrue(combination_validator.Validate(instance))

  def testValidateGoodGuidFormat(self):
    parsed = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'good_guid_format.yaml')])
    entity_instances = {}
    for entity_guid, entity in parsed.items():
      instance = entity_instance.EntityInstance.FromYaml(
          entity_guid, entity, code_to_guid_map={})
      entity_instances[instance.guid] = instance

    combination_validator = entity_instance.CombinationValidator(
        self.config_universe, _INIT_CFG, entity_instances)
    for _, instance in entity_instances.items():
      self.assertTrue(combination_validator.Validate(instance))

  def testValidateStates(self):
    parsed = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'good_translation_states.yaml')])
    for entity_code, entity_parsed in parsed.items():
      entity = entity_instance.EntityInstance.FromYaml(
          entity_code, entity_parsed, code_to_guid_map={})
      self.assertTrue(self.init_validator.Validate(entity))

  def testGoodConnectionType(self):
    parsed = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'good_building_connections.yaml')])
    entity_code, entity = next(iter(parsed.items()))
    expected_connections = [
        connection.Connection('FEEDS', 'ANOTHER-ENTITY-guid'),
        connection.Connection('CONTAINS', 'A-THIRD-ENTITY-guid')
    ]

    self.assertIn('connections', entity,
                  'entity does not have connections when expected')
    self.assertIsNotNone(self.config_universe.connection_universe,
                         'universe does not have a valid connections universe')

    instance = entity_instance.EntityInstance.FromYaml(
        entity_code,
        entity,
        code_to_guid_map={
            'ANOTHER-ENTITY': 'ANOTHER-ENTITY-guid',
            'A-THIRD-ENTITY': 'A-THIRD-ENTITY-guid'
        })

    self.assertTrue(self.init_validator.Validate(instance))
    self.assertCountEqual(expected_connections, instance.connections)

  def testGoodConnectionList(self):
    parsed = _Helper([
        path.join(_TESTCASE_PATH, 'GOOD', 'good_building_connection_list.yaml')
    ])
    entity_code, entity = next(iter(parsed.items()))
    expected_connections = [
        connection.Connection('FEEDS', 'ANOTHER-ENTITY-guid'),
        connection.Connection('CONTAINS', 'ANOTHER-ENTITY-guid')
    ]

    self.assertIn('connections', entity,
                  'entity does not have connections when expected')
    self.assertIsNotNone(self.config_universe.connection_universe,
                         'universe does not have a valid connections universe')

    instance = entity_instance.EntityInstance.FromYaml(
        entity_code,
        entity,
        code_to_guid_map={'ANOTHER-ENTITY': 'ANOTHER-ENTITY-guid'})

    self.assertTrue(self.init_validator.Validate(instance))
    self.assertCountEqual(expected_connections, instance.connections)

  def testBadConnectionType(self):
    parsed = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'bad_building_connections.yaml')])
    entity_code, entity = next(iter(parsed.items()))
    instance = entity_instance.EntityInstance.FromYaml(
        entity_code,
        entity,
        code_to_guid_map={
            'ANOTHER-ENTITY': 'ANOTHER-ENTITY-guid',
            'A-THIRD-ENTITY': 'A-THIRD-ENTITY-guid'
        })

    self.assertFalse(self.init_validator.Validate(instance))

  def testInstanceLinkSourceFieldMustExist(self):
    src_ok = entity_instance.EntityInstance(
        _UPDATE,
        entity_id='CDM/123456',
        guid='AHU-1-guid',
        code='AHU-1',
        links=[link.Link('CTRL-1-guid', {'run_status': 'run_status'})],
        etag='123')
    bad_src_field = entity_instance.EntityInstance(
        _UPDATE,
        entity_id='CDM/123456',
        guid='AHU-1-guid',
        code='AHU-1',
        links=[link.Link('CTRL-1-guid', {'nonexistent_status': 'run_status'})],
        etag='123')

    self.assertFalse(self.update_validator.Validate(bad_src_field))
    self.assertTrue(self.update_validator.Validate(src_ok))

  def testGraphOrphanLinkOkOnUpdate(self):
    target = entity_instance.EntityInstance(
        _UPDATE,
        entity_id='CDM/123456',
        guid='AHU-1-guid',
        code='AHU-1',
        links=[link.Link('CTRL-1-guid', {'run_status_1': 'run_status'})],
        etag='123')
    validator = entity_instance.GraphValidator(self.config_universe,
                                               _UPDATE_CFG,
                                               {'CTRL-1-guid': target})

    self.assertTrue(validator.Validate(target))

  def testGraphGoodConnection(self):
    target = entity_instance.EntityInstance(
        _ADD,
        entity_id='CDM/123456',
        guid='VAV-123-guid',
        code='VAV-123',
        connections=[connection.Connection('FEEDS', 'AHU-1-guid')])
    source = entity_instance.EntityInstance(
        _ADD,
        entity_id='CDM/987654',
        guid='AHU-1-guid',
        code='AHU-1',
        connections=[connection.Connection('FEEDS', 'AHU-1-guid')])
    instances = {'VAV-123-guid': target, 'AHU-1-guid': source}
    validator = entity_instance.GraphValidator(self.config_universe, _INIT_CFG,
                                               instances)

    self.assertTrue(validator.Validate(target))

  def testGraphRejectsOrphanConnectionOnInit(self):
    target = entity_instance.EntityInstance(
        _ADD,
        entity_id='CDM/123456',
        guid='VAV-123-guid',
        code='VAV-123',
        connections=[connection.Connection('FEEDS', 'AHU-1-guid')])
    validator = entity_instance.GraphValidator(self.config_universe, _INIT_CFG,
                                               {'VAV-123-guid': target})

    self.assertFalse(validator.Validate(target))

  def testGraphAllowsOrphanConnectionOnInit(self):
    target = entity_instance.EntityInstance(
        _UPDATE,
        entity_id='CDM/123456',
        guid='VAV-123-guid',
        code='VAV-123',
        connections=[connection.Connection('FEEDS', 'AHU-1-guid')],
        etag='123')
    validator = entity_instance.GraphValidator(self.config_universe,
                                               _UPDATE_CFG,
                                               {'VAV-123-guid': target})

    self.assertTrue(validator.Validate(target))

  def testInstanceEtagNotRequiredForDelete(self):
    no_tag = entity_instance.EntityInstance(
        _UPDATE, entity_id='CDM/123456', guid='VAV-123-guid', code='VAV-123')
    no_tag_delete = entity_instance.EntityInstance(
        _DELETE, entity_id='CDM/123456', guid='VAV-123-guid', code='VAV-123')

    self.assertFalse(self.update_validator.Validate(no_tag))
    self.assertTrue(self.update_validator.Validate(no_tag_delete))

  def testInstanceOperationRequiredOnUpdate(self):
    entity = entity_instance.EntityInstance(
        _UPDATE,
        entity_id='CDM/123456',
        guid='VAV-123-guid',
        code='VAV-123',
        etag='1234')

    self.assertFalse(self.init_validator.Validate(entity))

  def testInstanceMultipleUnitsNotAllowed(self):
    entity = entity_instance.EntityInstance(
        _UPDATE,
        entity_id='CDM/123456',
        guid='VAV-123-guid',
        code='VAV-123',
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

    self.assertFalse(self.update_validator.Validate(entity))

  def testInstance_DimensionalTranslation_MissingUnitMapping(self):
    try:
      entity_instance.EntityInstance(
          _UPDATE,
          entity_id='CDM/123456',
          guid='VAV-123-guid',
          code='VAV-123',
          etag='1234',
          translation={
              'foo_bar':
                  field_translation.DimensionalValue(
                      std_field_name='foo/bar',
                      unit_field_name='foo/unit',
                      raw_field_name='foo/raw',
                      unit_mappings={}),
          })
    except ValueError as e:
      self.assertEqual(type(e), ValueError)
    else:
      self.fail(f'{ValueError} was not raised')

  def testInstance_DimensionalTranslation_UndefinedField(self):
    entity = entity_instance.EntityInstance(
        _UPDATE,
        entity_id='CDM/123456',
        guid='VAV-123-guid',
        code='VAV-123',
        etag='1234',
        translation={
            'UNDEFINED_UNIT':
                field_translation.DimensionalValue(
                    std_field_name='foo/bar',
                    unit_field_name='foo/unit',
                    raw_field_name='foo/raw',
                    unit_mappings={'foo': 'bar'})
        })

    self.assertFalse(self.update_validator.Validate(entity))

  def testInstance_DimensionalTranslation_FieldHasInvalidUnit(self):
    entity = entity_instance.EntityInstance(
        _UPDATE,
        entity_id='CDM/123456',
        guid='VAV-123-guid',
        code='VAV-123',
        etag='1234',
        translation={
            'return_water_temperature_sensor':
                field_translation.DimensionalValue(
                    std_field_name='foo/bar',
                    unit_field_name='foo/unit',
                    raw_field_name='foo/raw',
                    unit_mappings={'INVALID_SENSOR_UNIT': 'degF'})
        })

    self.assertFalse(self.update_validator.Validate(entity))

  def testInstance_DimensionalTranslation_FieldIsValid(self):
    entity = entity_instance.EntityInstance(
        _UPDATE,
        entity_id='CDM/123456',
        guid='VAV-123-guid',
        code='VAV-123',
        etag='1234',
        translation={
            'return_water_temperature_sensor':
                field_translation.DimensionalValue(
                    std_field_name='foo/bar',
                    unit_field_name='foo/unit',
                    raw_field_name='foo/raw',
                    unit_mappings={'degrees_fahrenheit': 'degF'})
        })

    self.assertTrue(self.update_validator.Validate(entity))

  def testInstance_MultiStateTranslation_MissingStates(self):
    try:
      entity_instance.EntityInstance(
          _UPDATE,
          entity_id='CDM/123456',
          guid='VAV-123-guid',
          code='VAV-123',
          etag='1234',
          translation={
              'foo_bar':
                  field_translation.MultiStateValue(
                      std_field_name='foo/bar',
                      raw_field_name='foo/raw',
                      states={})
          })
    except ValueError as e:
      self.assertEqual(type(e), ValueError)
    else:
      self.fail('{ValueError} was not raised')

  def testInstance_MultiStateTranslation_UndefinedField(self):
    entity = entity_instance.EntityInstance(
        _UPDATE,
        entity_id='CDM/123456',
        guid='VAV-123-guid',
        code='VAV-123',
        etag='1234',
        translation={
            'UNDEFINED_STATE':
                field_translation.MultiStateValue(
                    std_field_name='foo/bar',
                    raw_field_name='foo/raw',
                    states={'foo': 'bar'})
        })

    self.assertFalse(self.update_validator.Validate(entity))

  def testInstance_MultiStateTranslation_FieldHasInvalidState(self):
    entity = entity_instance.EntityInstance(
        _UPDATE,
        entity_id='CDM/123456',
        guid='VAV-123-guid',
        code='VAV-123',
        etag='1234',
        translation={
            'exhaust_air_damper_command':
                field_translation.MultiStateValue(
                    std_field_name='exhaust_air_damper_command',
                    raw_field_name='exhaust_air_damper_command',
                    states={'INVALID_STATE': '1'})
        })

    self.assertFalse(self.update_validator.Validate(entity))

  def testInstance_MultiStateTranslation_FieldIsValid(self):
    entity = entity_instance.EntityInstance(
        _UPDATE,
        entity_id='CDM/123456',
        guid='VAV-123-guid',
        code='VAV-123',
        etag='1234',
        translation={
            'exhaust_air_damper_command':
                field_translation.MultiStateValue(
                    std_field_name='exhaust_air_damper_command',
                    raw_field_name='exhaust_air_damper_command',
                    states={
                        'OPEN': '1',
                        'CLOSED': '0'
                    })
        })

    self.assertTrue(self.update_validator.Validate(entity))

  def testInstance_DimensionalValue_noUnitsExpected_noUnitsPasses(self):
    entity = entity_instance.EntityInstance(
        _UPDATE,
        entity_id='CDM/123456',
        guid='VAV-123-guid',
        code='VAV-123',
        etag='1234',
        translation={
            'line_powerfactor_sensor':
                field_translation.DimensionalValue(
                    std_field_name='foo/bar',
                    unit_field_name='foo/unit',
                    raw_field_name='foo/raw',
                    unit_mappings={'no_units': 'no_units'}),
        })
    self.assertTrue(self.update_validator.Validate(entity))

  def testInstance_DimensionalValue_unitsExpected_noUnitsFails(self):
    entity = entity_instance.EntityInstance(
        _UPDATE,
        entity_id='CDM/123456',
        guid='VAV-123-guid',
        code='VAV-123',
        etag='1234',
        translation={
            'zone_air_cooling_temperature_setpoint':
                field_translation.DimensionalValue(
                    std_field_name='foo/bar',
                    unit_field_name='foo/unit',
                    raw_field_name='foo/raw',
                    unit_mappings={'no_units': 'no_units'}),
        })
    self.assertFalse(self.update_validator.Validate(entity))

  def testValidate_EmptyCode_ReturnsFalse(self):
    entity = entity_instance.EntityInstance(
        _ADD, entity_id='CDM/123456', guid='VAV-123-guid', code='')

    self.assertFalse(self.init_validator.Validate(entity))

  def testValidate_EmptyGuid_ReturnsFalse(self):
    entity = entity_instance.EntityInstance(
        _ADD, entity_id='CDM/123456', guid='', code='VAV-123')

    self.assertFalse(self.init_validator.Validate(entity))

  def testFromYaml_MissingCodeAndGuid_RaisesValueError(self):
    entity_code = 'VAV-123'
    entity_yaml = {
        'id': 'CDM/123456',
    }

    with self.assertRaises(
        ValueError, msg='Entity block must contain either "code" or "guid".'):
      entity_instance.EntityInstance.FromYaml(
          entity_code, entity_yaml, code_to_guid_map={})

  def testFromYaml_ContainsCodeAndGuid_RaisesValueError(self):
    entity_code = 'VAV-123'
    entity_yaml = {
        'id': 'CDM/123456',
        'guid': 'VAV-123-guid',
        'code': entity_code,
    }

    with self.assertRaises(
        ValueError, msg='Entity block cannot contain both "code" and "guid".'):
      entity_instance.EntityInstance.FromYaml(
          entity_code, entity_yaml, code_to_guid_map={})

  def testFromYaml_KeyIsCode_ExpectedResults(self):
    entity_code = 'VAV-123'
    entity_guid = 'VAV-123-guid'
    entity_yaml = {
        'id': 'CDM/123456',
        'guid': entity_guid,
    }

    entity = entity_instance.EntityInstance.FromYaml(
        entity_code, entity_yaml, code_to_guid_map={})

    self.assertEqual(entity.guid, entity_guid)
    self.assertEqual(entity.code, entity_code)

  def testFromYaml_KeyIsGuid_ExpectedResults(self):
    entity_code = 'VAV-123'
    entity_guid = 'VAV-123-guid'
    entity_yaml = {
        'id': 'CDM/123456',
        'code': entity_code,
    }

    entity = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity_yaml, code_to_guid_map={})

    self.assertEqual(entity.guid, entity_guid)
    self.assertEqual(entity.code, entity_code)

  def testValidate_requiresGuidOnAdd(self):
    instance = entity_instance.EntityInstance(
        _ADD,
        entity_id='FACILITIES/123456',
        guid=None,
        code='ENTITY-NAME',
        namespace='FACILITIES',
        type_name='BUILDING',
        etag='a12345',
        update_mask=['connections'])

    self.assertFalse(self.update_validator.Validate(instance))

  def testValidate_requiresGuidOnUpdate(self):
    instance = entity_instance.EntityInstance(
        _UPDATE,
        entity_id='FACILITIES/123456',
        guid=None,
        code='ENTITY-NAME',
        namespace='FACILITIES',
        type_name='BUILDING',
        etag='a12345',
        update_mask=['connections'])

    self.assertFalse(self.update_validator.Validate(instance))

if __name__ == '__main__':
  absltest.main()
