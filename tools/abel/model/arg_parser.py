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
"""Command line argument parser for ABEL."""

import argparse


def ParseArgs() -> argparse.ArgumentParser:
  """Generates an argument parser for user input.

  Returns:
    An instance of ArgumentParser class.
  """
  parser = argparse.ArgumentParser(
      description='Instantiate an ABEL argument parser')

  parser.add_argument(
      '-t',
      '--token',
      dest='token',
      required=True,
      help='Path to GCP project token.')

  parser.add_argument(
      '-s',
      '--spreadsheet-id',
      dest='spreadsheet_id',
      required=True,
      help='Google sheets spreadsheet ID.',
      metavar='STRING')

  parser.add_argument(
      '-b',
      '--building-config',
      dest='building_config',
      required=False,
      help='Filepath to Building Configuration YAML file.',
      metavar='FILE')

  return parser
