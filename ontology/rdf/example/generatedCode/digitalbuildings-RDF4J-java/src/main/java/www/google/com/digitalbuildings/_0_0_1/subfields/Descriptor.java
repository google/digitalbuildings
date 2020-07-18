package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Descriptor 
*/
@SuppressWarnings("serial")
public class Descriptor extends www.google.com.digitalbuildings._0_0_1.subfields.SubField implements IDescriptor{

	IRI newInstance;
	public Descriptor(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Descriptor"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IDescriptor> getAllDescriptorsObjectsCreated(){
		Set<IDescriptor> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Descriptor")).subjects().stream()
		.map(mapper->(IDescriptor)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}