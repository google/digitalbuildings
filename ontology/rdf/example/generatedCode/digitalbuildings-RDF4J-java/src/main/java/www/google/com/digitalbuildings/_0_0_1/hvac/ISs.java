package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.IPower_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_command;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_status;
import www.google.com.digitalbuildings._0_0_1.fields.ICurrent_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IPowerfactor_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IFlowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IPower_capacity;
/**
* Class Ss 
* Basic combination of run command and status (start/stop).
*/
public interface ISs extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesRun_command (IRun_command parameter);

	public Set<IRun_command> getUsesRun_command();

    public void addUsesRun_status (IRun_status parameter);

	public Set<IRun_status> getUsesRun_status();

    public void addUsesOptionalsCurrent_sensor (ICurrent_sensor parameter);

	public Set<ICurrent_sensor> getUsesOptionalsCurrent_sensor();

    public void addUsesOptionalsFlowrate_capacity (IFlowrate_capacity parameter);

	public Set<IFlowrate_capacity> getUsesOptionalsFlowrate_capacity();

    public void addUsesOptionalsPower_capacity (IPower_capacity parameter);

	public Set<IPower_capacity> getUsesOptionalsPower_capacity();

    public void addUsesOptionalsPower_sensor (IPower_sensor parameter);

	public Set<IPower_sensor> getUsesOptionalsPower_sensor();

    public void addUsesOptionalsPowerfactor_sensor (IPowerfactor_sensor parameter);

	public Set<IPowerfactor_sensor> getUsesOptionalsPowerfactor_sensor();

}