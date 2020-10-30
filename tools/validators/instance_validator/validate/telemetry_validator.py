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

TRANSLATION = "translation"
STATES = "states"
UNITS = "unit_values"

class TelemetryValidator(object):
  """TODO"""

  def __init__(self, entities):
    super().__init__()
    self.entities = entities
    self.validated_entities = {}
    self.validation_errors = {}

  def AddError(self, error):
    self.validation_errors.append(error)

  def AllEntitiesValidated(self):
    return self.entities.len() == self.validated_entities.len()

  def StartTimer(self):
    ###

  def MessageValidator(self, message):
    t = telemetry.Telemetry(message)
    entity = t.entity_name
    if entity in self.validated_entities:
      # Already validated telemetry for this entity, so the message can be skipped.
      return
    self.validated_entities[entity] = True

    if t.entity_name not in self.entities:
      self.AddError(TelemetryError(entity, None, "Unknown entity"))
      message.ack()
      return

    entity = entities[t.entity_name]
    for point_name, point_config in entity[TRANSLATION]:
      if point_name not in t.points.keys():
        self.AddError(TelemetryError(entity, point_name, "Missing point"))
        continue

      point = t.points[point_name]
      pv = point.present_value

      has_states = STATES in point_config
      has_units = UNITS in point_config

      if has_states:
        states = point_config[STATES]
        if pv not in states.keys():
          self.AddError(TelemetryError(entity, point_name, "Invalid state: " + pv))
          continue

      if value_is_numeric(pv):
        if value_is_integer(pv):
          if not (has_states or has_units):
            self.AddError(TelemetryError(entity, point_name, "Integer value without states or units: " + pv))
        elif not has_units:
            self.AddError(TelemetryError(entity, point_name, "Numeric value without units: " + pv))

    message.ack()

  def value_is_numeric(value):
    try:
      float(value)
    except ValueError:
      return False
    return True

  def value_is_integer(value):
    try:
      return int(value) == float(value)
    except ValueError:
      return False
