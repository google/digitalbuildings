# Entities

# There are three aspects of entities that we're concerned with:

# What entities exist

# Were their points identified properly

# Was their type assigned accurately

# While success at each of these likely correlates with success at the other two.  For example,  it may be possible to infer that an entity should exist and be a certain type without being able to explicitly identify the points that map to it.  As a result, we'd like to score them all separately.

# Entity Identification

# List all the canonically typed devices that exist in the solution
#   Identify reporting devices by cloud_device_id
#   Identify virtual devices by parent devices
#       Note: there may be more than one device with each ancestry
#   For each solution device or group, identify result devices that have the same identifier
#   Allow only one mapping from the result for each device in the solution

# The score is:
#  (number of correctly paired devices) - (number of unpaired result devices) total devices

# Again, reporting and virtual device results should be separable

class EntityId():
    def __init__(self):
        return False
