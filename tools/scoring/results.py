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
""" Top-level runner """

from utils.timestamp import timestamp
from utils import path_hash
from constants.dimension import Dimension

from validate import handler as validator


class Results:
  """Wraps full scoring report"""

  def __init__(self, proposed: str, solution: str, ontology: str,
               additions: str) -> None:
    started = timestamp()
    print("Started at " + str(started))

    # loop through args to aggregate files metadata

    # print(hash.file(proposed))
    print(path_hash.file(solution))
    # print(hash.directory(ontology))
    # print(hash.directory(additions))

    self.parsed = {
        solution: validator.Deserialize([solution]),
        proposed: validator.Deserialize([proposed]),
    }

  def _files(self):
    return "files"

  def __del__(self) -> None:  # Probably want to use a context manager for this
    finished = timestamp()
    print("Finished at " + str(finished))

  def tally(self):
    for dimension in Dimension:
      print(dimension.name)

  @property
  def meta(self):
    # 'meta': {
    #     'timeline': {
    #         'started': datetime,
    #         'finished': datetime
    #     },
    #     'files': {
    #         'ontology': {
    #             'path': 'path',
    #             'hash': 'string'
    #         },
    #         'solution': {},
    #         'proposed': {},
    #         'additions': {}
    #     },
    #     'flags': {
    #         'verbose': bool
    #     }
    # }
    return "meta"

  @property
  def scores(self):
    # 'scores': {
    #     # 'aggregate': float,
    #     'dimensions': {
    #         '...': {
    return "scores"
