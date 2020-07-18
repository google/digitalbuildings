package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_command;
/**
* Class Rwtc 
* Return water temperature control.
*/
public interface IRwtc extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesOptionalsRun_command (IRun_command parameter);

	public Set<IRun_command> getUsesOptionalsRun_command();

    public void addUsesOptionalsSupply_water_temperature_sensor (ISupply_water_temperature_sensor parameter);

	public Set<ISupply_water_temperature_sensor> getUsesOptionalsSupply_water_temperature_sensor();

    public void addUsesReturn_water_temperature_sensor (IReturn_water_temperature_sensor parameter);

	public Set<IReturn_water_temperature_sensor> getUsesReturn_water_temperature_sensor();

    public void addUsesReturn_water_temperature_setpoint (IReturn_water_temperature_setpoint parameter);

	public Set<IReturn_water_temperature_setpoint> getUsesReturn_water_temperature_setpoint();

}