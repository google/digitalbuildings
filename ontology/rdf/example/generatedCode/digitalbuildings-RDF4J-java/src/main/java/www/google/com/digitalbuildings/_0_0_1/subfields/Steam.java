package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Steam 
* Water in gaseous form.
*/
@SuppressWarnings("serial")
public class Steam extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements ISteam{

	IRI newInstance;
	public Steam(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Steam"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ISteam> getAllSteamsObjectsCreated(){
		Set<ISteam> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Steam")).subjects().stream()
		.map(mapper->(ISteam)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}