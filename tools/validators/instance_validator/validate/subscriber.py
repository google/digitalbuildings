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

# pylint: disable=g-importing-member
from google import auth
from google.cloud import pubsub_v1


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

  def Listen(self, callback):
    """Listens to a pubsub subscription.

    Args:
      callback: a callback function to handle the message.
    """
    credentials = auth.default()[0]
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
