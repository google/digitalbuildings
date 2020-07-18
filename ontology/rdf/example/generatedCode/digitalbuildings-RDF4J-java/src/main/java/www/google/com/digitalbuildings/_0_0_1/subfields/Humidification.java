package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Humidification 
* Process of adding moisture to air.
*/
@SuppressWarnings("serial")
public class Humidification extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IHumidification{

	IRI newInstance;
	public Humidification(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Humidification"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IHumidification> getAllHumidificationsObjectsCreated(){
		Set<IHumidification> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Humidification")).subjects().stream()
		.map(mapper->(IHumidification)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}