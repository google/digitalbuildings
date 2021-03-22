"""Constants for the ontology validator application tests."""
from os import path

from ontology_validator.yamlformat import constants

ONTOLOGY_ROOT = constants.ONTOLOGY_ROOT
TEST_ROOT = path.join(constants.APPLICATION_ROOT, 'tests')
TEST_RESOURCES = path.join(TEST_ROOT, 'fake_resources')
