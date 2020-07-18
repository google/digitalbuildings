package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Mixing 
* Process of mixing substance.
*/
@SuppressWarnings("serial")
public class Mixing extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IMixing{

	IRI newInstance;
	public Mixing(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Mixing"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IMixing> getAllMixingsObjectsCreated(){
		Set<IMixing> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Mixing")).subjects().stream()
		.map(mapper->(IMixing)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}