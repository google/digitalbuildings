"""Tests for model_helper module."""

# pylint: disable=g-importing-member
import os

from absl.testing import absltest

from model import import_helper
from model import model_helper
from model.entity_enumerations import EntityNamespace
from model.entity_enumerations import EntityOperationType
from model.entity_enumerations import EntityUpdateMaskAttribute
from model.model_builder import Model
from tests.test_constants import TEST_RESOURCES

_GOOD_TEST_BUILDING_CONFIG = os.path.join(
    TEST_RESOURCES, 'good_test_building_config.yaml'
)
_GOOD_TEST_BUILDING_CONFIG_EXPORT = os.path.join(
    TEST_RESOURCES, 'good_test_building_config_export.yaml'
)
_GOOD_TEST_UPDATED_BUILDING_CONFIG = os.path.join(
    TEST_RESOURCES, 'good_test_building_config_update.yaml'
)
_BAD_TEST_UPDATED_BUILDING_CONFIG = os.path.join(
    TEST_RESOURCES, 'bad_test_building_config_update.yaml'
)
_GOOD_PRE_SPLIT_CONFIG = os.path.join(
    TEST_RESOURCES, 'good_building_config_pre_split.yaml'
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
        self.current_model, self.updated_model, current_entity, updated_entity
    )

    self.assertEqual(actual_updated_mask, expected_updated_mask)

  def testDetermineReportingEntityUpdateMask_UpdatedFieldRawUnitValue(self):
    vav_4_guid = '15aa5434-3edc-47a9-8464-c01856d98db2'
    current_entity = self.current_model.GetEntity(vav_4_guid)
    updated_entity = self.updated_model.GetEntity(vav_4_guid)

    expected_updated_mask = [EntityUpdateMaskAttribute.TRANSLATION]

    actual_updated_mask = model_helper.DetermineReportingEntityUpdateMask(
        self.current_model, self.updated_model, current_entity, updated_entity
    )

    self.assertEqual(actual_updated_mask, expected_updated_mask)

  def testDetermineReportingEntityUpdateMask_UpdatedFieldRawStateValue(self):
    vav_5_guid = 'fb2d9f0d-a2b7-4a9b-beb9-3bade8ebda17'
    current_entity = self.current_model.GetEntity(vav_5_guid)
    updated_entity = self.updated_model.GetEntity(vav_5_guid)

    expected_updated_mask = [EntityUpdateMaskAttribute.TRANSLATION]

    actual_updated_mask = model_helper.DetermineReportingEntityUpdateMask(
        self.current_model, self.updated_model, current_entity, updated_entity
    )

    self.assertEqual(actual_updated_mask, expected_updated_mask)

  def testDetermineReportingEntityUpdateMask_UpdatedFieldPresentValuePath(self):
    vav_6_guid = '138d05e2-b7af-435c-9b6b-58c1af1adcbb'
    current_entity = self.current_model.GetEntity(vav_6_guid)
    updated_entity = self.updated_model.GetEntity(vav_6_guid)

    expected_updated_mask = [EntityUpdateMaskAttribute.TRANSLATION]

    actual_updated_mask = model_helper.DetermineReportingEntityUpdateMask(
        self.current_model, self.updated_model, current_entity, updated_entity
    )

    self.assertEqual(actual_updated_mask, expected_updated_mask)

  def testDetermineReportingEntityUpdateMask_UpdatedFieldUnitPath(self):
    vav_7_guid = '2768f729-b389-4ebd-8c43-4eb25c46cdf3'
    current_entity = self.current_model.GetEntity(vav_7_guid)
    updated_entity = self.updated_model.GetEntity(vav_7_guid)

    expected_updated_mask = [EntityUpdateMaskAttribute.TRANSLATION]

    actual_updated_mask = model_helper.DetermineReportingEntityUpdateMask(
        self.current_model, self.updated_model, current_entity, updated_entity
    )

    self.assertEqual(actual_updated_mask, expected_updated_mask)

  def testDetermineReportingEntityUpdateMask_UpdatedMissingField(self):
    vav_8_guid = 'e49b0687-e409-4a24-95d6-4629ed42e7b7'
    current_entity = self.current_model.GetEntity(vav_8_guid)
    updated_entity = self.updated_model.GetEntity(vav_8_guid)

    expected_updated_mask = [EntityUpdateMaskAttribute.TRANSLATION]

    actual_updated_mask = model_helper.DetermineReportingEntityUpdateMask(
        self.current_model, self.updated_model, current_entity, updated_entity
    )

    self.assertEqual(actual_updated_mask, expected_updated_mask)

  def testDetermineReportingEntityUpdateMask_UpdatedFieldIsMissing(self):
    vav_9_guid = '585cd867-f66a-4cca-abc1-ba0789abc7f0'
    current_entity = self.current_model.GetEntity(vav_9_guid)
    updated_entity = self.updated_model.GetEntity(vav_9_guid)

    expected_updated_mask = [EntityUpdateMaskAttribute.TRANSLATION]

    actual_updated_mask = model_helper.DetermineReportingEntityUpdateMask(
        self.current_model, self.updated_model, current_entity, updated_entity
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

  def testSplit(self):
    pre_split_building_config = import_helper.DeserializeBuildingConfiguration(
        _GOOD_PRE_SPLIT_CONFIG
    )
    post_split_building_config = import_helper.DeserializeBuildingConfiguration(
        _GOOD_TEST_BUILDING_CONFIG
    )
    unbuilt_pre_split_model, pre_split_operations = (
        Model.Builder.FromBuildingConfig(
            pre_split_building_config[0], pre_split_building_config[1]
        )
    )
    unbuilt_post_split_model, pre_split_operations = (
        Model.Builder.FromBuildingConfig(
            post_split_building_config[0], post_split_building_config[1]
        )
    )

    built_pre_split_model = unbuilt_pre_split_model.Build()
    built_post_split_model = unbuilt_post_split_model.Build()

    actual_split_model = model_helper.Split(
        built_pre_split_model, pre_split_operations, EntityNamespace.HVAC
    )[0]

    self.assertEqual(actual_split_model, built_post_split_model)


if __name__ == '__main__':
  absltest.main()
