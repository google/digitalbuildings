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
"""Main module for DBO explorer."""

import os
import sys
from typing import Optional
import warnings

from model import authenticator
from model import export_helper
from model import import_helper
from model.arg_parser import ParseArgs
from model.constants import EXPORT_BUILDING_CONFIG_NAME
from model.constants import INSTANCE_VALIDATION_REPORT_NAME
from model.constants import ONTOLOGY_ROOT
from model.constants import SPREADSHEET_RANGE
from model.constants import SPREADSHEET_VALIDATOR_FILE_NAME
from model.model_builder import ModelBuilder
from validators.spreadsheet_validator import SpreadsheetValidator
from validate import handler


# pylint: disable=line-too-long
@DeprecationWarning
def _token_spreadsheet_workflow(
    spreadsheet_id: str,
    gcp_token_path: Optional[str] = None,
    subscription: Optional[str] = None,
    service_account: Optional[str] = None,
    timeout: Optional[float] = None,
    modified_types_filepath: Optional[str] = None,
    output_dir: Optional[str] = os.getcwd(),
) -> None:
  """Helper function for executing the spreadsheet -> building config workflow.

  DEPRECATED

  User should use _credential_spreadsheet_workflow() as an alternative.

  Args:
    spreadsheet_id: Google Sheets spreadsheet ID to be parsed into ABEL.
    gcp_token_path: Path to GCP token for authenticating against Google sheets
      API. This is a short-lived credential for a service account as documented
      https://cloud.google.com/iam/docs/create-short-lived-credentials-direct.
    subscription: [Optional] Fully qualified path to a Google Cloud pubsub
      subscription.
    service_account: [Optional] Fully qualified path to a service account key
      file corresponding to an account that can read subscription topic
      messages.
    timeout: [Optional] The timeout duration in seconds for the telemetry
      validation test. The default value is 600 seconds, or 10 minutes.
    modified_types_filepath: [Optional] A path to a modified ontology. Default
      is the DigitalBuildings Ontology.
    output_dir: [Optional] A path to a directory where ABEL can output Building
      Config files and validation logs.
  """
  warnings.warn('Service accounts for authentication are to be derpecated in gcp')
  # gcp token path to be deprecated
  google_sheets_service = authenticator.GetGoogleSheetsServiceByToken(
      gcp_token_path=gcp_token_path
  )

  print(f'Importing spreadsheet from Google sheets: {spreadsheet_id}')
  imported_spreadsheet = import_helper.GetAllSheets(
      google_sheets_service=google_sheets_service,
      spreadsheet_id=spreadsheet_id,
      spreadsheet_range=SPREADSHEET_RANGE,
  )
  spreadsheet_validator = SpreadsheetValidator(
      filepath=os.path.join(output_dir, SPREADSHEET_VALIDATOR_FILE_NAME)
  )
  is_spreadsheet_valid = spreadsheet_validator.Validate(imported_spreadsheet)
  if not is_spreadsheet_valid:
    print(
        'Please resolve spreadsheet errors:'
        f' {os.path.join(output_dir, SPREADSHEET_VALIDATOR_FILE_NAME)}'
    )
  else:
    print('Spreadsheet validated.')
    # Build model
    print('Building model.')
    model_builder = ModelBuilder.FromSpreadsheet(imported_spreadsheet)
    model_builder.Build()
    print('Model built!')
    # export
    new_bc_exporter = export_helper.BuildingConfigExport(model_builder)
    new_bc_exporter.ExportBuildingConfiguration(
        filepath=os.path.join(output_dir, EXPORT_BUILDING_CONFIG_NAME)
    )
    # Run instance validator
    print('Validating Export.')
    handler.RunValidation(
        filenames=[os.path.join(output_dir, EXPORT_BUILDING_CONFIG_NAME)],
        report_filename=os.path.join(
            output_dir, INSTANCE_VALIDATION_REPORT_NAME
        ),
        modified_types_filepath=modified_types_filepath,
        default_types_filepath=ONTOLOGY_ROOT,
        subscription=subscription,
        service_account=service_account,
        timeout=timeout,
    )
    print(f'Instance validator log: {INSTANCE_VALIDATION_REPORT_NAME}')
    print(f'Exported Building Configuration: {EXPORT_BUILDING_CONFIG_NAME}')


@DeprecationWarning
def _token_bc_workflow(
    spreadsheet_id: str,
    bc_filepath: str,
    gcp_token_path: Optional[str] = None,
    modified_types_filepath: Optional[str] = None,
    output_dir: Optional[str] = os.getcwd(),
) -> None:
  """Helper function for Building Config -> spreadsheet workflow.

  DEPRECATED

  User should use _credential_bc_workflow() as an alternative.

  Args:
    spreadsheet_id: Exported Google spreadsheets id.
    bc_filepath: Imported Building Config filepath.
    gcp_token_path: Path to GCP token for authenticating against Google sheets
      API. This is a short-lived credential for a service account as documented
      https://cloud.google.com/iam/docs/create-short-lived-credentials-direct.
    modified_types_filepath: [Optional] A path to a modified ontology. Default
      is the DigitalBuildings Ontology.
    output_dir: [Optional] A path to a directory where ABEL can output Building
      Config files and validation logs.
  """
  print('Validating imported Building Config.')
  handler.RunValidation(
      filenames=[bc_filepath],
      report_filename=os.path.join(output_dir, INSTANCE_VALIDATION_REPORT_NAME),
      modified_types_filepath=modified_types_filepath,
      default_types_filepath=ONTOLOGY_ROOT,
  )
  print(f'Importing Building Configuration file from {bc_filepath}.')
  imported_building_config = import_helper.DeserializeBuildingConfiguration(
      filepath=bc_filepath
  )
  print('Building model from building configuration file.')
  model = ModelBuilder.FromBuildingConfig(
      site=imported_building_config[0],
      building_config_dict=imported_building_config[1],
  )
  model.Build()
  print('Exporting to spreadsheet to Google Sheets')
  model_dict = model.ToModelDictionary()
  export_engine = export_helper.GoogleSheetExport()

  # gcp token path to be deprecated
  google_sheets_service = authenticator.GetGoogleSheetsServiceByToken(
      gcp_token_path=gcp_token_path
  )

  export_engine.WriteAllSheets(
      spreadsheet_id=spreadsheet_id,
      google_sheets_service=google_sheets_service,
      spreadsheet_range=SPREADSHEET_RANGE,
      model_dict=model_dict,
  )


# pylint: disable=line-too-long
def _credential_spreadsheet_workflow(
    spreadsheet_id: str,
    gcp_credential_path: Optional[str] = None,
    subscription: Optional[str] = None,
    service_account: Optional[str] = None,
    timeout: Optional[float] = None,
    modified_types_filepath: Optional[str] = None,
    output_dir: Optional[str] = os.getcwd(),
) -> None:
  """Helper function for executing the spreadsheet -> building config workflow.

  Args:
    spreadsheet_id: Google Sheets spreadsheet ID to be parsed into ABEL.
    gcp_credential_path: Path to GCP oauth client credential file for
      authenticating against Google sheets API. This is an OAuth credential as
      documented.
      https://developers.google.com/sheets/api/quickstart/python
    subscription: [Optional] Fully qualified path to a Google Cloud pubsub
      subscription.
    service_account: [Optional] Fully qualified path to a service account key
      file corresponding to an account that can read subscription topic
      messages.
    timeout: [Optional] The timeout duration in seconds for the telemetry
      validation test. The default value is 600 seconds, or 10 minutes.
    modified_types_filepath: [Optional] A path to a modified ontology. Default
      is the DigitalBuildings Ontology.
    output_dir: [Optional] A path to a directory where ABEL can output Building
      Config files and validation logs.
  """
  google_sheets_service = authenticator.GetGoogleSheetsServiceByCredential(
      gcp_credential_path
  )

  print(f'Importing spreadsheet from Google sheets: {spreadsheet_id}')
  imported_spreadsheet = import_helper.GetAllSheets(
      google_sheets_service=google_sheets_service,
      spreadsheet_id=spreadsheet_id,
      spreadsheet_range=SPREADSHEET_RANGE,
  )
  spreadsheet_validator = SpreadsheetValidator(
      filepath=os.path.join(output_dir, SPREADSHEET_VALIDATOR_FILE_NAME)
  )
  is_spreadsheet_valid = spreadsheet_validator.Validate(imported_spreadsheet)
  if not is_spreadsheet_valid:
    print(
        'Please resolve spreadsheet errors:'
        f' {os.path.join(output_dir, SPREADSHEET_VALIDATOR_FILE_NAME)}'
    )
  else:
    print('Spreadsheet validated.')
    # Build model
    print('Building model.')
    model_builder = ModelBuilder.FromSpreadsheet(imported_spreadsheet)
    model_builder.Build()
    print('Model built!')
    # export
    new_bc_exporter = export_helper.BuildingConfigExport(model_builder)
    new_bc_exporter.ExportBuildingConfiguration(
        filepath=os.path.join(output_dir, EXPORT_BUILDING_CONFIG_NAME)
    )
    # Run instance validator
    print('Validating Export.')
    handler.RunValidation(
        filenames=[os.path.join(output_dir, EXPORT_BUILDING_CONFIG_NAME)],
        report_filename=os.path.join(
            output_dir, INSTANCE_VALIDATION_REPORT_NAME
        ),
        modified_types_filepath=modified_types_filepath,
        default_types_filepath=ONTOLOGY_ROOT,
        subscription=subscription,
        service_account=service_account,
        timeout=timeout,
    )
    print(f'Instance validator log: {INSTANCE_VALIDATION_REPORT_NAME}')
    print(f'Exported Building Configuration: {EXPORT_BUILDING_CONFIG_NAME}')


def _credential_bc_workflow(
    spreadsheet_id: str,
    bc_filepath: str,
    gcp_credential_path: Optional[str] = None,
    modified_types_filepath: Optional[str] = None,
    output_dir: Optional[str] = os.getcwd(),
) -> None:
  """Helper function for Building Config -> spreadsheet workflow.

  Args:
    spreadsheet_id: Exported Google spreadsheets id.
    bc_filepath: Imported Building Config filepath.
    gcp_credential_path: Path to GCP oauth client credential file for
      authenticating against Google sheets API. This is an OAuth credential as
      documented.
      https://developers.google.com/sheets/api/quickstart/python
    modified_types_filepath: [Optional] A path to a modified ontology. Default
      is the DigitalBuildings Ontology.
    output_dir: [Optional] A path to a directory where ABEL can output Building
      Config files and validation logs.
  """
  print('Validating imported Building Config.')
  handler.RunValidation(
      filenames=[bc_filepath],
      report_filename=os.path.join(output_dir, INSTANCE_VALIDATION_REPORT_NAME),
      modified_types_filepath=modified_types_filepath,
      default_types_filepath=ONTOLOGY_ROOT,
  )
  print(f'Importing Building Configuration file from {bc_filepath}.')
  imported_building_config = import_helper.DeserializeBuildingConfiguration(
      filepath=bc_filepath
  )
  print('Building model from building configuration file.')
  model = ModelBuilder.FromBuildingConfig(
      site=imported_building_config[0],
      building_config_dict=imported_building_config[1],
  )
  model.Build()
  print('Exporting to spreadsheet to Google Sheets')
  model_dict = model.ToModelDictionary()
  export_engine = export_helper.GoogleSheetExport()

  google_sheets_service = authenticator.GetGoogleSheetsServiceByCredential(
      gcp_credential_path
  )

  export_engine.WriteAllSheets(
      spreadsheet_id=spreadsheet_id,
      google_sheets_service=google_sheets_service,
      spreadsheet_range=SPREADSHEET_RANGE,
      model_dict=model_dict,
  )


def main(parsed_args: ParseArgs) -> None:
  # gcp_token_path to be deprecated
  if parsed_args.token is None and parsed_args.credential is None:
    raise ValueError(
        'gcp_token_path and gcp_credential_path cannot both be None'
    )
  if parsed_args.token and parsed_args.credential:
    raise ValueError(
        'gcp_token_path and gcp_credential_path cannot both be present'
    )
  if parsed_args.spreadsheet_id and not parsed_args.building_config:
    _token_spreadsheet_workflow(
        spreadsheet_id=parsed_args.spreadsheet_id,
        gcp_token_path=parsed_args.token,
        modified_types_filepath=args.modified_types_filepath,
        subscription=parsed_args.subscription,
        service_account=parsed_args.service_account,
        output_dir=args.output_dir,
    )
  elif parsed_args.building_config and parsed_args.spreadsheet_id:
    _token_bc_workflow(
        spreadsheet_id=parsed_args.spreadsheet_id,
        bc_filepath=parsed_args.building_config,
        gcp_token_path=parsed_args.token,
        modified_types_filepath=args.modified_types_filepath,
        output_dir=args.output_dir,
    )
  if parsed_args.spreadsheet_id and not parsed_args.building_config:
    _credential_spreadsheet_workflow(
        spreadsheet_id=parsed_args.spreadsheet_id,
        gcp_credential_path=parsed_args.credential,
        modified_types_filepath=args.modified_types_filepath,
        subscription=parsed_args.subscription,
        service_account=parsed_args.service_account,
        output_dir=args.output_dir,
    )
  elif parsed_args.building_config and parsed_args.spreadsheet_id:
    _credential_bc_workflow(
        spreadsheet_id=parsed_args.spreadsheet_id,
        bc_filepath=parsed_args.building_config,
        gcp_credential_path=parsed_args.credential,
        modified_types_filepath=args.modified_types_filepath,
        output_dir=args.output_dir,
    )


if __name__ == '__main__':
  args = ParseArgs().parse_args(sys.argv[1:])
  main(args)
