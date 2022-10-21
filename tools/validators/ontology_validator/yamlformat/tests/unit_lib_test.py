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

from absl.testing import absltest

from yamlformat.validator import findings_lib
from yamlformat.validator import unit_lib

_GOOD_PATH = '{0}/units/anyfolder'.format('mynamespace')


class UnitLibTest(absltest.TestCase):

  def testUnitUniverseGetUnitsForMeasurement(self):
    folder = unit_lib.UnitFolder(_GOOD_PATH)
    namespace = folder.local_namespace
    namespace.InsertUnit(
        'temperature',
        unit_lib.Unit(name='degrees_celsius', conversion_offset=273.15))
    namespace.InsertUnit('temperature',
                         unit_lib.Unit(name='kelvins', is_standard=True))
    namespace.InsertUnit('percent',
                         unit_lib.Unit(name='percent', is_standard=True))
    unit_universe = unit_lib.UnitUniverse([folder])

    units = unit_universe.GetUnitsForMeasurement('temperature', 'mynamespace')

    self.assertCountEqual(['degrees_celsius', 'kelvins'], units)

  def testFindingAddedForInvalidNamespace(self):
    folder = unit_lib.UnitFolder(_GOOD_PATH)
    namespace = folder.local_namespace
    namespace.parent_namespace = unit_lib.UnitNamespace('fake_parent')

    namespace.InsertUnit(
        'temperature',
        unit_lib.Unit(name='degrees_celsius', conversion_offset=273.15))
    unit_universe = unit_lib.UnitUniverse([folder])

    findings_universe = findings_lib.FindingsUniverse([folder])
    findings = findings_universe.GetFindings()

    self.assertLen(findings, 1)
    self.assertTrue(
        unit_universe.HasFindingTypes([findings_lib.InvalidUnitNamespaceError]))
    self.assertFalse(unit_universe.IsValid())

  def testUnitUniverseGetFindings(self):
    context = findings_lib.FileContext('{0}/file.yaml'.format(_GOOD_PATH))
    folder = unit_lib.UnitFolder(_GOOD_PATH)
    folder.AddFinding(findings_lib.InconsistentFileLocationError('', context))
    namespace = folder.local_namespace
    namespace.AddFinding(
        findings_lib.DuplicateUnitDefinitionError(namespace,
                                                  unit_lib.Unit('unit'),
                                                  context))
    unit = unit_lib.Unit('unit')
    unit.AddFinding(findings_lib.UnknownUnitTagError(unit.name, 'tag', context))
    namespace.InsertUnit('measurement', unit)
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
    folder.AddUnit('measurement', unit_lib.Unit('unit'))
    units = folder.local_namespace.GetUnitsForMeasurement('measurement')
    self.assertIn('unit', units)
    self.assertEmpty(folder.GetFindings())

  def testUnitFolderAddInvalidUnitFails(self):
    folder = unit_lib.UnitFolder(_GOOD_PATH)
    folder.AddUnit('invalid', unit_lib.Unit('bad-unit'))
    self.assertIsNone(folder.local_namespace.GetUnitsForMeasurement('invalid'))
    self.assertIsInstance(folder.GetFindings()[0],
                          findings_lib.InvalidUnitNameError)

  def testUnitFolderAddDuplicateUnitFails(self):
    folder = unit_lib.UnitFolder(_GOOD_PATH)
    folder.AddUnit('measurement', unit_lib.Unit('unit'))
    units = folder.local_namespace.GetUnitsForMeasurement('measurement')
    self.assertIn('unit', units)
    self.assertEmpty(folder.local_namespace.GetFindings())
    folder.AddUnit('measurement', unit_lib.Unit('unit'))
    self.assertIsInstance(folder.local_namespace.GetFindings()[0],
                          findings_lib.DuplicateUnitDefinitionError)

  def testUnitFolderAddFromConfig(self):
    doc = {
        'temperature': {
            'kelvins': 'STANDARD',
            'degrees_celsius': {
                'multiplier': 1,
                'offset': 273.15
            }
        }
    }
    folder = unit_lib.UnitFolder(_GOOD_PATH)
    folder.AddFromConfig([doc], '{0}/file.yaml'.format(_GOOD_PATH))

    units = folder.local_namespace.GetUnitsForMeasurement('temperature')
    self.assertEmpty(folder.GetFindings())
    self.assertCountEqual(['kelvins', 'degrees_celsius'], units)
    self.assertEqual(units['kelvins'],
                     unit_lib.Unit(name='kelvins', is_standard=True))
    self.assertEqual(
        units['degrees_celsius'],
        unit_lib.Unit(name='degrees_celsius', conversion_offset=273.15))

  def testUnitFolderAddFromConfigMultipleNoUnits(self):
    doc = {
        'powerfactor': {
            'no_units': 'STANDARD',
            'another_one': {
                'multiplier': 2,
                'offset': 0
            }
        },
        'voltageratio': {
            'no_units': 'STANDARD'
        },
    }
    folder = unit_lib.UnitFolder(_GOOD_PATH)
    folder.AddFromConfig([doc], '{0}/file.yaml'.format(_GOOD_PATH))
    pf_units = folder.local_namespace.GetUnitsForMeasurement('powerfactor')
    vr_units = folder.local_namespace.GetUnitsForMeasurement('voltageratio')

    self.assertEmpty(folder.GetFindings())
    self.assertCountEqual(['no_units', 'another_one'], pf_units)
    self.assertCountEqual(['no_units'], vr_units)

  def testUnitFolderAddFromConfigInvalidMeasurementFormat(self):
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
                          findings_lib.InvalidMeasurementFormatError)

  def testUnitFolderAddFromConfigInvalidUnitFormat(self):
    doc = {'temperature': {'kelvins': ['STANDARD']}}
    folder = unit_lib.UnitFolder(_GOOD_PATH)
    folder.AddFromConfig([doc], '{0}/file.yaml'.format(_GOOD_PATH))
    self.assertIsInstance(folder.GetFindings()[0],
                          findings_lib.InvalidUnitFormatError)

  def testUnitFolderAddFromConfigInvalidUnitConversionMultiplierKey(self):
    doc = {
        'temperature': {
            'kelvins': 'STANDARD',
            'degrees_celsius': {
                'multiply': 1,
                'offset': 273.15
            }
        }
    }
    folder = unit_lib.UnitFolder(_GOOD_PATH)
    folder.AddFromConfig([doc], '{0}/file.yaml'.format(_GOOD_PATH))
    units = folder.local_namespace.GetUnitsForMeasurement('temperature')
    self.assertIsInstance(folder.GetFindings()[0],
                          findings_lib.InvalidUnitConversionKeyError)
    self.assertCountEqual(['kelvins'], units)

  def testUnitFolderAddFromConfigInvalidUnitConversionMultiplierValue(self):
    doc = {
        'temperature': {
            'kelvins': 'STANDARD',
            'degrees_celsius': {
                'multiplier': '1',
                'offset': 273.15
            }
        }
    }
    folder = unit_lib.UnitFolder(_GOOD_PATH)
    folder.AddFromConfig([doc], '{0}/file.yaml'.format(_GOOD_PATH))
    units = folder.local_namespace.GetUnitsForMeasurement('temperature')
    self.assertIsInstance(folder.GetFindings()[0],
                          findings_lib.InvalidUnitConversionValueError)
    self.assertCountEqual(['kelvins'], units)

  def testUnitFolderAddFromConfigInvalidUnitConversionOffsetKey(self):
    doc = {
        'temperature': {
            'kelvins': 'STANDARD',
            'degrees_celsius': {
                'multiplier': 1,
                'OFFSET': 273.15
            }
        }
    }
    folder = unit_lib.UnitFolder(_GOOD_PATH)
    folder.AddFromConfig([doc], '{0}/file.yaml'.format(_GOOD_PATH))
    units = folder.local_namespace.GetUnitsForMeasurement('temperature')
    self.assertIsInstance(folder.GetFindings()[0],
                          findings_lib.InvalidUnitConversionKeyError)
    self.assertCountEqual(['kelvins'], units)

  def testUnitFolderAddFromConfigInvalidUnitConversionOffsetValue(self):
    doc = {
        'temperature': {
            'kelvins': 'STANDARD',
            'degrees_celsius': {
                'multiplier': 1,
                'offset': '273.15'
            }
        }
    }
    folder = unit_lib.UnitFolder(_GOOD_PATH)
    folder.AddFromConfig([doc], '{0}/file.yaml'.format(_GOOD_PATH))
    units = folder.local_namespace.GetUnitsForMeasurement('temperature')
    self.assertIsInstance(folder.GetFindings()[0],
                          findings_lib.InvalidUnitConversionValueError)
    self.assertCountEqual(['kelvins'], units)

  def testUnitFolderAddFromConfigInvalidUnitConversionMap(self):
    doc = {
        'temperature': {
            'kelvins': 'STANDARD',
            'degrees_celsius': {
                'multiplier': 1
            }
        }
    }
    folder = unit_lib.UnitFolder(_GOOD_PATH)
    folder.AddFromConfig([doc], '{0}/file.yaml'.format(_GOOD_PATH))
    units = folder.local_namespace.GetUnitsForMeasurement('temperature')
    self.assertIsInstance(folder.GetFindings()[0],
                          findings_lib.InvalidUnitConversionMapError)
    self.assertCountEqual(['kelvins'], units)

  def testUnitFolderAddFromConfigUnknownUnitTag(self):
    doc = {'temperature': {'kelvins': 'STANDARD', 'wrong': 'BAD_TAG'}}
    folder = unit_lib.UnitFolder(_GOOD_PATH)
    folder.AddFromConfig([doc], '{0}/file.yaml'.format(_GOOD_PATH))
    units = folder.local_namespace.GetUnitsForMeasurement('temperature')
    self.assertIsInstance(folder.GetFindings()[0],
                          findings_lib.UnknownUnitTagError)
    self.assertCountEqual(['kelvins'], units)

  def testUnitFolderAddFromConfigTooFewStandardUnits(self):
    doc = {
        'temperature': {
            'kelvins': {
                'multiplier': 1,
                'offset': 0
            },
            'degrees_celsius': {
                'multiplier': 1,
                'offset': 273.15
            }
        }
    }
    folder = unit_lib.UnitFolder(_GOOD_PATH)
    folder.AddFromConfig([doc], '{0}/file.yaml'.format(_GOOD_PATH))
    self.assertIsInstance(folder.GetFindings()[0],
                          findings_lib.StandardUnitCountError)

  def testUnitFolderAddFromConfigTooManyStandardUnits(self):
    doc = {
        'temperature': {
            'kelvins': 'STANDARD',
            'degrees_celsius': 'STANDARD',
        }
    }
    folder = unit_lib.UnitFolder(_GOOD_PATH)
    folder.AddFromConfig([doc], '{0}/file.yaml'.format(_GOOD_PATH))
    self.assertIsInstance(folder.GetFindings()[0],
                          findings_lib.StandardUnitCountError)

  def testUnitWithIllegalKeyTypeHasFindings(self):
    unit = unit_lib.Unit(False)
    self.assertIsInstance(unit.GetFindings()[0],
                          findings_lib.IllegalKeyTypeError)

  def testUnitWithIllegalNameHasFindings(self):
    unit = unit_lib.Unit('BADUNIT')
    self.assertIsInstance(unit.GetFindings()[0],
                          findings_lib.InvalidUnitNameError)

  def testUnitEquals(self):
    unit_one = unit_lib.Unit('unit_one')
    unit_one_dup = unit_lib.Unit('unit_one')
    unit_one_standard = unit_lib.Unit(name='unit_one', is_standard=True)
    unit_two = unit_lib.Unit('unit_two')
    self.assertEqual(unit_one, unit_one_dup)
    self.assertNotEqual(unit_one, unit_one_standard)
    self.assertNotEqual(unit_one, unit_two)

  def testUnitFolderAddFromConfigMeasurementAlias(self):
    doc = {
        'length': 'distance',
        'distance': {
            'meters': 'STANDARD',
            'feet': {
                'multiplier': 0.3048,
                'offset': 0
            }
        }
    }
    folder = unit_lib.UnitFolder(_GOOD_PATH)
    expected_units = ['meters', 'feet']

    folder.AddFromConfig([doc], '{0}/file.yaml'.format(_GOOD_PATH))
    distance_units = folder.local_namespace.GetUnitsForMeasurement('distance')
    length_units = folder.local_namespace.GetUnitsForMeasurement('length')

    self.assertEmpty(folder.local_namespace.GetFindings())
    self.assertCountEqual(expected_units, distance_units)
    self.assertCountEqual(expected_units, length_units)

  def testUnitFolderAddFromConfigBadAliasBase(self):
    doc = {
        'length': 'invalid',
        'distance': {
            'meters': 'STANDARD',
            'feet': {
                'multiplier': 0.3048,
                'offset': 0
            }
        }
    }
    folder = unit_lib.UnitFolder(_GOOD_PATH)

    folder.AddFromConfig([doc], '{0}/file.yaml'.format(_GOOD_PATH))

    self.assertIsInstance(folder.local_namespace.GetFindings()[0],
                          findings_lib.UnrecognizedMeasurementAliasBaseError)

  def testUnitFolderAddFromConfigAliasIsAlias(self):
    doc = {
        'distance': {
            'meters': 'STANDARD',
            'feet': {
                'multiplier': 0.3048,
                'offset': 0
            }
        },
        'length': 'distance',
        'level': 'length',
    }
    folder = unit_lib.UnitFolder(_GOOD_PATH)

    folder.AddFromConfig([doc], '{0}/file.yaml'.format(_GOOD_PATH))

    self.assertIsInstance(folder.local_namespace.GetFindings()[0],
                          findings_lib.MeasurementAliasIsAliasedError)

  def testUnitFolderAddFromConfigDuplicateAlias(self):
    doc_1 = {
        'distance': {
            'yards': 'STANDARD',
            'inches': {
                'multiplier': 0.0277778,
                'offset': 0
            }
        },
        'level': 'distance',
    }
    doc_2 = {
        'length': {
            'meters': 'STANDARD',
            'feet': {
                'multiplier': 0.3048,
                'offset': 0
            }
        },
        'level': 'length',
    }
    folder = unit_lib.UnitFolder(_GOOD_PATH)

    folder.AddFromConfig([doc_1, doc_2], '{0}/file.yaml'.format(_GOOD_PATH))

    self.assertIsInstance(folder.local_namespace.GetFindings()[0],
                          findings_lib.DuplicateMeasurementAliasError)


if __name__ == '__main__':
  absltest.main()
