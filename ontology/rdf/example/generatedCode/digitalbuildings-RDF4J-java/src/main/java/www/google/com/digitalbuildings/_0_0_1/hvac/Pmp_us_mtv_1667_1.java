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
* Class Pmp_us_mtv_1667_1 
* Non-standard type for 1667 PCWPs and CHWPs
*/
@SuppressWarnings("serial")
public class Pmp_us_mtv_1667_1 extends www.google.com.digitalbuildings._0_0_1.hvac.Pmp_ss_vsc implements IPmp_us_mtv_1667_1{

	IRI newInstance;
	public Pmp_us_mtv_1667_1(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Pmp_us_mtv_1667_1"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IPmp_us_mtv_1667_1> getAllPmp_us_mtv_1667_1sObjectsCreated(){
		Set<IPmp_us_mtv_1667_1> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Pmp_us_mtv_1667_1")).subjects().stream()
		.map(mapper->(IPmp_us_mtv_1667_1)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}