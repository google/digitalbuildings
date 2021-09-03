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


from constants.dimension import Dimension
"""Base class for scoring individual dimensions"""


class Score:
    # TODO: annotate args so as not to get confused between set and individual entities
    def __init__(self, dimension: Dimension, proposed, solution):
        self.dimension = dimension
        self.solution_entity = None
        self.correct = None
        self.underconstrained = None
        self.overconstrained = None
        self.total_possible = None
        self.is_reporting = None
        self.is_canonical = None

    def calculate(self, incorrect) -> float:
        return (self.correct - incorrect) / self.total_possible

    def evaluate(self, proposed, solution):
        return '123'
