# Copyright 2020 Google LLC
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
"""Generates the ontology universe for the instance validator."""

from __future__ import absolute_import
from __future__ import print_function

from os import path

from google3.third_party.digitalbuildings.tools.validators.instance_validator.validate import constants
from google3.third_party.digitalbuildings.tools.validators.instance_validator.validate import universe_helper
from google3.third_party.digitalbuildings.tools.validators.ontology_validator.yamlformat.validator import external_file_lib
from google3.third_party.digitalbuildings.tools.validators.ontology_validator.yamlformat.validator import namespace_validator
from google3.third_party.digitalbuildings.tools.validators.ontology_validator.yamlformat.validator import presubmit_validate_types_lib


def BuildUniverse(
    use_simplified_universe: bool = False,
    modified_types_filepath: str = None,
) -> presubmit_validate_types_lib.ConfigUniverse:
  """Generates the ontology universe.

  Args:
    use_simplified_universe: boolean to quick load minimal universe instead of
      full ontology
    modified_types_filepath: filepath to the modified ontology types

  Returns:
    Generated universe object.
  """
  if use_simplified_universe:
    yaml_files = None
    universe = universe_helper.create_simplified_universe()
  elif modified_types_filepath:
    modified_ontology_exists = path.exists(modified_types_filepath)
    if not modified_ontology_exists:
      print(f'Specified filepath [{modified_types_filepath}] '
            'modified ontology does not exist')
      return None

    modified_types_filepath = path.expanduser(modified_types_filepath)

    external_file_lib.Validate(
        filter_text=None,
        changed_directory=modified_types_filepath,
        original_directory=constants.ONTOLOGY_ROOT,
        interactive=False)
    yaml_files = external_file_lib.RecursiveDirWalk(modified_types_filepath)
  else:
    default_ontology_exists = path.exists(constants.ONTOLOGY_ROOT)
    if not default_ontology_exists:
      print(f'Specified filepath [{constants.ONTOLOGY_ROOT}] '
            'for default ontology does not exist')
      return None
    # use default location for ontology files
    yaml_files = external_file_lib.RecursiveDirWalk(constants.ONTOLOGY_ROOT)

  if yaml_files:
    config = presubmit_validate_types_lib.SeparateConfigFiles(yaml_files)
    universe = presubmit_validate_types_lib.BuildUniverse(config)

  namespace_validation = namespace_validator.NamespaceValidator(
      universe.GetEntityTypeNamespaces())

  if not namespace_validation.IsValid():
    print('Universe is not valid')
    return None

  return universe
