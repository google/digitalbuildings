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

"""RDF Helper Module.

Utility Code to create RDF Class and other RDF generic relationships
"""
from __future__ import print_function

import datetime

from absl import logging
import rdflib
from rdflib.extras import infixowl

from rdfformat.generator import constants


def CreateClassInGraph(graph,
                       class_name,
                       class_description,
                       parent_clazz,
                       entity_namespace=constants.DIGITAL_BUILDINGS_NS):
  """Utility function to create an RDF OWL Class and adds to the provided graph.

  Creates an RDF OWL Class with the input parameters
  OWL: Ontology Web Language
  RDF: Resource Description Framework

  Args:
     graph: the global graph where the ontology is being built in RDF.
     class_name: name of the RDF Class.
     class_description: the RDF Class description.
     parent_clazz: the parent RDF Class.
     entity_namespace: the entity_namespace to be used, DIGITAL_BUILDINGS_NS is
       by default

  Returns:
    graph: a graph with the newly built class
    clazz_object: the class object created
  """
  clazz = rdflib.URIRef(entity_namespace[class_name])

  # Add the OWL data to the graph
  clazz_tuple = (clazz, rdflib.RDF.type, rdflib.OWL.Class)
  graph.add(clazz_tuple)
  graph.add((clazz, rdflib.RDFS.subClassOf, parent_clazz))
  graph.add((clazz, rdflib.RDFS.label, rdflib.Literal(class_name)))
  if class_description is not None:
    graph.add((clazz, rdflib.RDFS.comment, rdflib.Literal(class_description)))
  graph.commit()
  return graph, clazz_tuple


def CreateInstanceInGraph(graph,
                          instance_name,
                          instance_description,
                          parent_clazz,
                          entity_namespace=constants.DIGITAL_BUILDINGS_NS):
  """Utility function to create an RDF OWL Instance
  and adds to the provided graph.

  Creates an RDF OWL Instance with the input parameters
  OWL: Ontology Web Language
  RDF: Resource Description Framework

  Args:
     graph: the global graph where the ontology is being built in RDF.
     instance_name: name of the RDF Instance.
     instance_description: the RDF Instance description.
     parent_clazz: the parent RDF Class.
     entity_namespace: the entity_namespace of the RDF Class.

  Returns:
    a graph with the newly built class
    instance object created
  """
  instance = rdflib.URIRef(entity_namespace[instance_name])

  # Add the OWL data to the graph
  instance_tuple = (instance, rdflib.RDF.type, rdflib.OWL.NamedIndividual)
  graph.add(instance_tuple)
  graph.add((instance, rdflib.RDF.type, parent_clazz[0]))
  graph.add((instance, rdflib.RDFS.label, rdflib.Literal(instance_name)))
  if instance_description is not None:
    graph.add(
        (instance, rdflib.RDFS.comment, rdflib.Literal(instance_description)))
  graph.commit()

  return graph, instance_tuple


def CreateDataPropertyInGraph(graph,
                              data_property_name,
                              data_property_description,
                              entity_namespace=constants.DIGITAL_BUILDINGS_NS):
  """Utility function to create an OWL Data Property relation
  and adds to the provided graph.

  Creates an RDF OWL Data Property with the input parameters
  OWL: Ontology Web Language
  RDF: Resource Description Framework

  Args:
     graph: the global graph where the ontology is being built in RDF.
     data_property_name: name of the OWL Data Property
     data_property_description: the RDF property description.
     entity_namespace: the entity_namespace of the RDF DataProperty.

  Returns:
     a graph with the newly built class
     the data property object created
  """
  data_property = rdflib.URIRef(entity_namespace[data_property_name])

  # Add the OWL data to the graph
  data_property_tuple = (data_property, rdflib.RDF.type,
                         rdflib.OWL.DatatypeProperty)
  graph.add(data_property_tuple)
  graph.add(
      (data_property, rdflib.RDFS.label, rdflib.Literal(data_property_name)))
  if data_property_description is not None:
    graph.add((data_property, rdflib.RDFS.comment,
               rdflib.Literal(data_property_description)))
  graph.commit()

  return graph, data_property_tuple


def CreateObjectPropertyInGraph(
    graph,
    object_property_name,
    object_property_description,
    entity_namespace=constants.DIGITAL_BUILDINGS_NS):
  """Utility function to create an OWL Object Property relation
   and adds to the provided graph.

  Creates an RDF OWL Object Property with the input parameters
  OWL: Ontology Web Language
  RDF: Resource Description Framework

  Args:
     graph: the global graph where the ontology is being built in RDF.
     object_property_name: name of the OWL Data Property
     object_property_description: the RDF Instance description.
     entity_namespace : the entity_namespace of the RDF Instance

  Returns:
    a graph with the newly built class
    the object property tuple created
  """
  object_property = rdflib.URIRef(entity_namespace[object_property_name])

  # Add the OWL data to the graph
  object_property_tuple = (object_property, rdflib.RDF.type,
                           rdflib.ObjectProperty)
  graph.add(object_property_tuple)
  graph.add((object_property, rdflib.RDFS.label,
             rdflib.Literal(object_property_name)))
  if object_property_description is not None:
    graph.add((object_property, rdflib.RDFS.comment,
               rdflib.Literal(object_property_description)))
  graph.commit()

  return graph, object_property_tuple


def CreatesStandardFieldNameCompositionInGraph(list_composition,
                                               standard_field_name,
                                               is_composed_of_property, graph):
  """Utility function takes a standard_field_name from the ontology
   and returns its composition constraint.

  Args:
    list_composition: a list of composition of standard field name defined by
      Carson. Example: ['Run', 'Command']
    standard_field_name: an ontology standard field name from Carson. Example:
      run_command
    is_composed_of_property: the property used to compose the standard field
      names, such as 'is_composed_of'
    graph: the global graph, example input run_command -> the returned result -
      is_composed_of_property only (Run and Command). - run_command subClassOf
      Command - Command subClassOf Point_type

  Returns:
    graph: updated graph with the composition.
  """
  class_owl = infixowl.Class(
      identifier=constants.FIELDS_NS[standard_field_name.capitalize()],
      graph=graph)
  graph = CreateCompositionInGraph(
      list_standard_field_names=list_composition,
      composition_operator="&",
      composition_property=is_composed_of_property,
      restriction=infixowl.only,
      class_owl=class_owl,
      graph=graph,
      entity_namespace=constants.SUBFIELDS_NS)

  return graph


def CreateCompositionInGraph(list_standard_field_names,
                             composition_operator,
                             composition_property,
                             restriction,
                             class_owl,
                             graph,
                             entity_namespace=constants.DIGITAL_BUILDINGS_NS,
                             sub_class_of=None):
  """Utility function that creates composition from a given list
  based on a composition operator and a restriction.

     the created composition is conform to the following pattern:
     class_owl = [composition_property  | restriction |
     list_standard_field_names[i] | composition_operator |
     list_standard_field_names [j]
     with i != j

  Args:
    list_standard_field_names: a list of standard field name defined by Carson.
      Example [compressor_run_status_4, supply_water_temperature_sensor,
      supply_water_temperature_setpoint]
    composition_operator: an '&' or '|' operator
    composition_property: the property which will relate the class and the list
      of standard field names
    restriction: the restriction imposed on the composition, 'only' or 'some'
    class_owl: the class where the composition is attached to.
    graph: the global graph
    entity_namespace: the name space for the composition elements
    sub_class_of: the subClass of the composition elements

  Returns:
    graph: updated graph with the composition.
  """
  index = 0
  if list_standard_field_names:
    # Prepare the first element
    first_element = infixowl.Class(
        identifier=entity_namespace[
            list_standard_field_names[index].capitalize()],
        graph=graph,
        subClassOf=sub_class_of)
    index += 1
    # Prepare the second element since the '&' operator is needed to determine
    # the nature of the composition
    if index < len(list_standard_field_names):
      if composition_operator == "&":
        concat = first_element & infixowl.Class(
            identifier=entity_namespace[
                list_standard_field_names[index].capitalize()],
            graph=graph,
            subClassOf=sub_class_of)
      elif composition_operator == "|":
        concat = first_element | infixowl.Class(
            identifier=entity_namespace[
                list_standard_field_names[index].capitalize()],
            graph=graph,
            subClassOf=sub_class_of)
      else:
        logging.error("Unknown operator %s", composition_operator)
        return graph
    else:  # there is only one element
      class_owl.subClassOf = [
          composition_property | restriction | first_element
      ]
      return graph

    index += 1
    # append the rest of the elements
    while index < len(list_standard_field_names):
      concat += infixowl.Class(
          identifier=entity_namespace[
              list_standard_field_names[index].capitalize()],
          graph=graph,
          subClassOf=sub_class_of)
      index += 1
    class_owl.subClassOf = [composition_property | restriction | concat]

  return graph


def DecomposeStandardFieldName(standard_field_name):
  """Utility function takes a standard_field_name from the ontology
   and returns its composition.

  Example: [run_command_1] -> ['Run', 'Command']
  Args:
    standard_field_name: a standard field name defined by Carson.

  Returns:
    list: a list of concepts that composes the standard field name.
  """
  split_points_data = standard_field_name.split("_")
  filtered_list = []
  for item in split_points_data:
    if not item.isdigit():
      filtered_list.append(item.capitalize())
  return filtered_list


def CreatesImplementsInGraph(graph, implements_list, applications_set,
                             application_class, class_object):
  """Utility function to handle the inheritance of types
  when the implements relation is used in the yaml file.

  Example: class_object subClassOf implements_list['CONTROL', 'MONITORING'].

  Args:
    graph: the global rdf graph
    implements_list: a list of implements from the yaml file
    applications_set: a set which contains the application already created in
      the graph to avoid recreating them.
    application_class: the application mother class which the implementation
      list inherits from
    class_object: the current class which is a subclass of the implements list

  Returns:
    graph: an updated graph
    applications_set: an updated application set
  """
  for implements_item in implements_list:
    application_sub_item = implements_item.capitalize()
    # Create the class only if it is not in the Set yet
    if application_sub_item not in applications_set:
      applications_set.add(application_sub_item)
      graph, application_sub_class = CreateClassInGraph(
          graph=graph,
          class_name=application_sub_item,
          class_description=None,
          parent_clazz=application_class[0]
      )  # getting the name of the class from the tuple
    application_sub_class = constants.DIGITAL_BUILDINGS_NS[
        implements_item.capitalize()]
    graph.add((class_object[0], rdflib.RDFS.subClassOf, application_sub_class))
  return graph, applications_set


def GetTimeNow():
  """Utility function returns the time in the
   following format %Y/%m/%d-%H:%M:%S.

  Returns:
    dt_string: an updated graph.
  """
  # datetime object containing current date and time
  dt_string = datetime.datetime.now().strftime("%Y/%m/%d-%H:%M:%S")
  return dt_string


def ReadFile(filename):
  """Utility function reads a file and returns its content.

  Args:
    filename: the file to read.

  Returns:
    The file content.
  """
  with open(filename, "r") as data_file:
    return data_file.read()
