"""Main module for DBO explorer."""
from yamlformat.validator import external_file_lib
from yamlformat.validator import presubmit_validate_types_lib
from yamlformat.validator import namespace_validator as nv

from lib.ontology_wrapper import OntologyWrapper
from lib import constants

def Build(ontology_path: str):
  """
  A constructor for the ontology explorer.

  Args:
    ontology_path: A path for an alternative ontology extended from DBO.

  returns:
    An instance of the OntologyWrapper class.
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

