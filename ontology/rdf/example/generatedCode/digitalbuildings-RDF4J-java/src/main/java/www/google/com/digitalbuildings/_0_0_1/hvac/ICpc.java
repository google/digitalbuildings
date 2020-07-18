package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.ICirculation_pump_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_command;
import www.google.com.digitalbuildings._0_0_1.fields.ICirculation_pump_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_status;
/**
* Class Cpc 
* Circulation pump control
*/
public interface ICpc extends IFunctionality{

	public IRI iri();

    public void addUsesCirculation_pump_run_command (ICirculation_pump_run_command parameter);

	public Set<ICirculation_pump_run_command> getUsesCirculation_pump_run_command();

    public void addUsesCirculation_pump_run_status (ICirculation_pump_run_status parameter);

	public Set<ICirculation_pump_run_status> getUsesCirculation_pump_run_status();

    public void addUsesRun_command (IRun_command parameter);

	public Set<IRun_command> getUsesRun_command();

    public void addUsesRun_status (IRun_status parameter);

	public Set<IRun_status> getUsesRun_status();

}