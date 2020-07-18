package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_speed_mode;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_speed_mode;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_run_status;

/**
* Class Dfmsc 
* Discharge fan multi-speed control.
*/
@SuppressWarnings("serial")
public class Dfmsc extends www.google.com.digitalbuildings._0_0_1.hvac.Functionality implements IDfmsc{

	IRI newInstance;
	public Dfmsc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Dfmsc"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesDischarge_fan_run_command (IDischarge_fan_run_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDischarge_fan_run_command> getUsesDischarge_fan_run_command (){
		Set<IDischarge_fan_run_command> UsesDischarge_fan_run_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_fan_run_command) {
				UsesDischarge_fan_run_command.add((Discharge_fan_run_command)action);
			}
		});
		return UsesDischarge_fan_run_command;
	}


  public void addUsesDischarge_fan_run_status (IDischarge_fan_run_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDischarge_fan_run_status> getUsesDischarge_fan_run_status (){
		Set<IDischarge_fan_run_status> UsesDischarge_fan_run_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_fan_run_status) {
				UsesDischarge_fan_run_status.add((Discharge_fan_run_status)action);
			}
		});
		return UsesDischarge_fan_run_status;
	}


  public void addUsesDischarge_fan_speed_mode (IDischarge_fan_speed_mode parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDischarge_fan_speed_mode> getUsesDischarge_fan_speed_mode (){
		Set<IDischarge_fan_speed_mode> UsesDischarge_fan_speed_mode = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_fan_speed_mode) {
				UsesDischarge_fan_speed_mode.add((Discharge_fan_speed_mode)action);
			}
		});
		return UsesDischarge_fan_speed_mode;
	}

	public static Set<IDfmsc> getAllDfmscsObjectsCreated(){
		Set<IDfmsc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Dfmsc")).subjects().stream()
		.map(mapper->(IDfmsc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}