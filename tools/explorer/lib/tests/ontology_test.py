"""Testing module for ontology.py"""
from absl.testing import absltest

from yamlformat.validator.external_file_lib import RecursiveDirWalk
from yamlformat.validator import presubmit_validate_types_lib
from yamlformat.validator import namespace_validator as nv
from yamlformat import constants

from lib.ontology import Ontology
from lib.model import EntityTypeField
from lib.model import StandardField
from lib import model

class OntologyTest(absltest.TestCase):

  def setUp(self):
    super(OntologyTest, self).setUp()
    self.yaml = RecursiveDirWalk(constants.ONTOLOGY_ROOT)
    self.config = presubmit_validate_types_lib.SeparateConfigFiles(self.yaml)
    self.universe = presubmit_validate_types_lib.BuildUniverse(self.config)
    nv.NamespaceValidator(self.universe.GetEntityTypeNamespaces())
    self.ontology = Ontology(self.universe)

  def testGetAllFieldsForTypeName(self):
    field_list = [
        EntityTypeField('HVAC', 'zone_use_label', False),
        EntityTypeField('HVAC', 'run_command', False),
        EntityTypeField('HVAC', 'manufacturer_label', False),
        EntityTypeField('HVAC', 'model_label', False),
        EntityTypeField('HVAC', 'supply_air_cooling_flowrate_capacity', False),
        EntityTypeField(
            'HVAC',
            'supply_air_ventilation_flowrate_requirement',
            False
        ),
        EntityTypeField('HVAC', 'supply_air_heating_flowrate_capacity', False),
        EntityTypeField('HVAC', 'cooling_thermal_power_capacity', False),
        EntityTypeField('HVAC', 'supply_air_temperature_sensor', False),
        EntityTypeField('HVAC', 'supply_air_flowrate_sensor', True),
        EntityTypeField('HVAC', 'supply_air_flowrate_setpoint', True),
        EntityTypeField('HVAC', 'supply_air_damper_percentage_command', True),
        EntityTypeField('HVAC', 'discharge_air_temperature_sensor', False),
        EntityTypeField('HVAC', 'zone_air_relative_humidity_sensor', False),
        EntityTypeField('HVAC', 'zone_air_temperature_sensor', True),
        EntityTypeField('HVAC', 'zone_air_cooling_temperature_setpoint', True),
        EntityTypeField('HVAC', 'zone_air_heating_temperature_setpoint', True),
        EntityTypeField('HVAC', 'zone_air_co2_concentration_sensor', True),
        EntityTypeField('HVAC', 'zone_air_co2_concentration_setpoint', True)
    ]
    function_output = self.ontology.GetFieldsForTypeName(
        'HVAC',
        'VAV_SD_DSP_CO2C'
    )
    field_list_sorted = sorted(
        field_list,
        key=lambda x: x.GetStandardFieldName(),
        reverse=False
    )
    function_output_sorted = sorted(
        function_output,
        key=lambda x: x.GetStandardFieldName(),
        reverse=False
    )
    self.assertEqual(function_output_sorted, field_list_sorted)

  def testGetRequiredFieldsForTypeName(self):
    field_list = [
        EntityTypeField('HVAC', 'supply_air_flowrate_sensor', True),
        EntityTypeField('HVAC', 'supply_air_flowrate_setpoint', True),
        EntityTypeField('HVAC', 'supply_air_damper_percentage_command', True),
        EntityTypeField('HVAC', 'zone_air_temperature_sensor', True),
        EntityTypeField('HVAC', 'zone_air_cooling_temperature_setpoint', True),
        EntityTypeField('HVAC', 'zone_air_heating_temperature_setpoint', True),
        EntityTypeField('HVAC', 'zone_air_co2_concentration_sensor', True),
        EntityTypeField('HVAC', 'zone_air_co2_concentration_setpoint', True)
    ]
    function_output = self.ontology.GetFieldsForTypeName(
        'HVAC',
        'VAV_SD_DSP_CO2C',
        True
    )
    field_list_sorted = sorted(
        field_list,
        key=lambda x: x.GetStandardFieldName(),
        reverse=False
    )
    function_output_sorted = sorted(
        function_output,
        key=lambda x: x.GetStandardFieldName(),
        reverse=False
    )

    self.assertEqual(function_output_sorted, field_list_sorted)

  def testGetEntityTypesFromFields(self):
    field_list = self.ontology.GetFieldsForTypeName(
        'HVAC',
        'VAV_SD_DSP'
    )
    field_list = model.ConvertETFtoSF(field_list)
    function_output = self.ontology.GetEntityTypesFromFields(
        field_list=field_list,
        match_type='EXACT'
    )
    my_entity_type_list = []
    my_entity_type_list.append(self.universe.entity_type_universe.GetEntityType(
        'HVAC',
        'VAV_SD_DSP'
    ))
    self.assertEqual(function_output, my_entity_type_list)

  def testValidField(self):
    my_field = StandardField('HVAC', 'supply_air_flowrate_sensor')
    function_output = self.ontology.IsFieldValid(my_field)
    self.assertEqual(function_output, True)

  def testInvalidField(self):
    my_field = StandardField('ELECTRICAL', 'failed_alarm')
    function_output = self.ontology.IsFieldValid(my_field)
    self.assertEqual(function_output, False)

if __name__ == '__main__':
  absltest.main()
