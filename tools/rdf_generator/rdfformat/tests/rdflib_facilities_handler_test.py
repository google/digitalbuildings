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

"""Tests for generator.rdf_facilities_handler."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import rdflib
from rdfformat.generator import constants
from rdfformat.generator import rdf_helper
from rdfformat.generator import rdflib_facilities_handler
from rdfformat.generator import yaml_handler
from absl.testing import absltest


class RdfFacilitiesHandlerTest(absltest.TestCase):

  def testFacilitiesGraphGeneration(self):

    fake_facilities = 'fake_resources/Facilities.yaml'

    file_contents = rdf_helper.ReadFile(fake_facilities)

    yaml_facilities = yaml_handler.ImportYamlFiles(file_contents)

    # Create global graph
    graph = rdflib.Graph()

    # Bind the rdflib.OWL and Digital Buildings name spaces
    namespace_manager = rdflib.namespace.NamespaceManager(graph)
    namespace_manager.bind('owl', rdflib.OWL)
    namespace_manager.bind('db', constants.DIGITAL_BUILDINGS_NS)
    graph.namespace_manager = namespace_manager

    g_facilities = rdflib_facilities_handler.GenerateGraph(
        yaml_facilities, graph)

    # Main Types
    entity_type = rdflib.URIRef(constants.DIGITAL_BUILDINGS_NS['EntityType'])
    physical_location = rdflib.URIRef(
        constants.FACILITIES_NS['PhysicalLocation'])
    building = rdflib.URIRef(constants.FACILITIES_NS['Building'])
    floor = rdflib.URIRef(constants.FACILITIES_NS['Floor'])
    room = rdflib.URIRef(constants.FACILITIES_NS['Room'])
    has_physical_location = rdflib.URIRef(
        constants.DIGITAL_BUILDINGS_NS['hasPhysicalLocation'])
    has_floor = rdflib.URIRef(constants.DIGITAL_BUILDINGS_NS['hasFloor'])
    has_room = rdflib.URIRef(constants.DIGITAL_BUILDINGS_NS['hasRoom'])

    # Main Classes
    physical_location_class = (physical_location, rdflib.RDF.type,
                               rdflib.OWL.Class)
    building_class = (building, rdflib.RDF.type, rdflib.OWL.Class)
    floor_class = (floor, rdflib.RDF.type, rdflib.OWL.Class)
    room_class = (room, rdflib.RDF.type, rdflib.OWL.Class)

    # Assertions
    # Class assertions
    self.assertIn(physical_location_class, g_facilities)
    self.assertIn(building_class, g_facilities)
    self.assertIn(floor_class, g_facilities)
    self.assertIn(room_class, g_facilities)

    # SubClasses assertions
    self.assertIn((physical_location, rdflib.RDFS.subClassOf, entity_type),
                  g_facilities)
    self.assertIn((building, rdflib.RDFS.subClassOf, physical_location),
                  g_facilities)
    self.assertIn((floor, rdflib.RDFS.subClassOf, physical_location),
                  g_facilities)
    self.assertIn((room, rdflib.RDFS.subClassOf, physical_location),
                  g_facilities)

    # Relations assertions
    self.assertIn(
        (has_physical_location, rdflib.RDF.type, rdflib.OWL.ObjectProperty),
        g_facilities)
    self.assertIn((has_floor, rdflib.RDF.type, rdflib.OWL.ObjectProperty),
                  g_facilities)
    self.assertIn((has_room, rdflib.RDF.type, rdflib.OWL.ObjectProperty),
                  g_facilities)


if __name__ == '__main__':
  absltest.main()
