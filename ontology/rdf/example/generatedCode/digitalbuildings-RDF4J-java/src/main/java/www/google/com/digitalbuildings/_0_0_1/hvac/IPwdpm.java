package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_water_differential_pressure_sensor;
/**
* Class Pwdpm 
* Differential pressure monitoring for process water.
*/
public interface IPwdpm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesProcess_water_differential_pressure_sensor (IProcess_water_differential_pressure_sensor parameter);

	public Set<IProcess_water_differential_pressure_sensor> getUsesProcess_water_differential_pressure_sensor();

}