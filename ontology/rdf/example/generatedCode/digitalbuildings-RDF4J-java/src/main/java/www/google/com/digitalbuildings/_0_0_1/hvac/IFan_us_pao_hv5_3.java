package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_damper_percentage_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_damper_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_damper_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_static_pressure_setpoint;
/**
* Class Fan_us_pao_hv5_3 
* Non-standard type for HV5
*/
public interface IFan_us_pao_hv5_3 extends IFan_ss_vsc_bspc{

	public IRI iri();

    public void addUsesExhaust_air_damper_percentage_command_1 (IExhaust_air_damper_percentage_command_1 parameter);

	public Set<IExhaust_air_damper_percentage_command_1> getUsesExhaust_air_damper_percentage_command_1();

    public void addUsesExhaust_air_damper_percentage_command_2 (IExhaust_air_damper_percentage_command_2 parameter);

	public Set<IExhaust_air_damper_percentage_command_2> getUsesExhaust_air_damper_percentage_command_2();

    public void addUsesExhaust_air_damper_percentage_command_3 (IExhaust_air_damper_percentage_command_3 parameter);

	public Set<IExhaust_air_damper_percentage_command_3> getUsesExhaust_air_damper_percentage_command_3();

    public void addUsesExhaust_air_static_pressure_sensor (IExhaust_air_static_pressure_sensor parameter);

	public Set<IExhaust_air_static_pressure_sensor> getUsesExhaust_air_static_pressure_sensor();

    public void addUsesExhaust_air_static_pressure_setpoint (IExhaust_air_static_pressure_setpoint parameter);

	public Set<IExhaust_air_static_pressure_setpoint> getUsesExhaust_air_static_pressure_setpoint();

}