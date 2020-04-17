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
"""Facilities RDF handler.

Takes a Facilities.yaml input and populate the RDF graph with the yaml content.

"""
import rdflib
from rdflib.extras import infixowl

from rdfformat.generator import constants
from rdfformat.generator import rdf_helper


def GenerateGraph(yaml_object, graph):
  """Utility function updates an RDF graph with the yaml content.

  Updates an RDF graph with the yaml content

  Args:
    yaml_object: the yaml content.
    graph: the global graph where the ontology is being built in RDF.

  Returns:
    a graph with the contents of the yaml file merged
  """
  # Create the node to add to the Graph
  physical_location = rdflib.URIRef(constants.FACILITIES_NS["PhysicalLocation"])
  entity_type = rdflib.URIRef(constants.DIGITAL_BUILDINGS_NS["EntityType"])
  has_physical_location = rdflib.URIRef(
      constants.DIGITAL_BUILDINGS_NS["hasPhysicalLocation"])
  has_floor = rdflib.URIRef(constants.DIGITAL_BUILDINGS_NS["hasFloor"])
  has_room = rdflib.URIRef(constants.DIGITAL_BUILDINGS_NS["hasRoom"])

  has_room_property = infixowl.Property(
      identifier=constants.DIGITAL_BUILDINGS_NS["hasRoom"],
      baseType=infixowl.OWL_NS.ObjectProperty,
      graph=graph)

  has_floor_property = infixowl.Property(
      identifier=constants.DIGITAL_BUILDINGS_NS["hasFloor"],
      baseType=infixowl.OWL_NS.ObjectProperty,
      graph=graph)

  # Add the OWL data to the graph
  graph.add((physical_location, rdflib.RDF.type, rdflib.OWL.Class))
  graph.add((physical_location, rdflib.RDFS.subClassOf, entity_type))
  graph.add((physical_location, rdflib.RDFS.label,
             rdflib.Literal("PhysicalLocation")))
  graph.add((physical_location, rdflib.RDFS.comment,
             rdflib.Literal("The class of all physical locations")))

  # Construct the classes and the subclasses
  map_name_object = {}
  for clazz in yaml_object.keys():
    clazz_content = yaml_object.get(clazz)
    description = clazz_content.get("description")
    clazz_object = rdf_helper.CreateClassInGraph(
        graph,
        clazz.capitalize(),
        description,
        physical_location,
        entity_namespace=constants.FACILITIES_NS)
    map_name_object[clazz.capitalize()] = clazz_object

  # Construct the object properties
  graph.add((has_physical_location, rdflib.RDF.type, rdflib.OWL.ObjectProperty))
  graph.add(
      (has_physical_location, rdflib.RDF.type, rdflib.OWL.TransitiveProperty))
  graph.add((has_floor, rdflib.RDF.type, rdflib.OWL.ObjectProperty))
  graph.add((has_room, rdflib.RDF.type, rdflib.OWL.ObjectProperty))

  # Construct the sub object properties
  graph.add((has_floor, rdflib.RDFS.subPropertyOf, has_physical_location))
  graph.add((has_room, rdflib.RDFS.subPropertyOf, has_physical_location))

  # Link the graph together, done manually until the yaml evolves
  class_floor = infixowl.Class(
      identifier=constants.FACILITIES_NS["Floor"], graph=graph)
  class_room = infixowl.Class(
      identifier=constants.FACILITIES_NS["Room"], graph=graph)
  class_building = infixowl.Class(
      identifier=constants.FACILITIES_NS["Building"], graph=graph)
  class_building.subClassOf = [has_floor_property | infixowl.only | class_floor]
  class_floor.subClassOf = [has_room_property | infixowl.only | class_room]

  return graph
