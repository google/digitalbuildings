"""
  A collection of classes to represent the building section of the YAML.

  They are responsible for filling up the section with data.
  
  Holds logic for reading input files to retrieve the data for a building.
"""

from building_blocks.building import Building


class DBOBuildingSection:

  def __init__(self, files):
    self._buildings = {}
    self._site_model_sheets = files.site_model_sheets
    self._site_model_columns = files.SiteModelColumns
    self._populate_buildings()

  def _create_building(self, row):
    if row[self._site_model_columns.SECTION] == "Buildings":
      building_name = row[self._site_model_columns.ENTITY_NAME]
      building_id = row[self._site_model_columns.ID] 
      return Building(building_name, building_id)

  def _populate_buildings(self):
    for row in self._site_model_sheets.LOCATIONS:
        building = self._create_building(row)
        if building is not None:
          self._buildings.update(building.to_dictionary())

  def to_dictionary(self):
    return self._buildings
