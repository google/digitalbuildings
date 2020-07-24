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

"""Tests for generator.rdflib_carson_types_handler."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import rdflib
from rdflib import namespace

from rdfformat.generator import constants
from rdfformat.generator import rdf_helper
from rdfformat.generator import rdflib_carson_types_handler
from rdfformat.generator import yaml_handler
from absl.testing import absltest


class RdfCarsonTypesHandlerTest(absltest.TestCase):

  def testFacilitiesGraphGeneration(self):

    fake_fans = 'fake_resources/FAN.yaml'

    file_contents = rdf_helper.ReadFile(fake_fans)

    yaml_fans = yaml_handler.ImportYamlFiles(file_contents)

    # Create global graph
    graph = rdflib.Graph()

    # Bind the OWL and Digital Buildings name spaces
    namespace_manager = namespace.NamespaceManager(graph)
    namespace_manager.bind('owl', rdflib.OWL)
    namespace_manager.bind('db', constants.DIGITAL_BUILDINGS_NS)
    graph.namespace_manager = namespace_manager

    g_fan = rdflib_carson_types_handler.GenerateGraph(yaml_fans, graph,
                                                      constants.HVAC_NS)

    # Main Types
    fan_ss_refm_csp = rdflib.URIRef(constants.HVAC_NS['Fan_ss_refm_csp'])
    fan_s_vscf = rdflib.URIRef(constants.HVAC_NS['Fan_s_vscf'])
    fan_ss_ffb = rdflib.URIRef(constants.HVAC_NS['Fan_ss_ffb'])

    # Main Classes
    fan_ss_refm_csp_class = (fan_ss_refm_csp, rdflib.RDF.type, rdflib.OWL.Class)
    fan_s_vscf_class = (fan_s_vscf, rdflib.RDF.type, rdflib.OWL.Class)
    fan_ss_ffb_class = (fan_ss_ffb, rdflib.RDF.type, rdflib.OWL.Class)

    # Assertions
    # Class assertions
    self.assertIn(fan_ss_refm_csp_class, g_fan)

    # Should not be created
    self.assertIsNot(fan_s_vscf_class, g_fan)
    self.assertIsNot(fan_ss_ffb_class, g_fan)


if __name__ == '__main__':
  absltest.main()
