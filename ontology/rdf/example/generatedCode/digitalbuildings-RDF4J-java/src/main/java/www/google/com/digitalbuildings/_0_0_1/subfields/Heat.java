package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Heat 
* Quality of media indicating energy level.
*/
@SuppressWarnings("serial")
public class Heat extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IHeat{

	IRI newInstance;
	public Heat(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Heat"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IHeat> getAllHeatsObjectsCreated(){
		Set<IHeat> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Heat")).subjects().stream()
		.map(mapper->(IHeat)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}