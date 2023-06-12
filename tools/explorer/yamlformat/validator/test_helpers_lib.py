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
"""Helpers for use in tests.

DON NOT USE IN PRODUCTION CODE.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from typing import List

from yamlformat.validator import entity_type_lib


def Field(fq_name: str, optional: bool = False) -> entity_type_lib.OptWrapper:
  """Creates a field Tuple from a fully qualified field name.

  Args:
    fq_name: fully qualified name of a field
    optional: whether or not this field is optional

  Returns:
    a OptWrapper tuple represting the field.
  """
  parts = fq_name.split('/')
  namespace = ''
  if len(parts) == 2:
    namespace = parts[0]
    fq_name = parts[1]
  match = entity_type_lib.FIELD_INCREMENT_STRIPPER_REGEX.match(fq_name)
  field = fq_name
  increment = ''
  if match:
    field = match.group(1)
    increment = match.group(2)
  return entity_type_lib.OptWrapper(
      field=entity_type_lib.FieldParts(
          namespace=namespace, field=field, increment=increment),
      optional=optional)


def Fields(fq_fields: List[str]) -> List[entity_type_lib.OptWrapper]:
  """Creates a qualified-field:tuple map for the list of qualified names.

  Args:
    fq_fields: an iterable of fully-qualified field names

  Returns:
    a list of OptWrapper tuples representing the field list with optional=False
  """
  return [Field(field, optional=False) for field in fq_fields]
