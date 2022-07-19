# Copyright 2021 Google LLC
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
"""Main module for DBO explorer."""

import datetime
import os
import sys

from google3.third_party.digitalbuildings.tools.concrete_model.model import authenticator
from google3.third_party.digitalbuildings.tools.concrete_model.model import export_helper
from google3.third_party.digitalbuildings.tools.concrete_model.model import import_helper
from google3.third_party.digitalbuildings.tools.concrete_model.model.arg_parser import ParseArgs
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import SPREADSHEET_RANGE
from google3.third_party.digitalbuildings.tools.concrete_model.model.model_builder import ModelBuilder
from google3.third_party.digitalbuildings.tools.concrete_model.validators.spreadsheet_validator import SpreadsheetValidator
from google3.third_party.digitalbuildings.tools.validators.instance_validator.validate import handler

# TODO(b/235149197) Implement telemetry validation.
DATETIME_STRING = datetime.datetime.now().strftime('%m-%d-%Y_%H:%M')

# Output path for spreadsheet validation report
SPREADSHEET_VALIDATOR_LOG_PATH = os.path.join(
    os.path.expanduser('~'),
    f'abel/spreadsheet_validation_{DATETIME_STRING}.log')

# Output path for Building Config instance validation report.
INSTANCE_VALIDATOR_LOG_PATH = os.path.join(
    os.path.expanduser('~'), f'abel/instance_validation_{DATETIME_STRING}.log')

# Output path for exporting a Building Config file.
BC_EXPORT_PATH = os.path.join(
    os.path.expanduser('~'), f'abel/bc_export_{DATETIME_STRING}.yaml')


def _spreadsheet_workflow(spreadsheet_id: str, gcp_token_path: str) -> None:
  """Helper function for executing the spreadsheet -> building config workflow.

  Args:
    spreadsheet_id: Google Sheets spreadsheet ID to be parsed into ABEL.
    gcp_token_path: Path to GCP token for authenticating against Google sheets
      API. This is a short-lived credential for a service account as documented
      https://cloud.google.com/iam/docs/create-short-lived-credentials-direct.
  """
  print(f'Importing spreadsheet from Google sheets: {spreadsheet_id}')
  google_sheets_service = authenticator.GetGoogleSheetsService(
      gcp_token_path=gcp_token_path)
  imported_spreadsheet = import_helper.GetAllSheets(
      google_sheets_service=google_sheets_service,
      spreadsheet_id=spreadsheet_id,
      spreadsheet_range=SPREADSHEET_RANGE)
  print('Validating spreadsheet')
  spreadsheet_validator = SpreadsheetValidator(
      filepath=SPREADSHEET_VALIDATOR_LOG_PATH)
  is_spreadsheet_valid = spreadsheet_validator.Validate(imported_spreadsheet)
  if not is_spreadsheet_valid:
    print(
        f'Please resolve spreadsheet errors: {SPREADSHEET_VALIDATOR_LOG_PATH}')
  else:
    print('Spreadsheet validated.')
    # Build model
    print('Building model.')
    model_builder = ModelBuilder.FromSpreadsheet(imported_spreadsheet)
    model_builder.Build()
    print('Model built!')
    # export
    new_bc_exporter = export_helper.BuildingConfigExport(model_builder)
    new_bc_exporter.ExportBuildingConfiguration(filepath=BC_EXPORT_PATH)
    # Run instance validator
    print('Validating Export.')
    handler.RunValidation(
        filenames=[BC_EXPORT_PATH], report_filename=INSTANCE_VALIDATOR_LOG_PATH)
    print(f'Instance validator log: {INSTANCE_VALIDATOR_LOG_PATH}')
    print(f'Exported Building Configuration: {BC_EXPORT_PATH}')


def _bc_workflow(spreadsheet_id: str, bc_filepath: str,
                 gcp_token_path: str) -> None:
  """Helper function for Building Config -> spreadsheet workflow.

  Args:
    spreadsheet_id: Exported Google spreadsheets id.
    bc_filepath: Imported Building Config filepath.
    gcp_token_path: Path to GCP token for authenticating against Google sheets
      API. This is a short-lived credential for a service account as documented
      https://cloud.google.com/iam/docs/create-short-lived-credentials-direct.
  """
  print('Validating imported Building Config.')
  handler.RunValidation(
      filenames=[bc_filepath], report_filename=INSTANCE_VALIDATOR_LOG_PATH)
  print(f'Importing Building Configuration file from {bc_filepath}.')
  imported_building_config = import_helper.DeserializeBuildingConfiguration(
      filepath=bc_filepath)
  print('Building model from building configuration file.')
  model = ModelBuilder.FromBuildingConfig(
      site=imported_building_config[0],
      building_config_dict=imported_building_config[1])
  model.Build()
  print('Exporting to spreadsheet to Google Sheets')
  model_dict = model.ToModelDictionary()
  export_engine = export_helper.GoogleSheetExport()
  google_sheets_service = authenticator.GetGoogleSheetsService(
      gcp_token_path=gcp_token_path)
  export_engine.WriteAllSheets(
      spreadsheet_id=spreadsheet_id,
      google_sheets_service=google_sheets_service,
      spreadsheet_range=SPREADSHEET_RANGE,
      model_dict=model_dict)


def main(parsed_args: ParseArgs) -> None:
  if parsed_args.spreadsheet_id and not parsed_args.building_config:
    _spreadsheet_workflow(
        spreadsheet_id=parsed_args.spreadsheet_id,
        gcp_token_path=parsed_args.token)
  elif parsed_args.building_config and parsed_args.spreadsheet_id:
    _bc_workflow(
        spreadsheet_id=parsed_args.spreadsheet_id,
        bc_filepath=parsed_args.building_config,
        gcp_token_path=parsed_args.token)


if __name__ == '__main__':
  args = ParseArgs().parse_args(sys.argv[1:])
  main(args)
