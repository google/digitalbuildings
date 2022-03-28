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

from typing import Dict, List, Optional

from score.constants import DimensionCategories
from score.constants import FileTypes
from score.dimensions.dimension import Dimension
from score.types_ import CloudDeviceId
from score.types_ import DeserializedFile
from score.types_ import DeserializedFilesDict
from score.types_ import DimensionCategory
from score.types_ import DimensionName
from score.types_ import TranslationsDict

from validate import handler as validator
from validate.generate_universe import BuildUniverse

PROPOSED, SOLUTION = FileTypes
SIMPLE, COMPLEX = DimensionCategories


class ParseConfig:
  """Parse config.

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
    """Init.

    Args:
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

  # TODO(b/210741084): refactor into smaller functions and return
  def append_types(self):
    """Appends types to deserialized files."""
    for file_type, file in self.deserialized_files.items():
      translations_absent = []
      types_absent = []
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
      *, proposed_entities: DeserializedFile,
      solution_entities: DeserializedFile) -> List[CloudDeviceId]:
    """Matches reporting entities by `cloud_device_id`.

    Args:
      proposed_entities: Dictionary of proposed entity names and
        `EntityInstance`s
      solution_entities: Dictionary of solution entity names and
        `EntityInstance`s

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
      *, matches: List[CloudDeviceId], proposed_entities: DeserializedFile,
      solution_entities: DeserializedFile) -> TranslationsDict:
    """Retrieves proposed and solution translations for all matched reporting entities.

    Args:
      matches: List of `cloud_device_id`s which have corresponding proposed and
        solution entities
      proposed_entities: Dictionary of proposed entity names and
        `EntityInstance`s
      solution_entities: Dictionary of solution entity names and
        `EntityInstance`s

    Returns:
      Dictionary with `cloud_device_id`s as keys
      and lists of translation tuples as values
    """

    translations = {}
    for cloud_device_id in matches:
      # Find the entity via comparison of the cloud_device_id against the
      # corresponding property of each EntityInstance in the specified dict
      proposed_entity = find_entity(proposed_entities, cloud_device_id)
      solution_entity = find_entity(solution_entities, cloud_device_id)

      # Isolate the translations of an entity for pairing below.
      # A reporting entity without a translation should not occur
      translations[cloud_device_id] = {
          f'{PROPOSED}_translations': aggregate_translations(proposed_entity),
          f'{SOLUTION}_translations': aggregate_translations(solution_entity)
      }

    return translations

  @staticmethod
  def aggregate_results(
      *, dimensions: Dict[DimensionCategory, List[Dimension]],
      translations: TranslationsDict, deserialized_files: DeserializedFilesDict
  ) -> Dict[DimensionName, Dimension]:
    """Wrapper which outputs a dictionary of results by invoking each specified.

    `Dimension` with the appropriate argument based on its category
    dbo_dimensions: List of `DboDimension`s to be evaluated
    proposed_entities: Dictionary of proposed entity names
      and `EntityInstance`s
    solution_entities: Dictionary of solution entity names
      and `EntityInstance`s

    Args:
      dimensions: Dictionary with lists of `Dimension`s to be evaluated keyed
        under their category ("simple" or "complex")
      translations: Dictionary with `cloud_device_id`s as keys and lists of
        translation tuples as values. Used as argument for "simple" dimensions.
      deserialized_files: Dictionary with deserialized configuration files keyed
        under their respective file type ("proposed" or "solution"). Used as
        argument for "complex" dimensions.

    Returns:
      Dictionary with dimension names as keys and `Dimension`s as values
    """
    results = {}

    for dimension_category, dimension_list in dimensions.items():
      # Invoke the functions and append the dictionary with their return values
      for dimension in dimension_list:
        if dimension_category == SIMPLE:
          invoked = dimension(translations=translations)
        elif dimension_category == COMPLEX:
          invoked = dimension(deserialized_files=deserialized_files)

        results[dimension.__name__] = invoked
    return results


def find_entity(dictionary, cloud_device_id):
  return [
      entity for entity in dictionary.values()
      if entity.cloud_device_id == cloud_device_id
  ][0]


def aggregate_translations(entity):
  return list(entity.translation.items()) if getattr(entity, 'translation',
                                                     None) else []
