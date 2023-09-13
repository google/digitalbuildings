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
"""Main module for DBO explorer."""

import sys

# pylint: disable=g-importing-member
from model.arg_parser import ParseArgs
from model.workflow import Workflow


def main(parsed_args: ParseArgs) -> None:
  print(
      '\nHow would you like to use ABEL?\n'
      + '1: Modify a spreadsheet/building config for an existing building\n'
      + '2: Create a spreadsheet for a new building\n'
      + 'q: quit\n'
  )
  function_choice = input('Please select an option: ')
  new_workflow = Workflow(parsed_args)
  if function_choice == '1':
    new_workflow.UpdateWorkflow()
  elif function_choice == '2':
    new_workflow.InitWorkflow()


if __name__ == '__main__':
  args = ParseArgs().parse_args(sys.argv[1:])
  main(args)
