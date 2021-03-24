
from ontology_match_lib import Ontology



# Initialize the ontology object, of which you will ask questions about real types based on field information.

ont = Ontology()


# Ask the ontology for all its namespaces
namespaces = ont.get_all_namespaces()

print('GET ALL THE NAMESPACES')
print(namespaces)
print('-'*100,'\n')

# Ask the ontology for all types in a given namespace
types = ont.get_all_types('LIGHTING')

print('GET ALL THE TYPES IN LIGHTING NAMESPACE')
print(types)
print('-'*100,'\n')

# Ask the ontology for all fields on a type in a specific namespace.

type_fields_light = ont.get_type_fields('LIGHTING','LT_SS')

print('GET ALL FIELDS FOR LIGHTING TYPE LT_SS')
print(type_fields_light)
print('-'*100,'\n')


type_fields_vav = ont.get_type_fields('HVAC','VAV_SD_DSP')

print('GET ALL FIELDS FOR HVAC TYPE VAV_SD_DSP')
print(type_fields_vav)
print('-'*100,'\n')


# Ask the ontology for the type that best fits a set of fields.
# A field set will either match the ontology in one of four ways:
# - EXACT (provided field set matches a canonical field set)
# - CLOSE (provided field set is a close superset of a canonical field set)
# - INCOMPLETE (provided field set is a close subset of a canonical field set)
# - NONE (provided field set is not a close subset or superset, or is not a strict sub- or superset)

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
fit.print_comparison(False)
print('-'*100,'\n')


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
fit.print_comparison(False)
print('-'*100,'\n')


real_fields_close = {
	'return_air_temperature_sensor',
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

fit = ont.find_best_fit_type(real_fields_close,'HVAC','VAV')
fit.print_comparison(False)
print('-'*100,'\n')


real_fields_none = {
	'return_air_temperature_sensor',
	'discharge_fan_run_command',
	'supply_air_damper_percentage_command'
}
fit = ont.find_best_fit_type(real_fields_none,'HVAC','VAV')
fit.print_comparison(False)






