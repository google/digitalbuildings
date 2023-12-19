# Copyright 2023 Google LLC
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
from typing import Dict, List, Tuple
from unittest import mock

from absl.testing import absltest
import strictyaml as syaml

from tests import test_constants
from validate import connection
from validate import entity_instance
from validate import field_translation
from validate import generate_universe
from validate import handler
from validate import instance_parser
from validate import link

_TESTCASE_PATH = test_constants.TEST_INSTANCES

_INIT_CFG = instance_parser.ConfigMode.INITIALIZE
_UPDATE_CFG = instance_parser.ConfigMode.UPDATE

_ADD = instance_parser.EntityOperation.ADD
_UPDATE = instance_parser.EntityOperation.UPDATE
_DELETE = instance_parser.EntityOperation.DELETE
_EXPORT = instance_parser.EntityOperation.EXPORT


# pylint: disable=line-too-long
# pylint: disable=protected-access
def _ParserHelper(testpaths: List[str]) -> instance_parser.InstanceParser:
  parser = instance_parser.InstanceParser()
  for filepath in testpaths:
    parser.AddFile(filepath)
  parser.Finalize()
  return parser


def _Helper(
    testpaths: List[str],
) -> Tuple[Dict[str, syaml.YAML], instance_parser.EntityOperation]:
  """Helper function for loading a list of building configuration filepaths.

  Args:
    testpaths: list of files to validate against

  Returns:
    entities: dict of entities keyed by guid; {<entity guid>: <entity dict>}
    default_operation: default operation corresponding to the ConfigMode

  Notes:
    <entity guid>: yaml block key; Str
    <entity dict>: yaml block attributes/properties; Dict
  """
  parser = _ParserHelper(testpaths)
  entities = parser.GetEntities()
  default_operation = handler.GetDefaultOperation(parser.GetConfigMode())
  return entities, default_operation


class EntityInstanceTest(absltest.TestCase):

  @classmethod
  def setUpClass(cls):
    super().setUpClass()
    cls.config_universe = generate_universe.BuildUniverse(
        use_simplified_universe=True
    )
    cls.init_validator = entity_instance.InstanceValidator(
        cls.config_universe, _INIT_CFG
    )
    cls.update_validator = entity_instance.InstanceValidator(
        cls.config_universe, _UPDATE_CFG
    )

  @mock.patch.object(
      entity_instance.InstanceValidator, 'Validate', return_value=True
  )
  @mock.patch.object(
      entity_instance.GraphValidator, 'Validate', return_value=True
  )
  @mock.patch.object(entity_instance, 'EntityInstance')
  def testCombinedChecksInstanceAndGraph(self, mock_entity, mock_gv, mock_iv):
    validator = entity_instance.CombinationValidator(
        self.config_universe, _UPDATE_CFG, {}
    )

    self.assertTrue(validator.Validate(mock_entity))
    # UDMI validation set to True by default.
    mock_iv.assert_called_once_with(mock_entity, True)
    mock_gv.assert_called_once_with(mock_entity)

  def testInstance_ValidEtagOnUpdate_Success(self):
    valid_instance = entity_instance.EntityInstance(
        _UPDATE,
        guid='ENTITY-GUID',
        code='ENTITY-NAME',
        etag='a12345',
        update_mask=['connections'],
    )

    self.assertTrue(self.update_validator.Validate(valid_instance))

  def testInstance_InValidEtagOnUpdate_Fails(self):
    invalid_instance = entity_instance.EntityInstance(
        _UPDATE,
        guid='ENTITY-GUID',
        code='ENTITY-NAME',
        update_mask=['connections'],
    )

    self.assertFalse(self.update_validator.Validate(invalid_instance))

  def testInstance_ValidType_Success(self):
    instance = entity_instance.EntityInstance(
        _UPDATE,
        guid='ENTITY-GUID',
        code='US-SEA-BLDG1',
        namespace='FACILITIES',
        type_name='BUILDING',
        etag='a12345',
        update_mask=['connections'],
    )

    self.assertTrue(self.update_validator.Validate(instance))

  def testInstance_InvalidFacilitiesFloorCode_Fails(self):
    instance = entity_instance.EntityInstance(
        _ADD,
        guid='ENTITY-GUID',
        code='UK-LON-X1-L01',
        namespace='FACILITIES',
        type_name='FLOOR',
        etag='a12345',
    )

    self.assertFalse(self.init_validator.Validate(instance))

  def testInstance_InvalidFacilitiesRoomCode_Fails(self):
    instance = entity_instance.EntityInstance(
        _ADD,
        guid='ENTITY-GUID',
        code='UK-LON-X1-L01-R25',
        namespace='FACILITIES',
        type_name='ROOM',
        etag='a12345',
    )

    self.assertFalse(self.init_validator.Validate(instance))

  def testInstance_ValidBuildingCode_Success(self):
    instance = entity_instance.EntityInstance(
        _ADD,
        guid='ENTITY-GUID',
        code='US-SEA-BLDG1',
        namespace='FACILITIES',
        type_name='BUILDING',
        etag='a12345',
    )

    self.assertTrue(self.init_validator.Validate(instance))

  def testInstance_ValidFacilitiesEntityCode_Success(self):
    instance = entity_instance.EntityInstance(
        _ADD,
        guid='ENTITY-GUID',
        code='US-SEA-B1-1-R25',
        namespace='FACILITIES',
        type_name='ROOM',
        etag='a12345',
    )

    self.assertTrue(self.init_validator.Validate(instance))

  def testInstance_InvalidFacilitiesBuildingCode_Fails(self):
    instance = entity_instance.EntityInstance(
        _ADD,
        guid='ENTITY-GUID',
        code='building-1',
        namespace='FACILITIES',
        type_name='BUILDING',
        etag='a12345',
    )

    self.assertFalse(self.init_validator.Validate(instance))

  def testInstance_InvalidNamespace_Fails(self):
    instance = entity_instance.EntityInstance(
        _UPDATE,
        guid='ENTITY-GUID',
        code='US-SEA-BLDG1',
        namespace='NOT_A_NAMESPACE',
        type_name='BUILDING',
        etag='a12345',
        update_mask=['connections'],
    )

    is_valid = self.update_validator.Validate(instance)

    self.assertFalse(is_valid)

  def testInstance_InvalidEntityTypeFormat_RaisesTypeError(self):
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'building_type.yaml')]
    )
    entity_guid = next(iter(parsed))
    entity = parsed[entity_guid]

    try:
      entity_instance.EntityInstance.FromYaml(
          entity_guid, entity, default_operation=default_operation
      )
    except TypeError as e:
      self.assertEqual(type(e), TypeError)
    else:
      self.fail(f'{TypeError} was not raised')

  def testInstance_RequiresEntityTypeToExistUpdate_Fails(self):
    """Test that the entity type exists."""
    instance = entity_instance.EntityInstance(
        _UPDATE,
        guid='ENTITY-GUID',
        code='ENTITY-NAME',
        namespace='FACILITIES',
        type_name='LIGHTING/NOT_A_LAMP',
        etag='a12345',
        update_mask=['connections'],
    )

    self.assertFalse(self.update_validator.Validate(instance))

  def testInstance_InvalidEntityNamespace_Fails(self):
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'building_type_namespace.yaml')]
    )
    entity_guid, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity, default_operation=default_operation
    )

    self.assertFalse(self.init_validator.Validate(instance))

  def testInstance_InvalidUseOfAbstractType_Fails(self):
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'abstract_type.yaml')]
    )
    entity_guid, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity, default_operation=default_operation
    )

    self.assertFalse(self.init_validator.Validate(instance))

  def testInstance_InvalidEntityType_Fails(self):
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'building_type_entity.yaml')]
    )
    entity_guid, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity, default_operation=default_operation
    )

    self.assertFalse(self.init_validator.Validate(instance))

  def testInstance_TranslationMissingStates_Fails(self):
    parsed, default_operation = _Helper(
        [
            path.join(
                _TESTCASE_PATH,
                'BAD',
                'translation_field_with_states_missing.yaml',
            )
        ]
    )
    entity_guid, entity = next(iter(parsed.items()))
    instance = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity, default_operation=default_operation
    )

    self.assertFalse(self.init_validator.Validate(instance))

  def testInstance_TranslationMissingUnits_Fails(self):
    parsed, default_operation = _Helper(
        [
            path.join(
                _TESTCASE_PATH,
                'BAD',
                'translation_field_with_units_missing.yaml',
            )
        ]
    )
    entity_guid, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity, default_operation=default_operation
    )

    self.assertFalse(self.init_validator.Validate(instance))

  def testInstance_ValidMultipleTranslationWithFields_Success(self):
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'building_translation_fields.yaml')]
    )
    entity_guid, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity, default_operation=default_operation
    )

    self.assertTrue(self.init_validator.Validate(instance))

  def testInstance_ExtraEnumeratedField_Fails(self):
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'entity_with_bad_enumeration.yaml')]
    )
    entity_guid, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity, default_operation=default_operation
    )

    self.assertFalse(self.init_validator.Validate(instance))

  def testInstance_InvalidTranslationRequiredFieldMissing_Fails(self):
    parsed, default_operation = _Helper(
        [
            path.join(
                _TESTCASE_PATH,
                'BAD',
                'translation_with_required_field_missing.yaml',
            )
        ]
    )
    entity_guid, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity, default_operation=default_operation
    )

    self.assertFalse(self.init_validator.Validate(instance))

  def testInstance_InvalidPassthroughTranslationFieldMissing_Fails(self):
    parsed, default_operation = _Helper(
        [
            path.join(
                _TESTCASE_PATH,
                'BAD',
                'translation_opt_field_marked_missing.yaml',
            )
        ]
    )
    entity_guid, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity, default_operation=default_operation
    )

    self.assertFalse(self.init_validator.Validate(instance))

  def testInstance_InvalidTranslationFieldCloudDeviceIdMissing_RaiesKeyError(
      self,
  ):
    try:
      _Helper(
          [
              path.join(
                  _TESTCASE_PATH,
                  'BAD',
                  'translation_missing_cloud_device_id.yaml',
              )
          ]
      )
    except KeyError as e:
      self.assertEqual(type(e), KeyError)
    else:
      self.fail(f'{KeyError} was not raised')

  def testInstanceValidator_InvalidCloudDeviceId(self):
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'entity_bad_cloud_device_id.yaml')]
    )
    entity_guid, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity, default_operation=default_operation
    )

    self.assertFalse(self.init_validator.Validate(instance))
    self.assertEqual(instance.cloud_device_id, 'bad_device_id')

  def testInstance_ValidTranslation_Success(self):
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'translation.yaml')]
    )
    entity_guid, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity, default_operation=default_operation
    )

    self.assertTrue(self.init_validator.Validate(instance))
    self.assertEqual(instance.cloud_device_id, '1234567890123456')

  def testInstance_ValidTranslationWithExplicitlyMissingReqField_Success(self):
    """Test that a MISSING required field is allowed."""
    parsed, default_operation = _Helper(
        [
            path.join(
                _TESTCASE_PATH,
                'GOOD',
                'translation_field_marked_missing.yaml',
            )
        ]
    )
    entity_guid, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity, default_operation=default_operation
    )

    self.assertTrue(self.init_validator.Validate(instance))

  def testInstance_InvalidEntityAllFieldTranslationsMarkedMissing_Failure(self):
    """Test that all translation fields not marked with PresenceMode as MISSING."""
    parsed, default_operation = _Helper(
        [
            path.join(
                _TESTCASE_PATH,
                'BAD',
                'translation_all_field_marked_missing.yaml',
            )
        ]
    )
    entity_guid, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity, default_operation=default_operation
    )

    self.assertFalse(self.init_validator.Validate(instance))

  def testInstance_ValidateMissingFieldOnGatewayEntity_Success(self):
    """Test that the MISSING fields on a gateway type are allowed."""
    parsed, default_operation = _Helper(
        [
            path.join(
                _TESTCASE_PATH,
                'GOOD',
                'translation_missing_fields_on_gateway.yaml',
            )
        ]
    )
    entity_guid, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity, default_operation=default_operation
    )

    self.assertTrue(self.init_validator.Validate(instance))

  def testInstance_ValidTranslationWithExplicityMissingOptField_Fails(self):
    """Test that a MISSING optional field is not allowed."""
    # parsed, default_operation = _Helper([])
    parsed, default_operation = _Helper(
        [
            path.join(
                _TESTCASE_PATH,
                'BAD',
                'translation_opt_field_marked_missing.yaml',
            )
        ]
    )
    entity_guid, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity, default_operation=default_operation
    )

    self.assertFalse(self.init_validator.Validate(instance))

  def testInstance_ValidMultipleTranslationsWithIdenticalTypes_Success(self):
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'translation_identical.yaml')]
    )
    entity_iter = iter(parsed.items())
    entity_1_guid, entity_1_block = next(entity_iter)
    entity_2_guid, entity_2_block = next(entity_iter)
    entity_3_guid, entity_3_block = next(entity_iter)

    entity_1 = entity_instance.EntityInstance.FromYaml(
        entity_1_guid, entity_1_block, default_operation=default_operation
    )
    entity_2 = entity_instance.EntityInstance.FromYaml(
        entity_2_guid, entity_2_block, default_operation=default_operation
    )
    entity_3 = entity_instance.EntityInstance.FromYaml(
        entity_3_guid, entity_3_block, default_operation=default_operation
    )

    self.assertTrue(self.init_validator.Validate(entity_1))
    self.assertTrue(self.init_validator.Validate(entity_2))
    self.assertTrue(self.init_validator.Validate(entity_3))

  def testInstance_InvalidTranslationExtraField_Fails(self):
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'translation_with_extra_field.yaml')]
    )
    entity_guid, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity, default_operation=default_operation
    )

    self.assertFalse(self.init_validator.Validate(instance))

  def testInstance_ValidTranslationUnits_Success(self):
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'translation_units.yaml')]
    )
    entity_guid, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity, default_operation=default_operation
    )

    self.assertTrue(self.init_validator.Validate(instance))

  def testInstance_ValidTranslationUnitsAndStates_Success(self):
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'translation_units_and_states.yaml')]
    )
    entity_guid, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity, default_operation=default_operation
    )

    self.assertTrue(self.init_validator.Validate(instance))

  def testInstance_InvalidUdmiUnitFieldName_Fails(self):
    parsed, default_operation = _Helper(
        [
            path.join(
                _TESTCASE_PATH,
                'BAD',
                'translation_invalid_udmi_unit_field_name.yaml',
            )
        ]
    )
    parsed_items = iter(parsed.items())
    entity_guid_1, entity_1 = next(parsed_items)
    entity_guid_2, entity_2 = next(parsed_items)

    instance1 = entity_instance.EntityInstance.FromYaml(
        entity_guid_1, entity_1, default_operation=default_operation
    )
    instance2 = entity_instance.EntityInstance.FromYaml(
        entity_guid_2, entity_2, default_operation=default_operation
    )

    self.assertFalse(self.init_validator.Validate(instance1, is_udmi=True))
    self.assertFalse(self.init_validator.Validate(instance2, is_udmi=True))

  def testInstance_InvalidUdmiPresentValueName_Fails(self):
    parsed, default_operation = _Helper(
        [
            path.join(
                _TESTCASE_PATH,
                'BAD',
                'translation_invalid_udmi_present_value_name.yaml',
            )
        ]
    )
    parsed_items = iter(parsed.items())
    entity_guid_1, entity_1 = next(parsed_items)
    entity_guid_2, entity_2 = next(parsed_items)
    entity_guid_3, entity_3 = next(parsed_items)

    instance1 = entity_instance.EntityInstance.FromYaml(
        entity_guid_1, entity_1, default_operation=default_operation
    )
    instance2 = entity_instance.EntityInstance.FromYaml(
        entity_guid_2, entity_2, default_operation=default_operation
    )
    instance3 = entity_instance.EntityInstance.FromYaml(
        entity_guid_3, entity_3, default_operation=default_operation
    )

    self.assertFalse(self.init_validator.Validate(instance1, is_udmi=True))
    self.assertFalse(self.init_validator.Validate(instance2, is_udmi=True))
    self.assertFalse(self.init_validator.Validate(instance3, is_udmi=True))

  def testInstance_MultipleUnitMappings_Fails(self):
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'translation_multiple_units.yaml')]
    )
    entity_guid, entity = next(iter(parsed.items()))

    with self.assertRaisesWithLiteralMatch(
        ValueError,
        expected_exception_message=(
            'There should be exactly 1 unit mapping in the translation for '
        )
        + 'field "zone_air_temperature_sensor".',
    ):
      entity_instance.EntityInstance.FromYaml(
          entity_guid, entity, default_operation=default_operation
      )

  def testInstance_ValidValueRange_Success(self):
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'translation_value_range.yaml')]
    )
    entity_guid, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity, default_operation=default_operation
    )

    self.assertTrue(self.init_validator.Validate(instance))

  def testInstance_ValueRangeWithNoUnits_Fails(self):
    parsed, default_operation = _Helper(
        [
            path.join(
                _TESTCASE_PATH,
                'BAD',
                'translation_value_range_with_no_units.yaml',
            )
        ]
    )
    entity_guid, entity = next(iter(parsed.items()))

    with self.assertRaisesWithLiteralMatch(
        ValueError,
        expected_exception_message=(
            'A value range cannot be provided without units in the translation '
        )
        + 'for field "zone_air_temperature_sensor".',
    ):
      entity_instance.EntityInstance.FromYaml(
          entity_guid, entity, default_operation=default_operation
      )

  def testInstance_InvalidValueRangeFormat_Fails(self):
    parsed, default_operation = _Helper(
        [
            path.join(
                _TESTCASE_PATH,
                'BAD',
                'translation_invalid_value_range_format.yaml',
            )
        ]
    )
    entity_guid, entity = next(iter(parsed.items()))

    with self.assertRaisesWithLiteralMatch(
        ValueError,
        expected_exception_message='Value range in the translation for field '
        + '"zone_air_temperature_sensor" should be formatted: <min>,<max>.',
    ):
      entity_instance.EntityInstance.FromYaml(
          entity_guid, entity, default_operation=default_operation
      )

  def testInstance_InvalidValueRangeOrder_Fails(self):
    parsed, default_operation = _Helper(
        [
            path.join(
                _TESTCASE_PATH,
                'BAD',
                'translation_invalid_value_range_order.yaml',
            )
        ]
    )
    entity_guid, entity = next(iter(parsed.items()))

    with self.assertRaisesWithLiteralMatch(
        ValueError,
        expected_exception_message='Value range in the translation for field '
        + '"zone_air_temperature_sensor" should have a min value that is less '
        + 'than the max value.',
    ):
      entity_instance.EntityInstance.FromYaml(
          entity_guid, entity, default_operation=default_operation
      )

  def testInstance_InvalidTranslationStates_Fails(self):
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'translation_states.yaml')]
    )
    entity_guid, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity, default_operation=default_operation
    )

    self.assertFalse(self.init_validator.Validate(instance))

  def testInstance_ValidTranslationStates_Success(self):
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'translation_states_list.yaml')]
    )
    entity_guid, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity, default_operation=default_operation
    )

    self.assertTrue(self.init_validator.Validate(instance))

  def testInstance_InvalidTranslationStatesDuplicate_Fails(self):
    parsed, default_operation = _Helper(
        [
            path.join(
                _TESTCASE_PATH,
                'BAD',
                'translation_states_list_with_duplicate.yaml',
            )
        ]
    )
    entity_guid, entity = next(iter(parsed.items()))

    instance = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity, default_operation=default_operation
    )

    self.assertFalse(self.init_validator.Validate(instance))

  def testInstance_InvalidTranslationStateMissingValue_Fails(self):
    parsed, default_operation = _Helper(
        [
            path.join(
                _TESTCASE_PATH,
                'BAD',
                'entity_missing_state_mapping_value.yaml',
            )
        ]
    )
    entity_guid, entity = next(iter(parsed.items()))

    with self.assertRaisesWithLiteralMatch(
        ValueError,
        expected_exception_message=(
            'States must have defined string key and value pairs'
        ),
    ):
      entity_instance.EntityInstance.FromYaml(
          entity_guid, entity, default_operation=default_operation
      )

  def testInstance_InvalidLinkFields_Fails(self):
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'building_links_fields.yaml')]
    )

    entity_instances = {}
    for entity_guid, entity_parsed in parsed.items():
      entity = entity_instance.EntityInstance.FromYaml(
          entity_guid, entity_parsed, default_operation=default_operation
      )
      entity_instances[entity.guid] = entity
    combination_validator = entity_instance.CombinationValidator(
        self.config_universe, _INIT_CFG, entity_instances
    )

    self.assertFalse(
        combination_validator.Validate(entity_instances.get('ENTITY-NAME-GUID'))
    )

  def testInstance_InvalidLinkEntityName_Fails(self):
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'building_links_entity_name.yaml')]
    )

    entity_instances = {}
    for entity_guid, entity_parsed in parsed.items():
      try:
        entity = entity_instance.EntityInstance.FromYaml(
            entity_guid, entity_parsed, default_operation=default_operation
        )
        entity_instances[entity.guid] = entity
      except ValueError:
        continue
    combination_validator = entity_instance.CombinationValidator(
        self.config_universe, _INIT_CFG, entity_instances
    )

    self.assertFalse(
        combination_validator.Validate(entity_instances.get('ENTITY-NAME-GUID'))
    )

  def testInstance_InvalidLinkFieldWrong_Fails(self):
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'links_wrong_link.yaml')]
    )

    entity_instances = {}
    for entity_guid, entity_parsed in parsed.items():
      entity = entity_instance.EntityInstance.FromYaml(
          entity_guid, entity_parsed, default_operation=default_operation
      )
      entity_instances[entity.guid] = entity
    combination_validator = entity_instance.CombinationValidator(
        self.config_universe, _UPDATE, entity_instances
    )

    self.assertFalse(
        combination_validator.Validate(entity_instances.get('ENTITY-NAME-GUID'))
    )

  def testInstance_InvalidLinkFieldMissing_Fails(self):
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'links_missing_field.yaml')]
    )

    entity_instances = {}
    for entity_guid, entity_parsed in parsed.items():
      entity = entity_instance.EntityInstance.FromYaml(
          entity_guid, entity_parsed, default_operation=default_operation
      )
      entity_instances[entity.guid] = entity
    combination_validator = entity_instance.CombinationValidator(
        self.config_universe, _INIT_CFG, entity_instances
    )

    self.assertFalse(
        combination_validator.Validate(entity_instances.get('ENTITY-NAME-GUID'))
    )

  def testInstance_TypeInstanceWithNoFields_Fails(self):
    parsed, default_operation = _Helper(
      [path.join(_TESTCASE_PATH, 'BAD', 'type_expecting_fields.yaml')]
    )

    bad_entity_guid, bad_entity_parsed = next(iter(parsed.items()))
    bad_entity = entity_instance.EntityInstance.FromYaml(
      bad_entity_guid, bad_entity_parsed, default_operation=default_operation
    )

    self.assertFalse(self.init_validator.Validate(bad_entity))

  def testInstance_ValidLinkEntityName_Success(self):
    parsed, default_operation = _Helper(
      [path.join(_TESTCASE_PATH, 'GOOD', 'links.yaml')]
    )

    entity_instances = {}
    for entity_guid, entity_parsed in parsed.items():
      entity = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity_parsed, default_operation=default_operation
      )
      entity_instances[entity.guid] = entity
    combination_validator = entity_instance.CombinationValidator(
      self.config_universe, _INIT_CFG, entity_instances
    )

    for _, instance in entity_instances.items():
      self.assertTrue(combination_validator.Validate(instance))

  def testInstance_ValidGoodLinkWithIncrementEntityName_Success(self):
    parsed, default_operation = _Helper(
        # KW: this one is a entity_franken-type it definitely won't make sense
        [path.join(_TESTCASE_PATH, 'GOOD', 'links_increment.yaml')]
    )

    entity_instances = {}
    for entity_guid, entity_parsed in parsed.items():
      entity = entity_instance.EntityInstance.FromYaml(
          entity_guid, entity_parsed, default_operation=default_operation
      )
      entity_instances[entity.guid] = entity
    combination_validator = entity_instance.CombinationValidator(
        self.config_universe, _INIT_CFG, entity_instances
    )

    for _, instance in entity_instances.items():
      self.assertTrue(combination_validator.Validate(instance))

  def testInstance_MissingSourceFieldLink_Failure(self):
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'missing_link_in_source_entity.yaml')]
    )

    entity_instances = {}
    for entity_guid, entity_parsed in parsed.items():
      entity = entity_instance.EntityInstance.FromYaml(
          entity_guid, entity_parsed, default_operation=default_operation
      )
      entity_instances[entity.guid] = entity
    combination_validator = entity_instance.CombinationValidator(
        self.config_universe, _INIT_CFG, entity_instances
    )
    invalid_instance = entity_instances.get('VIRTUAL-ENTITY-GUID')

    self.assertFalse(combination_validator.Validate(invalid_instance))

  def testInstance_ValidLinkToPassthroughEntity_Success(self):
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'links_passthrough.yaml')]
    )

    entity_instances = {}
    for entity_guid, entity_parsed in parsed.items():
      entity = entity_instance.EntityInstance.FromYaml(
          entity_guid, entity_parsed, default_operation=default_operation
      )
      entity_instances[entity.guid] = entity
    combination_validator = entity_instance.CombinationValidator(
        self.config_universe, _INIT_CFG, entity_instances
    )

    for _, instance in entity_instances.items():
      self.assertTrue(combination_validator.Validate(instance))

  def testInstance_ValidGoodGuidFormat_Success(self):
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'guid_format.yaml')]
    )

    entity_instances = {}
    for entity_guid, entity in parsed.items():
      instance = entity_instance.EntityInstance.FromYaml(
          entity_guid, entity, default_operation=default_operation
      )
      entity_instances[instance.guid] = instance
    combination_validator = entity_instance.CombinationValidator(
        self.config_universe, _INIT_CFG, entity_instances
    )

    for _, instance in entity_instances.items():
      self.assertTrue(combination_validator.Validate(instance))

  def testInstance_ValidateStates_Success(self):
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'translation_states.yaml')]
    )
    entity_iter = iter(parsed.items())
    entity_1_guid, entity_1_block = next(entity_iter)
    entity_2_guid, entity_2_block = next(entity_iter)

    entity_1 = entity_instance.EntityInstance.FromYaml(
        entity_1_guid, entity_1_block, default_operation=default_operation
    )
    entity_2 = entity_instance.EntityInstance.FromYaml(
        entity_2_guid, entity_2_block, default_operation=default_operation
    )

    self.assertTrue(self.init_validator.Validate(entity_1))
    self.assertTrue(self.init_validator.Validate(entity_2))

  def testInstance_GoodConnectionType_Success(self):
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'building_connections.yaml')]
    )

    entity_guid, entity = next(iter(parsed.items()))
    expected_connections = [
        connection.Connection('FEEDS', 'ANOTHER-ENTITY-GUID'),
        connection.Connection('CONTAINS', 'A-THIRD-ENTITY-GUID'),
    ]
    instance = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity, default_operation=default_operation
    )

    self.assertIn(
        'connections', entity, 'entity does not have connections when expected'
    )
    self.assertIsNotNone(
        self.config_universe.connection_universe,
        'universe does not have a valid connections universe',
    )
    self.assertTrue(self.init_validator.Validate(instance))
    self.assertCountEqual(expected_connections, instance.connections)

  def testInstance_ValidConnection_Success(self):
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'building_connection_list.yaml')]
    )

    entity_guid, entity = next(iter(parsed.items()))
    expected_connections = [
        connection.Connection('FEEDS', 'ANOTHER-ENTITY-GUID'),
        connection.Connection('CONTAINS', 'ANOTHER-ENTITY-GUID'),
    ]

    self.assertIn(
        'connections', entity, 'entity does not have connections when expected'
    )
    self.assertIsNotNone(
        self.config_universe.connection_universe,
        'universe does not have a valid connections universe',
    )

    instance = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity, default_operation=default_operation
    )

    self.assertTrue(self.init_validator.Validate(instance))
    self.assertCountEqual(expected_connections, instance.connections)

  def testInstance_InvalidConnectionType_Fails(self):
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'building_connections.yaml')]
    )

    entity_guid, entity = next(iter(parsed.items()))
    instance = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity, default_operation=default_operation
    )

    self.assertFalse(self.init_validator.Validate(instance))

  def testInstance_ValidLinkSourceField_Success(self):
    src_ok = entity_instance.EntityInstance(
        _UPDATE,
        guid='AHU-1-GUID',
        code='AHU-1',
        links=[link.Link('CTRL-1-GUID', {'run_status': 'run_status'})],
        etag='123',
    )

    self.assertTrue(self.update_validator.Validate(src_ok))

  def testInstance_InvalidLinkSourceField_Fails(self):
    src_field = entity_instance.EntityInstance(
        _UPDATE,
        guid='AHU-1-GUID',
        code='AHU-1',
        links=[link.Link('CTRL-1-GUID', {'nonexistent_status': 'run_status'})],
        etag='123',
    )

    self.assertFalse(self.update_validator.Validate(src_field))

  def testGraph_OrphanLinkOkOnUpdate_Success(self):
    target = entity_instance.EntityInstance(
        _UPDATE,
        guid='AHU-1-GUID',
        code='AHU-1',
        links=[link.Link('CTRL-1-GUID', {'run_status_1': 'run_status'})],
        etag='123',
    )
    validator = entity_instance.GraphValidator(
        self.config_universe, _UPDATE_CFG, {'CTRL-1-GUID': target}
    )

    self.assertTrue(validator.Validate(target))

  def testGraph_GoodConnection_Success(self):
    target = entity_instance.EntityInstance(
        _ADD,
        guid='VAV-123-GUID',
        code='VAV-123',
        connections=[connection.Connection('FEEDS', 'AHU-1-GUID')],
    )
    source = entity_instance.EntityInstance(
        _ADD,
        guid='AHU-1-GUID',
        code='AHU-1',
        connections=[connection.Connection('FEEDS', 'AHU-1-GUID')],
    )
    instances = {'VAV-123-GUID': target, 'AHU-1-GUID': source}
    validator = entity_instance.GraphValidator(
        self.config_universe, _INIT_CFG, instances
    )

    self.assertTrue(validator.Validate(target))

  def testGraph_RejectsOrphanConnectionOnInit_Fails(self):
    target = entity_instance.EntityInstance(
        _ADD,
        guid='VAV-123-GUID',
        code='VAV-123',
        connections=[connection.Connection('FEEDS', 'AHU-1-GUID')],
    )
    validator = entity_instance.GraphValidator(
        self.config_universe, _INIT_CFG, {'VAV-123-GUID': target}
    )

    self.assertFalse(validator.Validate(target))

  def testGraph_DoesNotAllowOrphanConnectionOnUpdate_Fails(self):
    target = entity_instance.EntityInstance(
        _UPDATE,
        guid='VAV-123-GUID',
        code='VAV-123',
        connections=[connection.Connection('FEEDS', 'AHU-1-GUID')],
        etag='123',
    )
    validator = entity_instance.GraphValidator(
        self.config_universe, _UPDATE_CFG, {'VAV-123-GUID': target}
    )

    self.assertFalse(validator.Validate(target))

  def testInstance_EtagRequiredForUpdate_Fails(self):
    no_tag_update = entity_instance.EntityInstance(
        _UPDATE, guid='VAV-123-GUID', code='VAV-123'
    )

    self.assertFalse(self.update_validator.Validate(no_tag_update))

  def testInstance_EtagRequiredForDelete_Success(self):
    no_tag_delete = entity_instance.EntityInstance(
        _DELETE, guid='VAV-123-GUID', code='VAV-123'
    )

    self.assertFalse(self.update_validator.Validate(no_tag_delete))

  def testInstance_OperationRequiredOnUpdate_Fails(self):
    entity = entity_instance.EntityInstance(
        _UPDATE, guid='VAV-123-GUID', code='VAV-123', etag='1234'
    )

    self.assertFalse(self.init_validator.Validate(entity))

  def testInstance_MultipleUnitsNotAllowed_Fails(self):
    entity = entity_instance.EntityInstance(
        _UPDATE,
        guid='VAV-123-GUID',
        code='VAV-123',
        etag='1234',
        namespace='GATEWAYS',
        type_name='PASSTHROUGH',
        translation={
            'foo_bar': field_translation.DimensionalValue(
                std_field_name='foo/bar',
                unit_field_name='foo/unit',
                raw_field_name='foo/raw',
                unit_mapping={'standard_unit_1': 'raw_unit_1'},
            ),
            'foo_baz': field_translation.DimensionalValue(
                std_field_name='foo/baz',
                unit_field_name='bar/unit',
                raw_field_name='bar/raw',
                unit_mapping={'standard_unit_1': 'raw_unit_2'},
            ),
        },
    )

    self.assertFalse(self.update_validator.Validate(entity))

  def testDimensionalTranslationMissingUnitMapping_ReturnsValueError(self):
    try:
      entity_instance.EntityInstance(
          _UPDATE,
          guid='VAV-123-GUID',
          code='VAV-123',
          etag='1234',
          translation={
              'foo_bar': field_translation.DimensionalValue(
                  std_field_name='foo/bar',
                  unit_field_name='foo/unit',
                  raw_field_name='foo/raw',
                  unit_mapping={},
              ),
          },
      )
    except ValueError as e:
      self.assertEqual(type(e), ValueError)
    else:
      self.fail(f'{ValueError} was not raised')

  def testInstance_InvalidDimensionalTranslationField_Fails(self):
    entity = entity_instance.EntityInstance(
        _UPDATE,
        guid='VAV-123-GUID',
        code='VAV-123',
        etag='1234',
        namespace='GATEWAYS',
        type_name='PASSTHROUGH',
        translation={
            'UNDEFINED_UNIT': field_translation.DimensionalValue(
                std_field_name='foo/bar',
                unit_field_name='foo/unit',
                raw_field_name='foo/raw',
                unit_mapping={'foo': 'bar'},
            )
        },
    )

    self.assertFalse(self.update_validator.Validate(entity))

  def testInstance_InvalidDimensionalTranslationFieldUnit_Fails(self):
    # pylint: disable=line-too-long
    entity = entity_instance.EntityInstance(
        _UPDATE,
        guid='VAV-123-GUID',
        code='VAV-123',
        etag='1234',
        namespace='GATEWAYS',
        type_name='PASSTHROUGH',
        translation={
            'return_water_temperature_sensor': (
                field_translation.DimensionalValue(
                    std_field_name='foo/bar',
                    unit_field_name='foo/unit',
                    raw_field_name='foo/raw',
                    unit_mapping={'INVALID_SENSOR_UNIT': 'degF'},
                )
            )
        },
    )

    self.assertFalse(self.update_validator.Validate(entity))

  def testInstance_ValidDimensionalValueTranslationField_Success(self):
    # pylint: disable=line-too-long
    entity = entity_instance.EntityInstance(
        _UPDATE,
        guid='VAV-123-GUID',
        code='VAV-123',
        etag='1234',
        namespace='GATEWAYS',
        type_name='PASSTHROUGH',
        cloud_device_id='2619178366980754',
        translation={
            'return_water_temperature_sensor': (
                field_translation.DimensionalValue(
                    std_field_name='return_water_temperature_sensor',
                    unit_field_name=(
                        'pointset.points.return_water_temperature_sensor.units'
                    ),
                    raw_field_name=(
                        'points.return_water_temperature_sensor.present_value'
                    ),
                    unit_mapping={'degrees_fahrenheit': 'degF'},
                )
            )
        },
    )

    self.assertTrue(self.update_validator.Validate(entity))

  def testInstance_DimensionalValueInvalidUnitMappingTranslationField_Fails(
      self,
  ):
    # pylint: disable=line-too-long
    entity = entity_instance.EntityInstance(
        _UPDATE,
        guid='VAV-123-GUID',
        code='VAV-123',
        etag='1234',
        namespace='GATEWAYS',
        type_name='PASSTHROUGH',
        cloud_device_id='2619178366980754',
        translation={
            'return_water_temperature_sensor': (
                field_translation.DimensionalValue(
                    std_field_name='return_water_temperature_sensor',
                    unit_field_name=(
                        'pointset.points.return_water_temperature_sensor.units'
                    ),
                    raw_field_name=(
                        'points.return_water_temperature_sensor.present_value'
                    ),
                    unit_mapping={'invalid_unit': 'invalid_unit'},
                )
            )
        },
    )

    self.assertFalse(self.update_validator.Validate(entity))

  def testInstance_DimensionalValueNoUnitsExpected_Success(self):
    entity = entity_instance.EntityInstance(
        _UPDATE,
        guid='VAV-123-GUID',
        code='VAV-123',
        etag='1234',
        namespace='GATEWAYS',
        type_name='PASSTHROUGH',
        cloud_device_id='2619178366980754',
        translation={
            'line_powerfactor_sensor': field_translation.DimensionalValue(
                std_field_name='line_powerfactor_sensor',
                unit_field_name='pointset.points.line_powerfactor_sensor.units',
                raw_field_name='points.line_powerfactor_sensor.present_value',
                unit_mapping={'no_units': 'no_units'},
            ),
        },
    )

    self.assertTrue(self.update_validator.Validate(entity))

  def testInstance_DimensionalValueUnitsExpected_Fails(self):
    entity = entity_instance.EntityInstance(
        _UPDATE,
        guid='VAV-123-GUID',
        code='VAV-123',
        etag='1234',
        namespace='GATEWAYS',
        type_name='PASSTHROUGH',
        translation={
            'zone_air_cooling_temperature_setpoint': (
                field_translation.DimensionalValue(
                    std_field_name='foo/bar',
                    unit_field_name='foo/unit',
                    raw_field_name='foo/raw',
                    unit_mapping={'no_units': 'no_units'},
                )
            ),
        },
    )

    self.assertFalse(self.update_validator.Validate(entity))

  def testInstance_FieldExpectedAsDimensionalValue_Fails(self):
    entity = entity_instance.EntityInstance(
        _UPDATE,
        guid='VAV-123-GUID',
        code='VAV-123',
        etag='1234',
        namespace='GATEWAYS',
        type_name='PASSTHROUGH',
        translation={
            'zone_air_cooling_temperature_setpoint': (
                field_translation.NonDimensionalValue(
                    std_field_name='foo/bar',
                    raw_field_name='foo/raw',
                )
            ),
        },
    )

    self.assertFalse(self.update_validator.Validate(entity))

  def testInstance_oneOfThreeFieldsIsInvalid_Fails(self):
    entity = entity_instance.EntityInstance(
        _UPDATE,
        guid='VAV-123-GUID',
        code='VAV-123',
        etag='1234',
        namespace='GATEWAYS',
        type_name='PASSTHROUGH',
        cloud_device_id='2619178366980754',
        translation={
            'line_powerfactor_sensor': field_translation.DimensionalValue(
                std_field_name='line_powerfactor_sensor',
                unit_field_name='pointset.points.line_powerfactor_sensor.units',
                raw_field_name='points.line_powerfactor_sensor.present_value',
                unit_mapping={'no_units': 'no_units'},
            ),
            'return_water_temperature_sensor': (
                field_translation.NonDimensionalValue(
                    std_field_name='return_water_temperature_sensor',
                    raw_field_name=(
                        'points.return_water_temperature_sensor.present_value'
                    ),
                )
            ),
            'exhaust_air_damper_command': field_translation.MultiStateValue(
                std_field_name='exhaust_air_damper_command',
                raw_field_name='exhaust_air_damper_command',
                states={'OPEN': '1', 'CLOSED': '0'},
            ),
        },
    )

    self.assertFalse(self.update_validator.Validate(entity))

  def testInstance_EntityWithNonDimensionalValue_InstantiatesNonDimensionalValueObjectSuccessfully(
      self,
  ):
    parsed, default_operation = _Helper(
        [
            path.join(
                _TESTCASE_PATH,
                'GOOD',
                'entity_with_non_dimensional_value.yaml',
            )
        ]
    )
    entity_guid, entity_parsed = next(iter(parsed.items()))

    entity = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity_parsed, default_operation=default_operation
    )

    self.assertIsInstance(
        entity.translation['model_label'],
        field_translation.NonDimensionalValue,
    )

  def testInstance_EntityWithNonDimensionalValue_ValidatesSuccessfully(self):
    parsed, default_operation = _Helper(
        [
            path.join(
                _TESTCASE_PATH,
                'GOOD',
                'entity_with_non_dimensional_value.yaml',
            )
        ]
    )
    entity_guid, entity_parsed = next(iter(parsed.items()))

    entity = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity_parsed, default_operation=default_operation
    )

    self.assertTrue(self.init_validator.Validate(entity))

  def testInstance_MultiStateTranslationMissingStates_RaisesValueError(self):
    try:
      entity_instance.EntityInstance(
          _UPDATE,
          guid='VAV-123-GUID',
          code='VAV-123',
          etag='1234',
          namespace='GATEWAYS',
          type_name='PASSTHROUGH',
          translation={
              'foo_bar': field_translation.MultiStateValue(
                  std_field_name='foo/bar', raw_field_name='foo/raw', states={}
              )
          },
      )
    except ValueError as e:
      self.assertEqual(type(e), ValueError)
    else:
      self.fail('{ValueError} was not raised')

  def testInstance_MultiStateTranslationUndefinedField_Fails(self):
    entity = entity_instance.EntityInstance(
        _UPDATE,
        guid='VAV-123-GUID',
        code='VAV-123',
        etag='1234',
        namespace='GATEWAYS',
        type_name='PASSTHROUGH',
        translation={
            'UNDEFINED_STATE': field_translation.MultiStateValue(
                std_field_name='foo/bar',
                raw_field_name='foo/raw',
                states={'foo': 'bar'},
            )
        },
    )

    self.assertFalse(self.update_validator.Validate(entity))

  def testInstance_InvalidMultiStateTranslationFieldState_Fails(self):
    entity = entity_instance.EntityInstance(
        _UPDATE,
        guid='VAV-123-GUID',
        code='VAV-123',
        etag='1234',
        namespace='GATEWAYS',
        type_name='PASSTHROUGH',
        translation={
            'exhaust_air_damper_command': field_translation.MultiStateValue(
                std_field_name='exhaust_air_damper_command',
                raw_field_name='exhaust_air_damper_command',
                states={'INVALID_STATE': '1'},
            )
        },
    )

    self.assertFalse(self.update_validator.Validate(entity))

  def testInstance_ValidMultiStateTranslationField_Success(self):
    entity = entity_instance.EntityInstance(
        _UPDATE,
        guid='VAV-123-GUID',
        code='VAV-123',
        etag='1234',
        namespace='GATEWAYS',
        type_name='PASSTHROUGH',
        cloud_device_id='2619178366980754',
        translation={
            'exhaust_air_damper_command': field_translation.MultiStateValue(
                std_field_name='exhaust_air_damper_command',
                raw_field_name='exhaust_air_damper_command',
                states={'OPEN': '1', 'CLOSED': '0'},
            )
        },
    )

    self.assertTrue(self.update_validator.Validate(entity))

  def testValidate_EmptyCode_Fails(self):
    entity = entity_instance.EntityInstance(
        _ADD, guid='VAV-123-GUID', code='VAV-123'
    )

    self.assertFalse(self.init_validator.Validate(entity))

  def testValidate_EmptyGuid_Fails(self):
    entity = entity_instance.EntityInstance(_ADD, guid='', code='VAV-123')

    self.assertFalse(self.init_validator.Validate(entity))

  def testFromYaml_EntityBlockMissingCodeAndGuid_RaisesValueError(self):
    entity_guid = 'VAV-123-GUID'
    entity_yaml = {}

    with self.assertRaisesWithLiteralMatch(
        ValueError,
        expected_exception_message=(
            'Keys "code" and "guid" missing from entity block. Fix this by'
            ' adding one of these keys to the entity definition.'
        ),
    ):
      entity_instance.EntityInstance.FromYaml(
          entity_guid, entity_yaml, default_operation=_EXPORT
      )

  def testFromYaml_EntityBlockContainsCodeAndGuid_RaisesValueError(self):
    entity_guid = 'VAV-123-GUID'
    entity_yaml = {'guid': entity_guid, 'code': 'VAV-123'}

    with self.assertRaisesWithLiteralMatch(
        ValueError,
        expected_exception_message=(
            'Entity block cannot contain both "code" and "guid".'
        ),
    ):
      entity_instance.EntityInstance.FromYaml(
          entity_guid, entity_yaml, default_operation=_EXPORT
      )

  def testFromYaml_KeyIsCode_Fails(self):
    # this test should now fail as entity_instance enforces entities keyed by
    # guid
    with self.assertRaises(ValueError):
      entity_code = 'VAV-123'
      entity_guid = 'VAV-123-GUID'
      entity_yaml = {'guid': entity_guid}

      # this will raise a ValueError as entity must be keyed by guid; using
      # presence of code as a proxy
      entity_instance.EntityInstance.FromYaml(
          entity_code, entity_yaml, default_operation=_EXPORT
      )

  def testFromYaml_KeyIsGuid_Success(self):
    entity_code = 'VAV-123'
    entity_guid = 'VAV-123-GUID'
    entity_yaml = {'code': entity_code}

    entity = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity_yaml, default_operation=_EXPORT
    )

    self.assertEqual(entity.guid, entity_guid)
    self.assertEqual(entity.code, entity_code)

  def testValidate_RequiresGuidOnAdd_Fails(self):
    instance = entity_instance.EntityInstance(
        _ADD,
        guid=None,
        code='ENTITY-NAME',
        namespace='FACILITIES',
        type_name='BUILDING',
        etag='a12345',
        update_mask=['connections'],
    )

    self.assertFalse(self.update_validator.Validate(instance))

  def testValidate_RequiresGuidOnUpdate_Fails(self):
    instance = entity_instance.EntityInstance(
        _UPDATE,
        guid=None,
        code='ENTITY-NAME',
        namespace='FACILITIES',
        type_name='BUILDING',
        etag='a12345',
        update_mask=['connections'],
    )

    self.assertFalse(self.update_validator.Validate(instance))

  def testValidate_UpdateEntityTypeOnly_Success(self):
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'update_entity_type_only.yaml')]
    )
    entity_guid, entity_parsed = next(iter(parsed.items()))

    entity = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity_parsed, default_operation=default_operation
    )

    self.assertTrue(self.update_validator.Validate(entity))

  def testValidate_UpdateEntityTypeAndTranslations_Success(self):
    parsed, default_operation = _Helper(
        [
            path.join(
                _TESTCASE_PATH,
                'GOOD',
                'update_entity_type_and_translations.yaml',
            )
        ]
    )
    entity_guid, entity_parsed = next(iter(parsed.items()))

    entity = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity_parsed, default_operation=default_operation
    )

    self.assertTrue(self.update_validator.Validate(entity))

  def testValidate_UpdateEntityType_Fails(self):
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'update_entity_type.yaml')]
    )
    entity_guid, entity = next(iter(parsed.items()))

    entity = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity, default_operation=default_operation
    )

    self.assertFalse(self.update_validator.Validate(entity))

  def testValidate_UpdateEntityClearType_Fails(self):
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'BAD', 'update_entity_clear_type.yaml')]
    )
    entity_guid, entity = next(iter(parsed.items()))

    entity = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity, default_operation=default_operation
    )

    self.assertFalse(self.update_validator.Validate(entity))

  def testValidate_GoodUpdateOperationDefaultExport_Success(self):
    parsed, default_operation = _Helper(
        [
            path.join(
                _TESTCASE_PATH,
                'GOOD',
                'update_no_operation_default_export.yaml',
            )
        ]
    )

    entity_instances = {}
    for entity_guid, entity_parsed in parsed.items():
      entity = entity_instance.EntityInstance.FromYaml(
          entity_guid, entity_parsed, default_operation=default_operation
      )
      entity_instances[entity_guid] = entity
    combination_validator = entity_instance.CombinationValidator(
        self.config_universe, _UPDATE_CFG, entity_instances
    )

    self.assertTrue(
        combination_validator.Validate(entity_instances['PHYSICAL-ENTITY-GUID'])
    )
    self.assertEqual(entity_instances['VIRTUAL-ENTITY-GUID'].operation, _UPDATE)
    self.assertTrue(
        combination_validator.Validate(entity_instances['VIRTUAL-ENTITY-GUID'])
    )
    self.assertEqual(
        entity_instances['PHYSICAL-ENTITY-GUID'].operation, _EXPORT
    )

  def testValidate_UpdateCloudDeviceID_Fails(self):
    instance = entity_instance.EntityInstance(
        _UPDATE,
        guid='ENTITY-GUID',
        code='ENTITY-NAME',
        namespace='FACILITIES',
        type_name='BUILDING',
        etag='a12345',
        cloud_device_id='CLOUD-DEVICE-ID',
        update_mask=['cloud_device_id'],
    )

    self.assertFalse(self.update_validator.Validate(instance))

  def testValidate_EntityWithCloudDeviceIdMissingTranslation_Fails(self):
    parsed, default_operation = _Helper(
        [
            path.join(
                _TESTCASE_PATH,
                'BAD',
                'cloud_device_id_but_missing_translation.yaml',
            )
        ]
    )
    entity_guid, entity_block = next(iter(parsed.items()))

    entity = entity_instance.EntityInstance.FromYaml(
        entity_guid, entity_block, default_operation=default_operation
    )

    self.assertFalse(self.init_validator.Validate(entity))

  def testValidate_GoodStatesCaseSensitivity_Success(self):
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'states_case_sensitive.yaml')]
    )

    entity_instances = {}
    for entity_guid, entity_parsed in parsed.items():
      entity = entity_instance.EntityInstance.FromYaml(
          entity_guid, entity_parsed, default_operation=default_operation
      )
      entity_instances[entity_guid] = entity
    combination_validator = entity_instance.CombinationValidator(
        self.config_universe, _INIT_CFG, entity_instances
    )

    self.assertTrue(
        combination_validator.Validate(entity_instances['FC2-1-1-GUID'])
    )

  def testValidate_BadStatesCaseSensitivity_Failure(self):
    # The example states_case_insensitive.yaml is used in instance validator and
    # this (entity instance) test. Case-insensitive is allowed to pass;
    # however, case-sensitivity is enforced between concrete and ontology
    # specifications
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'states_case_insensitive.yaml')]
    )

    entity_instances = {}
    for entity_guid, entity_parsed in parsed.items():
      entity = entity_instance.EntityInstance.FromYaml(
          entity_guid, entity_parsed, default_operation=default_operation
      )
      entity_instances[entity_guid] = entity
    combination_validator = entity_instance.CombinationValidator(
        self.config_universe, _INIT_CFG, entity_instances
    )

    self.assertFalse(
        combination_validator.Validate(entity_instances['FC2-1-1-GUID'])
    )

  def testValidate_BuildingConfigEntityWithId_Success(self):
    parsed, default_operation = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'bc_entity_with_id.yaml')]
    )
    entity_iter = iter(parsed.items())
    entity_1_guid, entity_1_block = next(entity_iter)
    entity_2_guid, entity_2_block = next(entity_iter)

    entity_1 = entity_instance.EntityInstance.FromYaml(
        entity_1_guid, entity_1_block, default_operation=default_operation
    )
    entity_2 = entity_instance.EntityInstance.FromYaml(
        entity_2_guid, entity_2_block, default_operation=default_operation
    )

    self.assertTrue(self.init_validator.Validate(entity_1))
    self.assertFalse(entity_instance.IsEntityIdPresent(entity_1))
    self.assertTrue(self.init_validator.Validate(entity_2))
    self.assertTrue(entity_instance.IsEntityIdPresent(entity_2))
    self.assertEqual(
        entity_2.entity_id,
        parsed['US-SEA-BLDG1-GUID'].get(instance_parser.ENTITY_ID_KEY),
    )

  def testPrivateFieldTranslationIsValid_BaseDefinedFieldNotCoveredByValidation_Fails(
      self,
  ):
    as_written_field_name = 'zone_air_cooling_temperature_setpoint'
    ft = field_translation.DefinedField(
        std_field_name='foo/bar',
        raw_field_name='foo/raw',
    )
    entity = entity_instance.EntityInstance(
        _UPDATE,
        guid='VAV-123-GUID',
        code='VAV-123',
        etag='1234',
        namespace='GATEWAYS',
        type_name='PASSTHROUGH',
        translation={
            as_written_field_name: ft,
        },
    )

    entity_type = self.config_universe.GetEntityType(
        entity.namespace, entity.type_name
    )
    qualified_field_name = entity_instance._GetAllowedField(
        self.config_universe, as_written_field_name, entity_type
    )

    self.assertFalse(
        self.update_validator._FieldTranslationIsValid(
            qualified_field_name, ft, entity
        )
    )

  def testPrivateValidateStates_FieldTranslationNotCoveredByValidation_Fails(
      self,
  ):
    as_written_field_name = 'return_water_temperature_sensor'
    ft = field_translation.DimensionalValue(
        std_field_name='return_water_temperature_sensor',
        unit_field_name='pointset.points.return_water_temperature_sensor.units',
        raw_field_name='points.return_water_temperature_sensor.present_value',
        unit_mapping={'degrees_fahrenheit': 'degF'},
    )

    entity = entity_instance.EntityInstance(
        _UPDATE,
        guid='VAV-123-GUID',
        code='VAV-123',
        etag='1234',
        namespace='GATEWAYS',
        type_name='PASSTHROUGH',
        translation={
            as_written_field_name: ft,
        },
    )

    entity_type = self.config_universe.GetEntityType(
        entity.namespace, entity.type_name
    )
    qualified_field_name = entity_instance._GetAllowedField(
        self.config_universe, as_written_field_name, entity_type
    )

    self.assertFalse(
        self.update_validator._ValidateStates(qualified_field_name, ft, entity)
    )

  def testPrivateValidateUnits_FieldTranslationNotCoveredByValidation_Fails(
      self,
  ):
    as_written_field_name = 'exhaust_air_damper_command'
    ft = field_translation.MultiStateValue(
        std_field_name='exhaust_air_damper_command',
        raw_field_name='exhaust_air_damper_command',
        states={'OPEN': '1', 'CLOSED': '0'},
    )

    entity = entity_instance.EntityInstance(
        _UPDATE,
        guid='VAV-123-GUID',
        code='VAV-123',
        etag='1234',
        namespace='GATEWAYS',
        type_name='PASSTHROUGH',
        translation={
            as_written_field_name: ft,
        },
    )

    entity_type = self.config_universe.GetEntityType(
        entity.namespace, entity.type_name
    )
    qualified_field_name = entity_instance._GetAllowedField(
        self.config_universe, as_written_field_name, entity_type
    )

    self.assertFalse(
        self.update_validator._ValidateUnits(qualified_field_name, ft, entity)
    )


if __name__ == '__main__':
  absltest.main()
