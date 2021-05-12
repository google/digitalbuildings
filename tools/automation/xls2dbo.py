#!/usr/bin/env python3
"""
  Automate the creation of dbo.yaml files.

  [Usage] 
  python3 xls2dbo.py [options] <sheet.xlsx>
"""

__author__ = "Francesco Anselmo, Edzel Monteverde"
__copyright__ = "Copyright 2021, Arup, ExcelRedstone"
__credits__ = ["Francesco Anselmo"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Francesco Anselmo"
__email__ = "francesco.anselmo@gmail.com"
__status__ = "Dev"

import re
import abc
import sys
import yaml
import argparse
from pyfiglet import *
from utilities.files import DBOFiles
from sections.building_section import DBOBuildingSection
from sections.floor_section import DBOFloorSection
from sections.room_section import DBORoomSection
from sections.device_section import DBODeviceSection
from sections.device_section import DBOVirtualDeviceSection
from sections.zone_section import DBOZoneSection


"""
  Base class representing a dbo yaml file.

  Extend as appropriate for your system.
"""
class YAML:

  # Default location for all YAML files.
  OUTPUT_PATH = "./dbo.yaml"

  # Write the YAML structure and contents into the dbo file.
  @abc.abstractmethod
  def create_yaml_file(self):
    None

  # Write dbo section into file.
  @staticmethod
  def write_yaml_section(yaml_file, section_dict, header):
    yaml_file.write(header)
    yaml.dump(
      section_dict, 
      yaml_file, 
      sort_keys=False,
      width=1000  # Keep long lines in one line.
    )
    yaml_file.write("\n")

  # Removes single quotes and empty bracket pairs from the finished YAML.
  def _cleanup_yaml(self):
    lines = []
    
    with open(self.OUTPUT_PATH, "r") as yaml_file:
      for line in yaml_file:
        lines.append(line)
    
    with open(self.OUTPUT_PATH, "w") as yaml_file:
      for line in lines:
        cleaned_line = re.sub(r"(.*: \{\}|')", "", line)
        yaml_file.write(cleaned_line)


class DBOYAML(YAML):
    
  OUTPUT_PATH = "./dbo.yaml"

  def __init__(self, site_model_path):
    DBO_files = DBOFiles(site_model_path)
    self.building_section = DBOBuildingSection(DBO_files)
    self.floor_section = DBOFloorSection(DBO_files)
    self.room_section = DBORoomSection(DBO_files)
    self.device_section = DBODeviceSection(DBO_files)
    self.virtual_device_section = DBOVirtualDeviceSection(DBO_files)
    self.zone_section = DBOZoneSection(DBO_files)

  def create_yaml_file(self):
    with open(self.OUTPUT_PATH, "w") as yaml_file:
      self.write_yaml_section(
        yaml_file, self.building_section.to_dictionary(), "# Building\n"
      )
      self.write_yaml_section(
        yaml_file, self.floor_section.to_dictionary(), "# Floor\n"
      )
      self.write_yaml_section(
        yaml_file, self.room_section.to_dictionary(), "# Rooms\n"
      )
      self.write_yaml_section(
        yaml_file, self.device_section.to_dictionary(), "# Devices\n"
      )
      self.write_yaml_section(
        yaml_file, self.virtual_device_section.to_dictionary(), "# Virtual Devices\n"
      )
      self.write_yaml_section(
        yaml_file, self.zone_section.to_dictionary(), "# Zones\n"
      )
    self._cleanup_yaml()


def show_title():
  """Show the program title
  """
  f1 = Figlet(font='standard')
  print(f1.renderText('xls2DBO'))

def main():
      
  show_title()

  parser = argparse.ArgumentParser()
  group = parser.add_mutually_exclusive_group()
  group.add_argument("-v", "--verbose", action="store_true", default=False, help="increase the verbosity level")
  parser.add_argument("-d", "--debug", action="store_true", default=False, help="print debug information")
  parser.add_argument("-i","--input", default="", help="input Excel sheet file name")

  args = parser.parse_args()

  if args.verbose:
    print("program arguments:")
    print(args)

  if os.path.exists(args.input):
    print("Started DBO building config generation ...")
    print("Creating DBO yaml file ...")
    DBOYAML(args.input).create_yaml_file()
    print("Done.")
  else:
    print("Please run ""%s -h"" to see the program options" % sys.argv[0])


if __name__ == "__main__":
  main()
