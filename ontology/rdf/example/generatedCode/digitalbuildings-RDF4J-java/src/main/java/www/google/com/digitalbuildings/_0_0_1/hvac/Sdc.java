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
* Class Sdc 
* Tag for automated window shade.
*/
@SuppressWarnings("serial")
public class Sdc extends www.google.com.digitalbuildings._0_0_1.Equipment implements ISdc{

	IRI newInstance;
	public Sdc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Sdc"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ISdc> getAllSdcsObjectsCreated(){
		Set<ISdc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Sdc")).subjects().stream()
		.map(mapper->(ISdc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}