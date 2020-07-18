package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_co2_concentration_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_co2_concentration_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_co2_concentration_sensor_1;
/**
* Class Co2c2x 
* Carbon dioxide control with dual zone sensors.
*/
public interface ICo2c2x extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesZone_air_co2_concentration_sensor_1 (IZone_air_co2_concentration_sensor_1 parameter);

	public Set<IZone_air_co2_concentration_sensor_1> getUsesZone_air_co2_concentration_sensor_1();

    public void addUsesZone_air_co2_concentration_sensor_2 (IZone_air_co2_concentration_sensor_2 parameter);

	public Set<IZone_air_co2_concentration_sensor_2> getUsesZone_air_co2_concentration_sensor_2();

    public void addUsesZone_air_co2_concentration_setpoint (IZone_air_co2_concentration_setpoint parameter);

	public Set<IZone_air_co2_concentration_setpoint> getUsesZone_air_co2_concentration_setpoint();

}