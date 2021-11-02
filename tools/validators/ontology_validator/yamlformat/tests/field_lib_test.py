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
"""Tests for field_lib."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl.testing import absltest

from yamlformat.validator import field_lib
from yamlformat.validator import findings_lib
from yamlformat.validator import subfield_lib

AGGREGATION = subfield_lib.SubfieldCategory.AGGREGATION
AGGREGATION_DESCRIPTOR = subfield_lib.SubfieldCategory.AGGREGATION_DESCRIPTOR
DESCRIPTOR = subfield_lib.SubfieldCategory.DESCRIPTOR
COMPONENT = subfield_lib.SubfieldCategory.COMPONENT
MEASUREMENT_DESCRIPTOR = subfield_lib.SubfieldCategory.MEASUREMENT_DESCRIPTOR
MEASUREMENT = subfield_lib.SubfieldCategory.MEASUREMENT
POINT_TYPE = subfield_lib.SubfieldCategory.POINT_TYPE

_GOOD_NAMESPACE = 'mynamespace'
_GOOD_PATH = '{0}/fields/anyfolder'.format(_GOOD_NAMESPACE)
_GOOD_GLOBAL_PATH = 'fields/anyfolder'


class FieldLibTest(absltest.TestCase):
  """Tests Functionality of classes for working with fields.

  Functionality for subfields doesn't yet exist, so tests mostly ignore them.
  """

  def testFieldsUniverseGetFindings(self):
    context = findings_lib.FileContext(_GOOD_PATH + '/file.yaml')
    folder = field_lib.FieldFolder(_GOOD_PATH)
    folder.AddFinding(findings_lib.InconsistentFileLocationError('', context))
    namespace = folder.local_namespace
    namespace.AddFinding(
        findings_lib.UnrecognizedSubfieldError(['any'],
                                          field_lib.Field(
                                              'two', file_context=context)))
    field = field_lib.Field('one', file_context=context)
    # Currently there are no warnings for fields, so using a subfield warning
    field.AddFinding(
        findings_lib.MissingSubfieldDescriptionWarning('one', context))
    namespace.InsertField(field)

    fields_universe = field_lib.FieldUniverse([folder])

    findings = fields_universe.GetFindings()
    self.assertLen(findings, 3)
    self.assertTrue(
        fields_universe.HasFindingTypes([
            findings_lib.InconsistentFileLocationError,
            findings_lib.UnrecognizedSubfieldError,
            findings_lib.MissingSubfieldDescriptionWarning
        ]))
    self.assertFalse(fields_universe.IsValid())

  def testFieldUniverse(self):
    # Create field folders
    folder = field_lib.FieldFolder(_GOOD_PATH)
    namespace = folder.local_namespace
    namespace.InsertField(field_lib.Field('meow'))
    namespace.InsertField(field_lib.Field('claws'))
    fields_universe = field_lib.FieldUniverse([folder])

    self.assertTrue(fields_universe.IsFieldDefined('meow', 'mynamespace'))
    self.assertTrue(fields_universe.IsFieldDefined('claws', 'mynamespace'))
    self.assertFalse(fields_universe.IsFieldDefined('clawsss', 'mynamespace'))

  def testFieldUniverseGetFieldMap(self):
    meow_cat = field_lib.Field('meow_cat')
    claws_cat = field_lib.Field('claws_cat')
    global_folder = field_lib.FieldFolder(_GOOD_GLOBAL_PATH)
    folder = field_lib.FieldFolder(_GOOD_PATH, global_folder.local_namespace)
    folder.local_namespace.PutIfAbsent(meow_cat)
    global_folder.local_namespace.PutIfAbsent(claws_cat)

    universe = field_lib.FieldUniverse([folder, global_folder])

    local_fields = universe.GetFieldsMap(_GOOD_NAMESPACE)
    global_fields = universe.GetFieldsMap('')
    all_fields = universe.GetFieldsMap()

    expected_local = {_GOOD_NAMESPACE + '/meow_cat': meow_cat}
    expected_global = {'/claws_cat': claws_cat}
    expected_all = {**expected_local, **expected_global}

    self.assertDictEqual(local_fields, expected_local)
    self.assertDictEqual(global_fields, expected_global)
    self.assertDictEqual(all_fields, expected_all)

  def testGetSubFieldList(self):
    field = field_lib.Field('test_name')
    expected = ['test', 'name']
    self.assertEqual(field.subfields, expected)

  def testAddFieldRejectsDuplicateSubfields(self):
    folder = field_lib.FieldFolder('/fields')
    field = 'field_name'
    field_dup = 'field_field_name'
    rel_filepath = '/fields/f.yaml'
    context = findings_lib.FileContext(rel_filepath)

    folder.AddField(field_lib.Field(field, file_context=context))
    self.assertEmpty(folder.GetFindings())
    folder.AddField(field_lib.Field(field_dup, file_context=context))
    self.assertLen(folder.GetFindings(), 1)
    self.assertIsInstance(folder.GetFindings()[0],
                          findings_lib.DuplicateSubfieldError)

  def testInsertFieldRejectsReversals(self):
    ns = field_lib.FieldNamespace('')
    field = field_lib.Field('field_name')
    field_rev = field_lib.Field('name_field')

    ns.InsertField(field)
    self.assertEmpty(ns.GetFindings())
    ns.InsertField(field_rev)
    self.assertIsInstance(ns.GetFindings()[0],
                          findings_lib.DuplicateFieldDefinitionError)

  def testInsertFieldInGlobalNamespaceNoSubfields(self):
    ns = field_lib.FieldNamespace('')
    field = field_lib.Field('field_name')

    ns.InsertField(field)
    self.assertEmpty(ns.GetFindings())
    self.assertEqual(ns.fields[frozenset({'field', 'name'})], field)

  def testInsertFieldInGlobalNamespaceMatchSubfields(self):
    sf_dict = {
        'field': subfield_lib.Subfield('field', DESCRIPTOR),
        'name': subfield_lib.Subfield('name', POINT_TYPE)
    }

    ns = field_lib.FieldNamespace('', subfields=sf_dict)

    field = field_lib.Field('field_name')

    ns.InsertField(field)
    self.assertEmpty(ns.GetFindings())
    self.assertEqual(ns.fields[frozenset({'field', 'name'})], field)

  def testInsertFieldInGlobalNamespaceMissingSubfields(self):
    sf_dict = {'field': subfield_lib.Subfield('field', POINT_TYPE)}
    ns = field_lib.FieldNamespace('', subfields=sf_dict)

    field = field_lib.Field('field_name')

    ns.InsertField(field)
    self.assertEqual(ns.fields, {})
    self.assertLen(ns.GetFindings(), 1)
    self.assertIsInstance(ns.GetFindings()[0],
                          findings_lib.UnrecognizedSubfieldError)

  def testInsertDuplicateFieldInGlobalNamespace(self):
    ns = field_lib.FieldNamespace('')

    field = field_lib.Field('field_name')
    field_clone = field_lib.Field('field_name')

    ns.InsertField(field)
    self.assertEmpty(ns.GetFindings())
    ns.InsertField(field_clone)
    self.assertEqual(ns.fields, {frozenset({'field', 'name'}): field})
    self.assertEqual(id(ns.fields[frozenset({'field', 'name'})]), id(field))
    self.assertLen(ns.GetFindings(), 1)
    self.assertIsInstance(ns.GetFindings()[0],
                          findings_lib.DuplicateFieldDefinitionError)

  def testInsertFieldInLocalNamespaceCanUpLevel(self):
    global_ns = field_lib.FieldNamespace('')
    ns = field_lib.FieldNamespace('local', parent_namespace=global_ns)
    field = field_lib.Field('field_name')

    ns.InsertField(field)
    self.assertEmpty(ns.GetFindings())
    self.assertEqual(global_ns.fields, {frozenset({'field', 'name'}): field})

  def testInsertFieldInLocalNamespace(self):
    sf_dict = {'field': subfield_lib.Subfield('field', DESCRIPTOR)}
    sf_glob_dict = {'name': subfield_lib.Subfield('name', POINT_TYPE)}
    global_ns = field_lib.FieldNamespace('', subfields=sf_glob_dict)
    ns = field_lib.FieldNamespace(
        'local', subfields=sf_dict, parent_namespace=global_ns)
    field = field_lib.Field('field_name')

    ns.InsertField(field)
    self.assertEmpty(ns.GetFindings())
    self.assertEqual(ns.fields, {frozenset({'field', 'name'}): field})

  def testInsertDuplicateFieldInLocalNamespace(self):
    sf_dict = {'field': subfield_lib.Subfield('field', DESCRIPTOR)}
    sf_glob_dict = {'name': subfield_lib.Subfield('name', POINT_TYPE)}
    global_ns = field_lib.FieldNamespace('', subfields=sf_glob_dict)
    ns = field_lib.FieldNamespace(
        'local', subfields=sf_dict, parent_namespace=global_ns)

    field = field_lib.Field('field_name')
    field_clone = field_lib.Field('field_name')

    ns.InsertField(field)
    self.assertEmpty(ns.GetFindings())
    ns.InsertField(field_clone)
    self.assertEqual(ns.fields, {frozenset({'field', 'name'}): field})
    self.assertEqual(id(ns.fields[frozenset({'field', 'name'})]), id(field))
    self.assertLen(ns.GetFindings(), 1)
    self.assertIsInstance(ns.GetFindings()[0],
                          findings_lib.DuplicateFieldDefinitionError)

  def testInsertFieldInLocalNamespaceMatchesGlobalSubs(self):
    sf_dict = {'field': subfield_lib.Subfield('field', DESCRIPTOR)}
    sf_glob_dict = {'name': subfield_lib.Subfield('name', POINT_TYPE)}
    global_ns = field_lib.FieldNamespace('', subfields=sf_glob_dict)
    ns = field_lib.FieldNamespace(
        'local', subfields=sf_dict, parent_namespace=global_ns)

    field = field_lib.Field('field_name')
    bad_field = field_lib.Field('field_name_unmatched')

    ns.InsertField(field)
    self.assertEmpty(ns.GetFindings())
    ns.InsertField(bad_field)
    self.assertEqual(ns.fields, {frozenset({'field', 'name'}): field})
    self.assertLen(ns.GetFindings(), 1)
    self.assertIsInstance(ns.GetFindings()[0],
                          findings_lib.UnrecognizedSubfieldError)

  def testInsertFieldValidatesCorrectConstruction(self):
    sf_dict = {
        'first': subfield_lib.Subfield('first', AGGREGATION_DESCRIPTOR),
        'second': subfield_lib.Subfield('second', AGGREGATION),
        'third': subfield_lib.Subfield('third', DESCRIPTOR),
        'fourth': subfield_lib.Subfield('fourth', COMPONENT),
        'fifth': subfield_lib.Subfield('fifth', MEASUREMENT_DESCRIPTOR),
        'sixth': subfield_lib.Subfield('sixth', MEASUREMENT),
        'seventh': subfield_lib.Subfield('seventh', POINT_TYPE)
    }
    ns = field_lib.FieldNamespace('local', subfields=sf_dict)
    field = field_lib.Field('first_second_third_fourth_fifth_sixth_seventh')

    ns.InsertField(field)
    self.assertEmpty(ns.GetFindings())

  def testInsertFieldValidatesMultipleDescriptors(self):
    sf_dict = {
        'first': subfield_lib.Subfield('first', DESCRIPTOR),
        'second': subfield_lib.Subfield('second', DESCRIPTOR),
        'third': subfield_lib.Subfield('third', POINT_TYPE)
    }
    ns = field_lib.FieldNamespace('local', subfields=sf_dict)
    field = field_lib.Field('first_second_third')

    ns.InsertField(field)
    self.assertEmpty(ns.GetFindings())

  def testAggregationDescriptorFailsWithoutAggregation(self):
    """Check that aggregation descriptors fail without associated
    aggregation. """

    sf_dict = {
        'first': subfield_lib.Subfield('first', AGGREGATION_DESCRIPTOR),
        'second': subfield_lib.Subfield('second', POINT_TYPE)
    }
    ns = field_lib.FieldNamespace('local', subfields=sf_dict)
    field = field_lib.Field('first_second')

    ns.InsertField(field)
    self.assertIsInstance(ns.GetFindings()[0],
                          findings_lib.InvalidFieldConstructionError)

  def testInsertRespectsAggregationDescriptorCount(self):
    sf_dict = {
        'first': subfield_lib.Subfield('first', AGGREGATION_DESCRIPTOR),
        'second': subfield_lib.Subfield('second', AGGREGATION_DESCRIPTOR),
        'third': subfield_lib.Subfield('third', AGGREGATION),
        'fourth': subfield_lib.Subfield('fourth', POINT_TYPE)
    }
    ns = field_lib.FieldNamespace('local', subfields=sf_dict)
    field = field_lib.Field('first_second_third_fourth')

    ns.InsertField(field)
    self.assertIsInstance(ns.GetFindings()[0],
                          findings_lib.InvalidFieldConstructionError)

  def testInsertFieldValidatesSubfieldsInMultipleNamespaces(self):
    sf_dict = {
        'first': subfield_lib.Subfield('first', DESCRIPTOR),
        'third': subfield_lib.Subfield('third', POINT_TYPE)
    }
    sf_glob_dict = {'second': subfield_lib.Subfield('second', DESCRIPTOR)}
    global_ns = field_lib.FieldNamespace('', subfields=sf_glob_dict)
    ns = field_lib.FieldNamespace(
        'local', subfields=sf_dict, parent_namespace=global_ns)
    field = field_lib.Field('first_second_third')

    ns.InsertField(field)
    self.assertEmpty(ns.GetFindings())

  def testInsertRespectsRequiredSubfields(self):
    sf_dict = {
        'first': subfield_lib.Subfield('first', DESCRIPTOR),
        'second': subfield_lib.Subfield('second', DESCRIPTOR),
    }
    ns = field_lib.FieldNamespace('local', subfields=sf_dict)
    field = field_lib.Field('first_second')

    ns.InsertField(field)
    self.assertIsInstance(ns.GetFindings()[0],
                          findings_lib.InvalidFieldConstructionError)

  def testInsertRespectsComponentCount(self):
    sf_dict = {
        'first': subfield_lib.Subfield('first', COMPONENT),
        'second': subfield_lib.Subfield('second', COMPONENT),
        'third': subfield_lib.Subfield('third', POINT_TYPE)
    }
    ns = field_lib.FieldNamespace('local', subfields=sf_dict)
    field = field_lib.Field('first_second_third')

    ns.InsertField(field)
    self.assertIsInstance(ns.GetFindings()[0],
                          findings_lib.InvalidFieldConstructionError)

  def testInsertRespectsMeasurementCount(self):
    sf_dict = {
        'first': subfield_lib.Subfield('first', MEASUREMENT),
        'second': subfield_lib.Subfield('second', MEASUREMENT),
        'third': subfield_lib.Subfield('third', POINT_TYPE)
    }
    ns = field_lib.FieldNamespace('local', subfields=sf_dict)
    field = field_lib.Field('first_second_third')

    ns.InsertField(field)
    self.assertIsInstance(ns.GetFindings()[0],
                          findings_lib.InvalidFieldConstructionError)

  def testInsertRespectsPointTypeCount(self):
    sf_dict = {
        'first': subfield_lib.Subfield('first', MEASUREMENT),
        'second': subfield_lib.Subfield('second', POINT_TYPE),
        'third': subfield_lib.Subfield('third', POINT_TYPE)
    }
    ns = field_lib.FieldNamespace('local', subfields=sf_dict)
    field = field_lib.Field('first_second_third')

    ns.InsertField(field)
    self.assertIsInstance(ns.GetFindings()[0],
                          findings_lib.InvalidFieldConstructionError)

  def testInsertRespectsMeasurementDescriptorCount(self):
    sf_dict = {
        'first': subfield_lib.Subfield('first', MEASUREMENT_DESCRIPTOR),
        'second': subfield_lib.Subfield('second', MEASUREMENT_DESCRIPTOR),
        'third': subfield_lib.Subfield('third', MEASUREMENT),
        'fourth': subfield_lib.Subfield('fourth', POINT_TYPE)
    }
    ns = field_lib.FieldNamespace('local', subfields=sf_dict)
    field = field_lib.Field('first_second_third_fourth')

    ns.InsertField(field)
    self.assertIsInstance(ns.GetFindings()[0],
                          findings_lib.InvalidFieldConstructionError)

  def testInsertRespectsDescriptorLimit(self):
    sf_dict = {
        'a': subfield_lib.Subfield('a', DESCRIPTOR),
        'b': subfield_lib.Subfield('b', DESCRIPTOR),
        'c': subfield_lib.Subfield('c', DESCRIPTOR),
        'd': subfield_lib.Subfield('d', DESCRIPTOR),
        'e': subfield_lib.Subfield('e', DESCRIPTOR),
        'f': subfield_lib.Subfield('f', DESCRIPTOR),
        'g': subfield_lib.Subfield('g', DESCRIPTOR),
        'h': subfield_lib.Subfield('h', DESCRIPTOR),
        'i': subfield_lib.Subfield('i', DESCRIPTOR),
        'j': subfield_lib.Subfield('j', DESCRIPTOR),
        'k': subfield_lib.Subfield('k', DESCRIPTOR),
        'l': subfield_lib.Subfield('l', POINT_TYPE)
    }
    ns = field_lib.FieldNamespace('local', subfields=sf_dict)
    field = field_lib.Field('a_b_c_d_e_f_g_h_i_j_k_l')

    ns.InsertField(field)
    self.assertIsInstance(ns.GetFindings()[0],
                          findings_lib.InvalidFieldConstructionError)

  def testInsertRejectsBadOrder(self):
    sf_dict = {
        'first': subfield_lib.Subfield('first', DESCRIPTOR),
        'second': subfield_lib.Subfield('second', COMPONENT),
        'third': subfield_lib.Subfield('third', POINT_TYPE)
    }
    ns = field_lib.FieldNamespace('local', subfields=sf_dict)
    field = field_lib.Field('second_first_third')

    ns.InsertField(field)
    self.assertIsInstance(ns.GetFindings()[0],
                          findings_lib.InvalidFieldConstructionError)

  def testInsertRejectsSetXWithNoMeasurement(self):
    sf_dict = {
        'first': subfield_lib.Subfield('first', COMPONENT),
        'sensor': subfield_lib.Subfield('sensor', POINT_TYPE),
        'setpoint': subfield_lib.Subfield('setpoint', POINT_TYPE),
        'accumulator': subfield_lib.Subfield('accumulator', POINT_TYPE)
    }
    ns = field_lib.FieldNamespace('local', subfields=sf_dict)
    field = field_lib.Field('first_sensor')
    field2 = field_lib.Field('first_setpoint')
    field3 = field_lib.Field('first_accumulator')

    ns.InsertField(field)
    self.assertIsInstance(ns.GetFindings()[0],
                          findings_lib.InvalidFieldConstructionError)
    ns.InsertField(field2)
    self.assertIsInstance(ns.GetFindings()[1],
                          findings_lib.InvalidFieldConstructionError)
    ns.InsertField(field3)
    self.assertIsInstance(ns.GetFindings()[1],
                          findings_lib.InvalidFieldConstructionError)

  def testAddFromConfig(self):
    yaml = {'literals': ['field_name']}
    folder = field_lib.FieldFolder('/fields')
    rel_filepath = '/fields/f.yaml'
    folder.AddFromConfig([yaml], rel_filepath)

    self.assertIn(frozenset({'field', 'name'}), folder.local_namespace.fields)
    created_field = folder.local_namespace.fields[frozenset({'field', 'name'})]
    self.assertEqual(created_field.file_context.filepath, rel_filepath)

  def testAddFromConfigNameRegex(self):
    yaml = {'literals': ['f_n', '2n', 'n2', 'n', 'nN', '_n', 'n_', 'n_1']}
    folder = field_lib.FieldFolder('/fields')
    rel_filepath = '/fields/f.yaml'
    folder.AddFromConfig([yaml], rel_filepath)

    self.assertSameElements(
        [frozenset({'f', 'n'}),
         frozenset({'n2'}),
         frozenset({'n'})], folder.local_namespace.fields)

  def testAddFromConfigBadYamlFilename(self):
    yaml = {'literals': ['field_name']}
    folder = field_lib.FieldFolder('/fields')
    rel_filepath = '/fields/f.yaml'
    bad_filepath = 'something/' + rel_filepath
    folder.AddFromConfig([yaml], bad_filepath)

    self.assertNotIn(
        frozenset({'field', 'name'}), folder.local_namespace.fields)
    self.assertIsInstance(folder.GetFindings()[0],
                          findings_lib.InconsistentFileLocationError)

  def testAddFromConfigWithStateList(self):
    yaml = {'literals': [{'field_name': ['A', 'B']}]}
    folder = field_lib.FieldFolder('/fields')
    rel_filepath = '/fields/f.yaml'
    folder.AddFromConfig([yaml], rel_filepath)

    self.assertEmpty(folder.GetFindings())
    self.assertCountEqual(['A', 'B'], folder.local_namespace.fields[frozenset(
        {'field', 'name'})].states)

  def testAddFromConfigWithStateListInvalidFieldFormat(self):
    yaml = {'literals': [{'field_name': ['A', 'B'], 'bad': ['WHOOPS']}]}
    folder = field_lib.FieldFolder('/fields')
    rel_filepath = '/fields/f.yaml'
    folder.AddFromConfig([yaml], rel_filepath)

    self.assertIsInstance(folder.GetFindings()[0],
                          findings_lib.InvalidFieldFormatError)

  def testAddFromConfigIllegalKeyType(self):
    yaml = {'literals': [False]}
    folder = field_lib.FieldFolder('/fields')
    rel_filepath = '/fields/f.yaml'
    folder.AddFromConfig([yaml], rel_filepath)

    self.assertNotIn(False, folder.local_namespace.fields)
    self.assertIsInstance(folder.GetFindings()[0],
                          findings_lib.IllegalKeyTypeError)

  def testAddFromConfigIllegalCharactersInName(self):
    yaml = {'literals': ['field_!ame']}
    folder = field_lib.FieldFolder('/fields')
    rel_filepath = '/fields/f.yaml'
    folder.AddFromConfig([yaml], rel_filepath)

    self.assertNotIn('field_!ame', folder.local_namespace.fields)
    self.assertIsInstance(folder.GetFindings()[0],
                          findings_lib.InvalidFieldNameError)

  def testAddFromBadConfigFormat(self):
    yaml = {'literaaaals': ['field_one']}
    yaml2 = {'literals': ['field_two']}
    folder = field_lib.FieldFolder('/fields')
    rel_filepath = '/fields/f.yaml'
    folder.AddFromConfig([yaml, yaml2], rel_filepath)

    self.assertNotIn(frozenset({'field', 'one'}), folder.local_namespace.fields)
    self.assertIn(frozenset({'field', 'two'}), folder.local_namespace.fields)
    self.assertIsInstance(folder.GetFindings()[0],
                          findings_lib.UnrecognizedKeyError)


if __name__ == '__main__':
  absltest.main()
