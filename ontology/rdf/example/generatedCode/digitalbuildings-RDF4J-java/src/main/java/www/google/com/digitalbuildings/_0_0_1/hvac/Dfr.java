package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IEquipment;
import www.google.com.digitalbuildings._0_0_1.Equipment;

/**
* Class Dfr 
* Tag for duct furnaces.
*/
@SuppressWarnings("serial")
public class Dfr extends www.google.com.digitalbuildings._0_0_1.Equipment implements IDfr{

	IRI newInstance;
	public Dfr(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Dfr"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IDfr> getAllDfrsObjectsCreated(){
		Set<IDfr> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Dfr")).subjects().stream()
		.map(mapper->(IDfr)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}