package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import www.google.com.digitalbuildings._0_0_1.fields.IFlowrate_requirement;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IEfficiency_percentage_specification;
import www.google.com.digitalbuildings._0_0_1.fields.ICirculation_pump_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_status;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_input_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IPower_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IPower_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICirculation_pump_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_command;
import www.google.com.digitalbuildings._0_0_1.fields.ICurrent_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IPowerfactor_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IFlowrate_capacity;
/**
* Class Blr_ss_swtc_cpc 
* Simple boiler with onboard circulation pump.
*/
public interface IBlr_ss_swtc_cpc extends ICpc, IBlr, ISs, ISwtc{

	public IRI iri();

}