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

Takes a units.yaml input and populate the RDF graph with the yaml content.

"""
import rdflib

from rdfformat.generator import constants
from rdfformat.generator import rdf_helper


def GenerateGraph(yaml_object, graph):
  """Utility function to populate in the graph yaml concepts.

  Populates an RDF graph from the yaml content.
  The units yaml content is either a string or a dictionary, example below:
    - kelvins: STANDARD
    - degrees_celsius
    - degrees_fahrenheit
  Args:
    yaml_object: the yaml content.
    graph: the global graph where the ontology is being built in RDF.

  Returns:
    a graph with the newly built class
  """
  # Create the node to add to the Graph
  unit = rdflib.URIRef(constants.UNITS_NS['Unit'])
  graph, _ = rdf_helper.CreateClassInGraph(
      graph,
      'Unit',
      'Class of all units',
      rdflib.OWL.Thing,
      entity_namespace=constants.UNITS_NS)
  graph, standard_unit_data_property_object = \
      rdf_helper.CreateDataPropertyInGraph(
          graph,
          data_property_name='is_standard_unit',
          data_property_description=
          'The International System of Units '
          '(abbreviated SI from systeme internationale , '
          'the French version of the name) is a scientific '
          'method of expressing the magnitudes or quantities'
          ' of important natural phenomena. There are seven '
          'base units in the system, from which other units are derived.')

  # Construct the classes and the subclasses
  for clazz in yaml_object.keys():
    graph, clazz_object = rdf_helper.CreateClassInGraph(
        graph=graph,
        class_name=clazz.capitalize(),
        class_description=None,
        parent_clazz=unit,
        entity_namespace=constants.UNITS_NS)
    clazz_content = yaml_object.get(clazz)
    for each_item in clazz_content:
      # When a unit is standard it is a dict, example: kelvins: STANDARD.
      if isinstance(each_item, dict):
        instance_name = list(each_item.keys())[0]
        is_standard = each_item[instance_name]
      else:
        is_standard = False
        instance_name = each_item
    # Construct the instances
      graph, instance_object = rdf_helper.CreateInstanceInGraph(
          graph=graph,
          instance_name=instance_name,
          instance_description=None,
          parent_clazz=clazz_object,
          entity_namespace=constants.UNITS_NS)
      if is_standard:
        graph.add((instance_object[0], standard_unit_data_property_object[0],
                   rdflib.Literal(True)))
      else:
        graph.add((instance_object[0], standard_unit_data_property_object[0],
                   rdflib.Literal(False)))

  return graph
