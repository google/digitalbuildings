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

"""RDF Init.

Prepares the Ontology with the main classes to be created before populate the
RDF graph with the yaml content.

"""

import rdflib
from rdflib.extras import infixowl

from rdfformat.generator import constants


def GenerateGraph(graph):
  """Utility function prepares the RDF graph with owl
  classes before the yaml content gets converted.

  Updates an RDF graph with the yaml content

  Args:
    graph: the global graph where the ontology is being built in RDF.

  Returns:
    a graph with the contents of the yaml file merged
  """
  # Create the entities to be added to the Graph
  entity_type = rdflib.URIRef(constants.DIGITAL_BUILDINGS_NS["EntityType"])
  physical_location = rdflib.URIRef(constants.FACILITIES_NS["PhysicalLocation"])
  multi_state = rdflib.URIRef(constants.STATES_NS["State"])
  field = rdflib.URIRef(constants.FIELDS_NS["Field"])
  application = rdflib.URIRef(constants.DIGITAL_BUILDINGS_NS["Application"])
  equipment = rdflib.URIRef(constants.DIGITAL_BUILDINGS_NS["Equipment"])
  functionality = rdflib.URIRef(constants.HVAC_NS["Functionality"])
  # Create the classes
  physical_location_class = infixowl.Class(
      identifier=constants.FACILITIES_NS["PhysicalLocation"],
      graph=graph,
      subClassOf=[entity_type])
  application_class = infixowl.Class(
      identifier=constants.DIGITAL_BUILDINGS_NS["Application"],
      graph=graph,
      subClassOf=[entity_type])
  equipment_class = infixowl.Class(
      identifier=constants.DIGITAL_BUILDINGS_NS["Equipment"],
      graph=graph,
      subClassOf=[entity_type])
  functionality_class = infixowl.Class(
      identifier=constants.HVAC_NS["Functionality"],
      graph=graph,
      subClassOf=[entity_type])
  # Make them disjoint with each other to avoid reasoning inconsistencies
  physical_location_class.disjointWith = [
      application_class, equipment_class, functionality_class
  ]
  application_class.disjointWith = [
      physical_location_class, equipment_class, functionality_class
  ]
  equipment_class.disjointWith = [
      application_class, physical_location_class, functionality_class
  ]
  functionality_class.disjointWith = [
      application_class, equipment_class, physical_location_class
  ]

  # Add the OWL Classes to the graph
  # EntityType
  graph.add((entity_type, rdflib.RDF.type, rdflib.OWL.Class))
  graph.add((entity_type, rdflib.RDFS.subClassOf, rdflib.OWL.Thing))

  # PhysicalLocation
  graph.add((physical_location, rdflib.RDF.type, rdflib.OWL.Class))
  graph.add((physical_location, rdflib.RDFS.subClassOf, entity_type))
  graph.add((physical_location, rdflib.RDFS.label,
             rdflib.Literal("PhysicalLocation")))
  graph.add((physical_location, rdflib.RDFS.comment,
             rdflib.Literal("The class of all physical locations")))

  # MultiState
  graph.add((multi_state, rdflib.RDF.type, rdflib.OWL.Class))
  graph.add((multi_state, rdflib.RDFS.subClassOf, rdflib.OWL.Thing))
  graph.add((multi_state, rdflib.RDFS.label, rdflib.Literal("State")))
  graph.add((multi_state, rdflib.RDFS.comment,
             rdflib.Literal("The class of all states")))

  # Functionality
  graph.add((functionality, rdflib.RDF.type, rdflib.OWL.Class))
  graph.add((functionality, rdflib.RDFS.subClassOf, entity_type))
  graph.add((functionality, rdflib.RDFS.label, rdflib.Literal("Functionality")))
  graph.add((functionality, rdflib.RDFS.comment,
             rdflib.Literal("The class of all functionalities")))

  # Field
  graph.add((field, rdflib.RDF.type, rdflib.OWL.Class))
  graph.add((field, rdflib.RDFS.subClassOf, rdflib.OWL.Thing))
  graph.add((field, rdflib.RDFS.label, rdflib.Literal("Field")))
  graph.add(
      (field, rdflib.RDFS.comment, rdflib.Literal("The class of all fields")))

  # Application
  graph.add((application, rdflib.RDF.type, rdflib.OWL.Class))
  graph.add((application, rdflib.RDFS.subClassOf, entity_type))
  graph.add((application, rdflib.RDFS.label, rdflib.Literal("Application")))
  graph.add((application, rdflib.RDFS.comment,
             rdflib.Literal("The class of all applications")))

  # Equipment
  graph.add((equipment, rdflib.RDF.type, rdflib.OWL.Class))
  graph.add((equipment, rdflib.RDFS.subClassOf, entity_type))
  graph.add((equipment, rdflib.RDFS.label, rdflib.Literal("Equipment")))
  graph.add((equipment, rdflib.RDFS.comment,
             rdflib.Literal("The class of all equipment")))

  return graph
