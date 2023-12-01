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

"""Standalone, rdf generator from ontology yaml files."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import ast
from os import path
import sys

from yamlformat.arg_parser import CreateParser
from yamlformat.validator import external_file_lib


def main(parsed_args: argparse.ArgumentParser):
  filter_text = None
  if len(sys.argv[1:]) >= 2:
    command = sys.argv[1]
    commands = command.split(':')
    if len(commands) == 2:
      if commands[0] == 'match':
        filter_text = commands[1].strip()

  modified_types_filepath = parsed_args.modified_types_filepath
  if modified_types_filepath is not None:
    modified_types_filepath = path.expanduser(
        parsed_args.modified_types_filepath)

  print('Starting Yaml Validator!')
  external_file_lib.Validate(
      filter_text,
      path.expanduser(parsed_args.original),
      modified_types_filepath,
      interactive=ast.literal_eval(parsed_args.interactive),
      require_type_guids=not parsed_args.allow_missing_type_guids)

if __name__ == '__main__':
  args = CreateParser().parse_args(sys.argv[1:])
  main(args)
