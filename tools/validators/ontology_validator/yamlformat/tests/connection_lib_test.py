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
"""Tests google3.corp.bizapps.rews.carson.ontology.validation.connection_lib."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl.testing import absltest

from yamlformat.validator import base_lib
from yamlformat.validator import connection_lib
from yamlformat.validator import findings_lib

_GOOD_PATH = '{0}/connections/anyfolder'.format(base_lib.GLOBAL_NAMESPACE)
_BAD_PATH = '{0}/connections/anyfolder'.format('nonglobal')


class ConnectionLibTest(absltest.TestCase):

  def testConnectionUniverseGetConnectionsMap(self):
    folder = connection_lib.ConnectionFolder(_GOOD_PATH)
    namespace = folder.local_namespace
    namespace.InsertConnection(connection_lib.Connection('FEEDS', 'one'))
    namespace.InsertConnection(connection_lib.Connection('CONTAINS', 'two'))
    connection_universe = connection_lib.ConnectionUniverse([folder])

    connections = connection_universe.GetConnectionsMap(
        base_lib.GLOBAL_NAMESPACE)

    self.assertIn('FEEDS', connections)
    self.assertIn('CONTAINS', connections)

  def testConnectionUniverseConnectionIsDefined(self):
    folder = connection_lib.ConnectionFolder(_GOOD_PATH)
    namespace = folder.local_namespace
    namespace.InsertConnection(connection_lib.Connection('FEEDS', 'one'))
    connection_universe = connection_lib.ConnectionUniverse([folder])

    self.assertTrue(connection_universe.IsDefined('FEEDS'))
    self.assertFalse(connection_universe.IsDefined('CONTAINS'))

  def testConnectionUniverseGetFindings(self):
    context = findings_lib.FileContext('{0}/file.yaml'.format(_GOOD_PATH))
    folder = connection_lib.ConnectionFolder(_GOOD_PATH)
    folder.AddFinding(findings_lib.InconsistentFileLocationError('', context))
    namespace = folder.local_namespace
    namespace.AddFinding(
        findings_lib.DuplicateConnectionDefinitionError(
            namespace, connection_lib.Connection('FEEDS'), context))
    connection = connection_lib.Connection('FEEDS', 'description')
    connection.AddFinding(
        findings_lib.MissingConnectionDescriptionWarning(connection))
    namespace.InsertConnection(connection)
    connection_universe = connection_lib.ConnectionUniverse([folder])

    findings = connection_universe.GetFindings()

    self.assertLen(findings, 3)
    self.assertTrue(
        connection_universe.HasFindingTypes([
            findings_lib.InconsistentFileLocationError,
            findings_lib.DuplicateConnectionDefinitionError,
            findings_lib.MissingConnectionDescriptionWarning
        ]))
    self.assertFalse(connection_universe.IsValid())

  def testConnectionFolderAddValidConnection(self):
    folder = connection_lib.ConnectionFolder(_GOOD_PATH)
    folder.AddConnection(connection_lib.Connection('FEEDS', 'description'))
    self.assertIn('FEEDS', folder.local_namespace.connections)
    self.assertEmpty(folder.GetFindings())

  def testConnectionFolderNonGlobalNamespace(self):
    folder = connection_lib.ConnectionFolder(_BAD_PATH)
    self.assertTrue(
        folder.HasFindingTypes([
            findings_lib.InvalidConnectionNamespaceError
        ]))

  def testConnectionFolderAddInvalidConnectionFails(self):
    folder = connection_lib.ConnectionFolder(_GOOD_PATH)
    folder.AddConnection(connection_lib.Connection('bad-connection', 'invalid'))
    self.assertNotIn('bad-connection', folder.local_namespace.connections)
    self.assertIsInstance(folder.GetFindings()[0],
                          findings_lib.InvalidConnectionNameError)

  def testConnectionFolderAddDuplicateConnectionFails(self):
    folder = connection_lib.ConnectionFolder(_GOOD_PATH)
    folder.AddConnection(connection_lib.Connection('FEEDS', 'description'))
    self.assertIn('FEEDS', folder.local_namespace.connections)
    self.assertEmpty(folder.local_namespace.GetFindings())
    folder.AddConnection(connection_lib.Connection('FEEDS', 'duplicate'))
    self.assertIsInstance(folder.local_namespace.GetFindings()[0],
                          findings_lib.DuplicateConnectionDefinitionError)

  def testConnectionFolderAddFromConfig(self):
    doc = {
        'FEEDS': {'description': 'one'},
        'CONTAINS': {'description': 'two'},
    }
    folder = connection_lib.ConnectionFolder(_GOOD_PATH)
    folder.AddFromConfig([doc], '{0}/file.yaml'.format(_GOOD_PATH))

    self.assertCountEqual(['FEEDS', 'CONTAINS'],
                          folder.local_namespace.connections)
    self.assertEmpty(folder.GetFindings())

  def testConnectionFolderAddFromConfigNotYamlFails(self):
    folder = connection_lib.ConnectionFolder(_GOOD_PATH)
    folder.AddFromConfig([{}], '{0}/file.txt'.format(_GOOD_PATH))
    self.assertIsInstance(folder.GetFindings()[0],
                          findings_lib.InconsistentFileLocationError)

  def testConnectionWithIllegalKeyTypeHasFindings(self):
    connection = connection_lib.Connection(False, 'invalid')
    self.assertIsInstance(connection.GetFindings()[0],
                          findings_lib.IllegalKeyTypeError)

  def testConnectionWithIllegalNameHasFindings(self):
    connection = connection_lib.Connection('bad-connection', 'invalid')
    self.assertIsInstance(connection.GetFindings()[0],
                          findings_lib.InvalidConnectionNameError)

  def testConnectionWithNoDescriptionHasFindings(self):
    connection = connection_lib.Connection('FEEDS', '')
    self.assertIsInstance(connection.GetFindings()[0],
                          findings_lib.MissingConnectionDescriptionWarning)

  def testConnectionEquals(self):
    connection_one = connection_lib.Connection('FEEDS', 'description')
    connection_one_dup = connection_lib.Connection('FEEDS', 'description')
    connection_one_no_desc = connection_lib.Connection('FEEDS', '')
    connection_two = connection_lib.Connection('CONTAINS', 'description')
    self.assertEqual(connection_one, connection_one_dup)
    self.assertNotEqual(connection_one, connection_one_no_desc)
    self.assertNotEqual(connection_one, connection_two)


if __name__ == '__main__':
  absltest.main()
