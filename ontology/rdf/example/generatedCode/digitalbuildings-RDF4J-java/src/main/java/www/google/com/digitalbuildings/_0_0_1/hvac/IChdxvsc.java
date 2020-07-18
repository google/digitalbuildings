package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_speed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status;
/**
* Class Chdxvsc 
* Variable speed compressor control.
*/
public interface IChdxvsc extends IFunctionality{

	public IRI iri();

    public void addUsesCompressor_run_command (ICompressor_run_command parameter);

	public Set<ICompressor_run_command> getUsesCompressor_run_command();

    public void addUsesCompressor_run_status (ICompressor_run_status parameter);

	public Set<ICompressor_run_status> getUsesCompressor_run_status();

    public void addUsesCompressor_speed_percentage_sensor (ICompressor_speed_percentage_sensor parameter);

	public Set<ICompressor_speed_percentage_sensor> getUsesCompressor_speed_percentage_sensor();

}