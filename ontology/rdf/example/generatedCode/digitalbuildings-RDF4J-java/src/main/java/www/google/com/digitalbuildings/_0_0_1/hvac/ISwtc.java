package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_temperature_setpoint;
/**
* Class Swtc 
* Supply water temperature control.
*/
public interface ISwtc extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesOptionalsCooling_request_count (ICooling_request_count parameter);

	public Set<ICooling_request_count> getUsesOptionalsCooling_request_count();

    public void addUsesOptionalsHeating_request_count (IHeating_request_count parameter);

	public Set<IHeating_request_count> getUsesOptionalsHeating_request_count();

    public void addUsesOptionalsReturn_water_temperature_sensor (IReturn_water_temperature_sensor parameter);

	public Set<IReturn_water_temperature_sensor> getUsesOptionalsReturn_water_temperature_sensor();

    public void addUsesOptionalsRun_command (IRun_command parameter);

	public Set<IRun_command> getUsesOptionalsRun_command();

    public void addUsesSupply_water_temperature_sensor (ISupply_water_temperature_sensor parameter);

	public Set<ISupply_water_temperature_sensor> getUsesSupply_water_temperature_sensor();

    public void addUsesSupply_water_temperature_setpoint (ISupply_water_temperature_setpoint parameter);

	public Set<ISupply_water_temperature_setpoint> getUsesSupply_water_temperature_setpoint();

}