package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_damper_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_damper_percentage_command;
/**
* Class Edpm 
* Exhaust air damper percentage monitoring.
*/
public interface IEdpm extends IFunctionality{

	public IRI iri();

    public void addUsesExhaust_air_damper_percentage_command (IExhaust_air_damper_percentage_command parameter);

	public Set<IExhaust_air_damper_percentage_command> getUsesExhaust_air_damper_percentage_command();

    public void addUsesExhaust_air_damper_percentage_sensor (IExhaust_air_damper_percentage_sensor parameter);

	public Set<IExhaust_air_damper_percentage_sensor> getUsesExhaust_air_damper_percentage_sensor();

}