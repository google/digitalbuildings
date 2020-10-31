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

"""Standalone, rdf generator from ontology yaml files."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from os import path

from absl import app
from absl import flags

from yamlformat.validator import external_file_lib

FLAGS = flags.FLAGS

flags.DEFINE_string('changed', None, 'The path of the changed files')
flags.DEFINE_string('original', None, 'The path of the original files')
flags.DEFINE_boolean('interactive', True, 'interactive mode')

def main(args):
  filter_text = None
  if len(args) >= 2:
    command = args[1]
    commands = command.split(':')
    if len(commands) == 2:
      if commands[0] == 'match':
        filter_text = commands[1].strip()

  changed = FLAGS.changed
  if changed is not None:
    changed = path.expanduser(FLAGS.changed)

  print('Starting Yaml Validator!')
  external_file_lib.Validate(filter_text, path.expanduser(FLAGS.original),
                             changed, interactive=FLAGS.interactive)


if __name__ == '__main__':
  flags.mark_flag_as_required('original')
  app.run(main)
