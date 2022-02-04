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
"""File parser for the configuration scoring tool."""
from typing import Dict, Optional, List

from validate import handler as validator
from validate.generate_universe import BuildUniverse

from score.dimensions.dimension import Dimension
from score.types import CloudDeviceId, DimensionName, TranslationsDict, DeserializedFile
from score.constants import FileTypes
PROPOSED, SOLUTION = FileTypes


class ParseConfig:
  """
    Attributes:
      args: Dictionary containing instance arguments
      universe: Built from the input ontology
      deserialized_files: Parsed configuration files
      results: Dictionary containing results for output

    Returns:
      An instance of the ParseConfig class.
  """
  def __init__(self,
               *,
               ontology: str,
               solution: str,
               proposed: str,
               verbose: Optional[bool] = False):
    """
      Arguments:
        ontology: Path to the ontology
        solution: Path to the solution config
        proposed: Path to the config to be evaluated
        verbose: Print specifics of missing types and translations (optional)
    """
    self.args = {
        'ontology': ontology,
        SOLUTION: solution,
        PROPOSED: proposed,
        'verbose': verbose
    }
    self.universe = BuildUniverse(modified_types_filepath=ontology)
    self.deserialized_files = {
        PROPOSED: validator.Deserialize([proposed])[0],
        SOLUTION: validator.Deserialize([solution])[0]
    }
    self.results = {}

  # TODO: refactor into smaller functions and return instead of printing
  def append_types(self):
    """
      Appends types or type names to deserialized files
    """
    for file_type, file in self.deserialized_files.items():
      translations_absent = []
      types_absent = []
      # TODO: This appends the full type to solution entities and only
      # the type name to proposed entities. Verify that this is the correct
      # behavior following implementation of the first dimension(s).
      type_or_name = 'type' if file_type == SOLUTION else 'type_name'

      for entity in file.values():
        entity.type = self.universe.GetEntityType(entity.namespace,
                                                  entity.type_name)

        if entity.type is None:
          types_absent.append(getattr(entity, type_or_name))
        if entity.links is not None:
          for link in entity.links:
            source = file[link.source] if link.source in file else None
            if source:
              if not getattr(source, 'type', None):
                source.type = self.universe.GetEntityType(
                    source.namespace, source.type_name)
                if source.type is None:
                  types_absent.append(getattr(source, type_or_name))
              link.source_type = source.type
              for target_field, source_field in link.field_map.items():
                if target_field != source_field:
                  try:
                    source.translation[target_field] = source.translation[
                        source_field]
                    source.translation[
                        target_field].std_field_name = target_field
                    del source.translation[source_field]
                  except KeyError:
                    translations_absent.append(
                        f'{link.source}.translation.{source_field}')

      print(f'{file_type} translations absent: ' +
            f'{len(set(translations_absent))} ' +
            f'(from {len(translations_absent)} links)')

      print(f'{file_type} types absent: {len(set(types_absent))} ' +
            f'({len(types_absent)} instances)')

  @staticmethod
  def match_reporting_entities(
      *,
      proposed_entities: DeserializedFile,
      solution_entities: DeserializedFile) -> List[CloudDeviceId]: # pylint: disable=line-too-long
    """
      Matches reporting entities by `cloud_device_id`

      Args:
        proposed_entities: Dictionary of proposed entity names
          and `EntityInstance`s
        solution_entities: Dictionary of solution entity names
          and `EntityInstance`s

      Returns:
        List of `cloud_device_id`s which have corresponding
        proposed and solution entities
    """
    matches = []
    for solution_entity in solution_entities.values():
      if solution_entity.cloud_device_id is None:
        continue  # as this is not a reporting device
      for proposed_entity in proposed_entities.values():
        if proposed_entity.cloud_device_id == solution_entity.cloud_device_id:
          matches.append(proposed_entity.cloud_device_id)

    return matches

  @staticmethod
  def retrieve_reporting_translations(
      *, matches: List[CloudDeviceId],
      proposed_entities: DeserializedFile,
      solution_entities: DeserializedFile
  ) -> TranslationsDict:
    """
      Retrieves proposed and solution translations
      for all matched reporting entities.

      Args:
        matches: List of `cloud_device_id`s which have corresponding
          proposed and solution entities
        proposed_entities: Dictionary of proposed entity names
          and `EntityInstance`s
        solution_entities: Dictionary of solution entity names
          and `EntityInstance`s

      Returns:
        Dictionary with `cloud_device_id`s as keys
        and lists of translation tuples as values
    """

    translations = {}
    for cloud_device_id in matches:
      # Find the entity via comparison of the cloud_device_id against the
      # corresponding property of each EntityInstance in the specified dict
      find_entity = lambda dictionary, cdid=cloud_device_id: [
          entity for entity in dictionary.values()
          if entity.cloud_device_id == cdid
      ][0]

      proposed_entity = find_entity(proposed_entities)
      solution_entity = find_entity(solution_entities)

      # Isolate the translations of an entity for pairing below.
      # A reporting entity without a translation should not occur
      aggregate_translations = lambda entity: list(entity.translation.items(
      )) if getattr(entity, 'translation', None) else []

      translations[cloud_device_id] = {
          f'{PROPOSED}_translations': aggregate_translations(proposed_entity),
          f'{SOLUTION}_translations': aggregate_translations(solution_entity)
      }

    return translations

  @staticmethod
  def aggregate_results_nondbo(
      *,
      dimensions: List[Dimension],
      translations: TranslationsDict) -> Dict[DimensionName, Dimension]: # pylint: disable=line-too-long
    """
      Wrapper which outputs a dictionary of results by invoking
      each specified `Dimension` with the `translations` argument

      Args:
        dimensions: List of `Dimension`s to be evaluated
        translations: Dictionary with `cloud_device_id`s as keys
          and lists of translation tuples as values

      Returns:
        Dictionary with dimension names as keys and `Dimension`s as values
    """
    results = {}
    for dimension in dimensions:
      # Invoke the function and append the dictionary with its return value
      results[dimension.__name__] = dimension(translations=translations)
    return results

  # TODO: update to reflect current combined signature of dimension
  @staticmethod
  def aggregate_results_dbo(
      *,
      dbo_dimensions: List[Dimension],
      proposed_entities: DeserializedFile,
      solution_entities: DeserializedFile) -> Dict[DimensionName, Dimension]: # pylint: disable=line-too-long
    """
      Wrapper which outputs a dictionary of results by invoking
      each specified `DboDimension` with the `proposed_entities`
      and `solution_entities` arguments

      Args:
        dbo_dimensions: List of `DboDimension`s to be evaluated
        proposed_entities: Dictionary of proposed entity names
          and `EntityInstance`s
        solution_entities: Dictionary of solution entity names
          and `EntityInstance`s

      Returns:
        Dictionary with dimension names as keys and `Dimension`s as values
    """
    results_dbo = {}
    for dbo_dimension in dbo_dimensions:
      # Invoke the function and append the dictionary with its return value
      results_dbo[dbo_dimension.__name__] = dbo_dimension(
          proposed_entities=proposed_entities,
          solution_entities=solution_entities)
    return results_dbo
