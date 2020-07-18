package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Condensing 
* Process of gaseous refrigerant changing to liquid.
*/
@SuppressWarnings("serial")
public class Condensing extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements ICondensing{

	IRI newInstance;
	public Condensing(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Condensing"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ICondensing> getAllCondensingsObjectsCreated(){
		Set<ICondensing> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Condensing")).subjects().stream()
		.map(mapper->(ICondensing)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}