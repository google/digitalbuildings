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

from filehash import FileHash
from dirhash import dirhash

from typing import Tuple


def directory(path: str) -> Tuple[str, str]:
  """Generates a SHA1 hash for quickly comparing directories.

  Args:
    path: the fully qualified path

  Returns:
    Input string
    Hash/checksum string
  """

  return (path, dirhash(path, "sha1", ignore=[".*", ".*/"]))


def file(path: str) -> Tuple[str, str]:
  """Generates a SHA1 hash for quickly comparing files.

  Args:
    path: the fully qualified path

  Returns:
    Input string
    Hash/checksum string
  """

  return (path, FileHash("sha1").hash_file(path))
