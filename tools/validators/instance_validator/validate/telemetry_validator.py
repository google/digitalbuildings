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

DEVICE_ID = "deviceId"
TRANSLATION = "translation"
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
    self.validation_errors = {}

  def StartTimer(self):
    """Starts the validation timeout timer."""
    threading.Timer(self.timeout, lambda: self.callback(self)).start()

  def AllEntitiesValidated(self):
    """Returns true if a message was received for every entity."""
    return self.entities.len() == self.validated_entities.len()

  def CheckAllEntitiesValidated(self):
    """Checks if all entities have been validated, and calls the callback."""
    if self.AllEntitiesValidated():
      self.callback(self)

  def AddError(self, error):
    """Adds a validation error."""
    self.validation_errors.append(error)

  def ValidateMessage(self, message):
    """Validates a telemetry message."""
    t = telemetry.Telemetry(message)
    entity = t.attributes[DEVICE_ID]

    if entity not in self.entities:
      self.AddError(
        telemetry_error.TelemetryError(entity, None, "Unknown entity"))
      message.ack()
      return

    if entity in self.validated_entities:
      # Already validated telemetry for this entity,
      # so the message can be skipped.
      return
    self.validated_entities[entity] = True

    entity = self.entities[t.entity_name]
    for point_name, point_config in entity[TRANSLATION]:
      if point_name not in t.points.keys():
        self.AddError(
          telemetry_error.TelemetryError(entity, point_name, "Missing point"))
        continue

      point = t.points[point_name]
      pv = point.present_value
      if pv is None:
        self.AddError(
          telemetry_error.TelemetryError(
            entity, point_name, "Missing present value"))
        continue

      has_states = STATES in point_config
      has_units = UNITS in point_config

      if has_states:
        states = point_config[STATES]
        if pv not in states.values():
          self.AddError(
            telemetry_error.TelemetryError(
              entity, point_name, "Invalid state: " + pv))
          continue

      if has_units and not self.ValueIsNumeric(pv):
        self.AddError(
          telemetry_error.TelemetryError(
            entity, point_name, "Invalid number: " + pv))

    message.ack()
    self.CheckAllEntitiesValidated()

  def ValueIsNumeric(self, value):
    """Returns true if the value is numeric."""
    try:
      float(value)
    except ValueError:
      return False
    return True
