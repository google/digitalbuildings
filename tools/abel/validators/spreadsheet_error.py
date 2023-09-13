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
"""Module for custom ABEL spreadsheet exceptions."""

import abc
from typing import Optional

# pylint: disable=g-importing-member
from model.constants import CONNECTIONS
from model.constants import ENTITIES


# pylint: disable=line-too-long
class BaseSpreadsheetError(Exception):
  """Custom exception to model validation errors on a concrete model spreadsheet.

  Attributes:
    table: Table name where the exception is raised.
    message: Custom exception message.
  """

  def __init__(self, table: str, message: Optional[str]):
    """Init.

    Args:
      table: Table name where the exception is raised.
      message: [Optional]Custom exception message.
    """
    self.table = table
    self.message = message
    super().__init__(message)

  @abc.abstractmethod
  def GetErrorMessage(self):
    pass


class InvalidNamingError(BaseSpreadsheetError):
  """Custom exception for invalid or incorrectly formatted entity names.

  Attributes:
    table: Table name where the name is invalid.
    row: Row number where the name is invalid.
    column: Column header for the invalid name.
    message: Custom exception message for the invalid name.
    invalid_name: Name that does not conform to provided pattern.
    naming_pattern: Regex pattern for entity names.
  """

  def __init__(self,
               table: str,
               row: str,
               column: str,
               invalid_name: str,
               naming_pattern: str,
               message: Optional[str] = ''):
    """Init.

    Args:
      table: Table name where the name is invalid.
      row: Row number where the name is invalid.
      column: Column header for the invalid name.
      invalid_name: Name that does not conform to provided pattern.
      naming_pattern: Regex pattern for entity names.
      message: [Optional] Custom exception message for the invalid name.
    """
    super().__init__(table, message)
    self.row = row
    self.column = column
    self.invalid_name = invalid_name
    self.naming_pattern = naming_pattern

  def GetErrorMessage(self) -> str:
    return f'Table: {self.table}, Row: {self.row}, Column: {self.column}, Message: {self.message}, entity name: {self.invalid_name} must follow naming pattern: {self.naming_pattern}'


class MissingSpreadsheetValueError(BaseSpreadsheetError):
  """Custom exception for missing values in an ABEL spreadsheet.

  Attributes:
    table: Table name where the value is missing.
    row: Row number where the value is missing.
    column: Column header for the missing value.
    message: Custom exception message for the missing value.
  """

  def __init__(self, table: str, row: str, column: str, message: Optional[str]):
    """Init.

    Args:
      table: Table name where the value is missing.
      row: Row number where the value is missing.
      column: Column header for the missing value.
      message: [Optional] Custom exception message for the missing value.
    """
    super().__init__(table, message)
    self.row = row
    self.column = column

  def GetErrorMessage(self) -> str:
    return f'Table: {self.table}, Row: {self.row}, Column: {self.column}, Message: {self.message}'


class MissingFieldError(BaseSpreadsheetError):
  """Exception to raise errors for validations associated with missing fields.

  Attributes:
    table: The Entity Fields table.
    row: Row number of invalid missing field values.
    column: column name of invalid cell values.
    Message: [Optional] Custom exception message for invalid cell values.
  """

  def __init__(self, table: str, row: str, column: str, message: Optional[str]):
    super().__init__(table, message)
    self.row = row
    self.column = column

  def GetErrorMessage(self) -> str:
    return f'Table: {self.table}, Row: {self.row}, Column: {self.column}, Message: {self.message}'


class DuplicateCodeError(BaseSpreadsheetError):
  """Custom exception for duplicate codes in an ABEL spreadsheet.

  Currently, this error only pertains to the Entities table, but if multiple
  sites are ever supported by ABEL then this error could be raised for the Sites
  table as well.

  Attributes:
    code: The duplicated code.
    table: The spreadsheet table where the duplicated code exists, default is
      Entities table.
    message: Custom error message.
  """

  def __init__(self, code: str, message: str, table: Optional[str] = ENTITIES):
    """Init.

    Args:
      code: The duplicated code.
      message: Custom error message.
      table: [Optional] The spreadsheet table where the duplicated code exists,
        default is Entities table.
    """
    super().__init__(table, message)
    self.code = code

  def GetErrorMessage(self) -> str:
    return f'Table: {self.table}, Duplicate Code: {self.code}, Message: {self.message}'


class SpreadsheetHeaderError(BaseSpreadsheetError):
  """Custom exception for missing column headers in an ABEL spreadsheet.

  Attributes:
    header: The missing header.
    table: Table name which is a missing a column header.
    message: custom exception message.
  """

  def __init__(self, header: str, table: str, message: str):
    """Init.

    Args:
      header: The missing column header value.
      table: Table name which is a missing a column headers.
      message: custom exception message.
    """
    super().__init__(table, message)
    self.header = header

  def GetErrorMessage(self) -> str:
    return f'Table: {self.table}, Missing Header: {self.header}, Message: {self.message}'


class CrossSheetDependencyError(BaseSpreadsheetError):
  """Custom exception for values that are referenced in multiple spreadsheet tables.

  This error is raised when a cell references a value in a separate table. For
  example, entity fields reference entity codes that are declared in the
  entities table. If the fields table references a code that is not defined in
  the entities table, this error will be raised.

  Attributes:
    source_table: Table name where the missing value is referenced.
    target_table: Table name where the value is missing.
    row: Row in the source table where the missing value is being referenced.
    column: Column name in the source table where the missing value is being
      referenced.
    cell_value: The missing value.
    message: Custom error message.
  """

  def __init__(self,
               source_table: str,
               target_table: str,
               row: str,
               column: str,
               cell_value: str,
               message: Optional[str] = ''):
    """Init.

    Args:
      source_table: Table name where the missing value is referenced.
      target_table: Table name where the value is missing.
      row: Row in the source table where the missing value is being referenced.
      column: Column name in the source table where the missing value is being
        referenced.
      cell_value: The missing value.
      message: Custom error message.
    """

    super().__init__(table=source_table, message=message)
    self.target_table = target_table
    self.row = row
    self.column = column
    self.cell_value = cell_value

  def GetErrorMessage(self) -> str:
    error_message = f'Row: {self.row}, Column: {self.column}, Source Table: {self.table}, Target Table: {self.target_table}.\n'
    error_message += f'{self.table} has a dependency on {self.target_table}, {self.cell_value} not found in {self.target_table}.'
    if self.message:
      error_message += f'\nMessage: {self.message}'
    return error_message


class ConnectionDependencyError(BaseSpreadsheetError):
  """Custom exception for connection dependency errors.

  This error is raised when an entity code is referenced in the Connections
  table and it is not defined in the Entities table.

  Attributes:
    row: Row number of the connection referencing an undefined code.
    missing_code: Undefined entity code.
    present_code: entity code which has a connection dependency on missing_code.
    table: Connections table.
    message: Custom error message.
  """

  def __init__(self,
               row: str,
               missing_code: str,
               present_code: str,
               table: Optional[str] = CONNECTIONS,
               message: Optional[str] = ''):
    """Init.

    Args:
      row: Row number of the connection referencing an undefined code.
      missing_code: Undefined entity code.
      present_code: entity code which has a connection dependency on
        missing_code.
      table: [Optional]Connections table.
      message: Custom error message.
    """
    super().__init__(table, message)
    self.row = row
    self.missing_code = missing_code
    self.present_code = present_code

  def GetErrorMessage(self) -> str:
    error_message = f'Row: {self.row},'
    error_message += f'Entity with code: {self.present_code} has a connection '
    error_message += f'dependency error, {self.missing_code} not found in {ENTITIES} table.'
    if self.message:
      error_message += f'\n Message: {self.message}'
    return error_message
