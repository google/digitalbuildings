package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.Operational;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_co2_concentration_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_co2_concentration_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_co2_concentration_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_co2_concentration_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_co2_concentration_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_co2_concentration_sensor_1;

/**
* Class Co2c2x 
* Carbon dioxide control with dual zone sensors.
*/
@SuppressWarnings("serial")
public class Co2c2x extends www.google.com.digitalbuildings._0_0_1.Operational implements ICo2c2x{

	IRI newInstance;
	public Co2c2x(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Co2c2x"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesZone_air_co2_concentration_sensor_1 (IZone_air_co2_concentration_sensor_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_co2_concentration_sensor_1> getUsesZone_air_co2_concentration_sensor_1 (){
		Set<IZone_air_co2_concentration_sensor_1> UsesZone_air_co2_concentration_sensor_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_co2_concentration_sensor_1) {
				UsesZone_air_co2_concentration_sensor_1.add((Zone_air_co2_concentration_sensor_1)action);
			}
		});
		return UsesZone_air_co2_concentration_sensor_1;
	}


  public void addUsesZone_air_co2_concentration_sensor_2 (IZone_air_co2_concentration_sensor_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_co2_concentration_sensor_2> getUsesZone_air_co2_concentration_sensor_2 (){
		Set<IZone_air_co2_concentration_sensor_2> UsesZone_air_co2_concentration_sensor_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_co2_concentration_sensor_2) {
				UsesZone_air_co2_concentration_sensor_2.add((Zone_air_co2_concentration_sensor_2)action);
			}
		});
		return UsesZone_air_co2_concentration_sensor_2;
	}


  public void addUsesZone_air_co2_concentration_setpoint (IZone_air_co2_concentration_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_co2_concentration_setpoint> getUsesZone_air_co2_concentration_setpoint (){
		Set<IZone_air_co2_concentration_setpoint> UsesZone_air_co2_concentration_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_co2_concentration_setpoint) {
				UsesZone_air_co2_concentration_setpoint.add((Zone_air_co2_concentration_setpoint)action);
			}
		});
		return UsesZone_air_co2_concentration_setpoint;
	}

	public static Set<ICo2c2x> getAllCo2c2xsObjectsCreated(){
		Set<ICo2c2x> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Co2c2x")).subjects().stream()
		.map(mapper->(ICo2c2x)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}