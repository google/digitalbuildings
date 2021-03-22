"""Constants for the ontology validator application."""

from os import path

# TODO(b/183433133):move to one constants file after refactoring.
REPO_ROOT = path.join(path.dirname(path.realpath(__file__)), '..', '..', '..', '..')
APPLICATION_ROOT = path.join(REPO_ROOT, 'tools', 'validators',
                             'ontology_validator', 'yamlformat')
ONTOLOGY_ROOT = path.join(REPO_ROOT, 'ontology', 'yaml', 'resources')
