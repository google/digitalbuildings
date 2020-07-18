package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IFilter_differential_pressure_sensor;
/**
* Class Fdpm 
* Filter pressure monitoring.
*/
public interface IFdpm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesFilter_differential_pressure_sensor (IFilter_differential_pressure_sensor parameter);

	public Set<IFilter_differential_pressure_sensor> getUsesFilter_differential_pressure_sensor();

}