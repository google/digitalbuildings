"""
  A collection of classes to represent the device section of the YAML.

  They are responsible for filling up the section with data.

  They also hold the logic for how to read the input files in order to
  retrieve the correct data for a device.
"""

import re
import abc

from building_blocks.device import Device

"""
  Base class for the device section.
"""
class DeviceSection:

  def __init__(self, files):
    self._devices = []

  # Logic for reading the excel data to fill up device data.
  @abc.abstractmethod
  def _create_device(self, data):
    pass

  # Logic for filling up device list goes here.
  @abc.abstractmethod
  def _populate_devices(self):
    pass

  # Call to retrieve the data in the form of a dictionary.
  def to_dictionary(self):
    device_dictionary = {}

    for device in self._devices:
      device_dictionary.update(device.to_dictionary())

    return device_dictionary


class DBODeviceSection(DeviceSection):
  
  def __init__(self, files):
    super().__init__(files)
    self._site_model_sheets = files.site_model_sheets
    self._site_model_columns = files.SiteModelColumns
    self._populate_devices()

  def _get_devices_from_string(self, devices):
    linked_devices = []

    for device in devices.split(","):
      linked_devices.append(device.strip())
      
    return linked_devices

  def _get_units_dict(self, units_string):
    unit_strings = units_string.split(":")
    return {unit_strings[0].strip(): unit_strings[1].strip()}

  def _get_states_dict(self, state_string):
    state_strings = state_string.split()
    state_dict = {}

    for state in state_strings:
      state_dict.update({
        state.split("=")[1].upper(): "\"" + state.split("=")[0].upper() + "\""
      })

    return state_dict

  def _fill_device_connections(self, row, device):
    feeds = row[self._site_model_columns.CONNECTION_FEEDS]
    controls = row[self._site_model_columns.CONNECTION_CONTROLS]

    if not feeds.isspace() and len(feeds) > 0:
      feeds = self._get_devices_from_string(feeds)
      for i in feeds:
        device.populate_connections(i, "FEEDS")

    if not controls.isspace() and len(controls) > 0:
      controls = self._get_devices_from_string(controls)
      for i in controls:
        device.populate_connections(i, "CONTROLS")

  def _fill_device_translations(self, row, device):
    device_payload_type = row[self._site_model_columns.POINTSET_POINTS]

    for point in self._site_model_sheets.PAYLOAD_TYPES:

      if device_payload_type == point[self._site_model_columns.POINTS_TYPE]:
        
        name = point[self._site_model_columns.TRANSLATION_FIELDS]
        value = point[self._site_model_columns.POINTSET_POINTS]
        units = point[self._site_model_columns.TRANSLATION_UNITS]
        states = point[self._site_model_columns.STATES]

        translation_dict = {}

        translation_dict.update({
          "present_value": "\"points." + value + ".present_value\""
        })

        if not units.isspace() and len(units) > 0:
          translation_dict.update({
            "units": {
              "key": "\"pointset.points." + value + ".units\"",
              "values": self._get_units_dict(units)
            }
          })
        
        if not states.isspace() and len(states) > 0:
          translation_dict.update({
            "states": self._get_states_dict(states)
          })
        
        if translation_dict:
          device.populate_translations(name, translation_dict)

  def _create_device(self, row):
    if row[self._site_model_columns.DEVICE_OR_VIRTUAL] == "Device":
      device_name = row[self._site_model_columns.INSTANCE_NAME]
      device_type = row[self._site_model_columns.DEVICE_TYPE]
      device_id = "CDM/" + row[self._site_model_columns.DEVICE_ID]
      device = Device(device_name, device_type, device_id)
      self._fill_device_connections(row, device)
      self._fill_device_translations(row, device)
      return device

  def _populate_devices(self):
    for row in self._site_model_sheets.ASSETS:
      device = self._create_device(row)
      if device is not None:
        self._devices.append(device)


class DBOVirtualDeviceSection(DeviceSection):

  def __init__(self, files):
    super().__init__(files)
    self._site_model_sheets = files.site_model_sheets
    self._site_model_columns = files.SiteModelColumns
    self._populate_devices()

  def _get_devices_from_string(self, devices):
    linked_devices = []

    for device in devices.split(","):
      linked_devices.append(device.strip())
      
    return linked_devices

  def _get_asset_point_type_for_device(self, linked_device_name):
    asset_point_type = None
    for device in self._site_model_sheets.ASSETS:
      if linked_device_name == device[self._site_model_columns.INSTANCE_NAME]:
        asset_point_type = device[self._site_model_columns.POINTSET_POINTS]
        break

    return asset_point_type

  def _fill_device_connections(self, row, device):
    feeds = row[self._site_model_columns.CONNECTION_FEEDS]
    controls = row[self._site_model_columns.CONNECTION_CONTROLS]

    if not feeds.isspace() and len(feeds) > 0:
      feeds = self._get_devices_from_string(feeds)
      for i in feeds:
        device.populate_connections(i, "FEEDS")

    if not controls.isspace() and len(controls) > 0:
      controls = self._get_devices_from_string(controls)
      for i in controls:
        device.populate_connections(i, "CONTROLS")

  def _fill_device_links(self, row, device):
    linked_devices_string = row[self._site_model_columns.LINKS]

    linked_devices = self._get_devices_from_string(linked_devices_string)
    points_type = row[self._site_model_columns.LINKS_POINTS]

    for linked_device in linked_devices:
      linked_points_dict = {}
      asset_point_type = self._get_asset_point_type_for_device(linked_device)

      for point in self._site_model_sheets.VIRTUAL_PAYLOAD_TYPES:
        if points_type == point[self._site_model_columns.LINKS_VIRTUAL_POINTS_TYPE] \
          and asset_point_type == point[self._site_model_columns.LINKS_DEVICE_POINTS_TYPE]:  
          name = point[self._site_model_columns.SOURCE_DEVICE_FIELD]
          value = point[self._site_model_columns.VIRTUAL_DEVICE_FIELD]
          linked_points_dict.update({name: value})
      
      if linked_points_dict:
        device.populate_links(linked_device, linked_points_dict)

  def _create_device(self, row):
    if row[self._site_model_columns.DEVICE_OR_VIRTUAL] == "Virtual":
      device_name = row[self._site_model_columns.INSTANCE_NAME]
      device_type = row[self._site_model_columns.DEVICE_TYPE]
      device_id = "CDM/" + row[self._site_model_columns.DEVICE_ID]
      device = Device(device_name, device_type, device_id)
      self._fill_device_connections(row, device)
      self._fill_device_links(row, device)
      return device

  def _populate_devices(self):
    for row in self._site_model_sheets.ASSETS:
      device = self._create_device(row)
      if device is not None:
        self._devices.append(device)
