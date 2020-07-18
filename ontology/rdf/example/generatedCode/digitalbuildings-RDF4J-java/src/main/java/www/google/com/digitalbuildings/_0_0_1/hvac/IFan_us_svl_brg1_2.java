package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_damper_status;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_damper_command;
/**
* Class Fan_us_svl_brg1_2 
* Non-standard type for BRG1
*/
public interface IFan_us_svl_brg1_2 extends IFan_ss{

	public IRI iri();

    public void addUsesExhaust_air_damper_command (IExhaust_air_damper_command parameter);

	public Set<IExhaust_air_damper_command> getUsesExhaust_air_damper_command();

    public void addUsesExhaust_air_damper_status (IExhaust_air_damper_status parameter);

	public Set<IExhaust_air_damper_status> getUsesExhaust_air_damper_status();

}