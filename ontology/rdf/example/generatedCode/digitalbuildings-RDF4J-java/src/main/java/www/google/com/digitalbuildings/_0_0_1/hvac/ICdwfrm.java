package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_water_flowrate_sensor;
/**
* Class Cdwfrm 
* Condenser water flowrate monitoring.
*/
public interface ICdwfrm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesCondensing_water_flowrate_sensor (ICondensing_water_flowrate_sensor parameter);

	public Set<ICondensing_water_flowrate_sensor> getUsesCondensing_water_flowrate_sensor();

}