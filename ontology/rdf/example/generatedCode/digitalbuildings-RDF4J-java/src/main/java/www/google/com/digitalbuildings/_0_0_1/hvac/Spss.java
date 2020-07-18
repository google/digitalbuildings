package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.Operational;
import www.google.com.digitalbuildings._0_0_1.fields.ISpray_pump_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Spray_pump_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISpray_pump_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.Spray_pump_run_status;

/**
* Class Spss 
* Spray pump start stop monitoring.
*/
@SuppressWarnings("serial")
public class Spss extends www.google.com.digitalbuildings._0_0_1.Operational implements ISpss{

	IRI newInstance;
	public Spss(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Spss"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesSpray_pump_run_command (ISpray_pump_run_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISpray_pump_run_command> getUsesSpray_pump_run_command (){
		Set<ISpray_pump_run_command> UsesSpray_pump_run_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Spray_pump_run_command) {
				UsesSpray_pump_run_command.add((Spray_pump_run_command)action);
			}
		});
		return UsesSpray_pump_run_command;
	}


  public void addUsesSpray_pump_run_status (ISpray_pump_run_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISpray_pump_run_status> getUsesSpray_pump_run_status (){
		Set<ISpray_pump_run_status> UsesSpray_pump_run_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Spray_pump_run_status) {
				UsesSpray_pump_run_status.add((Spray_pump_run_status)action);
			}
		});
		return UsesSpray_pump_run_status;
	}

	public static Set<ISpss> getAllSpsssObjectsCreated(){
		Set<ISpss> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Spss")).subjects().stream()
		.map(mapper->(ISpss)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}