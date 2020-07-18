package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Fan 
* Component used for the distribution of air.
*/
@SuppressWarnings("serial")
public class Fan extends www.google.com.digitalbuildings._0_0_1.subfields.Component implements IFan{

	IRI newInstance;
	public Fan(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Fan"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IFan> getAllFansObjectsCreated(){
		Set<IFan> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Fan")).subjects().stream()
		.map(mapper->(IFan)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}