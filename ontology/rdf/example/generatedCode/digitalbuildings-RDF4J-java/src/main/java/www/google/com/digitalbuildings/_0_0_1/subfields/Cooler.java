package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Cooler 
* Device used to cool product (e.g. walk-in food cooler) or media.
*/
@SuppressWarnings("serial")
public class Cooler extends www.google.com.digitalbuildings._0_0_1.subfields.Component implements ICooler{

	IRI newInstance;
	public Cooler(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Cooler"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ICooler> getAllCoolersObjectsCreated(){
		Set<ICooler> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Cooler")).subjects().stream()
		.map(mapper->(ICooler)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}