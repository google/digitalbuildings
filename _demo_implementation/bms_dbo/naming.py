"""FACILITIES entity code rules.

The DBO instance validator enforces a naming convention on building, floor and
room codes. It is easy to miss, because nothing in the ontology YAML mentions
it -- the patterns live in the validator's own source:

    tools/validators/instance_validator/validate/entity_instance.py

Reproduced here so a commissioning engineer finds out while naming the space,
not when the config reaches the cloud. Keep in step with upstream; the CI
gate that runs the real instance validator is what catches drift.
"""

from __future__ import annotations

import re

# --- component patterns, verbatim from entity_instance.py ------------------
MEZZANINE = r"([0-9]*)M"
SINGLE_LETTER = r"R|D|LG|FB|S|SBA|SBB"
PERMUTED_NUMBER_LETTER = r"B[0-9]*|[0-9]+B"  # basement levels
LETTER_NUMBER = r"(G|UG|M)[0-9]*"  # garage levels
NUMBERS = r"[0-9]+"

COUNTRY_ID = r"[A-Za-z]{2}"
CITY_ID = r"[A-Za-z]{2,4}"
BUILDING_ID = r"[A-Za-z0-9]{2,10}"
FLOOR_ID = f"{MEZZANINE}|{SINGLE_LETTER}|{PERMUTED_NUMBER_LETTER}|{LETTER_NUMBER}|{NUMBERS}"
ROOM_ID = r"([0-9A-Z]+)"

BUILDING_CODE_REGEX = f"^{COUNTRY_ID}-{CITY_ID}-{BUILDING_ID}$"
FLOOR_CODE_REGEX = f"^{COUNTRY_ID}-{CITY_ID}-{BUILDING_ID}-({FLOOR_ID})$"
ROOM_CODE_REGEX = (
    f"^{COUNTRY_ID}-{CITY_ID}-{BUILDING_ID}-({FLOOR_ID})-({ROOM_ID})$"
)

_PATTERNS = {
    "FACILITIES/BUILDING": re.compile(BUILDING_CODE_REGEX),
    "FACILITIES/FLOOR": re.compile(FLOOR_CODE_REGEX),
    "FACILITIES/ROOM": re.compile(ROOM_CODE_REGEX),
}

_EXPECTED = {
    "FACILITIES/BUILDING": "CC-CITY-BLDG, e.g. AU-MEL-DEMO",
    "FACILITIES/FLOOR": (
        "<building>-<floor>, where floor is a number (1), a garage or ground "
        "level (G, UG, M2), a basement (B1, 2B), a mezzanine (3M) or one of "
        "R/D/LG/FB/S/SBA/SBB -- e.g. AU-MEL-DEMO-1"
    ),
    "FACILITIES/ROOM": (
        "<floor>-<room>, room being digits and capitals only, "
        "e.g. AU-MEL-DEMO-1-101"
    ),
}


def check_code(code: str, entity_type: str) -> str | None:
    """Return a problem description, or None when *code* is acceptable.

    Types without a documented pattern (CORRIDOR, STAIRWELL, ...) return None
    rather than guessing.
    """
    pattern = _PATTERNS.get(entity_type)
    if pattern is None:
        return None
    if pattern.match(code):
        return None
    return (
        f"{code!r} does not follow the DBO {entity_type.split('/')[-1].lower()} "
        f"code convention: expected {_EXPECTED[entity_type]}"
    )
# AI:E87M claude-code 2026-08-27 s:2a846146
