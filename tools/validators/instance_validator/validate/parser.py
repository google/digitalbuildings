import jsonschema
import json
import os
import re
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012
from typing import Dict, Tuple, Any, List
import uuid
import yaml

from validate import enumerations
from validate import entity_instance
from validate import schema

try:
  from yaml import CLOader as Loader, CDumper as Dumper
except ImportError:
  from yaml import Loader, Dumper

_ENTITY_CODE_REGEX = r'^[a-zA-Z][a-zA-Z0-9/\-_ ]+:'
_ENTITY_GUID_REGEX = r'^[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}:'
_ENTITY_CODE_PATTERN = re.compile(_ENTITY_CODE_REGEX)
_ENTITY_GUID_PATTERN = re.compile(_ENTITY_GUID_REGEX)

# Exact key for the configuration metadata block
_CONFIG_METADATA_KEY = 'CONFIG_METADATA'
_CONFIG_METADATA_REGEX = f'^{_CONFIG_METADATA_KEY}:'
_CONFIG_METADATA_PATTERN = re.compile(_CONFIG_METADATA_REGEX)
_SCHEMA_ID = '$id'

class Parser(object):
  """A simple parser for building config yaml files.

  Attributes:
    config_mode: An instance of ConfigMode enumeration.
  """

  def __init__(self, schema_folder):
    """Init.
    Args:
      schema_folder: Absolute path to a folder of json schema files.
    """
    self.config_mode = enumerations.ConfigMode.EXPORT
    self.schema_folder = schema_folder

  def GetDefaultEntityOperation(self) -> enumerations.EntityOperation:
    """Returns the default EntityOperation for the ConfigMode."""
    if self.config_mode == enumerations.ConfigMode.EXPORT:
      return enumerations.EntityOperation.EXPORT
    elif self.config_mode == enumerations.ConfigMode.UPDATE:
      return enumerations.EntityOperation.EXPORT
    elif self.config_mode == enumerations.ConfigMode.INITIALIZE:
      return enumerations.EntityOperation.ADD

  def _CreateSchemaRegistry(self) -> Registry:
    resources = []
    for root, dir_names, filenames in os.walk(os.path.abspath(self.schema_folder)):
        for file in filenames:
            with open(os.path.abspath(os.path.join(root, file)), 'r') as f:
                parsed_json = json.loads(f.read())
                new_resource = Resource.from_contents(parsed_json)
                resources.append((file, new_resource))
    return Registry().with_resources(pairs=resources)


  def _ValidateMetadataSchema(self, metadata_block: Dict[str, Any]) -> bool:
    """Helper function to validate a building config's CONFIG METADATA block.

    Args:
      metadata_block: Dictionary mapping for a building config CONFIG METADATA block.

    Returns:
      a boolean representing if the metadata has been validated? is valid?
    """
    with open(os.path.abspath(os.path.join(self.schema_folder, 'config-metadata.schema.json')), 'r') as f:
      config_metadata_schema = json.loads(f.read())
    try:
      jsonschema.validate(instance=metadata_block, schema=config_metadata_schema)
      self.config_mode = enumerations.ConfigMode(metadata_block.get('operation'))
    except jsonschema.ValidationError as ve:
      print('CONFIG_METADATA is invalid')
      print(ve)
      return False
    except ValueError:
      print('CONFIG_METADATA operation invalid. Operation must be one of INITIALIZE, EXPORT, UPDATE')
      return False
    return True


  def _ValidateEntityInstance(self, guid: str, config_dict: Dict[str, Any], validator: jsonschema.Draft202012Validator) -> bool:
    """Helper function to validate a building config schema using jsonschema.

    Args:
      config_dict: A parsed dictionary representation of a building config yaml file.
      validator:

    Returns:
      a boolean indicating whether the block is valid
    """
    try:
      validator.validate(instance=config_dict)
    except jsonschema.ValidationError as ve:
      print(ve)
      return False
    return True


  def Deserialize(self, yaml_files: List[str]) -> Tuple[Dict[uuid.UUID, entity_instance.EntityInstance], enumerations.ConfigMode]:
    """New deserialize logic that uses pyyaml and jsonschema rather than strictyaml.

    Steps:
      1. Parse yaml file
      2. need to validate block by block
      3. separate out config metadata and validate
      4. For each block, ensure it matches one of the entity block schemas defined in schema.

    Args:
      yaml_files: A list of absolute paths for a collection of building config files.

    Returns:
      A tuple containing a dictionary mapping of uuid objects to entity instances
      and the building config's config mode.
    """

    for yaml_file in yaml_files:
      absolute_bc_path = os.path.expanduser(yaml_file)
      with open(absolute_bc_path) as f:
        yaml_dict = yaml.load(f.read(), Loader=Loader)

      # Fix metadata validation here
      # Enforce the existence opf
      metadata_block = yaml_dict.get(_CONFIG_METADATA_KEY)
      if not metadata_block:
        raise KeyError('[ERROR]\tBuilding config must contain CONFIG_METADATA')
      else:
        self._ValidateMetadataSchema(metadata_block)
        del yaml_dict[_CONFIG_METADATA_KEY]

      with open(os.path.abspath(os.path.join(self.schema_folder, 'entity-block-schema.schema.json')), 'r') as f:
        entity_block_schema = json.loads(f.read())
      try:
        jsonschema.Draft202012Validator.check_schema(schema=entity_block_schema)
      except jsonschema.SchemaError as schema_error:
        raise schema_error
      validator = jsonschema.Draft202012Validator(schema=entity_block_schema, registry=self._CreateSchemaRegistry())

      return_dict = {}
      for guid, entity_yaml in yaml_dict.items():
        if guid == _CONFIG_METADATA_KEY:
          raise jsonschema.ValidationError('Cannot have more than one config metadata block!')
        default_entity_operation = self.GetDefaultEntityOperation()
        is_valid = False
        try:
          valid_uuid = uuid.UUID(guid)
        except ValueError:
          # Great spot to append to a log here
          print('Not a valid guid')
          continue
        is_valid = self._ValidateEntityInstance(guid, entity_yaml, validator)
        if is_valid:
          entity = entity_instance.EntityInstance.FromYaml(
            str(valid_uuid), entity_yaml, default_entity_operation
          )
          return_dict.update({valid_uuid: entity})
      return return_dict, self.config_mode