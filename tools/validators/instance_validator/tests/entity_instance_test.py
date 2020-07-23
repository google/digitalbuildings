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

"""Tests for entity_instance.py"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from validate import generate_universe
from validate import entity_instance
from absl.testing import absltest

import instance_parser
import os

_TESTCASE_PATH = os.path.join('.', 'tests', 'fake_instances')

class EntityInstanceTest(absltest.TestCase):

  def setUp(self):
    self.universe = generate_universe.BuildUniverse()

  def testValidateGoodExample(self):
    parsed = dict(instance_parser.parse_yaml(
      os.path.join(_TESTCASE_PATH,
                   'GOOD',
                   'good_building_type.yaml')))

    entity_names = list(parsed.keys())

    for name in entity_names:
      entity = dict(parsed[name])
      instance = entity_instance.EntityInstance(entity, self.universe)

      if instance.IsValidEntityInstance() is False:
        self.fail('exception incorrectly raised')

  def testValidateBadEntityTypeFormat(self):
    parsed = dict(instance_parser.parse_yaml(
      os.path.join(_TESTCASE_PATH,
                   'BAD',
                   'bad_building_type.yaml')))

    entity_names = list(parsed.keys())

    for name in entity_names:
      entity = dict(parsed[name])
      instance = entity_instance.EntityInstance(entity, self.universe)

      if instance.IsValidEntityInstance() is not False:
        self.fail('exception not raised')

  def testValidateBadEntityNamespace(self):
    parsed = dict(instance_parser.parse_yaml(
      os.path.join(_TESTCASE_PATH,
                   'BAD',
                   'bad_building_type_namespace.yaml')))

    entity_names = list(parsed.keys())

    for name in entity_names:
      entity = dict(parsed[name])
      instance = entity_instance.EntityInstance(entity, self.universe)

      if instance.IsValidEntityInstance() is not False:
        self.fail('exception not raised')

  def testValidateBadEntityType(self):
    parsed = dict(instance_parser.parse_yaml(
      os.path.join(_TESTCASE_PATH,
                   'BAD',
                   'bad_building_type_entity.yaml')))

    entity_names = list(parsed.keys())

    for name in entity_names:
      entity = dict(parsed[name])
      instance = entity_instance.EntityInstance(entity, self.universe)

      if instance.IsValidEntityInstance() is not False:
        self.fail('exception not raised')

if __name__ == '__main__':
  absltest.main()
