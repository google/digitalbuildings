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

"""Link between two entities."""

class Link(object):
  """A link between a source and target field of two entities.

  The target entity is implied to be the same as the entity that contains this
  Link instance.

  Args:
    source: source entity name
    field_map: map from target entity field names to source entity field names
  """

  def __init__(self, source, field_map):
    super().__init__()
    self.source = source
    self.field_map = field_map
