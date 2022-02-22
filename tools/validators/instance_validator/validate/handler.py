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

import _thread
import datetime
import sys
from typing import Dict, List

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
    A map of entity GUID to EntityInstance.
  """

  print('Validating syntax please wait ...')
  parser = instance_parser.InstanceParser()
  for yaml_file in yaml_files:
    print(f'Opening file: {yaml_file}, please wait ...')
    parser.AddFile(yaml_file)
  parser.Finalize()

  default_entity_operation = instance_parser.EntityOperation.ADD
  if parser.GetConfigMode() == instance_parser.ConfigMode.UPDATE:
    default_entity_operation = instance_parser.EntityOperation.UPDATE

  code_to_guid_map = _CreateCodeToGuidMap(parser)

  entities = {}
  for entity_key, entity_yaml in parser.GetEntities().items():
    try:
      entity = entity_instance.EntityInstance.FromYaml(
          entity_key, entity_yaml, code_to_guid_map, default_entity_operation)
      entities[entity.guid] = entity
    except ValueError as ex:
      print(f'Invalid Entity {entity_key}: {ex}')
      raise
  return entities, parser.GetConfigMode()


def _CreateCodeToGuidMap(
    parser: instance_parser.InstanceParser) -> Dict[str, str]:
  """Creates a map from entity code to GUID for all entities."""
  code_to_guid_map: Dict[str, str] = {}

  for entity_key, entity_yaml in parser.GetEntities().items():
    if instance_parser.ENTITY_CODE_KEY in entity_yaml:
      entity_code = entity_yaml[instance_parser.ENTITY_CODE_KEY]
      entity_guid = entity_key
      code_to_guid_map[entity_code] = entity_guid
    else:
      entity_code = entity_key
      entity_guid = entity_yaml.get(instance_parser.ENTITY_GUID_KEY)
      code_to_guid_map[entity_code] = entity_guid

  return code_to_guid_map


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
                       timeout: int) -> None:
  """Runs all telemetry validation checks."""
  helper = TelemetryHelper(subscription, service_account)
  helper.Validate(entities, timeout)


def RunValidation(filenames: List[str],
                  use_simplified_universe: bool = False,
                  modified_types_filepath: str = None,
                  subscription: str = None,
                  service_account: str = None,
                  report_filename: str = None,
                  timeout: int = 60) -> None:
  """Master runner for all validations."""
  saved_stdout = sys.stdout
  report_file = None
  if report_filename:
    # pylint: disable=consider-using-with
    report_file = open(report_filename, 'w', encoding='utf-8')
    sys.stdout = report_file
  try:
    if bool(subscription) != bool(service_account):
      print('Subscription and a service account file are '
            'both needed for the telemetry validation!')
      sys.exit(0)
    print('\nStarting validator...\n')
    print('\nStarting universe generation...\n')
    universe = generate_universe.BuildUniverse(
        use_simplified_universe=use_simplified_universe,
        modified_types_filepath=modified_types_filepath)
    if not universe:
      print('\nError generating universe')
      sys.exit(0)
    print('\nStarting config validation...\n')
    entities = _ValidateConfig(filenames, universe)
    if subscription:
      print('\nStarting telemetry validation...\n')
      _ValidateTelemetry(subscription, service_account, entities, timeout)

  finally:
    sys.stdout = saved_stdout
    if report_file:
      report_file.close()


class TelemetryHelper(object):
  """A validation helper to encapsulate telemetry validation.

  Attributes:
    subscription: resource string referencing the subscription to check
    service_account_file: path to file with service account information
  """

  def __init__(self, subscription, service_account_file):
    super().__init__()
    self.subscription = subscription
    self.service_account_file = service_account_file

  def Validate(self, entities: Dict[str, entity_instance.EntityInstance],
               timeout: int) -> None:
    """Validates telemetry payload received from the subscription.

    Args:
      entities: EntityInstance dictionary keyed by entity name
      timeout: number of seconds to wait for telemetry
    """

    print('Connecting to pubsub subscription: ', self.subscription)
    sub = subscriber.Subscriber(self.subscription, self.service_account_file)
    validator = telemetry_validator.TelemetryValidator(
        entities, timeout, _TelemetryValidationCallback)
    validator.StartTimer()
    try:
      sub.Listen(validator.ValidateMessage)
    finally:
      validator.StopTimer()


def _TelemetryValidationCallback(
    validator: telemetry_validator.TelemetryValidator) -> None:
  """Callback when the telemetry validator finishes.

  This could be called due to a timeout or because telemetry messages were
  received and validated for every expected entity.

  Args:
    validator: the telemetry validator that triggered the callback.
  """

  print('Generating validation report ...')
  current_time = datetime.datetime.now()
  timestamp = current_time.strftime('%d-%b-%Y (%H:%M:%S)')
  report = f'\nReport Generated at: {timestamp}\n'

  if not validator.AllEntitiesValidated():
    report += ('No telemetry message was received for the following '
               'entities:')
    report += '\n'
    for entity_name in validator.GetUnvalidatedEntityNames():
      report += f'  {entity_name}\n'

  report += '\nTelemetry validation errors:\n'
  for error in validator.GetErrors():
    report += error.GetPrintableMessage()

  report += '\nTelemetry validation warnings:\n'
  for warnings in validator.GetWarnings():
    report += warnings.GetPrintableMessage()

  print('\n')
  print(report)
  print('Report Generated')
  _thread.interrupt_main()


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
      A dictionary containing valid entities by GUID

    Raises:
      SyntaxError: If no building is found in the config
    """
    print('Validating entities ...')
    building_found = False
    valid_entities = {}
    validator = entity_instance.CombinationValidator(self.universe, config_mode,
                                                     entities)
    for entity_guid, current_entity in entities.items():
      if (current_entity.operation is not instance_parser.EntityOperation.DELETE
          and current_entity.type_name.lower() == 'building'):
        building_found = True
      if not validator.Validate(current_entity):
        print(entity_guid, 'is not a valid instance')
        continue
      valid_entities[entity_guid] = current_entity

    if not building_found:
      print('Config must contain a non-deleted entity with a building type')
      raise SyntaxError('Building Config must contain an '
                        'entity with a building type')
    print('All entities validated')
    return valid_entities
