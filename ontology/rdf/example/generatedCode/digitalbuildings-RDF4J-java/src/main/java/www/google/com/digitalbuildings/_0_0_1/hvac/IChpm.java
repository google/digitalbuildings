package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IDifferential_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICondenser_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IEvaporator_pressure_sensor;
/**
* Class Chpm 
* Chiller pressure monitoring.
*/
public interface IChpm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesCondenser_pressure_sensor (ICondenser_pressure_sensor parameter);

	public Set<ICondenser_pressure_sensor> getUsesCondenser_pressure_sensor();

    public void addUsesDifferential_pressure_sensor (IDifferential_pressure_sensor parameter);

	public Set<IDifferential_pressure_sensor> getUsesDifferential_pressure_sensor();

    public void addUsesEvaporator_pressure_sensor (IEvaporator_pressure_sensor parameter);

	public Set<IEvaporator_pressure_sensor> getUsesEvaporator_pressure_sensor();

}