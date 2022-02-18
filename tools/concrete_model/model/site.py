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
"""Module for a site entity, and all relevant metadata for UDMI site model."""

from typing import Dict, List, Optional

from model.connection import Connection
from model.entity import Entity


# TODO(b/218318362) Be able to query an entity belonging to another site.
class Site(object):
  """Data container for a Building Configuration site.

  Within the Concrete Model, A site acts as the root node. While a site is an
  entity, it is aware of all of the nodes under itself as well.

  Attributes:
    name: a site's name.
    guid: a globally unique identification code for the site.
    latitude: A site's latitude.
    longitude: A site's longitude.
    altitude: A site's altitude.
    orientation: A site's orientation.
    address: A site's street address.
    street: The street which a site is one.
    city: The city which a site is in.
    state: The state which a site is in.
    county: The county which a site is in.
    country: The country which a site is in.
    postal_code: The postal code for a site.
    primary_function: The primary function for a site.
    timezone: A site's timezone.
    weather_station_ref: A site's weather station reference.
    entities: A mapping of entity guids to Entity instances to the construction
      of a building configuration document.
    entity_connections: A list of Connection instances where source entity is
      contained in self.
  """

  def __init__(self,
               name: str,
               entities: Dict[str, Entity],
               guid: Optional[str] = None,
               entity_connections: Optional[List[Connection]] = None,
               latitude: Optional[str] = None,
               longitude: Optional[str] = None,
               altitude: Optional[str] = None,
               orientation: Optional[str] = None,
               address: Optional[str] = None,
               street: Optional[str] = None,
               city: Optional[str] = None,
               state: Optional[str] = None,
               county: Optional[str] = None,
               country: Optional[str] = None,
               postal_code: Optional[str] = None,
               primary_function: Optional[str] = None,
               timezone: Optional[str] = None,
               weather_station_ref: Optional[str] = None) -> None:
    """Init. All arguments are optional.

    Args:
      name: site name.
      entities: A mapping of entity guids to Entity instances
        to the construction of a building configuration document.
      guid: A globally unique identifier(uuid4) for site.
      entity_connections: A list of Connection instances where source entity is
        contained in self.
      latitude: A site's latitude.
      longitude: A site's longitude.
      altitude: A site's altitude.
      orientation: A site's orientation.
      address: A site's street address.
      street: The street which a site is one.
      city: The city which a site is in.
      state: The state which a site is in.
      county: The county which a site is in.
      country: The country which a site is in.
      postal_code: The postal code for a site.
      primary_function: The primary function for a site.
      timezone: A site's timezone.
      weather_station_ref: A site's weather station reference.
    """
    self.name = name
    self._entities = entities
    self._guid = guid
    self.entity_connections = entity_connections
    self.latitude = latitude
    self.longitude = longitude
    self.altitude = altitude
    self.orientation = orientation
    self.address = address
    self.street = street
    self.city = city
    self.state = state
    self.county = county
    self.country = country
    self.postal_code = postal_code
    self.primary_function = primary_function
    self.timezone = timezone
    self.weather_station_ref = weather_station_ref

  @property
  def entities(self) -> Dict(str, Entity):
    """Returns a mapping of entity names to Entity instances."""
    return self._entities

  @entities.setter
  def entities(self, entities: Dict[str, Entity]) -> None:
    """Checks if entities is a valid mapping of entity names to instances and sets."""

  @property
  def guid(self) -> str:
    """Returns the GUID associated with self."""
    return self._guid

  @guid.setter
  def guid(self, guid: Optional[str] = None) -> str:
    """If guid argument is none, generate a new guid for set or just set if none.

    Args:
      guid: A UUID string.

    Returns:
      The generated GUID.
    """


class SiteMetadata(object):
  """Data container for UDMI site metadata.

  Attributes:
    cloud_region: The cloud region associated sith this site.
    site_name: The semantic name of the site used for validation and reporting.
    registry_id: Cloud IoT Core registry id for this site.
    devices: A Mapping of canonical device names to device information.
  """

  def __init__(self, cloud_region: str, site_name: str, registry_id: str):
    """Init.

    Args:
      cloud_region: The cloud region associated sith this site.
      site_name: The semantic name of the site used for validation and
        reporting.
      registry_id: Cloud IoT Core registry id for this site.
    """

    self.cloud_region = cloud_region
    self.site_name = site_name
    self.registry_id = registry_id

  def GetCloudIotConfig(self) -> Dict[str, str]:
    """Getter method for cloud iot config metadata.

    Returns:
      A mapping of Site instance attributes to their values.
    """
