# Copyright 2021 Google LLC
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

"""Constants for the instance validator application."""

from os import path

# internally, absolute path is used; github uses relative path
_USE_ABSOLUTE_PATH = False

if _USE_ABSOLUTE_PATH:
  REPO_ROOT = path.join('third_party', 'digitalbuildings')
else:
  REPO_ROOT = path.join(
      path.dirname(path.realpath(__file__)), path.join('..', '..', '..', '..')
  )

APPLICATION_ROOT = path.join(
    REPO_ROOT, 'tools', 'validators', 'instance_validator'
)
ONTOLOGY_ROOT = path.join(REPO_ROOT, 'ontology', 'yaml', 'resources')

# Default timeout duration for telemetry validation test
DEFAULT_TIMEOUT = 600

# Telemetry validation constants
TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
TELEMETRY_TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

# Report-level constants
REPORT_TIMESTAMP = 'updated'
EXTRA_DEVICES = 'extra_devices'
MISSING_DEVICES = 'missing_devices'
EXPECTED_DEVICES = 'expected_devices'
ERROR_DEVICES = 'errorDevices'

# Device-level constants
MESSAGE_TIMESTAMP = 'timestamp'
ENTITY_GUID = 'guid'
MISSING_VERSION = 'no_version'
MISSING_TIMESTAMP = 'no_timestamp'
TELEMETRY_MESSAGE_ERRORS = 'telemetryMessageErrors'
TELEMETRY_MESSAGE_WARNINGS = 'telemetryMessageWarnings'
ENTITY_CODE = 'entityCode'
MESSAGE_VERSION = 'version'
PRESENT_VALUE_KEY = 'present_value'
EXPECTED_POINTS = 'expectedPoints'
EXTRA_POINTS = 'extraPoints'
MISSING_POINTS = 'missingPoints'
UNMAPPED_STATES = 'unmapped_states'
MISSING_PRESENT_VALUES = 'missing_present_values'
INVALID_DIMENSIONAL_VALUES = 'invalid_dimensional_values'
ERRORS_INCONSISTENT = 'content inconsistent between messages'
EXTRA_POINTS_INCONSISTENT = 'extra points inconsistent between messages'
MISSING_POINTS_INCONSISTENT = 'missing points inconsistent between messages'
MESSAGE_DESCRIPTION = 'description'
