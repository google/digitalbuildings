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
"""A centralized runner for digitalbuildings/tools.

Toolkit.py is an argument parsing application allowing a user to setup and run
any of the tools within tools/. Currently, toolkit.py only supports the guid
generator and the instance validator.
"""

from __future__ import print_function

import argparse
import sys

from guid_generator import generator
from validate import handler

# Default timeout duration for telemetry validation test
DEFAULT_TIMEOUT = 600

# Default path to Digital Buildings Ontology
DEFAULT_ONTOLOGY_PATH = '../ontology/yaml/resources'


def _ParseArgs() -> argparse.ArgumentParser:
  """Generates an argument parser for user input.

  Returns:
    ArgumentParser object
  """
  parser = argparse.ArgumentParser()

  parser.add_argument(
      '-i',
      '--input',
      action='append',
      dest='filenames',
      required=True,
      help='Filepath(s) or directory path for Builcing Configurations',
      metavar='FILE')

  parser.add_argument(
      '-g',
      '--generate',
      action='store_true',
      dest='generate_guids',
      required=False,
      help='Provide this flag if GUIDs need to be generated')

  parser.add_argument(
      '-v',
      '--validate',
      action='store_true',
      dest='validate_instance',
      required=False,
      help='Provide this flag to validate a set if Building Configurations')

  parser.add_argument(
      '-m',
      '--modified-ontology-types',
      dest='modified_types_filepath',
      required=False,
      default=DEFAULT_ONTOLOGY_PATH,
      help='Filepath to modified type filepaths',
      metavar='MODIFIED_TYPE_FILEPATHS')

  parser.add_argument(
      '-s',
      '--subscription',
      dest='subscription',
      required=False,
      help='Pubsub subscription for telemetry to validate',
      metavar='subscription')

  parser.add_argument(
      '-a',
      '--service-account',
      dest='service_account',
      required=False,
      help='Service account used to pull messages from the subscription',
      metavar='service-account')

  parser.add_argument(
      '-t',
      '--timeout',
      dest='timeout',
      required=False,
      default=DEFAULT_TIMEOUT,
      help='Timeout duration (in seconds) for telemetry validation test',
      metavar='timeout')

  parser.add_argument(
      '-r',
      '--report-filename',
      dest='report_filename',
      required=False,
      default=None,
      help='Filename for the validation report',
      metavar='report-filename')

  parser.add_argument(
      '--udmi',
      dest='udmi',
      required=False,
      default=False,
      action='store_true',
      help='Parse messages as UDMI')

  return parser


if __name__ == '__main__':
  args = _ParseArgs().parse_args(sys.argv[1:])
  if args.generate_guids:
    filenames = generator.Generate(filenames=args.filenames)
  if args.validate_instance:
    handler.RunValidation(
        filenames=args.filenames,
        modified_types_filepath=args.modified_types_filepath,
        subscription=args.subscription,
        service_account=args.service_account,
        report_filename=args.report_filename,
        timeout=int(args.timeout),
        is_udmi=args.udmi)

