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

from typing import Dict, List, Optional

from model.constants import ENTITY_TYPE_KEY
from model.constants import GENERAL_TYPE_KEY
from model.constants import NAMESPACE_KEY
from model.constants import OPTIONAL_FIELDS_KEY
from model.constants import REQUIRED_FIELDS_KEY
from lib import ontology_wrapper
from lib.model import StandardField


class EntityType(object):
  """Class to store DBO entity type information relevant to an entity.

  Attributes:
    namespace: An entity's namespace in Digital Buildings Ontology.
    general_type: An entity's general type in Digital Buildings Ontology.
    required_fields: A list of standard field names required for a DBO entity
      type.
    optional_fields: A list of standard field names not required for a DBO enity
      type.
    entity_type_name: An entity's type as defined in Digital Buildings Ontology.
  """

  def __init__(self,
               namespace: str,
               general_type: str,
               required_fields: List[str],
               optional_fields: Optional[List[str]] = None,
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
  def FromDict(cls, entity_type_dict: Dict[str, str],
               ontology: ontology_wrapper.OntologyWrapper):
    """Creates an instance of EntityType class from a dictionary of entity type attributes.

    Args:
      entity_type_dict: A mapping of entity type attributes to corresponding
        values from a loadsheet of building configuration.
      ontology: An instance of OntologyWrapper to interface with DBO.

    Returns:
      An instance of EntityType class.
    """
    all_fields = entity_type_dict[
        REQUIRED_FIELDS_KEY] + entity_type_dict[
            OPTIONAL_FIELDS_KEY]
    entity_type = None
    if entity_type_dict[ENTITY_TYPE_KEY] is None:
      entity_type = cls.GetEntityTypeForStandardFieldList(
          cls, raw_field_list=all_fields, ontology=ontology)
    else:
      entity_type = entity_type_dict[ENTITY_TYPE_KEY]
    return cls(
        namespace=entity_type_dict[NAMESPACE_KEY],
        general_type=entity_type_dict[GENERAL_TYPE_KEY],
        required_fields=entity_type_dict[REQUIRED_FIELDS_KEY],
        optional_fields=entity_type_dict[OPTIONAL_FIELDS_KEY],
        entity_type=entity_type
    )

  def GetEntityTypeForStandardFieldList(
      self, raw_field_list: List[str],
      ontology: ontology_wrapper.OntologyWrapper) -> str:
    """Calls entity type matcher to determine an entity's type based on a list of fields.

    Args:
      raw_field_list: A list of standard field names to use as input with the
        entity type matcher.
      ontology: An OntologyWrapper instance for interfacing with DBO.

    Returns:
      A canonical entity type corresponding to the input fields.
    """
    standard_field_list = []
    for field in raw_field_list:
      standard_field = StandardField(
          standard_field_name=field,
          namespace_name=''
      )
      if ontology.IsFieldValid(standard_field):
        standard_field_list.append(standard_field)
    matches = ontology.GetEntityTypesFromFields(field_list=standard_field_list)
    generated_type_name = matches[0].GetEntityType().typename
    return generated_type_name
