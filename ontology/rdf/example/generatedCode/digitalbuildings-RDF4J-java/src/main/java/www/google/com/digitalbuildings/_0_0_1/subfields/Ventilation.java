package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Ventilation 
* Process used to provide fresh air into a system or zone. 
*/
@SuppressWarnings("serial")
public class Ventilation extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IVentilation{

	IRI newInstance;
	public Ventilation(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Ventilation"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IVentilation> getAllVentilationsObjectsCreated(){
		Set<IVentilation> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Ventilation")).subjects().stream()
		.map(mapper->(IVentilation)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}