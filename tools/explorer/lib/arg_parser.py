# Copyright 2021 Google LLC
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
"""Command line argument parser for ontology explorer."""

import argparse


def ParseArgs() -> argparse.ArgumentParser:
  """Generates an argument parser for user input.

  Returns:
    An instance of ArgumentParser class.
  """
  parser = argparse.ArgumentParser(
      description='Instantiate an ontology explorer')

  parser.add_argument(
      '-m',
      '--modified-ontology-types',
      dest='modified_types_filepath',
      required=False,
      help='Filepath to modified ontology filepaths',
      metavar='FILE')

  return parser
