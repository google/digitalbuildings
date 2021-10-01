
"""Constants for the ontology explorer application."""

from os import path

JOINS = path.join('..', '..', '..', '..')
REPO_ROOT = path.join(path.dirname(path.realpath(__file__)), JOINS)
APPLICATION_ROOT = path.join(REPO_ROOT, 'tools', 'validators',
                             'ontology_validator', 'yamlformat')
ONTOLOGY_ROOT = path.join(REPO_ROOT, 'ontology', 'yaml', 'resources')
