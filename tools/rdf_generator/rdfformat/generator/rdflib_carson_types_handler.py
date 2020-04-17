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
"""Carson Types RDF handler.

Takes as input any Carson yaml file such as VAV, PUMP, FCU, etc and populate the
RDF graph with the yaml content.

"""
import rdflib
from rdflib import namespace
from rdflib.extras import infixowl

from rdfformat.generator import constants
from rdfformat.generator import rdf_helper


def GenerateGraph(yaml_object, graph, entity_namespace):
  """Utility function updates an RDF graph with the yaml content.

  Updates an RDF graph with the yaml content

  Args:
    yaml_object: the yaml content.
    graph: the global graph where the ontology is being built in RDF.
    entity_namespace: the namespace to be attributed to the given types

  Returns:
    a graph with the contents of the yaml file merged
  """

  # Ignore entities implementing the following keywords in their definition
  ignore_generation_set = {
      "DEPRECATED", "INCOMPLETE", "IGNORE", "REMAP_REQUIRED"
  }
  field = rdflib.URIRef(constants.FIELDS_NS["Field"])
  # Prepare properties to be added to the graph and not in the yaml
  uses_property = infixowl.Property(
      identifier=constants.DIGITAL_BUILDINGS_NS["uses"],
      baseType=infixowl.OWL_NS.ObjectProperty,
      graph=graph)
  uses_property_optionally = infixowl.Property(
      identifier=constants.DIGITAL_BUILDINGS_NS["usesOptional"],
      baseType=infixowl.OWL_NS.ObjectProperty,
      graph=graph)
  is_composed_of_property = infixowl.Property(
      identifier=constants.DIGITAL_BUILDINGS_NS["isComposedOf"],
      baseType=infixowl.OWL_NS.ObjectProperty,
      graph=graph)
  infixowl.Class(identifier=constants.SUBFIELDS_NS["Point_type"], graph=graph)

  # Traverse the yaml content
  for clazz, clazz_content in yaml_object.items():
    class_name = clazz.capitalize()
    implements = clazz_content.get("implements")
    # implements content will decide if the class is added to the graph or not
    ignore_class = False
    if implements is not None:
      for implements_item in implements:
        if implements_item in ignore_generation_set:
          ignore_class = True

    # Generate the class if it does not have implements field
    #   or no (DEPRECATED or INCOMPLETE)
    if ignore_class:
      continue

    # Create the class
    parent = (
        entity_namespace[implements[0].capitalize()]
        if implements is not None else namespace.OWL.Thing)
    graph, _ = rdf_helper.CreateClassInGraph(
        graph=graph,
        class_name=class_name,
        class_description=clazz_content.get("description"),
        parent_clazz=parent,
        entity_namespace=entity_namespace)
    # update parents only if implements is not None
    if implements is not None:
      for implements_item in implements[1:]:
        graph.add(
            (entity_namespace[class_name.capitalize()], rdflib.RDFS.subClassOf,
             entity_namespace[implements_item.capitalize()]))

    # check the mandatory fields
    uses = clazz_content.get("uses")
    if uses is not None and isinstance(uses, list):
      for each_item in uses:
        list_composition = rdf_helper.DecomposeStandardFieldName(each_item)
        graph = rdf_helper.CreatesStandardFieldNameCompositionInGraph(
            graph=graph,
            list_composition=list_composition,
            standard_field_name=each_item,
            is_composed_of_property=is_composed_of_property)
        class_owl = infixowl.Class(
            identifier=entity_namespace[class_name],
            graph=graph,
            subClassOf=[parent])
        graph = rdf_helper.CreateCompositionInGraph(
            list_standard_field_names=uses,
            composition_operator="&",
            composition_property=uses_property,
            restriction=infixowl.only,
            class_owl=class_owl,
            graph=graph,
            entity_namespace=constants.FIELDS_NS,
            sub_class_of=[field])

    # check the optional fields
    opt_uses = clazz_content.get("opt_uses")
    if opt_uses is not None and isinstance(opt_uses, list):
      for each_item in opt_uses:
        list_composition = rdf_helper.DecomposeStandardFieldName(each_item)
        graph = rdf_helper.CreatesStandardFieldNameCompositionInGraph(
            graph=graph,
            list_composition=list_composition,
            standard_field_name=each_item,
            is_composed_of_property=is_composed_of_property)
        class_owl = infixowl.Class(
            identifier=entity_namespace[class_name],
            graph=graph,
            subClassOf=[parent])
        graph = rdf_helper.CreateCompositionInGraph(
            list_standard_field_names=opt_uses,
            composition_operator="|",
            composition_property=uses_property_optionally,
            restriction=infixowl.some,
            class_owl=class_owl,
            graph=graph,
            entity_namespace=constants.FIELDS_NS,
            sub_class_of=[field])
  return graph
