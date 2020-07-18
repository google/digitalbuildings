package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IEquipment;
import www.google.com.digitalbuildings._0_0_1.Equipment;

/**
* Class Dh 
* Tag for duct heater.
*/
@SuppressWarnings("serial")
public class Dh extends www.google.com.digitalbuildings._0_0_1.Equipment implements IDh{

	IRI newInstance;
	public Dh(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Dh"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IDh> getAllDhsObjectsCreated(){
		Set<IDh> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Dh")).subjects().stream()
		.map(mapper->(IDh)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}