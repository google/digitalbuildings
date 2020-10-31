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

"""Standalone, interactive runner for Entity type validation."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from absl import app
from absl import flags

from yamlformat.validator import internal_file_lib
from yamlformat.validator import presubmit_validate_types_lib

FLAGS = flags.FLAGS

flags.DEFINE_string('input', None,
                    'The path of the directory of the yaml files')


def main(args):
  filter_text = None
  if len(args) >= 2:
    command = args[1]
    commands = command.split(':')
    if len(commands) == 2:
      if commands[0] == 'match':
        filter_text = commands[1].strip()

  # This is the typical usage for g3
  if FLAGS.input is None:
    # Get depot filepaths of all config files currently in g3.
    src_depot_paths = internal_file_lib.GetSrcDepotPaths(
        os.path.join('google3', internal_file_lib.RESOURCE_PATH))
    files_list = internal_file_lib.GetSrcAbsPaths(src_depot_paths)

  # Preparing another option for github export
  else:
    print('Input folder given:', FLAGS.input)
    print('Preparing to load files ...')
    src_depot_paths = set()
    for root, _, files in os.walk(FLAGS.input, followlinks=False):
      for yaml_file in files:
        if '.yaml' in yaml_file:
          src_depot_paths.add(os.path.join(root, yaml_file))
    files_list = internal_file_lib.GetSrcAbsPaths(src_depot_paths)

  return presubmit_validate_types_lib.RunInteractive(
      filter_text, modified_base=[], modified_client=files_list)


if __name__ == '__main__':
  app.run(main)
