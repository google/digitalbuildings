package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.IDifferential_pressure_sensor;
/**
* Class Wdpm 
* Differential pressure monitoring.
*/
public interface IWdpm extends IFunctionality{

	public IRI iri();

    public void addUsesDifferential_pressure_sensor (IDifferential_pressure_sensor parameter);

	public Set<IDifferential_pressure_sensor> getUsesDifferential_pressure_sensor();

}