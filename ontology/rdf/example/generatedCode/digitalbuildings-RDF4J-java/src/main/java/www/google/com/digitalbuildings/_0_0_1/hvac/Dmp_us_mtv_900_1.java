package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_damper_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_damper_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_damper_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_damper_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IWest_building_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.West_building_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IEast_building_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.East_building_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_damper_command;
import www.google.com.digitalbuildings._0_0_1.fields.Return_air_damper_command;

/**
* Class Dmp_us_mtv_900_1 
* Non-standard type for SBO-900
*/
@SuppressWarnings("serial")
public class Dmp_us_mtv_900_1 extends www.google.com.digitalbuildings._0_0_1.hvac.Dmp implements IDmp_us_mtv_900_1{

	IRI newInstance;
	public Dmp_us_mtv_900_1(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Dmp_us_mtv_900_1"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesEast_building_air_static_pressure_sensor (IEast_building_air_static_pressure_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IEast_building_air_static_pressure_sensor> getUsesEast_building_air_static_pressure_sensor (){
		Set<IEast_building_air_static_pressure_sensor> UsesEast_building_air_static_pressure_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof East_building_air_static_pressure_sensor) {
				UsesEast_building_air_static_pressure_sensor.add((East_building_air_static_pressure_sensor)action);
			}
		});
		return UsesEast_building_air_static_pressure_sensor;
	}


  public void addUsesReturn_air_damper_command (IReturn_air_damper_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IReturn_air_damper_command> getUsesReturn_air_damper_command (){
		Set<IReturn_air_damper_command> UsesReturn_air_damper_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Return_air_damper_command) {
				UsesReturn_air_damper_command.add((Return_air_damper_command)action);
			}
		});
		return UsesReturn_air_damper_command;
	}


  public void addUsesSupply_air_damper_percentage_command_1 (ISupply_air_damper_percentage_command_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_air_damper_percentage_command_1> getUsesSupply_air_damper_percentage_command_1 (){
		Set<ISupply_air_damper_percentage_command_1> UsesSupply_air_damper_percentage_command_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_damper_percentage_command_1) {
				UsesSupply_air_damper_percentage_command_1.add((Supply_air_damper_percentage_command_1)action);
			}
		});
		return UsesSupply_air_damper_percentage_command_1;
	}


  public void addUsesSupply_air_damper_percentage_command_2 (ISupply_air_damper_percentage_command_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_air_damper_percentage_command_2> getUsesSupply_air_damper_percentage_command_2 (){
		Set<ISupply_air_damper_percentage_command_2> UsesSupply_air_damper_percentage_command_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_damper_percentage_command_2) {
				UsesSupply_air_damper_percentage_command_2.add((Supply_air_damper_percentage_command_2)action);
			}
		});
		return UsesSupply_air_damper_percentage_command_2;
	}


  public void addUsesWest_building_air_static_pressure_sensor (IWest_building_air_static_pressure_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IWest_building_air_static_pressure_sensor> getUsesWest_building_air_static_pressure_sensor (){
		Set<IWest_building_air_static_pressure_sensor> UsesWest_building_air_static_pressure_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof West_building_air_static_pressure_sensor) {
				UsesWest_building_air_static_pressure_sensor.add((West_building_air_static_pressure_sensor)action);
			}
		});
		return UsesWest_building_air_static_pressure_sensor;
	}

	public static Set<IDmp_us_mtv_900_1> getAllDmp_us_mtv_900_1sObjectsCreated(){
		Set<IDmp_us_mtv_900_1> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Dmp_us_mtv_900_1")).subjects().stream()
		.map(mapper->(IDmp_us_mtv_900_1)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}