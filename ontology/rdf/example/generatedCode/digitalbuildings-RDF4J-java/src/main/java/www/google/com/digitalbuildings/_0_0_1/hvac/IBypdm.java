package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IBypass_air_damper_percentage_command;
/**
* Class Bypdm 
* Bypass damper monitoring.
*/
public interface IBypdm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesBypass_air_damper_percentage_command (IBypass_air_damper_percentage_command parameter);

	public Set<IBypass_air_damper_percentage_command> getUsesBypass_air_damper_percentage_command();

}