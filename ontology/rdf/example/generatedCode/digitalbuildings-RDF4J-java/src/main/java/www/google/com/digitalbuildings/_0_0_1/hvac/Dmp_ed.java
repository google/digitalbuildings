package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_air_static_pressure_sensor;

/**
* Class Dmp_ed 
* Exhaust control damper.
*/
@SuppressWarnings("serial")
public class Dmp_ed extends www.google.com.digitalbuildings._0_0_1.hvac.Ed implements IDmp_ed{

	IRI newInstance;
	public Dmp_ed(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Dmp_ed"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesExhaust_air_static_pressure_sensor (IExhaust_air_static_pressure_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_air_static_pressure_sensor> getUsesExhaust_air_static_pressure_sensor (){
		Set<IExhaust_air_static_pressure_sensor> UsesExhaust_air_static_pressure_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_air_static_pressure_sensor) {
				UsesExhaust_air_static_pressure_sensor.add((Exhaust_air_static_pressure_sensor)action);
			}
		});
		return UsesExhaust_air_static_pressure_sensor;
	}

	public static Set<IDmp_ed> getAllDmp_edsObjectsCreated(){
		Set<IDmp_ed> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Dmp_ed")).subjects().stream()
		.map(mapper->(IDmp_ed)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}