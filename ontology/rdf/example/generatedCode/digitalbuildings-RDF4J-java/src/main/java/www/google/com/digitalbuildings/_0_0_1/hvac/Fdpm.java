package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IFilter_differential_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Filter_differential_pressure_sensor;

/**
* Class Fdpm 
* Filter pressure monitoring.
*/
@SuppressWarnings("serial")
public class Fdpm extends www.google.com.digitalbuildings._0_0_1.Monitoring implements IFdpm{

	IRI newInstance;
	public Fdpm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fdpm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesFilter_differential_pressure_sensor (IFilter_differential_pressure_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IFilter_differential_pressure_sensor> getUsesFilter_differential_pressure_sensor (){
		Set<IFilter_differential_pressure_sensor> UsesFilter_differential_pressure_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Filter_differential_pressure_sensor) {
				UsesFilter_differential_pressure_sensor.add((Filter_differential_pressure_sensor)action);
			}
		});
		return UsesFilter_differential_pressure_sensor;
	}

	public static Set<IFdpm> getAllFdpmsObjectsCreated(){
		Set<IFdpm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fdpm")).subjects().stream()
		.map(mapper->(IFdpm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}