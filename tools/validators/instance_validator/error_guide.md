# Instance Validator Error Message Guide
Please use the following documentation to lookup descriptions and examples of any instance validation errors resulting from your config file.

## Abstract Type Input as General Type

### Description:
User inputs an abstract type where a general type is expected.

### Example Bad Config:
```
# ZONE is an abstract type.

ZONE-105-GUID:
  type: HVAC/ZONE
  code: ZONE-105
```

### Error Message:
```
[ERROR]	Entity ZONE-105-GUID (ZONE-105) is defined with an abstract entity type: ZONE. Abstract types cannot be applied to individual entity instances. Define a non-abstract type that uses this abstract type and apply that to this instance.
```

## Invalid Entity Connection

### Description:
Entity connections must use one of the valid terms defined in DBO, i.e. “Contains,” “Feeds”.

### Example Bad Config:
```
# INVALID is not a valid connection for an entity to have.

US-SEA-BLDG1-GUID:
  type: FACILITIES/BUILDING
  code: US-SEA-BLDG1 
  connections:
    # Listed entities are sources on connections
    ANOTHER-ENTITY-GUID: FEEDS
    A-THIRD-ENTITY-GUID: INVALID
```

### Error Message:
```
[ERROR]	Entity US-SEA-BLDG1-GUID (US-SEA-BLDG1) defines connection INVALID, which does not exist in the ontology.
```

## Link to Nonexistent Entity 

### Description:
Each entity linked by another needs to be defined in the config file.

### Example Bad Config:
```
# NONEXISTENT-ENTITY-GUID is not defined in the config file.

ENTITY-NAME-GUID:
  type: FACILITIES/BUILDING
  code: ENTITY-NAME
  links:
    NONEXISTENT-ENTITY-GUID:
      supply_air_damper_command: supply_air_damper_position_command_1
      zone_air_temperature_sensor: zone_air_temperature_1

A-FOURTH-ENTITY-GUID:
  type: FACILITIES/BUILDING
  code: A-FOURTH-ENTITY
```

### Error Message:
```
[ERROR]	Entity ENTITY-NAME-GUID (ENTITY-NAME) links to target field supply_air_damper_command that is invalid for link: NONEXISTENT-ENTITY-GUID: {'supply_air_damper_command': 'supply_air_damper_position_command_1', 'zone_air_temperature_sensor': 'zone_air_temperature_1'}
[ERROR]	Entity ENTITY-NAME-GUID (ENTITY-NAME) links to target field zone_air_temperature_sensor that is invalid for link: NONEXISTENT-ENTITY-GUID: {'supply_air_damper_command': 'supply_air_damper_position_command_1', 'zone_air_temperature_sensor': 'zone_air_temperature_1'}
```

## Link to Invalid Field

### Description:
Each field in links needs to be valid within the ontology.

### Example Bad Config:
```
# supply_air_damper_position_command_1 is not a valid field.

ENTITY-NAME-GUID:
  type: FACILITIES/BUILDING
  code: ENTITY-NAME
  links:
    A-FOURTH-ENTITY-GUID:
      invalid_field: supply_air_damper_position_command_1

A-FOURTH-ENTITY-GUID:
  type: FACILITIES/BUILDING
  code: A-FOURTH-ENTITY
```

### Error Message:
```
ERROR]	Entity ENTITY-NAME-GUID (ENTITY-NAME) links to target field invalid_field that is invalid for link: A-FOURTH-ENTITY-GUID: {'invalid_field': 'supply_air_damper_position_command_1'}
```

## Entity Type Structure

### Description:
Entity types should be two levels deep, containing  NAMESPACE/TYPE_NAME.

### Example Bad Config:
```
US-SEA-BLDG1-GUID:
  type: FACILITIES/BUILDING/ERRORORO
  code: US-SEA-BLDG1
```

### Error Message:
```
TypeError: Type is improperly formatted: FACILITIES/BUILDING/ERRORORO. Proper formatting is: NAMESPACE/TYPE_NAME
```

## Invalid Entity Type

### Description:
Entity types must be a valid type defined in DBO.

### Example Bad Config:
```
US-SEA-BLDG1-GUID:
  type: LIGHTING/NOT_A_LAMP
  code: US-SEA-BLDG1
```

### Error Message:
```
[ERROR]	Entity US-SEA-BLDG1-GUID (US-SEA-BLDG1) is defined with an invalid entity type: NOT_A_LAMP in namespace LIGHTING. Confirm the type is defined in the ontology, and in the correct namespace.
```

## Invalid Namespace

### Description:
Namespaces must be defined in DBO.

### Example Bad Config:
```
US-SEA-BLDG1-GUID:
  type: NONEXISTENT/BUILDING
  code: US-SEA-BLDG1
```

### Error Message:
```
[ERROR]	Entity US-SEA-BLDG1-GUID (US-SEA-BLDG1) is defined with an invalid namespace: NONEXISTENT. Confirm the namespace is defined in the ontology.
```

## Onboarded Device with Missing Translation

### Description:
Devices that report to the cloud (containing a cloud device id) must have a defined translation, either the existing one or an updated one, unless the entity is being deleted.

### Example Bad Config:
```
# entity with cloud_device_id specified but no translations; fails as default operation is ADD

DMP_EDM-17-GUID:
  type: HVAC/DMP_EDM
  code: DMP_EDM-17
  cloud_device_id: "1234567890123456"

US-SEA-BLDG1-GUID:
  type: FACILITIES/BUILDING
  code: US-SEA-BLDG1
```

### Error Message:
```
[ERROR]	Entity (DMP_EDM-17-GUID: DMP_EDM-17) Has a type which has defined fields but this instance has neither links nor a translation.
[ERROR]	Entity DMP_EDM-17-GUID (DMP_EDM-17) has a cloud_device_id but is missing a translation. Reporting devices must have a translation when cloud_device_id is present; unless the operation is DELETE
```

## No Provided Fields

### Description:
Non-facility entities must have defined fields or link to a reporting device with their fields defined.

### Example Bad Config:
```
SDC_EXT-17-GUID:
  type: HVAC/SDC_EXT
  etag: a12345
  code: SDC_EXT-17

CONFIG_METADATA:
  operation: UPDATE

US-SEA-BLDG1-GUID:
  type: FACILITIES/BUILDING
  etag: b23456
  code: US-SEA-BLDG1
```

### Error Message:
```
[ERROR]	Entity (SDC_EXT-17-GUID: SDC_EXT-17) Has a type which has defined fields but this instance has neither links nor a translation.
```

## Duplicate Key/GUID

### Description:
Each defined entity must have a unique GUID.

### Example Bad Config:
```
SDC_EXT-17-GUID:
  type: HVAC/SDC_EXT
  code: SDC_EXT-17

SDC_EXT-17-GUID:
  type: HVAC/SDC_EXT
  code: SDC_EXT-17

US-SEA-BLDG1-GUID:
  type: FACILITIES/BUILDING
  code: US-SEA-BLDG1
```

### Error Message:
```
While parsing
  in "<unicode string>", line 4, column 1:
    SDC_EXT-17-GUID:
    ^ (line: 4)
Duplicate key 'SDC_EXT-17-GUID' found
  in "<unicode string>", line 4, column 16:
    SDC_EXT-17-GUID:
                   ^ (line: 4)
```

## Repeated Types

### Description:
Each entity must have a single defined type.

### Example Bad Config:
```
US-SEA-BLDG1-GUID:
  type: FACILITIES/BUILDING
  type: FACILITIES/123456b
  code: US-SEA-BLDG1
```

### Error Message:
```
While parsing
  in "<unicode string>", line 3, column 3:
      type: FACILITIES/123456b
      ^ (line: 3)
Duplicate key 'type' found
  in "<unicode string>", line 3, column 7:
      type: FACILITIES/123456b
          ^ (line: 3)
```

## Duplicate Metadata

### Description:
A config can only have one metadata block.

### Example Bad Config:
```
SDC_EXT-18-GUID:
  code: SDC_EXT-18

CONFIG_METADATA:
  operation: UPDATE

CONFIG_METADATA:
  operation: INITIALIZE

US-SEA-BLDG1-GUID:
  type: FACILITIES/BUILDING
  code: US-SEA-BLDG1
```

### Error Message:
```
while parsing a mapping
  in "<unicode string>", line 1, column 1:
    SDC_EXT-18-GUID:
     ^ (line: 1)
required key(s) 'type' not found
  in "<unicode string>", line 2, column 1:
      code: SDC_EXT-18
    ^ (line: 2)
```

## Update Mask with Add Operation

### Description:
Update masks can only exist then the defined operation is “Update”.

### Example Bad Config:
```
SDC_EXT-17-GUID:
  type: HVAC/SDC_EXT
  code: SDC_EXT-17
  operation: ADD
  update_mask:
  - translation

US-SEA-BLDG1-GUID:
  type: FACILITIES/BUILDING
  etag: a1234
  code: US-SEA-BLDG1
```

### Error Message:
```
while parsing a mapping
unexpected key not in schema 'operation'
  in "<unicode string>", line 4, column 1:
      operation: ADD
    ^ (line: 4)
```

## Cloud Device ID Structure

### Description:
A cloud device ID must be a 16 digit string.

### Example Bad Config:
```
SDC_EXT-17-GUID:
  type: HVAC/SDC_EXT
  code: SDC_EXT-17
  cloud_device_id: "bad_device_id"
  translation:
    shade_extent_percentage_command:
      present_value: "points.shade_extent_percentage_command.present_value"
      units:
        key: "points.shade_extent_percentage_command.units"
        values:
          percent: "%"

US-SEA-BLDG1-GUID:
  type: FACILITIES/BUILDING
  code: US-SEA-BLDG1
```

### Error Message:
```
[ERROR]	Entity SDC_EXT-17-GUID (SDC_EXT-17) invalid cloud_device_id, please refer to the documentation: https://github.com/google/digitalbuildings/blob/master/ontology/docs/building_config.md#identifiers [0-9]{16}
```

## Entity Update Requirements

### Description:
When updating an existing entity, the etag and update_mask must be specified.

### Example Bad Config:
```
CONFIG_METADATA:
  operation: UPDATE

US-SEA-BLDG1-GUID:
  operation: UPDATE
  type: FACILITIES/BUILDING
  code: US-SEA-BLDG1
```

### Error Message:
```
while parsing a mapping
  in "<unicode string>", line 1, column 1:
    US-SEA-BLDG1-GUID:
     ^ (line: 1)
required key(s) 'etag', 'update_mask' not found
  in "<unicode string>", line 4, column 1:
      code: US-SEA-BLDG1
    ^ (line: 4)
```

## Entity Export Requirements

### Description:
An etag is required on entities when performing an export operation.

### Example Bad Config:
```
CONFIG_METADATA:
  operation: UPDATE

SDC_EXT-19-GUID:
  type: HVAC/SDC_EXT
  code: SDC_EXT-19
  cloud_device_id: "baz"
  operation: EXPORT
```

### Error Message:
```
while parsing a mapping
  in "<unicode string>", line 1, column 1:
    SDC_EXT-19-GUID:
     ^ (line: 1)
required key(s) 'etag' not found
  in "<unicode string>", line 5, column 1:
      operation: EXPORT
    ^ (line: 5)
```

## Duplicate Cloud Device IDs

### Description:
Each entity must have a unique cloud device id.

### Example Bad Config:
```
SDC_EXT-17-GUID:
  type: HVAC/SDC_EXT
  code: SDC_EXT-17
  cloud_device_id: "2619178366980754"
  translation:
    shade_extent_percentage_command:
      present_value: "points.shade_extent_percentage_command.present_value"
      units:
        key: "pointset.points.shade_extent_percentage_command.units"
        values:
          percent: "%"

SDC_EXT-18-GUID:
  type: HVAC/SDC_EXT
  code: SDC_EXT-18
  cloud_device_id: "2619178366980754"
  translation:
    shade_extent_percentage_command:
      present_value: "points.shade_extent_percentage_command.present_value"
      units:
        key: "pointset.points.shade_extent_percentage_command.units"
        values:
          percent: "%"

US-SEA-BLDG1-GUID:
  type: FACILITIES/BUILDING
  code: US-SEA-BLDG1
```

### Error Message:
```
[ERROR]	Duplicate cloud device id 2619178366980754 used for multiple entities:
SDC_EXT-17-GUID: SDC_EXT-17
SDC_EXT-18-GUID: SDC_EXT-18
```

## Too Many Operations

### Description:
A building config can only contain two operations at once, one of which being export.

### Example Bad Config:
```
CONFIG_METADATA:
  operation: UPDATE

VIRTUAL-ENTITY-GUID:
  type: HVAC/CHWS_WDT
  code: VIRTUAL-ENTITY
  etag: a56789
  links:
    PHYSICAL-ENTITY-GUID:
      return_water_temperature_sensor: return_water_temperature_sensor
      supply_water_temperature_sensor: supply_water_temperature_sensor
      thermal_power_capacity: thermal_power_capacity
      differential_pressure_specification: differential_pressure_specification
  update_mask:
    - links

PHYSICAL-ENTITY-GUID:
  type: HVAC/CHWS_WDT
  code: PHYSICAL-ENTITY
  cloud_device_id: "foobar"
  translation:
    return_water_temperature_sensor:
      present_value: "points.return_water_temperature_sensor.present_value"
      units:
        key: "pointset.points.return_water_temperature_sensor.units"
        values:
          degrees_celsius: "degC"
    supply_water_temperature_sensor:
      present_value: "points.supply_water_temperature_sensor.present_value"
      units:
        key: "pointset.points.supply_water_temperature_sensor.units"
        values:
          degrees_celsius: "degC"
    thermal_power_capacity:
      present_value: "points.thermal_power_capacity.present_value"
      units:
        key: "pointset.points.thermal_power_capacity.units"
        values:
          kilowatts: "kilowatts"
    differential_pressure_specification:
      present_value: "points.differential_pressure_specification.present_value"
      units:
        key: "pointset.points.differential_pressure_specification.units"
        values:
          pascals: "pascals"
  operation: ADD

US-SEA-BLDG1-GUID:
  type: FACILITIES/BUILDING
  code: US-SEA-BLDG1
  etag: a56789
  operation: EXPORT
```

### Error Message:
```
[WARNING] (v1 Alpha): Building Config cannot have more than 2 operations; one being EXPORT.
```

## Entity Keyed by Code

### Description:
Each entity block must be keyed with a GUID with the code listed within the block.

### Example Bad Config:
```
CONFIG_METADATA:
  operation: INITIALIZE

PHYSICAL-ENTITY:
  type: HVAC/CHWS_WDT
  guid: PHYSICAL-ENTITY-GUID
  cloud_device_id: "foobar"
  translation:
    return_water_temperature_sensor:
      present_value: "points.return_water_temperature_sensor.present_value"
      units:
        key: "pointset.return_water_temperature_sensor.units"
        values:
          degrees_celsius: "degC"
    supply_water_temperature_sensor:
      present_value: "points.supply_water_temperature_sensor.present_value"
      units:
        key: "pointset.points.supply_water_temperature_sensor.units"
        values:
          degrees_celsius: "degC"
    thermal_power_capacity:
      present_value: "points.thermal_power_capacity.present_value"
      units:
        key: "pointset.points.thermal_power_capacity.units"
        values:
          kilowatts: "kilowatts"
    differential_pressure_specification:
      present_value: "points.differential_pressure_specification.present_value"
      units:
        key: "pointset.points.differential_pressure_specification.units"
        values:
          pascals: "pascals"

US-SEA-BLDG1:
  type: FACILITIES/BUILDING
  guid: US-SEA-BLDG1-GUID
```

### Error Message:
```
ValueError: Entity block must be keyed by a guid. Please adjust.
```

## Update Mask

### Description:
Update masks should only be included then the operation performed is “Update”.

### Example Bad Config:
```
US-SEA-BLDG1-GUID:
  type: FACILITIES/BUILDING
  code: US-SEA-BLDG1
  update_mask:
  - description
```

### Error Message:
```
while parsing a mapping
  in "<unicode string>", line 4, column 1:
      update_mask:
    ^ (line: 4)
unexpected key not in schema 'update_mask'
  in "<unicode string>", line 5, column 1:
      - description
    ^ (line: 5)
```

## State Structure

### Description:
States must include key value pairs of the DBO name and the name of the value coming from the controller.

### Example Bad Config:
```
FC2-1-1-GUID:
  cloud_device_id: '1234567890123456'
  code: FC2-1-1
  translation:
    compressor_run_command_1:
      present_value: data.binary-value_1.present-value
      states:
        OFF: 'inactive'
        ON:
  type: GATEWAYS/PASSTHROUGH

US-SEA-BLDG1-GUID:
  type: FACILITIES/BUILDING
  code: US-SEA-BLDG1
```

### Error Message:
```
ValueError: States must have defined string key and value pairs
```

## Operation Included with Initialize Mode

### Description:
When the config is in initialize mode, there cannot be any operations included on the entities.

### Example Bad Config:
```
US-SEA-BLDG1-GUID:
  type: FACILITIES/BUILDING
  operation: DELETE
  code: US-SEA-BLDG1

# Entity with bad enumeration
vav-guid-3:
  code: vav-3
  type: HVAC/CHWS_WDT
  cloud_device_id: 1234567891012345
  translation:
    thermal_power_capacity:
      present_value: "points.thermal_power_capacity.present_value"
      units:
        key: "pointset.points.thermal_power_capacity.units"
        values:
          watts: "Watts"
    differential_pressure_specification:
      present_value: "points.differential_pressure_specification.present_value"
      units:
        key: "pointset.points.differential_pressure_specification.units"
        values:
          pascals: "Pa"
    return_water_temperature_sensor:
      present_value: "points.return_water_temperature_sensor.present_value"
      units:
        key: "pointset.points.return_water_temperature_sensor.units"
        values:
          degrees_celsius: "degC"
    supply_water_temperature_sensor:
      present_value: "points.supply_water_temperature_sensor.present_value"
      units:
        key: "pointset.points.supply_water_temperature_sensor.units"
        values:
          degrees_celsius: "degC"
    supply_water_temperature_sensor_1:
      present_value: "points.supply_water_temperature_sensor_1.present_value"
      units:
        key: "pointset.points.supply_water_temperature_sensor_1.units"
        values:
          degrees_celsius: "degC"
```

### Error Message:
```
while parsing a mapping
unexpected key not in schema 'operation'
  in "<unicode string>", line 3, column 1:
      operation: DELETE
    ^ (line: 3)
```

## Reporting Entity Missing Fields

### Description:
Reporting entities must include all required fields of the entities that link to them.

### Example Bad Config:
```
# Building
US-SEA-BLDG1-GUID:
  type: FACILITIES/BUILDING
  code: US-SEA-BLDG1

ENTITY-NAME-GUID:
  type: HVAC/CHWS_WDT
  code: ENTITY-NAME
  links:
    A-FOURTH-ENTITY-GUID:
      # this is missing:
      # return_water_temperature_sensor: return_water_temperature_sensor
      supply_water_temperature_sensor: supply_water_temperature_sensor
      thermal_power_capacity: thermal_power_capacity
      differential_pressure_specification: differential_pressure_specification

A-FOURTH-ENTITY-GUID:
  type: HVAC/CHWS_WDT
  code: A-FOURTH-ENTITY
```

### Error message: 
```
Required field /return_water_temperature_sensor is missing from links
```

## Linked Target and Source Fields

### Description:
Linked target and source fields must have the same units of measurement.

### Example Bad Config:
```
ENTITY-NAME-GUID:
  type: HVAC/CHWS_WDT
  code: ENTITY-NAME
  links:
    A-FOURTH-ENTITY-GUID:
      return_water_temperature_sensor: return_water_temperature_sensor
      supply_water_temperature_sensor: thermal_power_capacity
      differential_pressure_specification: differential_pressure_specification

A-FOURTH-ENTITY-GUID:
  type: HVAC/CHWS_WDT
  code: A-FOURTH-ENTITY
```

### Error Message:
```
[ERROR]	Entity ENTITY-NAME-GUID (ENTITY-NAME) links target field /supply_water_temperature_sensor to source field /thermal_power_capacity but the units do not match between the fields.
```

## Missing Building

### Description:
The building must be provided in every building config.

### Example Bad Config:
```
AN-ENTITY-GUID:
  type: HVAC/CHWS_WDT
  code: AN-ENTITY
```

### Error Message:
```
SyntaxError: Building entity not found. Configs must contain a non-deleted entity of type FACILITIES/BUILDING.
```

## Missing Colon

### Description:
The YAML formatting requires colons for all keys in the config.

### Example Bad Config:
```
# Building
US-SEA-BLDG1-GUID:
  type: FACILITIES/BUILDING
  code US-SEA-BLDG1
```

### Error Message:
```
while scanning a simple key
  in "<unicode string>", line 3, column 3:
      code US-SEA-BLDG1
      ^ (line: 3)
could not find expected ':'
  in "<unicode string>", line 4, column 1:
    
    ^ (line: 4)
```

## Linked Field Mismatch

### Description:
Fields translated on a reporting entity must match the fields on the linked physical entity.

### Example Bad Config:
```
# this is a bad example since the virtual entity has a link to
# return_water_temperature_sensor_200 on the physical entity; however
# the physical entity doesn't have that point, it has
# return_water_temperature_sensor
VIRTUAL-ENTITY-GUID:
  type: HVAC/CHWS_WDT
  code: VIRTUAL-ENTITY
  links:
    PHYSICAL-ENTITY-GUID:
      return_water_temperature_sensor: return_water_temperature_sensor_200
      supply_water_temperature_sensor: supply_water_temperature_sensor
      thermal_power_capacity: thermal_power_capacity
      differential_pressure_specification: differential_pressure_specification

PHYSICAL-ENTITY-GUID:
  type: HVAC/CHWS_WDT
  code: PHYSICAL-ENTITY
  cloud_device_id: "1234567890123456"
  translation:
    return_water_temperature_sensor:
      present_value: "points.return_water_temperature_sensor.present_value"
      units:
        key: "pointset.points.return_water_temperature_sensor.units"
        values:
          degrees_celsius: "degC"
    supply_water_temperature_sensor:
      present_value: "points.supply_water_temperature_sensor.present_value"
      units:
        key: "pointset.points.supply_water_temperature_sensor.units"
        values:
          degrees_celsius: "degC"
    thermal_power_capacity:
      present_value: "points.thermal_power_capacity.present_value"
      units:
        key: "pointset.points.thermal_power_capacity.units"
        values:
          kilowatts: "kilowatts"
    differential_pressure_specification:
      present_value: "points.differential_pressure_specification.present_value"
      units:
        key: "pointset.points.differential_pressure_specification.units"
        values:
          pascals: "pascals"

US-SEA-BLDG1-GUID:
  type: FACILITIES/BUILDING
  code: US-SEA-BLDG1
```

### Error Message:
```
[ERROR]	Entity VIRTUAL-ENTITY-GUID (VIRTUAL-ENTITY) links to a source entity: PHYSICAL-ENTITY-GUID (PHYSICAL-ENTITY) that does not have the linked source field: return_water_temperature_sensor_200. Check that this field on source translation exists.
```

## Spacing

### Description:
Ensure there are no extra or missing leading spaces on a line as YAML files are read based on indentation.

### Example Bad Config:
```
US-SEA-BLDG1-GUID:
  type: FACILITIES/BUILDING
   code: US-SEA-BLDG1
```

### Error Message:
```
mapping values are not allowed here
  in "<unicode string>", line 3, column 8:
       code: US-SEA-BLDG1
           ^ (line: 3)
```

## Tabbing

### Description:
Ensure there are no extra or missing leading tabs on a line as YAML files are read based on indentation.

### Example Bad Config:
```
US-SEA-BLDG1-GUID:
    type: FACILITIES/BUILDING
  code: US-SEA-BLDG1
```

### Error Message:
```
while parsing a block mapping
  in "<unicode string>", line 1, column 1:
    US-SEA-BLDG1-GUID:
    ^ (line: 1)
expected <block end>, but found '<block mapping start>'
  in "<unicode string>", line 3, column 3:
      code: US-SEA-BLDG1
      ^ (line: 3)
```

## All Fields Missing 

### Description:
Every non-facility entity requires at least one non-missing field.

### Example Bad Config:
```
SDC_EXT-17-GUID:
  type: HVAC/SDC_EXT
  code: SDC_EXT-17
  cloud_device_id: "1234567890123456"
  translation:
    shade_extent_percentage_command: MISSING

US-SEA-BLDG1-GUID:
  type: FACILITIES/BUILDING
  code: US-SEA-BLDG1
```

### Error Message:
```
[ERROR]	Entity SDC_EXT-17-GUID (SDC_EXT-17) has all field translations marked as MISSING. This is not allowed.
```

## Translation Compliance

### Description:
Everything given in the translation section of a config must match, case-sensitive, to what is in DBO.

### Example Bad Config:
```
US-SEA-BLDG1-GUID:
  type: FACILITIES/BUILDING
  code: US-SEA-BLDG1

ENTITY_GUID:
  cloud_device_id: 0123456789012345
  code: LGRP-1
  translation:
    BRIGHTNESS_PERCENTAGE_COMMAND:
      present_value: points.brightness_percentage_command.present_value
      units:
        key: pointset.points.brightness_percentage_command.units
        values:
          percent: '%'
  type: LIGHTING/LGRP_DC
```

### Error Message:
```
when expecting string matching ^[a-z][a-z0-9]*(?:_[a-z][a-z0-9]*)*(?:_[0-9]+)*$
  in "<unicode string>", line 8, column 1:
        BRIGHTNESS_PERCENTAGE_COMMAND:
    ^ (line: 8)
found non-matching string
  in "<unicode string>", line 13, column 1:
              percent: '%'
    ^ (line: 13)
```

## Missing States

### Description:
All fields not marked as missing must include units or states in their translation.

### Example Bad Config:
```
ENTITY-GUID:
  cloud_device_id: '123456789'
  type: SAFETY/FACP_FA2X
  code: FACP-14
  translation:
    fire_alarm_1:
      present_value: points.fire_alarm_1.present_value
      states:
        ACTIVE: 'true'
        INACTIVE: 'false'
    fire_alarm_2:
      present_value: points.fire_alarm_2.present_value

US-ABC-BLDG-GUID:
  type: FACILITIES/BUILDING
  code: US-ABC-BLDG
```

### Error Message:
```
[ERROR]	Entity ENTITY-GUID (FACP-14) defines field /fire_alarm_2 without states, which are expected on the field. Define states.
```

## Missing Units

### Description:
All fields not marked as missing must include units or states in their translation.

### Example Bad Config:
```
# Test entity with numeric points missing units for supply_water_temperature_sensor

CHWS_WDT-17-GUID:
  type: HVAC/CHWS_WDT
  code: CHWS_WDT-17
  cloud_device_id: "123456789"
  translation:
    return_water_temperature_sensor:
      present_value: "points.return_water_temperature_sensor.present_value"
      units:
        key: "pointset.points.return_water_temperature_sensor.units"
        values:
          degrees_celsius: "degC"
    supply_water_temperature_sensor:
      present_value: "points.supply_water_temperature_sensor.present_value"

US-ABC-BLDG-GUID:
  type: FACILITIES/BUILDING
  code: US-ABC-BLDG
```

### Error Message:
```
[ERROR]	Entity CHWS_WDT-17-GUID (CHWS_WDT-17) defines field /supply_water_temperature_sensor but does not define valid units. Add units.
```


## Invalid UDMI Unit Structure

### Description:
UDMI requires units to be the following four levels deep: “pointset.points.[unit name].units”

### Example Bad Config:
```
PHYSICAL-ENTITY-GUID:
  type: GATEWAYS/PASSTHROUGH
  code: PHYSICAL-ENTITY
  cloud_device_id: "1234567890123456"
  translation:
    differential_pressure_specification:
      present_value: "points.differential_pressure_specification.present_value"
      units:
        # This is a bad unit path. The suffix must be `.units` and the prefix must be ‘pointset.points.’
        key: "points.differential_pressure_specification.present_value.unit"
        values:
          pascals: "pascals"

PHYSICAL-ENTITY-GUID-2:
  type: GATEWAYS/PASSTHROUGH
  code: PHYSICAL-ENTITY
  cloud_device_id: "1234567890123457"
  translation:
    differential_pressure_specification:
      present_value: "points.differential_pressure_specification.present_value"
      units:
        # This is a bad unit path. The suffix must be `.units` and the prefix must be ‘pointset.points.’
        key: "points.differential_pressure_specification"
        values:
          pascals: "pascals"
```

### Error Message:
```
[ERROR]	Entity PHYSICAL-ENTITY-GUID (PHYSICAL-ENTITY) translates field "points.differential_pressure_specification.present_value.unit" with a unit field name pattern that does not conform to UDMI pattern "^(pointset.points.)[a-z][a-z0-9]*(_[a-z0-9]+)*(.units)$".
[ERROR]	Entity PHYSICAL-ENTITY-GUID-2 (PHYSICAL-ENTITY) translates field "points.differential_pressure_specification" with a unit field name pattern that does not conform to UDMI pattern "^(pointset.points.)[a-z][a-z0-9]*(_[a-z0-9]+)*(.units)$".
```

## Invalid UDMI Present Value Structure

### Description:
UDMI requires present values to be the following three levels deep: “points.[present value name].present_value”.

### Example Bad Config:
```
PHYSICAL-ENTITY-GUID:
  type: GATEWAYS/PASSTHROUGH
  code: PHYSICAL-ENTITY
  cloud_device_id: "1234567890123456"
  translation:
    differential_pressure_specification:
      # Missing `present_value` suffix.
      present_value: "points.differential_pressure_specification"
      units:
        key: "points.differential_pressure_specification.present_value.units"
        values:
          pascals: "pascals"

PHYSICAL-ENTITY-GUID-2:
  type: GATEWAYS/PASSTHROUGH
  code: PHYSICAL-ENTITY
  cloud_device_id: "1234567890123457"
  translation:
    differential_pressure_specification:
      # Only the field name can exist between `points` and `present_value`.
      present_value: "points.differential_pressure_specification.garbage.present_value"
      units:
        key: "pointset.points.differential_pressure_specification.units"
        values:
          pascals: "pascals"

PHYSICAL-ENTITY-GUID-3:
  type: GATEWAYS/PASSTHROUGH
  code: PHYSICAL-ENTITY
  cloud_device_id: "1234567890123458"
  translation:
    differential_pressure_specification:
      # `Pointset` is an invalid prefix for a field's present value.
      present_value: "pointset.differential_pressure_specification.present_value"
      units:
        key: "pointset.points.differential_pressure_specification.units"
        values:
          pascals: "pascals"
```

### Error Message:
```
[ERROR]	Entity PHYSICAL-ENTITY-GUID (PHYSICAL-ENTITY) translates field "points.differential_pressure_specification" with a present value pattern that does not conform to the UDMI pattern."^(points.)[a-z][a-z0-9]*(_[a-z0-9]+)*(.present_value)$".
[ERROR]	Entity PHYSICAL-ENTITY-GUID (PHYSICAL-ENTITY) translates field "points.differential_pressure_specification.present_value.units" with a unit field name pattern that does not conform to UDMI pattern "^(pointset.points.)[a-z][a-z0-9]*(_[a-z0-9]+)*(.units)$".
[ERROR]	Entity PHYSICAL-ENTITY-GUID-2 (PHYSICAL-ENTITY) translates field "points.differential_pressure_specification.garbage.present_value" with a present value pattern that does not conform to the UDMI pattern."^(points.)[a-z][a-z0-9]*(_[a-z0-9]+)*(.present_value)$".
[ERROR]	Entity PHYSICAL-ENTITY-GUID-3 (PHYSICAL-ENTITY) translates field "pointset.differential_pressure_specification.present_value" with a present value pattern that does not conform to the UDMI pattern."^(points.)[a-z][a-z0-9]*(_[a-z0-9]+)*(.present_value)$".
```

## Invalid Range Format

### Description:
Field value ranges must include a minimum and a maximum.

### Example Bad Config:
```
US-SEA-BLDG1-GUID:
  type: FACILITIES/BUILDING
  code: US-SEA-BLDG1
  cloud_device_id: "foobar"
  translation:
    zone_air_temperature_sensor:
      present_value: "points.zone_air_temperature_sensor.present_value"
      value_range: 25
      units:
        key: "points.zone_air_temperature_sensor.units"
        values:
          degrees_celsius: "degC"
```

### Error Message:
```
[ERROR]	Invalid Entity syntax found for this entity: US-SEA-BLDG1-GUID and this content: "{'type': 'FACILITIES/BUILDING', 'code': 'US-SEA-BLDG1', 'cloud_device_id': 'foobar', 'translation': {'zone_air_temperature_sensor': {'present_value': 'points.zone_air_temperature_sensor.present_value', 'value_range': '25', 'units': {'key': 'points.zone_air_temperature_sensor.units', 'values': {'degrees_celsius': 'degC'}}}}}" and with error: "Value range in the translation for field "zone_air_temperature_sensor" should be formatted: <min>,<max>."
ValueError: Value range in the translation for field "zone_air_temperature_sensor" should be formatted: <min>,<max>.
```

## Invalid Value Range Order

### Description:
Field value ranges must specify the minimum prior to the maximum.

### Example Bad Config:
```
US-SEA-BLDG1-GUID:
  type: FACILITIES/BUILDING
  code: US-SEA-BLDG1
  cloud_device_id: "foobar"
  translation:
    zone_air_temperature_sensor:
      present_value: "points.zone_air_temperature_sensor.present_value"
      value_range: 25,15
      units:
        key: "points.zone_air_temperature_sensor.units"
        values:
          degrees_celsius: "degC"
```

### Error Message:
```
[ERROR]	Invalid Entity syntax found for this entity: US-SEA-BLDG1-GUID and this content: "{'type': 'FACILITIES/BUILDING', 'code': 'US-SEA-BLDG1', 'cloud_device_id': 'foobar', 'translation': {'zone_air_temperature_sensor': {'present_value': 'points.zone_air_temperature_sensor.present_value', 'value_range': '25,15', 'units': {'key': 'points.zone_air_temperature_sensor.units', 'values': {'degrees_celsius': 'degC'}}}}}" and with error: "Value range in the translation for field "zone_air_temperature_sensor" should have a min value that is less than the max value."
ValueError: Value range in the translation for field "zone_air_temperature_sensor" should have a min value that is less than the max value.
```

## Translation Keys

### Description:
Translations should only include fields and their corresponding present value and unit or state. 

### Example Bad Config:
```
# This config file is invalid because it fails to pass the syntax expectations
# for translation. The devices listed in translation need to follow specific
# formats, and `invalid_key` is not a valid part of any of them.

US-SEA-BLDG1-GUID:
  type: FACILITIES/BUILDING
  code: US-SEA-BLDG1
  cloud_device_id: "foobar"
  translation:
    zone_air_temperature_sensor:
      present_value: "temp_1"
      units:
        key: "units"
        values:
          degrees_celsius: "degC"
      invalid_key: "invalid"

SDC_EXT-17-GUID:
  type: HVAC/SDC_EXT
  code: SDC_EXT-17
  translation:
    shade_extent_percentage_command:
      present_value: "points.shade_extent_percentage_command.present_value"
      units:
        key: "points.shade_extent_percentage_command.units"
        values:
          percent: "%"

US-SEA-BLDG1-GUID:
  type: FACILITIES/BUILDING
  code: US-SEA-BLDG1
```

### Error Message:
```
while parsing a mapping
unexpected key not in schema 'invalid_key'
  in "<unicode string>", line 12, column 1:
          invalid_key: invalid
    ^ (line: 12)
```

## Missing Cloud Device ID on Entity with Translation

### Description:
Any entity with a translation must include a cloud device id.

### Example Bad Config:
```
SDC_EXT-17-GUID:
  type: HVAC/SDC_EXT
  code: SDC_EXT-17
  translation:
    shade_extent_percentage_command:
      present_value: "points.shade_extent_percentage_command.present_value"
      units:
        key: "points.shade_extent_percentage_command.units"
        values:
          percent: "%"

US-SEA-BLDG1-GUID:
  type: FACILITIES/BUILDING
  code: US-SEA-BLDG1
```

### Error Message: 
```
KeyError: 'cloud_device_id required when translation is present.'
```

## Multiple Units on a Field

### Description:
A field can only have one unit defined.

### Example Bad Config:
```
US-SEA-BLDG1-GUID:
  type: FACILITIES/BUILDING
  code: US-SEA-BLDG1
  cloud_device_id: "foobar"
  translation:
    zone_air_temperature_sensor:
      present_value: "temp_1"
      units:
        key: "units"
        values:
          degrees_celsius: "degC"
          degrees_fahrenheit: "degF"
```

### Error Message:
```
[ERROR]	Invalid Entity syntax found for this entity: US-SEA-BLDG1-GUID and this content: "{'type': 'FACILITIES/BUILDING', 'code': 'US-SEA-BLDG1', 'cloud_device_id': 'foobar', 'translation': {'zone_air_temperature_sensor': {'present_value': 'temp_1', 'units': {'key': 'units', 'values': {'degrees_celsius': 'degC', 'degrees_fahrenheit': 'degF'}}}}}" and with error: "There should be exactly 1 unit mapping in the translation for field "zone_air_temperature_sensor"."
ValueError: There should be exactly 1 unit mapping in the translation for field "zone_air_temperature_sensor".
```

## Missing Optional Field

### Description:
Only required fields should be marked as missing if the device does not have it. Any optional field that the device does not have should simply be omitted.

### Example Bad Config:
```
FAN-1-GUID-FOR-OPT-FIELD-MARKED-MISSING:
  type: HVAC/FAN_SS
  code: FAN-1
  cloud_device_id: "foobar"
  translation:
    run_command:
      present_value: "points.run_command.present_value"
      states:
        ON: "on"
        OFF: "off"
    run_status:
      present_value: "points.run_status.present_value"
      states:
        ON: "on"
        OFF: "off"
    power_sensor: MISSING

US-SEA-BLDG1-GUID:
  type: FACILITIES/BUILDING
  code: US-SEA-BLDG1
```

### Error Message:
```
[ERROR]	Entity FAN-1-GUID-FOR-OPT-FIELD-MARKED-MISSING (FAN-1) provides MISSING translation for field /power_sensor, which is optional on type FAN_SS. The use of MISSING fields is strictly reserved for required fields. Adjust the translation and remove MISSING optional fields.
```

## Invalid State

### Description:
States included in the config must be states that are defined in DBO for the given field.

### Example Bad Config:
```
PMP1-GUID:
  cloud_device_id: "foobar"
  type: HVAC/PMP_SS
  code: PMP-101
  translation:
    failed_alarm:
      present_value: points.failed_alarm.present_value
      states:
        ACTIVE: true
        INVALID_STATE: "2"
    run_status:
      present_value: points.run_status.present_value
      states:
        ON: true
        OFF: false
    run_command: MISSING
```

### Error Message:
```
[ERROR]	Entity PMP1-GUID (PMP-101) defines field /failed_alarm with an invalid state: INVALID_STATE. Allowed states are (['ACTIVE', 'INACTIVE']).
```

## Duplicate States

### Description:
Each telemetry value coming from the payload must only map to a single state on a field.

### Example Bad Config:
```
# This config file is invalid because the telemetry value "1" is mapped to
# both OPEN and CLOSED states of exhaust_air_damper_status.

DMP_EDM-17-GUID:
  type: HVAC/DMP_EDM
  code: DMP_EDM-17
  cloud_device_id: "foobar"
  translation:
    exhaust_air_damper_command:
      present_value: "points.exhaust_air_damper_command.present_value"
      states:
        OPEN: "1"
        CLOSED: "0"
    exhaust_air_damper_status:
      present_value: "points.exhaust_air_damper_status.present_value"
      states:
        OPEN:
        - "1"
        - "2"
        CLOSED: "1"

US-SEA-BLDG1-GUID:
  type: FACILITIES/BUILDING
  code: US-SEA-BLDG1
```

### Error Message:
```
[ERROR]	Entity DMP_EDM-17-GUID (DMP_EDM-17) defines field /exhaust_air_damper_status has raw value 1 mapped to more than one state: OPEN and CLOSED
```

## Unit Translation Structure

### Description:
Units must define a key with the 4 level unit name and values that link the unit name to the unit coming from the payload.

### Example Bad Config:
```
US-SEA-BLDG1-GUID:
  type: FACILITIES/BUILDING
  code: US-SEA-BLDG1
  translation:
    zone_air_temperature_sensor:
      present_value: "points.temp_1.present_value"
      units:
        values:
          degrees_celsius: "degC"
```

### Error Message:
```
while parsing a mapping
  in "<unicode string>", line 7, column 1:
          units:
    ^ (line: 7)
required key(s) 'key' not found
  in "<unicode string>", line 9, column 1:
              degrees_celsius: degC
    ^ (line: 9)
```

## Value Range without Units

### Description:
A value range for a field can only be provided when it has units defined.

### Example Bad Config:
```
US-SEA-BLDG1-GUID:
  type: FACILITIES/BUILDING
  code: US-SEA-BLDG1
  cloud_device_id: "foobar"
  translation:
    zone_air_temperature_sensor:
      present_value: "points.zone_air_temperature_sensor.present_value"
      value_range: 15,25
```

### Error Message:
```
[ERROR]	Invalid Entity syntax found for this entity: US-SEA-BLDG1-GUID and this content: "{'type': 'FACILITIES/BUILDING', 'code': 'US-SEA-BLDG1', 'cloud_device_id': 'foobar', 'translation': {'zone_air_temperature_sensor': {'present_value': 'points.zone_air_temperature_sensor.present_value', 'value_range': '15,25'}}}" and with error: "A value range cannot be provided without units in the translation for field "zone_air_temperature_sensor"."
ValueError: A value range cannot be provided without units in the translation for field "zone_air_temperature_sensor".
```

## Extra Fields 

### Description:
All fields provided in an entity’s translation must be defined on the DBO entity type (on the general type or one of the abstract types).

### Example Bad Config:
```
CHWS_WDT-17-GUID:
  type: HVAC/CHWS_WDT
  code: CHWS_WDT-17
  cloud_device_id: "foobar"
  translation:
    supply_water_temperature_sensor:
      present_value: "points.supply_water_temperature_sensor.present_value"
      units:
        key: "points.supply_water_temperature_sensor.units"
        values:
          degrees_celsius: "degC"
    return_water_temperature_sensor:
      present_value: "points.return_water_temperature_sensor.present_value"
      units:
        key: "points.return_water_temperature_sensor.units"
        values:
          degrees_celsius: "degC"
    discharge_air_temperature_sensor:
      present_value: "points.discharge_air_temperature_sensor.present_value"
      units:
        key: "points.discharge_air_temperature_sensor.units"
        values:
          degrees_celsius: "degC"

US-SEA-BLDG1-GUID:
  type: FACILITIES/BUILDING
  code: US-SEA-BLDG1
```

### Error Message:
```
[ERROR]	Entity CHWS_WDT-17-GUID (CHWS_WDT-17) translates field "discharge_air_temperature_sensor" which is not defined on the type "CHWS_WDT"
```

## Required Field Omitted

### Description:
All required fields must be listed in the translation for an entity. If the device does not have that field available then it should be included and labeled missing.

### Example Bad Config:
```
# Missing return_water_temperature_sensor

CHWS_WDT-17-GUID:
  type: HVAC/CHWS_WDT
  code: CHWS_WDT-17
  cloud_device_id: "foobar"
  translation:
    supply_water_temperature_sensor:
      present_value: "points.supply_water_temperature_sensor.present_value"
      units:
        key: "pointset.points.supply_water_temperature_sensor.units"
        values:
          degrees_celsius: "degC"
    #flowrate_requirement optional missing
```

### Error Message:
```
[ERROR]	Entity CHWS_WDT-17-GUID (CHWS_WDT-17) missing field "/return_water_temperature_sensor" which is required for assigned type "CHWS_WDT"
```

## Cleared Type

### Description:
Entities cannot be updated to clear required keys, i.e. code, type.

### Example Bad Config:
```
# Bad update specification of entity type and translation. not allowed to be cleared
# note: presence of update_mask implies update operation (if none is specified)

CONFIG_METADATA:
  operation: UPDATE

SDC_EXT-19-GUID:
  code: SDC_EXT-19
  cloud_device_id: "baz"
  etag: a56790
  update_mask:
  - type
```

### Error Message:
```
AttributeError: 'NoneType' object has no attribute 'lower'
```

## Updated Entity Type

### Description:
When updating the type of an existing entity, the existing or updated translation must include and only include the fields defined on the new type.

### Example Bad Config:
```
CONFIG_METADATA:
  operation: UPDATE

SDC_EXT-19-GUID:
  type: HVAC/SDC_EXT
  code: SDC_EXT-19
  cloud_device_id: "baz"
  etag: a56790
  update_mask:
    - type
    - translation
  translation:
    dis_command_should_break_um:
      present_value: "points.present_value"
      units:
        key: "points.units"
        values:
          percent: "%"
```

### Error Message:
```
[ERROR]	Entity SDC_EXT-19-GUID (SDC_EXT-19) translates field "dis_command_should_break_um" which is not defined on the type "SDC_EXT"
```

## Updated Virtual Entity

### Description:
Etags are required on virtual entities when an update is performed.

### Example Bad Config:
```
CONFIG_METADATA:
  operation: UPDATE

VIRTUAL-ENTITY-GUID:
  type: HVAC/CHWS_WDT
  code: VIRTUAL-ENTITY
  links:
    PHYSICAL-ENTITY-NOT-FOUND-GUID:
      return_water_temperature_sensor: return_water_temperature_sensor
      supply_water_temperature_sensor: supply_water_temperature_sensor
      thermal_power_capacity: thermal_power_capacity
      differential_pressure_specification: differential_pressure_specification
  update_mask:
    - links

PHYSICAL-ENTITY-GUID:
  type: HVAC/CHWS_WDT
  code: PHYSICAL-ENTITY
  cloud_device_id: "foobar"
  translation:
    return_water_temperature_sensor:
      present_value: "points.return_water_temperature_sensor.present_value"
      units:
        key: "pointset.return_water_temperature_sensor.units"
        values:
          degrees_celsius: "degC"
    supply_water_temperature_sensor:
      present_value: "points.supply_water_temperature_sensor.present_value"
      units:
        key: "pointset.points.supply_water_temperature_sensor.units"
        values:
          degrees_celsius: "degC"
    thermal_power_capacity:
      present_value: "points.thermal_power_capacity.present_value"
      units:
        key: "pointset.points.thermal_power_capacity.units"
        values:
          kilowatts: "kilowatts"
    differential_pressure_specification:
      present_value: "points.differential_pressure_specification.present_value"
      units:
        key: "pointset.points.differential_pressure_specification.units"
        values:
          pascals: "pascals"

US-SEA-BLDG1-GUID:
  type: FACILITIES/BUILDING
  code: US-SEA-BLDG1
```

### Error Message:
```
while parsing a mapping
  in "<unicode string>", line 1, column 1:
    VIRTUAL-ENTITY-GUID:
     ^ (line: 1)
required key(s) 'etag' not found
  in "<unicode string>", line 11, column 1:
      - links
    ^ (line: 11)
```

## Update Mask with Export

### Description:
Update masks should only be included when the config operation is “Update”. 

### Example Bad Config:
```
CONFIG_METADATA:
  operation: UPDATE

SDC_EXT-19-GUID:
  type: HVAC/SDC_EXT
  code: SDC_EXT-19
  cloud_device_id: "baz"
  etag: a56790
  operation: EXPORT
  update_mask:
    - connections
```

### Error Message:
```
while parsing a mapping
  in "<unicode string>", line 7, column 1:
      update_mask:
    ^ (line: 7)
unexpected key not in schema 'update_mask'
  in "<unicode string>", line 8, column 1:
      - connections
    ^ (line: 8)
```

## Update Mask Values

### Description:
Updates included in the update mask must be listed on their own lines as a hyphenated list.

### Example Bad Config:
```
# Bad Example: This config file is invalid because the update_mask values must be a
# UniqueSeq. 

CONFIG_METADATA:
  operation: UPDATE

SDC_EXT-19-GUID:
  type: HVAC/SDC_EXT
  code: SDC_EXT-19
  cloud_device_id: "baz"
  etag: a56790
  update_mask:
    translation
    - connection
  translation:
    shade_extent_percentage_command:
      present_value: "points.present_value"
      units:
        key: "points.units"
        values:
          percent: "%"
```

### Error Message:
```
when expecting a unique sequence
found arbitrary text
  in "<unicode string>", line 6, column 1:
      update_mask: translation - con ... 
    ^ (line: 6)
```

## Incorrect Metadata

### Description:
Config metadata and operations must be consistent, i.e. no operations would be expected with the config metadata set to initialize.

### Example Bad Config:
```
# Update operation that changes no data in the device (no-op)
CONFIG_METADATA:
  operation: INITIALIZE

US-SEA-BLDG1-GUID:
  operation: ADD
  type: FACILITIES/BUILDING
  code: US-SEA-BLDG1

SDC_EXT-18-GUID:
  code: SDC_EXT-18
  operation: UPDATE
```

### Error Message:
```
while parsing a mapping
unexpected key not in schema 'operation'
  in "<unicode string>", line 6, column 1:
      operation: UPDATE
    ^ (line: 6)
```
