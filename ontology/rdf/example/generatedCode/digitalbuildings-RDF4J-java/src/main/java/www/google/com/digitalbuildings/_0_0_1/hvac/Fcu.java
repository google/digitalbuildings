package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IEquipment;
import www.google.com.digitalbuildings._0_0_1.Equipment;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Return_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Return_air_temperature_sensor;

/**
* Class Fcu 
* Tag for fan-coil units.
*/
@SuppressWarnings("serial")
public class Fcu extends www.google.com.digitalbuildings._0_0_1.Equipment implements IFcu{

	IRI newInstance;
	public Fcu(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fcu"));
	}

	public IRI iri()
	{
		return newInstance;
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


  public void addUsesOptionalsReturn_air_temperature_sensor (IReturn_air_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IReturn_air_temperature_sensor> getUsesOptionalsReturn_air_temperature_sensor (){
		Set<IReturn_air_temperature_sensor> UsesOptionalsReturn_air_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Return_air_temperature_sensor) {
				UsesOptionalsReturn_air_temperature_sensor.add((Return_air_temperature_sensor)action);
			}
		});
		return UsesOptionalsReturn_air_temperature_sensor;
	}

	public static Set<IFcu> getAllFcusObjectsCreated(){
		Set<IFcu> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fcu")).subjects().stream()
		.map(mapper->(IFcu)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}