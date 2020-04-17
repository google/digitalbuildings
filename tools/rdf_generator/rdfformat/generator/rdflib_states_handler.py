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
"""States Yaml Ontology RDF handler.

Takes a states.yaml input and populate the RDF graph with the yaml content.

"""
import rdflib

from rdfformat.generator import constants
from rdfformat.generator import rdf_helper


def GenerateGraph(yaml_object, graph):
  """Utility function to populate in the graph yaml concepts.

  Populates an RDF graph from the yaml content.
  Args:
    yaml_object: the yaml content.
    graph: the global graph where the ontology is being built in RDF.

  Returns:
    a graph with the newly built class

  """
  # Create the node to add to the Graph
  # Construct the classes and the subclasses
  graph, multi_state = rdf_helper.CreateClassInGraph(
      graph=graph,
      class_name='State',
      class_description=None,
      parent_clazz=rdflib.OWL.Thing,
      entity_namespace=constants.STATES_NS)
  for clazz, clazz_content in yaml_object.items():
    graph, _ = rdf_helper.CreateClassInGraph(
        graph=graph,
        class_name=clazz.capitalize(),
        class_description=clazz_content,
        parent_clazz=multi_state[0],
        entity_namespace=constants.STATES_NS)
  return graph
