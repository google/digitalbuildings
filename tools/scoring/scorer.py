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
"""Command line interface and entry point for the configuration scoring tool."""

import argparse
import sys
import pprint

from score import parse_config


def parse_args() -> argparse.ArgumentParser:

  parser = argparse.ArgumentParser(description='Score a configuration')

  parser.add_argument(
      '-ont',
      '--ontology',
      dest='ontology',
      required=True,
      help='Absolute path for the directory which contains your ontology',
      metavar='ontology')

  parser.add_argument('-sol',
                      '--solution',
                      dest='solution',
                      required=True,
                      help='Absolute path for your solution configuration file',
                      metavar='solution')

  parser.add_argument(
      '-prop',
      '--proposed',
      dest='proposed',
      required=True,
      help='Absolute path for your proposed configuration file (to be scored)',
      metavar='proposed')

  parser.add_argument(
      '-v',
      '--verbose',
      dest='verbose',
      required=False,
      default=False,
      # Defining booleans in argparse is not intuitive!
      type=lambda x: (str(x).lower() in ['true', '1', 'yes']),
      help='Output additional details about the scoring process',
      metavar='verbose')

  return parser


if __name__ == '__main__':
  pp = pprint.PrettyPrinter()
  # pylint: disable=too-many-function-args
  args = parse_args().parse_args(sys.argv[1:])
  scorer = parse_config.ParseConfig(ontology=args.ontology,
                                    solution=args.solution,
                                    proposed=args.proposed,
                                    verbose=args.verbose)
  pp.pprint(scorer.execute())
