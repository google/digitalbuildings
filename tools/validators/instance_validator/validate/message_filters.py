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

"""Helper classes for filtering messages"""

class Udmi():
  """ Helper functions for filtering UDMI messages based on message and
      attributes
  """

  SUB_FOLDER = 'subFolder'
  SUB_TYPE = 'subType'
  STATE = 'state'
  POINTSET = 'pointset'

  @staticmethod
  def telemetry(attributes):
    """ Checks if a PubSub message is a UDMI Telemetry (pointset event) message
    based on message attributes

    Args:
      attributes: PubSub message attributes

    Returns:
      true/false if message type is UDMI telemetry
    """
    if (attributes.get(Udmi.SUB_FOLDER) == Udmi.POINTSET
      and attributes.get(Udmi.SUB_TYPE) != Udmi.STATE):
      return True
    return False
