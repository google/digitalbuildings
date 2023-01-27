# Chilled & Condensing Water Systems (CHWS & CWS)

## Type Definition
Hydronic cooling and condensing systems. Chilled water systems cool water mechanically, which circulates to end-use devices; they dump the heat absorbed from the chilled water loop either to atmosphere ('air-cooled') or to another water distribution system ('water-cooled'). Condensing systems serve those mechanical devices which rely on water-source heat rejection.

There are many varieties of chilled & condenser water system, but some common examples include:
- **Constant volume** (predominantly on condensing water systems), where pumps run at constant speeds providing fixed flowrates at given stages.
- **Variable primary**, where there is one loop between the chillers and the end devices. The pumps operate at variable speed.
- **Primary/Secondary**, where there are two separate loops, with the primary serving as the production loop and the secondary serving as the distribution loop.

## Type Requirements
- Chillers require the mechanical cooling of water.
- Condensers require that, regardless of their own cooling method (sensible or evaporative), they serve downstream devices which require water as a condensing source.
- Heat exchangers provide heat transfer between two fluid streams, without intermixing the fluids. They are modeled separately only if they are stand-alone devices. 

## Connection Requirements
- The equipment which is part of each system should be assigned a HAS_PART connection to it.
- The specific interconnections between equipment in the system can also be defined through feeds connections. In these cases, it is best to feed from the pumps.
- To simplify distribution specifics, the system (rather than the system pumps) should be used to feed downstream equipment.

## Example: Variable Primary CHWS (Air-Cooled) 
This version of CHWS has a single set of variable speed pumps which serve air-cooled chillers and downstream equipment.

### BMS Example
![CHWS Variable Primary](./figures/bms_screenshots/chw_aircooled.png)
**Notes:**
- The fields associated with individual devices (individual chiller commands, for example) get mapped to those devices; system level telemetry gets assigned to the system directly.

### System Diagram and Connections
![CHWS Variable Primary](./figures/system_diagrams/chws_aircooled.png)

### Sample Building Config
```yaml
# System definition. Everything that it serves will be fed by it, everything that comprises it will be contained by it.
CHWSYS-BLDG-1:
  cloud_device_id: 1234
  type: HVAC/CHWS_...
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

# Plant equipment, all contained by the system.
# Various interconnections between the pumps and the chillers can also be defined as feeds connections.
CH-1:
  cloud_device_id: 2345
  connections:
    CHWSYS-BLDG-1: HAS_PART
    PMP-1: FEEDS
    PMP-2: FEEDS
  type: HVAC/CH_...
  translation:
    supply_water_temperature_sensor:
      present_value: points.swt.present_value
      units:
        key: pointset.points.swt.units
        values:
          degrees_fahrenheit: 'deg-F'
    ...

PMP-1:
  cloud_device_id: 3456
  connections:
    CHWSYS-BLDG-1: HAS_PART
  type: HVAC/PMP_...
  translation:
    run_command:
      present_value: points.cmd.present_value
      states:
        OFF: 'false'
        ON: 'true'
    ...

PMP-2:
  cloud_device_id: 4567
  connections:
    CHWSYS-BLDG-1: HAS_PART
  type: HVAC/PMP_...
  translation:
    run_command:
      present_value: points.cmd.present_value
      states:
        OFF: 'false'
        ON: 'true'
    ...

# Equipment served by the chilled wwater system.
FCU-1:
  cloud_device_id: 5678
  connections:
    CHWSYS-BLDG-1: FEEDS
  type: HVAC/FCU_DFSS_DFVSC_...
  translation:
    chilled_water_valve_percentage_command:
      present_value: points.clg_valve_percentage_command.present_value
      units:
        key: pointset.points.clg_valve_percentage_command.units
        values:
          percent: '%'
    ...

AHU-1:
  cloud_device_id: 6789
  connections:
    CHWSYS-BLDG-1: FEEDS
  type: HVAC/AHU_DFSS_...
  translation:
    chilled_water_valve_percentage_command:
      present_value: points.chwv.present_value
      units:
        key: pointset.points.chwv.units
        values:
          percent: '%'
    ...


```

## Example: Variable Primary CHWS (Water-Cooled) 
This version of CHWS has a single set of variable speed chilled water pumps serving water-cooled chillers and downstream equipment. The condensing side serves the chillers via two pumps.

### BMS Example
![CHWS Variable Primary WC](./figures/bms_screenshots/chws_watercooled.png)
**Notes:**
- This example includes a parallel air-cooled chiller. It is simple enough to add; it doesnt change the way the rest of the system is modeled.

### System Diagram and Connections
![CHWS Variable Primary WC](./figures/system_diagrams/chws_watercooled.png)

### Sample Building Config
```yaml
# Chilled water system feeds the equipment, and contains the distribution/production equipment.
CHWSYS-BLDG-1:
  cloud_device_id: 1234
  connections:
    CDWSYS-BLDG-1: FEEDS
  type: HVAC/CHWS_...
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

# Condenser wawter system feeds the chilled water system, 
CDWSYS-BLDG-1:
  cloud_device_id: 2345
  type: HVAC/CDWS_...
  translation:
    supply_water_temperature_sensor:
      present_value: points.sys_swt.present_value
      units:
        key: pointset.points.sys_swt.units
        values:
          degrees_fahrenheit: 'deg-F'
    ...

# Equipment contained by chilld water system.
# Various interconnections between the pumps and the chillers can also be defined as feeds connections.
CH-1:
  cloud_device_id: 3456
  connections:
    CHWSYS-BLDG-1: HAS_PART
    CWP-4: FEEDS
  type: HVAC/CH_...
  translation:
    supply_water_temperature_sensor:
      present_value: points.swt.present_value
      units:
        key: pointset.points.swt.units
        values:
          degrees_fahrenheit: 'deg-F'
    ...

CH-2:
  cloud_device_id: 4567
  connections:
    CHWSYS-BLDG-1: HAS_PART
    CWP-3: FEEDS
  type: HVAC/CH_...
  translation:
    supply_water_temperature_sensor:
      present_value: points.swt.present_value
      units:
        key: pointset.points.swt.units
        values:
          degrees_fahrenheit: 'deg-F'
    ...

ACC-1: # Note: this is a non-compliant equipment name, which may exist in brownfield sites. 
  cloud_device_id: 5678
  connections:
    CHWSYS-BLDG-1: HAS_PART
  type: HVAC/CH_...
  translation:
    supply_water_temperature_sensor:
      present_value: points.swt.present_value
      units:
        key: pointset.points.swt.units
        values:
          degrees_fahrenheit: 'deg-F'
    ...

CHWP-1:
  cloud_device_id: 6789
  connections:
    CHWSYS-BLDG-1: HAS_PART
    CH-1: FEEDS
    CH-2: FEEDS
    CHWP-7: FEEDS
  type: HVAC/PMP_...
  translation:
    run_command:
      present_value: points.cmd.present_value
      states:
        OFF: 'false'
        ON: 'true'
    ...

CHWP-2:
  cloud_device_id: 7890
  connections:
    CHWSYS-BLDG-1: HAS_PART
    CH-1: FEEDS
    CH-2: FEEDS
    CHWP-7: FEEDS
  type: HVAC/PMP_...
  translation:
    run_command:
      present_value: points.cmd.present_value
      states:
        OFF: 'false'
        ON: 'true'
    ...

CHWP-7:
  cloud_device_id: 8901
  connections:
    CHWSYS-BLDG-1: HAS_PART
    ACC-1: FEEDS
  type: HVAC/PMP_...
  translation:
    run_command:
      present_value: points.cmd.present_value
      states:
        OFF: 'false'
        ON: 'true'
    ...

# Condensing water system equipment.
CT-1:
  cloud_device_id: 9012
  connections:
    CDWSYS-BLDG-1: HAS_PART
    CWP-3: FEEDS
    CWP-4: FEEDS
  type: HVAC/CT_...
  translation:
    supply_water_temperature_sensor:
      present_value: points.swt.present_value
      units:
        key: pointset.points.swt.units
        values:
          degrees_fahrenheit: 'deg-F'
    ...

CT-2:
  cloud_device_id: 11234
  connections:
    CDWSYS-BLDG-1: HAS_PART
    CWP-3: FEEDS
    CWP-4: FEEDS    
  type: HVAC/CT_...
  translation:
    supply_water_temperature_sensor:
      present_value: points.swt.present_value
      units:
        key: pointset.points.swt.units
        values:
          degrees_fahrenheit: 'deg-F'
    ...

CWP-3:
  cloud_device_id: 12234
  connections:
    CDWSYS-BLDG-1: HAS_PART
  type: HVAC/PMP_...
  translation:
    run_command:
      present_value: points.cmd.present_value
      states:
        OFF: 'false'
        ON: 'true'
    ...

CWP-4:
  cloud_device_id: 12334
  connections:
    CDWSYS-BLDG-1: HAS_PART
  type: HVAC/PMP_...
  translation:
    run_command:
      present_value: points.cmd.present_value
      states:
        OFF: 'false'
        ON: 'true'
    ...

# Equipment served by the chilled wwater system.
FCU-1:
  cloud_device_id: 12344
  connections:
    CHWSYS-BLDG-1: FEEDS
  type: HVAC/FCU_...
  translation:
    chilled_water_valve_percentage_command:
      present_value: points.clg_valve_percentage_command.present_value
      units:
        key: pointset.points.clg_valve_percentage_command.units
        values:
          percent: '%'
    ...

AHU-1:
  cloud_device_id: 12345
  connections:
    CHWSYS-BLDG-1: FEEDS
  type: HVAC/AHU_...
  translation:
    chilled_water_valve_percentage_command:
      present_value: points.chwv.present_value
      units:
        key: pointset.points.chwv.units
        values:
          percent: '%'
    ...


```

**Note:** All BMS screenshots taken from Google's WebCTRL instances. WebCTRL is a building automation system owned by Automated Logic.