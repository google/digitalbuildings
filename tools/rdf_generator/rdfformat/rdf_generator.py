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

from rdfformat.generator import rdf_manager

FLAGS = flags.FLAGS

flags.DEFINE_string('output', None, 'The path of the output file')
flags.DEFINE_string('input', None, 'The path of the input file')


def main(unused_argv):
  del unused_argv  # Unused.
  print('Starting RDF Extractor!')
  graph = rdf_manager.Generate(path.expanduser(FLAGS.input))
  rdf_manager.SerializeToFile(graph, path.expanduser(FLAGS.output))
  print('RDF File generated:', path.expanduser(FLAGS.output))


if __name__ == '__main__':
  flags.mark_flag_as_required('output')
  flags.mark_flag_as_required('input')
  app.run(main)
