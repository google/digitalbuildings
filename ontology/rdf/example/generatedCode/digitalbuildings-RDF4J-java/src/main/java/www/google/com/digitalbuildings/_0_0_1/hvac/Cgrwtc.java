package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.Operational;
import www.google.com.digitalbuildings._0_0_1.fields.ICogeneration_return_water_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Cogeneration_return_water_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ICogeneration_supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Cogeneration_supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICogeneration_return_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Cogeneration_return_water_temperature_sensor;

/**
* Class Cgrwtc 
* Cogeneration return water temperature control.
*/
@SuppressWarnings("serial")
public class Cgrwtc extends www.google.com.digitalbuildings._0_0_1.Operational implements ICgrwtc{

	IRI newInstance;
	public Cgrwtc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Cgrwtc"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesCogeneration_return_water_temperature_sensor (ICogeneration_return_water_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICogeneration_return_water_temperature_sensor> getUsesCogeneration_return_water_temperature_sensor (){
		Set<ICogeneration_return_water_temperature_sensor> UsesCogeneration_return_water_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Cogeneration_return_water_temperature_sensor) {
				UsesCogeneration_return_water_temperature_sensor.add((Cogeneration_return_water_temperature_sensor)action);
			}
		});
		return UsesCogeneration_return_water_temperature_sensor;
	}


  public void addUsesCogeneration_return_water_temperature_setpoint (ICogeneration_return_water_temperature_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICogeneration_return_water_temperature_setpoint> getUsesCogeneration_return_water_temperature_setpoint (){
		Set<ICogeneration_return_water_temperature_setpoint> UsesCogeneration_return_water_temperature_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Cogeneration_return_water_temperature_setpoint) {
				UsesCogeneration_return_water_temperature_setpoint.add((Cogeneration_return_water_temperature_setpoint)action);
			}
		});
		return UsesCogeneration_return_water_temperature_setpoint;
	}


  public void addUsesOptionalsCogeneration_supply_water_temperature_sensor (ICogeneration_supply_water_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ICogeneration_supply_water_temperature_sensor> getUsesOptionalsCogeneration_supply_water_temperature_sensor (){
		Set<ICogeneration_supply_water_temperature_sensor> UsesOptionalsCogeneration_supply_water_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Cogeneration_supply_water_temperature_sensor) {
				UsesOptionalsCogeneration_supply_water_temperature_sensor.add((Cogeneration_supply_water_temperature_sensor)action);
			}
		});
		return UsesOptionalsCogeneration_supply_water_temperature_sensor;
	}

	public static Set<ICgrwtc> getAllCgrwtcsObjectsCreated(){
		Set<ICgrwtc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Cgrwtc")).subjects().stream()
		.map(mapper->(ICgrwtc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}