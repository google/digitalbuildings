"""
  A collection of classes to represent the floor section of the YAML.

  They are responsible for filling up the section with data.
  
  Holds logic for reading input files to retrieve the data for a floor.
"""

from building_blocks.floor import Floor, DBOFloor


class DBOFloorSection:

  def __init__(self, files):
    self._floors = {}
    self._site_model_sheets = files.site_model_sheets
    self._site_model_columns = files.SiteModelColumns
    self._populate_floors()

  def _create_floor(self, row):
    if row[self._site_model_columns.SECTION] == "Floors":
      floor_name = row[self._site_model_columns.ENTITY_NAME]
      floor_id = row[self._site_model_columns.ID]
      floor_type = row[self._site_model_columns.TYPE]
      floor_contains = row[self._site_model_columns.CONNECTIONS_CONTAINS]
      floor = DBOFloor(floor_name, floor_id, floor_type)
      floor.populate_connections(floor_contains)
      return floor

  def _populate_floors(self):
    for row in self._site_model_sheets.LOCATIONS:
      floor = self._create_floor(row)
      if floor is not None:
        self._floors.update(floor.to_dictionary())

  def to_dictionary(self):
    return self._floors