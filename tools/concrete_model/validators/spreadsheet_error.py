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
"""Module for a custom spreadsheet exception."""


class SpreadsheetError(Exception):
  """Custom exception to model validation errors on a concrete model spreadsheet.

  Attributes:
    table: Table name where the exception is raised.
    row: Row number where the exception is raised.
    column: Column letter where the exception is raised.
    message: Custom exception message.
  """

  def __init__(self, row: str, column: str, table: str, message: str):
    """Init.

    Args:
      row: Row number where the exception is raised.
      column: Column letter where the exception is raised.
      table: Table name where the exception is raised.
      message: Custom exception message.
    """

    self.table = table
    self.row = row
    self.column = column
    self.message = message
    super().__init__(message)

  def __str__(self):
    return f'Table: {self.table}, Row: {self.row}, Column: {self.column}, Message: {self.message}'
