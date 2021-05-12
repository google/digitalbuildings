from absl.testing import absltest

import sys
sys.path.append('../')

from ontology_match_lib import Ontology

RDIR = '../../../ontology/yaml/resources'

expected_namespaces = ['ELECTRICAL', 'GLOBAL', 'CARSON', 'HVAC', 'SAFETY', 'METERS', 'LIGHTING', 'FACILITIES', 'PHYSICAL_SECURITY']

# Initialize the ontology object for use latere.
ont = Ontology(RDIR)


# Check that a field set matches to a specific fan coil unit.
class testGetAllNamespaces(absltest.TestCase):

	# Init Tests
	def test_get_all_namespaces(self):
		namespaces = ont.get_all_namespaces()
		self.assertEqual(namespaces,expected_namespaces)


if __name__ == '__main__':
	absltest.main()