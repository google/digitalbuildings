package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Humidifier 
* Component which humidifies.
*/
@SuppressWarnings("serial")
public class Humidifier extends www.google.com.digitalbuildings._0_0_1.subfields.Component implements IHumidifier{

	IRI newInstance;
	public Humidifier(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Humidifier"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IHumidifier> getAllHumidifiersObjectsCreated(){
		Set<IHumidifier> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Humidifier")).subjects().stream()
		.map(mapper->(IHumidifier)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}