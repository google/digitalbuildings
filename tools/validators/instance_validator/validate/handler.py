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

"""Validation Helper"""

from __future__ import print_function
import argparse
import sys

from validate import entity_instance
from validate import generate_universe
from validate import instance_parser
from validate import subscriber

# Default timeout duration for telemetry validation test
from validate import telemetry_validator

DEFAULT_TIMEOUT = 600


def deserialize(yaml_file, universe):
  """Parses a yaml configuration file and deserialize it.
  Args:
    yaml_file: the building configuration file.
    universe: the generated ontology universe.
  :returns
    entity_instances: all the deserialized instances.
    parsed: the raw parsed entities
  """
  raw_parse = instance_parser.parse_yaml(yaml_file)
  print('Passed syntax checks!')
  print('Serializing Passed syntax checks!')
  parsed = dict(raw_parse)
  entity_instances = {}
  entity_names = list(parsed.keys())
  # first build all the entity instances
  for entity_name in entity_names:
    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              universe,
                                              set(entity_names))
    entity_instances[entity_name] = instance
  return entity_instances, parsed


class ValidationHelper(object):
  """A validation helper to coordinate the various steps of the validation."""

  def __init__(self, args):
    super().__init__()
    self._ParseArgs(args)

  def Validate(self):
    universe = self.GenerateUniverse(self.args.modified_types_filepath)
    entity_instances, parsed_entities = deserialize(self.filename, universe)
    self.ValidateEntities(entity_instances)
    self.StartTelemetryValidation(self.subscription, self.service_account,
                                  parsed_entities)

  def GenerateUniverse(self, modified_types_filepath=None):
    """Generates the universe from the ontology.
    Args:
     modified_types_filepath: the path to a modified ontology.
       If it is not set, the universe is generated from the default path.
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

  def ValidateEntities(self, entity_instances):
    """Validates entity instances that are already deserialized.
      Args:
        entity_instances: a list of entity instances.
    """
    print('Validating entities ...')
    building_found = False
    for entity_name, current_entity_instance in entity_instances.items():
      if not current_entity_instance.IsValidEntityInstance(entity_instances):
        print(entity_name, 'is not a valid instance')
        sys.exit(0)
      if current_entity_instance.type_name.lower() == 'building':
        building_found = True

    if not building_found:
      print('Building Config must contain an entity with a building type')
      raise SyntaxError('Building Config must contain an '
                        'entity with a building type')
    print('Entities Validated !')


  def StartTelemetryValidation(self, subscription, service_account_file,
                               parsed_entities):
    """Validates telemetry payload received from the subscription.
     Args:
       subscription: a pubsub subscription.
       service_account_file: a GCP service account file.
       parsed_entities: dictionary of raw entities
    """
    if self.pubsub_validation_set:
      print('Connecting to pubsub subscription: ', subscription)
      sub = subscriber.Subscriber(subscription, service_account_file)
      validator = telemetry_validator.TelemetryValidator(
          parsed_entities, self.timeout, self.TelemetryValidationCallback)
      validator.StartTimer()
      sub.Listen(validator.ValidateMessage)


  def TelemetryValidationCallback(self, validator):
    """Callback when the telemetry validator finishes.

    This could be called due to a timeout or because telemetry messages were
    received and validated for every expected entity.

    Args:
      validator: the telemetry validator that triggered the callback."""

    report = ''

    if not validator.AllEntitiesValidated():
      report += 'No telemetry message was received for the following entities:'
      report += '\n'
      for entity_name in validator.GetUnvalidatedEntities():
        report += '  ' + entity_name + '\n'

    report += '\nTelemetry validation errors:\n'
    for error in validator.GetErrors():
      report += error.GetPrintableMessage()

    if self.report_filename:
      f = open(self.report_filename, 'w')
      f.write(report)
      f.close()
    else:
      print('\n')
      print(report)

    sys.exit(0)


  def _ParseArgs(self, args):
    """Prepares the arguments for the user input."""
    parser = argparse.ArgumentParser(
        description='Validate a YAML building configuration file')

    parser.add_argument(
        '-i', '--input',
        dest='filename',
        required=True,
        help='Filepath to YAML building configuration',
        metavar='FILE')

    parser.add_argument(
        '-m', '--modified-ontology-types',
        dest='modified_types_filepath',
        required=False,
        help='Filepath to modified type filepaths',
        metavar='MODIFIED_TYPE_FILEPATHS')

    parser.add_argument(
        '-s', '--subscription',
        dest='subscription',
        required=False,
        help='Pubsub subscription for telemetry to validate',
        metavar='subscription')

    parser.add_argument(
        '-a', '--service-account',
        dest='service_account',
        required=False,
        help='Service account used to pull messages from the subscription',
        metavar='service-account')

    parser.add_argument(
        '-t', '--timeout',
        dest='timeout',
        required=False,
        default=DEFAULT_TIMEOUT,
        help='Timeout duration (in seconds) for telemetry validation test',
        metavar='timeout')

    parser.add_argument(
        '-r', '--report-filename',
        dest = 'report_filename',
        required = False,
        default = None,
        help = 'Filename for the validation report',
        metavar = 'report-filename')

    self.args = parser.parse_args(args)
    self.filename = self.args.filename

    self.subscription = self.args.subscription
    self.service_account = self.args.service_account
    self.timeout = self.args.timeout
    self.report_filename = self.args.report_filename

    self.pubsub_validation_set = False
    if self.subscription is not None and self.args.service_account is not None:
      self.pubsub_validation_set = True
    elif self.args.subscription is None and self.args.service_account is None:
      self.pubsub_validation_set = False
    else:
      print(
          'Subscription and a service account file are '
          'both needed for the telemetry validation!')
      sys.exit(0)
