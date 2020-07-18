package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import www.google.com.digitalbuildings._0_0_1.fields.IEconomizer_mode;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_refrigerant_concentration_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_flowrate_requirement;
/**
* Class Fan_ss_refm_ztm 
* Refrigerant level and zone temp monitoring fan.
*/
public interface IFan_ss_refm_ztm extends IZtm, IRefm, IFan, ISs{

	public IRI iri();

}