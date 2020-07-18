package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.IDifferential_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Differential_pressure_sensor;

/**
* Class Wdpm 
* Differential pressure monitoring.
*/
@SuppressWarnings("serial")
public class Wdpm extends www.google.com.digitalbuildings._0_0_1.hvac.Functionality implements IWdpm{

	IRI newInstance;
	public Wdpm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Wdpm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesDifferential_pressure_sensor (IDifferential_pressure_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDifferential_pressure_sensor> getUsesDifferential_pressure_sensor (){
		Set<IDifferential_pressure_sensor> UsesDifferential_pressure_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Differential_pressure_sensor) {
				UsesDifferential_pressure_sensor.add((Differential_pressure_sensor)action);
			}
		});
		return UsesDifferential_pressure_sensor;
	}

	public static Set<IWdpm> getAllWdpmsObjectsCreated(){
		Set<IWdpm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Wdpm")).subjects().stream()
		.map(mapper->(IWdpm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}