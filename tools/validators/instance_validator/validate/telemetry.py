# Copyright 2022 Google LLC
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
"""Parses Telemetry Payload."""

from __future__ import print_function
import json
from typing import Dict, Tuple

from validate import point

DEVICE_ID = 'deviceId'
DEVICE_REGISTRY_ID = 'deviceRegistryId'
DEVICE_NUM_ID = 'deviceNumId'
SUB_FOLDER = 'subFolder'
SUB_TYPE = 'subType'
VERSION = 'version'
POINTS = 'points'
TIMESTAMP = 'timestamp'
PRESENT_VALUE = 'present_value'
PARTIAL_UPDATE = 'partial_update'


class Telemetry(object):
  """Container for pubsub message.

  Attributes;
    attributes: pubsub message attributes
    version: the version in the payload
    timestamp: timestamp of the message in the payload
    points: a dictionary containing as key the points name and as value a
    Point class.
    is_partial: true if this message has only a partial pointset
  """

  def __init__(self, message):
    """Creates an Telemetry object from a pubsub message.

    Args:
      message: a pubsub message

    Returns:
      An instance of the Telemetry class.
    """
    super().__init__()
    self.attributes = self._parse_attributes(message.attributes)
    self.version, self.timestamp, self.points, self.is_partial = (
        self._parse_data(message.data))

  def _parse_attributes(self, pubsub_message_attributes) -> Dict[str, str]:
    """Receives a pubsub message data and parses it.

    Args:
      pubsub_message_attributes: pubsub message attributes

    Returns:
      parsed message attributes data in a dict. the attributes are keyed by the
      following: DEVICE_ID, DEVICE_REGISTRY_ID, DEVICE_NUM_ID, SUB_FOLDER
    """
    parsed_attributes = {}
    parsed_attributes[DEVICE_ID] = pubsub_message_attributes.get(DEVICE_ID)
    parsed_attributes[DEVICE_REGISTRY_ID] = \
    pubsub_message_attributes.get(DEVICE_REGISTRY_ID)
    parsed_attributes[DEVICE_NUM_ID] = \
      pubsub_message_attributes.get(DEVICE_NUM_ID)
    parsed_attributes[SUB_FOLDER] = \
      pubsub_message_attributes.get(SUB_FOLDER)
    parsed_attributes[SUB_TYPE] = \
      pubsub_message_attributes.get(SUB_TYPE)
    return parsed_attributes

  def _parse_data(self,
                  message) -> Tuple[str, str, Dict[str, point.Point], bool]:
    """Receives a pubsub message data and parses it.

    Args:
      message: pubsub telemetry payload, UDMI compliant

    Returns:
      version: the version in the payload
      timestamp: timestamp of the message in the payload
      points: a dictionary containing as key the points name and as value a
      Point class.
      is_partial: true if this message has only a partial pointset
    """
    version, timestamp, points, is_partial = (None, None, None, None)
    try:
      if type(message) is int:
        print(f'Received an invalid message (non Json payload)\n{message}')
        return version, timestamp, points, is_partial
      json_object = json.loads(message)
    except json.JSONDecodeError:
      print(f'The following Json payload is invalid:\n{message}')
    except AttributeError:
      print(f'The following Json raised an attribute error:\n{message}')
    except ValueError:
      print(f'The following Json raised an ValueError error:\n{message}')
    else:
      if type(json_object) is int:
        print(f'Received an invalid Json payload containing: \n{json_object}')
        return version, timestamp, points, is_partial
      # UDMI v1 sends as int and v1+ sends version as String
      if VERSION not in json_object.keys():
        print('Error: no version in ', json_object)
      return version, timestamp, points, is_partial
      version = str(json_object[VERSION])

      if TIMESTAMP not in json_object.keys():
        print('Error: no timestamp in ', json_object)
      return version, timestamp, points, is_partial
      timestamp = json_object[TIMESTAMP]

      is_partial = bool(json_object.get(PARTIAL_UPDATE, False))

      points = {}
      if POINTS not in json_object.keys():
        print('Error: no points in ', json_object)
        return version, timestamp, points, is_partial
      json_points = json_object[POINTS]
      for point_name, value in json_points.items():
        p = point.Point(point_name, value.get(PRESENT_VALUE))
        points[point_name] = p
    return version, timestamp, points, is_partial
