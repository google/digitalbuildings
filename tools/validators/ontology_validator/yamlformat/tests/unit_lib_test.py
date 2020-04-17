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
"""Tests google3.corp.bizapps.rews.carson.ontology.validation.unit_lib."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from yamlformat.validator import findings_lib
from yamlformat.validator import unit_lib
from absl.testing import absltest

_GOOD_PATH = '{0}/units/anyfolder'.format('mynamespace')


class UnitLibTest(absltest.TestCase):

  def testUnitUniverseGetUnitsMap(self):
    folder = unit_lib.UnitFolder(_GOOD_PATH)
    namespace = folder.local_namespace
    namespace.InsertUnit(unit_lib.Unit('degrees_celsius', 'temperature', False))
    namespace.InsertUnit(unit_lib.Unit('kelvins', 'temperature', True))
    unit_universe = unit_lib.UnitUniverse([folder])

    units = unit_universe.GetUnitsMap('mynamespace')

    self.assertIn('degrees_celsius', units)
    self.assertIn('kelvins', units)

  def testUnitUniverseGetFindings(self):
    context = findings_lib.FileContext('{0}/file.yaml'.format(_GOOD_PATH))
    folder = unit_lib.UnitFolder(_GOOD_PATH)
    folder.AddFinding(findings_lib.InconsistentFileLocationError('', context))
    namespace = folder.local_namespace
    namespace.AddFinding(
        findings_lib.DuplicateUnitDefinitionError(
            unit_lib.Unit('unit', 'measurement'), 'namespace'))
    unit = unit_lib.Unit('unit', 'measurement')
    unit.AddFinding(findings_lib.UnknownUnitTagError(unit.name, 'tag', context))
    namespace.InsertUnit(unit)
    unit_universe = unit_lib.UnitUniverse([folder])

    findings = unit_universe.GetFindings()

    self.assertLen(findings, 3)
    self.assertTrue(
        unit_universe.HasFindingTypes([
            findings_lib.InconsistentFileLocationError,
            findings_lib.DuplicateUnitDefinitionError,
            findings_lib.UnknownUnitTagError,
        ]))
    self.assertFalse(unit_universe.IsValid())

  def testUnitFolderAddValidUnit(self):
    folder = unit_lib.UnitFolder(_GOOD_PATH)
    folder.AddUnit(unit_lib.Unit('unit', 'measurement'))
    self.assertIn('unit', folder.local_namespace.units)
    self.assertEmpty(folder.GetFindings())

  def testUnitFolderAddInvalidUnitFails(self):
    folder = unit_lib.UnitFolder(_GOOD_PATH)
    folder.AddUnit(unit_lib.Unit('bad-unit', 'invalid'))
    self.assertNotIn('bad-unit', folder.local_namespace.units)
    self.assertIsInstance(folder.GetFindings()[0],
                          findings_lib.IllegalCharacterError)

  def testUnitFolderAddDuplicateUnitFails(self):
    folder = unit_lib.UnitFolder(_GOOD_PATH)
    folder.AddUnit(unit_lib.Unit('unit', 'measurement'))
    self.assertIn('unit', folder.local_namespace.units)
    self.assertEmpty(folder.local_namespace.GetFindings())
    folder.AddUnit(unit_lib.Unit('unit', 'duplicate'))
    self.assertIsInstance(folder.local_namespace.GetFindings()[0],
                          findings_lib.DuplicateUnitDefinitionError)

  def testUnitFolderAddFromConfig(self):
    doc = {
        'temperature': [{
            'kelvins': 'STANDARD'
        }, 'degrees_celsius'],
    }
    folder = unit_lib.UnitFolder(_GOOD_PATH)
    folder.AddFromConfig([doc], '{0}/file.yaml'.format(_GOOD_PATH))

    units = folder.local_namespace.units
    self.assertEmpty(folder.GetFindings())
    self.assertCountEqual(['kelvins', 'degrees_celsius'], units)
    self.assertEqual(units['kelvins'],
                     unit_lib.Unit('kelvins', 'temperature', True))
    self.assertEqual(units['degrees_celsius'],
                     unit_lib.Unit('degrees_celsius', 'temperature', False))

  def testUnitFolderAddFromConfigInvalidUnitFormat(self):
    doc = {
        'temperature': [{
            'kelvins': 'STANDARD'
        }, {
            'something': 'oops',
            'huh': 'what'
        }],
    }
    folder = unit_lib.UnitFolder(_GOOD_PATH)
    folder.AddFromConfig([doc], '{0}/file.yaml'.format(_GOOD_PATH))
    self.assertIsInstance(folder.GetFindings()[0],
                          findings_lib.InvalidUnitFormatError)

  def testUnitFolderAddFromConfigUnknownUnitTag(self):
    doc = {
        'temperature': [{
            'kelvins': 'STANDARD'
        }, {
            'wrong': 'BAD_TAG'
        }],
    }
    folder = unit_lib.UnitFolder(_GOOD_PATH)
    folder.AddFromConfig([doc], '{0}/file.yaml'.format(_GOOD_PATH))
    self.assertIsInstance(folder.GetFindings()[0],
                          findings_lib.UnknownUnitTagError)

  def testUnitFolderAddFromConfigTooFewStandardUnits(self):
    doc = {
        'temperature': ['kelvins', 'degrees_celsius'],
    }
    folder = unit_lib.UnitFolder(_GOOD_PATH)
    folder.AddFromConfig([doc], '{0}/file.yaml'.format(_GOOD_PATH))
    self.assertIsInstance(folder.GetFindings()[0],
                          findings_lib.StandardUnitCountError)

  def testUnitFolderAddFromConfigTooManyStandardUnits(self):
    doc = {
        'temperature': [{
            'kelvins': 'STANDARD'
        }, {
            'degrees_celsius': 'STANDARD',
        }],
    }
    folder = unit_lib.UnitFolder(_GOOD_PATH)
    folder.AddFromConfig([doc], '{0}/file.yaml'.format(_GOOD_PATH))
    self.assertIsInstance(folder.GetFindings()[0],
                          findings_lib.StandardUnitCountError)

  def testUnitWithIllegalKeyTypeHasFindings(self):
    unit = unit_lib.Unit(False, 'invalid')
    self.assertIsInstance(unit.GetFindings()[0],
                          findings_lib.IllegalKeyTypeError)

  def testUnitWithIllegalNameHasFindings(self):
    unit = unit_lib.Unit('BADUNIT', 'invalid')
    self.assertIsInstance(unit.GetFindings()[0],
                          findings_lib.IllegalCharacterError)

  def testUnitEquals(self):
    unit_one = unit_lib.Unit('unit_one', 'measurement')
    unit_one_dup = unit_lib.Unit('unit_one', 'measurement')
    unit_one_diff_measurement = unit_lib.Unit('unit_one', 'changed')
    unit_one_standard = unit_lib.Unit('unit_one', 'measurement', True)
    unit_two = unit_lib.Unit('unit_two', 'measurement')
    self.assertEqual(unit_one, unit_one_dup)
    self.assertNotEqual(unit_one, unit_one_diff_measurement)
    self.assertNotEqual(unit_one, unit_one_standard)
    self.assertNotEqual(unit_one, unit_two)


if __name__ == '__main__':
  absltest.main()
