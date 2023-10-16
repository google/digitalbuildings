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
import enum

class ConfigMode(enum.Enum):
  """Enumerated building config file processing modes."""

  INITIALIZE = 'INITIALIZE'
  UPDATE = 'UPDATE'
  EXPORT = 'EXPORT'

  @classmethod
  def FromString(cls, value: str):
    """Returns a ConfigMode instance matching the provided string."""
    for _, member in cls.__members__.items():
      if member.value == value:
        return member
    raise LookupError

  @classmethod
  def Default(cls):
    """Returns the default ConfigMode if no config block is provided."""
    return cls.INITIALIZE


class EntityOperation(enum.Enum):
  """Enumerated building config entity processing modes."""

  UPDATE = 'UPDATE'
  ADD = 'ADD'
  DELETE = 'DELETE'
  EXPORT = 'EXPORT'

  @classmethod
  def FromString(cls, value: str):
    """Returns a ConfigMode instance matching the provided string."""
    for _, member in cls.__members__.items():
      if member.value == value:
        return member
    raise LookupError