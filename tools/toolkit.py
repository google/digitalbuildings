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

toolkit.py is an argument parsing CLI application allowing a user to set up and run
tools like the GUID generator and the instance validator.
"""

from __future__ import print_function

import argparse
import os
import sys
import logging

from guid_generator.instance.instance_guid_generator import generator
from validate import handler

# Default timeout duration for telemetry validation test
DEFAULT_TIMEOUT = 600

# Default path to Digital Buildings Ontology
DEFAULT_ONTOLOGY_PATH = '../ontology/yaml/resources'

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')


def _parse_args() -> argparse.ArgumentParser:
    """Generates an argument parser for user input."""
    parser = argparse.ArgumentParser(
        description="Digital Buildings Toolkit - Run GUID generator or validator",
        epilog="""
Examples:
  python toolkit.py -i my_config.yaml -g
  python toolkit.py -i my_config.yaml -v -s my-sub -c credentials.json
""",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '--version',
        action='version',
        version='Digital Buildings Toolkit 1.0',
        help='Show the version and exit',
    )

    parser.add_argument(
        '-i', '--input',
        action='append',
        dest='filenames',
        required=True,
        help='Filepath(s) or directory path(s) for Building Configurations',
        metavar='FILE',
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '-g', '--generate',
        action='store_true',
        dest='generate_guids',
        help='Generate GUIDs for provided configuration files',
    )
    group.add_argument(
        '-v', '--validate',
        action='store_true',
        dest='validate_instance',
        help='Validate a set of Building Configuration files',
    )

    parser.add_argument(
        '-m', '--modified-ontology-types',
        dest='modified_types_filepath',
        required=False,
        default=None,
        help='Filepath to modified ontology types (if any)',
        metavar='MODIFIED_TYPES',
    )

    parser.add_argument(
        '-s', '--subscription',
        dest='subscription',
        required=False,
        help='PubSub subscription name for telemetry validation',
        metavar='SUBSCRIPTION',
    )

    parser.add_argument(
        '-c', '--credential',
        dest='gcp_credential',
        required=False,
        help='GCP service account credential file for PubSub access',
        metavar='GCP_CREDENTIAL',
    )

    parser.add_argument(
        '-t', '--timeout',
        dest='timeout',
        required=False,
        default=DEFAULT_TIMEOUT,
        help='Timeout (in seconds) for telemetry validation',
        metavar='TIMEOUT',
        type=int,
    )

    parser.add_argument(
        '-d', '--report-directory',
        dest='report_directory',
        required=False,
        default=None,
        help='Directory to output validation and telemetry reports',
        metavar='REPORT_DIRECTORY',
    )

    parser.add_argument(
        '--udmi',
        dest='udmi',
        action='store_true',
        default=False,
        help='Parse telemetry messages using UDMI format',
    )

    return parser


def _validate_files(filenames):
    """Check that all provided file/directory paths exist."""
    for path in filenames:
        if not os.path.exists(path):
            logging.error(f"❌ File or directory not found: {path}")
            sys.exit(1)


def main():
    args = _parse_args().parse_args(sys.argv[1:])

    # Validate input paths
    _validate_files(args.filenames)

    try:
        if args.generate_guids:
            logging.info("🔧 Generating GUIDs...")
            generator.Generate(filenames=args.filenames)
            logging.info("✅ GUID generation completed successfully.")

        elif args.validate_instance:
            logging.info("🔍 Running instance validation...")
            handler.RunValidation(
                filenames=args.filenames,
                modified_types_filepath=args.modified_types_filepath,
                default_types_filepath=DEFAULT_ONTOLOGY_PATH,
                subscription=args.subscription,
                gcp_credential_path=args.gcp_credential,
                report_directory=args.report_directory,
                timeout=args.timeout,
                is_udmi=args.udmi,
            )
            logging.info("✅ Validation completed successfully.")

    except Exception as e:
        logging.error(f"❗ An error occurred: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
