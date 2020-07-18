package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Guidevane 
* Control vanes that meter refrigerant (on a centrifugal chiller) or air (on an AHU).
*/
@SuppressWarnings("serial")
public class Guidevane extends www.google.com.digitalbuildings._0_0_1.subfields.Component implements IGuidevane{

	IRI newInstance;
	public Guidevane(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Guidevane"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IGuidevane> getAllGuidevanesObjectsCreated(){
		Set<IGuidevane> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Guidevane")).subjects().stream()
		.map(mapper->(IGuidevane)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}