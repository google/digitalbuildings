package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_specificenthalpy_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_dewpoint_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_wetbulb_temperature_sensor;
/**
* Class Oa 
* Basic weather station (drybulb temp and humidity).
*/
public interface IOa extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesOptionalsOutside_air_dewpoint_temperature_sensor (IOutside_air_dewpoint_temperature_sensor parameter);

	public Set<IOutside_air_dewpoint_temperature_sensor> getUsesOptionalsOutside_air_dewpoint_temperature_sensor();

    public void addUsesOptionalsOutside_air_relative_humidity_sensor (IOutside_air_relative_humidity_sensor parameter);

	public Set<IOutside_air_relative_humidity_sensor> getUsesOptionalsOutside_air_relative_humidity_sensor();

    public void addUsesOptionalsOutside_air_specificenthalpy_sensor (IOutside_air_specificenthalpy_sensor parameter);

	public Set<IOutside_air_specificenthalpy_sensor> getUsesOptionalsOutside_air_specificenthalpy_sensor();

    public void addUsesOptionalsOutside_air_wetbulb_temperature_sensor (IOutside_air_wetbulb_temperature_sensor parameter);

	public Set<IOutside_air_wetbulb_temperature_sensor> getUsesOptionalsOutside_air_wetbulb_temperature_sensor();

    public void addUsesOutside_air_temperature_sensor (IOutside_air_temperature_sensor parameter);

	public Set<IOutside_air_temperature_sensor> getUsesOutside_air_temperature_sensor();

}