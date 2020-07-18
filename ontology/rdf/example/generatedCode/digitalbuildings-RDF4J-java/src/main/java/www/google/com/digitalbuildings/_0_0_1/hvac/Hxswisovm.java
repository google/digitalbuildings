package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IHeat_exchange_supply_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.Heat_exchange_supply_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.IHeat_exchange_supply_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.Heat_exchange_supply_water_isolation_valve_status;

/**
* Class Hxswisovm 
* Heat exchanger supply isolation water valve monitoring.
*/
@SuppressWarnings("serial")
public class Hxswisovm extends www.google.com.digitalbuildings._0_0_1.Monitoring implements IHxswisovm{

	IRI newInstance;
	public Hxswisovm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Hxswisovm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesHeat_exchange_supply_water_isolation_valve_command (IHeat_exchange_supply_water_isolation_valve_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IHeat_exchange_supply_water_isolation_valve_command> getUsesHeat_exchange_supply_water_isolation_valve_command (){
		Set<IHeat_exchange_supply_water_isolation_valve_command> UsesHeat_exchange_supply_water_isolation_valve_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Heat_exchange_supply_water_isolation_valve_command) {
				UsesHeat_exchange_supply_water_isolation_valve_command.add((Heat_exchange_supply_water_isolation_valve_command)action);
			}
		});
		return UsesHeat_exchange_supply_water_isolation_valve_command;
	}


  public void addUsesHeat_exchange_supply_water_isolation_valve_status (IHeat_exchange_supply_water_isolation_valve_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IHeat_exchange_supply_water_isolation_valve_status> getUsesHeat_exchange_supply_water_isolation_valve_status (){
		Set<IHeat_exchange_supply_water_isolation_valve_status> UsesHeat_exchange_supply_water_isolation_valve_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Heat_exchange_supply_water_isolation_valve_status) {
				UsesHeat_exchange_supply_water_isolation_valve_status.add((Heat_exchange_supply_water_isolation_valve_status)action);
			}
		});
		return UsesHeat_exchange_supply_water_isolation_valve_status;
	}

	public static Set<IHxswisovm> getAllHxswisovmsObjectsCreated(){
		Set<IHxswisovm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Hxswisovm")).subjects().stream()
		.map(mapper->(IHxswisovm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}