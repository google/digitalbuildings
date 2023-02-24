"""Constants for the guid generator application tests."""
from os import path

from instance_guid_generator import constants

GUID_GENERATOR_ROOT = path.join(
    constants.REPO_ROOT, 'tools', 'guid_generator', 'instance')
TEST_ROOT = path.join(constants.APPLICATION_ROOT, 'tests')
TEST_INSTANCES = path.join(TEST_ROOT, 'fake_instances')
