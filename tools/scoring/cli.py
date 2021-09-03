# Inputs/Output
# The tool should accept four sets of files, specified at the command line:
# Digital Building Ontology Ontology files (from github)
# Known good Building Configuration file
# Building Configuration to be scored
# Local type additions to DBO (in YAML, similar to the ontology)
# The tool must produce a matrix of scores along the dimensions described in scoring detail.  Output should be trivially importable into Google Sheets.
# Integration
# The new functionality should take advantage of existing code for reading and validating inputs wherever possible.

import argparse
import sys
from os import path

from results import Results

print('Let\'s get you a score…')


def _ParseArgs() -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser(description='Score an instance')

    parser.add_argument(
        '-ont',
        '--ontology',
        dest='ontology',
        required=False,
        default='/Users/atom/Documents/work/digitalbuildings/ontology/yaml',
        help='Absolute path for the directory which contains your ontology',
        metavar='ontology')

    parser.add_argument('-sol',
                        '--solution',
                        dest='solution',
                        required=True,
                        help='Absolute path for your solution instance file',
                        metavar='solution')

    parser.add_argument(
        '-prop',
        '--proposed',
        dest='proposed',
        required=True,
        help='Absolute path for your proposed instance file (to be scored)',
        metavar='proposed')

    parser.add_argument(
        '-add',
        '--additions',
        dest='additions',
        required=False,
        default='/Users/atom/Documents/work/digitalbuildings/ontology/yaml',
        help='Type additions',
        metavar='additions')

    # parser.add_argument(
    #   '-v',
    #   '--verbose',
    #   dest='verbose',
    #   required=False,
    #   default=False,
    #   help='',
    #   metavar='verbose')

    # parser.add_argument(
    #   # '-out',
    #   '--output',
    #   dest='output',
    #   required=False,
    #   default='object',
    #   help='Output format',
    #   metavar='output')

    return parser


if __name__ == '__main__':
    args = _ParseArgs().parse_args(sys.argv[1:])
    Results(args.ontology, args.solution, args.proposed, args.additions)
