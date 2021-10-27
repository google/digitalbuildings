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

"""Argument Parser for ontology files."""

import argparse


def CreateParser() -> argparse.ArgumentParser:
  """Generates an argument parser for user input.

  Returns:
    ArgumentParser instance
  """
  parser = argparse.ArgumentParser(
      description='Validate a library of yaml files defining DBO'
  )

  parser.add_argument(
      '-m',
      '--modified-ontology-types',
      dest='modified_types_filepath',
      default=None,
      help='Modified ontology types filepath',
      required=False,
      metavar='MODIFIED_TYPE_FILEPATH'
  )

  parser.add_argument(
      '-o',
      '--original',
      dest='original',
      default=None,
      help='path of the original ontology files',
      required=True,
      metavar='ORIGINAL_FILE_PATH'
  )

  parser.add_argument(
      '-i',
      '--interactive',
      dest='interactive',
      default=False,
      help='interactive mode',
      required=False,
      metavar='interactive mode'
  )

  return parser

