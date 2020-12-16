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

"""Connection between two entities."""

class Connection(object):
  """A connection between a source and target entity with a certain type.

  The target entity is implied to be the same as the entity that contains this
  Connection instance.

  Args:
    ctype: type of the connection
      (NOTE: 'type' is a reserved Python keyword)
    source: name of the source entity
  """

  def __init__(self, ctype, source):
    super().__init__()
    self.ctype = ctype
    self.source = source
