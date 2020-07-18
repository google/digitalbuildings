package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Voc 
* Measures volatile organic component concentration.
*/
@SuppressWarnings("serial")
public class Voc extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IVoc{

	IRI newInstance;
	public Voc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Voc"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IVoc> getAllVocsObjectsCreated(){
		Set<IVoc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Voc")).subjects().stream()
		.map(mapper->(IVoc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}