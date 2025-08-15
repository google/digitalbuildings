# Modeling Meter Systems

## Meter Load Designation

Digital Buildings provides abstract models that can be used to represent various types of loads within a building and can be connected to meter entities to indicate the types of loads measured by each metering device. This section describes how these loadtypes should be created and connected within a building configuration file.

*   For an explanation of building configuration files see [building_config](building_config.md)

### Create the Building Entity and Meter Device Entity

Use the syntax described in [building_config](building_config.md) to create a facility entity for the building and a reporting entity for the meter device. A `CONTAINS` connection should be used to indicate that the meter exists within the building.

### Create an Abstract Loadtype Entity

Create a loadtype entity to represent each of the types of loads the meters in the building measure. The entity will consist of a single abstract loadtype found in the file called `LOADTYPES.yaml` in the `METER` namespace. The abstract loadtype does not implement any fields. A `CONTAINS` connection should be used to indicate that the load exists within the building.

### Connect the Loadtype Entity to the Meter Entity via a `MEASURES_TYPE` Connection

Add a `MEASURES_TYPE` connection to the loadtype entity to indicate which meter(s) provide data for it. A building may have multiple meters that measure the same loadtype.

## Example Building Layout and Config

Example full building-loadtype-meter layout:

<img width="1996" height="1034" alt="image" src="https://github.com/user-attachments/assets/936cb3b3-c304-477f-88af-004fc289876e" />

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
    dde-453: MEASURES_TYPE

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

## Meter System Modelling

### Full System (Electrical Infrastructure Included)

Metering systems can be modeled with electrical infrastructure and load designation to provide a complete picture of the system as it physically exists. This section describes how all involved entities should be created and connected within a building configuration file.

#### Create the Building Entity, Meter Device Entities, Electrical Infrastructure Entities (Panels/Breakers/Equipment/etc), and Load Types

Use the syntax described in [building_config](building_config.md) to create a facility entity for the building and a reporting entity for the meter device. A `CONTAINS` connection should be used to indicate that the meter exists within the building. Create entities to represent the electrical infrastructure and abstract entities to represent load types.

#### Connect Electrical Infrastructure using `FEEDS` Connections

Please see the [connections documentation](connections.md) for a description of this connection type.

#### Connect the Loadtype Entities to the Meter Entities using a `MEASURES_TYPE` Connection and Electrical Infrastructure to the Meter Entities via `MEASURES` Connection

Add a `MEASURES_TYPE` connection to each loadtype entity as described above and a `MEASURES` connection to each entity representing the electrical infrastructure to indicate which meter(s) provides data for them. If a component if the electrical infrastructure is not measured by any meters then this connection can be omitted.

#### Connect the Meter Entities to each other with either a `PARTIALLY_AGGREGATES` or a `FULLY_AGGREGATES` Connection

Please see the [connections documentation](connections.md) for a description of these connection types and when to use each.

#### Example Building Layout and Config

Example full building-loadtype-meter-electrical-infrastructure layout:

<img width="2239" height="1410" alt="image" src="https://github.com/user-attachments/assets/f2796dd5-bd59-4bc2-8090-b784b1548b36" />

Example building-loadtype-meter-electrical-infrastructure connection in building configuration file:
``` yaml
# Building
bldg:
  code: BLDG-123
  type: FACILITIES/BUILDING

# Electrical / HVAC Equipment

msb:
  code: MSB
  type: ELECTRICAL/MSB
  connections:
    m_main: MEASURES
    bldg: CONTAINS

t1c:
  code: T1C
  type: ELECTRICAL/PANEL
  connections:
    msb: FEEDS
    m_tc1: MEASURES
    bldg: CONTAINS

1dlc:
  code: 1DLC
  type: ELECTRICAL/PANEL
  connections:
    t1c: FEEDS
    bldg: CONTAINS

4ha1:
  code: 4HA1
  type: ELECTRICAL/PANEL
  connections:
    msb: FEEDS
    m_4ha1: MEASURES
    bldg: CONTAINS

lcp1:
  code: LCP1
  type: ELECTRICAL/MSB
  connections:
    4ha1: FEEDS
    bldg: CONTAINS

ahu1:
  code: AHU-1
  type: HVAC/AHU
  connections:
    4ha1: FEEDS
    m_ahu1: MEASURES
    bldg: CONTAINS

ahu2:
  code: AHU-2
  type: HVAC/AHU
  connections:
    4ha1: FEEDS
    m_ahu2: MEASURES
    bldg: CONTAINS

ahu3:
  code: AHU-3
  type: HVAC/AHU
  connections:
    4ha1: FEEDS
    m_ahu3: MEASURES
    bldg: CONTAINS

# Meters

m_main:
  code: M_MAIN
  type: METERS/EM
  connections:
    bldg: CONTAINS

m_tc1:
  code: M_TC1
  type: METERS/EM
  connections:
    m_main: FULLY_AGGREGATES
    bldg: CONTAINS

m_4ha1:
  code: M_4HA1
  type: METERS/EM
  connections:
    m_main: FULLY_AGGREGATES
    bldg: CONTAINS

m_ahu1:
  code: M_AHU-1
  type: METERS/EM
  connections:
    m_4ha1: PARTIALLY_AGGREGATES
    bldg: CONTAINS

m_ahu2:
  code: AHU-2
  type: METERS/EM
  connections:
    m_4ha1: PARTIALLY_AGGREGATES
    bldg: CONTAINS

m_ahu3:
  code: AHU-3
  type: METERS/EM
  connections:
    m_4ha1: PARTIALLY_AGGREGATES
    bldg: CONTAINS

# Loadtypes

hvac:
  code: HVAC
  type: METERS/LOADTYPE
  connections:
    m_ahu1: MEASURES_TYPE
    m_ahu2: MEASURES_TYPE
    m_ahu3: MEASURES_TYPE
    bldg: CONTAINS

main:
  code: MAIN
  type: METERS/LOADTYPE
  connections:
    m_main: MEASURES_TYPE
    bldg: CONTAINS

plug:
  code: PLUG
  type: METERS/LOADTYPE
  connections:
    m_tc1: MEASURES_TYPE
    bldg: CONTAINS

```
### Metering System Only (Electrical Infrastructure not Included)

Often, the explicit modeling of the electrical system is outside an MSI’s base scope, and so will not be modeled. Given an understanding of the metering infrastructure and the electrical system, a simplified version of the same model can be generated without any electrical system. This section describes how all involved entities should be created and connected within a building configuration file.

#### Create the Building Entity, Meter Device Entities, and Load Types

Use the syntax described in [building_config](building_config.md) to create a facility entity for the building and a reporting entity for the meter device. A `CONTAINS` connection should be used to indicate that the meter exists within the building. Create abstract entities to represent load types.

#### Connect the Loadtype Entities to the Meter Entities via `MEASURES_TYPE` Connections

Add a `MEASURES_TYPE` connection to each loadtype entity to indicate which meter(s) provides data for them.

#### Connect the Meter Entities to each other with either a `PARTIALLY_AGGREGATES` or a `FULLY_AGGREGATES` Connection

Please see the [connections documentation](connections.md) for a description of these connection types and when to use each.

#### Example Building Layout and Config

Example full building-loadtype-meter layout:

<img width="1955" height="1485" alt="image" src="https://github.com/user-attachments/assets/09d0f7c9-5a10-4e4a-982a-871a0f852937" />

Example building-loadtype-meter connection in building configuration file:

``` yaml
# Building
bldg:
  code: BLDG-123
  type: FACILITIES/BUILDING

# Meters

m_main:
  code: M_MAIN
  type: METERS/EM
  connections:
    bldg: CONTAINS

m_tc1:
  code: M_TC1
  type: METERS/EM
  connections:
    m_main: FULLY_AGGREGATES
    bldg: CONTAINS

m_4ha1:
  code: M_4HA1
  type: METERS/EM
  connections:
    m_main: FULLY_AGGREGATES
    bldg: CONTAINS

m_ahu1:
  code: M_AHU-1
  type: METERS/EM
  connections:
    m_4ha1: PARTIALLY_AGGREGATES
    bldg: CONTAINS

m_ahu2:
  code: AHU-2
  type: METERS/EM
  connections:
    m_4ha1: PARTIALLY_AGGREGATES
    bldg: CONTAINS

m_ahu3:
  code: AHU-3
  type: METERS/EM
  connections:
    m_4ha1: PARTIALLY_AGGREGATES
    bldg: CONTAINS

# Loadtypes

hvac:
  code: HVAC
  type: METERS/LOADTYPE
  connections:
    m_ahu1: MEASURES_TYPE
    m_ahu2: MEASURES_TYPE
    m_ahu3: MEASURES_TYPE
    bldg: CONTAINS

main:
  code: MAIN
  type: METERS/LOADTYPE
  connections:
    m_main: MEASURES_TYPE
    bldg: CONTAINS

plug:
  code: PLUG
  type: METERS/LOADTYPE
  connections:
    m_tc1: MEASURES_TYPE
    bldg: CONTAINS

```
