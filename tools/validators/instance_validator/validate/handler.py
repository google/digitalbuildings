# Copyright 2020 Google LLC
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
"""Validation Helper."""

from __future__ import print_function

import argparse
import sys

from validate import entity_instance
from validate import generate_universe
from validate import instance_parser
from validate import subscriber
from validate import telemetry_validator
from datetime import datetime
from typing import Dict


# Default timeout duration for telemetry validation test
DEFAULT_TIMEOUT = 600


def deserialize(yaml_files: str) -> Dict[str, entity_instance.EntityInstance]:
  """Parses a yaml configuration file and deserialize it.

  Args:
    yaml_files: list of building configuration file.

  Returns:
    A map of entity name to Entity instance.
  """

  parsed_yaml = {}
  print('Validating syntax please wait ...')
  parser = instance_parser.InstanceParser()
  for yaml_file in yaml_files:
    print('Opening file: {0}, please wait ...'.format(yaml_file))
    parser.AddFile(yaml_file)
  parser.Finalize()

  entities = {}
  for entity_name, entity_yaml in parser.GetEntities().items():
    entities[entity_name] = entity_instance.EntityInstance(entity_yaml)

  return entities


class ValidationHelper(object):
  """A validation helper to coordinate the various steps of the validation."""

  def __init__(self, args):
    super().__init__()
    self._ParseArgs(args)

  def Validate(self):
    universe = self.GenerateUniverse(self.args.modified_types_filepath)
    entity_instances = deserialize(self.filenames)
    self.ValidateEntities(universe, entity_instances)
    self.StartTelemetryValidation(self.subscription, self.service_account,
                                  entity_instances)

  def GenerateUniverse(self, modified_types_filepath=None):
    """Generates the universe from the ontology.

    Args:
     modified_types_filepath: the path to a modified ontology. If it is not set,
       the universe is generated from the default path.
    """
    # SYNTAX VALIDATION
    print('\nValidator starting ...\n')
    # prints for syntax errors and exits gracefully

    print('Generating universe ...')
    universe = generate_universe.BuildUniverse(modified_types_filepath)
    if universe is None:
      print('\nError generating universe')
      sys.exit(0)

    print('Universe generated successfully')
    return universe

  def ValidateEntities(self, universe, entity_instances):
    """Validates entity instances that are already deserialized.

      Args:
        universe: ConfigUniverse representing the ontology
        entity_instances: a list of entity instances.
    """
    print('Validating entities ...')
    building_found = False
    for entity_name, current_entity_instance in entity_instances.items():
      if not current_entity_instance.IsValidEntityInstance(
          universe, entity_instances):
        print(entity_name, 'is not a valid instance')
        sys.exit(0)
      if current_entity_instance.type_name.lower() == 'building':
        building_found = True

    if not building_found:
      print('Building Config must contain an entity with a building type')
      raise SyntaxError('Building Config must contain an '
                        'entity with a building type')
    print('All entities validated')

  def StartTelemetryValidation(self, subscription, service_account_file,
                               entity_instances):
    """Validates telemetry payload received from the subscription.

     Args:
       subscription: a pubsub subscription.
       service_account_file: a GCP service account file.
       entity_instances: EntityInstance dictionary
    """
    if self.pubsub_validation_set:
      print('Connecting to pubsub subscription: ', subscription)
      sub = subscriber.Subscriber(subscription, service_account_file)
      validator = telemetry_validator.TelemetryValidator(
          entity_instances, self.timeout, self.TelemetryValidationCallback)
      validator.StartTimer()
      sub.Listen(validator.ValidateMessage)

  def TelemetryValidationCallback(self, validator):
    """Callback when the telemetry validator finishes.

    This could be called due to a timeout or because telemetry messages were
    received and validated for every expected entity.

    Args:
      validator: the telemetry validator that triggered the callback.
    """

    print('Generating validation report ...')
    current_time = datetime.now()
    timestamp = current_time.strftime('%d-%b-%Y (%H:%M:%S)')
    report = '\nReport Generated at: {0}\n'.format(timestamp)

    if not validator.AllEntitiesValidated():
      report += 'No telemetry message was received for the following entities:'
      report += '\n'
      for entity_name in validator.GetUnvalidatedEntityNames():
        report += '  {0}\n'.format(entity_name)

    report += '\nTelemetry validation errors:\n'
    for error in validator.GetErrors():
      report += error.GetPrintableMessage()

    report += '\nTelemetry validation warnings:\n'
    for warnings in validator.GetWarnings():
      report += warnings.GetPrintableMessage()

    if self.report_filename:
      f = open(self.report_filename, 'w')
      f.write(report)
      f.close()
    else:
      print('\n')
      print(report)
    print('Report Generated')
    sys.exit(0)

  def _ParseArgs(self, args):
    """Prepares the arguments for the user input."""
    parser = argparse.ArgumentParser(
        description='Validate a YAML building configuration file')

    parser.add_argument(
        '-i',
        '--input',
        action='append',
        dest='filenames',
        required=True,
        help='Filepaths to YAML building configurations',
        metavar='FILE')

    parser.add_argument(
        '-m',
        '--modified-ontology-types',
        dest='modified_types_filepath',
        required=False,
        help='Filepath to modified type filepaths',
        metavar='MODIFIED_TYPE_FILEPATHS')

    parser.add_argument(
        '-s',
        '--subscription',
        dest='subscription',
        required=False,
        help='Pubsub subscription for telemetry to validate',
        metavar='subscription')

    parser.add_argument(
        '-a',
        '--service-account',
        dest='service_account',
        required=False,
        help='Service account used to pull messages from the subscription',
        metavar='service-account')

    parser.add_argument(
        '-t',
        '--timeout',
        dest='timeout',
        required=False,
        default=DEFAULT_TIMEOUT,
        help='Timeout duration (in seconds) for telemetry validation test',
        metavar='timeout')

    parser.add_argument(
        '-r',
        '--report-filename',
        dest='report_filename',
        required=False,
        default=None,
        help='Filename for the validation report',
        metavar='report-filename')

    self.args = parser.parse_args(args)
    self.filenames = self.args.filenames

    self.subscription = self.args.subscription
    self.service_account = self.args.service_account
    self.timeout = int(self.args.timeout)
    self.report_filename = self.args.report_filename

    self.pubsub_validation_set = False
    if self.subscription is not None and self.args.service_account is not None:
      self.pubsub_validation_set = True
    elif self.args.subscription is None and self.args.service_account is None:
      self.pubsub_validation_set = False
    else:
      print('Subscription and a service account file are '
            'both needed for the telemetry validation!')
      sys.exit(0)
