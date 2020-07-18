package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_static_pressure_setpoint;
/**
* Class Rspc 
* Return air static pressure control.
*/
public interface IRspc extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesReturn_air_static_pressure_sensor (IReturn_air_static_pressure_sensor parameter);

	public Set<IReturn_air_static_pressure_sensor> getUsesReturn_air_static_pressure_sensor();

    public void addUsesReturn_air_static_pressure_setpoint (IReturn_air_static_pressure_setpoint parameter);

	public Set<IReturn_air_static_pressure_setpoint> getUsesReturn_air_static_pressure_setpoint();

}