package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_isolation_damper_command;
/**
* Class Vav_us_pao_mir3_2 
* Non-standard type for MIR3
*/
public interface IVav_us_pao_mir3_2 extends IVav_sd_csp{

	public IRI iri();

    public void addUsesSupply_air_isolation_damper_command (ISupply_air_isolation_damper_command parameter);

	public Set<ISupply_air_isolation_damper_command> getUsesSupply_air_isolation_damper_command();

}