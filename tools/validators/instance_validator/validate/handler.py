# Copyright 2023 Google LLC
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
import json
import os
import sys
from typing import Dict, List, Tuple

from validate import constants
from validate import entity_instance
from validate import generate_universe
from validate import instance_parser
from validate import subscriber
from validate import telemetry_validation_report as tvr
from validate import telemetry_validator
from yamlformat.validator import presubmit_validate_types_lib as pvt


def GetDefaultOperation(
    config_mode: instance_parser.ConfigMode,
) -> instance_parser.EntityOperation:
  """Returns the default EntityOperation for the ConfigMode."""
  if config_mode == instance_parser.ConfigMode.INITIALIZE:
    return instance_parser.EntityOperation.ADD
  # we default to export for a config update when no operation is specified
  elif config_mode == instance_parser.ConfigMode.UPDATE:
    return instance_parser.EntityOperation.EXPORT
  elif config_mode == instance_parser.ConfigMode.EXPORT:
    return instance_parser.EntityOperation.EXPORT
  else:
    raise LookupError


def Deserialize(
    yaml_files: List[str],
) -> Tuple[
    Dict[str, entity_instance.EntityInstance], instance_parser.ConfigMode
]:
  """Parses a yaml configuration file and deserializes it.

  Args:
    yaml_files: list of building configuration files.

  Returns:
    entities: A map of entity GUID to EntityInstance.
    ConfigMode: INITIALIZE or UPDATE
  """

  print('[INFO]\tStarting syntax validation.')
  parser = instance_parser.InstanceParser()
  for yaml_file in yaml_files:
    print(f'[INFO]\tOpening file: {yaml_file}.')
    parser.AddFile(yaml_file)
  parser.Finalize()

  default_entity_operation = GetDefaultOperation(parser.GetConfigMode())

  entities = {}
  for entity_key, entity_yaml in parser.GetEntities().items():
    try:
      entity = entity_instance.EntityInstance.FromYaml(
          entity_key, entity_yaml, default_entity_operation
      )
      entities[entity.guid] = entity
    except ValueError as ex:
      print(
          '[ERROR]\tInvalid Entity syntax found for this entity: '
          f'{entity_key} and this content: "{entity_yaml}" and with error'
          f': "{ex}"'
      )
      raise ex
    except KeyError as ex:
      print(
          '[ERROR]\tInvalid Entity syntax found for this entity: '
          f'{entity_key} and this content: "{entity_yaml}" and with error'
          f': "{ex}"'
      )
      raise ex

  return entities, parser.GetConfigMode()


def _ValidateConfig(
    filenames: List[str], universe: pvt.ConfigUniverse, is_udmi
) -> List[entity_instance.EntityInstance]:
  """Runs all config validation checks."""
  print(f'[INFO]\tLoading config files: {filenames}')
  entities, config_mode = Deserialize(filenames)
  print('[INFO]\tStarting config validation.')
  helper = EntityHelper(universe)
  return helper.Validate(entities, config_mode, is_udmi)


def _ValidateTelemetry(
    subscription: str,
    service_account: str,
    entities: Dict[str, entity_instance.EntityInstance],
    timeout: int,
    is_udmi: bool,
) -> None:
  """Runs all telemetry validation checks."""
  helper = TelemetryHelper(subscription, service_account)
  helper.Validate(entities, timeout, is_udmi)


def RunValidation(
    filenames: List[str],
    use_simplified_universe: bool = False,
    modified_types_filepath: str = None,
    default_types_filepath: str = constants.ONTOLOGY_ROOT,
    subscription: str = None,
    service_account: str = None,
    report_filename: str = None,
    timeout: int = constants.DEFAULT_TIMEOUT,
    is_udmi: bool = True,
) -> None:
  """Top level runner for all validations.

  Args:
    filenames: List of building config filenames to validate.
    use_simplified_universe: Boolean to use small testing ConfigUniverse.
    modified_types_filepath: Relative path to a modified ontology.
    default_types_filepath: Relative path to the DigitalBuildings ontology.
    subscription: Fully qualified path to a Google Cloud Pubsub subscription.
    service_account: Fully qualified path to a service account key file.
    report_filename: Fully qualified path to write a validation report to.
    timeout: Timeout duration of the telemetry validator. Default is 60 seconds.
    is_udmi: Telemetry follows UDMI standards.
  """
  saved_stdout = sys.stdout
  report_file = None

  print('[INFO]\tStarting validation process.')
  if report_filename:
    # pylint: disable=consider-using-with
    report_file = open(report_filename, 'w', encoding='utf-8')
    sys.stdout = report_file
  try:
    print('[INFO]\tLoading ontology.')
    universe = generate_universe.BuildUniverse(
        use_simplified_universe=use_simplified_universe,
        modified_types_filepath=modified_types_filepath,
        default_types_filepath=default_types_filepath,
    )
    if not universe:
      print('[ERROR]\tUniverse did not load properly.')
      sys.exit(0)
    print('[INFO]\tOntology loaded.')

    entities = _ValidateConfig(filenames, universe, is_udmi)
    if subscription:
      print('[INFO]\tStarting telemetry validation.')
      _ValidateTelemetry(
          subscription, service_account, entities, timeout, is_udmi
      )
    else:
      print(
          '[WARNING]\tTelemetry validation skipped, subscription '
          'not found. Please provide a subscription and service account to '
          'run telemetry validation. See here for more details: '
          'https://google.github.io/digitalbuildings/tools/validators/'
          'instance_validator/#telemetry-validation'
      )
  finally:
    sys.stdout = saved_stdout
    if report_file:
      print(f'[INFO]\tInstance valoidation report generated: {report_file}')
      report_file.close()
    print('[INFO]\tInstance validation completed.')


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

  def Validate(
      self,
      entities: Dict[str, entity_instance.EntityInstance],
      timeout: int,
      is_udmi: bool,
  ) -> None:
    """Validates telemetry payload received from the subscription.

    Args:
      entities: EntityInstance dictionary keyed by entity name
      timeout: number of seconds to wait for telemetry
      is_udmi: true/false treat telemetry stream as UDMI; default True.
    """

    print(f'[INFO]\tConnecting to PubSub subscription {self.subscription}')
    sub = subscriber.Subscriber(self.subscription, self.service_account_file)
    if is_udmi:
      print('[INFO]\tValidating telemetry payload for UDMI compliance.')
    validator = telemetry_validator.TelemetryValidator(
        entities, timeout, is_udmi, _TelemetryValidationCallback
    )
    validator.StartTimer()
    try:
      print('[INFO]\tStaring to listen to subscription messages.')
      sub.Listen(validator.ValidateMessage)
    finally:
      print('[INFO]\tStopping subscription listener.')
      validator.StopTimer()


def _TelemetryValidationCallback(
    validator: telemetry_validator.TelemetryValidator,
) -> None:
  """Callback when the telemetry validator finishes.

  This could be called due to a timeout or because telemetry messages were
  received and validated for every expected entity.

  Args:
    validator: the telemetry validator that triggered the callback.
  """

  print('[INFO]\tGenerating telemetry validation report.')
  expected_devices = {
      entity.guid: entity_code
      for entity_code, entity in validator.entities_with_translation.items()
  }
  error_devices = list(validator.GetInvalidMessageBlocks())

  # create validation report object
  validation_report = tvr.TelemetryValidationReport(
      expected_devices=expected_devices,
      missing_devices=validator.GetUnvalidatedEntities(),
      error_devices=error_devices,
      extra_devices=validator.GetExtraEntities(),
  )

  # create formatted validation report string
  validation_report_dict = validation_report.GenerateReport()

  # Export to filepath and write to console.
  telemetry_valdiation_report_path = os.path.join(
      os.getcwd(), 'telemetry_validation_report.json'
  )
  with open(
      telemetry_valdiation_report_path,
      'w',
  ) as report:
    report.write(json.dumps(validation_report_dict, indent=4))
    print(f'Report Generated: {telemetry_valdiation_report_path}')

  _thread.interrupt_main()


class EntityHelper(object):
  """A validation helper to coordinate the various steps of the validation.

  Attributes:
    universe: ConfigUniverse to validate against
  """

  def __init__(self, universe: pvt.ConfigUniverse):
    super().__init__()
    self.universe = universe

  def _IsDuplicateCDMIds(
      self, entities: Dict[str, entity_instance.EntityInstance]
  ) -> bool:
    """Returns whether a building config file has duplicate cloud device ids.

    Args:
      entities: Dict of entity guids to Entity instances.
    """
    cdm_dict = {}
    duplicate_cdm_set = set()
    for guid, entity in entities.items():
      if entity.cloud_device_id:
        if not cdm_dict.get(entity.cloud_device_id):
          cdm_dict.update({entity.cloud_device_id: [guid]})
        elif guid not in cdm_dict.get(entity.cloud_device_id):
          cdm_dict.get(entity.cloud_device_id).append(guid)
          duplicate_cdm_set.add(entity.cloud_device_id)
    for cdm_id in duplicate_cdm_set:
      print(
          f'[ERROR]\tDuplicate cloud device id {cdm_id} used for multiple'
          ' entities:'
      )
      for guid in cdm_dict.get(cdm_id):
        print(f'{guid}: {entities.get(guid).code}')
    if not duplicate_cdm_set:
      return True
    return False

  # TODO(b/266449585): Implement logging package to log errors to log file.
  def Validate(
      self,
      entities: Dict[str, entity_instance.EntityInstance],
      config_mode: instance_parser.ConfigMode,
      is_udmi: bool = True,
  ) -> Dict[str, entity_instance.EntityInstance]:
    """Validates entity instances that are already deserialized.

    Args:
      entities: a dict of entity instances
      config_mode: processing mode of the configuration
      is_udmi: flag to indicate validation under udmi; default True.

    Returns:
      A dictionary containing valid entities by GUID

    Raises:
      SyntaxError: If no building is found in the config
    """
    print('[INFO]\tValidating entity instance definitions.')
    building_found = False
    valid_entities = {}
    validator = entity_instance.CombinationValidator(
        self.universe, config_mode, entities
    )
    alpha_interdep_helper = AlphaInterdependencyHelper()
    is_valid = self._IsDuplicateCDMIds(entities)
    for entity_guid, current_entity in entities.items():
      if not alpha_interdep_helper.ValidateAndUpdateState(
          current_entity.operation
      ):
        raise ValueError(
            '(v1 Alpha): Building Config cannot have more '
            'than 2 operations; one being EXPORT.'
        )
      if (
          current_entity.operation is not instance_parser.EntityOperation.DELETE
          and current_entity.type_name.lower() == 'building'
      ):
        building_found = True
      if not validator.Validate(current_entity, is_udmi):
        is_valid = False
        continue
      valid_entities[entity_guid] = current_entity

    if not building_found:
      raise SyntaxError(
          'Building entity not found. Configs must contain '
          'a non-deleted entity of type FACILITIES/BUILDING.'
      )

    # Final validity determination.
    if is_valid:
      print('[INFO]\tAll entities validated SUCCESSFULLY.')
    else:
      print('[ERROR]\tSome entities FAILED validation. See logs.')
    return valid_entities


class AlphaInterdependencyHelper(object):
  """A validation helper to enforce v1 Alpha interdependency constraints."""

  def __init__(self):
    self.__other_entity_operation = None
    self.__validation_state = True

  def GetValidationState(self) -> bool:
    return self.__validation_state

  def ValidateAndUpdateState(
      self, entity_operation: instance_parser.EntityOperation
  ) -> bool:
    """Validates entity instance operation against v1 Alpha Milestones.

    Enforces the constraint that only one type of operation along with export
    operations are allowed.

    Args:
      entity_operation: entity instance operation

    Returns:
      True if entities seen thus far conform to v1 Alpha constraint; False o.w.
    """
    # first branch by EXPORT
    if entity_operation == instance_parser.EntityOperation.EXPORT:
      return self.GetValidationState()
    # either: ADD, DELETE, UPDATE
    # an entity operation of the three has been detected
    if self.__other_entity_operation is not None:
      # if this isn't the same one
      if self.__other_entity_operation != entity_operation:
        self.__validation_state = False
    else:
      self.__other_entity_operation = entity_operation
    return self.GetValidationState()
