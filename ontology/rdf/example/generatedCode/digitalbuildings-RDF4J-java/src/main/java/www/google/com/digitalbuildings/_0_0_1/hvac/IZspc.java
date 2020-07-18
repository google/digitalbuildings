package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_static_pressure_sensor;
/**
* Class Zspc 
* Zone static pressure control.
*/
public interface IZspc extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesZone_air_static_pressure_sensor (IZone_air_static_pressure_sensor parameter);

	public Set<IZone_air_static_pressure_sensor> getUsesZone_air_static_pressure_sensor();

    public void addUsesZone_air_static_pressure_setpoint (IZone_air_static_pressure_setpoint parameter);

	public Set<IZone_air_static_pressure_setpoint> getUsesZone_air_static_pressure_setpoint();

}