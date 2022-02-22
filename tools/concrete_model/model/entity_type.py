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
"""Module for canonical entity types."""

from typing import Optional, List, Dict


class EntityType(object):
  """Class to store DBO entity type information relevant to an entity.

  Attributes:
    namespace: An entity's namespace in digital buildings ontology.
    general_type: An entity's general type in digital buildings ontology.
    required_fields: A list of standard field names required for a DBO entity
      type.
    optional_fields: A list of standard field names not required for a DBO enity
      type.
    entity_type_name: An entity's type as defined in digital buildings ontology.
  """

  def __init__(self,
               namespace: str,
               general_type: str,
               required_fields: List[str],
               optional_fields: Optional[List[str]],
               entity_type: Optional[str] = None):
    """Init.

    Args:
      namespace: An entity's namespace in digital buildings ontology.
      general_type: An entity's general type in digital buildings ontolgogy.
      required_fields: A list of standard field names required for a DBO entity
        type.
      optional_fields: [Optional] List of standard field names not required for
        a DBO enity type.
      entity_type: [Optional] Entity type as defined in digital buildings
        ontology.
    """
    self.namespace = namespace
    self.general_type = general_type
    self.required_fields = required_fields
    self.optional_fields = optional_fields
    self.entity_type_name = entity_type

  @classmethod
  def FromDict(cls, entity_type_dict: Dict[str, str]):
    """Creates an instance of EntityType class from a dictionary of entity type attributes.

    Args:
      entity_type_dict: A mapping of entity type attributes to corresponding
        values from a loadsheet of building configuration.

    Returns:
      An instance of EntityType class.
    """

  def GetEntityTypeForStandardFieldList(self, fields: List[str]) -> str:
    """Calls entity type matcher to determine an entity's type based on a list of fields.

    Args:
      fields: A list of standard field names to use as input with the entity
        type matcher.

    Returns:
      A canonical entity type corresponding to the input fields.
    """
