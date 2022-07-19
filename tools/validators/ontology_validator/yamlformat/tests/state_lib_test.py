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

"""Tests google3.corp.bizapps.rews.carson.ontology.validation.state_lib."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from google3.third_party.digitalbuildings.tools.validators.ontology_validator.yamlformat.validator import findings_lib
from google3.third_party.digitalbuildings.tools.validators.ontology_validator.yamlformat.validator import state_lib
from absl.testing import absltest

_GOOD_PATH = '{0}/states/anyfolder'.format('mynamespace')


class StateLibTest(absltest.TestCase):

  def testStateUniverseGetStatesMap(self):
    folder = state_lib.StateFolder(_GOOD_PATH)
    namespace = folder.local_namespace
    namespace.InsertState(state_lib.State('STATE_ONE', 'one'))
    namespace.InsertState(state_lib.State('STATE_TWO', 'two'))
    state_universe = state_lib.StateUniverse([folder])

    states = state_universe.GetStatesMap('mynamespace')

    self.assertIn('STATE_ONE', states)
    self.assertIn('STATE_TWO', states)

  def testStateUniverseGetFindings(self):
    context = findings_lib.FileContext('{0}/file.yaml'.format(_GOOD_PATH))
    folder = state_lib.StateFolder(_GOOD_PATH)
    folder.AddFinding(findings_lib.InconsistentFileLocationError('', context))
    namespace = folder.local_namespace
    namespace.AddFinding(
        findings_lib.DuplicateStateDefinitionError(namespace,
                                                   state_lib.State('STATE'),
                                                   context))
    state = state_lib.State('STATE', 'description')
    state.AddFinding(findings_lib.MissingStateDescriptionWarning(state))
    namespace.InsertState(state)
    state_universe = state_lib.StateUniverse([folder])

    findings = state_universe.GetFindings()

    self.assertLen(findings, 3)
    self.assertTrue(
        state_universe.HasFindingTypes([
            findings_lib.InconsistentFileLocationError,
            findings_lib.DuplicateStateDefinitionError,
            findings_lib.MissingStateDescriptionWarning
        ]))
    self.assertFalse(state_universe.IsValid())

  def testStateFolderAddValidState(self):
    folder = state_lib.StateFolder(_GOOD_PATH)
    folder.AddState(state_lib.State('STATE', 'description'))
    self.assertIn('STATE', folder.local_namespace.states)
    self.assertEmpty(folder.GetFindings())

  def testStateFolderAddInvalidStateFails(self):
    folder = state_lib.StateFolder(_GOOD_PATH)
    folder.AddState(state_lib.State('bad-state', 'invalid'))
    self.assertNotIn('bad-state', folder.local_namespace.states)
    self.assertIsInstance(folder.GetFindings()[0],
                          findings_lib.InvalidStateNameError)

  def testStateFolderAddDuplicateStateFails(self):
    folder = state_lib.StateFolder(_GOOD_PATH)
    folder.AddState(state_lib.State('STATE', 'description'))
    self.assertIn('STATE', folder.local_namespace.states)
    self.assertEmpty(folder.local_namespace.GetFindings())
    folder.AddState(state_lib.State('STATE', 'duplicate'))
    self.assertIsInstance(folder.local_namespace.GetFindings()[0],
                          findings_lib.DuplicateStateDefinitionError)

  def testStateFolderAddFromConfig(self):
    doc = {
        'STATE_ONE': 'one',
        'STATE_TWO': 'two',
    }
    folder = state_lib.StateFolder(_GOOD_PATH)
    folder.AddFromConfig([doc], '{0}/file.yaml'.format(_GOOD_PATH))

    self.assertCountEqual(['STATE_ONE', 'STATE_TWO'],
                          folder.local_namespace.states)
    self.assertEmpty(folder.GetFindings())

  def testStateFolderAddFromConfigNotYamlFails(self):
    folder = state_lib.StateFolder(_GOOD_PATH)
    folder.AddFromConfig([{}], '{0}/file.txt'.format(_GOOD_PATH))
    self.assertIsInstance(folder.GetFindings()[0],
                          findings_lib.InconsistentFileLocationError)

  def testStateWithIllegalKeyTypeHasFindings(self):
    state = state_lib.State(False, 'invalid')
    self.assertIsInstance(state.GetFindings()[0],
                          findings_lib.IllegalKeyTypeError)

  def testStateWithIllegalNameHasFindings(self):
    state = state_lib.State('bad-state', 'invalid')
    self.assertIsInstance(state.GetFindings()[0],
                          findings_lib.InvalidStateNameError)

  def testStateWithNoDescriptionHasFindings(self):
    state = state_lib.State('STATE', '')
    self.assertIsInstance(state.GetFindings()[0],
                          findings_lib.MissingStateDescriptionWarning)

  def testStateEquals(self):
    state_one = state_lib.State('STATE_ONE', 'description')
    state_one_dup = state_lib.State('STATE_ONE', 'description')
    state_one_no_desc = state_lib.State('STATE_ONE', '')
    state_two = state_lib.State('STATE_TWO', 'description')
    self.assertEqual(state_one, state_one_dup)
    self.assertNotEqual(state_one, state_one_no_desc)
    self.assertNotEqual(state_one, state_two)


if __name__ == '__main__':
  absltest.main()
