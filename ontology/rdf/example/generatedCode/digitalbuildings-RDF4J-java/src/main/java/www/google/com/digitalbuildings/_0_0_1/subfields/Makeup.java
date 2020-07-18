package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Makeup 
* Process of adding ("making-up") water that has been lost due to blowdown or evaporation.
*/
@SuppressWarnings("serial")
public class Makeup extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IMakeup{

	IRI newInstance;
	public Makeup(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Makeup"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IMakeup> getAllMakeupsObjectsCreated(){
		Set<IMakeup> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Makeup")).subjects().stream()
		.map(mapper->(IMakeup)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}