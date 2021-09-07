"""Ontology class for ontology explorer."""
from typing import List

from model import EntityTypeField as ETF
from model import StandardField

from yamlformat.validator.entity_type_lib import EntityType
from yamlformat.validator.presubmit_validate_types_lib import ConfigUniverse


class Ontology(object):
  """Class providing an interface to do lookups on a DigitalBuildings ontology.

     Args:
          universe: an instantiated ConfigUniverse Object with inherited fields
            expanded
     Attributes:
          universe: A ConfigUniverse object detailing the various universes in
            the ontology

     Returns:
          An instance of Ontology class
  """

  # TODO(travis):Validate that universe has types expanded and fast-fail if not
  def __init__(self, universe: ConfigUniverse):
    super().__init__()
    self.universe = universe

  def GetFieldsForTypeName(self,
                           namespace: str,
                           entity_type_name: str,
                           required_only: bool = False) -> List[ETF]:
    """Gets a list of fields for a given typename within a namespace.

    Args:
       namespace: the name of the namespace as a string.
       entity_type_name: the name of the entity type as a string.
       required_only: when true will return only required fields for a given
         type.

    Returns:
            result_fields: a list of StandardField tuples
    """
    pass

  def GetEntityTypesFromFields(self,
                               field_list: List[StandardField],
                               general_type: str = None) -> List[EntityType]:
    """Get a list of EntityType objects matching a list of StandardField tuples.

    Args:
        field_list: a list of StandardField tuples to match to an entity
        general_type: a string indicating a general type name to narrow return
          results

    Returns:
          entities: a list of EntityType objects
          matching the provided list of fields
    """
    pass

  def IsFieldValid(self, field: StandardField) -> bool:
    """A method to validate a field name against the ontology."""
    pass
