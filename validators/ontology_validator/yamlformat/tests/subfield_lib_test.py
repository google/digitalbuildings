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
"""Tests google3.corp.bizapps.rews.carson.ontology.validation.subfield_lib."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from yamlformat.validator import findings_lib
from yamlformat.validator import subfield_lib
from absl.testing import absltest

_GOOD_PATH = '{0}/subfields/anyfolder'.format('mynamespace')
_BAD_SUBFOLDER = '{0}/subfield/anyfolder'.format('mynamespace')


class SubfieldLibTest(absltest.TestCase):

  def testSubfieldUniverseGetFindings(self):
    context = findings_lib.FileContext(_GOOD_PATH + '/file.yaml')
    folder = subfield_lib.SubfieldFolder(_GOOD_PATH)
    folder.AddFinding(findings_lib.InconsistentFileLocationError('', context))
    namespace = folder.local_namespace
    namespace.AddFinding(
        findings_lib.DuplicateSubfieldDefinitionError(
            subfield_lib.Subfield(
                'two', subfield_lib.SubfieldCategory.POINT_TYPE), 'any'))
    subfield = subfield_lib.Subfield(
        'one', subfield_lib.SubfieldCategory.POINT_TYPE, 'thing')
    subfield.AddFinding(
        findings_lib.MissingSubfieldDescriptionWarning('one', context))
    namespace.InsertSubfield(subfield)

    subfields_universe = subfield_lib.SubfieldUniverse([folder])

    findings = subfields_universe.GetFindings()
    self.assertLen(findings, 3)
    self.assertTrue(
        subfields_universe.HasFindingTypes([
            findings_lib.InconsistentFileLocationError,
            findings_lib.DuplicateSubfieldDefinitionError,
            findings_lib.MissingSubfieldDescriptionWarning
        ]))
    self.assertFalse(subfields_universe.IsValid())

  def testSubfieldUniverseGetSubfieldsMap(self):
    # Create field folders
    folder = subfield_lib.SubfieldFolder(_GOOD_PATH)
    namespace = folder.local_namespace
    namespace.InsertSubfield(subfield_lib.Subfield(
        'one', subfield_lib.SubfieldCategory.POINT_TYPE))
    namespace.InsertSubfield(subfield_lib.Subfield(
        'two', subfield_lib.SubfieldCategory.POINT_TYPE))
    subfields_universe = subfield_lib.SubfieldUniverse([folder])

    subfields_map = subfields_universe.GetSubfieldsMap('mynamespace')

    self.assertIn('one', subfields_map)
    self.assertIn('two', subfields_map)

  # TODO(nkilmer): See the TODO in config_folder_lib_test.py. These sorts of
  # tests should be on the base class, ConfigFolder. Applies to next 3 tests.
  def testCreateSubfieldFolderWithCorrectPath(self):
    sff = subfield_lib.SubfieldFolder(_GOOD_PATH)
    self.assertEqual('mynamespace', sff.local_namespace.namespace)

  def testCreateSubfieldFolderWithBadSubfolder(self):
    with self.assertRaises(RuntimeError):
      subfield_lib.SubfieldFolder(_BAD_SUBFOLDER)

  def testAddValidSubfield(self):
    sff = subfield_lib.SubfieldFolder(_GOOD_PATH)
    ctx = findings_lib.FileContext('{0}/file.yaml'.format(_GOOD_PATH))
    sff.AddSubfield(
        subfield_lib.Subfield('good', subfield_lib.SubfieldCategory.DESCRIPTOR,
                              'hi', ctx))
    self.assertIn('good', sff.local_namespace.subfields)

  def testAddInvalidSubfieldFails(self):
    sff = subfield_lib.SubfieldFolder(_GOOD_PATH)
    ctx = findings_lib.FileContext('{0}/file.yaml'.format(_GOOD_PATH))
    sff.AddSubfield(
        subfield_lib.Subfield('1-bad', subfield_lib.SubfieldCategory.DESCRIPTOR,
                              'hi', ctx))
    self.assertIsInstance(sff.GetFindings()[0],
                          findings_lib.IllegalCharacterError)

  def testAddDuplicateSubfieldFails(self):
    sff = subfield_lib.SubfieldFolder(_GOOD_PATH)
    ctx = findings_lib.FileContext('{0}/file.yaml'.format(_GOOD_PATH))
    sf = subfield_lib.Subfield('good', subfield_lib.SubfieldCategory.DESCRIPTOR,
                               'hi', ctx)
    sf2 = subfield_lib.Subfield(
        'good', subfield_lib.SubfieldCategory.POINT_TYPE, 'hi2', ctx)
    sff.AddSubfield(sf)
    self.assertEmpty(sff.local_namespace.GetFindings())
    sff.AddSubfield(sf2)
    self.assertIsInstance(sff.local_namespace.GetFindings()[0],
                          findings_lib.DuplicateSubfieldDefinitionError)

  def testAddSubfieldWithUpperFails(self):
    sff = subfield_lib.SubfieldFolder(_GOOD_PATH)
    ctx = findings_lib.FileContext('{0}/file.yaml'.format(_GOOD_PATH))
    sf = subfield_lib.Subfield('gOod', subfield_lib.SubfieldCategory.DESCRIPTOR,
                               'hi', ctx)
    sff.AddSubfield(sf)
    self.assertIsInstance(sff.GetFindings()[0],
                          findings_lib.IllegalCharacterError)

  def testAddFromConfig(self):
    doc = {
        'aggregation': {
            'agg': 'aggD'
        },
        'component': {
            'comp': 'compD'
        },
        'descriptor': {
            'desc': 'descD'
        },
        'measurement_descriptor': {
            'mdesc': 'mdescD'
        },
        'measurement': {
            'meas': 'measD'
        },
        'point_type': {
            'ptype': 'ptypeD'
        }
    }

    sff = subfield_lib.SubfieldFolder(_GOOD_PATH)
    sff.AddFromConfig([doc], '{0}/file.yaml'.format(_GOOD_PATH))
    ns = sff.local_namespace

    self.assertCountEqual(['agg', 'comp', 'desc', 'mdesc', 'meas', 'ptype'],
                          ns.subfields)
    self.assertEmpty(sff.GetFindings())

  def testAddFromConfigNotYaml(self):
    doc = {
        'aggregation': {
            'agg': 'aggD'
        },
    }

    sff = subfield_lib.SubfieldFolder(_GOOD_PATH)
    sff.AddFromConfig([doc], '{0}/file.yaaaml'.format(_GOOD_PATH))

    self.assertIsInstance(sff.GetFindings()[0],
                          findings_lib.InconsistentFileLocationError)

  def testAddFromConfigEmptyBlock(self):
    doc = {'aggregation': {}}

    sff = subfield_lib.SubfieldFolder(_GOOD_PATH)
    sff.AddFromConfig([doc], '{0}/file.yaml'.format(_GOOD_PATH))

    self.assertIsInstance(sff.GetFindings()[0], findings_lib.EmptyBlockWarning)

  def testCreateSubfieldNoDescription(self):
    ctx = findings_lib.FileContext('{0}/file.yaml'.format(_GOOD_PATH))
    sf = subfield_lib.Subfield('good', subfield_lib.SubfieldCategory.DESCRIPTOR,
                               '', ctx)
    self.assertIsInstance(sf.GetFindings()[0],
                          findings_lib.MissingSubfieldDescriptionWarning)

  def testCreateSubfieldIllegalKeyType(self):
    ctx = findings_lib.FileContext('{0}/file.yaml'.format(_GOOD_PATH))
    sf = subfield_lib.Subfield(False, subfield_lib.SubfieldCategory.DESCRIPTOR,
                               'hi', ctx)
    self.assertIsInstance(sf.GetFindings()[0], findings_lib.IllegalKeyTypeError)

  def testCreateSubfieldIllegalName(self):
    ctx = findings_lib.FileContext('{0}/file.yaml'.format(_GOOD_PATH))
    sf = subfield_lib.Subfield(
        'goo-1d', subfield_lib.SubfieldCategory.DESCRIPTOR, 'hi', ctx)
    self.assertIsInstance(sf.GetFindings()[0],
                          findings_lib.IllegalCharacterError)

  def testCreateSubfield(self):
    ctx = findings_lib.FileContext('{0}/file.yaml'.format(_GOOD_PATH))
    sf = subfield_lib.Subfield('good', subfield_lib.SubfieldCategory.DESCRIPTOR,
                               'hi', ctx)
    self.assertEmpty(sf.GetFindings())


if __name__ == '__main__':
  absltest.main()
