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
""" Generate hashes for readily differentiating between inputs """

from filehash import FileHash
from dirhash import dirhash


def directory(path: str) -> tuple:
  """Generates a hash for quickly comparing directories.

  Returns:
      A tuple containing the input string and the hash/checksum as
      a string of hexadecimal digits
  """

  return (path, dirhash(path, "sha1", ignore=[".*", ".*/"]))


def file(path: str) -> tuple:
  """Generates a hash for quickly comparing files.

  Returns:
      A tuple containing the input string and the hash/checksum as
      a string of hexadecimal digits
  """

  return (path, FileHash("sha1").hash_file(path))
