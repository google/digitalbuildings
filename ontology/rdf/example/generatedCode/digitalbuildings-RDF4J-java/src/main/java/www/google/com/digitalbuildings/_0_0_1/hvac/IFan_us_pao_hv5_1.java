package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_damper_percentage_command;
/**
* Class Fan_us_pao_hv5_1 
* Non-standard type for HV5
*/
public interface IFan_us_pao_hv5_1 extends IFan_ss_vsc_bspc{

	public IRI iri();

    public void addUsesExhaust_air_damper_percentage_command (IExhaust_air_damper_percentage_command parameter);

	public Set<IExhaust_air_damper_percentage_command> getUsesExhaust_air_damper_percentage_command();

    public void addUsesExhaust_air_static_pressure_sensor (IExhaust_air_static_pressure_sensor parameter);

	public Set<IExhaust_air_static_pressure_sensor> getUsesExhaust_air_static_pressure_sensor();

    public void addUsesExhaust_air_static_pressure_setpoint (IExhaust_air_static_pressure_setpoint parameter);

	public Set<IExhaust_air_static_pressure_setpoint> getUsesExhaust_air_static_pressure_setpoint();

}