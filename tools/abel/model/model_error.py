# Copyright 2022 Google LLC
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
"""Module for custom abel model exceptions."""

from typing import Any, Optional

# pylint: disable=g-importing-member
from googleapiclient.errors import HttpError


class SpreadsheetAuthorizationError(HttpError):
  """Extension of HttpError that adds a custom error message."""

  def __init__(self,
               resp: Any,
               content: Any,
               uri: Optional[Any] = None,
               spreadsheet_id: Optional[str] = None):
    """Init.

    Args:
      resp: Http response.
      content: Bytes instances for http response content.
      uri: Http request uri.
      spreadsheet_id: alpha-numerical id for a Google Sheets spreadsheet.
    """
    super().__init__(resp=resp, content=content)
    self.spreadsheet_id = spreadsheet_id

  def __repr__(self):
    error_string = 'User does not have access to spreadsheet: '
    error_string += f'https://docs.google.com/document/d/{self.spreadsheet_id}'
    return error_string

  __str__ = __repr__
