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
  ) -> None:
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
    if operations:
      export_helper.BuildingConfigExport(
          model
      ).ExportUpdateBuildingConfiguration(
          filepath=bc_path,
          operations=operations,
      )
    else:
      export_helper.BuildingConfigExport(model).ExportInitBuildingConfiguration(
          filepath=bc_path
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

  # TODO: b/296067948 - Ingest and export spreadsheet with update operations.
  def UpdateWorkflow(self) -> None:
    """Workflow for generating a building config with update operations.

    STEPS:
      1. Ingest a building config
      2. write to a spreadsheet
      3. Either let the user quit or build an update bc from updated spreadsheet
      4. If build update BC, ingest modified spreadsheet(same id) and bc(already
      persisting)
      5. Create operations with two models.
      6. Write to building config.
    """

    print(
        '\nHow would you like to use ABEL?\n'
        + '1: Edit or update an existing building config\n'
        + '2: Create building config from an updated spreadsheet\n'
        + 'q: quit\n'
    )
    function_choice = input('Please select an option: ')
    if function_choice == '1':
      # Export BC and build model
      self.bc_model, bc_operations = self._ImportBCAndBuildModel()
      spreadsheet_url, spreadsheet_id = self._ExportAndWriteToSpreadsheet(
          self.bc_model, bc_operations
      )

      # Write to spreadsheet
      webbrowser.open(spreadsheet_url)

      # Wait for user to edit spreadsheet
      input('Edit spreadsheet and press any key when done.')

      # Build model from spreadsheet
      self.ss_model, ss_operations = self._ImportSpreadsheetAndBuildModel(
          spreadsheet_id=spreadsheet_id
      )

      # Determine entity operations on an updated model
      generated_operations = model_helper.DetermineEntityOperations(
          current_model=self.bc_model, updated_model=self.ss_model
      )
      operations_list = model_helper.ReconcileOperations(
          generated_operations=generated_operations,
          model_operations=ss_operations,
      )

      # Finally export to building config
      export_engine = export_helper.BuildingConfigExport(model=self.ss_model)
      export_engine.ExportUpdateBuildingConfiguration(
          filepath=os.path.join(self.output_dir, EXPORT_BUILDING_CONFIG_NAME),
          operations=operations_list,
      )
    elif function_choice == '2':
      assert self.spreadsheet_id is not None and self.bc_filepath is not None
      self.bc_model = self._ImportBCAndBuildModel()[0]
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

  def InitWorkflow(self) -> None:
    """Workflow for generating a building config under the INITIALIZE operation.

    STEPS:
      1. Ingest and parse an ABEL spreadsheet.
      2. Export and validate a building config.
    """
    if not self.spreadsheet_id:
      self.spreadsheet_id = input(
          'Please provide a Google Sheets spreadsheet id.'
      )
    self.ss_model = self._ImportSpreadsheetAndBuildModel(self.spreadsheet_id)[0]
    self._ValidateAndExportBuildingConfig(model=self.ss_model)
