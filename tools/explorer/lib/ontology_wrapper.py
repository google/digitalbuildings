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
from termcolor import colored
from typing import List
from typing import Set

from lib.model import EntityTypeField
from lib.model import Match
from lib.model import StandardField
from lib import model

from yamlformat.validator.entity_type_lib import EntityType
from yamlformat.validator.entity_type_manager import EntityTypeManager
from yamlformat.validator.presubmit_validate_types_lib import ConfigUniverse

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

    Raises:
      Exception: when inherited fields are not expanded.
    """
    entity_type = self.universe.entity_type_universe.GetEntityType(
        namespace, entity_type_name)
    if entity_type is None:
      if not namespace:
        raise ValueError(
            f'\n{entity_type_name} is not defined in global namespace.')
      else:
        raise ValueError(
            f'\n{entity_type_name} is not defined in namespace: {namespace}.')
    if not entity_type.inherited_fields_expanded:
      raise Exception(
          'Inherited fields must be expanded to query fields.\n' +
          'Run NamespaceValidator on your ConfigUniverse to expand fields.')
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

  def _CalculateMatchScore(self, concrete_fields: Set[StandardField],
                           canonical_fields: Set[EntityTypeField])-> int:
    """Calculates a match's score in [0, 100].

    The score of a match is determined by calculating the average of two
    f-scores. The first f-score is the measure of correctly matched required
    fields in the canonical type and the second f-score is the measure of
    correctly matched fields regardless of optionality. Adding the two f-scores
    creates a preference for matches with a higher quantity of matched required
    canonical fields, and dividing by 2 keeps the range of the function in
    [0, 100].

    Args:
      concrete_fields: A set of StandardField objects belonging to the
        concrete entity being matched.
      canonical_fields: A set of EntityTypeField objects belonging to an Entity
        Type defined in DBO.

    Returns:
      A match's score as an integer in [0, 100].
    """

    required_canonical_fields = {
        model.StandardizeField(field) for field in canonical_fields
        if not field.IsOptional()
    }

    standard_canonical_fields: Set[StandardField] = set()
    for field in canonical_fields:
      standard_canonical_fields.add(model.StandardizeField(field))

    matched_fields = len(
        concrete_fields.intersection(standard_canonical_fields)
    )
    matched_required_fields = len(
        concrete_fields.intersection(required_canonical_fields)
    )

    total_required_type_fields = len(required_canonical_fields)
    total_entity_fields = len(concrete_fields)
    unmatched_entity_fields = len(
        concrete_fields.difference(standard_canonical_fields)
    )
    unmatched_required_fields = len(
        required_canonical_fields.difference(concrete_fields)
    )

    if total_entity_fields <= 0:
      raise ValueError('Concrete field set cannot be empty.')

    total_precision = matched_fields - unmatched_entity_fields
    total_precision /= total_entity_fields

    if total_required_type_fields <= 0:
      match_score = total_precision / 2.0
    else:
      required_precision = matched_required_fields - unmatched_required_fields
      required_precision /= total_required_type_fields
      match_score = (total_precision + required_precision) / 2.0
    final_score = int((match_score + 1.0) * 50)
    assert final_score in range(0, 101), f'Score: {final_score} out of range'
    return final_score

  def _CreateMatch(self, field_list: List[StandardField],
                   entity_type: EntityType) -> Match:
    """Creates a Match instance for an EntityType object and a list of
    StandardField objects.

    calls _CalculateMatchWeight() on field_list and the set of fields belonging
    to entity_type. The scoring function outputs aan integer in [0, 100]
    signifying the closeness of the match, and an instance of the Match class is
    created with field_list, entity_type, and match_score as arguments.

    Args:
      field_list: A list of EntityTypeField objects for a concrete entity.
      entity_type: An EntityType object.

    Returns:
      An instance of Match class.
    """
    canonical_field_set = set()
    for qualified_field in entity_type.GetAllFields().values():
      new_entity_type_field = EntityTypeField(
          qualified_field.field.namespace,
          qualified_field.field.field,
          qualified_field.optional,
          qualified_field.field.increment
      )
      canonical_field_set.add(new_entity_type_field)

    match_score = self._CalculateMatchScore(
        concrete_fields=frozenset(field_list),
        canonical_fields=frozenset(canonical_field_set)
    )
    new_match = Match(
        field_list,
        entity_type,
        match_score
    )
    return new_match

  def GetEntityTypesFromFields(self,
                               field_list: List[StandardField],
                               return_size: int = 0,
                               general_type: str = None) -> List[Match]:
    """Get a list of Match objects for all entity types defined in DBO.

    Args:
      field_list: A list of StandardField objects to match to an entity.
      general_type: A string indicating a general type name to filter return
        results.
      return_size: An int for the length of the return list of matches.
        e.g. if return_size is 10, the 10 matches with the highest score will
        be returned.
    Returns:
      A sorted list of Match objects.
    """
    entity_type_list = []
    type_namespaces_list = self.universe.GetEntityTypeNamespaces()
    for tns in type_namespaces_list:
      for entity_type in tns.valid_types_map.values():
        if entity_type.is_abstract or entity_type.GetAllFields() == {}:
          continue
        if general_type is not None:
          if general_type.upper() in entity_type.unqualified_parent_names:
            entity_type_list.append(entity_type)
        else:
          entity_type_list.append(entity_type)

    match_list = []
    for entity_type in entity_type_list:
      match_list.append(self._CreateMatch(field_list, entity_type))

    match_list_sorted = sorted(
        match_list,
        key=lambda x: x.GetMatchScore(),
        reverse=True
    )
    if return_size > 0:
      return match_list_sorted[:return_size]
    return match_list_sorted

  def _PopulateMatrix(self, match: Match):
    """Creates a matrix defining field relationships within a match between a
    concrete entity and a canonical type.

    Args:
      match: A instance of Match class

    Returns:
      final_matrix: a matrix concrete fields matching to canonical fields
      all_fields: a list of fields for a concrete entity and canonical type
    """
    final_matrix = []
    concrete_field_set = set(match.GetFieldList())

    canonical_field_dict = {}
    for qualified_field in match.GetEntityType().GetAllFields().values():
      new_entity_type_field = EntityTypeField(
          qualified_field.field.namespace,
          qualified_field.field.field,
          qualified_field.optional,
          qualified_field.field.increment
      )
      new_standard_field = model.StandardizeField(new_entity_type_field)
      canonical_field_dict[new_standard_field] = new_entity_type_field

    standard_canonical_field_set = set(canonical_field_dict.keys())

    only_concrete = concrete_field_set.difference(standard_canonical_field_set)
    for field in only_concrete:
      final_matrix.append([str(field), '', ''])

    intersection = standard_canonical_field_set.intersection(concrete_field_set)
    for field in intersection:
      final_matrix.append(
          [str(field), str(field), canonical_field_dict[field].IsOptional()])

    only_canonical = standard_canonical_field_set.difference(concrete_field_set)
    for field in only_canonical:
      final_matrix.append(
          ['', str(field), canonical_field_dict[field].IsOptional()])

    all_fields = list(intersection) + list(only_concrete) + list(only_canonical)

    return final_matrix, all_fields

  #TODO(b/210673114): Have this method return an object rather than a string.
  def PrintFieldSetComparison(self, match: Match)-> str:
    """creates a text representation of field set relations for a given match.

    Takes the intersection and differences in sets between a set of fields
    belonging to an entity type and concrete entity to create a big string
    representation of matching fields within a match. This method will be called
    by explorer.py when a user wants to visualize the field relationships
    between a list of fields and an entity type within a match.

    Args:
      match: An instance of Match class for which a field set relation wants
      to be visualized.
    Returns:
      A string to visualize a field set relation
    """
    final_matrix, all_fields = self._PopulateMatrix(match)

    padding = 3
    col_width = max(len(str(field)) for field in all_fields) + padding
    return_string = ''
    return_string += colored('MATCH SCORE: ', 'yellow')
    return_string += str(match.GetMatchScore()) + '\n'
    return_string += colored('MATCHED TYPE: ', 'yellow')
    return_string += str(match.GetEntityType().typename) + '\n'
    return_string += '\n'
    return_string += ''.join(
        colored(field.ljust(col_width), 'yellow')
        for field in ['ACTUAL FIELDS', 'TYPE FIELDS', 'OPTIONALITY'])
    return_string += '\n'
    return_string += ''.join(
        field.ljust(col_width) for field in ['='*(col_width-padding)]*3)
    return_string += '\n'
    for row in final_matrix:
      if not row[2]:
        row[2] = 'Required'
      elif row[2]:
        row[2] = 'Optional'
      elif row[2] == '':
        continue
      if row[0] != '' and row[1] != '':
        return_string += ''.join(
            colored(field.ljust(col_width), 'green') for field in row)
      else:
        return_string += ''.join(field.ljust(col_width) for field in row)
      return_string += '\n'
    return_string += '\n'

    return return_string

  def IsFieldValid(self, field: StandardField) -> bool:
    """A method to validate a field name against the ontology."""
    if not isinstance(field, StandardField):
      raise TypeError('Field argument must be a StandardField object.\n' +
                      f'You provided a {type(field)} object.')
    namespace_name = field.GetNamespaceName()
    standard_field_name = field.GetStandardFieldName()
    validity = self.universe.field_universe.IsFieldDefined(
        namespace_name=namespace_name, fieldname=standard_field_name)
    return validity
