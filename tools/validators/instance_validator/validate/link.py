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

  Args:
    source: source entity
    target: target entity
    source_field: name of the field on the source entity
    target_field: name of the field on the target entity

  Returns:
    A Link instance.
  """

  def __init__(self, source, target, source_field, target_field):
    super().__init__()
    self.source = source
    self.target = target
    self.source_field = source_field
    self.target_field = target_field
