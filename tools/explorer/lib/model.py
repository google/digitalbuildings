# Copyright 2021 Google LLC
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

"""Helper Field model classes for Ontology explorer."""
from typing import List

from yamlformat.validator.entity_type_lib import EntityType
from yamlformat.validator.field_lib import FIELD_CHARACTER_REGEX
from yamlformat.validator.field_lib import FIELD_INCREMENT_REGEX


class StandardField(object):
  """A class to represent a generic field without increment or optionality.

    Args:
        namespace_name: a field's defined namespace as a string.
        standard_field_name: the un-incremented name of the field as a string.
          must be lower-case and properly formatted.
    Attributes:
        namespace: the name of the namespace as a string
        name: the field name as a string.
    returns: An instance of the StandardField class.
  """

  def __init__(self, namespace_name: str, standard_field_name: str):
    super().__init__()
    if not FIELD_CHARACTER_REGEX.match(standard_field_name):
      raise ValueError(
          f'{namespace_name}/{standard_field_name} is incorrectly formatted')
    else:
      self._namespace = namespace_name
    self._name = standard_field_name

  def __hash__(self):
    return hash((self._namespace, self._name))

  def __eq__(self, other):
    try:
      namespace_eq = self._namespace == other.GetNamespaceName()
      name_eq = self._name == other.GetStandardFieldName()
      return name_eq and namespace_eq
    except AttributeError as ae:
      print(ae)
    except Exception as e:
      print(e)

  def __str__(self):
    return f'{self._namespace}/{self._name}'

  def GetNamespaceName(self) -> str:
    """Returns namespace variable as a string."""
    return self._namespace

  def GetStandardFieldName(self) -> str:
    """Returns the unqualified field name.

    without any increment as a string
    """
    return self._name


class EntityTypeField(StandardField):
  """A class to represent a field assigned to a type and extends StandardField.

  Attributes:
      namespace_name: a field's defined namespace as a string.
      standard_field_name: the name of the field as a string.
      increment: the increment of the field under a type as a string.
      is_optional: optionality of the field relative to it's Entity Type as a
        boolean.

  Returns:
      An instance of the EntityTypeField class.
  """

  def __init__(self,
               namespace_name: str,
               standard_field_name: str,
               is_optional: bool,
               increment: str = ''):
    super().__init__(namespace_name, standard_field_name)
    if not FIELD_INCREMENT_REGEX.match(increment):
      raise ValueError(
          f'Incremement of {namespace_name}/{standard_field_name}{increment} ' +
          'is unproperly formatted')
    self._increment = increment
    self._is_optional = is_optional

  def __hash__(self):
    return hash(
        (self._namespace, self._name, self._increment, self._is_optional))

  def __eq__(self, other):
    if isinstance(other, StandardField):
      return super().__eq__(other)
    elif not isinstance(other, self.__class__):
      raise TypeError(
          '{str(other)} and {str(self)} must be EntityTypeField objects')
    else:
      standard_eq = super().__eq__(other)
      increment_eq = self._increment == other.GetIncrement()
      optional_eq = self._is_optional == other.IsOptional()
      return standard_eq and increment_eq and optional_eq

  def __str__(self):
    standard_str = super().__str__()
    if self._is_optional:
      return f'{standard_str}_{self._increment}: optional'
    return f'{standard_str}_{self._increment}: required'

  def GetIncrement(self) -> str:
    """Returns the EntityType Field's increment as a string."""
    return self._increment

  def IsOptional(self) -> bool:
    """Returns the optionality of the field as a boolean."""
    return self._is_optional


class Match(object):
  """A class to hold the information about a match.

  The match is between EntityTypeFields objects and an EntityType object lists.

  Attributes:
    field_list: list of StandardField objects
    entity_type: An instance of EntityType class
    match_score: an integer representing the closeness of match between
      field_list and entity_type

  Returns:
    An instance of the Match class
  """

  def __init__(self, field_list: List[StandardField], entity_type: EntityType,
               match_score: float):
    """Init.

    Args:
      field_list: a list of StandardField objects
      entity_type: an entity type which implements a subset of field_list
      match_score: the closeness of a match between field_list and entity type
      as an integer.
    """
    super().__init__()
    self._field_list = field_list
    self._entity_type = entity_type
    self._match_score = match_score

  def __eq__(self, other):
    field_eq = self._field_list == other.GetFieldList()
    type_eq = self._entity_type == other.GetEntityType()
    match_eq = self._match_score == other.GetMatchScore()
    return field_eq and type_eq and match_eq

  def __str__(self):
    return f'{self._entity_type.typename}-match score:{str(self._match_score)}'

  def GetFieldList(self) -> List[EntityTypeField]:
    """Returns the list of EntityTypeField objects for a match."""
    return self._field_list

  def GetEntityType(self) -> EntityType:
    """Returns the entity type for a match."""
    return self._entity_type

  def GetMatchScore(self) -> int:
    """Returns the Match Type for a match."""
    return self._match_score

def StandardizeField(field: EntityTypeField) -> StandardField:
  return StandardField(field.GetNamespaceName(), field.GetStandardFieldName())
