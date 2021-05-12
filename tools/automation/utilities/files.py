"""
  Contains classes which make it easier to access the input data.

  Each class represents all the data that a YAML file will need:

  - All column names needed are made publicly available in the classes.
  - All sheets can be accessed as a dictionary
"""

import pandas as pd
from pandas import DataFrame, ExcelFile, Series, read_excel


class DBOFiles:

  class SiteModelSheets:

    def __init__(self, site_model_path):
      excel_file = ExcelFile(site_model_path)
      self.LOCATIONS = get_sheet_dict(excel_file, "locations")
      self.ASSETS = get_sheet_dict(excel_file, "assets")
      self.PAYLOAD_TYPES = get_sheet_dict(excel_file, "device_entities")
      self.VIRTUAL_PAYLOAD_TYPES = get_sheet_dict(excel_file, "virtual_device_entities")
    
  class SiteModelColumns:

    # Used in the Locations sheet.
    SECTION = "dbo.section"
    ENTITY_NAME = "dbo.entity_name"
    TYPE = "dbo.type"
    ID = "dbo.id"
    CONNECTIONS_CONTAINS = "dbo.connections.contains"

    # Used in the Assets/Payload Types sheets.
    DEVICE_OR_VIRTUAL = "dbo.devices_or_virtual_devices"
    INSTANCE_NAME = "entity_instance_name"
    DEVICE_TYPE = "dbo.type"
    DEVICE_ID = "udmi.physical_tag.asset.guid"
    CONNECTION_FEEDS = "dbo.connections.feeds"
    CONNECTION_CONTROLS = "dbo.connections.controls"
    POINTSET_POINTS = "udmi.pointset.points"
    POINTS_TYPE = "points_type"
    TRANSLATION_FIELDS = "dbo.translation.fields"
    TRANSLATION_UNITS = "dbo.translation.units"
    STATES = "dbo.states"
    LINKS = "dbo.links"
    LINKS_POINTS = "dbo.links.points"
    LINKS_VIRTUAL_POINTS_TYPE = "virtual_points_type"
    LINKS_DEVICE_POINTS_TYPE = "device_points_type"
    SOURCE_DEVICE_FIELD = "dbo.source_device_field"
    VIRTUAL_DEVICE_FIELD = "dbo.virtual_device_field"

  def __init__(self, site_model_path):
    self.site_model_sheets = self.SiteModelSheets(site_model_path)
    

"""
    Returns the contents of the excel sheet as a dictionary of format:

    Cleans up the excel sheet by:
    - Replacing "nan" values with empty space.
    - Removing trailing whitespace.

    Assumes that the excel sheet has headers.

    Format of output dictionary will look like this:
    [
      { column1: value, ... columnN: value }  # Row 1
      ...
      { column1: value, ... columnN: value }  # Row N
    ]

    This allows for easy access, without having to know how to use pandas.
"""
def get_sheet_dict(excel_file, sheet_name):
  sheet_dataframe = pd.read_excel(excel_file, sheet_name, dtype=str)
  
  # Replace "nan" values with empty whitespace.
  sheet_dataframe = sheet_dataframe.fillna("")

  # Remove all trailing whitespace.
  for column in sheet_dataframe.columns:
    sheet_dataframe[column] = sheet_dataframe[column].apply(
      lambda dataframe_column: dataframe_column.strip()
    )

  return sheet_dataframe.to_dict('records')
