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
"""Sets up a minimal test config universe required for testing."""

from google3.third_party.digitalbuildings.tools.validators.instance_validator.validate.universe_helper import connections
from google3.third_party.digitalbuildings.tools.validators.instance_validator.validate.universe_helper import fields
from google3.third_party.digitalbuildings.tools.validators.instance_validator.validate.universe_helper import states
from google3.third_party.digitalbuildings.tools.validators.instance_validator.validate.universe_helper import subfields
from google3.third_party.digitalbuildings.tools.validators.instance_validator.validate.universe_helper import types
from google3.third_party.digitalbuildings.tools.validators.instance_validator.validate.universe_helper import units
from google3.third_party.digitalbuildings.tools.validators.ontology_validator.yamlformat.validator import entity_type_lib
from google3.third_party.digitalbuildings.tools.validators.ontology_validator.yamlformat.validator import field_lib
from google3.third_party.digitalbuildings.tools.validators.ontology_validator.yamlformat.validator import namespace_validator
from google3.third_party.digitalbuildings.tools.validators.ontology_validator.yamlformat.validator import presubmit_validate_types_lib
from google3.third_party.digitalbuildings.tools.validators.ontology_validator.yamlformat.validator import unit_lib


def create_simplified_universe() -> presubmit_validate_types_lib.ConfigUniverse:
  """Creates a simplified test universe with minimal configuration for testing.

  Returns:
    config_universe a partially defined ConfigUniverse
  """

  # constant universes
  state_universe = states.STATE_UNIVERSE
  connection_universe = connections.CONNECTION_UNIVERSE
  subfield_universe = subfields.SUBFIELD_UNIVERSE

  # update unit folder with subfield_universe
  unit_folder = unit_lib.UnitFolder(folderpath='units')
  unit_folder.local_namespace.subfields = subfield_universe.GetSubfieldsMap(
      unit_folder.local_namespace.namespace)
  unit_folder.AddFromConfig(
      config_filename='units/units.yaml', documents=[units.UNIT_DOCUMENT])

  unit_universe = unit_lib.UnitUniverse(folders=[unit_folder])

  # subfield universe has to validate unit universe
  subfield_universe.ValidateUnits(unit_universe)

  # field universe depends on subfield and state universes
  field_folder = field_lib.FieldFolder(folderpath='fields')
  field_folder.local_namespace.subfields = subfield_universe.GetSubfieldsMap(
      field_folder.local_namespace.namespace)
  field_folder.local_namespace.states = state_universe.GetStatesMap(
      field_folder.local_namespace.namespace)

  field_folder.AddFromConfig(
      config_filename='fields/telemetry_fields.yaml',
      documents=[fields.TELEMETRY_FIELDS_DOCUMENT])
  field_folder.AddFromConfig(
      config_filename='fields/metadata_fields.yaml',
      documents=[fields.METADATA_FIELDS_DOCUMENT])

  field_universe = field_lib.FieldUniverse(folders=[field_folder])

  # entity type universe depends on field universe
  global_type_folder = entity_type_lib.EntityTypeFolder(
      folderpath='entity_types', field_universe=field_universe)
  facilities_type_folder = entity_type_lib.EntityTypeFolder(
      folderpath='FACILITIES/entity_types', field_universe=field_universe)
  gateways_type_folder = entity_type_lib.EntityTypeFolder(
      folderpath='GATEWAYS/entity_types', field_universe=field_universe)
  hvac_type_folder = entity_type_lib.EntityTypeFolder(
      folderpath='HVAC/entity_types', field_universe=field_universe)

  global_type_folder.AddFromConfig(
      config_filename='entity_types/global.yaml',
      documents=[types.GLOBAL_TYPES_DOCUMENT])
  facilities_type_folder.AddFromConfig(
      config_filename='FACILITIES/entity_types/Facilities.yaml',
      documents=[types.FACILITIES_TYPES_DOCUMENT])
  gateways_type_folder.AddFromConfig(
      config_filename='GATEWAYS/entity_types/GATEWAYS.yaml',
      documents=[types.GATEWAYS_TYPES_DOCUMENT])
  hvac_type_folder.AddFromConfig(
      config_filename='HVAC/entity_types/ANALYSIS.yaml',
      documents=[types.HVAC_ANALYSIS_TYPES_DOCUMENT])
  hvac_type_folder.AddFromConfig(
      config_filename='HVAC/entity_types/ABSTRACT.yaml',
      documents=[types.HVAC_ABSTRACT_TYPES_DOCUMENT])
  hvac_type_folder.AddFromConfig(
      config_filename='HVAC/entity_types/CHWS.yaml',
      documents=[types.HVAC_CHWS_TYPES_DOCUMENT])
  hvac_type_folder.AddFromConfig(
      config_filename='HVAC/entity_types/GENERALTYPES.yaml',
      documents=[types.HVAC_GENERAL_TYPES_DOCUMENT])
  hvac_type_folder.AddFromConfig(
      config_filename='HVAC/entity_types/SDC.yaml',
      documents=[types.HVAC_SDC_TYPES_DOCUMENT])
  hvac_type_folder.AddFromConfig(
      config_filename='HVAC/entity_types/DMP.yaml',
      documents=[types.HVAC_DMP_TYPES_DOCUMENT])

  entity_type_universe = entity_type_lib.EntityTypeUniverse(
      entity_type_folders=[
          global_type_folder, facilities_type_folder, gateways_type_folder,
          hvac_type_folder
      ])

  config_universe = presubmit_validate_types_lib.ConfigUniverse(
      entity_type_universe=entity_type_universe,
      field_universe=field_universe,
      subfield_universe=subfield_universe,
      state_universe=state_universe,
      connection_universe=connection_universe,
      unit_universe=unit_universe)

  # call this to expand inherited fields
  namespace_validator.NamespaceValidator(
      config_universe.GetEntityTypeNamespaces())

  return config_universe
