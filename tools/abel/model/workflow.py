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

  def __init__(self, argset: ParseArgs):
    self.google_sheets_service = (
        authenticator.GetGoogleSheetsServiceByCredential(argset.credential)
    )
    self.subscription = argset.subscription
    self.spreadsheet_id = argset.spreadsheet_id
    if not argset.building_config:
      self.bc_filepath = None
    else:
      self.bc_filepath = os.path.expanduser(argset.building_config)
    self.timeout = argset.timeout
    self.modified_types_filepath = argset.modified_types_filepath
    self.output_dir = argset.output_dir
    self.bc_model = None
    self.ss_model = None

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

  def _ImportBCAndBuildModel(self) -> Model:
    """Reads a local Building Config YAML file and returns and ABEL Model.

    Returns:
      An ABEL model instance and a list of EntityOperation instances.
    """
    imported_building_config = import_helper.DeserializeBuildingConfiguration(
        filepath=self.bc_filepath
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
    print('Validating Export.')
    report_name = handler.RunValidation(
        filenames=[bc_path],
        report_directory=self.output_dir,
        modified_types_filepath=self.modified_types_filepath,
        default_types_filepath=ONTOLOGY_ROOT,
        subscription=self.subscription,
        timeout=self.timeout,
    )
    print(f'Instance validator log: {report_name}')
    print(f'Exported Building Configuration: {bc_path}')

  def SpreadsheetWorkflow(self) -> None:
    """Workflow to write a Building Config from a spreadsheet

    Can either take just a spreadsheet or a spreadsheet and a building config.
    """
    # If user doesn't exit, write spreadsheet to a building config.
    if not self.bc_model:
      # This case statement will go away once ABEL can call DB API.
      # If a person just wants to create a bc, they shouldn't need to provide
      # a spreadsheet.
      print('No building config input')
      pass
    elif not self.ss_model:
      print('No spreadsheet id input.\nExiting ABEL...')
      sys.exit(0)

    self.ss_model, ss_operations = self._ImportSpreadsheetAndBuildModel(
      self.spreadsheet_id
    )
    generated_operations = model_helper.DetermineEntityOperations(
      current_model=self.bc_model, updated_model=self.ss_model
    )
    operations_list = model_helper.ReconcileOperations(
      generated_operations=generated_operations,
      model_operations=ss_operations,
    )
    self._ValidateAndExportBuildingConfig(
      model=self.ss_model,
      operations=operations_list,
    )

  def ConfigWorkflow(self) -> None:
    """Workflow to create a Google sheets spreadsheet from a building config"""

    self.bc_model, bc_operations = self._ImportBCAndBuildModel()
    spreadsheet_details = self._ExportAndWriteToSpreadsheet(
        self.bc_model, bc_operations
    )

    # Write to spreadsheet
    webbrowser.open(spreadsheet_details[0])
