"""
Ontology wrapper class for ontology explorer exposing certain functionality
of the Digital Buildings Ontology.
"""
from typing import List

from yamlformat.validator.entity_type_lib import EntityType
from yamlformat.validator.entity_type_manager import EntityTypeManager
from yamlformat.validator.presubmit_validate_types_lib import ConfigUniverse

from lib.model import StandardField
from lib.model import EntityTypeField
from lib.model import Match

class OntologyWrapper(object):
  """Class providing an interface to do lookups on a DigitalBuildings ontology.

     Attributes:
          universe: A ConfigUniverse object detailing the various universes in
            the ontology
          manager: An EntityTypeManager object to find greatest common subsets
            of fields between entity types and complete lists of inheritied
            fields for an entity type. This is primarily used for
            _CreateMatch().

     Returns:
          An instance of Ontology class.
  """

  # TODO(travis):Validate that universe has types expanded and fast-fail if not
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
      required_only: bool = False
  ) -> List[EntityTypeField]:
    """Gets a list of fields for a given typename within a namespace.

    Args:
       namespace: the name of the namespace as a string.
       entity_type_name: the name of the entity type as a string.
       required_only: when true will return only required fields for a given
         type.

    Returns:
            result_fields: a list of StandardField tuples
    """
    entity_type = self.universe.entity_type_universe.GetEntityType(
        namespace,
        entity_type_name
    )
    # Entity_type_lib.FieldParts NamedTuple to EntityTypeField object.
    entity_type_fields = [
        EntityTypeField(
            namespace_name=qualified_field.field.namespace,
            standard_field_name=qualified_field.field.field,
            is_optional=qualified_field.optional,
            increment=qualified_field.field.increment
        )
        for qualified_field in entity_type.GetAllFields().values()
    ]
    if required_only:
      entity_type_fields = [
          field for field in entity_type_fields if not field.IsOptional()
      ]
    entity_type_fields_sorted = sorted(
        entity_type_fields,
        key=lambda x: x.GetStandardFieldName(),
        reverse=False
    )

    return entity_type_fields_sorted

  def _CreateMatch(
      self,
      field_list: List[EntityTypeField],
      entity_type: EntityType
  ) -> Match:
    """
    Determines the closeness of a match between an EntityType object and a list
    of EntityTypeField objects by applying set operations provided by the
    EntityTypeManager on the required field of an EntityType's list of fields
    and the list of EntityType objects.

    If the list of EntityTypeField objects is a strict subset of the EntityType
    fields, then the match is CLOSE. If the reverse is true, the the match is
    INCOMPLETE, as the ontology does not inherit all of the fields necessary.
    If the two sets are equal, then the match is EXACT. If the sets are
    disjoint, the match is NONE.

    args:
      field_list: A list of EntityTypeField objects
      entity_type: An EntityType object

    Returns:
      An instance of the Match class
    """
    pass

  def GetEntityTypesFromFields(
      self,
      field_list: List[EntityTypeField],
      general_type: str = None
  ) -> List[EntityType]:
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
    namespace_name = field.GetNamespaceName()
    standard_field_name = field.GetStandardFieldName()
    validity = self.universe.field_universe.IsFieldDefined(
        namespace_name=namespace_name,
        fieldname=standard_field_name
    )
    return validity
