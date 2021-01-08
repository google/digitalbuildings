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

"""Parses and validates YAML instance files for syntax"""

from __future__ import print_function

import re
import strictyaml as syaml
import ruamel
import sys

_ENTITY_INSTANCE_REGEX = '^[A-Z][A-Z0-9\\-]+:'
_ENTITY_INSTANCE_PATTERN = re.compile(_ENTITY_INSTANCE_REGEX)

_IGNORE_PATTERN = re.compile(r'^(\W)*#|\n')
# number of entities to validate per batch
_ENTITIES_PER_BATCH = 1
_COMPLIANT_REGEX = u'^COMPLIANT$'
_TRANSLATION = 'translation'
_FIELD_REGEX = u'(^[a-z]+[a-z0-9]*(?:_[a-z]+[a-z0-9]*)*)((?:_[0-9]+)*)$'

"""Schema separately parses translation to account for multiple valid formats
github.com/google/digitalbuildings/blob/master/ontology/docs/building_config.md
#defining-translations"""
_TRANSLATION_SCHEMA = syaml.Regex(_COMPLIANT_REGEX) | syaml.MapPattern(
    syaml.Str(),
    syaml.Str() | syaml.Map({'present_value': syaml.Str(),
                             syaml.Optional('states'): syaml.MapPattern(
                                 syaml.Regex(u'^[A-Z_]'), syaml.Str()),
                             syaml.Optional('units'): syaml.Map(
                                 {'key': syaml.Str(),
                                  'values': syaml.MapPattern(syaml.Str(),
                                                             syaml.Str())
                                  }),
                             syaml.Optional('unit_values'): syaml.MapPattern(
                                 syaml.Str(), syaml.Str())
                             }))

"""strictyaml schema parses a YAML instance from its first level of keys
github.com/google/digitalbuildings/blob/master/ontology/docs/building_config.md
#config-format"""
_SCHEMA = syaml.MapPattern(syaml.Str(),
                           syaml.Map({
                               'type': syaml.Str(),
                               'id': syaml.Str(),
                               # TODO(b/166472270): revisit connection syntax
                               #  validation. Current code might not follow
                               #  the spec.
                               syaml.Optional('connections'): syaml.MapPattern(
                                   syaml.Str(), syaml.Str()) | syaml.Seq(
                                       syaml.MapPattern(syaml.Str(),
                                                        syaml.Str())),
                               syaml.Optional('links'): syaml.MapPattern(
                                   syaml.Str(),
                                   syaml.MapPattern(syaml.Regex(_FIELD_REGEX),
                                                    syaml.Regex(_FIELD_REGEX))),
                               syaml.Optional('translation'):
                                   _TRANSLATION_SCHEMA,
                               syaml.Optional('metadata'): syaml.Any()
                           }))


def _ValidateEntityWithSchema(content, schema):
  """Validates an entity instance based on a syaml-formatted YAML schema.

  Args:
    content: an entity instance in yaml format
    schema: YAML schema in syaml format

  Returns:
    Returns the parsed YAML data in a strictyaml-provided datastructure
    which is similar to a Python dictionary.
  """
  try:
    parsed = syaml.load(content, schema)
  except (ruamel.yaml.parser.ParserError,
          ruamel.yaml.scanner.ScannerError,
          syaml.exceptions.YAMLValidationError,
          syaml.exceptions.DuplicateKeysDisallowed,
          syaml.exceptions.InconsistentIndentationDisallowed) as exception:
    print(exception)
    sys.exit(0)

  return parsed


def _ValidateBlock(unvalidated_block, validated_blocks):
  """Validates a block of entities with the strictyaml schema and add them to
  the validated blocks.

  Args:
    unvalidated_block: string. A block of unvalidated entities
    validated_blocks: dictionary with entity name as key, entity as value.
     A block of validated entities

  Returns:
    a dictionary of validated entity blocks with strict yaml schema.
  """
  validated = _ValidateEntityWithSchema(unvalidated_block, _SCHEMA)
  validated_blocks.update(validated.data)

def ParseYaml(filename):
  """Loads an instance YAML file and parses it with
  multiple strictyaml-formatted YAML schemas. Expected format:
  github.com/google/digitalbuildings/blob/master/ontology/docs/
  building_config.md#config-format

  Args:
    filename: filepath location of the YAML file

  Returns:
    Returns the parsed YAML data in a strictyaml-provided datastructure
    which is similar to a Python dictionary.
  """
  print('Loading yaml file to validate with schema')
  entity_instance_block = ''
  found_entities = 0
  all_content = {}
  with open(filename) as file:
    for line in file:
      if _ENTITY_INSTANCE_PATTERN.match(line):
        # wait until entity instance block reaches _ENTITIES_PER_BATCH
        if found_entities > _ENTITIES_PER_BATCH:
          _ValidateBlock(entity_instance_block, all_content)
          entity_instance_block = ''
          found_entities = 0
        found_entities += 1
      else:
        if _IGNORE_PATTERN.match(line):
          continue
      entity_instance_block = entity_instance_block + line

  # handle the singleton case
  if found_entities > 0:
    _ValidateBlock(entity_instance_block, all_content)

  return all_content
