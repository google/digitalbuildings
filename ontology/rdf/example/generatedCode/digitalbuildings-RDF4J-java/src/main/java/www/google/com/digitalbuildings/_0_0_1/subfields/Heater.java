package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Heater 
* Component which provides heat to media.
*/
@SuppressWarnings("serial")
public class Heater extends www.google.com.digitalbuildings._0_0_1.subfields.Component implements IHeater{

	IRI newInstance;
	public Heater(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Heater"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IHeater> getAllHeatersObjectsCreated(){
		Set<IHeater> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Heater")).subjects().stream()
		.map(mapper->(IHeater)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}