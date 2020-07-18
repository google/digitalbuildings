package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Supply 
* Measurement or process of media as it is supplied to the end-use equipment within the system.
*/
@SuppressWarnings("serial")
public class Supply extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements ISupply{

	IRI newInstance;
	public Supply(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Supply"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ISupply> getAllSupplysObjectsCreated(){
		Set<ISupply> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Supply")).subjects().stream()
		.map(mapper->(ISupply)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}