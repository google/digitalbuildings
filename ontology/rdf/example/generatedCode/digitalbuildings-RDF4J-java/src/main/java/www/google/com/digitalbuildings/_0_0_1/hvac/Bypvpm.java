package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IBypass_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Bypass_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IBypass_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Bypass_valve_percentage_sensor;

/**
* Class Bypvpm 
* Bypass water valve percentage monitoring.
*/
@SuppressWarnings("serial")
public class Bypvpm extends www.google.com.digitalbuildings._0_0_1.Monitoring implements IBypvpm{

	IRI newInstance;
	public Bypvpm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Bypvpm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesOptionalsBypass_valve_percentage_sensor (IBypass_valve_percentage_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IBypass_valve_percentage_sensor> getUsesOptionalsBypass_valve_percentage_sensor (){
		Set<IBypass_valve_percentage_sensor> UsesOptionalsBypass_valve_percentage_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Bypass_valve_percentage_sensor) {
				UsesOptionalsBypass_valve_percentage_sensor.add((Bypass_valve_percentage_sensor)action);
			}
		});
		return UsesOptionalsBypass_valve_percentage_sensor;
	}


  public void addUsesBypass_valve_percentage_command (IBypass_valve_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IBypass_valve_percentage_command> getUsesBypass_valve_percentage_command (){
		Set<IBypass_valve_percentage_command> UsesBypass_valve_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Bypass_valve_percentage_command) {
				UsesBypass_valve_percentage_command.add((Bypass_valve_percentage_command)action);
			}
		});
		return UsesBypass_valve_percentage_command;
	}

	public static Set<IBypvpm> getAllBypvpmsObjectsCreated(){
		Set<IBypvpm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Bypvpm")).subjects().stream()
		.map(mapper->(IBypvpm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}