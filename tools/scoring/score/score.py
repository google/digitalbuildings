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
