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

from datetime import datetime
import sys
from typing import Callable, Dict, List, Optional

from validate import entity_instance
from validate import generate_universe
from validate import instance_parser
from validate import subscriber
from validate import telemetry_validator
from yamlformat.validator import presubmit_validate_types_lib as pvt


def Deserialize(
    yaml_files: List[str]) -> Dict[str, entity_instance.EntityInstance]:
  """Parses a yaml configuration file and deserializes it.

  Args:
    yaml_files: list of building configuration files.

  Returns:
    A map of entity name to EntityInstance.
  """

  print('Validating syntax please wait ...')
  parser = instance_parser.InstanceParser()
  for yaml_file in yaml_files:
    print('Opening file: {0}, please wait ...'.format(yaml_file))
    parser.AddFile(yaml_file)
  parser.Finalize()

  default_entity_operation = instance_parser.EntityOperation.ADD
  if parser.GetConfigMode() == instance_parser.ConfigMode.UPDATE:
    default_entity_operation = instance_parser.EntityOperation.UPDATE

  entities = {}
  for entity_name, entity_yaml in parser.GetEntities().items():
    try:
      entities[entity_name] = entity_instance.EntityInstance.FromYaml(
          entity_yaml, default_entity_operation)
    except ValueError:
      print('Invalid Entity ' + entity_name)
      raise
  return entities, parser.GetConfigMode()


def _ValidateConfig(
    filenames: List[str],
    universe: pvt.ConfigUniverse) -> List[entity_instance.EntityInstance]:
  """Runs all config validation checks."""
  print('\nLoading config files...\n')
  entities, config_mode = Deserialize(filenames)
  print('\nStarting config validation...\n')
  helper = EntityHelper(universe)
  return helper.Validate(entities, config_mode)


def _ValidateTelemetry(subscription: str, service_account: str,
                       entities: Dict[str, entity_instance.EntityInstance],
                       report_filename: str, timeout: int) -> None:
  """Runs all telemetry validation checks."""
  helper = TelemetryHelper(subscription, service_account, report_filename)
  helper.Validate(entities, report_filename, timeout)


def RunValidation(filenames: List[str],
                  modified_types_filepath: str = None,
                  subscription: str = None,
                  service_account: str = None,
                  report_filename: str = None,
                  timeout: int = 60) -> None:
  """Master runner for all validations."""
  if bool(subscription) != bool(service_account):
    print('Subscription and a service account file are '
          'both needed for the telemetry validation!')
    sys.exit(0)
  print('\nStarting validator...\n')
  print('\nStarting universe generation...\n')
  universe = generate_universe.BuildUniverse(modified_types_filepath)
  if not universe:
    print('\nError generating universe')
    sys.exit(0)
  print('\nStarting config validation...\n')
  entities = _ValidateConfig(filenames, universe)
  if subscription:
    print('\nStarting telemetry validation...\n')
    _ValidateTelemetry(subscription, service_account, entities, report_filename,
                       timeout)


class TelemetryHelper(object):
  """A validation helper to encapsulate telemetry validation.

  Attributes:
    subscription: resource string referencing the subscription to check
    service_account_file: path to file with service account information
    report_filename: a report filename provided by the user
  """

  def __init__(self, subscription, service_account_file, report_filename=None):
    super().__init__()
    self.report_filename = report_filename
    self.subscription = subscription
    self.service_account_file = service_account_file

  def Validate(self, entities: Dict[str, entity_instance.EntityInstance],
               report_filename: str, timeout: int) -> None:
    """Validates telemetry payload received from the subscription.

    Args:
      entities: EntityInstance dictionary keyed by entity name
      report_filename: path to write results to
      timeout: number of seconds to wait for telemetry
    """

    print('Connecting to pubsub subscription: ', self.subscription)
    sub = subscriber.Subscriber(self.subscription, self.service_account_file)
    validator = telemetry_validator.TelemetryValidator(
        entities, timeout,
        self.BuildTelemetryValidationCallback(report_filename))
    validator.StartTimer()
    sub.Listen(validator.ValidateMessage)

  def BuildTelemetryValidationCallback(
      self,
      report_filename: Optional[str] = None
  ) -> Callable[[telemetry_validator.TelemetryValidator], None]:
    """Returns a callback to be called when a telemetry message is received.

    Args:
      report_filename: path to write results to
    """

    def TelemetryValidationCallback(
        validator: telemetry_validator.TelemetryValidator) -> None:
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
        report += ('No telemetry message was received for the following '
                   'entities:')
        report += '\n'
        for entity_name in validator.GetUnvalidatedEntityNames():
          report += '  {0}\n'.format(entity_name)

      report += '\nTelemetry validation errors:\n'
      for error in validator.GetErrors():
        report += error.GetPrintableMessage()

      report += '\nTelemetry validation warnings:\n'
      for warnings in validator.GetWarnings():
        report += warnings.GetPrintableMessage()

      if report_filename:
        with open(self.report_filename, 'w') as f:
          f.write(report)
          f.close()
      else:
        print('\n')
        print(report)
      print('Report Generated')
      sys.exit(0)

    return TelemetryValidationCallback


class EntityHelper(object):
  """A validation helper to coordinate the various steps of the validation.

  Attributes:
    universe: ConfigUniverse to validate against
  """

  def __init__(self, universe: pvt.ConfigUniverse):
    super().__init__()
    self.universe = universe

  def Validate(
      self, entities: Dict[str, entity_instance.EntityInstance],
      config_mode: instance_parser.ConfigMode
  ) -> Dict[str, entity_instance.EntityInstance]:
    """Validates entity instances that are already deserialized.

    Args:
      entities: a dict of entity instances
      config_mode: processing mode of the configuration

    Returns:
      A dictionary containing valid entities by name

    Raises:
      SyntaxError: If no building is found in the config
    """
    print('Validating entities ...')
    building_found = False
    valid_entities = {}
    validator = entity_instance.CombinationValidator(self.universe, config_mode,
                                                     entities)
    for entity_name, current_entity in entities.items():
      if (current_entity.operation is not instance_parser.EntityOperation.DELETE
          and current_entity.type_name.lower() == 'building'):
        building_found = True
      if not validator.Validate(current_entity):
        print(entity_name, 'is not a valid instance')
        continue
      valid_entities[entity_name] = current_entity

    if not building_found:
      print('Config must contain a non-deleted entity with a building type')
      raise SyntaxError('Building Config must contain an '
                        'entity with a building type')
    print('All entities validated')
    return valid_entities
