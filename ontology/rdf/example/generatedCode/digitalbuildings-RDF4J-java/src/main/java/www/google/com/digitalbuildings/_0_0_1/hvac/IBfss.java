package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.IBoost_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IBoost_fan_run_command;
/**
* Class Bfss 
* Booster fan start-stop and feedback.
*/
public interface IBfss extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesBoost_fan_run_command (IBoost_fan_run_command parameter);

	public Set<IBoost_fan_run_command> getUsesBoost_fan_run_command();

    public void addUsesBoost_fan_run_status (IBoost_fan_run_status parameter);

	public Set<IBoost_fan_run_status> getUsesBoost_fan_run_status();

}