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

from typing import Dict, Optional, List, Any

from validate import handler as validator
from validate.generate_universe import BuildUniverse
from yamlformat.validator.presubmit_validate_types_lib import ConfigUniverse

from score.dimensions.dimension import Dimension
from score.scorer_types import DimensionName, TranslationsDict, DeserializedFile, DeserializedFilesDict
from score.constants import FileTypes, DimensionCategories
from score.dimensions import entity_connection_identification, entity_identification, entity_point_identification, entity_type_identification, raw_field_selection, standard_field_naming, state_mapping, unit_mapping

PROPOSED, SOLUTION = FileTypes
SIMPLE, COMPLEX = DimensionCategories


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
    print('Scoring — building universe')
    self.universe = BuildUniverse(modified_types_filepath=ontology)
    print('Scoring — deserializing files')
    self.deserialized_files = {
        PROPOSED: validator.Deserialize([proposed])[0],
        SOLUTION: validator.Deserialize([solution])[0]
    }
    self.results = {}

  @staticmethod
  def append_types(
      *, universe: ConfigUniverse,
      deserialized_files: DeserializedFilesDict) -> DeserializedFilesDict:
    """
      Appends types to deserialized files for purposes
      of filtering entities and for evaluating "complex" dimensions.

      Args:
        universe: The ontology universe to reference
        deserialized_files: Dictionary with deserialized configuration files
          keyed under their respective file type ("proposed" or "solution").

      Returns:
        The deserialized files dictionary with types
        appended to each entity in the respective files.
    """
    print('Scoring — appending entity types')
    for file_type, file in deserialized_files.items():
      translations_absent = []
      types_absent = []
      type_or_name = 'type' if file_type == SOLUTION else 'type_name'

      for entity in file.values():
        entity.type = universe.GetEntityType(entity.namespace, entity.type_name)

        if entity.type is None:
          types_absent.append(getattr(entity, type_or_name))
        if entity.links is not None:
          for link in entity.links:
            source = file[link.source] if link.source in file else None
            if source:
              if not getattr(source, 'type', None):
                source.type = universe.GetEntityType(source.namespace,
                                                     source.type_name)
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

      print(f'    {file_type} translations absent: ' +
            f'{len(set(translations_absent))} ' +
            f'(from {len(translations_absent)} links)')

      print(f'    {file_type} types absent: {len(set(types_absent))} ' +
            f'({len(types_absent)} instances)')

    return deserialized_files

  @staticmethod
  def retrieve_reporting_translations(
      *, proposed_entities: DeserializedFile,
      solution_entities: DeserializedFile) -> TranslationsDict:
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
        and values which are dictionaries containing lists
        of translations for the device, keyed under the file type
    """

    translations = {}
    for solution_entity in solution_entities.values():
      if solution_entity.cloud_device_id is None:
        continue  # as this is not a reporting device
      if not Dimension.is_entity_canonical(solution_entity):
        continue  # as noncanonical entities are skipped

      cloud_device_id = solution_entity.cloud_device_id

      def find_matches(cdid: str) -> List[Any]:
        """Find the matching proposal via cloud_device_id comparison.

        Args:
          cdid: cloud device id string.

        Returns:
          List of matching entities.
        """
        matches = [
            proposed_entity for proposed_entity in proposed_entities.values()
            if proposed_entity.cloud_device_id == cdid]
        return matches

      proposed_entity = find_matches(cloud_device_id)[0] if find_matches(
          cloud_device_id) else {}

      def aggregate_translations(entity) -> List[Any]:
        """Isolate translation of an entity pairing."""
        if getattr(entity, 'translation', None):
          return list(entity.translation.items())
        return []

      translations[cloud_device_id] = {
          f'{PROPOSED}': aggregate_translations(proposed_entity),
          f'{SOLUTION}': aggregate_translations(solution_entity)
      }

    return translations

  @staticmethod
  def aggregate_results(
      *, dimensions: List[Dimension], translations: TranslationsDict,
      deserialized_files: DeserializedFilesDict
  ) -> Dict[DimensionName, Dimension]:
    """
      Wrapper which outputs a dictionary of results by invoking each
      specified `Dimension` with the appropriate argument based on its category

      Args:
        dimensions: List of `Dimension`s to be evaluated
        translations: Dictionary with `cloud_device_id`s as keys
          and lists of translation tuples as values. Used as argument for
          "simple" dimensions.
        deserialized_files: Dictionary with deserialized configuration files
          keyed under their respective file type ("proposed" or "solution").
          Used as argument for "complex" dimensions.

      Returns:
        Dictionary with dimension names as keys and `Dimension`s as values
    """
    results = {}

    for dimension in dimensions:
      # Invoke the functions and append the dictionary with their return values
      if dimension.category == SIMPLE:
        evaluated = dimension(translations=translations).evaluate()
      elif dimension.category == COMPLEX:
        evaluated = dimension(deserialized_files=deserialized_files).evaluate()

      results[dimension.__name__] = evaluated
    return results

  def execute(self) -> Dict[DimensionName, str]:
    """
      Wrapper for all functionality herein.

      Returns:
        Dictionary containing human-readable
        represenation of every scored dimension.
    """
    deserialized_files_appended = self.append_types(
        universe=self.universe, deserialized_files=self.deserialized_files)

    translations = self.retrieve_reporting_translations(
        proposed_entities=deserialized_files_appended[PROPOSED],
        solution_entities=deserialized_files_appended[SOLUTION])

    dimensions = [
        raw_field_selection.RawFieldSelection,
        standard_field_naming.StandardFieldNaming, state_mapping.StateMapping,
        unit_mapping.UnitMapping,
        entity_connection_identification.EntityConnectionIdentification,
        entity_identification.EntityIdentification,
        entity_point_identification.EntityPointIdentification,
        entity_type_identification.EntityTypeIdentification
    ]

    self.results = self.aggregate_results(
        dimensions=dimensions,
        translations=translations,
        deserialized_files=deserialized_files_appended)

    readable = {
        name: str(dimension)
        for name, dimension in self.results.items()
    }

    return readable
