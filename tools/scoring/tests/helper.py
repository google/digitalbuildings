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
"""Utilities for testing."""

from score.constants import FileTypes, DimensionCategories
from score.parse_config import ParseConfig

from validate import handler as validator
from validate.generate_universe import BuildUniverse

PROPOSED, SOLUTION = FileTypes
SIMPLE, COMPLEX = DimensionCategories

# TODO: Test scorer with new config file format (where primary key is guid)
# https://trello.com/c/rw6o4HVa/34-test-scorer-with-new-config-file-format-where-primary-key-is-guid


class TestHelper:
  """Utilities for testing."""
  @staticmethod
  def prepare_dimension_argument(*, dimension_type, proposed_path,
                                 solution_path):
    """Prepare argument for direct invocation of a dimension for purposes of
      testing (i.e. mimic parse_config.py).

      NOTE: this uses the simplified universe. If the test data references types
      which are not contained therein, results will differ from those which use
      the full universe because entities with missing types are skipped!

        Arguments:
          dimension_type: the category of the dimension. (Literal[SIMPLE, COMPLEX])
          proposed_path: the path to the proposed YAML file
          solution_path: the path to the solution YAML file

        Returns:
          The appropriate value for the dimension's singular named argument"""

    universe = BuildUniverse(use_simplified_universe=True)
    proposed_config = validator.Deserialize([proposed_path])[0]
    solution_config = validator.Deserialize([solution_path])[0]
    deserialized_files = {PROPOSED: proposed_config, SOLUTION: solution_config}

    deserialized_files_appended = ParseConfig.append_types(
        universe=universe, deserialized_files=deserialized_files)

    if dimension_type == SIMPLE:
      matches = ParseConfig.match_reporting_entities(
          proposed_entities=deserialized_files_appended[PROPOSED],
          solution_entities=deserialized_files_appended[SOLUTION])

      translations = ParseConfig.retrieve_reporting_translations(
          matches=matches,
          proposed_entities=deserialized_files_appended[PROPOSED],
          solution_entities=deserialized_files_appended[SOLUTION])

      return translations
    elif dimension_type == COMPLEX:
      return deserialized_files_appended
