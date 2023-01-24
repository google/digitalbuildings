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
"""Reads payload from a pubsub subscription."""

from __future__ import print_function

from concurrent import futures
import json
from typing import Optional

from google import auth
from google.cloud import pubsub_v1


class Subscriber(object):
  """Reads payload from a subscription.

  Attributes:
    subscription_name: Name of the subscription.
    service_account_info_json_file: [optional] Service account information from
      the GCP project. When not provided, appplication default credentials are
      used.
  """

  def __init__(self,
               subscription_name: str,
               service_account_info_json_file: Optional[str] = None):
    """Init.

    Args:
      subscription_name: Pubsub subscription name.
      service_account_info_json_file: [optional] Service account information
        from the GCP project. When not provided, appplication default
        credentials are used.
    """

    super().__init__()
    assert subscription_name
    self.subscription_name = subscription_name
    self.service_account_info_json_file = service_account_info_json_file

  def Listen(self, callback):
    """Listens to a pubsub subscription.

    Args:
      callback: a callback function to handle the message.
    """
    if self.service_account_info_json_file:
      with open(self.service_account_info_json_file, encoding='utf-8') as f:
        service_account_info = json.load(f)
      audience = 'https://pubsub.googleapis.com/google.pubsub.v1.Subscriber'
      credentials = auth.jwt.Credentials.from_service_account_info(
          service_account_info, audience=audience)
    else:
      print('[INFO]\tNo service account. Using application default credentials')
      # pylint: disable=unused-variable
      credentials, project_id = auth.default()

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
