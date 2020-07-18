package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Device 
* The core equipment being represented by the Field groupings.
*/
@SuppressWarnings("serial")
public class Device extends www.google.com.digitalbuildings._0_0_1.subfields.Component implements IDevice{

	IRI newInstance;
	public Device(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Device"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IDevice> getAllDevicesObjectsCreated(){
		Set<IDevice> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Device")).subjects().stream()
		.map(mapper->(IDevice)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}