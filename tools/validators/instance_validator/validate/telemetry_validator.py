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
specfied timeout duration is reached."""

import threading

from validate import telemetry
from validate import telemetry_error
from validate import telemetry_warning

DEVICE_ID = "deviceId"
TRANSLATION = "translation"
TYPE = "type"
STATES = "states"
UNITS = "unit_values"

class TelemetryValidator(object):
  """Validates telemetry messages against a building config file.

  Args:
    entities: parsed entities from building config
    timeout: validation timeout duration in seconds
    callback: callback function to be called when the validation finishes
  """

  def __init__(self, entities, timeout, callback):
    super().__init__()
    self.entities = entities
    self.timeout = timeout
    self.callback = callback
    self.validated_entities = {}
    self.validation_errors = []
    self.validation_warnings = []

  def StartTimer(self):
    """Starts the validation timeout timer."""
    threading.Timer(self.timeout, lambda: self.callback(self)).start()

  def AllEntitiesValidated(self):
    """Returns true if a message was received for every entity."""
    return len(self.entities) == len(self.validated_entities)

  def GetUnvalidatedEntities(self):
    """Returns a set of entities that have not been validated."""
    return set(self.entities.keys()) - set(self.validated_entities.keys())

  def CallbackIfCompleted(self):
    """Checks if all entities have been validated, and calls the callback."""
    if self.AllEntitiesValidated():
      self.callback(self)

  def AddError(self, error):
    """Adds a validation error."""
    self.validation_errors.append(error)

  def GetErrors(self):
    """Returns all validation errors."""
    return self.validation_errors

  def AddWarning(self, warning):
    """Adds a validation Warning."""
    self.validation_warnings.append(warning)

  def GetWarnings(self):
    """Returns all validation warnings."""
    return self.validation_warnings

  def ValidateMessage(self, message):
    """Validates a telemetry message.

    Adds all validation errors for the message to a list of all errors
    discovered by this validator."""

    t = telemetry.Telemetry(message)
    entity_name = t.attributes[DEVICE_ID]

    if entity_name not in self.entities:
      self.AddError(
          telemetry_error.TelemetryError(
              entity_name, None, "Unknown entity"))
      message.ack()
      return

    if entity_name in self.validated_entities:
      # Already validated telemetry for this entity,
      # so the message can be skipped.
      message.ack()
      return
    self.validated_entities[entity_name] = True

    entity = self.entities[entity_name]
    print("Validating telemetry message for entity: {0}".format(entity_name))

    if TRANSLATION not in entity.keys():
      # TODO: ignore if the type is a facility
      print("Missing Translation in Building Config for entity: {0}"
            .format(entity_name))
      self.AddWarning(
        telemetry_warning.TelemetryWarning(entity_name,
                                           None,
                                           "Missing Translation in Building Config"))
      message.ack()
      return

    for point_name, point_config in entity[TRANSLATION].items():
      if point_name not in t.points.keys():
        self.AddError(
            telemetry_error.TelemetryError(
                entity_name, point_name, "Missing point"))
        continue

      point = t.points[point_name]
      pv = point.present_value
      if pv is None:
        self.AddError(
            telemetry_error.TelemetryError(
                entity_name, point_name, "Missing present value"))
        continue

      has_states = STATES in point_config
      has_units = UNITS in point_config

      if has_states:
        states = point_config[STATES]
        if pv not in states.values():
          self.AddError(
              telemetry_error.TelemetryError(
                  entity_name, point_name, "Invalid state: {}".format(pv)))
          continue

      if has_units and not self.ValueIsNumeric(pv):
        self.AddError(
            telemetry_error.TelemetryError(
                entity_name, point_name, "Invalid number: {}".format(pv)))

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
