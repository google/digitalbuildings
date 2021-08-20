from datetime import datetime
from utils.timestamp import timestamp
from utils.hash import hash

class Score:
    def __init__(self, ontology: tuple, solution: tuple, proposed: tuple, additions: tuple) -> None:
        print(timestamp())
        print(hash(ontology))
        print(hash(solution))
        print(hash(proposed))
        print(hash(additions))

    def _calculate(correct: int, incorrect: int, total: int) -> float:
        return (correct - incorrect) / total

    def __del__(self) -> None: ## Probably want to use a context manager for this https://stackoverflow.com/questions/40536821/python-enter-exit-vs-init-or-new-del
        print(timestamp())

output = {
    'meta': {
        'timeline': {
            'started': datetime,
            'finished': datetime
        },
        'files': {
            'ontology': {
                'path': 'path',
                'hash': 'string' # Where to calc?
            },
            'solution': {},
            'proposed': {},
            'additions': {}
        },
        'flags': {
            'verbose': bool
        }
    },
    'scores': {
        # 'aggregate': float,
        'unit_mapping': {
            'solution': 'string',
            'correct': int,
            'underconstrained': int,
            'overconstrained': int,
            'total': float,
            'is_reporting': bool,
            'is_canonical': bool
        },
        'state_mapping': {},
        'field_selection': {},
        'field_naming': {},
        'entity': {
            'connection_id': {},
            'id': {},
            'point_id': {},
            'type_id': {}
        }
    }
}
