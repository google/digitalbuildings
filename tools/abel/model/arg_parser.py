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
"""Command line argument parser for ABEL."""

import argparse
import os

# pylint: disable=g-importing-member
from validate.constants import DEFAULT_TIMEOUT


def ParseArgs() -> argparse.ArgumentParser:
  """Generates an argument parser for user input.

  Returns:
    An instance of ArgumentParser class.
  """
  parser = argparse.ArgumentParser(
      description='Instantiate an ABEL argument parser'
  )

  parser.add_argument(
      '-m',
      '--modified-ontology-types',
      dest='modified_types_filepath',
      required=False,
      help='Filepath to modified type filepaths',
      metavar='MODIFIED_TYPE_FILEPATHS',
  )

  parser.add_argument(
      '-c',
      '--credential',
      dest='credential',
      required=True,
      default=None,
      help='Path to GCP oauth client credential',
  )

  parser.add_argument(
      '-s',
      '--spreadsheet-id',
      dest='spreadsheet_id',
      required=False,
      help='Google sheets spreadsheet ID.',
      metavar='STRING',
  )

  parser.add_argument(
      '-b',
      '--building-config',
      dest='building_config',
      required=False,
      help='Filepath to Building Configuration YAML file.',
      metavar='FILE',
  )

  parser.add_argument(
      '-p',
      '--subscription',
      dest='subscription',
      required=False,
      help='Pubsub subscription for telemetry to validate',
      metavar='subscription',
  )

  parser.add_argument(
      '-a',
      '--service-account',
      dest='service_account',
      required=False,
      help='Service account used to pull messages from the subscription',
      metavar='service-account',
  )

  parser.add_argument(
      '-o',
      '--timeout',
      dest='timeout',
      required=False,
      default=DEFAULT_TIMEOUT,
      help='Timeout duration (in seconds) for telemetry validation test',
      metavar='timeout',
  )

  parser.add_argument(
      '-d',
      '--output-dir',
      dest='output_dir',
      required=False,
      default=os.getcwd(),
      help=(
          'Absolute or relative path to a directory for output files to be'
          ' written to'
      ),
      metavar='output-directory',
  )

  return parser
