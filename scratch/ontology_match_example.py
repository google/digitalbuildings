
from ontology_match_lib import Ontology
from ontology_match_lib import PrettyPrint


# Initialize the ontology object, of which you will ask questions about real types based on field information.

ont = Ontology()

ont.refresh()

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



real_fields_none = {
	'return_air_temperature_sensor',
	'discharge_fan_run_command',
	'supply_air_damper_percentage_command'
}
fit = ont.find_best_fit_type(real_fields_none,'HVAC','VAV')
fit.print_comparison(False)



# Say that you have a type that you think your field set should match: there is a call you can make to 
# the ontology and compare a specific set of points directly to a type you think should match to find
# the differences between. 

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



# Set up a loop to check that all the types for a given set of fields and allows you to define a new one that covers the new type.
# Grab all the unique sets of fields and compare them all to the ontology.
fieldtypes = {
	'DMP_SDBPC_DMM':['device_mode', 'supply_air_damper_percentage_command', 'supply_air_damper_percentage_sensor', 'supply_air_flowrate_sensor', 'supply_air_static_pressure_sensor', 'supply_air_static_pressure_setpoint'],
	'FCU_DFSS_DFVSC_RTC_CHWRC_FDPM_DMM':['chilled_water_flowrate_sensor', 'chilled_water_valve_percentage_command', 'chilled_water_valve_percentage_sensor', 'device_mode', 'discharge_air_static_pressure_sensor', 'discharge_air_temperature_sensor', 'discharge_fan_run_command', 'discharge_fan_run_status', 'discharge_fan_speed_percentage_command', 'filter_differential_pressure_sensor', 'return_air_temperature_sensor', 'return_air_temperature_setpoint'],
	'FCU_DFSS_DFVSC_ZTC_CHWZTC_FDPM_DMM':['chilled_water_flowrate_sensor', 'chilled_water_valve_percentage_command', 'chilled_water_valve_percentage_sensor', 'device_mode', 'discharge_air_static_pressure_sensor', 'discharge_air_temperature_sensor', 'discharge_fan_run_command', 'discharge_fan_run_status', 'discharge_fan_speed_percentage_command', 'filter_differential_pressure_sensor', 'return_air_temperature_sensor', 'zone_air_temperature_sensor', 'zone_air_temperature_setpoint'],
	'FCU_DFSS_DFVSC_ZTC_ZHC_CHWDC_FDPM_DMM':['chilled_water_flowrate_sensor', 'chilled_water_valve_percentage_command', 'chilled_water_valve_percentage_sensor', 'device_mode', 'discharge_air_static_pressure_sensor', 'discharge_air_temperature_sensor', 'discharge_air_temperature_setpoint', 'discharge_fan_run_command', 'discharge_fan_run_status', 'discharge_fan_speed_percentage_command', 'filter_differential_pressure_sensor', 'return_air_temperature_sensor', 'zone_air_relative_humidity_sensor', 'zone_air_relative_humidity_setpoint', 'zone_air_temperature_sensor', 'zone_air_temperature_setpoint'],
	'FCU_DFSS_DFVSC_RTC_CHWRC_HWRC_FDPM_DMM':['chilled_water_flowrate_sensor', 'chilled_water_valve_percentage_command', 'chilled_water_valve_percentage_sensor', 'device_mode', 'discharge_air_static_pressure_sensor', 'discharge_air_temperature_sensor', 'discharge_fan_run_command', 'discharge_fan_run_status', 'discharge_fan_speed_percentage_command', 'filter_differential_pressure_sensor', 'heating_water_flowrate_sensor', 'heating_water_valve_percentage_command', 'heating_water_valve_percentage_sensor', 'return_air_temperature_sensor', 'return_air_temperature_setpoint'],
	'FCU_DFSS_DFVSC_ZTC_CHWDC_HWDC_FDPM_DMM':['chilled_water_flowrate_sensor', 'chilled_water_valve_percentage_command', 'chilled_water_valve_percentage_sensor', 'device_mode', 'discharge_air_static_pressure_sensor', 'discharge_air_temperature_sensor', 'discharge_air_temperature_setpoint', 'discharge_fan_run_command', 'discharge_fan_run_status', 'discharge_fan_speed_percentage_command', 'filter_differential_pressure_sensor', 'heating_water_flowrate_sensor', 'heating_water_valve_percentage_command', 'heating_water_valve_percentage_sensor', 'return_air_temperature_sensor', 'zone_air_temperature_sensor', 'zone_air_temperature_setpoint'],
	'FCU_DFSS_DFVSC_ZTC_CHWZTC_FDPM_CO2M_DMM':['chilled_water_flowrate_sensor', 'chilled_water_valve_percentage_command', 'chilled_water_valve_percentage_sensor', 'device_mode', 'discharge_air_static_pressure_sensor', 'discharge_air_temperature_sensor', 'discharge_fan_run_command', 'discharge_fan_run_status', 'discharge_fan_speed_percentage_command', 'filter_differential_pressure_sensor', 'return_air_temperature_sensor', 'zone_air_co2_concentration_sensor', 'zone_air_relative_humidity_sensor', 'zone_air_temperature_sensor', 'zone_air_temperature_setpoint'],
	'FCU_DFSS_DFVSC_ZTC_CHWZTC_HWZTC_FDPM_DMM':['chilled_water_flowrate_sensor', 'chilled_water_valve_percentage_command', 'chilled_water_valve_percentage_sensor', 'device_mode', 'discharge_air_static_pressure_sensor', 'discharge_air_temperature_sensor', 'discharge_fan_run_command', 'discharge_fan_run_status', 'discharge_fan_speed_percentage_command', 'filter_differential_pressure_sensor', 'heating_water_flowrate_sensor', 'heating_water_valve_percentage_command', 'heating_water_valve_percentage_sensor', 'return_air_temperature_sensor', 'zone_air_temperature_sensor', 'zone_air_temperature_setpoint'],
	'FCU_DFSS_DFVSC_ZTC_ZHC_CHWDC_HWDC_FDPM_DMM':['chilled_water_flowrate_sensor', 'chilled_water_valve_percentage_command', 'chilled_water_valve_percentage_sensor', 'device_mode', 'discharge_air_temperature_sensor', 'discharge_air_temperature_setpoint', 'discharge_fan_run_command', 'discharge_fan_run_status', 'discharge_fan_speed_percentage_command', 'filter_differential_pressure_sensor', 'heating_water_flowrate_sensor', 'heating_water_valve_percentage_command', 'heating_water_valve_percentage_sensor', 'return_air_temperature_sensor', 'zone_air_relative_humidity_sensor', 'zone_air_relative_humidity_setpoint', 'zone_air_temperature_sensor', 'zone_air_temperature_setpoint'],
	'FCU_DFSS_DFVSC_ZTC_CHWZTC_HWZTC_FDPM_CO2M_DMM':['chilled_water_flowrate_sensor', 'chilled_water_valve_percentage_command', 'chilled_water_valve_percentage_sensor', 'device_mode', 'discharge_air_static_pressure_sensor', 'discharge_air_temperature_sensor', 'discharge_fan_run_command', 'discharge_fan_run_status', 'discharge_fan_speed_percentage_command', 'filter_differential_pressure_sensor', 'heating_water_flowrate_sensor', 'heating_water_valve_percentage_command', 'heating_water_valve_percentage_sensor', 'return_air_temperature_sensor', 'zone_air_co2_concentration_sensor', 'zone_air_relative_humidity_sensor', 'zone_air_temperature_sensor', 'zone_air_temperature_setpoint'],
	'SENSOR_ZTM_ZHM_CO2M':['zone_air_co2_concentration_sensor', 'zone_air_relative_humidity_sensor', 'zone_air_temperature_sensor'],
	'VAV_ED_DMM':['device_mode', 'exhaust_air_damper_percentage_command', 'exhaust_air_damper_percentage_sensor', 'exhaust_air_flowrate_sensor', 'exhaust_air_flowrate_setpoint', 'exhaust_air_static_pressure_sensor'],
	'VAV_PDSCV_CO2C_VOCPC_ZHM_DMM':['device_mode', 'supply_air_damper_percentage_command', 'supply_air_damper_percentage_sensor', 'zone_air_co2_concentration_sensor', 'zone_air_co2_concentration_setpoint', 'zone_air_relative_humidity_sensor', 'zone_air_voc_percentage_sensor', 'zone_air_voc_percentage_setpoint'],
	'VLV_CHWVM_RTM_DTM':['chilled_water_flowrate_sensor', 'chilled_water_valve_percentage_command', 'chilled_water_valve_percentage_sensor', 'discharge_air_temperature_sensor', 'return_air_temperature_sensor'],
	'VLV_HWVM':['heating_water_flowrate_sensor', 'heating_water_valve_percentage_command', 'heating_water_valve_percentage_sensor']
}


namespace = 'HVAC'

for device in fieldtypes:
	gentype = device.split('_')[0]
	fit = ont.find_best_fit_type(fieldtypes[device],namespace,gentype)

	print(namespace, device)
	fit.print_comparison(False)
