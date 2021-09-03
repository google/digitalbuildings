# Entity Type Identification

# Field identification is a rough proxy for type identification because once a user identifies a sufficiently large set of required fields, the number of applicable types is likely to be very small.  There may be cases type identification itself is interesting, however:

# When a device is missing one or more fields, particularly required ones, or the application is unable to identify them successfully

# When the application's field filtering does not eliminate all unimportant fields

# When two distinct types overlapping valid field sets.

# In either of these cases it may be possible for an application to identify a type correctly without having a correct field set or have to select the correct type in addition to finding the correct field set.

# In addition to the above, it may be possible for the application to identify a type that is less specific than the ideal type.  Ex: VAV vs VAV_SD_DSP.

# By relaxing some of the building_config validation requirements, it is possible for participants to select types independently of the fields of a device.

# Type selection can be scored by the number of abstract types that the selected type has in common with the correct type.  The mapping of solution device to result device should be the same as for entity points.  Specifically, scoring would be:
#  (direct parent types matching correct type's parents) - (direct parent types not matching correct type's parents) total parent types

# As with fields, exact matches should also be counted separately and types assigned to virtual devices counted separately from reporting devices.  It may be interesting to be able to see the median device score as well as the overall score for the building.

from score.score import Score


class TypeId(Score):
    def __init__(self):
        return False
