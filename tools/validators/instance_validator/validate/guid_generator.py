# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the License);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an AS IS BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""GUID generator."""

from typing import List, Dict
import uuid
import strictyaml as syaml

from validate import instance_parser


class GuidGenerator(object):
  """Class for gnerator entity GUIDs."""

  def __init__(self):
    pass

  def WriteYamlToFile(self, filename: str,
                      entity_yaml_list: List[Dict[str, str]]) -> None:
    """Converts list of python dictionaries to yaml document and writes to a file.

    Args:
      filename: Building Config instance name which is being validated.
      entity_yaml_list: list of python dictionaries representing entities to be
        converted to yaml document.
    """
    for entity_yaml in entity_yaml_list:
      try:
        with open(filename, 'w', encoding='utf-8') as file:
          file.write(syaml.as_document(entity_yaml).as_yaml())
      except PermissionError:
        print(f'Permission denied when writing to {filename}')

  def GenerateGuids(self, yaml_files: List[str]) -> None:
    """Generates GUIDs for all entities missing GUIDs.

    Args:
      yaml_files: list of building config .yaml file paths
    """
    for yaml_file in yaml_files:
      parser = instance_parser.InstanceParser()
      parser.AddFile(yaml_file)
      parser.Finalize()

      entity_yaml_list = []
      for entity_yaml in parser.GetEntities().values():
        if instance_parser.ENTITY_GUID_KEY not in entity_yaml.keys(
        ) or not entity_yaml[instance_parser.ENTITY_GUID_KEY]:
          entity_yaml[instance_parser.ENTITY_GUID_KEY] = str(uuid.uuid4())
        entity_yaml_list.append(entity_yaml)
      self.WriteYamlToFile(yaml_file, entity_yaml_list)
