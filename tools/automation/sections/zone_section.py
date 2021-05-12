"""
  A collection of classes to represent the building section of the YAML.

  They are responsible for filling up the section with data.

  They also hold the logic for how to read the input files in order to
  retrieve the correct data for a building.
"""

import re
import abc
from building_blocks.zone import Zone

"""
  Base class for the building section.
"""
class ZoneSection:

  def __init__(self, files):
    self._zones = []

  # Logic for reading the excel data to fill up building data.
  @abc.abstractmethod
  def _create_zone(self):
    pass

  # Logic for filling up building list goes here.
  @abc.abstractmethod
  def _populate_zones(self):
    pass

  # Call to retrieve the data in the form of a dictionary.
  def to_dictionary(self):
    zone_dictionary = {}

    for zone in self._zones:
      zone_dictionary.update(zone.to_dictionary())

    return zone_dictionary


class DBOZoneSection:

  def __init__(self, files):
    self._zones = {}
    self._site_model_sheets = files.site_model_sheets
    self._site_model_columns = files.SiteModelColumns
    self._populate_zones()

  def _create_zone(self, row):
    if row[self._site_model_columns.SECTION] == "Zones":
      zone_name = row[self._site_model_columns.ENTITY_NAME]
      zone_id = "CDM/" + row[self._site_model_columns.ID]
      zone_type = row[self._site_model_columns.TYPE]
      zone_contains = row[self._site_model_columns.CONNECTIONS_CONTAINS]
      zone = Zone(zone_name, zone_type, zone_id)
      zone.populate_connections(zone_contains, "CONTAINS")
      return zone

  def _populate_zones(self):
    for row in self._site_model_sheets.LOCATIONS:
      zone = self._create_zone(row)
      if zone is not None:
        self._zones.update(zone.to_dictionary())

  def to_dictionary(self):
    return self._zones
