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
"""Reads payload from a pubsub subscription."""

from __future__ import print_function

from concurrent import futures
import os

# pylint: disable=g-importing-member
from google.auth.exceptions import MutualTLSChannelError
from google.cloud import pubsub_v1
from google_auth_oauthlib.flow import InstalledAppFlow


_SCOPES = ['https://www.googleapis.com/auth/pubsub']


class Subscriber(object):
  """Reads payload from a subscription.

  Attributes:
    subscription_name: Name of the subscription.
  """

  def __init__(
      self,
      subscription_name: str,
  ):
    """Init.

    Args:
      subscription_name: Pubsub subscription name.
    """

    super().__init__()
    assert subscription_name
    self.subscription_name = subscription_name

  def Listen(self, callback, gcp_credential_path: str):
    """Listens to a pubsub subscription.

    Args:
      callback: a callback function to handle the message.
      gcp_credential_path: Path to GCP credential file for authenticating
        against Google sheets API. This is an OAuth credential as documented.
        https://developers.google.com/sheets/api/quickstart/python
    """
    try:
      flow = InstalledAppFlow.from_client_secrets_file(
          os.path.abspath(gcp_credential_path), scopes=_SCOPES
      )
      credentials = flow.run_local_server(port=0)
    except FileNotFoundError as err:
      raise FileNotFoundError(
          'Oauth client id credential file json file not found. Please check'
          ' the path provided.'
      ) from err
    except MutualTLSChannelError as err:
      raise MutualTLSChannelError(
          'ABEL cannot authenticate against Google Sheets API with the provided'
          ' client credential.'
      ) from err

    sub_client = pubsub_v1.SubscriberClient(credentials=credentials)
    future = sub_client.subscribe(self.subscription_name, callback)
    print('[INFO]\tListening to pub/sub topic. Please wait.')
    # KeyboardInterrupt does not always cause `result` to exit early, so we
    # give the thread a chance to handle that within a reasonable amount of
    # time by repeatedly calling `result` with a short timeout.
    while True:
      try:
        future.result(timeout=5)
      except futures.TimeoutError:
        continue
      except (futures.CancelledError, KeyboardInterrupt):
        future.cancel()
      except Exception as ex:  # pylint: disable=broad-except
        print(f'[ERROR]\tPub/sub subscription failed with error: {ex}')
        future.cancel()
      break
