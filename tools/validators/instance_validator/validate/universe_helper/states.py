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

"""Sets up a minimal state universe required for testing."""

from yamlformat.validator import state_lib

STATE_FOLDER = state_lib.StateFolder(folderpath='states')
STATE_UNIVERSE = state_lib.StateUniverse(folders=[STATE_FOLDER])

STATE_FOLDER.AddFromConfig(
    config_filename='states/states.yaml',
    documents=[{
        'ON': 'foobar',
        'OFF': 'foobar',
        'AUTO': 'foobar',
        'MANUAL': 'foobar',
        'OPEN': 'foobar',
        'CLOSED': 'foobar',
        'LOW': 'foobar',
        'MEDIUM': 'foobar',
        'HIGH': 'foobar',
        'OCCUPIED': 'foobar',
        'UNOCCUPIED': 'foobar',
        'COMMISSIONING': 'foobar',
        'FLUSHING': 'foobar',
        'HEATING': 'foobar',
        'COOLING': 'foobar',
        'NEUTRAL': 'foobar',
        'ACCESS_FAILED': 'foobar',
        'ACTIVE': 'foobar',
        'CALENDAR_STARTUP': 'foobar',
        'CALENDAR_SUCCESS': 'foobar',
        'DISABLED': 'foobar',
        'DOES_NOT_MATCH': 'foobar',
        'ENABLED': 'foobar',
        'INACTIVE': 'foobar',
        'MATCHES': 'foobar',
        'SUBSCRIPTION_FAILED': 'foobar',
        'UNKNOWN': 'foobar',
        'WAITING_FOR_RESPONSE': 'foobar',
        'PRESENT': 'foobar',
        'ABSENT': 'foobar',
        'CHARGING': 'foobar',
        'DISCHARGING': 'foobar',
        'STANDBY': 'foobar',
        'REMOTE': 'foobar',
        'LOCAL': 'foobar',
    }])
