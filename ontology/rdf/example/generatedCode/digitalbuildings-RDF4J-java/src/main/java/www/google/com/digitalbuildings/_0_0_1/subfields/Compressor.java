package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Compressor 
* Component which drives refrigerant compression (and thus cooling processes) within a device or system.
*/
@SuppressWarnings("serial")
public class Compressor extends www.google.com.digitalbuildings._0_0_1.subfields.Component implements ICompressor{

	IRI newInstance;
	public Compressor(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Compressor"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ICompressor> getAllCompressorsObjectsCreated(){
		Set<ICompressor> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Compressor")).subjects().stream()
		.map(mapper->(ICompressor)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}