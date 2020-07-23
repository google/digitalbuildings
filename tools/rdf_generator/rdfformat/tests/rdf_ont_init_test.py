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
from rdflib import namespace

from rdfformat.generator import constants
from rdfformat.generator import rdf_ont_init
from absl.testing import absltest


class RdfOntInitTest(absltest.TestCase):

  def testRdfOntInitGraphGeneration(self):

    # Create global graph
    graph = rdflib.Graph()

    # Bind the OWL and Digital Buildings name spaces
    namespace_manager = namespace.NamespaceManager(graph)
    namespace_manager.bind("owl", rdflib.OWL)
    namespace_manager.bind("db", constants.DIGITAL_BUILDINGS_NS)
    graph.namespace_manager = namespace_manager

    g_ont_init = rdf_ont_init.GenerateGraph(graph)

    # Main Types
    entity_type = rdflib.URIRef(constants.DIGITAL_BUILDINGS_NS["EntityType"])
    physical_location = rdflib.URIRef(
        constants.FACILITIES_NS["PhysicalLocation"])
    state = rdflib.URIRef(constants.STATES_NS["State"])
    field = rdflib.URIRef(constants.FIELDS_NS["Field"])
    application = rdflib.URIRef(constants.DIGITAL_BUILDINGS_NS["Application"])
    equipment = rdflib.URIRef(constants.DIGITAL_BUILDINGS_NS["Equipment"])
    functionality = rdflib.URIRef(constants.HVAC_NS["Functionality"])

    # Main Classes
    entity_type_class = (entity_type, rdflib.RDF.type, rdflib.OWL.Class)
    multi_state_class = (state, rdflib.RDF.type, rdflib.OWL.Class)
    physical_location_class = (physical_location, rdflib.RDF.type,
                               rdflib.OWL.Class)
    field_class = (field, rdflib.RDF.type, rdflib.OWL.Class)
    application_class = (application, rdflib.RDF.type, rdflib.OWL.Class)
    equipment_class = (equipment, rdflib.RDF.type, rdflib.OWL.Class)
    functionality_class = (functionality, rdflib.RDF.type, rdflib.OWL.Class)

    # Assertions
    # Class assertions
    self.assertIn(entity_type_class, g_ont_init)
    self.assertIn(physical_location_class, g_ont_init)
    self.assertIn(multi_state_class, g_ont_init)
    self.assertIn(field_class, g_ont_init)
    self.assertIn(application_class, g_ont_init)
    self.assertIn(equipment_class, g_ont_init)
    self.assertIn(functionality_class, g_ont_init)

    # SubClasses assertions
    self.assertIn((entity_type, rdflib.RDFS.subClassOf, rdflib.OWL.Thing),
                  g_ont_init)
    self.assertIn((physical_location, rdflib.RDFS.subClassOf, entity_type),
                  g_ont_init)
    self.assertIn((state, rdflib.RDFS.subClassOf, rdflib.OWL.Thing), g_ont_init)
    self.assertIn((field, rdflib.RDFS.subClassOf, rdflib.OWL.Thing), g_ont_init)
    self.assertIn((application, rdflib.RDFS.subClassOf, entity_type),
                  g_ont_init)
    self.assertIn((equipment, rdflib.RDFS.subClassOf, entity_type), g_ont_init)
    self.assertIn((functionality, rdflib.RDFS.subClassOf, entity_type),
                  g_ont_init)

    # Disjoint assertions
    self.assertIn((application, rdflib.OWL.disjointWith, equipment), g_ont_init)
    self.assertIn((application, rdflib.OWL.disjointWith, functionality),
                  g_ont_init)
    self.assertIn((application, rdflib.OWL.disjointWith, physical_location),
                  g_ont_init)

    self.assertIn((equipment, rdflib.OWL.disjointWith, application), g_ont_init)
    self.assertIn((equipment, rdflib.OWL.disjointWith, functionality),
                  g_ont_init)
    self.assertIn((equipment, rdflib.OWL.disjointWith, physical_location),
                  g_ont_init)

    self.assertIn((functionality, rdflib.OWL.disjointWith, application),
                  g_ont_init)
    self.assertIn((functionality, rdflib.OWL.disjointWith, equipment),
                  g_ont_init)
    self.assertIn((functionality, rdflib.OWL.disjointWith, physical_location),
                  g_ont_init)

    self.assertIn((physical_location, rdflib.OWL.disjointWith, application),
                  g_ont_init)
    self.assertIn((physical_location, rdflib.OWL.disjointWith, functionality),
                  g_ont_init)
    self.assertIn((physical_location, rdflib.OWL.disjointWith, equipment),
                  g_ont_init)


if __name__ == "__main__":
  absltest.main()
