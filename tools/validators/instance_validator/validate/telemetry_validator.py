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

import datetime
import re
import sys
import threading
import time
from typing import Dict

# pylint: disable=g-importing-member
from validate import field_translation as ft_lib
from validate import telemetry
from validate import telemetry_validation_report as tvr
from validate.constants import TELEMETRY_TIMESTAMP_FORMAT

DEVICE_ID = telemetry.DEVICE_ID
DEVICE_NUM_ID = telemetry.DEVICE_NUM_ID
GUID = 'guid'
MAX_TIMESTAMP_DIFFERENCE_SEC = 10  # in seconds


class TelemetryValidator(object):
  """Validates telemetry messages against a building config file.

  Attributes:
    entities_with_translation: Mapping of entity codes to EntityInstances that
      map 1:1 from a building config to a telemetry message.
    timeout: The max time the validator must read messages from pubsub.
    callback: The method called by the pubsub listener upon receiving a msg.
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

  def __init__(self, entities, timeout, callback, report_directory=None):
    """Init.

    Args:
      entities: EntityInstance dictionary
      timeout: validation timeout duration in seconds
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
    # TODO(b/267794785): Calling flush to work around an assert in the Python
    # runtime when the stdout is flushed with large buffers. The actual issue
    # is likely caused by a threading bug somewhere else.
    # See https://yaqs.corp.google.com/eng/q/4487223501186400256.
    sys.stdout.flush()

    tele = telemetry.Telemetry(message)
    entity_code = tele.attributes[DEVICE_ID]
    cloud_device_id = tele.attributes[DEVICE_NUM_ID]

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

    validation_block = self._ValidationBlockHelper(message, entity)

    if not validation_block.valid:
      self.AddInvalidMessageBlock(validation_block)
    message.ack()
    self.CallbackIfCompleted()

  def _PublishTimeDifferenceHelper(
      self, message_publish_time: datetime.datetime, message_timestamp: str
  ) -> float:
    """Returns difference between telemetry message timestamp and publish time.

    timestamp is given according to UTC ISO8601 (ex.
    2020-10-15T17:21:59.000Z)
    Args:
      message_publish_time: time, as a datetime.datetime object, the message was
        published by pubsub.
      message_timestamp: the recorded timestamp, as a string, of the data
        payload

    Returns:
      publish_timestamp_difference: total absolute difference between
      message_publish_time and message_timestamp in seconds as a float
    """

    # pylint: disable=line-too-long
    def _FormatTimestamp(timestamp: str) -> datetime.datetime:
      """Helper function to format string timestamps."""
      # remove microseconds if present
      timestamp_pattern = re.compile(
          r'^([0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{2,}Z)'
      )
      if timestamp_pattern.match(timestamp):
        timestamp = timestamp[:19] + 'Z'
      return datetime.datetime(
          *time.strptime(timestamp, TELEMETRY_TIMESTAMP_FORMAT)[0:6],
          tzinfo=datetime.timezone.utc,
      )

    publish_timestamp_difference = abs(
        (
            message_publish_time - _FormatTimestamp(message_timestamp)
        ).total_seconds()
    )

    return publish_timestamp_difference

  def _ValidationBlockHelper(
      self, message, entity
  ) -> tvr.TelemetryMessageValidationBlock:
    """Validates a telemetry message points and creates a validation block.

    Args:
      message: The telemetry message to validate.
      entity: The entity corresponding to the message.

    Returns:
      validation_block: Results of comparing entity points to telemetry message.
    """
    tele = telemetry.Telemetry(message)
    entity_code = tele.attributes[DEVICE_ID]
    cloud_device_id = tele.attributes[DEVICE_NUM_ID]
    message_timestamp = tele.timestamp
    message_publish_time = tele.publish_time
    message_version = tele.version

    expected_points = [
        field_translation.std_field_name
        for field_translation in entity.translation.values()
        if field_translation.mode == ft_lib.PresenceMode.PRESENT
    ]

    validation_block = tvr.TelemetryMessageValidationBlock(
        guid=entity.guid,
        code=entity_code,
        timestamp=message_timestamp,
        version=message_version,
        expected_points=expected_points,
    )
    # Check that pubsub message publish time vs message timestamp
    publish_timestamp_difference = self._PublishTimeDifferenceHelper(
        message_publish_time, message_timestamp
    )
    if publish_timestamp_difference > MAX_TIMESTAMP_DIFFERENCE_SEC:
      validation_block.AddDescription(
          '[WARNING]\tTelemetry message publish time vs timestamp'
          f' differs by {publish_timestamp_difference} seconds.'
      )

    # Check a telemetry message cloud device id exists in the building config.
    if cloud_device_id != entity.cloud_device_id:
      validation_block.AddDescription(
          f'[ERROR]\tBuilding Config entity: {entity.code} with Guid:'
          f' {entity.guid} has invalid cloud device id:'
          f' {entity.cloud_device_id}. Expecting {cloud_device_id}'
      )

    print(f'Validating telemetry message for entity: {entity_code}')
    point_full_paths = {
        f'points.{key}.present_value': key for key in tele.points
    }
    # check telemetry points against entity points to determine extra points
    raw_field_names = {
        field_translation.raw_field_name: field_translation.std_field_name
        for field_translation in entity.translation.values()
        if isinstance(field_translation, ft_lib.DefinedField)
    }
    for point_path, point_name in point_full_paths.items():
      if point_path in raw_field_names:
        continue
      validation_block.AddExtraPoint(point_name)
    # check entity points against telemetry points to determine missing and
    # others
    for field_translation in entity.translation.values():
      if isinstance(field_translation, ft_lib.UndefinedField):
        continue
      if field_translation.raw_field_name not in point_full_paths:
        if not tele.is_partial:
          validation_block.AddMissingPoint(field_translation.std_field_name)
        continue

      point = tele.points[point_full_paths[field_translation.raw_field_name]]
      pv = point.present_value

      if pv is None:
        validation_block.AddMissingPresentValue(point=point.point_name)
        continue

      if isinstance(field_translation, ft_lib.MultiStateValue):
        if pv not in field_translation.raw_values:
          validation_block.AddUnmappedState(state=pv, point=point.point_name)
          continue

      elif isinstance(
          field_translation, ft_lib.DimensionalValue
      ) and not self.ValueIsNumeric(pv):
        validation_block.AddInvalidDimensionalValue(
            value=pv, point=point.point_name
        )

    return validation_block

  def ValueIsNumeric(self, value):
    """Returns true if the value is numeric."""
    if isinstance(value, bool):
      return False
    try:
      float(value)
    except ValueError:
      return False
    return True
