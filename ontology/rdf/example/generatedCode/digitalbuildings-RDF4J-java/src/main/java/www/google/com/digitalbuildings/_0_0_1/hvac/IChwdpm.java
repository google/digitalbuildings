package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_water_differential_pressure_sensor;
/**
* Class Chwdpm 
* Differential pressure monitoring for chilled water.
*/
public interface IChwdpm extends IFunctionality{

	public IRI iri();

    public void addUsesChilled_water_differential_pressure_sensor (IChilled_water_differential_pressure_sensor parameter);

	public Set<IChilled_water_differential_pressure_sensor> getUsesChilled_water_differential_pressure_sensor();

}