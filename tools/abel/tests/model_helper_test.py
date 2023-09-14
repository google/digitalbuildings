"""Tests for model_helper module."""

# pylint: disable=g-importing-member
import os

from absl.testing import absltest

from model import import_helper
from model import model_helper
from model.entity_enumerations import EntityOperationType
from model.entity_enumerations import EntityUpdateMaskAttribute
from model.model_builder import Model
from tests.test_constants import TEST_RESOURCES

_GOOD_TEST_BUILDING_CONFIG_EXPORT = os.path.join(
    TEST_RESOURCES, 'good_test_building_config_export.yaml'
)
_GOOD_TEST_UPDATED_BUILDING_CONFIG = os.path.join(
    TEST_RESOURCES, 'good_test_building_config_update.yaml'
)
_BAD_TEST_UPDATED_BUILDING_CONFIG = os.path.join(
    TEST_RESOURCES, 'bad_test_building_config_update.yaml'
)


# pylint: disable=unused-variable
class ModelHelperTest(absltest.TestCase):

  def setUp(self):
    super().setUp()

    imported_current_building_config = (
        import_helper.DeserializeBuildingConfiguration(
            _GOOD_TEST_BUILDING_CONFIG_EXPORT
        )
    )
    unbuilt_current_model, operations = Model.Builder.FromBuildingConfig(
        imported_current_building_config[0], imported_current_building_config[1]
    )
    self.current_model = unbuilt_current_model.Build()
    imported_updated_building_config = (
        import_helper.DeserializeBuildingConfiguration(
            _GOOD_TEST_UPDATED_BUILDING_CONFIG
        )
    )
    unbuilt_updated_model, operations = Model.Builder.FromBuildingConfig(
        imported_updated_building_config[0], imported_updated_building_config[1]
    )
    self.updated_model = unbuilt_updated_model.Build()

  def testCompareReportingEntityandVirtualEntityRaisesTypeError(self):
    imported_bad_update_config = import_helper.DeserializeBuildingConfiguration(
        _BAD_TEST_UPDATED_BUILDING_CONFIG
    )
    unbuilt_bad_model, operations = Model.Builder.FromBuildingConfig(
        imported_bad_update_config[0], imported_bad_update_config[1]
    )
    bad_model = unbuilt_bad_model.Build()

    with self.assertRaises(TypeError):
      model_helper.DetermineEntityOperations(self.current_model, bad_model)

  def testDetermineAddOperation(self):
    operations = model_helper.DetermineEntityOperations(
        current_model=self.current_model, updated_model=self.updated_model
    )

    self.assertIn(
        EntityOperationType.ADD,
        [operation.operation for operation in operations],
    )

  def testDetermineReportingEntityUpdateMask(self):
    entity_guid = '8318f346-10b4-44f0-ac0b-bf7659510bfa'
    current_entity = self.current_model.GetEntity(entity_guid)
    updated_entity = self.updated_model.GetEntity(entity_guid)
    expected_updated_mask = [
        EntityUpdateMaskAttribute.TYPE,
        EntityUpdateMaskAttribute.CONNECTIONS,
        EntityUpdateMaskAttribute.TRANSLATION,
    ]

    actual_updated_mask = model_helper.DetermineReportingEntityUpdateMask(
        current_entity, updated_entity
    )

    self.assertEqual(actual_updated_mask, expected_updated_mask)

  def testDetermineVirtualEntityUpdateMask(self):
    entity_guid = '4931e096-dea5-4b81-86ad-234c6d07b978'
    current_entity = self.current_model.GetEntity(entity_guid)
    updated_entity = self.updated_model.GetEntity(entity_guid)
    expected_updated_mask = [
        EntityUpdateMaskAttribute.TYPE,
        EntityUpdateMaskAttribute.CONNECTIONS,
        EntityUpdateMaskAttribute.LINKS,
    ]

    actual_updated_mask = model_helper.DetermineVirtualEntityUpdateMask(
        current_entity, updated_entity
    )

    self.assertEqual(actual_updated_mask, expected_updated_mask)


if __name__ == '__main__':
  absltest.main()
