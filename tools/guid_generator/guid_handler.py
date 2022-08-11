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

from typing import Any, Dict
import uuid
import strictyaml as syaml

from validate import instance_parser


class GuidGenerator(object):
  """Class for generator entity GUIDs."""

  @staticmethod
  def WriteYamlToFile(filename: str, entity_yaml_dict: Dict[str,
                                                            object]) -> None:
    """Converts a dictionary of entity instances to yaml file.

    Args:
      filename: path to import/export building config yaml file; input building
      config file is overwritten with entities keyed by guid.
      entity_yaml_dict: Dictionary with entity yaml blocks keyed by entity
        instance code or GUID.
    """
    try:
      with open(filename, 'w', encoding='utf-8') as file:
        file.write('')
      with open(filename, 'a', encoding='utf-8') as file:
        for entity_key, entity_block in entity_yaml_dict.items():
          file.write(syaml.as_document({entity_key: entity_block}).as_yaml())
          file.write('\n')
    except PermissionError:
      print(f'Permission denied when writing to {filename}')

  @classmethod
  def GenerateGuids(cls, file_path: str) -> None:
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
    code_to_guid_map: Dict[str, str] = {}
    guid_key_entities: Dict[str, Any] = {}
    code_key_entities: Dict[str, Any] = {}
    for entity_key, entity_yaml in parser.GetEntities().items():
      entity_code: str = None
      entity_guid: str = None
      if instance_parser.ENTITY_CODE_KEY in entity_yaml.keys():
        # New format with GUID as key and a code attribute.
        entity_code = entity_yaml[instance_parser.ENTITY_CODE_KEY]
        entity_guid = entity_key
        guid_key_entities[entity_guid] = entity_yaml
      else:
        # Old format with code as key and a GUID attribute.
        entity_code = entity_key
        if not entity_yaml.get(instance_parser.ENTITY_GUID_KEY):
          entity_yaml[instance_parser.ENTITY_GUID_KEY] = str(uuid.uuid4())
        entity_guid = entity_yaml[instance_parser.ENTITY_GUID_KEY]
        code_key_entities[entity_code] = entity_yaml
      code_to_guid_map[entity_code] = entity_guid

    # If the document is entirely the new format already, do nothing.
    if not code_key_entities:
      return
    # If the document contains any entities in the GUID-based format, all
    # entities must be converted to that format in the output.
    if code_key_entities:
      entity_yaml_dict.update(guid_key_entities)
      for entity_code, entity_yaml in code_key_entities.items():
        entity_guid = entity_yaml[instance_parser.ENTITY_GUID_KEY]
        cls._ConvertEntityToGuidFormat(entity_code, entity_yaml,
                                       code_to_guid_map)
        entity_yaml_dict[entity_guid] = entity_yaml
    else:
      entity_yaml_dict.update(code_key_entities)

    cls.WriteYamlToFile(file_path, entity_yaml_dict)

  @staticmethod
  def _ConvertEntityToGuidFormat(entity_code: str, entity_yaml: Dict[str, Any],
                                 code_to_guid_map: Dict[str, str]) -> None:
    """Converts an entity from code-based to GUID-based format."""
    del entity_yaml[instance_parser.ENTITY_GUID_KEY]
    entity_yaml[instance_parser.ENTITY_CODE_KEY] = entity_code

    if instance_parser.CONNECTIONS_KEY in entity_yaml:
      old_connections = entity_yaml[instance_parser.CONNECTIONS_KEY].items()
      new_connections = {}
      for source_entity_code, connection_type in old_connections:
        source_entity_guid = code_to_guid_map.get(source_entity_code,
                                                  source_entity_code)
        new_connections[source_entity_guid] = connection_type
      entity_yaml[instance_parser.CONNECTIONS_KEY] = new_connections

    if instance_parser.LINKS_KEY in entity_yaml:
      old_links = entity_yaml[instance_parser.LINKS_KEY].items()
      new_links = {}
      for source_entity_code, field_map in old_links:
        source_entity_guid = code_to_guid_map.get(source_entity_code,
                                                  source_entity_code)
        new_links[source_entity_guid] = field_map
      entity_yaml[instance_parser.LINKS_KEY] = new_links
