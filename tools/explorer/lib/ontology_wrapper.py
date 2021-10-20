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

"""Ontology wrapper class for DBO explorer."""
from typing import List, Set
import sys

from lib.model import EntityTypeField
from lib.model import Match
from lib.model import StandardField

from yamlformat.validator.entity_type_lib import EntityType
from yamlformat.validator.entity_type_manager import EntityTypeManager
from yamlformat.validator.presubmit_validate_types_lib import ConfigUniverse

sys.tracebacklimit = 0

class OntologyWrapper(object):
  """Class providing an interface to do lookups on DBO.

     Attributes:
          universe: A ConfigUniverse object detailing the various universes in
            DBO.
          manager: An EntityTypeManager object to find greatest common subsets
            of fields between entity types and complete lists of inherited
            fields for a concrete entity. This is primarily used for
            _CreateMatch().

     Returns:
          An instance of OntologyWrapper class.
  """

  def __init__(self, universe: ConfigUniverse):
    """Init.

    Args:
      universe: an instantiated ConfigUniverse Object with inherited fields
        expanded.
    """
    super().__init__()
    self.universe = universe
    self.manager = EntityTypeManager(self.universe)

  def GetFieldsForTypeName(
      self,
      namespace: str,
      entity_type_name: str,
      required_only: bool = False) -> List[EntityTypeField]:
    """Gets a list of fields for a given typename within a namespace.

    Args:
       namespace: the name of the namespace as a string.
       entity_type_name: the name of the entity type as a string.
       required_only: when true will return only required fields for a given
         type.

    Returns:
            result_fields: a list of EntityTypeField objects.
    """
    entity_type = self.universe.entity_type_universe.GetEntityType(
        namespace,
        entity_type_name
    )
    if entity_type is None:
      if namespace == '':
        raise ValueError(
            f'\n{entity_type_name} is not defined in global namespace.'
        )
      else:
        raise ValueError(
            f'\n{entity_type_name} is not defined in namespace: {namespace}.'
        )
    if not entity_type.inherited_fields_expanded:
      raise Exception(
          'Inherited fields must be expanded to query fields.\n'+
          'Run NamespaceValidator on your ConfigUniverse to expand fields.'
      )
    # Entity_type_lib.FieldParts NamedTuple to EntityTypeField object.
    entity_type_fields = []
    for qualified_field in entity_type.GetAllFields().values():
      new_entity_type_field = EntityTypeField(qualified_field.field.namespace,
                                              qualified_field.field.field,
                                              qualified_field.optional,
                                              qualified_field.field.increment)
      entity_type_fields.append(new_entity_type_field)

    if required_only:
      entity_type_fields = [
          field for field in entity_type_fields if not field.IsOptional()
      ]
    entity_type_fields_sorted = sorted(
        entity_type_fields,
        key=lambda x: x.GetStandardFieldName(),
        reverse=False)

    return entity_type_fields_sorted

  def _CalculateMatchWeight(self, concrete_fields: Set[EntityTypeField],
                            canonical_fields: Set[EntityTypeField]) -> float:
    """Determines the weight of a match and returns that weight as a float.

    Finds the size of the intersection(x) between the two sets of fields and
    the size of the sets of fields unique to the concrete entity and canonical
    type(y and z). These three variables are input into the function
    f(x,y,z) = 1/((x^2)+(z-y)) to determine the weight.

    Args:
      concrete_fields: A set of EntityTypeField objects belonging to the
        concrete entity being matched.
      canonical_fields: A set of EntityTypeField objects belonging to an Entity
        Type defined in DBO.

    Returns:
      The weight of the match as a floating point number.
    """

  def _CreateMatch(self, field_list: List[EntityTypeField],
                   entity_type: EntityType) -> Match:
    """Determines the match between: EntityType and EntityTypeFields.

    calls _CalculateMatchWeight() on field_list and the set of fields belonging
    to entity_type. The weight function outputs a weight signifying the
    closeness of the match and an instance of the Match class is created with
    field_list, entity_type, and weight as arguments.

    Args:
      field_list: A list of EntityTypeField objects.
      entity_type: An EntityType object.

    Returns:
      An instance of the Match class.
    """
    pass

  def GetEntityTypesFromFields(self,
                               field_list: List[EntityTypeField],
                               general_type: str = None) -> List[EntityType]:
    """Get a list of EntityType objects matching a list of EntityTypeFields.

    Args:
        field_list: a list of EntityTypeField objects to match to an entity
        general_type: a string indicating a general type name to filter return
          results.

    Returns:
          entities: a list of EntityType objects matching the provided list of
          fields.
    """
    pass

  def IsFieldValid(self, field: StandardField) -> bool:
    """A method to validate a field name against the ontology."""
    if not isinstance(field, StandardField):
      raise TypeError(
          'Field argument must be a StandardField object.\n'+
          f'You provided a {type(field)} object.'
      )
    namespace_name = field.GetNamespaceName()
    standard_field_name = field.GetStandardFieldName()
    validity = self.universe.field_universe.IsFieldDefined(
        namespace_name=namespace_name, fieldname=standard_field_name)
    return validity
