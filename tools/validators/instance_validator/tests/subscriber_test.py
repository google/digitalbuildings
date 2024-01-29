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
"""Tests tools.validators.instance_validator.instance_validator."""
from unittest import mock
from absl.testing import absltest
from validate import subscriber

FAKE_SUBSCRIPTION_NAME = 'fake/subscription'
mock_callback = mock.Mock()


class SubscriberTest(absltest.TestCase):

  def setUp(self):
    super().setUp()
    self.subscriber = subscriber.Subscriber(FAKE_SUBSCRIPTION_NAME)

  @mock.patch.object(subscriber, 'InstalledAppFlow')
  @mock.patch.object(subscriber, 'pubsub_v1')
  def test_listen_no_service_account(self, test_pubsub, test_flow):
    test_flow.from_client_secrets_file.return_value = 'fake_credentials'
    test_pubsub.SubscriberClient.return_value = None
    with self.assertRaises(AttributeError):
      self.subscriber.Listen(
          callback=mock_callback, gcp_credential_path='fake_credential_path'
      )
    test_flow.from_client_secrets_file.assert_called_once()


if __name__ == '__main__':
  absltest.main()
