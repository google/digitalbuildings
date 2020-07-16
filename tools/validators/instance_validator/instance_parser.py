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

import strictyaml as syaml

_COMPLIANT = 'COMPLIANT'
_TRANSLATION = 'translation'

"""Schema separately parses translation to account for multiple valid formats
github.com/google/digitalbuildings/blob/master/ontology/docs/building_config.md#defining-translations"""
_TRANSLATION_SCHEMA = syaml.Str() | syaml.Any()

# TODO check valid ontological content in next validation steps
"""strictyaml schema parses a YAML instance from its first level of keys
github.com/google/digitalbuildings/blob/master/ontology/docs/building_config.md#config-format"""
_SCHEMA = syaml.MapPattern(syaml.Str(),
                           syaml.Map({
                               'type': syaml.Str(),
                               'id': syaml.Str(),
                               syaml.Optional('connections'):
                               syaml.MapPattern(syaml.Str(),
                                                syaml.Str()) |
                               syaml.Seq(
                                   syaml.MapPattern(syaml.Str(),
                                                    syaml.Str())),
                               syaml.Optional('links'): syaml.MapPattern(
                                   syaml.Str(),
                                   syaml.MapPattern(syaml.Str(), syaml.Str())),
                               syaml.Optional('translation'): syaml.Any(),
                               syaml.Optional('metadata'): syaml.Any()
                               }))

# TODO add manual check to de-duplicate units/unit_values/states
# TODO add all units/unit_values/states to translation_data_schema
"""Further account for multiple valid translation formats
github.com/google/digitalbuildings/blob/master/ontology/docs/building_config.md#defining-translations"""
_TRANSLATION_DATA_SCHEMA = syaml.Str() | syaml.Map({
    'present_value': syaml.Str(),
    syaml.Optional('states'): syaml.MapPattern(syaml.Str(), syaml.Str()),
    syaml.Optional('units'): syaml.Map({
        'key': syaml.Str(),
        'values': syaml.MapPattern(syaml.Str(), syaml.Str())
    }),
    syaml.Optional('unit_values'): syaml.MapPattern(syaml.Str(), syaml.Str())
    })

def _load_yaml_with_schema(filepath, schema):
  """Loads an instance YAML file and parses
  it based on a syaml-formatted YAML schema.

  Args:
    filepath: filepath location of the YAML file
    schema: YAML schema in syaml format

  Returns:
    Returns the parsed YAML data in a stricyaml-provided
    datastructure which is similar to a Python dictionary.
  """
  yaml_file = open(filepath)
  content = yaml_file.read()
  yaml_file.close()

  try:
    parsed = syaml.load(content, schema)

    return parsed
  except Exception:
    return None

def parse_yaml(filename):
  """Loads an instance YAML file and parses it with
  multiple strictyaml-formatted YAML schemas. Expected format:
  github.com/google/digitalbuildings/blob/master/ontology/docs/building_config.md#config-format

  Args:
    filename: filepath location of the YAML file

  Returns:
    Returns the parsed YAML data in a stricyaml-provided
    datastructure which is similar to a Python dictionary.
  """
  yaml = _load_yaml_with_schema(filename, _SCHEMA)

  if yaml is None:
    return None

  top_name = yaml.keys()[0]

  if _TRANSLATION in yaml[top_name].keys():
    translation = yaml[top_name][_TRANSLATION]
    translation.revalidate(_TRANSLATION_SCHEMA)

    # TODO can this be automatically verified based on ontology?
    # if translation is not UDMI compliant
    if translation.data != _COMPLIANT:
      translation_keys = translation.keys()

      for key in translation_keys:
        translation[key].revalidate(_TRANSLATION_DATA_SCHEMA)

  return yaml
