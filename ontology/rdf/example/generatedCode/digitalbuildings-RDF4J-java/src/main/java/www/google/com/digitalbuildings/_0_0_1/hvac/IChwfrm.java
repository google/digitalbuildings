package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_water_flowrate_sensor;
/**
* Class Chwfrm 
* Chilled water flowrate monitoring.
*/
public interface IChwfrm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesChilled_water_flowrate_sensor (IChilled_water_flowrate_sensor parameter);

	public Set<IChilled_water_flowrate_sensor> getUsesChilled_water_flowrate_sensor();

}