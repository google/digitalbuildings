package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_supply_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_supply_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_supply_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_supply_water_isolation_valve_percentage_command;

/**
* Class Chwswisovpm 
* Supply side isolation valve monitoring.
*/
@SuppressWarnings("serial")
public class Chwswisovpm extends www.google.com.digitalbuildings._0_0_1.Monitoring implements IChwswisovpm{

	IRI newInstance;
	public Chwswisovpm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Chwswisovpm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesChilled_supply_water_isolation_valve_percentage_command (IChilled_supply_water_isolation_valve_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IChilled_supply_water_isolation_valve_percentage_command> getUsesChilled_supply_water_isolation_valve_percentage_command (){
		Set<IChilled_supply_water_isolation_valve_percentage_command> UsesChilled_supply_water_isolation_valve_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_supply_water_isolation_valve_percentage_command) {
				UsesChilled_supply_water_isolation_valve_percentage_command.add((Chilled_supply_water_isolation_valve_percentage_command)action);
			}
		});
		return UsesChilled_supply_water_isolation_valve_percentage_command;
	}


  public void addUsesChilled_supply_water_isolation_valve_percentage_sensor (IChilled_supply_water_isolation_valve_percentage_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IChilled_supply_water_isolation_valve_percentage_sensor> getUsesChilled_supply_water_isolation_valve_percentage_sensor (){
		Set<IChilled_supply_water_isolation_valve_percentage_sensor> UsesChilled_supply_water_isolation_valve_percentage_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_supply_water_isolation_valve_percentage_sensor) {
				UsesChilled_supply_water_isolation_valve_percentage_sensor.add((Chilled_supply_water_isolation_valve_percentage_sensor)action);
			}
		});
		return UsesChilled_supply_water_isolation_valve_percentage_sensor;
	}

	public static Set<IChwswisovpm> getAllChwswisovpmsObjectsCreated(){
		Set<IChwswisovpm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Chwswisovpm")).subjects().stream()
		.map(mapper->(IChwswisovpm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}