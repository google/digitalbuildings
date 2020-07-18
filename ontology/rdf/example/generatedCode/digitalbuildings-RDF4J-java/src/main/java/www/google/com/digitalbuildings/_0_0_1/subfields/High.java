package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class High 
* Level of control or measurement; above medium and low; opposite of low.
*/
@SuppressWarnings("serial")
public class High extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IHigh{

	IRI newInstance;
	public High(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#High"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IHigh> getAllHighsObjectsCreated(){
		Set<IHigh> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#High")).subjects().stream()
		.map(mapper->(IHigh)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}