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

"""Tests for generator.rdflib_function_handler."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import rdflib
from rdflib import compare
from rdflib.extras import infixowl

from rdfformat.generator import constants
from rdfformat.generator import rdf_helper
from rdfformat.generator import rdflib_function_handler
from rdfformat.generator import yaml_handler
from absl.testing import absltest


class RdfFunctionHandlerTest(absltest.TestCase):

  def testAbstractGraphGeneration(self):

    fake_abstract = 'fake_resources/Abstract.yaml'

    file_contents = rdf_helper.ReadFile(fake_abstract)

    yaml_abstract = yaml_handler.ImportYamlFiles(file_contents)

    # Create global graph
    graph = rdflib.Graph()
    # Generate the graph by the function handler
    graph = rdflib_function_handler.GenerateGraph(yaml_abstract, graph)

    # Build a second graph manually in order to compare it with the one above:
    # DD:
    # description: "Dual duct flow control (hot deck, cold deck)."
    # is_abstract: true
    # opt_uses:
    # - discharge_air_temperature_sensor
    # - run_command
    # uses:
    # - heating_air_flowrate_sensor
    # - heating_air_flowrate_setpoint
    # implements:
    # - CONTROL

    expected_graph = rdflib.Graph()
    # Main Types
    functionality = rdflib.URIRef(constants.HVAC_NS['Functionality'])
    entity_type = rdflib.URIRef(constants.DIGITAL_BUILDINGS_NS['EntityType'])
    dd_description = 'Dual duct flow control (hot deck, cold deck).'
    # Main Classes
    dd_expected = infixowl.Class(
        identifier=constants.HVAC_NS['Dd'],
        graph=expected_graph,
        subClassOf=[functionality])
    expected_graph, _ = rdf_helper.CreateClassInGraph(
        graph=expected_graph,
        class_name='Dd',
        class_description=dd_description,
        parent_clazz=functionality,
        entity_namespace=constants.HVAC_NS)
    infixowl.Class(
        identifier=constants.SUBFIELDS_NS['Point_type'], graph=expected_graph)

    uses_property = infixowl.Property(
        identifier=constants.DIGITAL_BUILDINGS_NS['uses'],
        baseType=infixowl.OWL_NS.ObjectProperty,
        graph=expected_graph)

    is_composed_of_property = infixowl.Property(
        identifier=constants.DIGITAL_BUILDINGS_NS['isComposedOf'],
        baseType=infixowl.OWL_NS.ObjectProperty,
        graph=expected_graph)
    uses_property_optionally = infixowl.Property(
        identifier=constants.DIGITAL_BUILDINGS_NS['usesOptional'],
        baseType=infixowl.OWL_NS.ObjectProperty,
        graph=expected_graph)

    infixowl.Class(
        identifier=constants.SUBFIELDS_NS['Air'], graph=expected_graph)

    infixowl.Class(
        identifier=constants.SUBFIELDS_NS['Flowrate'], graph=expected_graph)

    infixowl.Class(
        identifier=constants.SUBFIELDS_NS['Heating'], graph=expected_graph)

    infixowl.Class(
        identifier=constants.SUBFIELDS_NS['Run'], graph=expected_graph)

    infixowl.Class(
        identifier=constants.SUBFIELDS_NS['Command'], graph=expected_graph)

    infixowl.Class(
        identifier=constants.SUBFIELDS_NS['Discharge'], graph=expected_graph)

    infixowl.Class(
        identifier=constants.SUBFIELDS_NS['Temperature'], graph=expected_graph)

    infixowl.Class(
        identifier=constants.SUBFIELDS_NS['Sensor'], graph=expected_graph)

    infixowl.Class(
        identifier=constants.FIELDS_NS['Field'], graph=expected_graph)

    heating_air_flowrate_sensor = infixowl.Class(
        identifier=constants.FIELDS_NS['Heating_air_flowrate_sensor'],
        graph=expected_graph,
        subClassOf=[constants.FIELDS_NS['Field']])
    heating_air_flowrate_setpoint = infixowl.Class(
        identifier=constants.FIELDS_NS['Heating_air_flowrate_setpoint'],
        graph=expected_graph,
        subClassOf=[constants.FIELDS_NS['Field']])

    concat = heating_air_flowrate_sensor & heating_air_flowrate_setpoint
    dd_expected.subClassOf = [uses_property | infixowl.only | concat]

    discharge_air_temperature_sensor = infixowl.Class(
        identifier=constants.FIELDS_NS['Discharge_air_temperature_sensor'],
        graph=expected_graph,
        subClassOf=[constants.FIELDS_NS['Field']])
    run_command = infixowl.Class(
        identifier=constants.FIELDS_NS['Run_command'],
        graph=expected_graph,
        subClassOf=[constants.FIELDS_NS['Field']])

    concat2 = discharge_air_temperature_sensor | run_command
    dd_expected.subClassOf = [
        uses_property_optionally | infixowl.some | concat2
    ]

    list_composition = rdf_helper.DecomposeStandardFieldName(
        'Discharge_air_temperature_sensor')
    expected_graph = rdf_helper.CreatesStandardFieldNameCompositionInGraph(
        graph=expected_graph,
        list_composition=list_composition,
        standard_field_name='Discharge_air_temperature_sensor',
        is_composed_of_property=is_composed_of_property)

    list_composition = rdf_helper.DecomposeStandardFieldName('Run_command')
    expected_graph = rdf_helper.CreatesStandardFieldNameCompositionInGraph(
        graph=expected_graph,
        list_composition=list_composition,
        standard_field_name='Run_command',
        is_composed_of_property=is_composed_of_property)

    list_composition = rdf_helper.DecomposeStandardFieldName(
        'Heating_air_flowrate_sensor')
    expected_graph = rdf_helper.CreatesStandardFieldNameCompositionInGraph(
        graph=expected_graph,
        list_composition=list_composition,
        standard_field_name='Heating_air_flowrate_sensor',
        is_composed_of_property=is_composed_of_property)

    list_composition = rdf_helper.DecomposeStandardFieldName(
        'Heating_air_flowrate_setpoint')
    expected_graph = rdf_helper.CreatesStandardFieldNameCompositionInGraph(
        graph=expected_graph,
        list_composition=list_composition,
        standard_field_name='Heating_air_flowrate_setpoint',
        is_composed_of_property=is_composed_of_property)

    expected_graph, functionality_class = rdf_helper.CreateClassInGraph(
        graph=expected_graph,
        class_name='Functionality',
        class_description=None,
        parent_clazz=entity_type,
        entity_namespace=constants.HVAC_NS)

    expected_graph, application = rdf_helper.CreateClassInGraph(
        graph=expected_graph,
        class_name='Application',
        class_description=None,
        parent_clazz=entity_type)

    expected_graph, control = rdf_helper.CreateClassInGraph(
        graph=expected_graph,
        class_name='Control',
        class_description=None,
        parent_clazz=application[0])

    expected_graph, _ = rdf_helper.CreateClassInGraph(
        graph=expected_graph,
        class_name='Dd',
        class_description=dd_description,
        parent_clazz=functionality_class[0],
        entity_namespace=constants.HVAC_NS)

    expected_graph, _ = rdf_helper.CreateClassInGraph(
        graph=expected_graph,
        class_name='Dd',
        class_description=dd_description,
        parent_clazz=control[0],
        entity_namespace=constants.HVAC_NS)

    # Check if they are similar
    self.assertTrue(compare.similar(graph, expected_graph))


if __name__ == '__main__':
  absltest.main()
