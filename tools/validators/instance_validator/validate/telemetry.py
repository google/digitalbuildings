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
"""Parses Telemetry Payload"""

from __future__ import print_function
import json
from validate import point

DEVICE_ID = 'deviceId'
DEVICE_REGISTRY_ID = 'deviceRegistryId'
DEVICE_NUM_ID = 'deviceNumId'
SUB_FOLDER = 'subFolder'
VERSION = 'version'
POINTS = 'points'
TIMESTAMP = 'timestamp'
PRESENT_VALUE = 'present_value'
PARTIAL_UPDATE = 'partial_update'


class Telemetry(object):
  """Creates an Telemetry object from a pubsub message.

  Args:
    message: a pubsub message

  Returns:
    An instance of the Telemetry class.
  """

  def __init__(self, message):
    super().__init__()
    self.attributes = self._parse_attributes(message.attributes)
    self.version, self.timestamp, self.points, self.is_partial = (
        self._parse_data(message.data))

  def _parse_attributes(self, pubsub_message_attributes):
    """Receives a pubsub message data and parses it.

      Args:
        pubsub_message_attributes: pubsub message attributes.

      Returns:
        Returns the parsed message data in a dict.
    """
    parsed_attributes = {}
    parsed_attributes[DEVICE_ID] = pubsub_message_attributes.get(DEVICE_ID)
    parsed_attributes[DEVICE_REGISTRY_ID] = \
      pubsub_message_attributes.get(DEVICE_REGISTRY_ID)
    parsed_attributes[DEVICE_NUM_ID] = \
      pubsub_message_attributes.get(DEVICE_NUM_ID)
    parsed_attributes[SUB_FOLDER] = \
      pubsub_message_attributes.get(SUB_FOLDER)
    return parsed_attributes

  def _parse_data(self, data):
    """Receives a pubsub message data and parses it.

    Args:
     message: pubsub telemetry payload, UDMI compliant

    Returns:
     version: the version in the payload
     timestamp: timestamp of the message in the payload
     points: a dictionary containing as key the points name and as value a Point
     class.
     is_partial: true if this message has only a partial pointset
  """
    json_object = json.loads(data)
    version = json_object[VERSION]
    timestamp = json_object[TIMESTAMP]
    is_partial = bool(json_object.get(PARTIAL_UPDATE, False))
    points = {}
    if POINTS not in json_object.keys():
      print('Error no points in ', json_object)
      return version, timestamp, None, is_partial
    json_points = json_object[POINTS]
    for point_name, value in json_points.items():
      p = point.Point(point_name, value.get(PRESENT_VALUE))
      points[point_name] = p
    return version, timestamp, points, is_partial
