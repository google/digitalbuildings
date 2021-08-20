from datetime import datetime, time

class Score:
    def __init__(self, timestamp: datetime, ontology: str, solution: str, proposed: str, additions: str) -> None:
        print(timestamp, ontology, solution, proposed, additions)

    def _calculate(correct: int, incorrect: int, total: int) -> float:
        return (correct - incorrect) / total
