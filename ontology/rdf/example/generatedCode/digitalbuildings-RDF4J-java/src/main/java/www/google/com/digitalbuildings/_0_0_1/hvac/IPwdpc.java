package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_water_differential_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_water_differential_pressure_sensor;
/**
* Class Pwdpc 
* Process water differential pressure control.
*/
public interface IPwdpc extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesProcess_water_differential_pressure_sensor (IProcess_water_differential_pressure_sensor parameter);

	public Set<IProcess_water_differential_pressure_sensor> getUsesProcess_water_differential_pressure_sensor();

    public void addUsesProcess_water_differential_pressure_setpoint (IProcess_water_differential_pressure_setpoint parameter);

	public Set<IProcess_water_differential_pressure_setpoint> getUsesProcess_water_differential_pressure_setpoint();

}