package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_return_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_return_water_temperature_sensor;

/**
* Class Chwdt 
* Temperature differential across chilled water.
*/
@SuppressWarnings("serial")
public class Chwdt extends www.google.com.digitalbuildings._0_0_1.Monitoring implements IChwdt{

	IRI newInstance;
	public Chwdt(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Chwdt"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesChilled_return_water_temperature_sensor (IChilled_return_water_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IChilled_return_water_temperature_sensor> getUsesChilled_return_water_temperature_sensor (){
		Set<IChilled_return_water_temperature_sensor> UsesChilled_return_water_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_return_water_temperature_sensor) {
				UsesChilled_return_water_temperature_sensor.add((Chilled_return_water_temperature_sensor)action);
			}
		});
		return UsesChilled_return_water_temperature_sensor;
	}


  public void addUsesChilled_supply_water_temperature_sensor (IChilled_supply_water_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IChilled_supply_water_temperature_sensor> getUsesChilled_supply_water_temperature_sensor (){
		Set<IChilled_supply_water_temperature_sensor> UsesChilled_supply_water_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_supply_water_temperature_sensor) {
				UsesChilled_supply_water_temperature_sensor.add((Chilled_supply_water_temperature_sensor)action);
			}
		});
		return UsesChilled_supply_water_temperature_sensor;
	}

	public static Set<IChwdt> getAllChwdtsObjectsCreated(){
		Set<IChwdt> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Chwdt")).subjects().stream()
		.map(mapper->(IChwdt)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}