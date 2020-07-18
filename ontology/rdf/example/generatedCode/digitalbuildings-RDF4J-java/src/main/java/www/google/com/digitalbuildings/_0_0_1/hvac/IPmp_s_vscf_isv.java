package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IMixing_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_supply_water_temperature_setpoint;
/**
* Class Pmp_s_vscf_isv 
* One-off pump that performs chilled water blending.
*/
public interface IPmp_s_vscf_isv extends IPmp_ss_vsc{

	public IRI iri();

    public void addUsesMixing_valve_percentage_command (IMixing_valve_percentage_command parameter);

	public Set<IMixing_valve_percentage_command> getUsesMixing_valve_percentage_command();

}