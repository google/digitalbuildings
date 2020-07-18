package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.ICirculation_pump_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Circulation_pump_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_command;
import www.google.com.digitalbuildings._0_0_1.fields.Run_command;
import www.google.com.digitalbuildings._0_0_1.fields.ICirculation_pump_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.Circulation_pump_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_status;
import www.google.com.digitalbuildings._0_0_1.fields.Run_status;

/**
* Class Cpc 
* Circulation pump control
*/
@SuppressWarnings("serial")
public class Cpc extends www.google.com.digitalbuildings._0_0_1.hvac.Functionality implements ICpc{

	IRI newInstance;
	public Cpc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Cpc"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesCirculation_pump_run_command (ICirculation_pump_run_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICirculation_pump_run_command> getUsesCirculation_pump_run_command (){
		Set<ICirculation_pump_run_command> UsesCirculation_pump_run_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Circulation_pump_run_command) {
				UsesCirculation_pump_run_command.add((Circulation_pump_run_command)action);
			}
		});
		return UsesCirculation_pump_run_command;
	}


  public void addUsesCirculation_pump_run_status (ICirculation_pump_run_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICirculation_pump_run_status> getUsesCirculation_pump_run_status (){
		Set<ICirculation_pump_run_status> UsesCirculation_pump_run_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Circulation_pump_run_status) {
				UsesCirculation_pump_run_status.add((Circulation_pump_run_status)action);
			}
		});
		return UsesCirculation_pump_run_status;
	}


  public void addUsesRun_command (IRun_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IRun_command> getUsesRun_command (){
		Set<IRun_command> UsesRun_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Run_command) {
				UsesRun_command.add((Run_command)action);
			}
		});
		return UsesRun_command;
	}


  public void addUsesRun_status (IRun_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IRun_status> getUsesRun_status (){
		Set<IRun_status> UsesRun_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Run_status) {
				UsesRun_status.add((Run_status)action);
			}
		});
		return UsesRun_status;
	}

	public static Set<ICpc> getAllCpcsObjectsCreated(){
		Set<ICpc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Cpc")).subjects().stream()
		.map(mapper->(ICpc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}