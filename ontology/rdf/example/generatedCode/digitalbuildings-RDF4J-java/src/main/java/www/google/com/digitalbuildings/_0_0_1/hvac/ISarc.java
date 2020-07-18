package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IControl;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IPressurization_request_count;
/**
* Class Sarc 
* AHU supply air reset control.
*/
public interface ISarc extends IFunctionality, IControl{

	public IRI iri();

    public void addUsesCooling_request_count (ICooling_request_count parameter);

	public Set<ICooling_request_count> getUsesCooling_request_count();

    public void addUsesPressurization_request_count (IPressurization_request_count parameter);

	public Set<IPressurization_request_count> getUsesPressurization_request_count();

    public void addUsesSupply_air_static_pressure_setpoint (ISupply_air_static_pressure_setpoint parameter);

	public Set<ISupply_air_static_pressure_setpoint> getUsesSupply_air_static_pressure_setpoint();

    public void addUsesSupply_air_temperature_setpoint (ISupply_air_temperature_setpoint parameter);

	public Set<ISupply_air_temperature_setpoint> getUsesSupply_air_temperature_setpoint();

    public void addUsesOptionalsHeating_request_count (IHeating_request_count parameter);

	public Set<IHeating_request_count> getUsesOptionalsHeating_request_count();

    public void addUsesOptionalsSupply_air_flowrate_sensor (ISupply_air_flowrate_sensor parameter);

	public Set<ISupply_air_flowrate_sensor> getUsesOptionalsSupply_air_flowrate_sensor();

}