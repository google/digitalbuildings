# Entity Point Identification

# For each entity we care that all of its points are identified successfully.  While applying a point to a reporting device should be trivial once the point is identified and named, it is more difficult for virtual devices, and therefore worth scoring.
#
# Procedurally, scoring is accomplished by first building a multi-mapping between solution devices or device groups (for virtual devices) and result devices.  Starting with the best possible match in the group, devices are scored and removed from the global set until all solution devices have been processed.
#  (number of correctly mapped fields) - (number of incorrect or extra fields) total fields in all devices

# Results can be viewed separately for reporting and virtual devices.

class PointId:
    def __init__(self):
        return False
