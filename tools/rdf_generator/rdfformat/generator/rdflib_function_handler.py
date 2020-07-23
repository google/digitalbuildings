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

"""Function RDF handler.

Takes an Abstract.yaml input and populate the RDF graph with the yaml content.

"""
import rdflib
from rdflib.extras import infixowl

from rdfformat.generator import constants
from rdfformat.generator import rdf_helper


def GenerateGraph(yaml_object, graph):
  """Utility function updates an RDF graph with
  the yaml content of the Abstract.yaml.

  The content of each object is similar to the following:
    DXRC:
      description: "Compressor run control on return air side (RC)."
      opt_uses:
        discharge_air_temperature_sensor
        leaving_cooling_coil_temperature_sensor
        cooling_thermal_power_capacity
      uses:
        return_air_temperature_setpoint
        return_air_temperature_sensor
        compressor_run_command
        compressor_run_status
      implements:
        CONTROL

  Updates an RDF graph with the yaml content.

  Args:
    yaml_object: the yaml content.
    graph: the global graph where the ontology is being built in RDF.

  Returns:
    a graph with the contents of the yaml file merged
  """
  # Applications Set used to avoid recreating applications again in the graph
  applications_set = set()
  # Prepare classes to be added to the graph and not in the yaml
  functionality = rdflib.URIRef(constants.HVAC_NS["Functionality"])
  entity_type = rdflib.URIRef(constants.DIGITAL_BUILDINGS_NS["EntityType"])
  field = rdflib.URIRef(constants.FIELDS_NS["Field"])
  infixowl.Class(identifier=constants.FIELDS_NS["Field"], graph=graph)
  infixowl.Class(identifier=constants.SUBFIELDS_NS["Point_type"], graph=graph)
  graph, _ = rdf_helper.CreateClassInGraph(
      graph=graph,
      class_name="Functionality",
      class_description=None,
      parent_clazz=entity_type,
      entity_namespace=constants.HVAC_NS)

  graph, application_class = rdf_helper.CreateClassInGraph(
      graph=graph,
      class_name="Application",
      class_description=None,
      parent_clazz=entity_type)

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

  # Traverse the yaml content
  for clazz, clazz_content in yaml_object.items():
    class_name = clazz.capitalize()
    graph, clazz_object = rdf_helper.CreateClassInGraph(
        graph=graph,
        class_name=class_name,
        class_description=clazz_content.get("description"),
        parent_clazz=functionality,
        entity_namespace=constants.HVAC_NS)

    implements = clazz_content.get("implements")
    if implements is not None:
      graph, applications_set = rdf_helper.CreatesImplementsInGraph(
          graph=graph,
          implements_list=implements,
          applications_set=applications_set,
          application_class=application_class,
          class_object=clazz_object)

    uses = clazz_content.get("uses")
    if uses is not None:
      if isinstance(uses, list):
        for each_item in uses:
          list_composition = rdf_helper.DecomposeStandardFieldName(each_item)
          graph = rdf_helper.CreatesStandardFieldNameCompositionInGraph(
              graph=graph,
              list_composition=list_composition,
              standard_field_name=each_item,
              is_composed_of_property=is_composed_of_property)
        class_owl = infixowl.Class(
            identifier=constants.HVAC_NS[class_name],
            graph=graph,
            subClassOf=[functionality])
        graph = rdf_helper.CreateCompositionInGraph(
            list_standard_field_names=uses,
            composition_operator="&",
            composition_property=uses_property,
            restriction=infixowl.only,
            class_owl=class_owl,
            graph=graph,
            entity_namespace=constants.FIELDS_NS,
            sub_class_of=[field])

    opt_uses = clazz_content.get("opt_uses")
    if opt_uses is not None:
      if isinstance(opt_uses, list):
        for each_item in opt_uses:
          list_composition = rdf_helper.DecomposeStandardFieldName(each_item)
          graph = rdf_helper.CreatesStandardFieldNameCompositionInGraph(
              graph=graph,
              list_composition=list_composition,
              standard_field_name=each_item,
              is_composed_of_property=is_composed_of_property)
        class_owl = infixowl.Class(
            identifier=constants.HVAC_NS[class_name],
            graph=graph,
            subClassOf=[functionality])
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
