package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IFilter_differential_pressure_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.IFilter_differential_pressure_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.IFilter_differential_pressure_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IFilter_differential_pressure_sensor_1;
/**
* Class Fdpm4x 
* Filter pressure monitoring (4 sensors).
*/
public interface IFdpm4x extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesFilter_differential_pressure_sensor_1 (IFilter_differential_pressure_sensor_1 parameter);

	public Set<IFilter_differential_pressure_sensor_1> getUsesFilter_differential_pressure_sensor_1();

    public void addUsesFilter_differential_pressure_sensor_2 (IFilter_differential_pressure_sensor_2 parameter);

	public Set<IFilter_differential_pressure_sensor_2> getUsesFilter_differential_pressure_sensor_2();

    public void addUsesFilter_differential_pressure_sensor_3 (IFilter_differential_pressure_sensor_3 parameter);

	public Set<IFilter_differential_pressure_sensor_3> getUsesFilter_differential_pressure_sensor_3();

    public void addUsesFilter_differential_pressure_sensor_4 (IFilter_differential_pressure_sensor_4 parameter);

	public Set<IFilter_differential_pressure_sensor_4> getUsesFilter_differential_pressure_sensor_4();

}