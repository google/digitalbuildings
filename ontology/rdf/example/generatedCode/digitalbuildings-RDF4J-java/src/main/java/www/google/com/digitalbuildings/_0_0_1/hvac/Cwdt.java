package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Condensing_supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_return_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Condensing_return_water_temperature_sensor;

/**
* Class Cwdt 
* Temperature differential across condenser water.
*/
@SuppressWarnings("serial")
public class Cwdt extends www.google.com.digitalbuildings._0_0_1.Monitoring implements ICwdt{

	IRI newInstance;
	public Cwdt(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Cwdt"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesCondensing_return_water_temperature_sensor (ICondensing_return_water_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICondensing_return_water_temperature_sensor> getUsesCondensing_return_water_temperature_sensor (){
		Set<ICondensing_return_water_temperature_sensor> UsesCondensing_return_water_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Condensing_return_water_temperature_sensor) {
				UsesCondensing_return_water_temperature_sensor.add((Condensing_return_water_temperature_sensor)action);
			}
		});
		return UsesCondensing_return_water_temperature_sensor;
	}


  public void addUsesCondensing_supply_water_temperature_sensor (ICondensing_supply_water_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICondensing_supply_water_temperature_sensor> getUsesCondensing_supply_water_temperature_sensor (){
		Set<ICondensing_supply_water_temperature_sensor> UsesCondensing_supply_water_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Condensing_supply_water_temperature_sensor) {
				UsesCondensing_supply_water_temperature_sensor.add((Condensing_supply_water_temperature_sensor)action);
			}
		});
		return UsesCondensing_supply_water_temperature_sensor;
	}

	public static Set<ICwdt> getAllCwdtsObjectsCreated(){
		Set<ICwdt> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Cwdt")).subjects().stream()
		.map(mapper->(ICwdt)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}