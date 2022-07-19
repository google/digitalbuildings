"""Constants for the guid generator application tests."""
from os import path

from google3.third_party.digitalbuildings.tools.validators.instance_validator.validate import constants

GUID_GENERATOR_ROOT = path.join(constants.REPO_ROOT, 'tools', 'guid_generator')
TEST_ROOT = path.join(GUID_GENERATOR_ROOT, 'tests')
TEST_INSTANCES = path.join(TEST_ROOT, 'fake_instances')
