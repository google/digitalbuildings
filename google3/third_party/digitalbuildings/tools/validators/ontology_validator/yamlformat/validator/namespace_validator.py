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

"""Class for validating entity types for consistency across their namespaces.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from google3.third_party.digitalbuildings.tools.validators.ontology_validator.yamlformat.validator import base_lib
from google3.third_party.digitalbuildings.tools.validators.ontology_validator.yamlformat.validator import findings_lib


MIN_SIZE_FOR_LOCAL_FIELD_DUPES = 2


class NamespaceValidator(findings_lib.Findings):
  """Creates NamespaceValidator object to validate types across namespaces.

  Records any findings found during validation.

  Args:
    type_namespaces: a list of TypeNamespace objects.

  Attributes:
    type_namespaces_map: a dictionary. Keys are namespace strings and
      values are TypeNamespace objects. All entity types within
      TypeNamespace objects are expanded, with inherited_field_names updated and
      inherited_fields_expanded set to True.

  Returns:
    An instance of the NamespaceValidator class.
  """

  def __init__(self, type_namespaces):

    super(NamespaceValidator, self).__init__()

    self.type_namespaces_map = {}
    self._CreateTypeNamespacesMap(type_namespaces)
    self._ExpandTypesMap(self.type_namespaces_map)
    self._FindBadIncrements(self.type_namespaces_map)

    # if any fatal inheritance errors were found, don't do this check
    if self.IsValid():
      self._CheckDuplicateFieldSets(self.type_namespaces_map)

  def _CreateTypeNamespacesMap(self, type_namespaces):
    """Creates a dict mapping namespace strings to TypeNamespace objects.

    Sets the self.type_namespaces_map attribute of the class.

    Args:
      type_namespaces: a list of TypeNamespace objects.
    """
    for type_namespace in type_namespaces:
      # Qualification is a no-op if completed already (which it should be).
      type_namespace.QualifyParentNames()
      self.type_namespaces_map[type_namespace.namespace] = type_namespace

  def _ExpandTypesMap(self, type_namespaces_map):
    """Expand the fields for all types within type_namespaces_map."""
    for type_namespace in type_namespaces_map.values():
      namespace = type_namespace.namespace
      for entity_type in type_namespace.valid_types_map.values():
        on_stack = set()
        try:
          self._ExpandFieldsForType(namespace, entity_type, on_stack)
        # terminate if any fatal inheritance errors are encountered
        except (findings_lib.NonexistentEntityProcessError,
                findings_lib.InheritanceCycleProcessError):
          break

  def _ExpandFieldsForType(self, namespace, entity_type, on_stack):
    """Updates the inherited_field_names attribute for an entity recursively.

    Uses a DFS approach. Expands fields during the DFS according to parent
       relationships and updates inherited_field_names for all entity
       types encountered. All types encountered are marked as expanded
       (inherited_fields_expanded is set to True)

    If cycles are detected in the inheritance graph, records
      InheritanceCycleError.
    If a parent entity type does not exist, records NonexistentParentError.

    Args:
      namespace: namespace we are currently in.
      entity_type: current entity_type object.
      on_stack: set to keep track of nodes on the recursion stack.

    Returns:
      Set of local and inherited fields for entity_type, if it exists.

    Raises:
      NonexistentEntityProcessError: entity type does not exist.
      InheritanceCycleProcessError: inheritance cycle detected.
    """

    # if current entity does not exist, record error
    if not entity_type:
      raise findings_lib.NonexistentEntityProcessError('')

    # If reached leaf node or entity_type has already been expanded,
    # return the union of the local and inherited field sets
    if not entity_type.parent_names or entity_type.inherited_fields_expanded:
      entity_type.inherited_fields_expanded = True
      return entity_type.GetAllFields()

    # Add current entity to recursion stack.
    stack_key = '{0}/{1}'.format(namespace, entity_type.typename)
    on_stack.add(stack_key)

    # Recurse for all parents. If any parent is in on_stack,
    # report a cycle.
    for parent_literal in entity_type.parent_names:
      # Get namespace info and a normalized key from parent.
      # Parent_name has already been validated for formatting.
      parent_tuple = entity_type.parent_names[parent_literal]
      parent_namespace = parent_tuple.namespace
      parent_name = parent_tuple.typename
      parent_key = parent_literal

      # if on stack, there is a cycle
      if parent_key in on_stack:
        self.AddFinding(findings_lib.InheritanceCycleError(
            entity_type, parent_literal))
        raise findings_lib.InheritanceCycleProcessError('')

      # Recurse.
      try:
        parent_type = None
        type_namespace = self.type_namespaces_map.get(parent_namespace)
        if type_namespace is not None:
          parent_type = type_namespace.valid_types_map.get(parent_name)
        fields = self._ExpandFieldsForType(
            parent_namespace, parent_type, on_stack)
      except findings_lib.NonexistentEntityProcessError as e:
        self.AddFinding(findings_lib.NonexistentParentError(
            entity_type, parent_key))
        raise e
      for field in fields:
        fv = fields[field]
        if not fv.optional or field not in entity_type.inherited_field_names:
          entity_type.inherited_field_names[field] = fv

    # Mark entity as expanded
    entity_type.inherited_fields_expanded = True
    on_stack.remove(stack_key)
    # Return union of local and inherited fields
    return entity_type.GetAllFields()

  def _FindBadIncrements(self, type_namespaces_map):
    """Add errors if any types have incremented fields without duplicate bases.

    Fields should only have _# increments if not having them would cause there
    to be duplicate fields in the class.  This method validates that rule.

    Args:
      type_namespaces_map: a dict mapping namespace strings to
        TypeNamespace objects.

    Returns:
      True if all types validate.
    """
    is_clean = True
    for type_namespace in type_namespaces_map.values():
      for entity_type in type_namespace.valid_types_map.values():
        field_lookup = {}
        # Do union manually here as we still want to check types where a bad
        # config caused one or more parent types not to be found
        all_fields = entity_type.GetAllFields(True)
        for field in all_fields:
          field_tuple = all_fields[field].field
          namespace = field_tuple.namespace
          field_only = field_tuple.field

          if field_tuple.increment:
            key = '{0}/{1}'.format(namespace, field_only)
            if key in field_lookup:
              field_lookup[key] = None
            else:
              field_lookup[key] = field
          else:
            field_lookup[field] = None

        for key in field_lookup:
          if field_lookup[key] is not None:
            # Illegal increments are only warnings for autogenerated types.
            if base_lib.AUTOGENERATED_TYPES.intersection(
                entity_type.parent_names):
              entity_type.AddFinding(findings_lib.IllegalFieldIncrementWarning(
                  entity_type, field_lookup[key]))
            else:
              # Don't worry about adding this finding to the namespace.  It is a
              # short-circuiting error, making universe integrity irrelevant.
              self.AddFinding(findings_lib.IllegalFieldIncrementError(
                  entity_type, field_lookup[key]))
              is_clean = False

    return is_clean

  def _CheckDuplicateFieldSets(self, type_namespaces_map):
    """Warn if any types in type_namespaces_map declare the same set of fields.

    Records warning in class if either duplicate local field sets are found,
      or duplicate expanded field sets are found.

    Args:
      type_namespaces_map: a dict mapping namespace strings to
        TypeNamespace objects.
    """
    # Check for duplicate local field sets
    # Map local field sets from self.types_map to their entity types
    field_sets = {}
    for type_namespace in type_namespaces_map.values():
      for entity_type in type_namespace.valid_types_map.values():
        # convert list of fields into immutable tuple of fields, for hashing
        fields = frozenset(entity_type.local_field_names)
        if len(fields) < MIN_SIZE_FOR_LOCAL_FIELD_DUPES:
          continue

        mapped_type = field_sets.get(fields)
        # If a duplicate field set is encountered, or the field set is empty
        if mapped_type and fields:
          field_sets[fields].append(entity_type)
        elif fields:
          field_sets[fields] = [entity_type]
    for types in field_sets.values():
      if len(types) > 1:
        self._WarnDuplicateLocalFields(types)

  def _WarnDuplicateLocalFields(self, types):
    found_inheritance = False
    for et in types:
      if et.inherited_field_names:
        found_inheritance = True
        break
    if not found_inheritance:
      return

    i = 0
    type_len = len(types)
    while i < type_len:
      target = types.pop(0)
      target.AddFinding(findings_lib.DuplicateLocalFieldSetsWarning(
          target, types))
      types.append(target)
      i += 1
