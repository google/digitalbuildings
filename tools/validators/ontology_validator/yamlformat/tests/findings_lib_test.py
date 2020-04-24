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
"""Tests for ...phred.tools.typegenerator.typevalidator.base_lib."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from validation.validator import entity_type_lib
from validation.validator import findings_lib
from validation.validator import test_helpers_lib
from absl.testing import absltest

_F = test_helpers_lib.Fields


class FindingsLibTest(absltest.TestCase):

  def setUp(self):
    self.findings_class = findings_lib.Findings()
    self.file_context = findings_lib.FileContext(filepath='some_path')

  def testFindingGood(self):
    findings_lib.Finding('message', self.file_context)

  def testFindingBadMessage(self):
    # no message
    with self.assertRaises(TypeError):
      findings_lib.Finding(self.file_context)

    # message isn't string
    some_list = []
    with self.assertRaises(TypeError):
      findings_lib.Finding(some_list, self.file_context)

  def testFindingBadFileContext(self):
    # no file context
    with self.assertRaises(TypeError):
      findings_lib.Finding('message')

    # wrong type
    with self.assertRaises(TypeError):
      findings_lib.Finding('message', 'filepath')

  def testFindingEqualityKey(self):
    key = object()
    key2 = object()

    finding1 = findings_lib.Finding('', self.file_context, equality_key=key)
    finding2 = findings_lib.Finding('', self.file_context, equality_key=key)
    finding3 = findings_lib.Finding('', self.file_context, equality_key=key2)
    finding4 = findings_lib.Finding('', self.file_context)

    self.assertEqual(finding1, finding2)
    self.assertNotEqual(finding1, finding3)
    self.assertNotEqual(finding1, finding4)
    self.assertEqual(finding4, finding4)

  def testValidationWarningEqualityKey(self):
    key = object()
    finding1 = findings_lib.ValidationWarning(
        'm', self.file_context, equality_key=key)
    finding2 = findings_lib.ValidationWarning(
        'm', self.file_context, equality_key=key)
    self.assertEqual(finding1, finding2)

  def testSmallDeviationFindingEqualityKey(self):
    parents = ['wolf', 'ANIMAL', 'dingo']
    entity_type = entity_type_lib.EntityType(
        filepath='path/to/ANIMAL/mammal',
        typename='dog',
        description='canine animal')
    key = object()
    finding1 = findings_lib.SmallFieldDeviationWarning(
        entity_type, parents, 3, _F(['a', 'b']), key)
    finding2 = findings_lib.SmallFieldDeviationWarning(
        entity_type, parents, 3, _F(['a', 'b']), key)
    self.assertEqual(finding1, finding2)

  def testFindingsAddValidationError(self):
    self.findings_class.AddFinding(findings_lib.ValidationError(
        'message', findings_lib.FileContext('filepath')))
    findings = self.findings_class.GetFindings()
    self.assertLen(findings, 1)
    self.assertFalse(self.findings_class.IsValid())

  def testFindingsAddValidationWarning(self):
    self.findings_class.AddFinding(findings_lib.ValidationWarning(
        'message', findings_lib.FileContext('filepath')))
    findings = self.findings_class.GetFindings()
    self.assertLen(findings, 1)
    self.assertTrue(self.findings_class.IsValid())

  def testFindingsAddMultiple(self):
    self.findings_class.AddFinding(findings_lib.ValidationError(
        'message', findings_lib.FileContext('filepath')))
    self.findings_class.AddFinding(findings_lib.ValidationWarning(
        'message', findings_lib.FileContext('filepath')))
    findings = self.findings_class.GetFindings()
    self.assertLen(findings, 2)
    self.assertFalse(self.findings_class.IsValid())

  def testFindingsAddBadArg(self):
    with self.assertRaises(TypeError):
      self.findings_class.AddFinding('some string.')

  def testFindingsAddGoodList(self):
    good_list = [
        findings_lib.ValidationError(
            'message', findings_lib.FileContext('filepath')),
        findings_lib.ValidationWarning(
            'message', findings_lib.FileContext('filepath'))]
    self.findings_class.AddFindings(good_list)
    findings = self.findings_class.GetFindings()
    self.assertLen(findings, 2)
    self.assertFalse(self.findings_class.IsValid())

  def testFindingsAddBadList(self):
    bad_list = [
        findings_lib.ValidationError(
            'message', findings_lib.FileContext('filepath')),
        'some string',
        findings_lib.ValidationWarning(
            'message', findings_lib.FileContext('filepath'))]

    with self.assertRaises(TypeError):
      self.findings_class.AddFindings(bad_list)

  def testFindingsHasFindingTypes(self):
    self.assertFalse(self.findings_class.HasFindingTypes(
        [findings_lib.ValidationError]))

    self.findings_class.AddFinding(findings_lib.ValidationError(
        'message', findings_lib.FileContext('filepath')))

    self.assertTrue(self.findings_class.HasFindingTypes(
        [findings_lib.ValidationError]))
    self.assertFalse(self.findings_class.HasFindingTypes(
        [findings_lib.ValidationWarning]))
    self.assertTrue(self.findings_class.HasFindingTypes(
        [findings_lib.ValidationError,
         findings_lib.ValidationWarning]))

  def testFindingsHandlesDeduplication(self):
    high = findings_lib.Finding(
        'high', findings_lib.FileContext('f'), 2, 2, 2, 'key', False)
    med = findings_lib.Finding(
        'med', findings_lib.FileContext('f'), 3, 2, 2, 'key', False)
    low = findings_lib.Finding(
        'low', findings_lib.FileContext('f'), 3, 3, 2, 'key', False)
    bottom = findings_lib.Finding(
        'bottom', findings_lib.FileContext('f'), 3, 3, 3, 'key', False)
    master = findings_lib.Finding(
        'master', findings_lib.FileContext('f'), 3, 3, 3, 'key', True)
    # Check each paired sort, working from lowest to highest
    self.findings_class.AddFinding(master)
    self.findings_class.AddFinding(bottom)
    findings = self.findings_class.GetFindings()
    self.assertLen(findings, 1)
    self.assertEqual('master', findings[0].message)

    self.findings_class.AddFinding(low)
    self.findings_class.AddFinding(bottom)
    findings = self.findings_class.GetFindings()
    self.assertLen(findings, 1)
    self.assertEqual('low', findings[0].message)

    self.findings_class.AddFinding(med)
    self.findings_class.AddFinding(low)
    findings = self.findings_class.GetFindings()
    self.assertLen(findings, 1)
    self.assertEqual('med', findings[0].message)

    self.findings_class.AddFinding(high)
    self.findings_class.AddFinding(med)
    findings = self.findings_class.GetFindings()
    self.assertLen(findings, 1)
    self.assertEqual('high', findings[0].message)


if __name__ == '__main__':
  absltest.main()
