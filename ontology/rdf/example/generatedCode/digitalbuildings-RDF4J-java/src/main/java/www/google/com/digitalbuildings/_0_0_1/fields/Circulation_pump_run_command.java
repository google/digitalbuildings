package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.subfields.ICommand;
import www.google.com.digitalbuildings._0_0_1.subfields.Command;
import www.google.com.digitalbuildings._0_0_1.subfields.IRun;
import www.google.com.digitalbuildings._0_0_1.subfields.Run;
import www.google.com.digitalbuildings._0_0_1.subfields.ICirculation;
import www.google.com.digitalbuildings._0_0_1.subfields.Circulation;
import www.google.com.digitalbuildings._0_0_1.subfields.IPump;
import www.google.com.digitalbuildings._0_0_1.subfields.Pump;


@SuppressWarnings("serial")
public class Circulation_pump_run_command extends www.google.com.digitalbuildings._0_0_1.fields.Field implements ICirculation_pump_run_command{

	IRI newInstance;
	public Circulation_pump_run_command(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Circulation_pump_run_command"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addComposedOfCirculation (ICirculation parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<ICirculation> getComposedOfCirculation (){
		Set<ICirculation> ComposedOfCirculation = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Circulation) {
				ComposedOfCirculation.add((Circulation)action);
			}
		});
		return ComposedOfCirculation;
	}


  public void addComposedOfCommand (ICommand parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<ICommand> getComposedOfCommand (){
		Set<ICommand> ComposedOfCommand = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Command) {
				ComposedOfCommand.add((Command)action);
			}
		});
		return ComposedOfCommand;
	}


  public void addComposedOfPump (IPump parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IPump> getComposedOfPump (){
		Set<IPump> ComposedOfPump = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Pump) {
				ComposedOfPump.add((Pump)action);
			}
		});
		return ComposedOfPump;
	}


  public void addComposedOfRun (IRun parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IRun> getComposedOfRun (){
		Set<IRun> ComposedOfRun = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Run) {
				ComposedOfRun.add((Run)action);
			}
		});
		return ComposedOfRun;
	}

	public static Set<ICirculation_pump_run_command> getAllCirculation_pump_run_commandsObjectsCreated(){
		Set<ICirculation_pump_run_command> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Circulation_pump_run_command")).subjects().stream()
		.map(mapper->(ICirculation_pump_run_command)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}