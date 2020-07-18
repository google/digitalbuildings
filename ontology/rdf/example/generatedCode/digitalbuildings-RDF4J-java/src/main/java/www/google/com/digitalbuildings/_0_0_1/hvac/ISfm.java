package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_sensor;
/**
* Class Sfm 
* Supply air flow monitoring.
*/
public interface ISfm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesSupply_air_flowrate_sensor (ISupply_air_flowrate_sensor parameter);

	public Set<ISupply_air_flowrate_sensor> getUsesSupply_air_flowrate_sensor();

}