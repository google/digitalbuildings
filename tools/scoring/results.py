from utils.timestamp import timestamp
from utils import hash
from constants.dimension import Dimension

from validate import handler as validator
"""Top-level runner"""


class Results:
    def __init__(self, proposed: str, solution: str, ontology: str,
                 additions: str) -> None:
        started = timestamp()
        print('Started at ' + str(started))

        # loop through args to aggregate files metadata

        # print(hash.file(proposed))
        print(hash.file(solution))
        # print(hash.directory(ontology))
        # print(hash.directory(additions))

        self.parsed = {
            solution: validator.Deserialize([solution]),
            proposed: validator.Deserialize([proposed])
        }

    def _files(self):
        return 'files'

    def __del__(
            self) -> None:  # Probably want to use a context manager for this
        finished = timestamp()
        print('Finished at ' + str(finished))

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
        return 'meta'

    @property
    def scores(self):
        # 'scores': {
        #     # 'aggregate': float,
        #     'dimensions': {
        #         '...': {
        return 'scores'
