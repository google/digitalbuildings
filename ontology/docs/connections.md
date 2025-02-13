# Connections

Connections are a type of relationship between two entities that describe 
the how the entities are associated. This may be a physical (e.g., `FEEDS`) 
or logical (e.g., `HAS_PART`) association. This document details the definitions
of the various supported connections and in what scenarios each should be used.
When onboarding virtual devices the connections should be made on the virtual
device and not on the gateway.

## Contains

#### Definition: Source physically encapsulates at least part of Target.

The Contains connection should be used when one entity, or at least a component of it,
exists physically within another. This connection is commonly used to represent the 
location of an entity within a building. For example, a building may contain a floor 
which contains a room or zone, which contains a `VAV`. In this instance the connection
between the building and room should be set on the room and the connection between the 
room and `VAV` should be set on the `VAV` as follows:

``` yaml
ROOM-GUID: 
  code: Room 123
  connections:
    BUILDING-GUID:
    - CONTAINS
```
``` yaml
VAV-GUID: 
  code: VAV 1-2
  connections:
    ROOM-GUID:
    - CONTAINS
```

## Controls

#### Definition: Source determines or affects the internal state or behavior of Target.

The Controls connection should be used when one entity impacts the behavior of another.
An example of when this connection may be used would be where a lighting control 
module, `LCM`, controls one or more luminaires, `LT`. In this example the connection should
be set on the `LT` entity as follows:

``` yaml
LT-GUID: 
  code: LT 123
  connections:
    LCM-GUID:
    - CONTROLS
```

The target entity of a Controls connection must be one that performs an action. This
excludes `FACILITIES` entities.

## Feeds

#### Definition: Source provides some media (ex: water or air) to Target.

The Feeds connection should be used when one entity is located pysically upstream of 
another in regards to its media, so that one device supplies the media to the other.
A very common use case for this connections is when an `AHU` feeds air to a `VAV`.
In this example the connection should be set on the `VAV` entity as follows:

``` yaml
VAV-GUID: 
  code: VAV 1-2
  connections:
    AHU-GUID:
    - FEEDS
```

Feeds connections source entities must be devices that provide a medium. These devices
will typically be in the `HVAC` or `PLUMBING` namespaces. The target entity can be 
another device or can be a `FACILITIES` entity.

## Has Part

#### Definition: Source has some component or part defined by Target.

The Has Part connection should be used to represent which system a component belongs to.
This can be used to represent something like a pump, `PMP`, that belongs to a chilled 
water system, `CHWS`. In this example the connection should be set on the `PMP` entity as follows:

``` yaml
PMP-GUID: 
  code: PMP 1
  connections:
    CHWS-GUID:
    - HAS_PART
```

## Has Range

#### Definition: Source has a coverage or detection range defined by Target.

The has range connection should be used when the limitations of one entity are defined by another.
This could be used to describe something like an occupancy sensor, `SENSOR_ZOC`, that would have
a has range connection to a room, as the sensor can only measure the occupancy within the 
boundaries of said room. In this example the connection should be set on the room entity as follows:

``` yaml
ROOM-GUID: 
  code: Room 123
  connections:
    SENSOR-ZOC-GUID:
    - HAS_RANGE
```

The source entity for the Has Range connection must be a device that performs detection.
This typically includes `SENSORS`.

## Measures

#### Definition: Source quantifies attributes of the Target.

The measures connection should be used to decribe when an entity ascertains the 
quantity or value of another's attributes. One common example would be a meter that measures a 
[load type](https://github.com/google/digitalbuildings/blob/master/ontology/yaml/resources/METERS/entity_types/LOADTYPES.yaml).
In these instances the connection should be set on the `LOADTYPE` entity as follows:

``` yaml
LOADTYPE-GUID: 
  code: Loadtype HVAC
  connections:
    METER-GUID:
    - MEASURES
```

The source entity for the Measures connection must be a device that performs quantification.
This typically includes `METERS`.
