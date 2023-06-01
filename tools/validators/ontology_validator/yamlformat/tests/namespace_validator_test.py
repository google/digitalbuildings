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

"""Tests for namespace_validator."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl.testing import absltest
from yamlformat.validator import entity_type_lib
from yamlformat.validator import findings_lib
from yamlformat.validator import namespace_validator
from yamlformat.validator import test_helpers_lib

# pylint: disable=superfluous-parens
_F = test_helpers_lib.Fields
_F1 = test_helpers_lib.Field


class NamespaceValidatorTest(absltest.TestCase):

  def setUp(self):
    super(NamespaceValidatorTest, self).setUp()
    # Create a list of good TypeNamespace objects
    self.good_entity_type_1 = entity_type_lib.EntityType(
        filepath='path/to/ANIMAL/mammal',
        typename='animal',
        description='member of the animal kingdom',
        local_field_tuples=_F(['/animalia']),
    )

    self.good_entity_type_2 = entity_type_lib.EntityType(
        filepath='path/to/ANIMAL/mammal',
        typename='dog',
        description='canine animal',
        local_field_tuples=_F(['/woof', '/wag']),
        parents=['ANIMAL/animal'],
    )

    self.good_entity_type_3 = entity_type_lib.EntityType(
        filepath='path/to/ANIMAL/mammal',
        typename='puppy',
        description='baby dog',
        local_field_tuples=_F(['/cute']),
        parents=['ANIMAL/dog', 'ANIMAL/animal', 'ANIMAL/baby'],
    )

    self.good_entity_type_4 = entity_type_lib.EntityType(
        filepath='path/to/ANIMAL/mammal',
        typename='baby',
        description='young animal',
        local_field_tuples=_F(['/young']),
    )

    self.type_namespace = entity_type_lib.TypeNamespace(namespace='ANIMAL')
    self.type_namespace.InsertType(self.good_entity_type_1)
    self.type_namespace.InsertType(self.good_entity_type_2)
    self.type_namespace.InsertType(self.good_entity_type_3)
    self.type_namespace.InsertType(self.good_entity_type_4)

    self.validate_good = (
        namespace_validator.NamespaceValidator([self.type_namespace]))

  def testNamespaceValidator_goodEntityTypes_returnsEmptyListOfFindings(self):
    self.assertFalse(self.validate_good.GetFindings())

  def testNamespaceValidator_typesMapInheritedFieldsCorrectly_success(self):
    self.assertLen(self.validate_good.type_namespaces_map, 1)

    expanded_type_namespace = self.validate_good.type_namespaces_map.get(
        self.type_namespace.namespace)

    entity_type_1 = expanded_type_namespace.valid_types_map.get(
        self.good_entity_type_1.typename
    )
    entity_type_2 = expanded_type_namespace.valid_types_map.get(
        self.good_entity_type_2.typename
    )
    entity_type_3 = expanded_type_namespace.valid_types_map.get(
        self.good_entity_type_3.typename
    )
    entity_type_4 = expanded_type_namespace.valid_types_map.get(
        self.good_entity_type_4.typename
    )

    self.assertEmpty(entity_type_1.inherited_field_names)
    self.assertLen(entity_type_2.inherited_field_names, 1)
    self.assertLen(entity_type_3.inherited_field_names, 4)
    self.assertEmpty(entity_type_4.inherited_field_names)

  def testNamespaceValidator_typesMapLocalFieldsCorrectly_success(self):
    expanded_type_namespace = self.validate_good.type_namespaces_map.get(
        self.type_namespace.namespace)
    entity_type_1 = expanded_type_namespace.valid_types_map.get(
        self.good_entity_type_1.typename
    )
    entity_type_2 = expanded_type_namespace.valid_types_map.get(
        self.good_entity_type_2.typename
    )
    entity_type_3 = expanded_type_namespace.valid_types_map.get(
        self.good_entity_type_3.typename
    )
    entity_type_4 = expanded_type_namespace.valid_types_map.get(
        self.good_entity_type_4.typename
    )

    self.assertLen(entity_type_1.local_field_names, 1)
    self.assertLen(entity_type_2.local_field_names, 2)
    self.assertLen(entity_type_3.local_field_names, 1)
    self.assertLen(entity_type_4.local_field_names, 1)

  def testNamespaceValidator_typesMapIsExpandedForInheritedFields_success(self):
    type_namespace = self.validate_good.type_namespaces_map.get(
        self.type_namespace.namespace
    )

    entity_type_1 = type_namespace.valid_types_map.get(
        self.good_entity_type_1.typename
    )
    entity_type_2 = type_namespace.valid_types_map.get(
        self.good_entity_type_2.typename
    )
    entity_type_3 = type_namespace.valid_types_map.get(
        self.good_entity_type_3.typename
    )
    entity_type_4 = type_namespace.valid_types_map.get(
        self.good_entity_type_4.typename
    )

    self.assertTrue(entity_type_1.inherited_fields_expanded)
    self.assertTrue(entity_type_2.inherited_fields_expanded)
    self.assertTrue(entity_type_3.inherited_fields_expanded)
    self.assertTrue(entity_type_4.inherited_fields_expanded)

  def testNamespaceValidator_TypeHasNonexistentParent_AddsFindingToFindingsListSuccess(
      self,
  ):
    entity_type = entity_type_lib.EntityType(
        filepath='path/to/ANIMAL/mammal',
        typename='dog',
        description='canine animal',
        local_field_tuples=_F(['/woof']),
        parents=[('/nonexistent')])

    type_namespace = entity_type_lib.TypeNamespace(namespace='ANIMAL')
    type_namespace.InsertType(entity_type)
    namespace_validate = (
        namespace_validator.NamespaceValidator([type_namespace]))

    self.assertTrue(
        namespace_validate.HasFindingTypes(
            [findings_lib.NonexistentParentError]))

  def testNamespaceValidator_EntityTypeInheritsFromPassthroughType_errorAddsToFindings(
      self,
  ):
    passthrough_type = entity_type_lib.EntityType(
        filepath='path/to/ANIMAL/gateway',
        typename='dog',
        description='a gateway to dogs',
        allow_undefined_fields=True)
    entity_type = entity_type_lib.EntityType(
        filepath='path/to/ANIMAL/mammal',
        typename='dingo',
        description='canine animal',
        local_field_tuples=_F(['/woof']),
        parents=['ANIMAL/dog'])

    type_namespace = entity_type_lib.TypeNamespace(namespace='ANIMAL')
    type_namespace.InsertType(passthrough_type)
    type_namespace.InsertType(entity_type)
    namespace_validate = (
        namespace_validator.NamespaceValidator([type_namespace]))

    self.assertTrue(
        namespace_validate.HasFindingTypes(
            [findings_lib.PassthroughParentError]))

  def testNamespaceValidator_goodFieldIncrementWithDuplicateBase_success(self):
    entity_type = entity_type_lib.EntityType(
        filepath='path/to/ANIMAL/mammal',
        typename='dog',
        description='canine animal',
        local_field_tuples=_F(['/woof', '/woof_1']))

    type_namespace = entity_type_lib.TypeNamespace(namespace='ANIMAL')
    type_namespace.InsertType(entity_type)
    namespace_validate = (
        namespace_validator.NamespaceValidator([type_namespace]))

    self.assertTrue(namespace_validate.IsValid())

  def testNamespaceValidator_badFieldIncrementWithoutDuplicateBase_errorAddsToFindings(
      self,
  ):
    entity_type = entity_type_lib.EntityType(
        filepath='path/to/ANIMAL/mammal',
        typename='dog',
        description='canine animal',
        local_field_tuples=_F(['/woof_1']))

    type_namespace = entity_type_lib.TypeNamespace(namespace='ANIMAL')
    type_namespace.InsertType(entity_type)
    namespace_validate = (
        namespace_validator.NamespaceValidator([type_namespace]))

    self.assertTrue(
        namespace_validate.HasFindingTypes(
            [findings_lib.IllegalFieldIncrementError]))

  def testNamespaceValidator_validatesPassthroughType_success(self):
    passthrough_type = entity_type_lib.EntityType(
        filepath='path/to/ANIMAL/gateway',
        typename='dog',
        description='a gateway to dogs',
        allow_undefined_fields=True,
        local_field_tuples=_F(['/woof_1', '/woof_2', '/woof_3']),
    )

    type_namespace = entity_type_lib.TypeNamespace(namespace='ANIMAL')
    type_namespace.InsertType(passthrough_type)
    namespace_validate = namespace_validator.NamespaceValidator(
        [type_namespace]
    )

    self.assertTrue(namespace_validate.IsValid())

  def testNamespaceValidator_detectsInheritanceCycleInCommonNamespace_errorAddsToFindings(
      self,
  ):
    entity_type_1 = entity_type_lib.EntityType(
        filepath='path/to/ANIMAL/mammal',
        typename='dog',
        description='canine animal',
        local_field_tuples=_F(['/woof']),
        parents=['ANIMAL/wolf'],
    )

    entity_type_2 = entity_type_lib.EntityType(
        filepath='path/to/ANIMAL/mammal',
        typename='wolf',
        description='canine animal',
        local_field_tuples=_F(['/growl']),
        parents=['ANIMAL/dingo'],
    )

    entity_type_3 = entity_type_lib.EntityType(
        filepath='path/to/ANIMAL/mammal',
        typename='dingo',
        description='canine animal',
        local_field_tuples=_F(['/wag']),
        parents=['ANIMAL/dog'],
    )

    type_namespace = entity_type_lib.TypeNamespace(namespace='ANIMAL')
    type_namespace.InsertType(entity_type_1)
    type_namespace.InsertType(entity_type_2)
    type_namespace.InsertType(entity_type_3)
    namespace_validate = (
        namespace_validator.NamespaceValidator([type_namespace]))

    self.assertTrue(
        namespace_validate.HasFindingTypes([findings_lib.InheritanceCycleError
                                           ]))

  def testNamespaceValidator_detectsInheritanceCycleAcrossNamepsaces_errorAddsToFindings(
      self,
  ):
    type1 = entity_type_lib.EntityType(
        filepath='path/to/ANIMAL/mammal',
        typename='dog',
        description='canine animal',
        local_field_tuples=_F(['/woof']),
        parents=['ANIMAL/wolf'])

    type2 = entity_type_lib.EntityType(
        filepath='path/to/ANIMAL/mammal',
        typename='wolf',
        description='canine animal',
        local_field_tuples=_F(['/growl']),
        parents=['FUZZY_ANIMAL/dingo'])

    type3 = entity_type_lib.EntityType(
        filepath='path/to/FUZZY_ANIMAL/mammal',
        typename='dingo',
        description='canine animal',
        local_field_tuples=_F(['/wag']),
        parents=['ANIMAL/dog'])

    namespace = entity_type_lib.TypeNamespace(namespace='ANIMAL')
    namespace.InsertType(type1)
    namespace.InsertType(type2)
    namespace2 = entity_type_lib.TypeNamespace(namespace='FUZZY_ANIMAL')
    namespace2.InsertType(type3)
    namespace_validate = (
        namespace_validator.NamespaceValidator([namespace, namespace2]))

    self.assertTrue(
        namespace_validate.HasFindingTypes([findings_lib.InheritanceCycleError
                                           ]))

  def testNamespaceValidator_detectsDuplicateLocalFieldSets_warningAddsToFindings(
      self,
  ):
    type1 = entity_type_lib.EntityType(
        filepath='path/to/ANIMAL/mammal',
        typename='dog',
        description='canine animal',
        local_field_tuples=_F(['/woof', '/howl']))

    type2 = entity_type_lib.EntityType(
        filepath='path/to/ANIMAL/mammal',
        typename='wolf',
        description='canine animal',
        local_field_tuples=_F(['/woof', '/howl']))
    type2.inherited_field_names = ({'/bark': _F1('/bark', optional=True)})

    type_namespace = entity_type_lib.TypeNamespace(namespace='ANIMAL')
    type_namespace.InsertType(type1)
    type_namespace.InsertType(type2)

    namespace_validator.NamespaceValidator([type_namespace])

    self.assertTrue(
        type1.HasFindingTypes([findings_lib.DuplicateLocalFieldSetsWarning]))
    self.assertTrue(
        type2.HasFindingTypes([findings_lib.DuplicateLocalFieldSetsWarning]))

  def testNamespaceValidator_typesWithEmptyFields_success(self):
    type1 = entity_type_lib.EntityType(
        filepath='path/to/ANIMAL/mammal',
        typename='dog',
        description='canine animal')

    type2 = entity_type_lib.EntityType(
        filepath='path/to/ANIMAL/mammal',
        typename='wolf',
        description='canine animal')

    type_namespace = entity_type_lib.TypeNamespace(namespace='ANIMAL')
    type_namespace.InsertType(type1)
    type_namespace.InsertType(type2)

    namespace_validate = namespace_validator.NamespaceValidator(
        [type_namespace]
    )

    self.assertFalse(
        type1.HasFindingTypes([findings_lib.DuplicateLocalFieldSetsWarning]))
    self.assertFalse(
        type2.HasFindingTypes([findings_lib.DuplicateLocalFieldSetsWarning]))
    self.assertTrue(namespace_validate.IsValid())

  def testNamespaceValidator_InheritTypesFromDifferentNamespace_success(self):
    entity_type_1 = entity_type_lib.EntityType(
        filepath='path/to/ANIMAL/mammal',
        typename='dog',
        description='canine animal',
        local_field_tuples=_F(['/woof', '/howl']),
    )
    entity_type_2 = entity_type_lib.EntityType(
        filepath='path/to/INSECT/fly',
        typename='moth',
        description='flying insect.',
        local_field_tuples=_F(['/wings']),
        parents=['ANIMAL/dog'],
    )

    type_namespace_1 = entity_type_lib.TypeNamespace(namespace='ANIMAL')
    type_namespace_1.InsertType(entity_type_1)
    type_namespace_2 = entity_type_lib.TypeNamespace(namespace='INSECT')
    type_namespace_2.InsertType(entity_type_2)
    namespace_validate = (
        namespace_validator.NamespaceValidator(
            [type_namespace_1, type_namespace_2]))

    expanded_type_namespace_1 = namespace_validate.type_namespaces_map.get(
        type_namespace_1.namespace)
    expanded_type_namespace_2 = namespace_validate.type_namespaces_map.get(
        type_namespace_2.namespace)
    entity_type_1_expanded = expanded_type_namespace_1.valid_types_map.get(
        entity_type_1.typename
    )
    entity_type_2_expanded = expanded_type_namespace_2.valid_types_map.get(
        entity_type_2.typename
    )
    self.assertFalse(namespace_validate.GetFindings())
    self.assertTrue(namespace_validate.IsValid())
    self.assertEmpty(entity_type_1_expanded.inherited_field_names)
    self.assertLen(entity_type_2_expanded.inherited_field_names, 2)

  def testNamespaceValidator_inheritTypesFromNonExistentNamespace_errorAddsToFindings(
      self,
  ):
    entity_type_1 = entity_type_lib.EntityType(
        filepath='path/to/ANIMAL/mammal',
        typename='dog',
        description='canine animal',
        local_field_tuples=_F(['/woof', '/howl']),
    )
    entity_type_2 = entity_type_lib.EntityType(
        filepath='path/to/INSECT/fly',
        typename='moth',
        description='flying insect.',
        local_field_tuples=_F(['/wings']),
        parents=['ANIMALLLLL/dog'],
    )

    type_namespace_1 = entity_type_lib.TypeNamespace(namespace='ANIMAL')
    type_namespace_1.InsertType(entity_type_1)
    type_namespace_2 = entity_type_lib.TypeNamespace(namespace='INSECT')
    type_namespace_2.InsertType(entity_type_2)
    namespace_validate = (
        namespace_validator.NamespaceValidator(
            [type_namespace_1, type_namespace_2]))

    self.assertTrue(
        namespace_validate.HasFindingTypes(
            [findings_lib.NonexistentParentError]))
    self.assertFalse(namespace_validate.IsValid())

  def testNamespaceValidator_inheritsOptionality_setOptionalityOnInheritedFields(
      self,
  ):
    entity_type_1 = entity_type_lib.EntityType(
        filepath='path/to/ANIMAL/mammal',
        typename='dog',
        description='canine animal',
        local_field_tuples=[
            _F1('/woof', optional=True),
            _F1('/growl', optional=True)
        ],
        parents=[])
    entity_type_2 = entity_type_lib.EntityType(
        filepath='path/to/ANIMAL/mammal',
        typename='wolf',
        description='canine animal',
        local_field_tuples=[_F1('/woof', optional=True),
                            _F1('/growl', optional=False)],
        parents=[])
    entity_type_3 = entity_type_lib.EntityType(
        filepath='path/to/ANIMAL/mammal',
        typename='dingo',
        description='canine animal',
        local_field_tuples=[_F1('/wag', optional=False)],
        parents=['ANIMAL/dog', 'ANIMAL/wolf'])

    type_namespace_1 = entity_type_lib.TypeNamespace(namespace='ANIMAL')
    type_namespace_1.InsertType(entity_type_1)
    type_namespace_1.InsertType(entity_type_2)
    type_namespace_1.InsertType(entity_type_3)
    namespace_validate = (
        namespace_validator.NamespaceValidator([type_namespace_1]))

    self.assertTrue(namespace_validate.IsValid())
    field_map = entity_type_3.GetAllFields()
    self.assertFalse(field_map['/growl'].optional)
    self.assertTrue(field_map['/woof'].optional)
    self.assertFalse(field_map['/wag'].optional)


if __name__ == '__main__':
  absltest.main()
