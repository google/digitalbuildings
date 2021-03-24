"""Constants for the instance validator application tests."""
from os import path

from validate import constants

ONTOLOGY_ROOT = constants.ONTOLOGY_ROOT
TEST_ROOT = path.join(constants.APPLICATION_ROOT, 'tests')
TEST_INSTANCES = path.join(TEST_ROOT, 'fake_instances')
TEST_RESOURCES = path.join(TEST_ROOT, 'fake_resources')
TEST_TELEMETRY = path.join(TEST_ROOT, 'fake_telemetry')

