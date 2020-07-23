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

"""Tests for generator.rdf_subfields_handler."""

import rdflib
from rdflib import namespace

from rdfformat.generator import constants
from rdfformat.generator import rdf_helper
from rdfformat.generator import rdflib_subfields_handler
from rdfformat.generator import yaml_handler
from absl.testing import absltest


class RdfSubfieldsHandlerTest(absltest.TestCase):

  def testSubfieldsGraphGeneration(self):

    fake_units = 'fake_resources/subfields.yaml'

    file_contents = rdf_helper.ReadFile(fake_units)

    yaml_subfields = yaml_handler.ImportYamlFiles(file_contents)

    # Create global graph
    graph = rdflib.Graph()

    # Bind the OWL and Digital Buildings name spaces
    namespace_manager = namespace.NamespaceManager(graph)
    namespace_manager.bind('owl', namespace.OWL)
    namespace_manager.bind('db', constants.DIGITAL_BUILDINGS_NS)
    graph.namespace_manager = namespace_manager

    g_subfields = rdflib_subfields_handler.GenerateGraph(yaml_subfields, graph)

    # Main Types
    subfield_type = rdflib.URIRef(constants.SUBFIELDS_NS['SubField'])
    point_type = rdflib.URIRef(constants.SUBFIELDS_NS['Point_type'])
    capacity = rdflib.URIRef(constants.SUBFIELDS_NS['Capacity'])
    capacity_description = ('A design parameter quantity. Ex: design motor '
                            'power capacity. Is always a maximum limit.')
    point_type_class = (point_type, rdflib.RDF.type, rdflib.OWL.Class)
    capacity_class = (capacity, rdflib.RDF.type, rdflib.OWL.Class)

    measurement_descriptor = rdflib.URIRef(
        constants.SUBFIELDS_NS['Measurement_descriptor'])
    absolute = rdflib.URIRef(constants.SUBFIELDS_NS['Absolute'])
    absolute_description = ('Quality of media with respect to non-relativistic '
                            'boudaries (e.g. absolute temperature).')
    measurement_descriptor_class = (measurement_descriptor, rdflib.RDF.type,
                                    rdflib.OWL.Class)
    absolute_class = (absolute, rdflib.RDF.type, rdflib.OWL.Class)

    measurement = rdflib.URIRef(constants.SUBFIELDS_NS['Measurement'])
    concentration = rdflib.URIRef(constants.SUBFIELDS_NS['Concentration'])
    concentration_description = ('Concentration of chemical (usually in parts '
                                 'per million or parts per billion).')
    measurement_class = (measurement, rdflib.RDF.type, rdflib.OWL.Class)
    concentration_class = (concentration, rdflib.RDF.type, rdflib.OWL.Class)

    descriptor = rdflib.URIRef(constants.SUBFIELDS_NS['Descriptor'])
    air = rdflib.URIRef(constants.SUBFIELDS_NS['Air'])
    air_description = 'Atmospheric air, either conditioned or unconditioned'
    descriptor_class = (descriptor, rdflib.RDF.type, rdflib.OWL.Class)
    air_class = (air, rdflib.RDF.type, rdflib.OWL.Class)

    component = rdflib.URIRef(constants.SUBFIELDS_NS['Component'])
    coil = rdflib.URIRef(constants.SUBFIELDS_NS['Coil'])
    coil_description = ('Component that exchanges heat between two media '
                        'streams.')
    component_class = (component, rdflib.RDF.type, rdflib.OWL.Class)
    coil_class = (coil, rdflib.RDF.type, rdflib.OWL.Class)

    aggregation = rdflib.URIRef(constants.SUBFIELDS_NS['Aggregation'])
    max_ref = rdflib.URIRef(constants.SUBFIELDS_NS['Max'])
    min_ref = rdflib.URIRef(constants.SUBFIELDS_NS['Min'])
    max_description = 'Maximum value (e.g. Max_Cooling_Air_Flow_Setpoint)'
    aggregation_class = (aggregation, rdflib.RDF.type, rdflib.OWL.Class)
    max_class = (max_ref, rdflib.RDF.type, rdflib.OWL.Class)
    min_class = (min_ref, rdflib.RDF.type, rdflib.OWL.Class)

    # Assertions
    self.assertIn(capacity_class, g_subfields)
    self.assertIn(point_type_class, g_subfields)
    self.assertIn(
        (capacity, rdflib.RDFS.comment, rdflib.Literal(capacity_description)),
        g_subfields)

    self.assertIn(measurement_descriptor_class, g_subfields)
    self.assertIn(absolute_class, g_subfields)
    self.assertIn(
        (absolute, rdflib.RDFS.comment, rdflib.Literal(absolute_description)),
        g_subfields)

    self.assertIn(measurement_class, g_subfields)
    self.assertIn(concentration_class, g_subfields)
    self.assertIn((concentration, rdflib.RDFS.comment,
                   rdflib.Literal(concentration_description)), g_subfields)

    self.assertIn(descriptor_class, g_subfields)
    self.assertIn(air_class, g_subfields)
    self.assertIn((air, rdflib.RDFS.comment, rdflib.Literal(air_description)),
                  g_subfields)

    self.assertIn(component_class, g_subfields)
    self.assertIn(coil_class, g_subfields)
    self.assertIn((coil, rdflib.RDFS.comment, rdflib.Literal(coil_description)),
                  g_subfields)

    self.assertIn(aggregation_class, g_subfields)
    self.assertIn(min_class, g_subfields)
    self.assertIn(max_class, g_subfields)
    self.assertIn(
        (max_ref, rdflib.RDFS.comment, rdflib.Literal(max_description)),
        g_subfields)

    # SubClasses assertions
    self.assertIn((point_type, rdflib.RDFS.subClassOf, subfield_type),
                  g_subfields)
    self.assertIn((capacity, rdflib.RDFS.subClassOf, point_type), g_subfields)

    self.assertIn((aggregation, rdflib.RDFS.subClassOf, subfield_type),
                  g_subfields)
    self.assertIn((min_ref, rdflib.RDFS.subClassOf, aggregation), g_subfields)
    self.assertIn((max_ref, rdflib.RDFS.subClassOf, aggregation), g_subfields)


if __name__ == '__main__':
  absltest.main()
