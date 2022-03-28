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
"""Helper module for concrete model construction."""

from typing import List, Dict, Any

from model.entity import Entity
from model.entity_field import EntityField
from model.site import Site
from google3.third_party.digitalbuildings.tools.concrete_model.translators.loadsheet import Spreadsheet


class ModelBuilder(object):
  """Class to  build a Concrete Model from standard data types.

  Attributes:
    fields: A list of EntityField instances.
    entities: A list Entity instances.
    sites: A list of site instances.
  """

  def __init__(self):
    self.fields: List[EntityField] = []
    self.entities: List[Entity] = []
    self.sites: List[Site] = []

  @classmethod
  def FromLoadsheet(cls, spreadsheet: Spreadsheet) ->...:
    """Converts a Spreadsheet instance into fields, entities, and sites.

    Args:
      spreadsheet: A Spreadsheet instance.

    Returns:
      An instance of ModelBuilder.
    """

  @classmethod
  def FromYaml(cls, building_config_yaml: Dict[str, Any]) ->...:
    """Converts a yaml document into fields, entities, and sites.

    Args:
      building_config_yaml: A yaml document containing building(site) data.

    Returns:
      A ModelBuilder instance.
    """

  # TODO(traviscwelch): Create custom DisconnectedGraphError exception.
  def Build(self) -> bool:
    """Connects all entities to a site, fields to entities, and entities to entities based on attributes.

    Raises:
      DisconnectedGraphError: raised if there exists an un-connected element(s)
      in the concrete model graph.
    """
