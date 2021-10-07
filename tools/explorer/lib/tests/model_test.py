"""Testing module for model.py."""
from absl.testing import absltest
from lib.model import EntityTypeField
from lib.model import Match
from lib.model import StandardField
from lib.model import StandardizeField
from lib.tests import test_constants

from yamlformat.validator import namespace_validator as nv
from yamlformat.validator import presubmit_validate_types_lib
from yamlformat.validator.entity_type_lib import EntityType
from yamlformat.validator.external_file_lib import RecursiveDirWalk


class StandardFieldTest(absltest.TestCase):

  def setUp(self):
    super(StandardFieldTest).setUp()
    self.test_standard_field = StandardField(
        namespace_name='', standard_field_name='supply_air_flowrate_sensor')

  def testGetNamespaceName(self):
    # testing with '' because it is the global namespace which, in practice,
    # all fields are defined under the global namespace
    expected_output = ''
    function_output = self.test_standard_field.GetNamespaceName()

    self.assertEqual(function_output, expected_output)

  def testGetStandardFieldName(self):
    expected_output = 'supply_air_flowrate_sensor'
    function_output = self.test_standard_field.GetStandardFieldName()

    self.assertEqual(function_output, expected_output)


class EntityTypeFieldTest(absltest.TestCase):
  # Testing EntityTypeField objects defined in the global namespace

  def setUp(self):
    super(EntityTypeFieldTest).setUp()
    self.test_entity_type_field = EntityTypeField(
        namespace_name='',
        standard_field_name='supply_air_flowrate_sensor',
        is_optional=False,
        increment='_1_12')

  def testGetIncrement(self):
    expected_output = '_1_12'
    function_output = self.test_entity_type_field.GetIncrement()

    self.assertEqual(function_output, expected_output)

  def testIsOptional(self):
    self.assertFalse(self.test_entity_type_field.IsOptional())

  def testStandardizeField(self):
    expected_output = StandardField(
        namespace_name='', standard_field_name='supply_air_flowrate_sensor')

    function_output = StandardizeField(self.test_entity_type_field)

    self.assertEqual(function_output, expected_output)


class ModelTest(absltest.TestCase):

  def setUp(self):
    super(ModelTest).setUp()
    self.yaml = RecursiveDirWalk(test_constants.ONTOLOGY_ROOT)
    self.config = presubmit_validate_types_lib.SeparateConfigFiles(self.yaml)
    self.universe = presubmit_validate_types_lib.BuildUniverse(self.config)
    nv.NamespaceValidator(self.universe.GetEntityTypeNamespaces())
    test_entity_type = self.universe.entity_type_universe.GetEntityType(
        namespace_name='HVAC', typename='ZONE_HVAC')
    test_field_list = [
        EntityTypeField(optwrapper.field.namespace, optwrapper.field.field[0:],
                        optwrapper.optional, optwrapper.field.increment)
        for optwrapper in test_entity_type.GetAllFields().values()
    ]
    self.test_match = Match(
        field_list=test_field_list,
        entity_type=test_entity_type,
        match_type='EXACT')

  def testGetFieldList(self):
    expected_output = [
        EntityTypeField(
            namespace_name='',
            standard_field_name='zone_use_label',
            is_optional=True,
            increment='')
    ]

    function_output = self.test_match.GetFieldList()

    self.assertEqual(function_output, expected_output)

  def testGetEntityType(self):
    function_output = self.test_match.GetEntityType()

    self.assertIsInstance(function_output, EntityType)
    self.assertEqual(function_output.typename, 'ZONE_HVAC')

  def testGetMatchType(self):
    function_output = self.test_match.GetMatchType()

    self.assertEqual(function_output, 'EXACT')


if __name__ == '__main__':
  absltest.main()
