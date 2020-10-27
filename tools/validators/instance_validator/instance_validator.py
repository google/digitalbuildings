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

"""Main of the instance validator. This script takes a YAML building
configuration file as an argument and validates it for coherence with the
Digital Buildings ontology.

This is done by first ensuring the file syntax is valid YAML, then by
parsing the ontology and comparing it with the file contents.

This tool allows clients to independently validate their configuration files.
It saves time and provides more accuracy than manual error checks."""

from __future__ import print_function

from validate import generate_universe
from validate import entity_instance
from validate import instance_parser
from validate import subscriber
from validate import telemetry
import argparse
import sys

# TODO(nkilmer): update as you see good
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

# TODO add input and return type checks in all functions
if __name__ == '__main__':
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
                      help='Pubsub subscription for telemetry to validate',
                      metavar='subscription')

  parser.add_argument('-a', '--service-account',
                      dest='service_account',
                      required=False,
                      help='Service account used to pull messages from the subscription',
                      metavar='service-account')

  arg = parser.parse_args()

  # SYNTAX VALIDATION
  print('\nValidator starting ...\n')
  filename = arg.filename

  pubsub_validation_set = False
  if arg.subscription is not None and arg.service_account is not None:
    pubsub_validation_set = True
  else:
    print('Subscription and a service account file are both '
          'needed for the telemetry validation!')
    sys.exit(0)

  # prints for syntax errors and exits gracefully
  raw_parse = instance_parser.parse_yaml(filename)

  print('Passed syntax checks!')

  modified_types_filepath = arg.modified_types_filepath

  print('Generating universe ...')
  universe = generate_universe.BuildUniverse(modified_types_filepath)

  if universe is None:
    print('\nError generating universe')
    sys.exit(0)

  print('Universe generated successfully')

  parsed_entities = dict(raw_parse)
  entity_instances = {}
  entity_names = set(parsed_entities.keys())
  # first build all the entity instances
  for name, entity in parsed_entities.items():
    instance = entity_instance.EntityInstance(entity,
                                              universe,
                                              entity_names)
    entity_instances[name] = instance

  for entity_name, entity_instance in entity_instances.items():
    if not entity_instance.IsValidEntityInstance(entity_instances):
      print(entity_name, 'is not a valid instance')
      sys.exit(0)

  print('File passes all checks!')
  if pubsub_validation_set:
    print('Connecting to pubsub subscription: ', arg.subscription)
    sub = subscriber.Subscriber(arg.subscription, arg.service_account)
    validator = telemetry_validator.TelemetryValidator(parsed_entities)
    sub.Listen(validator.message_handler)
