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
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either exintess or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Module for various ABEL workflows.."""

import os
import sys
from typing import List, Optional
import warnings
import webbrowser

# pylint: disable=g-importing-member
from model import authenticator
from model import export_helper
from model import import_helper
from model import model_helper
from model.arg_parser import ParseArgs
from model.constants import EXPORT_BUILDING_CONFIG_NAME
from model.constants import ONTOLOGY_ROOT
from model.constants import SPREADSHEET_RANGE
from model.constants import SPREADSHEET_VALIDATOR_FILE_NAME
from model.entity_operation import EntityOperation
from model.model_builder import Model
from validators.spreadsheet_validator import SpreadsheetValidator
from validate import handler


# TODO: b/296067081 - Write unit tests for workflow class.
class Workflow(object):
  """Class to model an ABEL workflow.

  Creating this class enables a more modular approach to implementing ABEL
  workfows. The various workflow pathway components are:
  1: Ingest a spreadsheet with no updates and create an INIT BC
  2: Ingest a modified spreadsheet and create an UPDATE BC
  3: Ingest an exported BC and write to spreadsheet that user can then modify.
  """

  def __init__(self, oauth_credential: str, modified_types_filepath: str =
  None, output_dir: str = None):
    self.google_sheets_service = (
        authenticator.GetGoogleSheetsServiceByCredential(oauth_credential)
    )
    self.modified_types_filepath = modified_types_filepath
    self.output_dir = output_dir

  def _ImportSpreadsheetAndBuildModel(self, spreadsheet_id) -> Model:
    """Reads a Google Sheets spreadsheet and builds an ABEL model.

    Args:
      spreadsheet_id: Google Sheets spreadsheed id.

    Returns:
      An ABEL Model instance and a list of EntityOperation instances.
    """
    is_spreadsheet_valid = False
    while not is_spreadsheet_valid:
      spreadsheet_validator = SpreadsheetValidator(
          filepath=os.path.join(
              self.output_dir, SPREADSHEET_VALIDATOR_FILE_NAME
          )
      )
      is_spreadsheet_valid = spreadsheet_validator.Validate(
          import_helper.GetAllSheets(
              google_sheets_service=self.google_sheets_service,
              spreadsheet_id=spreadsheet_id,
              spreadsheet_range=SPREADSHEET_RANGE,
          )
      )
      if not is_spreadsheet_valid:
        input(
            'Please resolve spreadsheet errors and press any key when done.'
            ' Validation logs can be found at: '
            f'{os.path.join(self.output_dir, SPREADSHEET_VALIDATOR_FILE_NAME)}'
        )
    unbuilt_model, operations = Model.Builder.FromSpreadsheet(
        import_helper.GetAllSheets(
            google_sheets_service=self.google_sheets_service,
            spreadsheet_id=spreadsheet_id,
            spreadsheet_range=SPREADSHEET_RANGE,
        )
    )
    return unbuilt_model.Build(), operations

  def _ImportBCAndBuildModel(self, bc_filepath: str) -> Model:
    """Reads a local Building Config YAML file and returns and ABEL Model.

    Returns:
      An ABEL model instance and a list of EntityOperation instances.
    """
    warnings.simplefilter("ignore", UserWarning)
    imported_building_config = import_helper.DeserializeBuildingConfiguration(
        filepath=bc_filepath
    )

    # STEP 2
    print('Building model from building configuration file.')
    unbuilt_model, operations = Model.Builder.FromBuildingConfig(
        site=imported_building_config[0],
        building_config_dict=imported_building_config[1],
    )
    return unbuilt_model.Build(), operations

  def _ExportAndWriteToSpreadsheet(
      self, model: Model, operations: Optional[List[EntityOperation]] = None
  ) -> tuple[str, str]:
    """Exports an ABEL spreadsheet for a user to interact with.

    Args:
      model: An ABEL Model instance.
      operations: [Optional] List of EntityOperations instances.

    Returns:
      A tuple where the first entry is the Url of the generated spreadsheet and
      the second entry is the spreadsheet id.
    """
    model_dict = model.ToModelDictionary(operations)
    export_engine = export_helper.GoogleSheetExport()
    spreadsheet_response = export_engine.CreateSpreadsheet(
        google_sheets_service=self.google_sheets_service,
        model_dict=model_dict,
    )
    return (
        spreadsheet_response.get('spreadsheetUrl'),
        spreadsheet_response.get('spreadsheetId'),
    )

  # TODO: b/296067791 - Validate building config before export.
  def _ValidateAndExportBuildingConfig(
      self,
      model: Model,
      operations: list[EntityOperation] = None,
      subscription: str = None,
      timeout: str = None
  ) -> None:
    """Helper function for validating and exporting a building config.

    Args:
      model: An ABEL Model instance.
      operations: [Optional] A list of EntityOperation instances for the model.
    """
    bc_path = os.path.join(self.output_dir, EXPORT_BUILDING_CONFIG_NAME)
    export_helper.BuildingConfigExport(
        model
    ).ExportBuildingConfiguration(
        filepath=bc_path,
        operations=operations,
    )
    # Run instance validator
    print('Validating building config yaml file export.')
    report_name = handler.RunValidation(
        filenames=[bc_path],
        report_directory=self.output_dir,
        modified_types_filepath=self.modified_types_filepath,
        default_types_filepath=ONTOLOGY_ROOT,
        subscription=subscription,
        timeout=timeout,
    )
    print(f'Instance validator log: {report_name}')
    print(f'Exported Building Configuration: {bc_path}')

  def SpreadsheetWorkflow(
      self,
      spreadsheet_id: str,
      bc_filepath: str = None,
      gcp_subscription: str = None,
      timeout: int = None
  ) -> None:
    """Workflow that Ingests a a spreadsheet and outputs a valid building
      config.

    If a building config path is provided to this workflow, then ABEL can
    compare entities in a spreadsheet to entities in a building config,
    and determine update operations. If no building config path is provided
    then the spreadsheet will be treating as an init config.

    Args:
        spreadsheet_id: Google Sheets spreadsheet ID.
        bc_filepath: Relative or Absolute filepath to a building config yaml
          file.
        gcp_subscription: Path to a GCP PubSub subscription.
        timeout: Timeout duration in seconds for listening to PubSub.
    """
    # TODO: b/
    if bc_filepath:
      bc_model, bc_operations = self._ImportBCAndBuildModel(bc_filepath)
    else:
      print('No building config input')
      bc_model = None

    if not spreadsheet_id:
      print('No spreadsheet id input.\nExiting ABEL...')
      sys.exit(0)

    ss_model, ss_operations = self._ImportSpreadsheetAndBuildModel(
      spreadsheet_id
    )
    generated_operations = model_helper.DetermineEntityOperations(
      current_model=bc_model, updated_model=ss_model
    )
    operations_list = model_helper.ReconcileOperations(
      generated_operations=generated_operations,
      model_operations=ss_operations,
    )
    self._ValidateAndExportBuildingConfig(
      model=ss_model,
      operations=operations_list,
      subscription=gcp_subscription,
      timeout=timeout
    )

  def ConfigWorkflow(self, bc_filepath: str) -> None:
    """Workflow to create a Google sheets spreadsheet from a building config"""

    bc_model, bc_operations = self._ImportBCAndBuildModel(bc_filepath)
    spreadsheet_details = self._ExportAndWriteToSpreadsheet(
        bc_model, bc_operations
    )

    # Write to spreadsheet
    webbrowser.open(spreadsheet_details[0])
