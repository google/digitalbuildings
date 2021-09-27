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
"""Validates telemetry messages against a building config file.

The validator will call a specified callback function if at least one message
is received for all of the entities in the building config file, or if the
specfied timeout is reached. Current version only supports UDMI payloads.
"""

import threading

from validate import field_translation as ft_lib
from validate import telemetry
from validate import telemetry_error
from validate import telemetry_warning

DEVICE_ID = 'deviceId'


class TelemetryValidator(object):
  """Validates telemetry messages against a building config file.

  Attributes;
    entities: a dict with entity_name as a key and EntityInstance as value.
    timeout: the max time the validator must read messages from pubsub.
    callback: the method called by the pubsub listener upon receiving a msg.

  Args:
    entities: EntityInstance dictionary
    timeout: validation timeout duration in seconds
    callback: callback function to be called either because messages for all
      entities were seen or because the timeout duration was reached
  """

  def __init__(self, entities, timeout, callback):
    super().__init__()
    self.entities_with_translation = dict(
        filter((lambda entities: entities[1].translation), entities.items()))
    self.timeout = timeout
    self.callback = callback
    self.validated_entities = {}
    # TODO(charbull): refactor by having on validation_report object instead
    #  of two: warning and errors
    self._validation_errors = []
    self._validation_warnings = []

  #TODO(charbull): fix this timeout
  def StartTimer(self):
    """Starts the validation timeout timer."""
    threading.Timer(self.timeout, lambda: self.callback(self)).start()

  def AllEntitiesValidated(self):
    """Returns true if a message was received for every entity."""
    return len(self.entities_with_translation) == len(self.validated_entities)

  def GetUnvalidatedEntityNames(self):
    """Returns a set of entities that have not been validated."""
    return set(self.entities_with_translation.keys()) \
                  - set(self.validated_entities.keys())

  def CallbackIfCompleted(self):
    """Checks if all entities have been validated, and calls the callback."""
    if self.AllEntitiesValidated():
      self.callback(self)

  def AddError(self, error):
    """Adds a validation error."""
    self._validation_errors.append(error)

  def GetErrors(self):
    """Returns all validation errors."""
    return self._validation_errors

  def AddWarning(self, warning):
    """Adds a validation Warning."""
    self._validation_warnings.append(warning)

  def GetWarnings(self):
    """Returns all validation warnings."""
    return self._validation_warnings

  def ValidateMessage(self, message):
    """Validates a telemetry message.

    Adds all validation errors for the message to a list of all errors
    discovered by this validator.
    """

    tele = telemetry.Telemetry(message)
    entity_name = tele.attributes[DEVICE_ID]

    # Telemetry message received for an entity not in building config
    if entity_name not in self.entities_with_translation.keys():
      #TODO(charbull): refactor warning class
      self.AddWarning(
          telemetry_warning.TelemetryWarning(
              entity_name, None, 'Telemetry message received for an entity not '
              'in building config'))
      message.ack()
      return

    if entity_name in self.validated_entities:
      # Already validated telemetry for this entity,
      # so the message can be skipped.
      message.ack()
      return
    self.validated_entities[entity_name] = True

    entity = self.entities_with_translation[entity_name]

    print('Validating telemetry message for entity: {0}'.format(entity_name))
    point_full_paths = {
        'points.{0}.present_value'.format(key): key for key in tele.points
    }
    for field_translation in entity.translation.values():
      if isinstance(field_translation, ft_lib.UndefinedField):
        continue
      if field_translation.raw_field_name not in point_full_paths:
        if not tele.is_partial:
          self.AddError(
              telemetry_error.TelemetryError(
                  entity_name, field_translation.raw_field_name,
                  'Field missing from telemetry message'))
        continue
      point = tele.points[point_full_paths[field_translation.raw_field_name]]
      pv = point.present_value
      if pv is None:
        if isinstance(field_translation, ft_lib.MultiStateValue):
          self.AddError(
              telemetry_error.TelemetryError(
                  entity_name, field_translation.raw_field_name,
                  'Missing state in telemetry '
                  'message: {}'.format(pv)))
        elif isinstance(field_translation, ft_lib.DimensionalValue):
          self.AddError(
              telemetry_error.TelemetryError(
                  entity_name, field_translation.raw_field_name,
                  'Missing number in telemetry '
                  'message: {}'.format(pv)))
        else:
          self.AddError(
              telemetry_error.TelemetryError(
                  entity_name, field_translation.raw_field_name,
                  'Present value missing from '
                  'telemetry message'))
        continue

      if isinstance(field_translation, ft_lib.MultiStateValue):
        if pv not in field_translation.states.values():
          self.AddError(
              telemetry_error.TelemetryError(
                  entity_name, field_translation.raw_field_name,
                  'Invalid state in telemetry message: {}'.format(pv)))

          continue

      if isinstance(field_translation,
                    ft_lib.DimensionalValue) and not self.ValueIsNumeric(pv):
        self.AddError(
            telemetry_error.TelemetryError(
                entity_name, field_translation.raw_field_name,
                'Invalid number in telemetry message: {}'.format(pv)))

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
