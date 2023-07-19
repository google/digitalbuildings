# Copyright 202i Google LLC
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
"""Main module for DBO explorer."""
from lib import constants
from lib.ontology_wrapper import OntologyWrapper

from yamlformat.validator import external_file_lib
from yamlformat.validator import namespace_validator as nv
from yamlformat.validator import presubmit_validate_types_lib


def Build(ontology_path: str) -> OntologyWrapper:
  """A constructor for the ontology explorer.

  Args:
    ontology_path: A path for an alternative ontology extended from DBO.

  Returns:
    ontology: An instance of the OntologyWrapper class.
  """
  if ontology_path is not None:
    yaml_file_path = ontology_path
  else:
    yaml_file_path = constants.ONTOLOGY_ROOT
  yaml_files = external_file_lib.RecursiveDirWalk(yaml_file_path)
  config = presubmit_validate_types_lib.SeparateConfigFiles(yaml_files)
  universe = presubmit_validate_types_lib.BuildUniverse(config)
  nv.NamespaceValidator(universe.GetEntityTypeNamespaces())
  ontology = OntologyWrapper(universe)
  return ontology
