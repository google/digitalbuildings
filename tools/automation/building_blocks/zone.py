"""
  Contains classes which are used to store data for a zone.

  Ready to use, or extend subclasses as required to fill cases where more 
  information needs to be stored.

  Call to_dictionary() to retrieve all the data.
"""

import abc

class Zone:
  
  class ZoneLink:

    def __init__(self, name, points):
      self._name = name
      self._points = points

    def to_dictionary(self):
      return {self._name: self._points}

  class ZoneConnection:

    def __init__(self, name, value):
      self._name = name
      self._value = value

    def to_dictionary(self):
      return {self._name: self._value}
  
  def __init__(self, zone_name, zone_type, zone_id):
    self._name = zone_name
    self._type = zone_type
    self._id = zone_id
    self._links = {}
    self._connections = {}

  def populate_links(self, name, points):
    self._links.update(self.ZoneLink(name, points).to_dictionary())

  def populate_connections(self, name, value):
    self._connections.update(self.ZoneConnection(name, value).to_dictionary())

  """
    Call this to retrieve a dictionary representing this data.

    If links are empty, don't add the link value to dictionary.
  """
  def to_dictionary(self):
    return_dictionary = {
      self._name: {
        "type": self._type,
        "id": self._id,
      }
    }

    if len(self._links) > 0:
      return_dictionary[self._name].update({
        "links": self._links
      })

    if len(self._connections) > 0:
      return_dictionary[self._name].update({
        "connections": self._connections
      })

    return return_dictionary
