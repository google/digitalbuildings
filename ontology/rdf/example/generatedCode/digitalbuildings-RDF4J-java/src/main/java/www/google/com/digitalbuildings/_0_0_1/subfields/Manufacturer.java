package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Manufacturer 
* The company which produces the asset or device.
*/
@SuppressWarnings("serial")
public class Manufacturer extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IManufacturer{

	IRI newInstance;
	public Manufacturer(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Manufacturer"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IManufacturer> getAllManufacturersObjectsCreated(){
		Set<IManufacturer> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Manufacturer")).subjects().stream()
		.map(mapper->(IManufacturer)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}