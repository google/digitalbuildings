"""
  A collection of classes to represent the group section of the YAML.

  They are responsible for filling up the section with data.

  They also hold the logic for how to read the input files in order to
  retrieve the correct data for a group.
"""

import re
import abc
from building_blocks.group import LTGWGroup


"""
  Base class for the group section.
"""
class GroupSection:

  def __init__(self, files):
    self._groups = dict()

  # Logic for reading the excel data to fill up group data.
  @abc.abstractmethod
  def _create_group(self, data):
    pass

  # Logic for filling up group list goes here.
  @abc.abstractmethod
  def _populate_groups(self):
    pass

  @abc.abstractmethod
  def _fill_group_connections(self):
    pass

  # Call to retrieve the data in the form of a dictionary.
  def to_dictionary(self):
    group_dictionary = {}
    
    for group in self._groups:
      group_dictionary.update(self._groups[group].to_dictionary())
      
    return group_dictionary
