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
"""Shared classes for use in objects describing ontology components.

Classes representing ontology components parsed from files should use these.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import os
import re
import enum
import typing

# Holds the root path to the ontology and relative path to a file from the root
PathParts = typing.NamedTuple('PathParts', [('root', str),
                                            ('relative_path', str)])

GOOGLE3_REGEX = re.compile(r'^.*google3/(.*$)')
# Isolates the first segment of a typename, typically the equipment class
EQUIPMENT_CLASS_REGEX = re.compile(r'^(.*/)?([a-zA-Z]+)(_.*)*$')
GLOBAL_NAMESPACE = ''

DEPRECATED_TYPES = frozenset([
    'DEPRECATED', '/DEPRECATED', 'HVAC/DEPRECATED', 'INCOMPLETE', '/INCOMPLETE',
    'HVAC/INCOMPLETE'
])


class ComponentType(enum.Enum):
  """Possible component types for a folder to contain."""
  SUBFIELD = 'subfields'
  MULTI_STATE = 'states'
  FIELD = 'fields'
  ENTITY_TYPE = 'entity_types'
  UNIT = 'units'
  CONNECTION = 'connections'

  @classmethod
  def FromString(cls, value: str):
    """Returns a ComponentType instance matching the provided string."""
    for _, member in cls.__members__.items():
      if member.value == value:
        return member
    raise LookupError('Invalid component: ' + value)


def GetTreeLocation(relpath: str):
  """Returns folderpath and ComponentType obtained from parsing a path.

  Given a relative path from the root of the ontology, the method identifies the
  path to the top level of the compoment folder and the ComponentType of the
  folder.

  Args:
    relpath: relative path to the folder from ontology root.

  Raises:
    ValueError: if the path cannot be parsed according to folder structure rules
  """

  testpath = relpath
  component = None
  folderpath = None
  leading_directories = 0
  while testpath:
    path_pair = os.path.split(testpath)
    if component:
      leading_directories += 1
    else:
      try:
        component = ComponentType.FromString(path_pair[1])
        folderpath = testpath
      except LookupError:
        pass
    testpath = path_pair[0]

  if leading_directories > 1 or not component:
    raise ValueError('Invalid directory name: ' + relpath)

  return folderpath, component


def HasDeprecatedType(parent_names):
  """True if list contains a DEPRECATED or INCOMPLETE type name.

  Args:
    parent_names: a list of parent names from an entity. qualified or not
  """
  return DEPRECATED_TYPES.intersection(parent_names)


def GetEquipmentClass(typename):
  """Parses out the equipment class from a typename.

  Args:
    typename: a relative or fully qualified typename

  Returns:
    The equipment class string or None
  """
  p_match = EQUIPMENT_CLASS_REGEX.match(typename)
  if p_match:
    return p_match.group(2)
  return None


def GetGoogle3RelativePath(path):
  """Parses out google3 local path from an absolute path.

  Args:
    path: a path to a directory in google3

  Returns:
    the relative path to google3 with no leading / or None
  """

  m = GOOGLE3_REGEX.match(path)
  if m is not None:
    return m.group(1)
  return None
