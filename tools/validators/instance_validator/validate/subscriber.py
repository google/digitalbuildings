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

"""Reads payload from a pubsub subscription"""

from __future__ import print_function

import json
from google.auth import jwt
from google.cloud import pubsub_v1


class Subscriber(object):
  """Reads payload from a subscription.

  Args:
    subscription_name: name of the subscription.
    service_account_info: service account information from the GCP project.
  """

  def __init__(self, subscription_name, service_account_info_json_file):
    super().__init__()
    assert subscription_name
    assert service_account_info_json_file
    self.subscription_name = subscription_name
    self.service_account_info_json_file = service_account_info_json_file

  def Listen(self, callback):
    """Listens to a pubsub subscription.

    Args:
      callback: a callback function to handle the message.
    """
    with open(self.service_account_info_json_file) as f:
      service_account_info = json.load(f)
    audience = "https://pubsub.googleapis.com/google.pubsub.v1.Subscriber"
    credentials = jwt.Credentials.from_service_account_info(service_account_info
                                                            , audience=audience)
    sub_client = pubsub_v1.SubscriberClient(credentials=credentials)
    future = sub_client.subscribe(self.subscription_name, callback)
    print("Listening to pubsub, please wait ...")
    try:
      future.result()
    except KeyboardInterrupt:
      future.cancel()
