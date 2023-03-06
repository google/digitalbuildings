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
"""Validates telemetry messages against a building config file.

The validator will call a specified callback function if at least one message
is received for all of the entities in the building config file, or if the
specfied timeout is reached. Current version only supports UDMI payloads.
"""

import threading
from typing import Dict

from validate import field_translation as ft_lib
from validate import message_filters
from validate import telemetry
from validate import telemetry_validation_report as tvr

DEVICE_ID = telemetry.DEVICE_ID
DEVICE_NUM_ID = telemetry.DEVICE_NUM_ID
GUID = 'guid'


class TelemetryValidator(object):
  """Validates telemetry messages against a building config file.

  Attributes:
    entities_with_translation: Mapping of entity codes to EntityInstances that
      map 1:1 from a building config to a telemetry message.
    timeout: The max time the validator must read messages from pubsub.
    callback: The method called by the pubsub listener upon receiving a msg.
    is_udmi: Flag to indicate whether telemtry payloads should conform to the
      UDMI standard.
    validated_entities: Map of entity guid to entity code Entities that have
      been run through ValidateMessage() and passed.
    timer: Validation timeout timer.
    invalid_message_blocks: List of TelemetryMessageValidationBlock instances
      for invalid pubsub messages.
    extra_entities: Mapping of entity guids to entity codes for entities
      reported in a tlemetry payload but not recorded in the building config
      file being validated.
    report_directory: fully qualified path to report output directory
  """

  def __init__(
      self, entities, timeout, is_udmi, callback, report_directory=None
  ):
    """Init.

    Args:
      entities: EntityInstance dictionary
      timeout: validation timeout duration in seconds
      is_udmi: Flag to indicate whether telemtry payloads should conform to the
        UDMI standard.
      callback: callback function to be called either because messages for all
        entities were seen or because the timeout duration was reached.
      report_directory: [Optional] fully quailified path to report output
        directory.
    """
    super().__init__()
    # cloud_device_id update requires translations; enforced in entity_instance
    self.entities_with_translation = {
        entity.code: entity
        for entity in entities.values()
        if entity.translation
    }
    self.timeout = timeout
    self.callback = callback
    self.is_udmi = is_udmi
    self.validated_entities = {}
    self._timer: threading.Timer = None
    self._invalid_message_blocks = []
    self._extra_entities = {}
    self.report_directory = report_directory

  def AddInvalidMessageBlock(self, validation_block):
    self._invalid_message_blocks.append(validation_block)

  def GetInvalidMessageBlocks(self):
    """Returns list of TelemetryMessageValidationBlock for invalid messages.

    A TelemetryMessageValidationBlock instance is a container for validations
    performed on a pubsub message.
    """
    return self._invalid_message_blocks

  def StartTimer(self):
    """Starts the validation timeout timer."""
    if not self._timer:
      self._timer = threading.Timer(self.timeout, lambda: self.callback(self))
      self._timer.start()

  def StopTimer(self):
    """Stops the validation timeout timer."""
    if self._timer:
      self._timer.cancel()
      self._timer = None

  def AllEntitiesValidated(self):
    """Returns True if every entity maps to a telemetry message."""
    return len(self.entities_with_translation) == len(self.validated_entities)

  def GetUnvalidatedEntities(self) -> Dict[str, str]:
    """Gets entities in a building config that do not map to a telemetry stream.

    Returns:
      Mapping of entity_guid to entity_code of entities not present in telemetry
      stream.
    """
    unvalidated_entities = self.entities_with_translation.copy()
    for (
        validated_entity_guid,
        validated_entity_code,
    ) in self.validated_entities.items():
      try:
        unvalidated_entities.pop(validated_entity_code)
      except KeyError:
        self._extra_entities.update(
            {validated_entity_guid: validated_entity_code}
        )
        continue
    return {
        entity.guid: entity_code
        for entity_code, entity in unvalidated_entities.items()
    }

  def GetExtraEntities(self) -> Dict[str, str]:
    """Gets entities reported in telemetry payload but not in building config.

    Returns:
        Mapping of cloud_device_id to entity_code.
    """
    return self._extra_entities

  def CallbackIfCompleted(self):
    """Checks if all entities have been validated, and calls the callback."""
    if self.AllEntitiesValidated():
      self.callback(self)

  def ValidateMessage(self, message):
    """Validates a telemetry message.

    Args:
      message: the telemetry message to validate.  Adds all validation errors
        for the message to a list of all errors and warnings discovered by this
        validator.
    """

    tele = telemetry.Telemetry(message)
    entity_code = tele.attributes[DEVICE_ID]
    cloud_device_id = tele.attributes[DEVICE_NUM_ID]
    message_timestamp = tele.timestamp
    message_version = tele.version

    # Telemetry message received for an entity not in building config
    if entity_code not in self.entities_with_translation.keys():
      self._extra_entities.update({cloud_device_id: entity_code})
      message.ack()
      return

    entity = self.entities_with_translation[entity_code]

    # Telemetry message received for a device that's already been validated.
    if entity.guid in self.validated_entities:
      # Already validated telemetry for this entity,
      # so the message can be skipped.
      message.ack()
      return
    self.validated_entities.update({entity.guid: entity_code})

    validation_block = tvr.TelemetryMessageValidationBlock(
        guid=entity.guid,
        code=entity_code,
        timestamp=message_timestamp,
        version=message_version,
        expected_points=entity.translation.values(),
    )

    # Check a telemetry message cloud device id exists in the building config.
    if cloud_device_id != entity.cloud_device_id:
      validation_block.description = (
          f'[ERROR]\tBuilding Config entity: {entity.code} with Guid:'
          f' {entity.guid} has invalid cloud device id:'
          f' {entity.cloud_device_id}. Expecting {cloud_device_id}'
      )

    # UDMI Pub/Sub streams could include messages which aren't telemetry
    # Raise a warning for devices that are sending non-udmi compliant payloads
    if self.is_udmi and not message_filters.Udmi.telemetry(message.attributes):
      validation_block.description += (
          f'[ERROR]\tMessage for {entity_code} does not conform to UDMI'
          ' standard.'
      )
      message.ack()
      return

    print(f'Validating telemetry message for entity: {entity_code}')
    point_full_paths = {
        f'points.{key}.present_value': key for key in tele.points
    }
    for field_translation in entity.translation.values():
      if isinstance(field_translation, ft_lib.UndefinedField):
        continue
      if field_translation.raw_field_name not in point_full_paths:
        if not tele.is_partial:
          validation_block.AddMissingPoint(field_translation.raw_field_name)
        continue

      point = tele.points[point_full_paths[field_translation.raw_field_name]]
      pv = point.present_value

      if pv is None:
        validation_block.AddMissingPresentValue(point=point)

      elif isinstance(field_translation, ft_lib.MultiStateValue):
        if pv not in field_translation.raw_values:
          validation_block.AddUnmappedState(state=pv, point=point)
          continue

      elif isinstance(
          field_translation, ft_lib.DimensionalValue
      ) and not self.ValueIsNumeric(pv):
        validation_block.AddInvalidDimensionalValue(value=pv, point=point)

    if not validation_block.valid:
      self.AddInvalidMessageBlock(validation_block)
    message.ack()
    self.CallbackIfCompleted()

  def ValueIsNumeric(self, value):
    """Returns true if the value is numeric."""
    if isinstance(value, bool):
      return False
    try:
      float(value)
    except ValueError:
      return False
    return True
