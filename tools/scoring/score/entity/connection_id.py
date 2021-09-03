# Entity Connection Identification

# Connections are scored on targets (because this is where they are defined).

# Connections can be scored:

#  (correctly defined connections) - (incorrectly defined connections) total connections

# In addition to overall score, sub-scored should be available for connections where the source is another piece of equipment vs. a Facilities entity (building/floor).

from score.score import Score


class ConnectionId(Score):
    def __init__(self):
        return False
