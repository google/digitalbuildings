# Copyright 2022 Google LLC
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
"""Tests for States class."""

from absl.testing import absltest

from model.units import Units


class UnitsTest(absltest.TestCase):

  def setUp(self):
    super().setUp()
    self.test_unit_path = 'pointset.points.filter_differential_pressure_setpoint.units'
    self.test_units_map = {'pascals': 'Pa'}

  def testUnitsInit(self):
    test_units = Units(self.test_unit_path, self.test_units_map)

    self.assertEqual(
        test_units.raw_unit_path,
        'pointset.points.filter_differential_pressure_setpoint.units')
    self.assertEqual(test_units.standard_to_raw_unit_map, {'pascals': 'Pa'})

if __name__ == '__main__':
  absltest.main()
