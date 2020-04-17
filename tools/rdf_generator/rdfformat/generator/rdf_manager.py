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
"""RDF Manager, orchestrates the rdf generation."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import rdflib
from rdflib import namespace
from rdflib.extras import infixowl

from rdfformat.generator import constants
from rdfformat.generator import rdf_helper
from rdfformat.generator import rdf_ont_init
from rdfformat.generator import rdflib_carson_types_handler
from rdfformat.generator import rdflib_facilities_handler
from rdfformat.generator import rdflib_function_handler
from rdfformat.generator import rdflib_generaltypes_handler
from rdfformat.generator import rdflib_states_handler
from rdfformat.generator import rdflib_subfields_handler
from rdfformat.generator import rdflib_units_handler
from rdfformat.generator import yaml_handler

FACILITIES = '/FACILITIES/entity_types/Facilities.yaml'
UNITS = '/units/units.yaml'
SUBFIELDS = '/subfields/subfields.yaml'
ABSTRACT = '/HVAC/entity_types/ABSTRACT.yaml'
GENERALTYPES = '/HVAC/entity_types/GENERALTYPES.yaml'
STATES = '/states/states.yaml'

FAN = '/HVAC/entity_types/FAN.yaml'
PMP = '/HVAC/entity_types/PMP.yaml'
FCU = '/HVAC/entity_types/FCU.yaml'
VAV = '/HVAC/entity_types/VAV.yaml'
DH = '/HVAC/entity_types/DH.yaml'
AHU = '/HVAC/entity_types/AHU.yaml'
BLR = '/HVAC/entity_types/BLR.yaml'
CDWS = '/HVAC/entity_types/CDWS.yaml'
CH = '/HVAC/entity_types/CH.yaml'
CHWS = '/HVAC/entity_types/CHWS.yaml'
CT = '/HVAC/entity_types/CT.yaml'
DC = '/HVAC/entity_types/DC.yaml'
DFR = '/HVAC/entity_types/DFR.yaml'
DMP = '/HVAC/entity_types/DMP.yaml'
HWS = '/HVAC/entity_types/HWS.yaml'
HX = '/HVAC/entity_types/HX.yaml'
MAU = '/HVAC/entity_types/MAU.yaml'
SDC = '/HVAC/entity_types/SDC.yaml'
UH = '/HVAC/entity_types/UH.yaml'
ZONE = '/HVAC/entity_types/ZONE.yaml'

carson_types = {
    FAN, PMP, FCU, VAV, DH, AHU, BLR, CDWS, CH, CHWS, CT, DC, DFR, DMP, HWS, HX,
    MAU, SDC, UH, ZONE
}


def Generate(resource_path):
  """Generates the RDF from Yaml.

  Handles the overall orchestration of the process.

  Args:
    resource_path: the path where to find the yaml files.

  Returns:
    graph: the rdf graph
  """
  # Create global graph
  graph = rdflib.Graph()

  # Bind the OWL and Digital Buildings name spaces
  namespace_manager = namespace.NamespaceManager(graph)
  namespace_manager.bind('owl', namespace.OWL)
  namespace_manager.bind('db', constants.DIGITAL_BUILDINGS_NS)
  namespace_manager.bind('dcterms', 'http://purl.org/dc/terms/')
  graph.namespace_manager = namespace_manager

  # Initialize the ontology headers
  digital_building_ont = infixowl.Ontology(
      identifier=rdflib.URIRef(constants.DB), graph=graph)
  digital_building_ont.label = rdflib.Literal('Digital Buildings')

  graph.add((digital_building_ont.identifier, constants.DCTERMS['title'],
             rdflib.Literal('Digital Buildings Ontology')))
  graph.add((digital_building_ont.identifier, constants.DCTERMS['license'],
             rdflib.Literal(constants.GITHUB_LICENSE)))
  graph.add((digital_building_ont.identifier, constants.DCTERMS['modified'],
             rdflib.Literal(rdf_helper.GetTimeNow())))
  graph.add((digital_building_ont.identifier, rdflib.OWL['versionInfo'],
             rdflib.Literal(constants.ONT_VERSION)))
  graph.add((digital_building_ont.identifier, constants.DCTERMS['creator'],
             rdflib.Literal(constants.AUTHORS)))
  graph.add((digital_building_ont.identifier, constants.DCTERMS['contributor'],
             rdflib.Literal(constants.CONTRIBUTORS)))
  graph.add((digital_building_ont.identifier, rdflib.OWL['seeAlso'],
             rdflib.Literal(constants.GITHUB)))
  graph.add((digital_building_ont.identifier, constants.DCTERMS['description'],
             rdflib.Literal(constants.ONT_DESCRIPTION)))

  # Initialize the main classes
  graph = rdf_ont_init.GenerateGraph(graph)

  # Handle the Facilities file
  facilities_file = rdf_helper.ReadFile(resource_path + FACILITIES)
  yaml_facilities = yaml_handler.ImportYamlFiles(facilities_file)
  graph = rdflib_facilities_handler.GenerateGraph(yaml_facilities, graph)
  # Handle the Units file
  units_file = rdf_helper.ReadFile(resource_path + UNITS)
  yaml_units = yaml_handler.ImportYamlFiles(units_file)
  graph = rdflib_units_handler.GenerateGraph(yaml_units, graph)
  # Handle the Subfields file
  subfields_file = rdf_helper.ReadFile(resource_path + SUBFIELDS)
  yaml_subfields = yaml_handler.ImportYamlFiles(subfields_file)
  graph = rdflib_subfields_handler.GenerateGraph(yaml_subfields, graph)
  # # Handle the Abstract file
  abstract_file = rdf_helper.ReadFile(resource_path + ABSTRACT)
  yaml_abstract = yaml_handler.ImportYamlFiles(abstract_file)
  graph = rdflib_function_handler.GenerateGraph(yaml_abstract, graph)
  # # Handle the General Types file
  generaltypes_file = rdf_helper.ReadFile(resource_path + GENERALTYPES)
  yaml_generaltypes = yaml_handler.ImportYamlFiles(generaltypes_file)
  graph = rdflib_generaltypes_handler.GenerateGraph(yaml_generaltypes, graph)
  # Handle the states file
  states_file = rdf_helper.ReadFile(resource_path + STATES)
  yaml_states = yaml_handler.ImportYamlFiles(states_file)
  graph = rdflib_states_handler.GenerateGraph(yaml_states, graph)

  # Handle the HVAC files
  for hvac_type in carson_types:
    type_file = rdf_helper.ReadFile(resource_path + hvac_type)
    yaml_type = yaml_handler.ImportYamlFiles(type_file)
    graph = rdflib_carson_types_handler.GenerateGraph(yaml_type, graph,
                                                      constants.HVAC_NS)

  return graph


def SerializeToFile(graph, output_file):
  """Serializes the graph into an RDF File.

  Relies on the rdf_helper to serialize

  Args:
    graph: the rdf graph to serialize.
    output_file: the output file path where to serialize the rdf file
  """
  graph.serialize(destination=output_file, format='pretty-xml')
  print('Serialization Done!')
