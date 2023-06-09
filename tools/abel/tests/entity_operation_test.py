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
"""Tests from ABEL model entity operation class."""

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

  def test_entity_operation_init_add(self):
    test_entity_operation = EntityOperation(
        entity=self.test_entity, operation_type=EntityOperationType.ADD
    )
    self.assertIsInstance(test_entity_operation, EntityOperation)
    self.assertEqual(test_entity_operation.entity, self.test_entity)
    self.assertEqual(
        test_entity_operation.operation_type,
        EntityOperationType.ADD
    )
    self.assertIsNone(test_entity_operation.update_mask)

  def test_entity_operation_init_update(self):
    test_entity_operation = EntityOperation(
        entity=self.test_entity,
        operation_type=EntityOperationType.UPDATE,
        update_mask=[EntityUpdateMaskAttribute.CONNECTIONS],
    )
    self.assertIsInstance(test_entity_operation, EntityOperation)
    self.assertEqual(test_entity_operation.entity, self.test_entity)
    self.assertEqual(
        test_entity_operation.operation_type, EntityOperationType.UPDATE
    )
    self.assertSequenceEqual(
        test_entity_operation.update_mask,
        [EntityUpdateMaskAttribute.CONNECTIONS],
    )

  def test_entity_operation_init_update_fails(self):
    with self.assertRaises(AssertionError):
      EntityOperation(
          entity=self.test_entity, operation_type=EntityOperationType.UPDATE
      )


if __name__ == "__main__":
  absltest.main()
