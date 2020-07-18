package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.IDifferential_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IPressurization_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.IDifferential_pressure_setpoint;
/**
* Class Wdpc 
* Differential pressure control in whichever system.
*/
public interface IWdpc extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesDifferential_pressure_sensor (IDifferential_pressure_sensor parameter);

	public Set<IDifferential_pressure_sensor> getUsesDifferential_pressure_sensor();

    public void addUsesDifferential_pressure_setpoint (IDifferential_pressure_setpoint parameter);

	public Set<IDifferential_pressure_setpoint> getUsesDifferential_pressure_setpoint();

    public void addUsesOptionalsPressurization_request_count (IPressurization_request_count parameter);

	public Set<IPressurization_request_count> getUsesOptionalsPressurization_request_count();

}