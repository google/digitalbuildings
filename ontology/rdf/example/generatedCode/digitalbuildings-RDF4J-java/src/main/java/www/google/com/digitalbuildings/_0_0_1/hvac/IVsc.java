package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.ISpeed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IPower_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_command;
import www.google.com.digitalbuildings._0_0_1.fields.ICurrent_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_status;
import www.google.com.digitalbuildings._0_0_1.fields.ISpeed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISpeed_frequency_sensor;
/**
* Class Vsc 
* Variable speed control generic.
*/
public interface IVsc extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesOptionalsCurrent_sensor (ICurrent_sensor parameter);

	public Set<ICurrent_sensor> getUsesOptionalsCurrent_sensor();

    public void addUsesOptionalsPower_sensor (IPower_sensor parameter);

	public Set<IPower_sensor> getUsesOptionalsPower_sensor();

    public void addUsesOptionalsSpeed_frequency_sensor (ISpeed_frequency_sensor parameter);

	public Set<ISpeed_frequency_sensor> getUsesOptionalsSpeed_frequency_sensor();

    public void addUsesOptionalsSpeed_percentage_sensor (ISpeed_percentage_sensor parameter);

	public Set<ISpeed_percentage_sensor> getUsesOptionalsSpeed_percentage_sensor();

    public void addUsesRun_command (IRun_command parameter);

	public Set<IRun_command> getUsesRun_command();

    public void addUsesRun_status (IRun_status parameter);

	public Set<IRun_status> getUsesRun_status();

    public void addUsesSpeed_percentage_command (ISpeed_percentage_command parameter);

	public Set<ISpeed_percentage_command> getUsesSpeed_percentage_command();

}