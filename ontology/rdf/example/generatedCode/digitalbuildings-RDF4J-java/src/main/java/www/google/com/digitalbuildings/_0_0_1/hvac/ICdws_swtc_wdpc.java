package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import www.google.com.digitalbuildings._0_0_1.fields.IDifferential_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IPressurization_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.IDifferential_pressure_setpoint;
/**
* Class Cdws_swtc_wdpc 
* Condenser water system with supply temp and differential pressure control.
*/
public interface ICdws_swtc_wdpc extends ICdws, IWdpc, ISwtc{

	public IRI iri();

}