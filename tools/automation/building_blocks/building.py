"""
  Contains classes which are used to store data for a building.

  Ready to use, or extend subclasses as required to fill cases where more 
  information needs to be stored.

  Call to_dictionary() to retrieve all the data.
"""

import abc

class Building:
  
  def __init__(self, building_name, building_id):
    self._name = building_name
    self._id = "FACILITIES/{0}".format(building_id)
  
  """
    Call this to retrieve a dictionary representing this dataset.
  """
  def to_dictionary(self):
    return {
      self._name: {
        "type": "FACILITIES/BUILDING",
        "id": self._id
      }
    }
