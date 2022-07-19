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
"""Sets up a minimal connection universe required for testing."""

from google3.third_party.digitalbuildings.tools.validators.ontology_validator.yamlformat.validator import connection_lib

CONNECTION_FOLDER = connection_lib.ConnectionFolder(folderpath='connections')
CONNECTION_UNIVERSE = connection_lib.ConnectionUniverse(
    folders=[CONNECTION_FOLDER])

CONNECTION_FOLDER.AddFromConfig(
    documents=[{
        'CONTAINS': {
            'description': 'foobar',
        },
        'CONTROLS': {
            'description': 'foobar',
        },
        'FEEDS': {
            'description': 'foobar',
        },
        'HAS_PART': {
            'description': 'foobar',
        },
        'HAS_RANGE': {
            'description': 'foobar',
        },
    }],
    config_filename='connections/connections.yaml')
