package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IFlowrate_sensor;
/**
* Class Wfrm 
* Water flowrate monitoring.
*/
public interface IWfrm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesFlowrate_sensor (IFlowrate_sensor parameter);

	public Set<IFlowrate_sensor> getUsesFlowrate_sensor();

}