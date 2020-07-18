package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_water_flowrate_sensor;
/**
* Class Pwfrm 
* Flowrate monitoring for process water.
*/
public interface IPwfrm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesProcess_water_flowrate_sensor (IProcess_water_flowrate_sensor parameter);

	public Set<IProcess_water_flowrate_sensor> getUsesProcess_water_flowrate_sensor();

}