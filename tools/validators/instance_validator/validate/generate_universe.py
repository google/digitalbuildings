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

from __future__ import print_function
from __future__ import absolute_import

from os import path

from yamlformat.validator import external_file_lib
from yamlformat.validator import presubmit_validate_types_lib
from yamlformat.validator import namespace_validator

def BuildUniverse(modified_types_filepath=None):
  """Generates the ontology universe.

  Args:
    modified_types_filepath: filepath to the modified ontology types

  Returns:
    Generated universe object.
  """

  if modified_types_filepath:
    modified_ontology_exists = path.exists(modified_types_filepath)
    if not modified_ontology_exists:
      print('Specified filepath for modified ontology does not exist')
      return None

    modified_types_filepath = path.expanduser(modified_types_filepath)

    external_file_lib.Validate(filter_text=None,
                               changed_directory=modified_types_filepath,
                               original_directory=path.join('..',
                                                            '..',
                                                            '..',
                                                            'ontology',
                                                            'yaml',
                                                            'resources'),
                               interactive=False)
    yaml_files = external_file_lib.RecursiveDirWalk(modified_types_filepath)
  else:
    # use default location for ontology files
    yaml_files = external_file_lib.RecursiveDirWalk(path.join(
        '..', '..', '..', 'ontology', 'yaml', 'resources'))

  config = presubmit_validate_types_lib.SeparateConfigFiles(yaml_files)
  universe = presubmit_validate_types_lib.BuildUniverse(config)

  namespace_validation = namespace_validator.NamespaceValidator(
      universe.GetEntityTypeNamespaces())

  if not namespace_validation.IsValid():
    print('Universe is not valid')
    return None

  return universe
