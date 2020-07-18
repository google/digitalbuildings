package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.ISpray_pump_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISpray_pump_run_status;
/**
* Class Spss 
* Spray pump start stop monitoring.
*/
public interface ISpss extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesSpray_pump_run_command (ISpray_pump_run_command parameter);

	public Set<ISpray_pump_run_command> getUsesSpray_pump_run_command();

    public void addUsesSpray_pump_run_status (ISpray_pump_run_status parameter);

	public Set<ISpray_pump_run_status> getUsesSpray_pump_run_status();

}