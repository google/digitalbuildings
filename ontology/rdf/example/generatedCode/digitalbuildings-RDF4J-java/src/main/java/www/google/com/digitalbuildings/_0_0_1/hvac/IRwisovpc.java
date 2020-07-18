package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_command;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_valve_percentage_sensor;
/**
* Class Rwisovpc 
* Return water isolation valve percentage monitoring.
*/
public interface IRwisovpc extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesOptionalsRun_command (IRun_command parameter);

	public Set<IRun_command> getUsesOptionalsRun_command();

    public void addUsesReturn_water_valve_percentage_command (IReturn_water_valve_percentage_command parameter);

	public Set<IReturn_water_valve_percentage_command> getUsesReturn_water_valve_percentage_command();

    public void addUsesReturn_water_valve_percentage_sensor (IReturn_water_valve_percentage_sensor parameter);

	public Set<IReturn_water_valve_percentage_sensor> getUsesReturn_water_valve_percentage_sensor();

}