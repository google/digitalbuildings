package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_return_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Condensing_return_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_return_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Condensing_return_water_isolation_valve_percentage_sensor;

/**
* Class Cwrisovpm 
* Condensing water return isolation monitoring.
*/
@SuppressWarnings("serial")
public class Cwrisovpm extends www.google.com.digitalbuildings._0_0_1.Monitoring implements ICwrisovpm{

	IRI newInstance;
	public Cwrisovpm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Cwrisovpm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesCondensing_return_water_isolation_valve_percentage_command (ICondensing_return_water_isolation_valve_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICondensing_return_water_isolation_valve_percentage_command> getUsesCondensing_return_water_isolation_valve_percentage_command (){
		Set<ICondensing_return_water_isolation_valve_percentage_command> UsesCondensing_return_water_isolation_valve_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Condensing_return_water_isolation_valve_percentage_command) {
				UsesCondensing_return_water_isolation_valve_percentage_command.add((Condensing_return_water_isolation_valve_percentage_command)action);
			}
		});
		return UsesCondensing_return_water_isolation_valve_percentage_command;
	}


  public void addUsesCondensing_return_water_isolation_valve_percentage_sensor (ICondensing_return_water_isolation_valve_percentage_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICondensing_return_water_isolation_valve_percentage_sensor> getUsesCondensing_return_water_isolation_valve_percentage_sensor (){
		Set<ICondensing_return_water_isolation_valve_percentage_sensor> UsesCondensing_return_water_isolation_valve_percentage_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Condensing_return_water_isolation_valve_percentage_sensor) {
				UsesCondensing_return_water_isolation_valve_percentage_sensor.add((Condensing_return_water_isolation_valve_percentage_sensor)action);
			}
		});
		return UsesCondensing_return_water_isolation_valve_percentage_sensor;
	}

	public static Set<ICwrisovpm> getAllCwrisovpmsObjectsCreated(){
		Set<ICwrisovpm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Cwrisovpm")).subjects().stream()
		.map(mapper->(ICwrisovpm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}