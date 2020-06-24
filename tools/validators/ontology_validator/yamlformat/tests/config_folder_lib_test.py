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

"""Tests for corp.bizapps.rews.carson.ontology.validation.config_folder_lib."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl.testing import absltest

# TODO(berkoben) Write tests for this lib.  Currently all functionality is
# covered because ConfigFolder is inherited and all methods are tested
# indirectly in child classes.


class BaseLibTest(absltest.TestCase):

  def test_give_me_a_name(self):
    pass


if __name__ == '__main__':
  absltest.main()
