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

from typing import Optional

from validate import handler as validator
from validate.generate_universe import BuildUniverse


class ParseConfig:
  """
    Attributes:
      args: Dictionary containing instance arguments
      universe: Built from the input ontology
      parsed: Deserialized configuration files
      scores: Dictionary containing scores for output

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
        proposed: Path to the config to be scored
        verbose: Print specifics of missing types and translations (optional)
    """
    self.args = {
        'ontology': ontology,
        'solution': solution,
        'proposed': proposed,
        'verbose': verbose
    }
    self.universe = BuildUniverse(modified_types_filepath=ontology)
    self.parsed = {
        'proposed': validator.Deserialize([proposed])[0],
        'solution': validator.Deserialize([solution])[0]
    }
    self.scores = {}

  # TODO: refactor into smaller functions and return instead of printing
  def append_types(self):
    """
      Appends types or type names to parsed files
    """
    for file_type, file in self.parsed.items():
      translations_absent = []
      types_absent = []
      # TODO: This appends the full type to solution entities and only
      # the type name to proposed entities. Verify that this is the correct
      # behavior following implementation of the first dimension(s).
      type_or_name = 'type' if file_type == 'solution' else 'type_name'

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
