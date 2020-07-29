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

"""Tests for presubmit_validate_types_lib."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from absl import flags

from yamlformat.validator import base_lib
from yamlformat.validator import entity_type_lib
from yamlformat.validator import field_lib
from yamlformat.validator import findings_lib
from yamlformat.validator import namespace_validator
from yamlformat.validator import presubmit_validate_types_lib
from yamlformat.validator import state_lib
from yamlformat.validator import subfield_lib
from yamlformat.validator import test_helpers_lib
from yamlformat.validator import unit_lib
from absl.testing import absltest

FLAGS = flags.FLAGS

_F = test_helpers_lib.Fields
_F1 = test_helpers_lib.Field

# Constant to point to test files.
RESOURCE_PATH = 'fake_resources'
# Override this value to keep tests stable
namespace_validator.MIN_SIZE_FOR_LOCAL_FIELD_DUPES = 1


class PresubmitValidateTypesTest(absltest.TestCase):

  def setUp(self):
    super(PresubmitValidateTypesTest, self).setUp()
    self.base_dir = RESOURCE_PATH

    # Paths to testing files
    # subfield files
    self.global_subfields = base_lib.PathParts(
        root=self.base_dir, relative_path='subfields/global_subfields.yaml')
    self.good_local_subfields = base_lib.PathParts(
        root=self.base_dir, relative_path='GOOD/subfields/local_subfields.yaml')
    self.bad_local_subfields = base_lib.PathParts(
        root=self.base_dir,
        relative_path='BAD/subfields/bad_local_subfields.yaml')

    # field files
    self.global_fields = base_lib.PathParts(
        root=self.base_dir, relative_path='fields/global_fields.yaml')
    self.good_local_fields = base_lib.PathParts(
        root=self.base_dir, relative_path='GOOD/fields/local_fields.yaml')
    self.bad_local_fields = base_lib.PathParts(
        root=self.base_dir, relative_path='BAD/fields/bad_local_fields.yaml')

    # type files
    self.bad1_file = base_lib.PathParts(
        root=self.base_dir, relative_path='BAD/entity_types/bad1.yaml')
    self.bad2_file = base_lib.PathParts(
        root=self.base_dir, relative_path='BAD/entity_types/bad2.yaml')
    self.bad3_file = base_lib.PathParts(
        root=self.base_dir, relative_path='BAD/entity_types/bad3.yaml')
    self.bad4_file = base_lib.PathParts(
        root=self.base_dir, relative_path='BAD/entity_types/bad4.yaml')
    self.bad5_file = base_lib.PathParts(
        root=self.base_dir, relative_path='BAD/entity_types/bad5.yaml')

    self.good1_file = base_lib.PathParts(
        root=self.base_dir, relative_path='GOOD/entity_types/good1.yaml')
    self.good2_file = base_lib.PathParts(
        root=self.base_dir, relative_path='GOOD/entity_types/good2.yaml')

    self.good1_depot_path = os.path.join('//depot/google3', RESOURCE_PATH,
                                         'GOOD/entity_types/good1.yaml')

  def CreateConfig(self,
                   fields=tuple(),
                   subfields=tuple(),
                   states=tuple(),
                   type_defs=tuple(),
                   units=tuple()):
    # Config namedtuple
    return presubmit_validate_types_lib.Config(
        fields=fields,
        subfields=subfields,
        states=states,
        type_defs=type_defs,
        units=units)

  def ListHasType(self, findings_list, finding_type):
    for f in findings_list:
      if isinstance(f, finding_type):
        return True
    return False

  def testConfigUniverse(self):
    context = findings_lib.FileContext('')
    type_universe = entity_type_lib.EntityTypeUniverse([])
    type_universe.AddFinding(
        findings_lib.IllegalCharacterError('stuff', context))
    field_universe = field_lib.FieldUniverse([])
    field_universe.AddFinding(
        findings_lib.InconsistentFileLocationError('', context))
    subfield_universe = subfield_lib.SubfieldUniverse([])
    subfield_universe.AddFinding(
        findings_lib.CapitalizationError('Hi', context))
    state_universe = state_lib.StateUniverse([])
    unit_universe = unit_lib.UnitUniverse([])
    config_universe = presubmit_validate_types_lib.ConfigUniverse(
        subfield_universe=subfield_universe, field_universe=field_universe,
        entity_type_universe=type_universe, state_universe=state_universe,
        unit_universe=unit_universe)

    findings = config_universe.GetFindings()
    self.assertLen(findings, 3)
    self.assertTrue(
        config_universe.HasFindingTypes([
            findings_lib.InconsistentFileLocationError,
            findings_lib.IllegalCharacterError, findings_lib.CapitalizationError
        ]))
    self.assertFalse(config_universe.IsValid())

  def testConfigUniverseGetEntityTypeNamespace(self):
    context = findings_lib.FileContext('')
    type_universe = entity_type_lib.EntityTypeUniverse([])
    type_universe.AddFinding(
        findings_lib.IllegalCharacterError('stuff', context))
    field_universe = field_lib.FieldUniverse([])
    field_universe.AddFinding(
        findings_lib.InconsistentFileLocationError('', context))
    subfield_universe = subfield_lib.SubfieldUniverse([])
    subfield_universe.AddFinding(
        findings_lib.CapitalizationError('Hi', context))
    state_universe = state_lib.StateUniverse([])
    unit_universe = unit_lib.UnitUniverse([])
    config_universe = presubmit_validate_types_lib.ConfigUniverse(
        subfield_universe=subfield_universe, field_universe=field_universe,
        entity_type_universe=type_universe, state_universe=state_universe,
        unit_universe=unit_universe)

    entity_type_namespace = config_universe.GetEntityTypeNamespace('NONEXISTENT')

    self.assertIsNone(entity_type_namespace)

  def testConfigUniverseGetEntityType(self):
    context = findings_lib.FileContext('')
    type_universe = entity_type_lib.EntityTypeUniverse([])
    type_universe.AddFinding(
        findings_lib.IllegalCharacterError('stuff', context))
    field_universe = field_lib.FieldUniverse([])
    field_universe.AddFinding(
        findings_lib.InconsistentFileLocationError('', context))
    subfield_universe = subfield_lib.SubfieldUniverse([])
    subfield_universe.AddFinding(
        findings_lib.CapitalizationError('Hi', context))
    state_universe = state_lib.StateUniverse([])
    unit_universe = unit_lib.UnitUniverse([])
    config_universe = presubmit_validate_types_lib.ConfigUniverse(
        subfield_universe=subfield_universe, field_universe=field_universe,
        entity_type_universe=type_universe, state_universe=state_universe,
        unit_universe=unit_universe)

    entity_type = config_universe.GetEntityType('NONEXISTENT', 'NONEXISTENT')

    self.assertIsNone(entity_type)

  def testValidateUndefinedFields(self):
    # bad3_file declares an undefined field
    findings = presubmit_validate_types_lib.RunPresubmit(
        [], [], [self.bad3_file, self.global_fields])
    self.assertTrue(
        self.ListHasType(findings, findings_lib.UndefinedFieldError))

  def testBadFieldsFile(self):
    findings = presubmit_validate_types_lib.RunPresubmit(
        [], [], [self.bad3_file, self.global_fields, self.bad_local_fields])
    self.assertTrue(
        self.ListHasType(findings, findings_lib.DuplicateFieldDefinitionError))
    self.assertTrue(
        self.ListHasType(findings, findings_lib.UndefinedFieldError))

  def testBadSubfieldsFile(self):
    findings = presubmit_validate_types_lib.RunPresubmit([], [], [
        self.good2_file, self.global_fields, self.global_subfields,
        self.bad_local_subfields
    ])
    # Bad subfields should be ignored
    self.assertTrue(
        self.ListHasType(findings,
                         findings_lib.DuplicateSubfieldDefinitionError))
    # Rest of validation should proceed with no problems.
    # only one finding from duplicate subfield
    self.assertLen(findings, 1)

  def testFileBadPath(self):
    bad_path = base_lib.PathParts(self.base_dir, 'bad_type_file')
    with self.assertRaises(RuntimeError):
      presubmit_validate_types_lib.RunPresubmit([], [], [bad_path])

  def testSeparateConfigFiles(self):
    field1 = base_lib.PathParts(
        root='', relative_path='path/to/resources/fields/field1')
    field2 = base_lib.PathParts(
        root='', relative_path='path/to/resources/fields/field2')
    types1 = base_lib.PathParts(
        root='', relative_path='path/to/resources/TEST/entity_types/types1')
    types2 = base_lib.PathParts(
        root='', relative_path='path/to/resources/TEST/entity_types/types2')
    subfield1 = base_lib.PathParts(
        root='', relative_path='path/to/resources/subfields/subfield1')
    state1 = base_lib.PathParts(
        root='', relative_path='path/to/resources/states/state1')
    unit1 = base_lib.PathParts(
        root='', relative_path='path/to/resources/units/unit1')

    config_list = [field1, field2, types1, types2, subfield1, state1, unit1]
    config = presubmit_validate_types_lib.SeparateConfigFiles(config_list)

    self.assertIn(field1, config.fields)
    self.assertIn(field2, config.fields)
    self.assertIn(types1, config.type_defs)
    self.assertIn(types2, config.type_defs)
    self.assertIn(subfield1, config.subfields)
    self.assertIn(state1, config.states)
    self.assertIn(unit1, config.units)

  def testOrganizeFindingsByFile(self):
    finding1 = findings_lib.Finding('error1',
                                    findings_lib.FileContext(filepath='path1'))
    finding2 = findings_lib.Finding('error2',
                                    findings_lib.FileContext(filepath='path1'))
    finding3 = findings_lib.Finding('error3',
                                    findings_lib.FileContext(filepath='path2'))
    finding4 = findings_lib.Finding('error4',
                                    findings_lib.FileContext(filepath='path3'))

    findings_list = [finding1, finding2, finding3, finding4]
    findings_map = presubmit_validate_types_lib.OrganizeFindingsByFile(
        findings_list)

    self.assertLen(findings_map, 3)
    path1_list = findings_map.get('path1')
    path2_list = findings_map.get('path2')
    path3_list = findings_map.get('path3')

    self.assertLen(path1_list, 2)
    self.assertIn(finding1, path1_list)
    self.assertIn(finding2, path1_list)
    self.assertLen(path2_list, 1)
    self.assertIn(finding3, path2_list)
    self.assertLen(path3_list, 1)
    self.assertIn(finding4, path3_list)

  def testBackwardsCompatibilityRemovedNamespace(self):
    # Two namespaces. Both have an entitytype. One type is abstract.
    ns1_path = '{0}/entity_types/anyfolder'.format('namespace_one')
    folder1 = entity_type_lib.EntityTypeFolder(ns1_path)
    ns1 = folder1.local_namespace
    type1 = entity_type_lib.EntityType(
        filepath=ns1_path + '/file.yaml',
        typename='type1',
        inherited_fields_expanded=True)
    ns1.InsertType(type1)

    ns2_path = '{0}/entity_types/anyfolder'.format('namespace_two')
    folder2 = entity_type_lib.EntityTypeFolder(ns2_path)
    ns2 = folder2.local_namespace
    type2 = entity_type_lib.EntityType(
        filepath=ns2_path + '/file.yaml',
        typename='type2',
        inherited_fields_expanded=True,
        is_abstract=True)
    ns2.InsertType(type2)
    old_uv = entity_type_lib.EntityTypeUniverse([folder1, folder2])

    # no namespaces
    new_uv = entity_type_lib.EntityTypeUniverse([])

    findings = presubmit_validate_types_lib.CheckBackwardsCompatibility(
        new_uv, old_uv)

    self.assertLen(findings, 1)
    self.assertIsInstance(findings[0], findings_lib.RemovedNamespaceWarning)
    self.assertIn('namespace_one', str(findings[0]))

  def testBackwardsCompatibilityRemovedType(self):
    # Two types.  One is abstract.
    ns1_path = '{0}/entity_types/anyfolder'.format('namespace_one')
    folder1 = entity_type_lib.EntityTypeFolder(ns1_path)
    ns1 = folder1.local_namespace
    type1 = entity_type_lib.EntityType(
        filepath=ns1_path + '/file.yaml',
        typename='type1',
        inherited_fields_expanded=True)
    ns1.InsertType(type1)
    type2 = entity_type_lib.EntityType(
        filepath=ns1_path + '/file.yaml',
        typename='type2',
        inherited_fields_expanded=True,
        is_abstract=True)
    ns1.InsertType(type2)
    old_uv = entity_type_lib.EntityTypeUniverse([folder1])

    # No Types.
    folder1a = entity_type_lib.EntityTypeFolder(ns1_path)
    new_uv = entity_type_lib.EntityTypeUniverse([folder1a])

    findings = presubmit_validate_types_lib.CheckBackwardsCompatibility(
        new_uv, old_uv)

    self.assertLen(findings, 1)
    self.assertIsInstance(findings[0], findings_lib.RemovedTypeWarning)
    self.assertIn('type1', str(findings[0]))

  def testBackwardsCompatibilityRemovedTypeWithIds(self):
    # Two types.  One is abstract.
    ns1_path = '{0}/entity_types/anyfolder'.format('namespace_one')
    folder1 = entity_type_lib.EntityTypeFolder(ns1_path)
    ns1 = folder1.local_namespace
    type1 = entity_type_lib.EntityType(
        filepath=ns1_path + '/file.yaml',
        typename='type1',
        inherited_fields_expanded=True,
        uid='1')
    ns1.InsertType(type1)
    type2 = entity_type_lib.EntityType(
        filepath=ns1_path + '/file.yaml',
        typename='type2',
        inherited_fields_expanded=True,
        uid='2')
    ns1.InsertType(type2)
    old_uv = entity_type_lib.EntityTypeUniverse([folder1])

    folder1a = entity_type_lib.EntityTypeFolder(ns1_path)
    ns1a = folder1a.local_namespace
    type1a = entity_type_lib.EntityType(
        filepath=ns1_path + '/file.yaml',
        typename='type1a',
        inherited_fields_expanded=True,
        uid='1')
    ns1a.InsertType(type1a)
    type2a = entity_type_lib.EntityType(
        filepath=ns1_path + '/file.yaml',
        typename='type2',
        inherited_fields_expanded=True,
        uid='3')
    ns1a.InsertType(type2a)
    new_uv = entity_type_lib.EntityTypeUniverse([folder1a])

    findings = presubmit_validate_types_lib.CheckBackwardsCompatibility(
        new_uv, old_uv)

    self.assertLen(findings, 1)
    self.assertIsInstance(findings[0], findings_lib.RemovedTypeWarning)
    self.assertIn('type2', str(findings[0]))

  def testBackwardsCompatibilityAcrossNamespaces(self):
    # Two types.  One is abstract.
    ns1_path = '{0}/entity_types/anyfolder'.format('namespace_one')
    ns2_path = '{0}/entity_types/anyfolder'.format('namespace_two')
    folder1 = entity_type_lib.EntityTypeFolder(ns1_path)
    ns1 = folder1.local_namespace
    type1 = entity_type_lib.EntityType(
        filepath=ns1_path + '/file.yaml',
        typename='type1',
        inherited_fields_expanded=True,
        uid='1')
    ns1.InsertType(type1)
    old_uv = entity_type_lib.EntityTypeUniverse([folder1])

    folder1a = entity_type_lib.EntityTypeFolder(ns1_path)
    folder2 = entity_type_lib.EntityTypeFolder(ns2_path)
    ns2 = folder1a.local_namespace
    type1a = entity_type_lib.EntityType(
        filepath=ns2_path + '/file.yaml',
        typename='type1a',
        inherited_fields_expanded=True,
        uid='1')
    ns2.InsertType(type1a)
    new_uv = entity_type_lib.EntityTypeUniverse([folder1a, folder2])

    findings = presubmit_validate_types_lib.CheckBackwardsCompatibility(
        new_uv, old_uv)

    self.assertEmpty(findings)

  def testBackwardsCompatibilityOptionalAddedFieldsOk(self):
    # Two types.  One is abstract.
    ns1_path = '{0}/entity_types/anyfolder'.format('namespace_one')
    folder1 = entity_type_lib.EntityTypeFolder(ns1_path)
    ns1 = folder1.local_namespace
    type1 = entity_type_lib.EntityType(
        filepath=ns1_path + '/file.yaml',
        typename='type1',
        local_field_tuples=_F(['local1']),
        inherited_fields_expanded=True)
    ns1.InsertType(type1)
    type2 = entity_type_lib.EntityType(
        filepath=ns1_path + '/file.yaml',
        typename='type2',
        local_field_tuples=_F(['local1']),
        inherited_fields_expanded=True)
    ns1.InsertType(type2)
    old_uv = entity_type_lib.EntityTypeUniverse([folder1])

    # Same Types with added fields
    folder1a = entity_type_lib.EntityTypeFolder(ns1_path)
    ns1a = folder1a.local_namespace
    type1a = entity_type_lib.EntityType(
        filepath=ns1_path + '/file.yaml',
        typename='type1',
        local_field_tuples=[_F1('local1', False),
                            _F1('local2', False)],
        inherited_fields_expanded=True)
    ns1a.InsertType(type1a)
    type2a = entity_type_lib.EntityType(
        filepath=ns1_path + '/file.yaml',
        typename='type2',
        local_field_tuples=[_F1('local1', False),
                            _F1('local2', True)],
        inherited_fields_expanded=True)
    ns1a.InsertType(type2a)
    new_uv = entity_type_lib.EntityTypeUniverse([folder1a])

    findings = presubmit_validate_types_lib.CheckBackwardsCompatibility(
        new_uv, old_uv)

    self.assertLen(findings, 1)
    self.assertTrue(type1a.HasFindingTypes([findings_lib.AddedFieldWarning]))
    self.assertFalse(type2a.HasFindingTypes([findings_lib.AddedFieldWarning]))

  def testBackwardsCompatibilityAddedFields(self):
    # Two types.  One is abstract.
    ns1_path = '{0}/entity_types/anyfolder'.format('namespace_one')
    folder1 = entity_type_lib.EntityTypeFolder(ns1_path)
    ns1 = folder1.local_namespace
    type1 = entity_type_lib.EntityType(
        filepath=ns1_path + '/file.yaml',
        typename='type1',
        local_field_tuples=_F(['local1']),
        inherited_fields_expanded=True)
    type1.inherited_field_names = {'/inherited1': _F1('/inherited1', False)}
    ns1.InsertType(type1)
    type2 = entity_type_lib.EntityType(
        filepath=ns1_path + '/file.yaml',
        typename='type2',
        local_field_tuples=_F(['abstract1']),
        inherited_fields_expanded=True,
        is_abstract=True)
    type2.inherited_field_names = {'/abstract1a': _F1('/abstract1a', False)}
    ns1.InsertType(type2)
    old_uv = entity_type_lib.EntityTypeUniverse([folder1])

    # Same Types with added fields
    folder1a = entity_type_lib.EntityTypeFolder(ns1_path)
    ns1a = folder1a.local_namespace
    type1a = entity_type_lib.EntityType(
        filepath=ns1_path + '/file.yaml',
        typename='type1',
        local_field_tuples=_F(['local1', 'local2']),
        inherited_fields_expanded=True)
    type1a.inherited_field_names = {
        '/inherited1': _F1('/inherited1', False),
        '/inherited2': _F1('/inherited2', False)
    }
    ns1a.InsertType(type1a)
    type2a = entity_type_lib.EntityType(
        filepath=ns1_path + '/file.yaml',
        typename='type2',
        local_field_tuples=_F(['abstract1', 'abstract2']),
        inherited_fields_expanded=True,
        is_abstract=True)
    type2a.inherited_field_names = {
        '/abstract1a': _F1('/abstract1a', False),
        '/abstract2a': _F1('/abstract2a', False)
    }
    ns1a.InsertType(type2a)
    new_uv = entity_type_lib.EntityTypeUniverse([folder1a])

    findings = presubmit_validate_types_lib.CheckBackwardsCompatibility(
        new_uv, old_uv)

    self.assertLen(findings, 2)
    field1 = 'local2'
    field2 = 'inherited2'
    if field1 not in str(findings[0]):
      field1 = 'inherited2'
      field2 = 'local2'
    self.assertIsInstance(findings[0], findings_lib.AddedFieldWarning)
    self.assertIn(field1, str(findings[0]))
    self.assertIsInstance(findings[1], findings_lib.AddedFieldWarning)
    self.assertIn(field2, str(findings[1]))

  def testBackwardsCompatibilityRemovedFields(self):
    # Two types.  One is abstract.
    ns1_path = '{0}/entity_types/anyfolder'.format('namespace_one')
    folder1 = entity_type_lib.EntityTypeFolder(ns1_path)
    ns1 = folder1.local_namespace
    type1 = entity_type_lib.EntityType(
        filepath=ns1_path + '/file.yaml',
        typename='type1',
        local_field_tuples=_F(['local1', 'local2']),
        inherited_fields_expanded=True)
    type1.inherited_field_names = {
        '/inherited1': _F1('/inherited1', False),
        '/inherited2': _F1('/inherited2', False)
    }
    ns1.InsertType(type1)
    type2 = entity_type_lib.EntityType(
        filepath=ns1_path + '/file.yaml',
        typename='type2',
        local_field_tuples=_F(['abstract1', 'abstract2']),
        inherited_fields_expanded=True,
        is_abstract=True)
    type2.inherited_field_names = {
        '/abstract1a': _F1('/abstract1a', False),
        '/abstract2a': _F1('/abstract2a', False)
    }
    ns1.InsertType(type2)
    old_uv = entity_type_lib.EntityTypeUniverse([folder1])

    # Same Types with removed fields
    folder1a = entity_type_lib.EntityTypeFolder(ns1_path)
    ns1a = folder1a.local_namespace
    type1a = entity_type_lib.EntityType(
        filepath=ns1_path + '/file.yaml',
        typename='type1',
        local_field_tuples=_F(['local1']),
        inherited_fields_expanded=True)
    type1a.inherited_field_names = {'/inherited1': _F1('/inherited1', False)}
    ns1a.InsertType(type1a)
    type2a = entity_type_lib.EntityType(
        filepath=ns1_path + '/file.yaml',
        typename='type2',
        local_field_tuples=_F(['abstract1']),
        inherited_fields_expanded=True,
        is_abstract=True)
    type2a.inherited_field_names = {'/abstract1a': _F1('/abstract1a', False)}
    ns1a.InsertType(type2a)
    new_uv = entity_type_lib.EntityTypeUniverse([folder1a])

    findings = presubmit_validate_types_lib.CheckBackwardsCompatibility(
        new_uv, old_uv)
    self.assertLen(findings, 2)
    field1 = 'local2'
    field2 = 'inherited2'
    if field1 not in str(findings[0]):
      field1 = 'inherited2'
      field2 = 'local2'
    self.assertIsInstance(findings[0], findings_lib.RemovedFieldWarning)
    self.assertIn(field1, str(findings[0]))
    self.assertIsInstance(findings[1], findings_lib.RemovedFieldWarning)
    self.assertIn(field2, str(findings[1]))

if __name__ == '__main__':
  absltest.main()
