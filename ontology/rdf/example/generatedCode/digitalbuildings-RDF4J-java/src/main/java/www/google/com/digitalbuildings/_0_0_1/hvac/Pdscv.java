package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IControl;
import www.google.com.digitalbuildings._0_0_1.Control;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_damper_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_damper_percentage_sensor;

/**
* Class Pdscv 
* Pressure-dependent supply damper control for ventilation purposes (CO2 or VOC).
*/
@SuppressWarnings("serial")
public class Pdscv extends www.google.com.digitalbuildings._0_0_1.Control implements IPdscv{

	IRI newInstance;
	public Pdscv(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Pdscv"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesSupply_air_damper_percentage_command (ISupply_air_damper_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_air_damper_percentage_command> getUsesSupply_air_damper_percentage_command (){
		Set<ISupply_air_damper_percentage_command> UsesSupply_air_damper_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_damper_percentage_command) {
				UsesSupply_air_damper_percentage_command.add((Supply_air_damper_percentage_command)action);
			}
		});
		return UsesSupply_air_damper_percentage_command;
	}


  public void addUsesSupply_air_damper_percentage_sensor (ISupply_air_damper_percentage_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_air_damper_percentage_sensor> getUsesSupply_air_damper_percentage_sensor (){
		Set<ISupply_air_damper_percentage_sensor> UsesSupply_air_damper_percentage_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_damper_percentage_sensor) {
				UsesSupply_air_damper_percentage_sensor.add((Supply_air_damper_percentage_sensor)action);
			}
		});
		return UsesSupply_air_damper_percentage_sensor;
	}

	public static Set<IPdscv> getAllPdscvsObjectsCreated(){
		Set<IPdscv> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Pdscv")).subjects().stream()
		.map(mapper->(IPdscv)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}