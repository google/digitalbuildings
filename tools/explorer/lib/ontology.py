"""Ontology class for ontology explorer"""
from typing import List

from yamlformat.validator.entity_type_lib import EntityType
from yamlformat.validator.presubmit_validate_types_lib import ConfigUniverse

from lib.model import StandardField
from lib.model import EntityTypeField as ETF
from lib.model import Match

class Ontology(object):
  """Class providing an interface to do lookups on a DigitalBuildings ontology

     Args:
          universe: an instantiated ConfigUniverse Object
          with inherited fields expanded

     Attributes:
          universe: A ConfigUniverse object detailing
          the various universes in the ontology

     Returns:
          An instance of Ontology class
  """

  #TODO: Validate that universe has types expanded and fast-fail if not
  def __init__(self, universe: ConfigUniverse):
    super().__init__()
    self.universe = universe

  def GetFieldsForTypeName(self,
                           namespace: str,
                           entity_type_name: str,
                           required_only: bool = False) -> List[ETF]:
    """Gets a list of fields for a given typename within a namespace

       Args:
            namespace: the name of the namespace as a string
            entity_type_name: name of the entity type as a string
            required_only: when true will return
            only required fields for a given type

       Returns:
            result_fields: a list of StandardField tuples
    """
    entity_type = self.universe.entity_type_universe.GetEntityType(
        namespace,
        entity_type_name
    )
    qualified_fields = entity_type.GetAllFields()
    field_optwrappers = [
        entity_type.GetField(field)
        for field in qualified_fields
    ]
    entity_type_fields = [
        ETF(namespace,
            field.field.field[0:],
            not field.optional,
            field.field.increment) for field in field_optwrappers
    ]
    if required_only:
      fields_temp = entity_type_fields
      entity_type_fields = []
      for field in fields_temp:
        if field.IsRequired():
          entity_type_fields.append(field)

    return entity_type_fields

  #TODO: Expand NONE matching logic
  def _CreateMatch(
      self,
      field_list: List[StandardField],
      entity_type: EntityType
  ) -> str:
    """Determines the closeness of the match between
    the field list and the entity type

    Args:
      field_list: a list of StandardField objects
      entity_type: An EntityType object

    Returns:
      The match type as a string
    """
    match_type = ''

    entity_field_optwrappers = entity_type.GetAllFields().values()
    entity_field_set = {
        StandardField(entity_type.namespace.namespace, ow.field.field)
        for ow in entity_field_optwrappers
    }
    input_field_set = set(field_list)

    if entity_field_set.issubset(input_field_set):
      if input_field_set.issubset(entity_field_set):
        match_type = 'EXACT'
    elif entity_field_set.issubset(input_field_set):
      if not input_field_set.issubset(entity_field_set):
        match_type = 'CLOSE'
    elif not entity_field_set.issubset(input_field_set):
      if input_field_set.issubset(entity_field_set):
        match_type = 'INCOMPLETE'
    else:
      match_type = 'NONE'
    my_match = Match(field_list, entity_type, match_type=match_type)
    return my_match

  def GetEntityTypesFromFields(self,
                               field_list: List[StandardField],
                               general_type: str = None,
                               match_type: str = None) -> List[EntityType]:
    """Gets a list of EntityType objects matching
       a given a list of StandardField tuples

       Args:
            field_list: a list of StandardField tuples to match to an entity
            general_type: a string indicating a general type name
            to narrow return results

       Returns:
            entities: a list of EntityType objects
            matching the provided list of fields
    """
    match_list = []

    field_list_namespace = {
        field.GetNamespaceName() for field in field_list
    }
    assert len(field_list_namespace) == 1, 'Fields not under one namespace'
    namespace = field_list_namespace.pop()
    my_namespace = self.universe.entity_type_universe.GetNamespace(namespace)
    for entity_type in my_namespace.valid_types_map.values():
      match = self._CreateMatch(field_list, entity_type)
      match_list.append(match)
    if match_type is None and general_type is None:
      return [
          match.GetEntityType() for match in match_list
          if match.GetMatchType() != 'NONE'
      ]
    elif match_type is None and general_type is not None:
      return [
          match.GetEntityType for match in match_list
          if general_type in match.GetEntityType().parent_names
          and match.GetMatchType() != 'NONE'
      ]
    elif match_type is not None and general_type is None:
      return [
          match.GetEntityType() for match in match_list
          if match.GetMatchType() == match_type
      ]
    elif match_type is not None and general_type is not None:
      return [
          match.GetEntityType() for match in match_list
          if general_type in match.GetEntityType().parent_names
          and match.GetMatchType() == match_type
      ]

  def IsFieldValid(self, field: StandardField) -> bool:
    """A method to validate a field name against the ontology"""
    namespace = field.GetNamespaceName()
    name = field.GetStandardFieldName()
    validity = self.universe.field_universe.IsFieldDefined(
        namespace,
        name
    )
    return validity

