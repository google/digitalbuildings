package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_co_concentration_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_co_concentration_sensor;
/**
* Class Fan_ss_coc 
* On/off fan with carbon monoxide control.
*/
public interface IFan_ss_coc extends IFan, ICoc, ISs{

	public IRI iri();

}