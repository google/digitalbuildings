from enum import Enum, auto, unique
"""Criteria upon which proposed solutions are scored."""


@unique
class Dimension(Enum):
    UNIT_MAPPING = auto()
    STATE_MAPPING = auto()
    FIELD_SELECTION = auto()
    FIELD_NAMING = auto()
    ENTITY = Enum('entity', ['CONNECTION_ID', 'ID' 'POINT_ID' 'TYPE_ID'])

    def __str__(self):
        return self.value.lower()
