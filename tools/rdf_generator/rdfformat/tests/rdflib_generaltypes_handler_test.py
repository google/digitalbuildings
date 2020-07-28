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

"""Tests for generator.rdflib_generaltypes_handler_test."""
import rdflib

from rdfformat.generator import constants
from rdfformat.generator import rdf_helper
from rdfformat.generator import rdflib_generaltypes_handler
from rdfformat.generator import yaml_handler
from absl.testing import absltest


class RdfFunctionHandlerTest(absltest.TestCase):

  def testAbstractGraphGeneration(self):

    fake_general_types = 'fake_resources/GeneralTypes.yaml'

    file_contents = rdf_helper.ReadFile(fake_general_types)

    yaml_general_types = yaml_handler.ImportYamlFiles(file_contents)

    # Create global graph
    graph = rdflib.Graph()

    # Bind the OWL and Digital Buildings name spaces
    namespace_manager = rdflib.namespace.NamespaceManager(graph)
    namespace_manager.bind('owl', rdflib.OWL)
    namespace_manager.bind('db', constants.DIGITAL_BUILDINGS_NS)
    graph.namespace_manager = namespace_manager

    g_general_types = rdflib_generaltypes_handler.GenerateGraph(
        yaml_general_types, graph)

    # Check that the following are present
    # EQUIPMENT:
    # id: "9693662434551660544"
    # description: "A piece of equipment."
    # is_abstract: true
    # opt_uses:
    # - manufacturer_label
    # - model_label
    # VAV:
    # id: "6599610325710929920"
    # description: "Tag for terminal units with variable volume control."
    # is_abstract: true
    # implements:
    # - EQUIPMENT
    # opt_uses:
    # - zone_use_label
    equipment = rdflib.URIRef(constants.DIGITAL_BUILDINGS_NS['Equipment'])
    vav = rdflib.URIRef(constants.HVAC_NS['Vav'])
    vav_description = 'Tag for terminal units with variable volume control.'

    # Main Classes
    equipment_class = (equipment, rdflib.RDF.type, rdflib.OWL.Class)
    vav_class = (vav, rdflib.RDF.type, rdflib.OWL.Class)

    # Assertions
    # Class assertions
    self.assertIn(equipment_class, g_general_types)
    self.assertIn(vav_class, g_general_types)
    self.assertIn((vav, rdflib.RDFS.comment, rdflib.Literal(vav_description)),
                  g_general_types)

    # SubClasses assertions
    self.assertIn((vav, rdflib.RDFS.subClassOf, equipment), g_general_types)


if __name__ == '__main__':
  absltest.main()
