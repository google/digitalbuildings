package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IHeat_exchange_supply_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Heat_exchange_supply_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IHeat_exchange_supply_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Heat_exchange_supply_water_isolation_valve_percentage_command;

/**
* Class Hxswisovpm 
* Heat exchanger supply isolation water valve percentage monitoring.
*/
@SuppressWarnings("serial")
public class Hxswisovpm extends www.google.com.digitalbuildings._0_0_1.Monitoring implements IHxswisovpm{

	IRI newInstance;
	public Hxswisovpm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Hxswisovpm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesHeat_exchange_supply_water_isolation_valve_percentage_command (IHeat_exchange_supply_water_isolation_valve_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IHeat_exchange_supply_water_isolation_valve_percentage_command> getUsesHeat_exchange_supply_water_isolation_valve_percentage_command (){
		Set<IHeat_exchange_supply_water_isolation_valve_percentage_command> UsesHeat_exchange_supply_water_isolation_valve_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Heat_exchange_supply_water_isolation_valve_percentage_command) {
				UsesHeat_exchange_supply_water_isolation_valve_percentage_command.add((Heat_exchange_supply_water_isolation_valve_percentage_command)action);
			}
		});
		return UsesHeat_exchange_supply_water_isolation_valve_percentage_command;
	}


  public void addUsesHeat_exchange_supply_water_isolation_valve_percentage_sensor (IHeat_exchange_supply_water_isolation_valve_percentage_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IHeat_exchange_supply_water_isolation_valve_percentage_sensor> getUsesHeat_exchange_supply_water_isolation_valve_percentage_sensor (){
		Set<IHeat_exchange_supply_water_isolation_valve_percentage_sensor> UsesHeat_exchange_supply_water_isolation_valve_percentage_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Heat_exchange_supply_water_isolation_valve_percentage_sensor) {
				UsesHeat_exchange_supply_water_isolation_valve_percentage_sensor.add((Heat_exchange_supply_water_isolation_valve_percentage_sensor)action);
			}
		});
		return UsesHeat_exchange_supply_water_isolation_valve_percentage_sensor;
	}

	public static Set<IHxswisovpm> getAllHxswisovpmsObjectsCreated(){
		Set<IHxswisovpm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Hxswisovpm")).subjects().stream()
		.map(mapper->(IHxswisovpm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}