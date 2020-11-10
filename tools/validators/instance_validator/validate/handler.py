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
from validate import telemetry


def message_handler(message):
  """Handles a pubsub message.
    Args:
      message: a pubsub message containing telemetry payload.
  """
  t = telemetry.Telemetry(message)
  for key, value in t.points.items():
    print()
    print('-point: ', key)
    print('-- point_name: ', value.point_name)
    print('-- present_value: ', value.present_value)
  message.ack()


def deserialize(yaml_file, universe):
  """Parses a yaml configuration file and deserialize it.
  Args:
    yaml_file: the building configuration file.
    universe: the generated ontology universe.
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
  return entity_instances


class ValidationHelper(object):
  """A validation helper to coordiante the various steps of the validation."""

  def __init__(self):
    super().__init__()
    self._PrepareArgs()

  def Validate(self):
    universe = self.GenerateUniverse(self.args.modified_types_filepath)
    entity_instances = deserialize(self.filename, universe)
    self.ValidateEntities(entity_instances)
    self.StartTelemetryValidation(self.subscription, self.service_account,
                                  message_handler)

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
      print('Building Config must contain on entity with a building type')
      sys.exit(0)
    print('Entities Validated !')


  def StartTelemetryValidation(self, subscription,
                               service_account_file, msg_handler):
    """Validates telemetry payload received from the subscription.
     Args:
       subscription: a pubsub subscription.
       service_account_file: a GCP service account file.
    """
    if self.pubsub_validation_set:
      print('Connecting to pubsub subscription: ', subscription)
      sub = subscriber.Subscriber(subscription, service_account_file)
      sub.Listen(msg_handler)

  def _PrepareArgs(self):
    """Prepares the arguments for the user input."""
    parser = argparse.ArgumentParser(
        description='Validate a YAML building configuration file')

    parser.add_argument('-i', '--input',
                        dest='filename',
                        required=True,
                        help='Filepath to YAML building configuration',
                        metavar='FILE')

    parser.add_argument('-m', '--modified-ontology-types',
                        dest='modified_types_filepath',
                        required=False,
                        help='Filepath to modified type filepaths',
                        metavar='MODIFIED_TYPE_FILEPATHS')

    parser.add_argument('-s', '--subscription',
                        dest='subscription',
                        required=False,
                        help='pubsub subscription',
                        metavar='subscription')

    parser.add_argument('-a', '--service-account',
                        dest='service_account',
                        required=False,
                        help='service account',
                        metavar='service-account')

    self.args = parser.parse_args()
    self.filename = self.args.filename

    self.subscription = self.args.subscription
    self.service_account = self.args.service_account
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
