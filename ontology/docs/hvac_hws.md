# Heating Water Systems (HWS)

## Type Definition
Hydronic heating systems (HWS) contain boilers (BLR), pumps (PMP), and associated field telemetry.

## Type Requirements
- It *must* handle water for the purposes of heating.

## Example: Variable Primary HWS 
This version of HWS has a single set of variable speed pumps which serve boilers and downstream equipment.

### BMS Example
![HWS Variable Primary](./figures/bms_screenshots/hwsys.png)
**Notes:**
- The fields associated with individual devices (individual supply water temps for each boiler, for example) get mapped to those devices; system level telemetry gets assigned to the system directly.

### System Diagram and Connections
![HWS Variable Primary](./figures/system_diagrams/hwsys.png)

### Sample Building Config
```yaml
BLDG-1:
  type: FACILITIES/BUILDING

ZONE-1:
  connections:
    BLDG-1: CONTAINS
  type: FACILITIES/ZONE

ZONE-2:
  connections:
    BLDG-1: CONTAINS
  type: FACILITIES/ZONE

BLR-1:
  connections:
    BLDG-1: CONTAINS
    HWSYS-BLDG-1: CONTAINS
  type: HVAC/BLR_...
  translation:
    supply_water_temperature_sensor:
      present_value: points.swt.present_value
      units:
        key: pointset.points.swt.units
        values:
          degrees_fahrenheit: 'deg-F'
    ...

BLR-2:
  connections:
    BLDG-1: CONTAINS
    HWSYS-BLDG-1: CONTAINS
  type: HVAC/BLR_...
  translation:
    supply_water_temperature_sensor:
      present_value: points.swt.present_value
      units:
        key: pointset.points.swt.units
        values:
          degrees_fahrenheit: 'deg-F'
    ...

PMP-1:
  connections:
    BLDG-1: CONTAINS
    HWSYS-BLDG-1: CONTAINS
  type: HVAC/PMP_...
  translation:
    run_command:
      present_value: points.cmd.present_value
      states:
        OFF: 'false'
        ON: 'true'
    ...

PMP-2:
  connections:
    BLDG-1: CONTAINS
    HWSYS-BLDG-1: CONTAINS
  type: HVAC/PMP_...
  translation:
    run_command:
      present_value: points.cmd.present_value
      states:
        OFF: 'false'
        ON: 'true'
    ...

HWSYS-BLDG-1:
  connections:
    BLDG-1: CONTAINS
    FCU-1: FEEDS
    VAV-1: FEEDS
  type: HVAC/HWS_...
  translation:
    supply_water_temperature_sensor:
      present_value: points.sys_swt.present_value
      units:
        key: pointset.points.sys_swt.units
        values:
          degrees_fahrenheit: 'deg-F'
    differential_pressure_sensor:
      present_value: points.sys_dp.present_value
      units:
        key: pointset.points.sys_dp.units
        values:
          pascals: 'Pa'
    ...

FCU-1:
  connections:
    ZONE-1: FEEDS
    BLDG-1: CONTAINS
  type: HVAC/FCU_DFSS_DFVSC_...
  translation:
    heating_water_valve_percentage_command:
      present_value: points.htg_valve_percentage_command.present_value
      units:
        key: pointset.points.htg_valve_percentage_command.units
        values:
          percent: '%'
    ...

VAV-1:
  connections:
    ZONE-2: FEEDS
    BLDG-1: CONTAINS
  type: HVAC/VAV_SD_DSP_...
  translation:
    heating_water_valve_percentage_command:
      present_value: points.hwv.present_value
      units:
        key: pointset.points.hwv.units
        values:
          percent: '%'
    ...


```