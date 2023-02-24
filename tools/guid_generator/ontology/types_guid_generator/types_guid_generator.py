# Copyright 2023 Google LLC
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

"""GUID generator runner for entity types ontology YAML files."""

from __future__ import print_function

import argparse
import sys
from typing import List
import uuid
import yaml

from yamlformat.validator import parse_config_lib


def GenerateGuids(file_paths: List[str]) -> None:
  """Runner method for GUID generation.

  Args:
    file_paths: file paths for entity types ontology YAML files
  """
  for file_path in file_paths:
    print(f'Generating GUIDs for {file_path}')
    file_contents = []
    types_missing_guid = set()
    with open(file_path, encoding='utf-8') as file:
      for line in file:
        file_contents.append(line)
    with open(file_path, encoding='utf-8') as file:
      document = yaml.load(file, Loader=parse_config_lib.UniqueKeyLoader)
      for entity_type in document:
        if 'guid' not in document[entity_type]:
          types_missing_guid.add(entity_type)

    # Write all original file content with added GUIDs.
    with open(file_path, 'w', encoding='utf-8') as file:
      for line in file_contents:
        file.write(line)
        if not line.startswith('  ') and line.endswith(':\n'):
          type_name = line[:-2]
          if type_name in types_missing_guid:
            file.write(f'  guid: "{str(uuid.uuid4())}"\n')


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument(
      '-f',
      '--files',
      action='append',
      dest='filenames',
      required=True,
      help='Filepath(s) of modified entity type ontology YAML file(s)',
      metavar='FILE',
  )
  args = parser.parse_args(sys.argv[1:])
  GenerateGuids(args.filenames)
