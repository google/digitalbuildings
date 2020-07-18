package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Seismic 
* Related to seismic activity (such as seismic gas shutoff valves).
*/
@SuppressWarnings("serial")
public class Seismic extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements ISeismic{

	IRI newInstance;
	public Seismic(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Seismic"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ISeismic> getAllSeismicsObjectsCreated(){
		Set<ISeismic> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Seismic")).subjects().stream()
		.map(mapper->(ISeismic)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}