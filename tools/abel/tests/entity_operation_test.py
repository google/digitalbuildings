"""Tests from ABEL model entity operation class."""

# pylint: disable=g-importing-member
from absl.testing import absltest
from model.entity import ReportingEntity
from model.entity_enumerations import EntityOperationType
from model.entity_enumerations import EntityUpdateMaskAttribute
from model.entity_operation import EntityOperation
from tests.test_constants import TEST_REPORTING_ENTITY_DICT


class EntityOperationTest(absltest.TestCase):

  def setUp(self):
    super().setUp()
    self.test_entity = ReportingEntity.FromDict(TEST_REPORTING_ENTITY_DICT)

  def testEntityOperationInitAdd(self):
    test_entity_operation = EntityOperation(
        entity=self.test_entity, operation=EntityOperationType.ADD
    )
    self.assertIsInstance(test_entity_operation, EntityOperation)
    self.assertEqual(test_entity_operation.entity, self.test_entity)
    self.assertEqual(test_entity_operation.operation, EntityOperationType.ADD)
    self.assertIsNone(test_entity_operation.update_mask)

  def testEntityOperationInitUpdate(self):
    test_entity_operation = EntityOperation(
        entity=self.test_entity,
        operation=EntityOperationType.UPDATE,
        update_mask=[EntityUpdateMaskAttribute.CONNECTIONS],
    )
    self.assertIsInstance(test_entity_operation, EntityOperation)
    self.assertEqual(test_entity_operation.entity, self.test_entity)
    self.assertEqual(
        test_entity_operation.operation, EntityOperationType.UPDATE
    )
    self.assertSequenceEqual(
        test_entity_operation.update_mask,
        [EntityUpdateMaskAttribute.CONNECTIONS],
    )

  def testEntityOperationInitUpdateFails(self):
    with self.assertRaises(AssertionError):
      EntityOperation(
          entity=self.test_entity, operation=EntityOperationType.UPDATE
      )

  def testEntityOperationEquality(self):
    test_entity_operation_1 = EntityOperation(
        entity=self.test_entity,
        operation=EntityOperationType.UPDATE,
        update_mask=[EntityUpdateMaskAttribute.CONNECTIONS],
    )
    test_entity_operation_2 = EntityOperation(
        entity=self.test_entity,
        operation=EntityOperationType.UPDATE,
        update_mask=[EntityUpdateMaskAttribute.CONNECTIONS],
    )

    self.assertEqual(test_entity_operation_1, test_entity_operation_2)

  def testEntityOperationInequality(self):
    test_entity_operation_1 = EntityOperation(
        entity=self.test_entity,
        operation=EntityOperationType.UPDATE,
        update_mask=[EntityUpdateMaskAttribute.CONNECTIONS],
    )
    test_entity_operation_2 = EntityOperation(
        entity=self.test_entity,
        operation=EntityOperationType.ADD,
    )
    self.assertNotEqual(test_entity_operation_1, test_entity_operation_2)


if __name__ == "__main__":
  absltest.main()
