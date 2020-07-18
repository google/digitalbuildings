package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Open 
* Indicates full open (for two-position actuators).  This is the default sense if unspecified
*/
@SuppressWarnings("serial")
public class Open extends www.google.com.digitalbuildings._0_0_1.subfields.Measurement_descriptor implements IOpen{

	IRI newInstance;
	public Open(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Open"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IOpen> getAllOpensObjectsCreated(){
		Set<IOpen> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Open")).subjects().stream()
		.map(mapper->(IOpen)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}