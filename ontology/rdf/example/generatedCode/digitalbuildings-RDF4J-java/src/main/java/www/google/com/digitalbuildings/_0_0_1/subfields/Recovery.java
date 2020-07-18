package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Recovery 
* Component or process used for the reclamation of heat.
*/
@SuppressWarnings("serial")
public class Recovery extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IRecovery{

	IRI newInstance;
	public Recovery(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Recovery"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IRecovery> getAllRecoverysObjectsCreated(){
		Set<IRecovery> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Recovery")).subjects().stream()
		.map(mapper->(IRecovery)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}