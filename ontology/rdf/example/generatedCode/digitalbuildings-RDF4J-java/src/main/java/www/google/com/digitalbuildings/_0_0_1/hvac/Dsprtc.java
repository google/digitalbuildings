package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.Operational;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Return_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Return_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_heating_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Return_air_heating_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_cooling_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Return_air_cooling_temperature_setpoint;

/**
* Class Dsprtc 
* Dual setpoint return air temp control.
*/
@SuppressWarnings("serial")
public class Dsprtc extends www.google.com.digitalbuildings._0_0_1.Operational implements IDsprtc{

	IRI newInstance;
	public Dsprtc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Dsprtc"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesReturn_air_cooling_temperature_setpoint (IReturn_air_cooling_temperature_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IReturn_air_cooling_temperature_setpoint> getUsesReturn_air_cooling_temperature_setpoint (){
		Set<IReturn_air_cooling_temperature_setpoint> UsesReturn_air_cooling_temperature_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Return_air_cooling_temperature_setpoint) {
				UsesReturn_air_cooling_temperature_setpoint.add((Return_air_cooling_temperature_setpoint)action);
			}
		});
		return UsesReturn_air_cooling_temperature_setpoint;
	}


  public void addUsesReturn_air_heating_temperature_setpoint (IReturn_air_heating_temperature_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IReturn_air_heating_temperature_setpoint> getUsesReturn_air_heating_temperature_setpoint (){
		Set<IReturn_air_heating_temperature_setpoint> UsesReturn_air_heating_temperature_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Return_air_heating_temperature_setpoint) {
				UsesReturn_air_heating_temperature_setpoint.add((Return_air_heating_temperature_setpoint)action);
			}
		});
		return UsesReturn_air_heating_temperature_setpoint;
	}


  public void addUsesReturn_air_temperature_sensor (IReturn_air_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IReturn_air_temperature_sensor> getUsesReturn_air_temperature_sensor (){
		Set<IReturn_air_temperature_sensor> UsesReturn_air_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Return_air_temperature_sensor) {
				UsesReturn_air_temperature_sensor.add((Return_air_temperature_sensor)action);
			}
		});
		return UsesReturn_air_temperature_sensor;
	}


  public void addUsesOptionalsDischarge_air_temperature_sensor (IDischarge_air_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IDischarge_air_temperature_sensor> getUsesOptionalsDischarge_air_temperature_sensor (){
		Set<IDischarge_air_temperature_sensor> UsesOptionalsDischarge_air_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_air_temperature_sensor) {
				UsesOptionalsDischarge_air_temperature_sensor.add((Discharge_air_temperature_sensor)action);
			}
		});
		return UsesOptionalsDischarge_air_temperature_sensor;
	}


  public void addUsesOptionalsReturn_air_relative_humidity_sensor (IReturn_air_relative_humidity_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IReturn_air_relative_humidity_sensor> getUsesOptionalsReturn_air_relative_humidity_sensor (){
		Set<IReturn_air_relative_humidity_sensor> UsesOptionalsReturn_air_relative_humidity_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Return_air_relative_humidity_sensor) {
				UsesOptionalsReturn_air_relative_humidity_sensor.add((Return_air_relative_humidity_sensor)action);
			}
		});
		return UsesOptionalsReturn_air_relative_humidity_sensor;
	}

	public static Set<IDsprtc> getAllDsprtcsObjectsCreated(){
		Set<IDsprtc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Dsprtc")).subjects().stream()
		.map(mapper->(IDsprtc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}