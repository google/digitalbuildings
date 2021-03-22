# Copyright 2020 Google LLC
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
"""Classes and methods for working with connection values in the ontology."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import re
from typing import Optional, Dict, List

from yamlformat.validator import base_lib
from yamlformat.validator import config_folder_lib
from yamlformat.validator import findings_lib

CONNECTION_NAME_VALIDATOR = re.compile(r'^[A-Z]+(_[A-Z]+)*$')


class ConnectionUniverse(findings_lib.FindingsUniverse):
  """Helper class to represent the defined universe of connections.

  Only contains valid connections.
  """

  def _GetNamespaceMapValue(
      self,
      namespace: 'ConnectionNamespace') -> Dict[str, Dict[str, 'Connection']]:
    """Helper method for FindingsUniverse._MakeNamespaceMap.

    Used to create a map from namespace names to connection maps.

    Args:
      namespace: ConnectionNamespace

    Returns:
      The connections map from the namespace.
    """
    return namespace.connections

  def IsDefined(
      self,
      connection_name: str,
      namespace_name: Optional[str] = base_lib.GLOBAL_NAMESPACE) -> bool:
    return connection_name in self.GetConnectionsMap(namespace_name)

  def GetConnectionsMap(self, namespace_name: str) -> Dict[str, 'Connection']:
    """Returns a map from connection names to Connections in the namespace.

    If there are no defined connections in the namespace, returns an empty dict.

    Args:
      namespace_name: string.
    """
    return self._namespace_map.get(namespace_name, {})


class ConnectionFolder(config_folder_lib.ConfigFolder):
  """Class representing a folder of Connections.

  Class contains the context information and methods to validate connections.

  Attributes:
    local_namespace: object representing the contents of the local namespace
  """

  def __init__(self, folderpath: str):
    """Creates a ConnectionFolder.

    Args:
      folderpath: required str with full path to folder containing connections.
    """
    super(ConnectionFolder, self).__init__(folderpath,
                                           base_lib.ComponentType.CONNECTION)
    self.local_namespace = ConnectionNamespace(self._namespace_name)

    if base_lib.GLOBAL_NAMESPACE != self.local_namespace.namespace:
      self.local_namespace.AddFinding(
          findings_lib.InvalidConnectionNamespaceError(
              self.local_namespace.namespace,
              findings_lib.FileContext(folderpath)))

  def AddConnection(self, connection: 'Connection'):
    """Validates a connection and adds it to the correct namespace.

    Findings will be added to the ConnectionFolder if validation finds any
    problems. Use AddFromConfig for validation of input file. The connection
    will not be added if validation fails.

    Args:
      connection: Connection object to add.
    """
    if not connection.IsValid():
      self.AddFindings(connection.GetFindings())
      return
    self.local_namespace.InsertConnection(connection)

  def _AddFromConfigHelper(self, document: object,
                           context: findings_lib.FileContext) -> None:
    """Reads a single yaml document and adds all connections found.

    Args:
      document: yaml document
      context: config file context
    """
    for connection in document:
      description = document[connection].get('description', '')
      self.AddConnection(Connection(connection, description, context))


class ConnectionNamespace(findings_lib.Findings):
  """Class representing a namespace of connections.

  Attributes:
    namespace: string name of this namespace
    connections: a map from connection names to Connections in this namespace.
  """

  def __init__(self, namespace: str):
    super(ConnectionNamespace, self).__init__()
    self.namespace = namespace
    self.connections = {}

  def _GetDynamicFindings(
      self, filter_old_warnings: bool) -> List[findings_lib.Finding]:
    findings = []
    for connection in self.connections.values():
      findings += connection.GetFindings(filter_old_warnings)
    return findings

  def InsertConnection(self, connection: 'Connection') -> None:
    """Inserts a connection into this namespace.

    If the connection already exists in the namespace, adds a
    DuplicateConnectionDefinitionError to the findings and the duplicate is not
    inserted.

    Args:
      connection: connection object to attempt to insert.
    """
    if connection.name in self.connections:
      self.AddFinding(
          findings_lib.DuplicateConnectionDefinitionError(connection, self))
      return
    self.connections[connection.name] = connection


class Connection(findings_lib.Findings):
  """Namespace-unaware class representing an individual connection definition.

  Attributes:
    name: the full name (without namespace) of this connection
    description: explanation of what this connection represents
    context: the config file context for where this connection was defined
  """

  def __init__(self,
               name: str,
               description: str = None,
               context: findings_lib.FileContext = None):
    super(Connection, self).__init__()
    self.name = name
    self.description = description
    self.context = context

    if not isinstance(name, str):
      self.AddFinding(findings_lib.IllegalKeyTypeError(name, context))
    elif not CONNECTION_NAME_VALIDATOR.match(name):
      self.AddFinding(findings_lib.IllegalCharacterError(name, context))
    if not description:
      self.AddFinding(findings_lib.MissingConnectionDescriptionWarning(self))

  def __eq__(self, other):
    if isinstance(other, Connection):
      return self.name == other.name and self.description == other.description
    return False

  def __ne__(self, other):
    return not self.__eq__(other)

  __hash__ = None
