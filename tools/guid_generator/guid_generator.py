# Copyright 2022 Google LLC
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
from __future__ import print_function

from typing import Dict
import uuid
import strictyaml as syaml

from validate import instance_parser


class GuidGenerator(object):
  """Class for gnerator entity GUIDs."""

  def WriteYamlToFile(self, filename: str,
                      entity_yaml_dict: Dict[str, object]) -> None:
    """Converts a dictionary of entity instances to yaml file.

    Args:
      filename: Building Config instance name which is being validated.
      entity_yaml_dict: Dictionary with entity yaml blocks keyed by
      entity instance names.

    """
    try:
      with open(filename, 'w', encoding='utf-8') as file:
        file.write(syaml.as_document(entity_yaml_dict).as_yaml())
    except PermissionError:
      print(f'Permission denied when writing to {filename}')

  def GenerateGuids(self, file_path: str) -> None:
    """Generates GUIDs for all entities missing GUIDs.

    Args:
      file_path: A Building Configuration .yaml file path.
    """
    parser = instance_parser.InstanceParser()
    parser.AddFile(file_path)
    parser.Finalize()

    entity_yaml_dict = {}
    entity_yaml_dict['CONFIG_METADATA'] = {
        'operation': parser.GetConfigMode().value
    }
    for entity_name, entity_yaml in parser.GetEntities().items():
      if instance_parser.ENTITY_GUID_KEY not in entity_yaml.keys(
      ) or not entity_yaml[instance_parser.ENTITY_GUID_KEY]:
        entity_yaml[instance_parser.ENTITY_GUID_KEY] = str(uuid.uuid4())
      entity_yaml_dict[entity_name] = entity_yaml
      self.WriteYamlToFile(file_path, entity_yaml_dict)
