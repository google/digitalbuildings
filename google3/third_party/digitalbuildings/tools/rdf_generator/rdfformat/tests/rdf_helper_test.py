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

"""Tests for generator.rdf_helper."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import rdflib
from rdflib import compare
from rdflib import namespace
from rdflib.extras import infixowl

from rdfformat.generator import constants
from rdfformat.generator import rdf_helper
from absl.testing import absltest


class RdfHelperLibTest(absltest.TestCase):

  def testClassHelper(self):
    graph = rdflib.Graph()
    updated_graph, clazz_object = rdf_helper.CreateClassInGraph(
        graph=graph,
        class_name='class_name',
        class_description='description',
        parent_clazz=rdflib.OWL.Thing)
    clazz = rdflib.URIRef(constants.DIGITAL_BUILDINGS_NS['class_name'])
    clazz_object_test = (clazz, rdflib.RDF.type, rdflib.OWL.Class)
    self.assertEqual(clazz_object, clazz_object_test)
    self.assertIn(clazz_object_test, updated_graph)
    self.assertIn((clazz, rdflib.RDFS.subClassOf, rdflib.OWL.Thing),
                  updated_graph)
    self.assertIn((clazz, rdflib.RDFS.label, rdflib.Literal('class_name')),
                  updated_graph)
    self.assertIn((clazz, rdflib.RDFS.comment, rdflib.Literal('description')),
                  updated_graph)

  def testClassHelperNoDescription(self):
    graph = rdflib.Graph()
    updated_graph, clazz_object = rdf_helper.CreateClassInGraph(
        graph=graph,
        class_name='class_name',
        class_description=None,
        parent_clazz=rdflib.OWL.Thing)
    clazz = rdflib.URIRef(constants.DIGITAL_BUILDINGS_NS['class_name'])
    clazz_object_test = (clazz, rdflib.RDF.type, rdflib.OWL.Class)
    self.assertEqual(clazz_object, clazz_object_test)
    self.assertIn(clazz_object_test, updated_graph)
    self.assertIn((clazz, rdflib.RDFS.subClassOf, rdflib.OWL.Thing),
                  updated_graph)
    self.assertIn((clazz, rdflib.RDFS.label, rdflib.Literal('class_name')),
                  updated_graph)
    self.assertNotIn((clazz, rdflib.RDFS.comment, rdflib.Literal('')),
                     updated_graph)

  def testInstanceHelper(self):
    graph = rdflib.Graph()
    updated_graph, clazz_object = rdf_helper.CreateClassInGraph(
        graph=graph,
        class_name='class_name',
        class_description='description',
        parent_clazz=rdflib.OWL.Thing)

    updated_graph, instance_object = rdf_helper.CreateInstanceInGraph(
        graph=updated_graph,
        instance_name='instance_name',
        instance_description='description',
        parent_clazz=clazz_object)
    instance = rdflib.URIRef(constants.DIGITAL_BUILDINGS_NS['instance_name'])
    instance_object_test = (instance, rdflib.RDF.type,
                            rdflib.OWL.NamedIndividual)
    self.assertEqual(instance_object, instance_object_test)
    self.assertIn(instance_object_test, updated_graph)
    self.assertIn((instance, rdflib.RDF.type, clazz_object[0]), updated_graph)
    self.assertIn(
        (instance, rdflib.RDFS.label, rdflib.Literal('instance_name')),
        updated_graph)
    self.assertIn(
        (instance, rdflib.RDFS.comment, rdflib.Literal('description')),
        updated_graph)

  def testInstanceHelperNoDescription(self):
    graph = rdflib.Graph()
    updated_graph, clazz_object = rdf_helper.CreateClassInGraph(
        graph=graph,
        class_name='class_name',
        class_description='description',
        parent_clazz=rdflib.OWL.Thing)
    updated_graph, instance_object = rdf_helper.CreateInstanceInGraph(
        graph=updated_graph,
        instance_name='instance_name',
        instance_description=None,
        parent_clazz=clazz_object)
    instance = rdflib.URIRef(constants.DIGITAL_BUILDINGS_NS['instance_name'])
    instance_object_test = (instance, rdflib.RDF.type,
                            rdflib.OWL.NamedIndividual)
    self.assertEqual(instance_object, instance_object_test)
    self.assertIn(instance_object_test, updated_graph)
    self.assertIn((instance, rdflib.RDF.type, clazz_object[0]), updated_graph)
    self.assertIn(
        (instance, rdflib.RDFS.label, rdflib.Literal('instance_name')),
        updated_graph)
    self.assertNotIn((instance, rdflib.RDFS.comment, rdflib.Literal('')),
                     updated_graph)

  def testDataPropertyHelper(self):
    data_property_name_test = rdflib.URIRef(
        constants.DIGITAL_BUILDINGS_NS['property_name'])
    data_property_object = (data_property_name_test, rdflib.RDF.type,
                            rdflib.OWL.DatatypeProperty)

    graph = rdflib.Graph()
    updated_graph, data_property_object_returned = \
        rdf_helper.CreateDataPropertyInGraph(
            graph,
            data_property_name='property_name',
            data_property_description='description')

    self.assertEqual(data_property_object_returned, data_property_object)
    self.assertIn(data_property_object, updated_graph)
    self.assertIn((data_property_name_test, rdflib.RDFS.label,
                   rdflib.Literal('property_name')), updated_graph)
    self.assertIn((data_property_name_test, rdflib.RDFS.comment,
                   rdflib.Literal('description')), updated_graph)

  def testDataPropertyHelperNoDescription(self):
    data_property_name_test = rdflib.URIRef(
        constants.DIGITAL_BUILDINGS_NS['property_name'])
    data_property_object = (data_property_name_test, rdflib.RDF.type,
                            rdflib.OWL.DatatypeProperty)

    graph = rdflib.Graph()
    updated_graph, data_property_object_returned = \
        rdf_helper.CreateDataPropertyInGraph(
            graph,
            data_property_name='property_name',
            data_property_description=None)

    self.assertEqual(data_property_object_returned, data_property_object)
    self.assertIn(data_property_object, updated_graph)
    self.assertIn((data_property_name_test, rdflib.RDFS.label,
                   rdflib.Literal('property_name')), updated_graph)
    self.assertNotIn(
        (data_property_name_test, rdflib.RDFS.comment, rdflib.Literal('')),
        updated_graph)

  def testHandlesStandardFieldName(self):
    standard_field_name = 'run_command'
    list_concepts = rdf_helper.DecomposeStandardFieldName(standard_field_name)
    self.assertIn('Run', list_concepts)
    self.assertIn('Command', list_concepts)

  def testHandlesStandardFieldNameNoLiterals(self):
    standard_field_name = 'run_command_1'
    list_concepts = rdf_helper.DecomposeStandardFieldName(standard_field_name)
    self.assertIn('Run', list_concepts)
    self.assertIn('Command', list_concepts)
    self.assertIsNot('1', list_concepts)

  def testHandlesStandardFieldNameNoSplit(self):
    standard_field_name = 'run'
    list_concepts = rdf_helper.DecomposeStandardFieldName(standard_field_name)
    self.assertIn('Run', list_concepts)

  def testCreatesImplementsInGraph(self):
    # Prepare data
    graph = rdflib.Graph()
    implements_list = ['CONTROL', 'MONITORING']
    applications_set = set()
    graph, application_class = rdf_helper.CreateClassInGraph(
        graph=graph,
        class_name='Application',
        class_description=None,
        parent_clazz=rdflib.OWL.Thing)

    graph, clazz_object = rdf_helper.CreateClassInGraph(
        graph=graph,
        class_name='clazz',
        class_description='description',
        parent_clazz=application_class[0])

    graph, applications_set = rdf_helper.CreatesImplementsInGraph(
        graph, implements_list, applications_set, application_class,
        clazz_object)

    # Assertions that the applications_set is updated
    self.assertIn('Control', applications_set)
    self.assertIn('Monitoring', applications_set)

    # Assertions for the class relations creations
    self.assertIn(
        (application_class[0], rdflib.RDFS.subClassOf, rdflib.OWL.Thing), graph)
    self.assertIn(
        (clazz_object[0], rdflib.RDFS.subClassOf, application_class[0]), graph)
    self.assertIn((clazz_object[0], rdflib.RDFS.subClassOf,
                   constants.DIGITAL_BUILDINGS_NS['Control']), graph)
    self.assertIn((clazz_object[0], rdflib.RDFS.subClassOf,
                   constants.DIGITAL_BUILDINGS_NS['Control']), graph)
    self.assertIn((constants.DIGITAL_BUILDINGS_NS['Control'],
                   rdflib.RDFS.subClassOf, application_class[0]), graph)
    self.assertIn((constants.DIGITAL_BUILDINGS_NS['Monitoring'],
                   rdflib.RDFS.subClassOf, application_class[0]), graph)

  def testCreatesStandardFieldNameCompositionInGraph(self):
    # Prepare data

    # Build First Graph with the method
    graph = rdflib.Graph()
    # Bind the OWL and Digital Buildings name spaces
    namespace_manager = namespace.NamespaceManager(graph)
    namespace_manager.bind('owl', rdflib.OWL)
    namespace_manager.bind('db', constants.DIGITAL_BUILDINGS_NS)
    graph.namespace_manager = namespace_manager
    list_composition = ['Cooling', 'Air', 'Flowrate', 'Sensor']
    standard_field_name = 'cooling_air_flowrate_sensor_1'
    is_composed_of_property = infixowl.Property(
        identifier=constants.DIGITAL_BUILDINGS_NS['isComposedOf'],
        baseType=infixowl.OWL_NS.ObjectProperty,
        graph=graph)
    point_type = infixowl.Class(
        identifier=constants.SUBFIELDS_NS['Point_type'], graph=graph)

    infixowl.Class(
        identifier=constants.SUBFIELDS_NS['Sensor'],
        graph=graph,
        subClassOf=[point_type])

    field = infixowl.Class(identifier=constants.FIELDS_NS['Field'], graph=graph)

    infixowl.Class(
        identifier=constants.FIELDS_NS['Cooling_air_flowrate_sensor_1'],
        graph=graph,
        subClassOf=[field])
    graph = rdf_helper.CreatesStandardFieldNameCompositionInGraph(
        list_composition=list_composition,
        standard_field_name=standard_field_name,
        is_composed_of_property=is_composed_of_property,
        graph=graph)

    # Build a second graph that is expected
    expected_graph = rdflib.Graph()
    # Bind the OWL and Digital Buildings name spaces
    namespace_manager_expected = namespace.NamespaceManager(expected_graph)
    namespace_manager_expected.bind('owl', rdflib.OWL)
    namespace_manager_expected.bind('db', constants.DIGITAL_BUILDINGS_NS)
    expected_graph.namespace_manager = namespace_manager_expected
    field_expected = infixowl.Class(
        identifier=constants.FIELDS_NS['Field'], graph=expected_graph)
    point_type_expected = infixowl.Class(
        identifier=constants.SUBFIELDS_NS['Point_type'], graph=expected_graph)
    cooling_expected = infixowl.Class(
        identifier=constants.SUBFIELDS_NS['Cooling'], graph=expected_graph)
    air_expected = infixowl.Class(
        identifier=constants.SUBFIELDS_NS['Air'], graph=expected_graph)
    flowrate_expected = infixowl.Class(
        identifier=constants.SUBFIELDS_NS['Flowrate'], graph=expected_graph)
    sensor_expected = infixowl.Class(
        identifier=constants.SUBFIELDS_NS['Sensor'],
        graph=expected_graph,
        subClassOf=[point_type_expected])
    sfn_expected = infixowl.Class(
        identifier=constants.FIELDS_NS['Cooling_air_flowrate_sensor_1'],
        graph=expected_graph,
        subClassOf=[field_expected])
    is_composed_of_property_expected = infixowl.Property(
        identifier=constants.DIGITAL_BUILDINGS_NS['isComposedOf'],
        baseType=infixowl.OWL_NS.ObjectProperty,
        graph=expected_graph)

    concat = sensor_expected & flowrate_expected
    concat += air_expected
    concat += cooling_expected
    sfn_expected.subClassOf = [
        is_composed_of_property_expected | infixowl.only | concat
    ]

    # Check if they are similar
    self.assertTrue(compare.similar(graph, expected_graph))

  def testCreatesCompositionInGraphAndOperator(self):
    # Prepare data

    # Build First Graph with the method
    graph = rdflib.Graph()
    # Bind the OWL and Digital Buildings name spaces
    namespace_manager = namespace.NamespaceManager(graph)
    namespace_manager.bind('owl', rdflib.OWL)
    namespace_manager.bind('db', constants.DIGITAL_BUILDINGS_NS)
    graph.namespace_manager = namespace_manager
    list_standard_field_name = ['cooling_air_flowrate_sensor_1', 'run_command']
    uses_property = infixowl.Property(
        identifier=constants.DIGITAL_BUILDINGS_NS['uses'],
        baseType=infixowl.OWL_NS.ObjectProperty,
        graph=graph)
    class_owl = infixowl.Class(
        identifier=constants.DIGITAL_BUILDINGS_NS['DFSS'], graph=graph)

    graph = rdf_helper.CreateCompositionInGraph(
        composition_operator='&',
        list_standard_field_names=list_standard_field_name,
        restriction=infixowl.only,
        composition_property=uses_property,
        class_owl=class_owl,
        graph=graph)

    # Build a second graph that is expected
    expected_graph = rdflib.Graph()
    # Bind the OWL and Digital Buildings name spaces
    namespace_manager_expected = namespace.NamespaceManager(expected_graph)
    namespace_manager_expected.bind('owl', rdflib.OWL)
    namespace_manager_expected.bind('db', constants.DIGITAL_BUILDINGS_NS)
    expected_graph.namespace_manager = namespace_manager_expected
    class_owl_expected = infixowl.Class(
        identifier=constants.DIGITAL_BUILDINGS_NS['DFSS'], graph=expected_graph)

    sfn1_expected = infixowl.Class(
        identifier=constants
        .DIGITAL_BUILDINGS_NS['Cooling_air_flowrate_sensor_1'],
        graph=expected_graph)
    sfn2_expected = infixowl.Class(
        identifier=constants.DIGITAL_BUILDINGS_NS['Run_command'],
        graph=expected_graph)
    uses_property_expected = infixowl.Property(
        identifier=constants.DIGITAL_BUILDINGS_NS['uses'],
        baseType=infixowl.OWL_NS.ObjectProperty,
        graph=expected_graph)

    concat = sfn1_expected & sfn2_expected
    class_owl_expected.subClassOf = [
        uses_property_expected | infixowl.only | concat
    ]

    # Check if they are similar
    self.assertTrue(compare.similar(graph, expected_graph))

  def testCreatesCompositionInGraphOrOperator(self):
    # Prepare data

    # Build First Graph with the method
    graph = rdflib.Graph()
    # Bind the OWL and Digital Buildings name spaces
    namespace_manager = namespace.NamespaceManager(graph)
    namespace_manager.bind('owl', rdflib.OWL)
    namespace_manager.bind('db', constants.DIGITAL_BUILDINGS_NS)
    graph.namespace_manager = namespace_manager
    list_standard_field_name = ['cooling_air_flowrate_sensor_1', 'run_command']
    uses_property = infixowl.Property(
        identifier=constants.DIGITAL_BUILDINGS_NS['uses'],
        baseType=infixowl.OWL_NS.ObjectProperty,
        graph=graph)
    class_owl = infixowl.Class(
        identifier=constants.DIGITAL_BUILDINGS_NS['DFSS'], graph=graph)

    graph = rdf_helper.CreateCompositionInGraph(
        composition_operator='|',
        list_standard_field_names=list_standard_field_name,
        restriction=infixowl.only,
        composition_property=uses_property,
        class_owl=class_owl,
        graph=graph)

    # Build a second graph that is expected
    expected_graph = rdflib.Graph()
    # Bind the OWL and Digital Buildings name spaces
    namespace_manager_expected = namespace.NamespaceManager(expected_graph)
    namespace_manager_expected.bind('owl', rdflib.OWL)
    namespace_manager_expected.bind('db', constants.DIGITAL_BUILDINGS_NS)
    expected_graph.namespace_manager = namespace_manager_expected
    class_owl_expected = infixowl.Class(
        identifier=constants.DIGITAL_BUILDINGS_NS['DFSS'], graph=expected_graph)

    sfn1_expected = infixowl.Class(
        identifier=constants
        .DIGITAL_BUILDINGS_NS['Cooling_air_flowrate_sensor_1'],
        graph=expected_graph)
    sfn2_expected = infixowl.Class(
        identifier=constants.DIGITAL_BUILDINGS_NS['Run_command'],
        graph=expected_graph)
    uses_property_expected = infixowl.Property(
        identifier=constants.DIGITAL_BUILDINGS_NS['uses'],
        baseType=infixowl.OWL_NS.ObjectProperty,
        graph=expected_graph)

    concat = sfn1_expected | sfn2_expected
    class_owl_expected.subClassOf = [
        uses_property_expected | infixowl.only | concat
    ]

    # Check if they are similar
    self.assertTrue(compare.similar(graph, expected_graph))

  def testCreatesCompositionInGraphSomeRestriction(self):
    # Prepare data

    # Build First Graph with the method
    graph = rdflib.Graph()
    # Bind the OWL and Digital Buildings name spaces
    namespace_manager = namespace.NamespaceManager(rdflib.Graph())
    namespace_manager.bind('owl', rdflib.OWL)
    namespace_manager.bind('db', constants.DIGITAL_BUILDINGS_NS)
    graph.namespace_manager = namespace_manager
    list_standard_field_name = ['cooling_air_flowrate_sensor_1', 'run_command']
    uses_property = infixowl.Property(
        identifier=constants.DIGITAL_BUILDINGS_NS['uses'],
        baseType=infixowl.OWL_NS.ObjectProperty,
        graph=graph)
    class_owl = infixowl.Class(
        identifier=constants.DIGITAL_BUILDINGS_NS['DFSS'], graph=graph)

    graph = rdf_helper.CreateCompositionInGraph(
        composition_operator='|',
        list_standard_field_names=list_standard_field_name,
        restriction=infixowl.some,
        composition_property=uses_property,
        class_owl=class_owl,
        graph=graph)

    # Build a second graph that is expected
    expected_graph = rdflib.Graph()
    # Bind the OWL and Digital Buildings name spaces
    namespace_manager_expected = namespace.NamespaceManager(rdflib.Graph())
    namespace_manager_expected.bind('owl', rdflib.OWL)
    namespace_manager_expected.bind('db', constants.DIGITAL_BUILDINGS_NS)
    expected_graph.namespace_manager = namespace_manager_expected
    class_owl_expected = infixowl.Class(
        identifier=constants.DIGITAL_BUILDINGS_NS['DFSS'], graph=expected_graph)

    sfn1_expected = infixowl.Class(
        identifier=constants
        .DIGITAL_BUILDINGS_NS['Cooling_air_flowrate_sensor_1'],
        graph=expected_graph)
    sfn2_expected = infixowl.Class(
        identifier=constants.DIGITAL_BUILDINGS_NS['Run_command'],
        graph=expected_graph)
    uses_property_expected = infixowl.Property(
        identifier=constants.DIGITAL_BUILDINGS_NS['uses'],
        baseType=infixowl.OWL_NS.ObjectProperty,
        graph=expected_graph)

    concat = sfn1_expected | sfn2_expected
    class_owl_expected.subClassOf = [
        uses_property_expected | infixowl.some | concat
    ]

    # Check if they are similar
    self.assertTrue(compare.similar(graph, expected_graph))


if __name__ == '__main__':
  absltest.main()
