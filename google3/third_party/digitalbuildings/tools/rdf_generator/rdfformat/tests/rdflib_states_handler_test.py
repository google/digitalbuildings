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

"""Tests for generator.rdflib_states_handler."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import rdflib
from rdflib import namespace

from rdfformat.generator import constants
from rdfformat.generator import rdf_helper
from rdfformat.generator import rdflib_states_handler
from rdfformat.generator import yaml_handler
from absl.testing import absltest


class RdfStatesHandlerTest(absltest.TestCase):

  def testStatesGraphGeneration(self):

    fake_states = 'fake_resources/states.yaml'

    file_contents = rdf_helper.ReadFile(fake_states)

    yaml_states = yaml_handler.ImportYamlFiles(file_contents)

    # Create global graph
    graph = rdflib.Graph()

    # Bind the OWL and Digital Buildings name spaces
    namespace_manager = namespace.NamespaceManager(graph)
    namespace_manager.bind('owl', rdflib.OWL)
    namespace_manager.bind('db', constants.DIGITAL_BUILDINGS_NS)
    graph.namespace_manager = namespace_manager

    g_states = rdflib_states_handler.GenerateGraph(yaml_states, graph)

    # Main Types
    state = rdflib.URIRef(constants.STATES_NS['State'])
    on = rdflib.URIRef(constants.STATES_NS['On'])
    off = rdflib.URIRef(constants.STATES_NS['Off'])
    on_desc = 'Powered on.'

    # Main Classes
    state_class = (state, rdflib.RDF.type, rdflib.OWL.Class)
    on_class = (on, rdflib.RDF.type, rdflib.OWL.Class)
    off_class = (off, rdflib.RDF.type, rdflib.OWL.Class)

    # Assertions
    # Class assertions
    self.assertIn(state_class, g_states)
    self.assertIn(on_class, g_states)
    self.assertIn(off_class, g_states)

    # SubClasses assertions
    self.assertIn((state, rdflib.RDFS.subClassOf, rdflib.OWL.Thing), g_states)
    self.assertIn((on, rdflib.RDFS.subClassOf, state), g_states)
    self.assertIn((off, rdflib.RDFS.subClassOf, state), g_states)

    # Relations assertions
    self.assertIn((on, rdflib.RDFS.comment, rdflib.Literal(on_desc)), g_states)


if __name__ == '__main__':
  absltest.main()
