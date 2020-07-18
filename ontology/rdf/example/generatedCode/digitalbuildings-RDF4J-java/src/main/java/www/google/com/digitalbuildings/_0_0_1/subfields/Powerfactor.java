package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Powerfactor 
* Ratio of real and apparent power.
*/
@SuppressWarnings("serial")
public class Powerfactor extends www.google.com.digitalbuildings._0_0_1.subfields.Measurement implements IPowerfactor{

	IRI newInstance;
	public Powerfactor(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Powerfactor"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IPowerfactor> getAllPowerfactorsObjectsCreated(){
		Set<IPowerfactor> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Powerfactor")).subjects().stream()
		.map(mapper->(IPowerfactor)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}