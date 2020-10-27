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

class TelemetryValidator(object):
  """TODO"""

  def __init__(self, entities, ontology):
    super().__init__()
    self.entities = entities
    # track unvalidated entities by name, once no entities are left to be validated (or some timeout period passes), we can call the telemetry 'validated'
    self.validated_entities = {}

  def message_handler(self, message):
    t = telemetry.Telemetry(message)
    if t.entity_name in self.validated_entities:
      # Already validated telemetry for this entity, so the message can be skipped.
      return

    entity = entities[t.entity_name]
    # TODO: check existence of translation key
    for k, v in entity["translation"]: # TODO: clean


    for k, v in t.points.items():
      print()
    message.ack()

# to validate:
# - translation exists
# - all points in entity config are sent in telemetry
# - numeric points have a unit defined
# - multistate points have a state map
