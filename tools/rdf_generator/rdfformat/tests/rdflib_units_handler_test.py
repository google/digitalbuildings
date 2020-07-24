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

"""Tests for generator.rdflib_units_handler."""

import rdflib

from rdfformat.generator import constants
from rdfformat.generator import rdf_helper
from rdfformat.generator import rdflib_units_handler
from rdfformat.generator import yaml_handler
from absl.testing import absltest


class RdfUnitHandlerTest(absltest.TestCase):

  def testUnitGraphGeneration(self):

    fake_units = 'fake_resources/units.yaml'

    file_contents = rdf_helper.ReadFile(fake_units)

    yaml_units = yaml_handler.ImportYamlFiles(file_contents)

    # Create global graph
    graph = rdflib.Graph()

    # Bind the OWL and Digital Buildings name spaces
    namespace_manager = rdflib.namespace.NamespaceManager(graph)
    namespace_manager.bind('owl', rdflib.OWL)
    namespace_manager.bind('db', constants.DIGITAL_BUILDINGS_NS)
    graph.namespace_manager = namespace_manager

    g_units = rdflib_units_handler.GenerateGraph(yaml_units, graph)

    # Main Types
    unit = rdflib.URIRef(constants.UNITS_NS['Unit'])
    temperature = rdflib.URIRef(constants.UNITS_NS['Temperature'])
    degrees_celsius = rdflib.URIRef(constants.UNITS_NS['degrees_celsius'])
    degrees_fahrenheit = rdflib.URIRef(constants.UNITS_NS['degrees_fahrenheit'])
    kelvins = rdflib.URIRef(constants.UNITS_NS['kelvins'])
    is_standard_unit = rdflib.URIRef(
        constants.DIGITAL_BUILDINGS_NS['is_standard_unit'])
    is_standard_unit_degrees_celsius = (degrees_celsius, is_standard_unit,
                                        rdflib.Literal(False))
    is_standard_unit_degrees_fahrenheit = (degrees_fahrenheit, is_standard_unit,
                                           rdflib.Literal(False))
    is_standard_unit_kelvin = (kelvins, is_standard_unit, rdflib.Literal(True))

    # Classes Under Test
    unit_class = (unit, rdflib.RDF.type, rdflib.OWL.Class)
    temperature_class = (temperature, rdflib.RDF.type, rdflib.OWL.Class)

    # Data Properties Under Test
    is_standard_unit_object = (is_standard_unit, rdflib.RDF.type,
                               rdflib.OWL.DatatypeProperty)

    # Instances Under Test
    degrees_celsius_object = (degrees_celsius, rdflib.RDF.type,
                              rdflib.OWL.NamedIndividual)
    degrees_fahrenheit_object = (degrees_fahrenheit, rdflib.RDF.type,
                                 rdflib.OWL.NamedIndividual)
    kelvins_object = (kelvins, rdflib.RDF.type, rdflib.OWL.NamedIndividual)

    # Assertions
    # Class assertions
    self.assertIn(unit_class, g_units)
    self.assertIn(temperature_class, g_units)

    # SubClass assertions
    self.assertIn((unit, rdflib.RDFS.subClassOf, rdflib.OWL.Thing), g_units)
    self.assertIn((temperature, rdflib.RDFS.subClassOf, unit), g_units)

    # Instance assertions
    self.assertIn(degrees_celsius_object, g_units)
    self.assertIn(degrees_fahrenheit_object, g_units)
    self.assertIn(kelvins_object, g_units)
    self.assertIn((degrees_celsius, rdflib.RDF.type, temperature), g_units)
    self.assertIn((degrees_fahrenheit, rdflib.RDF.type, temperature), g_units)
    self.assertIn((kelvins, rdflib.RDF.type, temperature), g_units)

    # Data Property assertions
    self.assertIn(is_standard_unit_object, g_units)
    self.assertIn(is_standard_unit_degrees_celsius, g_units)
    self.assertIn(is_standard_unit_degrees_fahrenheit, g_units)
    self.assertIn(is_standard_unit_kelvin, g_units)


if __name__ == '__main__':
  absltest.main()
