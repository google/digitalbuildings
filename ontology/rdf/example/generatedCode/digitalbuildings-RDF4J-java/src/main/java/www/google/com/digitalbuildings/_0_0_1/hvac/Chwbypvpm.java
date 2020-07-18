package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_water_bypass_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_water_bypass_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_water_bypass_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_water_bypass_valve_percentage_sensor;

/**
* Class Chwbypvpm 
* Chilled water bypass valve percentage monitoring.
*/
@SuppressWarnings("serial")
public class Chwbypvpm extends www.google.com.digitalbuildings._0_0_1.Monitoring implements IChwbypvpm{

	IRI newInstance;
	public Chwbypvpm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Chwbypvpm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesChilled_water_bypass_valve_percentage_command (IChilled_water_bypass_valve_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IChilled_water_bypass_valve_percentage_command> getUsesChilled_water_bypass_valve_percentage_command (){
		Set<IChilled_water_bypass_valve_percentage_command> UsesChilled_water_bypass_valve_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_water_bypass_valve_percentage_command) {
				UsesChilled_water_bypass_valve_percentage_command.add((Chilled_water_bypass_valve_percentage_command)action);
			}
		});
		return UsesChilled_water_bypass_valve_percentage_command;
	}


  public void addUsesChilled_water_bypass_valve_percentage_sensor (IChilled_water_bypass_valve_percentage_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IChilled_water_bypass_valve_percentage_sensor> getUsesChilled_water_bypass_valve_percentage_sensor (){
		Set<IChilled_water_bypass_valve_percentage_sensor> UsesChilled_water_bypass_valve_percentage_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_water_bypass_valve_percentage_sensor) {
				UsesChilled_water_bypass_valve_percentage_sensor.add((Chilled_water_bypass_valve_percentage_sensor)action);
			}
		});
		return UsesChilled_water_bypass_valve_percentage_sensor;
	}

	public static Set<IChwbypvpm> getAllChwbypvpmsObjectsCreated(){
		Set<IChwbypvpm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Chwbypvpm")).subjects().stream()
		.map(mapper->(IChwbypvpm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}