package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_command;
/**
* Class Hws_rwtc_wdpc 
* Simple heating water system with return temp control and differential pressure control.
*/
public interface IHws_rwtc_wdpc extends IRwtc, IHws, IWdpc{

	public IRI iri();

}