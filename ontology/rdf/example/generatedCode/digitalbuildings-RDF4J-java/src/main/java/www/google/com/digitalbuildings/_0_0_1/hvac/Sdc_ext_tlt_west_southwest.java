package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.ISouthwest_illuminance_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Southwest_illuminance_sensor;

/**
* Class Sdc_ext_tlt_west_southwest 
* Multi-directional shade (West and Southwest).
*/
@SuppressWarnings("serial")
public class Sdc_ext_tlt_west_southwest extends www.google.com.digitalbuildings._0_0_1.hvac.Sdc_ext_tlt_west implements ISdc_ext_tlt_west_southwest{

	IRI newInstance;
	public Sdc_ext_tlt_west_southwest(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Sdc_ext_tlt_west_southwest"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesSouthwest_illuminance_sensor (ISouthwest_illuminance_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISouthwest_illuminance_sensor> getUsesSouthwest_illuminance_sensor (){
		Set<ISouthwest_illuminance_sensor> UsesSouthwest_illuminance_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Southwest_illuminance_sensor) {
				UsesSouthwest_illuminance_sensor.add((Southwest_illuminance_sensor)action);
			}
		});
		return UsesSouthwest_illuminance_sensor;
	}

	public static Set<ISdc_ext_tlt_west_southwest> getAllSdc_ext_tlt_west_southwestsObjectsCreated(){
		Set<ISdc_ext_tlt_west_southwest> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Sdc_ext_tlt_west_southwest")).subjects().stream()
		.map(mapper->(ISdc_ext_tlt_west_southwest)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}