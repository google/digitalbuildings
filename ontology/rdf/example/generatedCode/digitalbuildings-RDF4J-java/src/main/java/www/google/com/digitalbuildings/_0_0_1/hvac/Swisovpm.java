package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_water_isolation_valve_percentage_sensor;

/**
* Class Swisovpm 
* Supply side isolation valve monitoring.
*/
@SuppressWarnings("serial")
public class Swisovpm extends www.google.com.digitalbuildings._0_0_1.Monitoring implements ISwisovpm{

	IRI newInstance;
	public Swisovpm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Swisovpm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesSupply_water_isolation_valve_percentage_command (ISupply_water_isolation_valve_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_water_isolation_valve_percentage_command> getUsesSupply_water_isolation_valve_percentage_command (){
		Set<ISupply_water_isolation_valve_percentage_command> UsesSupply_water_isolation_valve_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_water_isolation_valve_percentage_command) {
				UsesSupply_water_isolation_valve_percentage_command.add((Supply_water_isolation_valve_percentage_command)action);
			}
		});
		return UsesSupply_water_isolation_valve_percentage_command;
	}


  public void addUsesSupply_water_isolation_valve_percentage_sensor (ISupply_water_isolation_valve_percentage_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_water_isolation_valve_percentage_sensor> getUsesSupply_water_isolation_valve_percentage_sensor (){
		Set<ISupply_water_isolation_valve_percentage_sensor> UsesSupply_water_isolation_valve_percentage_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_water_isolation_valve_percentage_sensor) {
				UsesSupply_water_isolation_valve_percentage_sensor.add((Supply_water_isolation_valve_percentage_sensor)action);
			}
		});
		return UsesSupply_water_isolation_valve_percentage_sensor;
	}

	public static Set<ISwisovpm> getAllSwisovpmsObjectsCreated(){
		Set<ISwisovpm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Swisovpm")).subjects().stream()
		.map(mapper->(ISwisovpm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}