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

"""Classes and methods for working with state values for multistate fields in the ontology."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import re

from yamlformat.validator import base_lib
from yamlformat.validator import config_folder_lib
from yamlformat.validator import findings_lib

STATE_NAME_VALIDATOR = re.compile(r'^[A-Z]+(_[A-Z]+)*$')


class StateUniverse(findings_lib.FindingsUniverse):
  """Helper class to represent the defined universe of states.

  Only contains valid states.
  """

  def _GetNamespaceMapValue(self, namespace):
    """Helper method for FindingsUniverse._MakeNamespaceMap.

    Used to create a map from namespace names to state maps.

    Args:
      namespace: StateNamespace

    Returns:
      The states map from the namespace.
    """
    return namespace.states

  def GetStatesMap(self, namespace_name):
    """Returns a map from state names to State objects in the namespace.

    If there are no defined states in the namespace, returns an empty dict.

    Args:
      namespace_name: string.
    """
    return self._namespace_map.get(namespace_name, {})


class StateFolder(config_folder_lib.ConfigFolder):
  """Class representing a folder of States.

  Class contains all the context information and methods to validate states.

  Args:
    folderpath: required string with full path to the folder containing states.
      Path should be relative to google3/ and have no leading or trailing /.
  Attributes:
    local_namespace: object representing the contents of the local namespace
  """

  def __init__(self, folderpath):
    super(StateFolder, self).__init__(folderpath,
                                      base_lib.ComponentType.MULTI_STATE)
    self.local_namespace = StateNamespace(self._namespace_name)

  def AddState(self, state):
    """Validates a state and adds it to the correct namespace.

    Findings will be added to the StateFolder if validation finds any problems.
    Use AddFromConfig for validation of input file. The state will not be added
    if validation fails.

    Args:
      state: State object to add.
    """
    if not state.IsValid():
      self.AddFindings(state.GetFindings())
      return
    self.local_namespace.InsertState(state)

  def _AddFromConfigHelper(self, document, context):
    """Helper method that reads a single yaml document and adds all states found.

    Args:
      document: yaml document
      context: config file context
    """
    for state in document:
      description = document[state]
      self.AddState(State(state, description, context))


class StateNamespace(findings_lib.Findings):
  """Class representing a namespace of states.

  Args:
    namespace: required string representing the name of the namespace.
  Attributes:
    namespace: string name of this namespace
    states: a map from state names to State objects defined in this namespace.
  """

  def __init__(self, namespace):
    super(StateNamespace, self).__init__()
    self.namespace = namespace
    self.states = {}

  def _GetDynamicFindings(self, filter_old_warnings):
    findings = []
    for state in self.states.values():
      findings += state.GetFindings(filter_old_warnings)
    return findings

  def InsertState(self, state):
    """Inserts a state into this namespace.

    If the state already exists in the namespace, adds a
    DuplicateStateDefinitionError to the findings and the duplicate is not
    inserted.

    Args:
      state: state object to attempt to insert.
    """
    if state.name in self.states:
      self.AddFinding(
          findings_lib.DuplicateStateDefinitionError(state, self.namespace))
      return
    self.states[state.name] = state


class State(findings_lib.Findings):
  """Namespace-unaware class representing an individual state definition.

  Args:
    name: required string representing the state.
    description: optional (for now) string semantic definition for the state.
    context: optional object with the config file location of this state.
  Attributes:
    name: the full name (without namespace) of this state
    description: explanation of what this state represents
    context: the config file context for where this state was defined
  """

  def __init__(self, name, description=None, context=None):
    super(State, self).__init__()
    self.name = name
    self.description = description
    self.context = context

    if not isinstance(name, str):
      self.AddFinding(findings_lib.IllegalKeyTypeError(name, context))
    elif not STATE_NAME_VALIDATOR.match(name):
      self.AddFinding(findings_lib.IllegalCharacterError(name, context))
    if not description:
      self.AddFinding(findings_lib.MissingStateDescriptionWarning(self))

  def __eq__(self, other):
    if isinstance(other, State):
      return self.name == other.name and self.description == other.description
    return False

  def __ne__(self, other):
    return not self.__eq__(other)

  __hash__ = None
