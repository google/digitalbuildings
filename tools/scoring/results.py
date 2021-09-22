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
from utils import path_sha1

from validate import handler as validator

from dimensions.field_selection import FieldSelection

from typing import Dict
from validate.entity_instance import EntityInstance


class Results:
  """ A full scoring report

  Args:
    ontology: Path to the ontology
    solution: Path to the solution config
    proposed: Path to the config to be scored
    additions: Path to type additions

  Props:
    args: Dictionary ocontaining the arguments
    started: UTC datetime for when the process began
    finished: UTC datetime for when the process ended
    meta: Program metadata for output
    parsed: Deserialized YAML inputs
    scores: Scores for output
  """

  def __init__(self,
               *,
               ontology: str = None,
               solution: str,
               proposed: str,
               additions: str = None):
    self.args = {
        'ontology': ontology,
        'proposed': proposed,
        'solution': solution,
        'additions': additions
    }

    self.started = timestamp()
    self.finished = None
    self.parsed = self._parsed()
    print('Started at ' + str(self.started))
    self.tally()

  def __del__(self):
    self.finished = timestamp()
    print('Finished at ' + str(self.finished))

  # FUNCTIONALITY

  def _parsed(self) -> Dict[str, Dict[str, EntityInstance]]:
    # parsed = {}
    # for path in [self.args['solution'], self.args['proposed']]:
    #   entities = validator.Deserialize([path])[0]
    #   parsed[path] = entities
    # return parsed
    return {
        'proposed': validator.Deserialize([self.args['proposed']])[0],
        'solution': validator.Deserialize([self.args['solution']])[0]
    }

  def tally(self):
    dimension = FieldSelection(
        proposed_set=self.parsed['proposed'],
        solution_set=self.parsed['solution'])
    dimension.evaluate()

  # EXTERNAL INTERFACE

  @property
  def meta(self) -> Dict:
    """ Dict for report output """
    return {
        'meta': {
            'timeline': {
                'started': self.started,
                'finished': self.finished
            },
            'files': self._files()
        }
    }

  def _files(self):
    """ Provide human-digestible way to quickly differentiate between inputs """
    files = {}
    for name, value in self.args.items():
      if value is None:
        files[name] = None
        continue
      elif name in ['proposed', 'solution']:
        path, sha1 = path_sha1.file(value)
      else:
        path, sha1 = path_sha1.directory(value)
      files[name] = {'path': path, 'sha1': sha1}
    return files

  @property
  def scores(self) -> Dict:
    """ Dict for report output """
    # 'scores': {
    #     # 'aggregate': float,
    #     'dimensions': {
    #         '...': {
    pass
