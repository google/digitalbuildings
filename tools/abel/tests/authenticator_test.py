# Copyright 2023 Google LLC
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
"""Tests for authenticator."""

from absl.testing import absltest

from model import authenticator


class AuthenticatorTest(absltest.TestCase):
  """Tests GetGoogleSheetsService method in authenticator module."""

  def testGetGoogleSheetsServiceByCred_badFilePath_raisesFileNotFoundError(
      self,
  ):
    bad_file_path = './credential.json'

    with self.assertRaises(FileNotFoundError):
      authenticator.GetGoogleSheetsServiceByCredential(
          gcp_credential_path=bad_file_path
      )


if __name__ == '__main__':
  absltest.main()
