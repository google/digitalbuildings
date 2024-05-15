# Meter Load Designation

Digital Buidlings provides abstract models that can be used to represent various 
types of loads within a building and can be connected to meter entities to indicate the types
of loads measured by each metering device. This document describes how these loadtypes 
should be created and connected within a building configuration file.

*   For an explanation of building configuration files see
    [building_config](building_config.md)

- [Meter Load Designation](#meter-load-designation)
  * [Create the Building Entity and Meter Device Entity](#create-the-building-entity-and-a-meter-device-entity)
  * [Create an Abstract Loadtype Entity](#create-an-abstract-loadtype-entity)
  * [Connect the Meter Entity to the Loadtype Entity via a `MEASURES` Connection](#connect-the-meter-entity-to-the-loadtype-entity-via-a-measures-connection)
    
### Create the Building Entity and Meter Device Entity

Use the syntax described in [building_config](building_config.md) to create a
facility entity for the building and a reporting entity for the meter device.
A `CONTAINS` connection should be used to indicate that the meter exists within
the building.

Example building and meter entities:
``` yaml
# The building
ccb-342:
  code: US-SVL-BORD1212
  type: FACILITIES/BUILDING    

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

## Create an Abstract Loadtype Entity

Create a loadtype entity to represent each of the types of loads the meters in 
the building measure. The entity will consist of a single abstract loadtype 
found in the file called `LOADTYPES.yaml` in the `METER` namespace. The abstract
loadtype does not implement any fields. A `CONTAINS` connection should be used 
to indicate that the load exists within the building.

Example loadtype entity:
``` yaml
# The abstract entity for MAIN load
abc-123:
  code: MAIN
  type: METERS/LOADTYPE_MAIN
  connections:
    ccb-342: CONTAINS
```

## Connect the Meter Entity to the Loadtype Entity via a `MEASURES` Connection

Add a `MEASURES` connection to the meter entity to indicate which loadtype 
the meter provides data for. A building may have multiple meters that 
measure the same loadtype.

Example `MEASURES` connection:
``` yaml  
# The updated reporting entity for the meter
dde-453:
  code: EM-1
  cloud_device_id: 1234
  type: METERS/EM_PWM
  connections:
    ccb-342: CONTAINS
    abc-123: MEASURES
  translation:
    power_sensor:
      present_value: points.kW.present_value
      units:
        key: pointset.points.kW.units
        values: 
          kilowatts: "kW"
```
