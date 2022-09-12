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

"""Constants for the GUID generator application."""

from os import path

# internally, absolute path is used; github uses relative path
_USE_ABSOLUTE_PATH = False

if _USE_ABSOLUTE_PATH:
  REPO_ROOT = path.join('third_party', 'digitalbuildings')
else:
  REPO_ROOT = path.join(
      path.dirname(path.realpath(__file__)), path.join('..', '..'))

APPLICATION_ROOT = path.join(REPO_ROOT, 'tools', 'guid_generator')
