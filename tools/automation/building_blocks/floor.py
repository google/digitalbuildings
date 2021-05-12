"""
  Contains classes which are used to store data for a floor.

  Ready to use, or extend subclasses as required to fill cases where more 
  information needs to be stored.

  Call to_dictionary() to retrieve all the data.
"""

import abc

class Floor:
  
  def __init__(self, floor_name, floor_id):
    self._name = floor_name
    self._id = "FACILITIES/{0}".format(floor_id)
    self._connections = {}
  
  def populate_connections(self, building_name):
    self._connections.update({building_name: "CONTAINS"})

  def to_dictionary(self):
    return_dictionary = {
      self._name: {
        "type": "FACILITIES/FLOOR",
        "id": self._id
      }
    }
    
    if len(self._connections) > 0:
      return_dictionary[self._name].update({
        "connections": self._connections
      })

    return return_dictionary

class DBOFloor(Floor):

  def __init__(self, floor_name, floor_id, floor_type):
    super().__init__(floor_name, floor_id)
    self._floor_type = floor_type

  def to_dictionary(self):
    return_dictionary = {
      self._name: {
        "type": self._floor_type,
        "id": self._id
      }
    }

    if len(self._connections) > 0:
      return_dictionary[self._name].update({
        "connections": self._connections
      })

    return return_dictionary

