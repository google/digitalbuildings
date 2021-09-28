"""Testing module for model.py"""
from absl.testing import absltest

from lib.model import StandardField
from lib.model import EntityTypeField
from lib.model import Match
from lib.model import StandardizeField
from lib.tests import test_constants

from yamlformat.validator.entity_type_lib import EntityType
from yamlformat.validator.external_file_lib import RecursiveDirWalk
from yamlformat.validator import presubmit_validate_types_lib
from yamlformat.validator import namespace_validator as nv

class StandardFieldTest(absltest.TestCase):
  def setUp(self):
    self.test_standard_field = StandardField(
        namespace_name='',
        standard_field_name='supply_air_flowrate_sensor'
    )

  def testGetNamespaceName(self):
    expected_output = ''
    function_output = self.test_standard_field.GetNamespaceName()

    self.assertEqual(function_output, expected_output)

  def testGetStandardFieldName(self):
    expected_output = 'supply_air_flowrate_sensor'
    function_output = self.test_standard_field.GetStandardFieldName()

    self.assertEqual(function_output, expected_output)

class EntityTypeFieldTest(absltest.TestCase):
  def setUp(self):
    self.test_entity_type_field = EntityTypeField(
        namespace_name='',
        standard_field_name='supply_air_flowrate_sensor',
        is_optional=False,
        increment=''
    )

  def testGetIncrement(self):
    expected_output = ''
    function_output = self.test_entity_type_field.GetIncrement()

    self.assertEqual(function_output, expected_output)

  def testIsOptional(self):
    self.assertFalse(self.test_entity_type_field.IsOptional())

  def testStandardizeField(self):
    expected_output = StandardField(
        namespace_name='',
        standard_field_name='supply_air_flowrate_sensor'
    )

    function_output = StandardizeField(self.test_entity_type_field)

    self.assertEqual(function_output, expected_output)

class ModelTest(absltest.TestCase):
  def setUp(self):
    self.yaml = RecursiveDirWalk(test_constants.ONTOLOGY_ROOT)
    self.config = presubmit_validate_types_lib.SeparateConfigFiles(self.yaml)
    self.universe = presubmit_validate_types_lib.BuildUniverse(self.config)
    nv.NamespaceValidator(self.universe.GetEntityTypeNamespaces())
    test_entity_type = self.universe.entity_type_universe.GetEntityType(
        namespace_name='HVAC',
        typename='ZONE_HVAC'
    )
    test_field_list = [
        EntityTypeField(
            namespace_name=optwrapper.field.namespace,
            standard_field_name=optwrapper.field.field[0:],
            is_optional=optwrapper.optional,
            increment=optwrapper.field.increment
        ) for optwrapper in test_entity_type.GetAllFields().values()
    ]
    self.test_match = Match(
        field_list=test_field_list,
        entity_type=test_entity_type,
        match_type='EXACT'
    )

  def testGetFieldList(self):
    #print(test_constants.ONTOLOGY_ROOT)
    #print(self.universe.entity_type_universe.type_namespaces_map)
    expected_output = [
        EntityTypeField(
            namespace_name='',
            standard_field_name='zone_use_label',
            is_optional=True,
            increment=''
        )
    ]

    function_output = self.test_match.GetFieldList()

    self.assertEqual(function_output, expected_output)

  def testGetEntityType(self):
    function_output = self.test_match.GetEntityType()

    self.assertTrue(isinstance(function_output, EntityType))
    self.assertEqual(function_output.typename, 'ZONE_HVAC')

  def testGetMatchType(self):
    function_output = self.test_match.GetMatchType()

    self.assertEqual(function_output, 'EXACT')

if __name__ == '__main__':
  absltest.main()
