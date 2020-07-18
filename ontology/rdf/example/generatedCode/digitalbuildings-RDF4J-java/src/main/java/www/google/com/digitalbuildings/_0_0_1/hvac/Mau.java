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
* Class Mau 
* Tag for make-up air units.
*/
@SuppressWarnings("serial")
public class Mau extends www.google.com.digitalbuildings._0_0_1.Equipment implements IMau{

	IRI newInstance;
	public Mau(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Mau"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IMau> getAllMausObjectsCreated(){
		Set<IMau> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Mau")).subjects().stream()
		.map(mapper->(IMau)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}