package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_cooling_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_heating_temperature_setpoint;
/**
* Class Stdspc 
* Supply temperature control dual setpoint.
*/
public interface IStdspc extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesOptionalsCooling_request_count (ICooling_request_count parameter);

	public Set<ICooling_request_count> getUsesOptionalsCooling_request_count();

    public void addUsesOptionalsHeating_request_count (IHeating_request_count parameter);

	public Set<IHeating_request_count> getUsesOptionalsHeating_request_count();

    public void addUsesSupply_air_cooling_temperature_setpoint (ISupply_air_cooling_temperature_setpoint parameter);

	public Set<ISupply_air_cooling_temperature_setpoint> getUsesSupply_air_cooling_temperature_setpoint();

    public void addUsesSupply_air_heating_temperature_setpoint (ISupply_air_heating_temperature_setpoint parameter);

	public Set<ISupply_air_heating_temperature_setpoint> getUsesSupply_air_heating_temperature_setpoint();

    public void addUsesSupply_air_temperature_sensor (ISupply_air_temperature_sensor parameter);

	public Set<ISupply_air_temperature_sensor> getUsesSupply_air_temperature_sensor();

}