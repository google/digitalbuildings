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
"""Module for operation enumeration modules."""
import enum


class EntityOperationType(enum.Enum):
  """Building config entity operations."""

  # An entity is being updated with the current building config.
  UPDATE = 'UPDATE'

  # An entity is being added in the current building config.
  ADD = 'ADD'

  # An entity is being deleted in the current building config.
  DELETE = 'DELETE'

  # An entity is being exported in the current building config.
  EXPORT = 'EXPORT'


class EntityUpdateMaskAttribute(enum.Enum):
  """possible values for an entity update mask."""

  # An entity's human readable code or name.
  CODE = 'code'

  # An entity's DBO entity type name.
  TYPE = 'type'

  # A reporting entity's translation.
  TRANSLATION = 'translation'

  # An entity's connections.
  CONNECTIONS = 'connections'

  # A virtual entity's links.
  LINKS = 'links'


class EntityNamespace(enum.Enum):
  """Possible values for an entity namespace."""

  HVAC = 'HVAC'
  FACILTIES = 'FACILITIES'
  ELECTRICAL = 'ELECTRICAL'
  GATEWAYS = 'GATEWAYS'
  INFO_TECH = 'INFO_TECH'
  LIGHTING = 'LIGHTING'
  METERS = 'METERS'
  PHYSICAL_SECURITY = 'PHYSICAL_SECURITY'
  PLUMBING = 'PLUMBING'
  SAFETY = 'SAFETY'
  TRANSPORT = 'TRANSPORT'
  UNTYPED = 'UNTYPED'
