package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_water_differential_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_water_differential_pressure_sensor;

/**
* Class Chwdpm 
* Differential pressure monitoring for chilled water.
*/
@SuppressWarnings("serial")
public class Chwdpm extends www.google.com.digitalbuildings._0_0_1.hvac.Functionality implements IChwdpm{

	IRI newInstance;
	public Chwdpm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Chwdpm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesChilled_water_differential_pressure_sensor (IChilled_water_differential_pressure_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IChilled_water_differential_pressure_sensor> getUsesChilled_water_differential_pressure_sensor (){
		Set<IChilled_water_differential_pressure_sensor> UsesChilled_water_differential_pressure_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_water_differential_pressure_sensor) {
				UsesChilled_water_differential_pressure_sensor.add((Chilled_water_differential_pressure_sensor)action);
			}
		});
		return UsesChilled_water_differential_pressure_sensor;
	}

	public static Set<IChwdpm> getAllChwdpmsObjectsCreated(){
		Set<IChwdpm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Chwdpm")).subjects().stream()
		.map(mapper->(IChwdpm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}