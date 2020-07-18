package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.ISoutheast_illuminance_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Southeast_illuminance_sensor;

/**
* Class Sdc_ext_tlt_east_southeast 
* Multi-directional shade (East and Southeast).
*/
@SuppressWarnings("serial")
public class Sdc_ext_tlt_east_southeast extends www.google.com.digitalbuildings._0_0_1.hvac.Sdc_ext_tlt_east implements ISdc_ext_tlt_east_southeast{

	IRI newInstance;
	public Sdc_ext_tlt_east_southeast(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Sdc_ext_tlt_east_southeast"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesSoutheast_illuminance_sensor (ISoutheast_illuminance_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISoutheast_illuminance_sensor> getUsesSoutheast_illuminance_sensor (){
		Set<ISoutheast_illuminance_sensor> UsesSoutheast_illuminance_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Southeast_illuminance_sensor) {
				UsesSoutheast_illuminance_sensor.add((Southeast_illuminance_sensor)action);
			}
		});
		return UsesSoutheast_illuminance_sensor;
	}

	public static Set<ISdc_ext_tlt_east_southeast> getAllSdc_ext_tlt_east_southeastsObjectsCreated(){
		Set<ISdc_ext_tlt_east_southeast> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Sdc_ext_tlt_east_southeast")).subjects().stream()
		.map(mapper->(ISdc_ext_tlt_east_southeast)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}