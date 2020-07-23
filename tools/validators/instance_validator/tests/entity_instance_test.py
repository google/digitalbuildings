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

_GOOD_EXAMPLE = {'UK-LON-S2': {'type': 'FACILITIES/BUILDING',
                               'id': 'FACILITIES/123456'}}
_BAD_TYPE_EXAMPLE = {'UK-LON-S2': {'type': 'FACILITIES/BUILDING/ERROR',
                                   'id': 'FACILITIES/123456'}}
_BAD_ENTITY_EXAMPLE = {'UK-LON-S2': {'type': 'LIGHTING/NOT_A_LAMP',
                                     'id': 'FACILITIES/123456'}}
_BAD_NAMESPACE_EXAMPLE = {'UK-LON-S2': {'type': 'NONEXISTENT/BUILDING',
                                        'id': 'FACILITIES/123456'}}

class EntityInstanceTest(absltest.TestCase):

  def setUp(self):
    self.universe = generate_universe.build_universe()

  def testValidateGoodExample(self):
    entity_names = list(_GOOD_EXAMPLE.keys())
    for name in entity_names:
      entity = dict(_GOOD_EXAMPLE[name])
      instance = entity_instance.EntityInstance(entity, self.universe)

      if instance.is_valid_entity_instance() is False:
        self.fail('exception incorrectly raised')

  def testValidateBadNamespaceExample(self):
    entity_names = list(_BAD_NAMESPACE_EXAMPLE.keys())
    for name in entity_names:
      entity = dict(_BAD_NAMESPACE_EXAMPLE[name])
      instance = entity_instance.EntityInstance(entity, self.universe)

      if instance.is_valid_entity_instance():
        self.fail('exception failed to raise')

  def testValidateBadTypeExample(self):
    entity_names = list(_BAD_TYPE_EXAMPLE.keys())
    for name in entity_names:
      entity = dict(_BAD_TYPE_EXAMPLE[name])
      instance = entity_instance.EntityInstance(entity, self.universe)

      if instance.is_valid_entity_instance():
        self.fail('exception failed to raise')

  def testValidateBadEntityExample(self):
    entity_names = list(_BAD_ENTITY_EXAMPLE.keys())
    for name in entity_names:
      entity = dict(_BAD_ENTITY_EXAMPLE[name])
      instance = entity_instance.EntityInstance(entity, self.universe)

      if instance.is_valid_entity_instance():
        self.fail('exception failed to raise')

if __name__ == '__main__':
  absltest.main()
