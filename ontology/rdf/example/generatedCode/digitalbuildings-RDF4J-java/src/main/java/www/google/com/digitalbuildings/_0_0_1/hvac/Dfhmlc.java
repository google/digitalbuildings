package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.Operational;
import www.google.com.digitalbuildings._0_0_1.IRemap_required;
import www.google.com.digitalbuildings._0_0_1.Remap_required;
import www.google.com.digitalbuildings._0_0_1.fields.IMedium_discharge_fan_speed_command;
import www.google.com.digitalbuildings._0_0_1.fields.Medium_discharge_fan_speed_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.ILow_discharge_fan_speed_command;
import www.google.com.digitalbuildings._0_0_1.fields.Low_discharge_fan_speed_command;
import www.google.com.digitalbuildings._0_0_1.fields.IHigh_discharge_fan_speed_command;
import www.google.com.digitalbuildings._0_0_1.fields.High_discharge_fan_speed_command;

/**
* Class Dfhmlc 
* Discharge fan three-speed (high/medium/low/off) speed control.
*/
@SuppressWarnings("serial")
public class Dfhmlc extends www.google.com.digitalbuildings._0_0_1.Operational implements IDfhmlc{

	IRI newInstance;
	public Dfhmlc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Dfhmlc"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesOptionalsDischarge_fan_run_command (IDischarge_fan_run_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IDischarge_fan_run_command> getUsesOptionalsDischarge_fan_run_command (){
		Set<IDischarge_fan_run_command> UsesOptionalsDischarge_fan_run_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_fan_run_command) {
				UsesOptionalsDischarge_fan_run_command.add((Discharge_fan_run_command)action);
			}
		});
		return UsesOptionalsDischarge_fan_run_command;
	}


  public void addUsesOptionalsDischarge_fan_run_status (IDischarge_fan_run_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IDischarge_fan_run_status> getUsesOptionalsDischarge_fan_run_status (){
		Set<IDischarge_fan_run_status> UsesOptionalsDischarge_fan_run_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_fan_run_status) {
				UsesOptionalsDischarge_fan_run_status.add((Discharge_fan_run_status)action);
			}
		});
		return UsesOptionalsDischarge_fan_run_status;
	}


  public void addUsesHigh_discharge_fan_speed_command (IHigh_discharge_fan_speed_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IHigh_discharge_fan_speed_command> getUsesHigh_discharge_fan_speed_command (){
		Set<IHigh_discharge_fan_speed_command> UsesHigh_discharge_fan_speed_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof High_discharge_fan_speed_command) {
				UsesHigh_discharge_fan_speed_command.add((High_discharge_fan_speed_command)action);
			}
		});
		return UsesHigh_discharge_fan_speed_command;
	}


  public void addUsesLow_discharge_fan_speed_command (ILow_discharge_fan_speed_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ILow_discharge_fan_speed_command> getUsesLow_discharge_fan_speed_command (){
		Set<ILow_discharge_fan_speed_command> UsesLow_discharge_fan_speed_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Low_discharge_fan_speed_command) {
				UsesLow_discharge_fan_speed_command.add((Low_discharge_fan_speed_command)action);
			}
		});
		return UsesLow_discharge_fan_speed_command;
	}


  public void addUsesMedium_discharge_fan_speed_command (IMedium_discharge_fan_speed_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IMedium_discharge_fan_speed_command> getUsesMedium_discharge_fan_speed_command (){
		Set<IMedium_discharge_fan_speed_command> UsesMedium_discharge_fan_speed_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Medium_discharge_fan_speed_command) {
				UsesMedium_discharge_fan_speed_command.add((Medium_discharge_fan_speed_command)action);
			}
		});
		return UsesMedium_discharge_fan_speed_command;
	}

	public static Set<IDfhmlc> getAllDfhmlcsObjectsCreated(){
		Set<IDfhmlc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Dfhmlc")).subjects().stream()
		.map(mapper->(IDfhmlc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}