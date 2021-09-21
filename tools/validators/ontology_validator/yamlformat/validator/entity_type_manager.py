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
"""Code to dentify type hierarchy and naming suggestions in config files.

The classes here help to keep the ontology clean by highlighting places where
naming or type inheritance could be improved.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import itertools

from yamlformat.validator import base_lib
from yamlformat.validator import findings_lib

# Smallest set of fieldset we consider for automated matching. Must be >=1
MIN_SET_SIZE = 1
# Max allowed number of required fields difference between two types in an
# incomplete flex type warning
MAX_FIELDS_FOR_INCOMPLETE = 3
# Max number of types to include in a processing group
# number must be small enough such that the combinations of type pairs with a
# single field must never overrun the system memory.  <20 is probably safe
# 2019-10-03: For the current data, brute force (size=1) is empirically fastest.
MAX_TYPE_SHARD_SIZE = 1


def _CreateOptionalityInsensitiveCopy(sets_to_types):
  """Makes Optionality-insensitive copy of the passed dict and returns it."""
  oi_sets_to_types = collections.defaultdict(set)
  for key in sets_to_types:
    new_key = frozenset([field.field for field in key])
    oi_sets_to_types[new_key].update(sets_to_types[key])
  return oi_sets_to_types


def _CleanMap(typenames_by_subset, complete_field_sets):
  """Removes values that are whole types and keys with too-small sets."""
  group_too_small = set()
  for subset in typenames_by_subset:
    if len(typenames_by_subset[subset]) < 2:
      group_too_small.add(subset)
      continue
    whole_types = complete_field_sets.get(subset, set())
    to_remove = set()
    for entity_type in typenames_by_subset[subset]:
      if entity_type in whole_types:
        to_remove.add(entity_type)
    typenames_by_subset[subset].difference_update(to_remove)
    if not typenames_by_subset[subset]:
      group_too_small.add(subset)
  for subset in group_too_small:
    del typenames_by_subset[subset]


class EntityTypeManager(findings_lib.Findings):
  """Implements advanced management of EntityType construction.

  Method expects types in passed universe to have inherited_fields_expanded.

  Args:
    entity_type_universe: ConfigUniverse to evaluate
  """

  def __init__(self, entity_type_universe):
    super(EntityTypeManager, self).__init__()
    self._universe = entity_type_universe
    self._complete_field_sets_oi = None  # OI = optionality insensitive
    self._typenames_by_subset_oi = None  # OI = optionality insensitive
    self._new_parents = 0

  def Analyze(self):
    """Performs analysis on the universe to suggest parentage and naming.

    Thoughts about how to improve:
    - group all results for a type together in the results

        (this will happen automatically when we pull findings from universe)
    - score results by some function of number of fields and number of matches
    - score full type matches above all, sort by num fields? Maybe not best
        because sometimes you want two smaller types as parents?
    - filter for best X matches
    - canonical types can only inherit from canonical types
    - only inherit from canonical types?
    - prefer new inheriting from old?
    - what types of old type matches do we not filter?

    Returns:
      A list of the findings added to the universe.  This should generally only
      be used for debugging.
    """
    self._complete_field_sets_oi = {}
    self._typenames_by_subset_oi = {}

    findings = []
    self._MapFields(MIN_SET_SIZE)

    findings.extend(self._FindDuplicates())
    findings.extend(self._FindFlexibleParents())

    return findings

  def _FindFlexibleParents(self):
    """Finds smaller types that can be represented by larger, flexible types."""
    findings = []
    for subset in self._complete_field_sets_oi:
      parent_rollup = {}
      # used by the commented code below, reduce the verbosity of warnings.
      # incomplete_parent_rollup = {}
      # Check each complete type for partial types having same fields
      possible_parents = self._typenames_by_subset_oi.get(subset, None)
      if not possible_parents:
        continue

      # Loop through every complete type to find possible parents
      typenames = self._complete_field_sets_oi[subset]
      for typename in typenames:
        # Skip any types that look like they've already been triaged
        entity_type = self._GetTypeByName(typename)
        if base_lib.HasDeprecatedType(entity_type.parent_names):
          continue
        if (len(entity_type.parent_names) == 1 and
            not entity_type.local_field_names):
          continue

        matching_parents = {}
        incomplete_parent_matches = {}
        best_diff = 1000000
        best_incomplete_diff = 1000000
        best_incomplete_diff_opt = 1000000
        entity_type_fields = set(entity_type.GetAllFields().keys())
        # get difference set of entity_type and each parent with this subset
        # check that every remaining field is optional.
        # Each loop tests one possible pairing
        # Goal is to find best type for each device, which tyically means device
        # with smallest diff
        t_match = base_lib.GetEquipmentClass(typename)
        for parent in possible_parents:
          if parent in typenames:
            continue
          parent_entity = self._GetTypeByName(parent)
          # only suggest canonical parents
          if not parent_entity.is_canonical:
            continue

          # Right now only match things with the same equipment classes
          p_match = base_lib.GetEquipmentClass(parent)
          if not (p_match and t_match and (p_match == t_match)):
            continue

          parent_fields = set(parent_entity.GetAllFields().keys())
          subset_fields = parent_fields.intersection(entity_type_fields)
          diff = parent_fields.difference(entity_type_fields)

          # skip anything where the diff is 0 because it will be handled by
          # duplicate type. this may not ever happen because complete types
          # should be stripped out of the map
          if not diff:
            continue

          # Validate that common fields are compatible
          optionality_compatible = True
          optionality_changes = 0
          for field in subset_fields:
            parent_field = parent_entity.GetAllFields()[field]
            child_field = entity_type.GetAllFields()[field]
            if not parent_field.optional and child_field.optional:
              optionality_compatible = False
            if parent_field != child_field:
              optionality_changes += 1
          if not optionality_compatible:
            continue

          is_match = True
          is_optional = False
          missing_required_fields = []
          for field in diff:
            wrapped_field = parent_entity.GetAllFields()[field]
            if not wrapped_field.optional:
              is_match = False
              if (not parent_entity.is_canonical or parent_entity.is_abstract or
                  base_lib.HasDeprecatedType(parent_entity.parent_names)):
                break
              missing_required_fields.append(field)
            else:
              is_optional = True

          if is_match:
            if not matching_parents or len(diff) <= best_diff:
              if len(diff) < best_diff:
                matching_parents = {}
              matching_parents[parent] = diff
              best_diff = len(diff)
          elif missing_required_fields and is_optional:
            if len(missing_required_fields) > MAX_FIELDS_FOR_INCOMPLETE:
              continue
            if not incomplete_parent_matches or len(
                missing_required_fields) <= best_incomplete_diff:
              opt_diff = len(diff) - len(
                  missing_required_fields) + optionality_changes
              if len(missing_required_fields) < best_incomplete_diff:
                incomplete_parent_matches = {}
              else:
                if (best_incomplete_diff_opt is not None and
                    best_incomplete_diff_opt > opt_diff):
                  incomplete_parent_matches = {}
                elif (best_incomplete_diff_opt is not None and
                      best_incomplete_diff_opt < opt_diff):
                  continue

              incomplete_parent_matches[parent] = missing_required_fields
              best_incomplete_diff = len(missing_required_fields)
              best_incomplete_diff_opt = opt_diff

        if matching_parents:
          finding = findings_lib.OverlappingFlexTypeChildWarning(
              entity_type, best_diff, matching_parents)
          entity_type.AddFinding(finding)
          findings.append(finding)

          for parent in matching_parents:
            parent_rollup[parent] = {typename: matching_parents[parent]}

# This is commented to reduce the verbosity of warnings for the user.
# To uncomment, remove the comments in bulk using a shortcut key map in your
# favorite editor.
#         if incomplete_parent_matches:
#           finding = findings_lib.PossibleOverlappingFlexTypeChildWarning(
#               entity_type, best_incomplete_diff, incomplete_parent_matches)
#           entity_type.AddFinding(finding)
#           findings.append(finding)

#           for parent in incomplete_parent_matches:
#             incomplete_parent_rollup[parent] = {
#                 typename: incomplete_parent_matches[parent]}

#       for parent in incomplete_parent_rollup:
#         entity_type = self._GetTypeByName(parent)
#         finding = findings_lib.PossibleOverlappingFlexTypeParentWarning(
#             entity_type, incomplete_parent_rollup[parent])
#         entity_type.AddFinding(finding)
#         findings.append(finding)

      for parent in parent_rollup:
        parent_type = self._GetTypeByName(parent)
        finding = findings_lib.OverlappingFlexTypeParentWarning(
            parent_type, parent_rollup[parent])
        parent_type.AddFinding(finding)
        findings.append(finding)

    return findings

  def _FindDuplicates(self):
    """Identifies types that have identical field sets."""
    findings = []
    for subset in self._complete_field_sets_oi:
      if not subset:
        continue
      typenames = self._complete_field_sets_oi[subset]
      if len(typenames) < 2:
        continue

      for typename in typenames:
        entity_type = self._GetTypeByName(typename)

        # Filter duplicates where the two types inherit from one another
        other_typenames = typenames.difference([typename])
        not_related = {}
        qparents_by_child = {}
        for other_name in other_typenames:
          if other_name not in qparents_by_child:
            other_type = self._GetTypeByName(other_name)
            qparents_by_child[other_name] = other_type.parent_names
          if (typename not in qparents_by_child[other_name] and
              other_name not in entity_type.parent_names):

            optionality_compatible = True
            optionality_changes = 0
            for field in entity_type.GetAllFields():
              parent_field = entity_type.GetAllFields()[field]
              other_field = other_type.GetAllFields()[field]
              if not parent_field.optional and other_field.optional:
                optionality_compatible = False
                break
              if parent_field != other_field:
                optionality_changes += 1
            if not optionality_compatible:
              continue
            not_related[other_name] = optionality_changes

        if not not_related:
          continue
        key_list = list(not_related.keys())
        key_list.append(typename)
        finding = findings_lib.DuplicateExpandedFieldSetsWarning(
            entity_type, not_related, frozenset(key_list))
        entity_type.AddFinding(finding)
        findings.append(finding)
    return findings

  def _GetTypeByName(self, qualified_name):
    split = qualified_name.split('/')
    return self._universe.GetEntityType(split[0], split[1])

  def _GetNamespaceForName(self, qualified_name):
    split = qualified_name.split('/')
    return self._universe.GetNamespace(split[0])

  def _MapFields(self, min_set_size):
    """Executes unique common subsets detection.

    Identifies all the unique field subsets of at least min_set_size that have
    at least 2 associated types. As a side effect this also creates
    a map of all the field sets for complete types. Both optionality sensitive
    and optionality insensitive version of the maps are created.

    Args:
      min_set_size: minimum number of fields a subset must have to be included
    """
    current_shard = set()
    type_shards = []
    type_shards.append(current_shard)
    complete_field_sets_output = {}
    typenames_by_subset_output = {}
    # Map each individual field to the types that have that field
    # In the process also define groups of types to shard
    field_to_typenames = {}
    for namespace in self._universe.GetNamespaces():
      ns_name = namespace.namespace
      for entity_type in namespace.valid_types_map.values():
        if base_lib.HasAutogeneratedType(
            entity_type.parent_names) or entity_type.is_abstract:
          continue
        full_qual_type = '{0}/{1}'.format(ns_name, entity_type.typename)

        # Sharding list calculation
        if len(current_shard) >= MAX_TYPE_SHARD_SIZE:
          current_shard = set()
          type_shards.append(current_shard)
        current_shard.add(full_qual_type)

        all_qualified_fields = frozenset(
            [et.field for et in entity_type.GetAllFields().values()])

        for full_qual_field in all_qualified_fields:
          if full_qual_field not in field_to_typenames:
            field_to_typenames[full_qual_field] = set()
          field_to_typenames[full_qual_field].add(full_qual_type)

        # Add type to mapping of full type field sets.
        if all_qualified_fields not in complete_field_sets_output:
          complete_field_sets_output[all_qualified_fields] = set()
        complete_field_sets_output[all_qualified_fields].add(full_qual_type)

    # Evaluate the sets in each shard and merge them
    for shard in type_shards:
      typenames_by_subset = self._MapTypenamesBySubset(shard,
                                                       field_to_typenames,
                                                       min_set_size)

      # Check each new subset against the existing master subsets
      # NB: All subsets should initially be large enough
      new_subsets = {}
      for subset in typenames_by_subset:
        if subset not in typenames_by_subset_output:
          if subset not in new_subsets:
            new_subsets[subset] = set()
          new_subsets[subset].update(typenames_by_subset[subset])

        for master_subset in typenames_by_subset_output:
          # Add new Types to master group for any identical field subsets
          if subset == master_subset:
            typenames_by_subset_output[master_subset].update(
                typenames_by_subset[subset])
            continue

          # Find the common fields from the two field sets
          new_subset = frozenset(subset.intersection(master_subset))
          # if new set of fields is big enough, save for addition to master list
          if len(new_subset) >= min_set_size:
            combined_typenames = typenames_by_subset[subset].union(
                typenames_by_subset_output[master_subset])
            if new_subset not in typenames_by_subset_output:
              if new_subset not in new_subsets:
                new_subsets[new_subset] = set()
              new_subsets[new_subset].update(combined_typenames)
              continue
            typenames_by_subset_output[new_subset].update(combined_typenames)

      # Add any new subsets that were created
      for new_subset in new_subsets:
        typenames_by_subset_output[new_subset] = new_subsets[new_subset]

    self._typenames_by_subset_oi = typenames_by_subset_output
    self._complete_field_sets_oi = complete_field_sets_output
    _CleanMap(self._typenames_by_subset_oi, self._complete_field_sets_oi)

  def _MapTypenamesBySubset(self, types_to_include, field_to_typenames,
                            min_set_size):
    """Creates a map of type sets keyed by unique fields sets."""

    subsets_by_typegroup = {}
    for field in field_to_typenames:
      types_with_field = field_to_typenames[field].intersection(
          types_to_include)
      i = 1
      stable_types_with_field = list(types_with_field)
      while i <= len(stable_types_with_field):
        groups = itertools.combinations(stable_types_with_field, i)
        for group in groups:
          typegroup = frozenset(group)
          if typegroup not in subsets_by_typegroup:
            subsets_by_typegroup[typegroup] = set()
          subsets_by_typegroup[typegroup].add(field)
        i += 1

    # at the end of the above, it's possible to get multiple type groups with
    # the same field sets.  We merge them below to get one group of types mapped
    # to each unique set of fields
    # Reverse the mapping to find unique subsets and their associated types
    typenames_by_subset = {}
    for typegroup in subsets_by_typegroup:
      fields = subsets_by_typegroup[typegroup]
      if len(fields) < min_set_size:
        continue
      field_set = frozenset(fields)
      if field_set not in typenames_by_subset:
        typenames_by_subset[field_set] = set()
      typenames_by_subset[field_set].update(typegroup)

    return typenames_by_subset


  def GetCompleteFieldSetsOI(self) -> dict():
    """Returns a mapping of complete field sets to EntityType strings"""
    #NOTE:This is a temporary implementation meant for development
    #TODO:Refactor underlying logic to expose field set to entity type maps
    if self._complete_field_sets_oi is None:
      raise Exception('Run Analyze() to access this mapping')
    return self._complete_field_sets_oi

  def GetTypenamesBySubsetOI(self) -> dict():
    """Returns a mapping of field subsets to EntityType strings"""
    #NOTE:This is a temporary implementation meant for development
    #TODO:Refactor underlying logic to expose field subset to entity type maps
    if self._typenames_by_subset_oi is None:
      raise Exception('Run Analyze() to access this mapping')
    return self._typenames_by_subset_oi
