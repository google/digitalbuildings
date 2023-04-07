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
"""Module to authenticate against Google Sheets api."""

from __future__ import print_function

import datetime
import json
import os.path

from google.auth.exceptions import MutualTLSChannelError
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.discovery import Resource

from model.constants import ACCESS_TOKEN
from model.constants import EXPIRE_TIME
from model.constants import SHEETS
from model.constants import V4

_SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


# TODO(b/269463912): Deprecate authentication support for service accounts.
def GetGoogleSheetsServiceByToken(gcp_token_path: str) -> Resource:
  """Uses client API credentials to obtain a Resource instance.

  Resource instance contains methods for interacting with the Google Sheets
  service.

  Args:
    gcp_token_path: Path to GCP token for authenticating against Google sheets
      API. This is a short-lived credential for a service account as documented.
      https://cloud.google.com/iam/docs/create-short-lived-credentials-direct

  Returns:
    A Google Python API Client discovery.Resource instance with methods for
    interacting with the Google Sheets service.

  Raises:
    FileNotFoundError: gcp_token_path does not exist.
  """
  creds = None
  try:
    with open(os.path.abspath(gcp_token_path), encoding='utf-8') as token:
      token_data = json.load(token)
      expiry = datetime.datetime.strptime(
          token_data[EXPIRE_TIME], '%Y-%m-%dT%H:%M:%SZ'
      )
    creds = Credentials(
        token=token_data[ACCESS_TOKEN], expiry=expiry, scopes=_SCOPES
    )
    return build(SHEETS, V4, credentials=creds)
  except FileNotFoundError as err:
    raise FileNotFoundError(
        'GCP project token not found. See user manual for token generation.'
    ) from err
  except MutualTLSChannelError as err:
    raise MutualTLSChannelError(
        'Unable to access google sheet service with GCP token provided'
    ) from err


def GetGoogleSheetsServiceByCredential(gcp_credential_path: str) -> Resource:
  """Uses client Oauth API credentials to obtain a Resource instance.

  Resource instance contains methods for interacting with the Google Sheets
  service.

  Args:
    gcp_credential_path: Path to GCP credential file for authenticating against
      Google sheets API. This is a OAuth credential as documented.
      https://developers.google.com/sheets/api/quickstart/python

  Returns:
    A Google Python API Client discovery.Resource instance with methods for
    interacting with the Google Sheets service.

  Raises:
    FileNotFoundError: gcp_credential_path does not exist.
    MutualTLSChannelError: ABEL cannot authenticate against Google Sheets API
    with the provided client credential.
  """
  creds = None
  try:
    flow = InstalledAppFlow.from_client_secrets_file(
        os.path.abspath(gcp_credential_path), scopes=_SCOPES
    )
    creds = flow.run_local_server(port=0)
    return build(SHEETS, V4, credentials=creds)
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
