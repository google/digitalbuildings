"""Constants for the types guid generator application tests."""

from os import path

# internally, absolute path is used; github uses relative path
_USE_ABSOLUTE_PATH = False

if _USE_ABSOLUTE_PATH:
  REPO_ROOT = path.join('third_party', 'digitalbuildings')
else:
  REPO_ROOT = path.join(
      path.dirname(path.realpath(__file__)),
      path.join('..', '..', '..', '..', '..'),
  )

TEST_INSTANCES = path.join(
    REPO_ROOT,
    'tools',
    'guid_generator',
    'ontology',
    'types_guid_generator',
    'tests',
    'test_data',
)
