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

"""Tests corp.bizapps.rews.carson.ontology.validation.entity_type_manager."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from absl.testing import absltest

from yamlformat.validator import entity_type_lib
from yamlformat.validator import entity_type_manager
from yamlformat.validator import field_lib
from yamlformat.validator import findings_lib
from yamlformat.validator import namespace_validator
from yamlformat.validator.entity_type_lib import FieldParts

# Overwrite thresholds for grouping to ensure stability
entity_type_manager.MIN_SET_SIZE = 1


def _GetFieldFolder(yaml, namespace=''):
  folderpath = os.path.join(namespace, 'fields')
  field_folder = field_lib.FieldFolder(folderpath)
  good_filepath = os.path.join(folderpath, 'f.yaml')
  field_folder.AddFromConfig([yaml], good_filepath)
  return field_folder


def _GetEntityTypeFolder(field_universe, yaml, namespace=''):
  folderpath = os.path.join(namespace, 'entity_types')
  type_folder = entity_type_lib.EntityTypeFolder(folderpath, field_universe)
  good_filepath = os.path.join(folderpath, 'f.yaml')
  type_folder.AddFromConfig([yaml], good_filepath)
  return type_folder


def _GetEntityTypeUniverse(type_folders):
  namespace_validator.NamespaceValidator(
      [type_folder.local_namespace for type_folder in type_folders])
  return entity_type_lib.EntityTypeUniverse(type_folders)


class EntityTypeManagerTest(absltest.TestCase):

  def testAnalyzeFindsFlexibleParents(self):
    yaml = {'literals': ['field1', 'field2', 'field3', 'field4']}
    field_universe = field_lib.FieldUniverse(
        [_GetFieldFolder(yaml)])
    yaml = {
        'VAV_parent': {
            'description': 'parent',
            'is_canonical': True,
            'uses': ['field1', 'field4'],
            'opt_uses': ['field2', 'field3']
        },
        'VAV_child1': {
            'description': 'child1',
            'uses': ['field1', 'field4'],
            'opt_uses': ['field2']
        },
        'VAV_child2': {
            'description': 'child2',
            'uses': ['field1', 'field3', 'field4']
        },
        'different_equip_type': {
            'description': 'different',
            'uses': ['field1', 'field3', 'field4']
        },
        'VAV_nomatch': {
            'description': 'nomatch',
            'uses': ['field1', 'field2', 'field3']
        },
    }
    type_folder = _GetEntityTypeFolder(field_universe, yaml)
    universe = _GetEntityTypeUniverse([type_folder])
    manager = entity_type_manager.EntityTypeManager(universe)

    manager.Analyze()

    child1 = universe.GetEntityType('', 'VAV_child1')
    child2 = universe.GetEntityType('', 'VAV_child2')
    child2_nm = universe.GetEntityType('', 'different_equip_type')
    parent = universe.GetEntityType('', 'VAV_parent')
    nomatch = universe.GetEntityType('', 'VAV_nomatch')

    self.assertTrue(parent.HasFindingTypes(
        [findings_lib.OverlappingFlexTypeParentWarning]))
    self.assertFalse(parent.HasFindingTypes(
        [findings_lib.OverlappingFlexTypeChildWarning]))

    self.assertTrue(child1.HasFindingTypes(
        [findings_lib.OverlappingFlexTypeChildWarning]))
    self.assertFalse(child1.HasFindingTypes(
        [findings_lib.OverlappingFlexTypeParentWarning]))

    self.assertTrue(child2.HasFindingTypes(
        [findings_lib.OverlappingFlexTypeChildWarning]))
    self.assertFalse(child2.HasFindingTypes(
        [findings_lib.OverlappingFlexTypeParentWarning]))

    self.assertFalse(child2_nm.HasFindingTypes(
        [findings_lib.OverlappingFlexTypeChildWarning,
         findings_lib.OverlappingFlexTypeParentWarning]))
    self.assertFalse(nomatch.HasFindingTypes(
        [findings_lib.OverlappingFlexTypeChildWarning,
         findings_lib.OverlappingFlexTypeParentWarning]))

  def testAnalyzeIgnoresNonCanonicalFlexibleParents(self):
    yaml = {'literals': ['field1', 'field2', 'field3', 'field4']}
    field_universe = field_lib.FieldUniverse(
        [_GetFieldFolder(yaml)])
    yaml = {
        'VAV_parent': {
            'description': 'parent',
            'uses': ['field1', 'field4'],
            'opt_uses': ['field2', 'field3']
        },
        'VAV_child1': {
            'description': 'child1',
            'uses': ['field1', 'field4'],
            'opt_uses': ['field2']
        },
    }
    type_folder = _GetEntityTypeFolder(field_universe, yaml)
    universe = _GetEntityTypeUniverse([type_folder])
    manager = entity_type_manager.EntityTypeManager(universe)

    manager.Analyze()

    parent = universe.GetEntityType('', 'VAV_parent')

    self.assertFalse(parent.HasFindingTypes(
        [findings_lib.OverlappingFlexTypeChildWarning,
         findings_lib.OverlappingFlexTypeParentWarning]))

  def testAnalyzeFindsDuplicates(self):
    yaml = {'literals': ['field1', 'field2', 'field3', 'field4', 'field5']}
    field_universe = field_lib.FieldUniverse(
        [_GetFieldFolder(yaml)])
    yaml = {
        'parent': {
            'description': 'parent',
            'uses': ['field1', 'field2', 'field3']
        },
        'child1': {
            'description': 'child1',
            'implements': ['parent'],
            'uses': ['field4']
        },
        'child2': {
            'description': 'child2',
            'uses': ['field1', 'field2', 'field3', 'field4']
        },
    }
    type_folder = _GetEntityTypeFolder(field_universe, yaml)
    universe = _GetEntityTypeUniverse([type_folder])
    manager = entity_type_manager.EntityTypeManager(universe)

    manager.Analyze()

    child1 = universe.GetEntityType('', 'child1')
    child2 = universe.GetEntityType('', 'child2')
    parent = universe.GetEntityType('', 'parent')

    self.assertTrue(child2.HasFindingTypes(
        [findings_lib.DuplicateExpandedFieldSetsWarning]))
    self.assertTrue(child1.HasFindingTypes(
        [findings_lib.DuplicateExpandedFieldSetsWarning]))
    self.assertFalse(parent.HasFindingTypes(
        [findings_lib.DuplicateExpandedFieldSetsWarning]))

  def testAnalyzeIgnoresPassthroughTypes(self):
    yaml = {'literals': ['field1', 'field2', 'field3', 'field4']}
    field_universe = field_lib.FieldUniverse(
        [_GetFieldFolder(yaml)])
    yaml = {
        'parent': {
            'description': 'parent',
            'uses': ['field1', 'field2', 'field3']
        },
        'PASSTHROUGH': {
            'description': 'PASSTHROUGH',
            'allow_undefined_fields': True,
            'uses': ['field1', 'field2', 'field3', 'field4']
        },
    }
    type_folder = _GetEntityTypeFolder(
        field_universe, yaml)
    universe = _GetEntityTypeUniverse([type_folder])
    manager = entity_type_manager.EntityTypeManager(universe)

    findings = manager.Analyze()

    self.assertEmpty(findings)

  def testAnalyzeHandlesNamespaces(self):
    yaml1 = {'literals': ['field1']}
    yaml2 = {'literals': ['field1', 'field2', 'field3', 'field4', 'field5']}
    field_folder1 = _GetFieldFolder(yaml1, 'HVAC')
    field_folder2 = _GetFieldFolder(yaml2)

    field_universe = field_lib.FieldUniverse([field_folder1, field_folder2])
    yaml1 = {
        'parent': {
            'description': 'parent',
            'uses': ['HVAC/field1', 'field2', 'field3']
        },
    }
    yaml2 = {
        'child1': {
            'description': 'child1',
            'uses': ['field1', 'field2', 'field3']
        },
    }
    type_folder1 = _GetEntityTypeFolder(
        field_universe, yaml1, 'other_namespace')
    type_folder2 = _GetEntityTypeFolder(
        field_universe, yaml2, 'HVAC')
    universe = _GetEntityTypeUniverse(
        [type_folder1, type_folder2])
    manager = entity_type_manager.EntityTypeManager(universe)

    findings = manager.Analyze()

    child1 = universe.GetEntityType('HVAC', 'child1')
    parent = universe.GetEntityType('other_namespace', 'parent')

    self.assertLen(findings, 2)
    self.assertLen(child1.GetFindings(), 1)
    self.assertTrue(child1.HasFindingTypes(
        [findings_lib.DuplicateExpandedFieldSetsWarning]))
    self.assertLen(parent.GetFindings(), 1)
    self.assertTrue(parent.HasFindingTypes(
        [findings_lib.DuplicateExpandedFieldSetsWarning]))

  def testGetCompleteFieldSetsOI(self):
    # build test universe
    yaml = {'literals': ['field1', 'field2', 'field3', 'field4']}
    field_universe = field_lib.FieldUniverse(
        [_GetFieldFolder(yaml)])
    yaml = {
        'parent': {
            'description': 'parent',
            'uses': ['field1', 'field2', 'field3']
        },
        'child1': {
            'description': 'child1',
            'implements': ['parent'],
            'uses': ['field4']
        },
        'child2': {
            'description': 'child2',
            'uses': ['field1', 'field2', 'field3', 'field4']
        },
    }
    type_folder = _GetEntityTypeFolder(field_universe, yaml)
    universe = _GetEntityTypeUniverse([type_folder])
    manager = entity_type_manager.EntityTypeManager(universe)
    # expected output for GetCompleteFieldSetsOI() once Analyze() is called
    expected_output = {
        frozenset({
            FieldParts(namespace='', field='field1', increment=''),
            FieldParts(namespace='', field='field2', increment=''),
            FieldParts(namespace='', field='field3', increment='')
        }): {'/parent'},
        frozenset({
            FieldParts(namespace='', field='field1', increment=''),
            FieldParts(namespace='', field='field2', increment=''),
            FieldParts(namespace='', field='field4', increment=''),
            FieldParts(namespace='', field='field3', increment='')
        }): {'/child1', '/child2'}
    }

    # test field sets have not been instantiated
    self.assertRaises(Exception, manager.GetCompleteFieldSetsOI)

    # instantiate and build field sets
    manager.Analyze()
    function_output = manager.GetCompleteFieldSetsOI()

    self.assertEqual(expected_output, function_output)

  def testGetTypenamesBySubsetOI(self):
    # build test universe
    yaml = {'literals': ['field1', 'field2', 'field3', 'field4']}
    field_universe = field_lib.FieldUniverse(
        [_GetFieldFolder(yaml)])
    yaml = {
        'VAV_child1': {
            'description': 'child1',
            'uses': ['field1', 'field4'],
            'opt_uses': ['field2']
        },
        'VAV_child2': {
            'description': 'child2',
            'uses': ['field1', 'field3', 'field4']
        },
    }
    type_folder = _GetEntityTypeFolder(field_universe, yaml)
    universe = _GetEntityTypeUniverse([type_folder])
    manager = entity_type_manager.EntityTypeManager(universe)
    # expected output for GetTypenamesBySubsetOI() once Analyze() is called
    expected_output = {
        frozenset({
            FieldParts(namespace='', field='field4', increment=''),
            FieldParts(namespace='', field='field1', increment='')
        }): {'/VAV_child2', '/VAV_child1'}
    }

    # test field sets have not been instantiated
    self.assertRaises(Exception, manager.GetTypenamesBySubsetOI)

    # instantiate and build field sets
    manager.Analyze()
    function_output = manager.GetTypenamesBySubsetOI()

    self.assertEqual(expected_output, function_output)

if __name__ == '__main__':
  absltest.main()
