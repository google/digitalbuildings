
# Ontology Mapper

## Overview

This library is meant to allow for easy exploration of the ontology. It allows a user to ask questions of the ontology related to types, fields, and subfields. Since entity inheritance is widely used, and since optionality of fields may be different from parent to parent, it can be difficult to know what fields exist on a given type and what the optionality oft hose fields are. This tool provides methods for easily exploring the constructed ontology and matching given sets of fields to types within the ontology.

## Some Important Notes
1. This tool is intended to be used as part of an interactive Python session or as part of a script.
2. This tool only allows comparison for canonical types (it will not match to anything where is_abstract=true or is_canonical=false)

## Classes

### ontology_match_lib.Ontology
An object representing the entire ontology (that is, the fields, subfields, and types fully expanded from their inheritance).

#### Methods
**Ontology.refresh()** Refreshes the ontology based on any recent changes within the ontologgy directory.
- Parameters: 
	- *none*
- Returns: 
	- *none*

**Ontology.get_all_namespaces()** 
Gets all the namespaces within the ontology.
- Parameters:
	- *none*
- Returns: 	
	- *list:* A list of all the namespaces within the ontology.

**Ontology.get_all_types(namespace)**
Get all types within a specified namespace.
- Parameters:
	- **namespace:** *string:* The name of the namespace to return types for.
- Returns:
	- *list:* The names of all types within the namespace.

**Ontology.compare_to_type(fields,namespace,type_name,show_optional=False)**
Compares a set of fields to a specific type.
- Parameters:
	- **fields:** *list, set:* A set or list of fields which constitute a real device.
	- **namespace:** *string:* The name of the namespace to return types for.
	- **type_name:** *string:* The name of the canonical type
- Returns:
	- *stdout:* A printout of the exact comparison between two types. 

**Ontology.find_best_fit_type(fields,namespace,general_type,real_entities_list=[])**:
Find the best fitting type among all types within a namespace and general type group.
- Parameters:
	- **fields:** *list, set:* A set or list of fields which constitute a real device.
	- **namespace:** *string:* The name of the namespace to return types for.
	- **general_type:** *string:* The first part of the entity name (e.g. 'FCU' from 'FCU_DFSS_DFVSC_RTC_CHWRC'). NOTE: this will be changed in the future to support actual inheritance.
	- **real_entities_list (optional):** *list:* Provide a list of the real entities that this type apply to so they can be attached to the Match object.
- Returns:
	- *Match:* a Match object containing particular details of the match.

### ontology_match_lib.Match
An object representing the match between a set of fields and a canonical type.

#### Attributes

**Match.match_type** *string* The match type, which will be one of the following:
	1. **EXACT:** all canonical required fields covered and all real type fields covered. 
	2. **CLOSE:** all required fields are covered but not all real type fields are covered.
	3. **INCOMPLETE:** all real type fields covered but not all canonical required fields covered. 
	4. **NOT:** neither real types nor required fields are completely covered. 
**Match.real_type_fields**
**Match.ont_type_fields**
**Match.ont_type_name**
**Match.unmatched_real**
**Match.unmatched_required**

#### Methods

**Match.print_comparison(show_optional=False)
Prints the comparison made in the Match object, including missing and matched fields, and the match type.
- Parameters:
	- **show_optional (optional):** *bool:* A flag for whether to print optional fields (note if set to false, some optional fields may be displayed but only if they are in the actual entity's field list).
- Returns:
	- *stdout:* a printout of the comparison.

## Examples

A few key examples:

1. Print out the difference between a set of fields and the specified canonical type.
```
from ontology_match_lib import Ontology
from ontology_match_lib import PrettyPrint

ont = Ontology()

field_set = [
	'run_command',
	'supply_air_flowrate_sensor',
	'zone_air_co2_concentration_sensor', 
	'supply_air_damper_percentage_command', 
	'zone_air_cooling_temperature_setpoint', 
	'supply_air_flowrate_setpoint', 
	'zone_air_heating_temperature_setpoint', 
	'zone_air_co2_concentration_setpoint', 
	'zone_air_temperature_sensor'
]

ont.compare_to_type(field_set,'HVAC','VAV_SD_DSP_CO2C')
```

2. Get the best fit for a given set of fields within a namespace and with a speficic generral type.


```
from ontology_match_lib import Ontology
from ontology_match_lib import 

ont = Ontology()

real_fields_exact = {
	'supply_air_flowrate_sensor',
	'zone_air_co2_concentration_sensor', 
	'supply_air_damper_percentage_command', 
	'zone_air_cooling_temperature_setpoint', 
	'supply_air_flowrate_setpoint', 
	'zone_air_heating_temperature_setpoint', 
	'run_command', 
	'zone_air_co2_concentration_setpoint', 
	'zone_air_temperature_sensor'
}

fit = ont.find_best_fit_type(real_fields_exact,'HVAC','VAV')
fit.print_comparison()

real_fields_incomplete = {
	'zone_air_co2_concentration_sensor', 
	'zone_air_co2_concentration_setpoint', 
	'supply_air_damper_percentage_command', 
	'supply_air_flowrate_setpoint', 
	'zone_air_cooling_temperature_setpoint', 
	'zone_air_heating_temperature_setpoint', 
	'zone_air_temperature_sensor',
	'run_command' 
}

fit = ont.find_best_fit_type(real_fields_incomplete,'HVAC','VAV')
fit.print_comparison()
```

