# Meter Load Designation

Digital Buildings provides abstract models that can be used to represent various types of loads within a building and can be connected to meter entities to indicate the types of loads measured by each metering device. This document describes how these loadtypes should be created and connected within a building configuration file.

*   For an explanation of building configuration files see [building_config](building_config.md)

### Create the Building Entity and Meter Device Entity

Use the syntax described in [building_config](building_config.md) to create a facility entity for the building and a reporting entity for the meter device. A `CONTAINS` connection should be used to indicate that the meter exists within the building.

### Create an Abstract Loadtype Entity

Create a loadtype entity to represent each of the types of loads the meters in the building measure. The entity will consist of a single abstract loadtype found in the file called `LOADTYPES.yaml` in the `METER` namespace. The abstract loadtype does not implement any fields. A `CONTAINS` connection should be used to indicate that the load exists within the building.

### Connect the Loadtype Entity to the Meter Entity via a `MEASURES` Connection

Add a `MEASURES` connection to the loadtype entity to indicate which meter(s) provide data for it. A building may have multiple meters that measure the same loadtype.

## Example Building Layout and Config

Example full building-loadtype-meter layout:

![image](https://github.com/shambergoldstein/digitalbuildings/assets/124837286/427e4c03-c132-468c-94e7-20486117643a)

Example building-loadtype-meter connection in building configuration file:
``` yaml
# The building
ccb-342:
  code: BLDG-123
  type: FACILITIES/BUILDING

# The abstract entity for MAIN load
abc-123:
  code: MAIN
  type: METERS/LOADTYPE_MAIN
  connections:
    ccb-342: CONTAINS
    dde-453: MEASURES

# The reporting entity for the meter
dde-453:
  code: EM-1
  cloud_device_id: 1234
  type: METERS/EM_PWM
  connections:
    ccb-342: CONTAINS
  translation:
    power_sensor:
      present_value: points.kW.present_value
      units:
        key: pointset.points.kW.units
        values:
          kilowatts: "kW"
```
