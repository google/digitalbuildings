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
"""Checks for spelling mistakes in ontology yaml files."""

# pylint: disable=g-importing-member, bare-except
import os
from pathlib import Path
from textblob import TextBlob
import yaml


def process_file(path: str) -> None:
  """Processes a yaml file and checks for spelling mistakes.

  Prints spelling mistakes to console.

  Args:
      path: Path to yaml file.
  """
  if os.path.splitext(path)[1] != ".yaml":
    return
  try:
    structure = yaml.safe_load(Path(path).read_text())
  except:
    print("[WARN] Failed to load file %s.")
    return
  for key in structure.keys():
    value = structure[key]
    if isinstance(value, dict):
      continue
    if "description" not in value:
      continue
    description = value["description"]
    text_blob = TextBlob(description)
    corrected = text_blob.correct()
    if corrected != description:
      print("[CORRECTIONS] in file %s at key %s" % (path, key))
      print("  Did you mean '%s' instead of '%s'" % (description, corrected))


def process_directory(path: str) -> None:
  """Recursively processes a directory of yaml files.

  Args:
      path: Path to a directory of yaml files.
  """
  children = os.listdir(path)
  for child in children:
    full_child = path + os.sep + child
    if os.path.isdir(full_child):
      process_directory(full_child)
    else:
      process_file(full_child)


process_directory("ontology/yaml")
