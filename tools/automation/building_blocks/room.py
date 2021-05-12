"""
  Contains classes which are used to store data for a room.

  Ready to use, or extend subclasses as required to fill cases where more 
  information needs to be stored.

  Call to_dictionary() to retrieve all the data.
"""

import abc


class Room:
  
  def __init__(self, room_name, room_id):
    self._name = room_name
    self._id = "FACILITIES/{0}".format(room_id)
    self._connections = {}
  
  def populate_connections(self, room_name):
    self._connections.update({room_name: "CONTAINS"})    

  def to_dictionary(self):
    return_dictionary = {
      self._name: {
        "type": "FACILITIES/ROOM",
        "id": self._id
      }
    }
    
    if len(self._connections) > 0:
      return_dictionary[self._name].update({
        "connections": self._connections
      })

    return return_dictionary

class DBORoom(Room):

  def __init__(self, room_name, room_id, room_type):
    super().__init__(room_name, room_id)
    self._room_type = room_type

  def to_dictionary(self):
    return_dictionary = {
      self._name: {
        "type": self._room_type,
        "id": self._id
      }
    }

    if len(self._connections) > 0:
      return_dictionary[self._name].update({
        "connections": self._connections
      })

    return return_dictionary
