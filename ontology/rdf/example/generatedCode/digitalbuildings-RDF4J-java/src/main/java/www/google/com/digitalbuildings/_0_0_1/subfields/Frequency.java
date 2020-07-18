package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Frequency 
* The rate of cycling within a process. Typically used to describe voltage (and amperage) oscillation within AC power distribution components.
*/
@SuppressWarnings("serial")
public class Frequency extends www.google.com.digitalbuildings._0_0_1.subfields.Measurement implements IFrequency{

	IRI newInstance;
	public Frequency(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Frequency"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IFrequency> getAllFrequencysObjectsCreated(){
		Set<IFrequency> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Frequency")).subjects().stream()
		.map(mapper->(IFrequency)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}