"""Testing module for ontology.py"""
from absl.testing import absltest

from yamlformat.validator.external_file_lib import RecursiveDirWalk
from yamlformat.validator import presubmit_validate_types_lib
from yamlformat.validator import namespace_validator as nv

from lib.ontology_wrapper import OntologyWrapper
from lib.model import EntityTypeField
from lib.tests import test_constants

class OntologyTest(absltest.TestCase):

  def setUp(self):
    super(OntologyTest, self).setUp()
    self.yaml = RecursiveDirWalk(test_constants.ONTOLOGY_ROOT)
    self.config = presubmit_validate_types_lib.SeparateConfigFiles(self.yaml)
    self.universe = presubmit_validate_types_lib.BuildUniverse(self.config)
    nv.NamespaceValidator(self.universe.GetEntityTypeNamespaces())
    self.ontology = OntologyWrapper(self.universe)

  def testGetAllFieldsForTypeName(self):
    expected_output = [
        EntityTypeField('', 'zone_use_label', True),
        EntityTypeField('', 'run_command', True),
        EntityTypeField('', 'manufacturer_label', True),
        EntityTypeField('', 'model_label', True),
        EntityTypeField('', 'supply_air_cooling_flowrate_capacity', True),
        EntityTypeField(
            '',
            'supply_air_ventilation_flowrate_requirement',
            True
        ),
        EntityTypeField('', 'supply_air_heating_flowrate_capacity', True),
        EntityTypeField('', 'cooling_thermal_power_capacity', True),
        EntityTypeField('', 'supply_air_temperature_sensor', True),
        EntityTypeField('', 'supply_air_flowrate_sensor', False),
        EntityTypeField('', 'supply_air_flowrate_setpoint', False),
        EntityTypeField('', 'supply_air_damper_percentage_command', False),
        EntityTypeField('', 'discharge_air_temperature_sensor', True),
        EntityTypeField('', 'zone_air_relative_humidity_sensor', True),
        EntityTypeField('', 'zone_air_temperature_sensor', False),
        EntityTypeField('', 'zone_air_cooling_temperature_setpoint', False),
        EntityTypeField('', 'zone_air_heating_temperature_setpoint', False),
        EntityTypeField('', 'zone_air_co2_concentration_sensor', False),
        EntityTypeField('', 'zone_air_co2_concentration_setpoint', False)
    ]
    expected_output_sorted = sorted(
        expected_output,
        key=lambda x: x.GetStandardFieldName(),
        reverse=False
    )

    function_output = self.ontology.GetFieldsForTypeName(
        'HVAC',
        'VAV_SD_DSP_CO2C'
    )
    function_output_sorted = sorted(
        function_output,
        key=lambda x: x.GetStandardFieldName(),
        reverse=False
    )

    self.assertEqual(function_output_sorted, expected_output_sorted)

  def testGetRequiredFieldsForTypeName(self):
    expected_output = [
        EntityTypeField('', 'supply_air_flowrate_sensor', False),
        EntityTypeField('', 'supply_air_flowrate_setpoint', False),
        EntityTypeField('', 'supply_air_damper_percentage_command', False),
        EntityTypeField('', 'zone_air_temperature_sensor', False),
        EntityTypeField('', 'zone_air_cooling_temperature_setpoint', False),
        EntityTypeField('', 'zone_air_heating_temperature_setpoint', False),
        EntityTypeField('', 'zone_air_co2_concentration_sensor', False),
        EntityTypeField('', 'zone_air_co2_concentration_setpoint', False)
    ]
    expected_output_sorted = sorted(
        expected_output,
        key=lambda x: x.GetStandardFieldName(),
        reverse=False
    )

    function_output = self.ontology.GetFieldsForTypeName(
        namespace='HVAC',
        entity_type_name='VAV_SD_DSP_CO2C',
        required_only=True
    )
    function_output_sorted = sorted(
        function_output,
        key=lambda x: x.GetStandardFieldName(),
        reverse=False
    )

    self.assertEqual(function_output_sorted, expected_output_sorted)

  def testGetEntityTypesFromFields(self):
    pass

  def testValidField(self):
    pass

  def testInvalidField(self):
    pass

if __name__ == '__main__':
  absltest.main()
