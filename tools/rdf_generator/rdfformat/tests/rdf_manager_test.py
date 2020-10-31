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

"""Tests for generator.rdf_manager."""

import rdflib

from rdfformat.generator import constants
from rdfformat.generator import rdf_manager
from absl.testing import absltest

# Override the Facilities.yaml file
rdf_manager.FACILITIES = '/Facilities.yaml'
rdf_manager.UNITS = '/units.yaml'
rdf_manager.SUBFIELDS = '/subfields.yaml'
rdf_manager.STATES = '/states.yaml'
rdf_manager.ABSTRACT = '/Abstract.yaml'
rdf_manager.GENERALTYPES = '/GeneralTypes.yaml'
rdf_manager.FAN = '/FAN.yaml'
rdf_manager.PMP = '/PUMP.yaml'
rdf_manager.FCU = '/FCU.yaml'
rdf_manager.VAV = '/VAV.yaml'
rdf_manager.carson_types = {
    rdf_manager.FAN, rdf_manager.PMP, rdf_manager.FCU, rdf_manager.VAV
}


class RdfManagerTest(absltest.TestCase):

  def testManagerGenerate(self):
    resource_path = 'fake_resources'
    generated_graph = rdf_manager.Generate(resource_path)

    ## Make sure Facilities are generated in the graph
    # Main Types
    entity_type = rdflib.URIRef(constants.DIGITAL_BUILDINGS_NS['EntityType'])
    physical_location = rdflib.URIRef(
        constants.FACILITIES_NS['PhysicalLocation'])
    has_physical_location = rdflib.URIRef(
        constants.DIGITAL_BUILDINGS_NS['hasPhysicalLocation'])

    # Main Classes
    physical_location_class = (physical_location, rdflib.RDF.type,
                               rdflib.OWL.Class)

    # Assertions
    # Class assertions
    self.assertIn(physical_location_class, generated_graph)

    # SubClasses assertions
    self.assertIn((physical_location, rdflib.RDFS.subClassOf, entity_type),
                  generated_graph)

    # Relations assertions
    self.assertIn(
        (has_physical_location, rdflib.RDF.type, rdflib.OWL.ObjectProperty),
        generated_graph)

    ## Make sure Units are generated in the graph
    # Main Types
    unit = rdflib.URIRef(constants.UNITS_NS['Unit'])
    temperature = rdflib.URIRef(constants.UNITS_NS['Temperature'])
    degrees_celsius = rdflib.URIRef(constants.UNITS_NS['degrees_celsius'])
    is_standard_unit = rdflib.URIRef(
        constants.DIGITAL_BUILDINGS_NS['is_standard_unit'])
    is_standard_unit_degrees_celsius = (degrees_celsius, is_standard_unit,
                                        rdflib.Literal(False))

    # Classes Under Test
    unit_class = (unit, rdflib.RDF.type, rdflib.OWL.Class)
    temperature_class = (temperature, rdflib.RDF.type, rdflib.OWL.Class)

    # Data Properties Under Test
    is_standard_unit_object = (is_standard_unit, rdflib.RDF.type,
                               rdflib.OWL.DatatypeProperty)

    # Instances Under Test
    degrees_celsius_object = (degrees_celsius, rdflib.RDF.type,
                              rdflib.OWL.NamedIndividual)

    # Assertions
    # Class assertions
    self.assertIn(unit_class, generated_graph)
    self.assertIn(temperature_class, generated_graph)

    # SubClass assertions
    self.assertIn((unit, rdflib.RDFS.subClassOf, rdflib.OWL.Thing),
                  generated_graph)
    self.assertIn((temperature, rdflib.RDFS.subClassOf, unit), generated_graph)

    # Instance assertions
    self.assertIn(degrees_celsius_object, generated_graph)
    self.assertIn((degrees_celsius, rdflib.RDF.type, temperature),
                  generated_graph)

    # Data Property assertions
    self.assertIn(is_standard_unit_object, generated_graph)
    self.assertIn(is_standard_unit_degrees_celsius, generated_graph)

    ## Make sure subfields are generated in the graph
    # Main types
    aggregation = rdflib.URIRef(constants.SUBFIELDS_NS['Aggregation'])
    subfield = rdflib.URIRef(constants.SUBFIELDS_NS['SubField'])
    max_ref = rdflib.URIRef(constants.SUBFIELDS_NS['Max'])
    min_ref = rdflib.URIRef(constants.SUBFIELDS_NS['Min'])

    self.assertIn((aggregation, rdflib.RDFS.subClassOf, subfield),
                  generated_graph)
    self.assertIn((min_ref, rdflib.RDFS.subClassOf, aggregation),
                  generated_graph)
    self.assertIn((max_ref, rdflib.RDFS.subClassOf, aggregation),
                  generated_graph)

    ## Make sure Abstract are generated in the graph
    # Main types
    application = rdflib.URIRef(constants.DIGITAL_BUILDINGS_NS['Application'])
    functionality = rdflib.URIRef(constants.HVAC_NS['Functionality'])
    point_type = rdflib.URIRef(constants.SUBFIELDS_NS['Point_type'])
    sensor = rdflib.URIRef(constants.SUBFIELDS_NS['Sensor'])
    is_composed_of = rdflib.URIRef(
        constants.DIGITAL_BUILDINGS_NS['isComposedOf'])
    uses = rdflib.URIRef(constants.DIGITAL_BUILDINGS_NS['uses'])
    uses_optional = rdflib.URIRef(
        constants.DIGITAL_BUILDINGS_NS['usesOptional'])

    self.assertIn((application, rdflib.RDFS.subClassOf, entity_type),
                  generated_graph)
    self.assertIn((functionality, rdflib.RDFS.subClassOf, entity_type),
                  generated_graph)
    self.assertIn((point_type, rdflib.RDFS.subClassOf, subfield),
                  generated_graph)
    self.assertIn((sensor, rdflib.RDFS.subClassOf, point_type), generated_graph)
    # Relations assertions
    self.assertIn((is_composed_of, rdflib.RDF.type, rdflib.OWL.ObjectProperty),
                  generated_graph)
    self.assertIn((uses, rdflib.RDF.type, rdflib.OWL.ObjectProperty),
                  generated_graph)
    self.assertIn((uses_optional, rdflib.RDF.type, rdflib.OWL.ObjectProperty),
                  generated_graph)

    ## Make sure GeneralTypes are generated in the graph
    # Main types
    vav = rdflib.URIRef(constants.HVAC_NS['Vav'])
    vav_description = 'Tag for terminal units with variable volume control.'

    # Main Classes
    vav_class = (vav, rdflib.RDF.type, rdflib.OWL.Class)

    # Assertions
    # Class assertions that the VAV has been created
    self.assertIn(vav_class, generated_graph)
    self.assertIn((vav, rdflib.RDFS.comment, rdflib.Literal(vav_description)),
                  generated_graph)

    ## Make sure FANs are generated in the graph
    fan_ss_refm_csp = rdflib.URIRef(constants.HVAC_NS['Fan_ss_refm_csp'])

    # Main Classes
    fan_ss_refm_csp_class = (fan_ss_refm_csp, rdflib.RDF.type, rdflib.OWL.Class)

    # Assertions
    # Class assertions
    self.assertIn(fan_ss_refm_csp_class, generated_graph)

    ## Make sure VAVs are generated in the graph
    vav_sd = rdflib.URIRef(constants.HVAC_NS['Vav_sd'])

    # Main Classes
    vav_sd_class = (vav_sd, rdflib.RDF.type, rdflib.OWL.Class)

    # Assertions
    # Class assertions
    self.assertIn(vav_sd_class, generated_graph)

    ## Make sure Pumps are generated in the graph
    pump = rdflib.URIRef(constants.HVAC_NS['Pump_ss_vsc_cm'])

    # Main Classes
    pump_class = (pump, rdflib.RDF.type, rdflib.OWL.Class)

    # Assertions
    # Class assertions
    self.assertIn(pump_class, generated_graph)

    ## Make sure an FCU with incomplete is not generated in the graph
    fcu = rdflib.URIRef(
        constants.HVAC_NS['FCU_DFST_VSC_DSP_CH_DTC'.capitalize()])

    # Main Classes
    fcu_class = (fcu, rdflib.RDF.type, rdflib.OWL.Class)

    # Assertions
    # Class assertions
    self.assertNotIn(fcu_class, generated_graph)

    ## Make sure states are generated
    # Main Types
    state = rdflib.URIRef(constants.STATES_NS['State'])
    on = rdflib.URIRef(constants.STATES_NS['On'])
    off = rdflib.URIRef(constants.STATES_NS['Off'])

    # Main Classes
    state_class = (state, rdflib.RDF.type, rdflib.OWL.Class)
    on_class = (on, rdflib.RDF.type, rdflib.OWL.Class)
    off_class = (off, rdflib.RDF.type, rdflib.OWL.Class)

    # Assertions
    # Class assertions
    self.assertIn(state_class, generated_graph)
    self.assertIn(on_class, generated_graph)
    self.assertIn(off_class, generated_graph)


if __name__ == '__main__':
  absltest.main()
