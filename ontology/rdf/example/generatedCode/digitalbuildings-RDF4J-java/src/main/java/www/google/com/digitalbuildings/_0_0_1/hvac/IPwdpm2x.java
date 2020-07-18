package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_water_differential_pressure_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_water_differential_pressure_sensor_2;
/**
* Class Pwdpm2x 
* Differential pressure monitoring for 2 process water headers.
*/
public interface IPwdpm2x extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesProcess_water_differential_pressure_sensor_1 (IProcess_water_differential_pressure_sensor_1 parameter);

	public Set<IProcess_water_differential_pressure_sensor_1> getUsesProcess_water_differential_pressure_sensor_1();

    public void addUsesProcess_water_differential_pressure_sensor_2 (IProcess_water_differential_pressure_sensor_2 parameter);

	public Set<IProcess_water_differential_pressure_sensor_2> getUsesProcess_water_differential_pressure_sensor_2();

}